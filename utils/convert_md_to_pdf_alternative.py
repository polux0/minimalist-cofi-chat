from convert_md_to_pdf_single_alternative import convert_md_to_pdf
import os

directory = "./data_cleaned/blogs"
output_directory = "/data_cleaned/blogs_pdf"

os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["DOTNET_SYSTEM_GLOBALIZATION_INVARIANT"] = "1"

file_names_list = os.listdir(directory)
# sanity check
# print(file_names_list)
for file_name in file_names_list:
    if file_name.endswith(".md") and not file_name.endswith(".pdf"):
        input_md_file = os.path.join(directory, file_name)
        # input_md_file is maybe `.md`, so in the output it should be replace to `.pdf`        
        output_final = os.path.join(output_directory, file_name)
        print("\n outputfinal")
        print(output_final)
        # Process the file here
        convert_md_to_pdf(input_md_file, output_final)
    else:
        print("The file is not an '.md' file or it's a PDF file.")
print("!It's finished!")
