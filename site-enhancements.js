function syncGalleryLink(){
  const link=document.getElementById("gallery-link");
  if(!link)return;
  link.href=document.documentElement.lang==="es"?"gallery.html?lang=es":"gallery.html?lang=en";
}
syncGalleryLink();
document.getElementById("lang")?.addEventListener("click",()=>queueMicrotask(syncGalleryLink));
