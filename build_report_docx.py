from pathlib import Path
import re
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "docs" / "informe-tecnico-primer-ciclo.md"
OUT = ROOT / "docs" / "informe-tecnico-primer-ciclo.docx"

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)

def borders(table):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        e = OxmlElement(f'w:{edge}')
        e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:color'),'D9D9D9')
        tblBorders.append(e)
    tblPr.append(tblBorders)

def add_inline(p, text):
    parts = re.split(r'(\*\*.*?\*\*)', text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            r=p.add_run(part[2:-2]); r.bold=True
        else:
            p.add_run(part)

doc=Document()
sec=doc.sections[0]
sec.page_width=Inches(8.5); sec.page_height=Inches(11)
sec.top_margin=Inches(.72); sec.bottom_margin=Inches(.68); sec.left_margin=Inches(.78); sec.right_margin=Inches(.78)
styles=doc.styles
styles['Normal'].font.name='Aptos'; styles['Normal'].font.size=Pt(10.5)
styles['Normal'].paragraph_format.space_after=Pt(7); styles['Normal'].paragraph_format.line_spacing=1.08
for name,size in [('Title',30),('Subtitle',15),('Heading 1',20),('Heading 2',14),('Heading 3',12)]:
    st=styles[name]; st.font.name='Aptos Display'; st.font.size=Pt(size); st.font.color.rgb=RGBColor(0,0,0); st.font.bold=True
    st.paragraph_format.space_before=Pt(12); st.paragraph_format.space_after=Pt(7)

title=doc.add_paragraph(style='Title'); title.add_run('600 kits para crear')
sub=doc.add_paragraph(style='Subtitle'); sub.add_run('Informe técnico del primer ciclo')
meta=doc.add_paragraph(); meta.alignment=WD_ALIGN_PARAGRAPH.LEFT
add_inline(meta,'Periodo documentado: julio a 14 de noviembre de 2026\nEstado operativo: 600 kits armados y 600 kits entregados\nCoordinación: Creative Commons Venezuela y equipo estudiantil de la Facultad de Ciencias de la UCV')
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
p.add_run().add_picture(str(ROOT/'status-600-delivered-es.png'), width=Inches(4.35))
cap=doc.add_paragraph('Estado final del primer ciclo al 15 de noviembre de 2026')
cap.alignment=WD_ALIGN_PARAGRAPH.CENTER; cap.runs[0].italic=True; cap.runs[0].font.size=Pt(8.5)
doc.add_page_break()

lines=SRC.read_text(encoding='utf-8').splitlines()[5:]
i=0
while i < len(lines):
    line=lines[i].rstrip()
    if not line:
        i+=1; continue
    if line.startswith('## '):
        doc.add_paragraph(line[3:],style='Heading 1'); i+=1; continue
    if line.startswith('### '):
        doc.add_paragraph(line[4:],style='Heading 2'); i+=1; continue
    if line.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].startswith('|'):
            rows.append([c.strip() for c in lines[i].strip('|').split('|')]); i+=1
        if len(rows)>1 and all(set(c)<=set('-: ') for c in rows[1]): rows.pop(1)
        table=doc.add_table(rows=0, cols=len(rows[0])); table.alignment=WD_TABLE_ALIGNMENT.CENTER; table.autofit=True
        for ri,row in enumerate(rows):
            cells=table.add_row().cells
            for ci,val in enumerate(row):
                cells[ci].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
                p=cells[ci].paragraphs[0]; add_inline(p,val)
                if ri==0:
                    shade(cells[ci],'17265A')
                    for run in p.runs: run.font.color.rgb=RGBColor(255,255,255); run.bold=True
                elif ri%2==0: shade(cells[ci],'F2F6FB')
        borders(table)
        doc.add_paragraph()
        continue
    if re.match(r'^\d+\. ',line):
        p=doc.add_paragraph(style='List Number'); add_inline(p,re.sub(r'^\d+\. ','',line)); i+=1; continue
    if line.startswith('- '):
        p=doc.add_paragraph(style='List Bullet'); add_inline(p,line[2:]); i+=1; continue
    para=[line]; i+=1
    while i<len(lines) and lines[i] and not lines[i].startswith(('#','|','- ')) and not re.match(r'^\d+\. ',lines[i]):
        para.append(lines[i].strip()); i+=1
    p=doc.add_paragraph(); add_inline(p,' '.join(para))

doc.add_page_break()
doc.add_paragraph('Cronología visual',style='Heading 1')
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
p.add_run().add_picture(str(ROOT/'chronology-es-v2.png'), width=Inches(4.65))
doc.core_properties.title='600 kits para crear Informe técnico del primer ciclo'
doc.core_properties.subject='Documentación del diseño, producción, armado y entrega de 600 kits educativos'
doc.core_properties.author='Creative Commons Venezuela'
doc.save(OUT)
print(OUT)
