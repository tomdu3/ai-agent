from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_tool_calling_agent, AgentExecutor
from temps.base_template import prompt, parser

load_dotenv()

    

llm = ChatOpenAI(model="gpt-40-mini")
llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022")

agent = create_tool_calling_agent(
    llm2,
    tools=[],
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)

def main():
    print("Hello from ai-agent!")
    print("-" * 20)
    
    raw_response = agent_executor.invoke({
        "query": "What is the best way to learn Python?"
    })
    
    print(raw_response)
    formated_response = parser.parse(raw_response.get("output")[0]["text"])
    print(formated_response)


if __name__ == "__main__":
    main()
