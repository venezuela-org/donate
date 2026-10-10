# Gallery and delivery evidence model

This document defines the data required for the public gallery and the separate private project ledger. The public repository must contain only approved, non-identifying information.

## 1. Public gallery record

Stored in `drawings.json` after review and approval.

| Field | Required | Example | Publication rule |
|---|---:|---|---|
| `id` | yes | `drawing-0060` | New public ID; never reuse the QR token. |
| `title.es` / `title.en` | yes | `El árbol feliz` | Editorial title or title supplied with permission. |
| `image` | yes for production | `drawings/drawing-0060.webp` | Metadata removed; no faces or identifiers visible. |
| `thumbnail` | recommended | `drawings/thumbs/drawing-0060.webp` | Optimised WebP or AVIF. |
| `ageGroup` | yes | `6–8` | Age range only; never exact birth date. |
| `location` | optional | `Caracas` | City or state only, never an address or school. |
| `theme` | yes | `nature` | Controlled value: `nature`, `community`, `future`, `free`. |
| `published` | yes | `true` | Must remain `false` until review is complete. |
| `featured` | optional | `false` | Editorial status. |
| `winner` | optional | `false` | Set only after jury decision. |

The public file must not contain names, email addresses, phone numbers, schools, delivery addresses, QR identifiers, consent documents or internal evidence references.

## 2. Private drawing ledger

Keep outside the public GitHub repository in an access-controlled spreadsheet or database.

| Field | Example / placeholder |
|---|---|
| Internal drawing ID | `[DRAWING_INTERNAL_ID]` |
| Public gallery ID | `[PUBLIC_ID or NOT_PUBLISHED]` |
| Original QR token | `[QR_TOKEN]` |
| Submission timestamp and timezone | `[YYYY-MM-DD HH:MM America/Caracas]` |
| Original file checksum | `[SHA-256]` |
| Original file location | `[PRIVATE_STORAGE_REFERENCE]` |
| Adult contact | `[PRIVATE_EMAIL_OR_PHONE]` |
| Contact supplied voluntarily | `[YES/NO]` |
| Permission to publish drawing | `[YES/NO/UNCLEAR]` |
| Permission scope | `[WEBSITE/SOCIAL/EXHIBITION/REPORT]` |
| Consent evidence reference | `[MESSAGE_OR_FORM_REFERENCE]` |
| Review status | `[PENDING/APPROVED/REJECTED]` |
| Reviewer and review time | `[TEAM_MEMBER]`, `[TIMESTAMP]` |
| Redaction required | `[YES/NO + DETAILS]` |
| Metadata removed | `[YES/NO + TOOL/TIMESTAMP]` |
| Published file checksum | `[SHA-256]` |
| Notes | `[INTERNAL_NOTES]` |

## 3. Private delivery ledger

One record per delivery event. Addresses and direct contacts remain private.

| Field | Example / placeholder |
|---|---|
| Delivery ID | `[DELIVERY-YYYY-NNN]` |
| Organisation | `[ORGANISATION]` |
| Public location | `[CITY/STATE]` |
| Exact private address | `[FULL_ADDRESS]` |
| Delivery date | `[YYYY-MM-DD]` |
| Start / end time and timezone | `[HH:MM–HH:MM America/Caracas]` |
| Kits planned / delivered | `[N] / [N]` |
| Remaining stock after event | `[N]` |
| Approximate age groups | `[4–5, 6–8, 9–12, 13+]` |
| Organisation contact | `[NAME/ROLE/PHONE/EMAIL]` |
| UCV team members present | `[NAMES OR INTERNAL IDS]` |
| Handover evidence | `[SIGNED RECEIPT / MESSAGE / PHOTO REFERENCES]` |
| Photo/video count | `[N]` |
| Privacy review completed | `[YES/NO]` |
| Faces or identifiers visible | `[NO / REDACTION REQUIRED]` |
| Incident or discrepancy | `[NONE / DETAILS]` |
| Recorded by / verified by | `[TWO PEOPLE WHEN POSSIBLE]` |

## 4. Reconciliation rules

At every update, verify:

1. `kits assembled = kits delivered + kits physically remaining`.
2. Sum of delivery-event quantities equals the public delivered total.
3. Every published drawing has an approved private consent record.
4. Every image has a stored original checksum and a separate published-file checksum.
5. Public location granularity cannot identify a child or household.
6. No direct contact or exact address is committed to the repository.
7. Dates always include the source timezone; public dates may be simplified only after reconciliation.

## 5. Evidence still to be collected from Reinaldo and the team

- `[DELIVERY_LIST_WITH_DATES_AND_QUANTITIES]`
- `[EXACT_PRIVATE_ADDRESSES]`
- `[ORGANISATION_AND_RESPONSIBLE_CONTACT_PER_DELIVERY]`
- `[START_AND_END_TIMES]`
- `[HANDOVER_CONFIRMATION_REFERENCE]`
- `[PHOTO_AND_VIDEO_INVENTORY]`
- `[PRIVACY_REVIEW_STATUS]`
- `[CURRENT_PHYSICAL_STOCK_COUNT]`
- `[DRAWING_SUBMISSION_EXPORT]`
- `[PUBLICATION_CONSENT_STATUS_PER_DRAWING]`
- `[EXPENSE_AND_TRANSPORT_REFERENCES]`

These placeholders are intentionally not exposed on the public gallery.
