from convert_md_to_pdf_single import md_to_pdf
import os

directory = "./data/blogs"
output_directory = "../data/blogs_pdf"

file_names_list = os.listdir(directory)
# sanity check
# print(file_names_list)
for file_name in file_names_list:
    if file_name.endswith(".md") and not file_name.endswith(".pdf"):
        input_md_file = os.path.join(directory, file_name)
        print("\n file:")
        print(input_md_file)
        # input_md_file is maybe `.md`, so in the output it should be replace to `.pdf`        
        output_final = os.path.join(output_directory, input_md_file)
        md_to_pdf(input_md_file, output_final)
        # Process the input_md_file here
    else:
        print("The file is not an '.md' file or it's a PDF file.")

