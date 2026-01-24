from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load() #* this will take lot of time consuming to load all the pdf simultaneously
docs = loader.lazy_load() #& refer notes

for document in docs:
    print(document.metadata)