from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
import os
def collect_documents_from_directory_upgraded(directory: str):
    file_names_list = os.listdir(directory)
    documents = []
    for file_name in file_names_list:
        print(file_name)
        file_path = os.path.join(directory,
                            file_name)
        documents = []
        if file_name.endswith(".md"):
            loader = PyPDFLoader(file_path)
            document = loader.load()
        elif file_name.endswith(".pdf"):
            loader = UnstructuredMarkdownLoader(file_path)
            document = loader.load()
        else:
            print(f"The file '{file_name}' is neither an '.md' file nor a '.pdf' file.")
        documents += document

    return documents
