from dotenv import load_dotenv, dotenv_values
load_dotenv()
import os
# from langchain.llms import OpenAI
# llm = OpenAI(openai_api_key="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")

# result = llm.predict("기분이 어때?")

# print(result)

print(os.getenv("OPENAI_API_KEY"))

# from langchain.chat_models import ChatOpenAI
# llm = ChatOpenAI()

# result = llm.predict("저녁 메뉴 추천해줘")

# print(result)