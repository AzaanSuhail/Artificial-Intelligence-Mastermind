from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)

#& temperature does not directly means randomness or correctiveness of the output

#* It means when you set the temperature near about 0 then the output will remains same for every time same input  and when you set the temperature near about 1 then the output will be more random for same input