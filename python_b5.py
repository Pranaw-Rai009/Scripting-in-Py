import os

messy_folder = [
    "notes.txt",
    "holiday_photo.jpg",
    "invoice_2026.pdf",
    "resume_draft.docx",
    "backup_folder",
    "tax_report.pdf"
]

for file in messy_folder:
    if file.endswith(".pdf"):
        print(f"Moving {file} to PDFs folder")

    if"." in file:
        if not file.endswith(".pdf"):
            print(f"Skipping {file}...")

    if "." not in file:
        print(f"Ignoring directory {file}")
