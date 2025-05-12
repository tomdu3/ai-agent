from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()


llm = ChatOpenAI(model="gpt-40-mini")
llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022")

def main():
    print("Hello from ai-agent!")
    print("-" * 20)
    response = llm2.invoke("What is the first thing you learn in Python?")
    
    print(response)


if __name__ == "__main__":
    main()
