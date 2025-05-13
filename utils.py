from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


# https://python.langchain.com/docs/integrations/tools/ddg/
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search_duckduckgo",
    func=search.run,
    description="Search the web with DuckDuckGo",
)

# https://python.langchain.com/docs/integrations/tools/wikipedia
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=1000,  # characters of the output text
    api_key=None,  # optional API key
)

wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# custom tool
def save_to_txt(text: str, filename: str = "output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    formatted_output = f"--- search output ---\nTimestamp: {timestamp}\n{text}\n"
    print(formatted_output)
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    
    return f"Output Saved to {filename}"

save_to_txt_tool = Tool(
    name="save_to_txt",
    func=save_to_txt,
    description="Save the output to a text file",
)