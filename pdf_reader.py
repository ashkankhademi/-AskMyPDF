# pdf_reader.py
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text_chunks = []
    
    for page in doc:
        text = page.get_text().strip()
        if text:
            # Split by single newlines instead of double newlines
            lines = text.split("\n")
            
            buffer = ""
            for line in lines:
                clean_line = line.strip()
                if clean_line:
                    buffer += clean_line + " "
                
                # When we reach 2–3 lines worth of content, save it
                if len(buffer.split()) > 30:  # adjust threshold if needed
                    text_chunks.append(buffer.strip())
                    buffer = ""

            # Append leftover text
            if buffer:
                text_chunks.append(buffer.strip())

    return text_chunks

