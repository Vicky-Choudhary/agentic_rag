from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DataPreproccesor:

    def get_file_content(file_path):
        
        '''
        Get file path and return content of the file 

        '''
        loader = PyPDFLoader(file_path)
        document = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 100
        )
        texts = text_splitter.split_documents(document)
        return texts