from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

# Add this after load_dotenv()
import os
print("ANTHROPIC_API_KEY:", os.getenv("ANTHROPIC_API_KEY"))

# llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

llm = ChatAnthropic(model="claude-opus-4-20250514", temperature=0.0)
response = llm.invoke("What is the meaning of life?")
print(response)