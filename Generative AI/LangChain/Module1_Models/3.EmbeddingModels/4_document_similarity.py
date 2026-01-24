from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]  #LEARN Cosine Similarity needs 2 paramaters in the 2-D list form

print(enumerate(scores),key=lambda x:x[1])  #~ Enumerate will mark index with value after sorting also the index attached will remains same & we are sorting the on the basis of second index value 

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]   #*we need the highest score
& the highest value is at the last (sorted ascendingly) so we have used [-1] to extract 
 
print(query)
print(documents[index])
print("similarity score is:", score)




