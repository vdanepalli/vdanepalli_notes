import os
import subprocess
import sys

def convert_djvu_to_pdf(djvu_path, pdf_path='output.pdf'):
    
    if not os.path.isfile(djvu_path):
        print(f"Error: The file {djvu_path} does not exist.")
        return

    command = ['ddjvu', '-format=pdf', djvu_path, pdf_path]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted {djvu_path} to {pdf_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 convert_djvu_to_pdf.py <input.djvu> <output.pdf>")
        sys.exit(1)

    input_djvu = sys.argv[1]
    output_pdf = sys.argv[2]

    convert_djvu_to_pdf(input_djvu, output_pdf)