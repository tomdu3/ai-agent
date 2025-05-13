from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_tool_calling_agent, AgentExecutor
from temps.base_template import prompt, parser
from utils import search_tool

load_dotenv()

    

llm = ChatOpenAI(model="gpt-40-mini")
llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022")

tools = [search_tool]
agent = create_tool_calling_agent(
    llm2,
    tools=tools,
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    print("Hello from ai-agent!")
    print("-" * 20)
    print()
    query = input("Enter your search query: ")
    print()
    raw_response = agent_executor.invoke({
        "query": query,
    })
    
    try:
        formated_response = parser.parse(raw_response.get("output")[0]["text"])
        print(formated_response)

    except Exception as e:
        print(f"Error parsing response: {e}\nRaw response: {raw_response}")


if __name__ == "__main__":
    main()
