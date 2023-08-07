# imports
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import os
from collect_documents import collect_documents_from_directory
from collect_documents_upgraded import collect_documents_from_directory_upgraded
load_dotenv()

DATA_DIRECTORY = os.getenv("DATA_DIRECTORY")

# working version, expect we created embedding that has bigger chunk size > 500
# text_splitter = CharacterTextSplitter(chunk_size = 1500, separator = "\n")
# experimental version, added more separators
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separators=[" ", ",", "\n"])
# working version
documents = collect_documents_from_directory(DATA_DIRECTORY)
# experimenting with upgraded version ( includes .md files)
#documents = collect_documents_from_directory_upgraded(DATA_DIRECTORY)
chunks = text_splitter.split_documents(documents)

# initialize embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# index the vector database by embedding then inserting document chunks
embeddings_output_directory=f"./{DATA_DIRECTORY}_embeddings"

db = Chroma.from_documents(chunks, embedding_function,
                        #metadatas=[{"source": f"{i}-ssingle-test"} for i in range(len(chunks))],
                        persist_directory = embeddings_output_directory)
db.persist()