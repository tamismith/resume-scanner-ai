



#def parse_resume(file_path: str) -> dict:
import os

def detect_file_type(file_path):
    _, ext = os.path.splitext(file_path)  # the '_' means disregard the first part
    ext = ext.lower()  # normalize to lowercase

    if ext == ".pdf":
        return "pdf"
    elif ext == ".docx":
        return "docx"
    else:
        return "unsupported"

        

print(detect_file_type("resume.docx"))   # docx
print(detect_file_type("resume.pdf"))    # pdf
print(detect_file_type("resume.txt"))    # unsupported


