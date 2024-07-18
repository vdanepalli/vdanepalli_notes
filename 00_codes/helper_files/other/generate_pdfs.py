# python -m venv my_env
# source my_env/bin/activate
# pip install markdown2 pdfkit
# brew install --cask wkhtmltopdf


import os
import markdown2
import pdfkit

def convert_md_to_pdf(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Walk through the input directory
    for root, dirs, files in os.walk(input_dir):
        # Create corresponding directory structure in the output directory
        relative_path = os.path.relpath(root, input_dir)
        output_path = os.path.join(output_dir, relative_path)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        for file in files:
            if file.endswith('.md'):
                md_file_path = os.path.join(root, file)
                html_file_path = os.path.join(output_path, file[:-3] + '.html')
                pdf_file_path = os.path.join(output_path, file[:-3] + '.pdf')
                
                # Read the markdown file
                with open(md_file_path, 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()
                    
                # Convert markdown to HTML
                html_content = markdown2.markdown(md_content)
                
                # Write the HTML to a temporary file
                with open(html_file_path, 'w', encoding='utf-8') as html_file:
                    html_file.write(html_content)
                    
                # Convert HTML to PDF
                pdfkit.from_file(html_file_path, pdf_file_path)
                
                # Remove the temporary HTML file
                os.remove(html_file_path)

# Example usage
input_directory = '/Users/vd/Desktop/Github/vdanepalli_notes'
output_directory = '/Users/vd/Desktop/Github/vdanepalli_notes/generated_content'
convert_md_to_pdf(input_directory, output_directory)