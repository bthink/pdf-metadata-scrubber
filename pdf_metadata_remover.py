import PyPDF2
import sys
from pathlib import Path

def remove_metadata(input_path, output_path=None):
    """
    Remove metadata from a PDF file
    
    Args:
        input_path (str): Path to input PDF file
        output_path (str, optional): Path for output PDF file. If not provided,
                                   will append '_clean' to original filename
    """
    try:
        with open(input_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            pdf_writer = PyPDF2.PdfWriter()
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            pdf_writer.add_metadata({})
            if output_path is None:
                input_file = Path(input_path)
                output_path = input_file.parent / f"{input_file.stem}_clean{input_file.suffix}"
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            print(f"Metadata removed successfully. Cleaned PDF saved as: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_metadata_remover.py <input_pdf_path> [output_pdf_path]")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    remove_metadata(input_path, output_path) 