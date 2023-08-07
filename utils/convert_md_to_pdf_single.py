import os
import markdown
import pdfkit

def md_to_pdf(md_file, output_pdf_file):
    try:
        with open(md_file, 'r', encoding='utf-8') as file:
            md_content = file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)

        # Convert HTML to PDF
        pdfkit.from_string(html_content, output_pdf_file)
        
        print(f"Successfully converted '{md_file}' to '{output_pdf_file}'.")
    except Exception as e:
        print(f"Error: {e}")