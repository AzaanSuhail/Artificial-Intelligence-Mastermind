from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])

# Read this : https://docs.langchain.com/oss/python/integrations/document_loaders#pdfs