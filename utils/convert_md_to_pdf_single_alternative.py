# This code example demonstrates how to convert a Markdown file to a particular PDF standard.
import aspose.words as aw
import os

def convert_md_to_pdf(input_file, output_file):
    os.environ["PYTHONIOENCODING"] = "utf-8"
    os.environ["DOTNET_SYSTEM_GLOBALIZATION_INVARIANT"] = "1"

    # Load an existing Markdown document
    doc = aw.Document(input_file)

    # Specify save options and set PDF compliance
    saveOptions = aw.saving.PdfSaveOptions()
    saveOptions.compliance = aw.saving.PdfCompliance.PDF17

    # Save the document as PDF
    doc.save(output_file)
    print('saved the document', output_file)