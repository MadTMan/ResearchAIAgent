from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name = "search",
    func=search.run,
    description="Use search to find information on the web. Input should be a search query.",
    
)

api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=2000)
wikipedia_tool = WikipediaQueryRun(
    name="wikipedia",
    api_wrapper=api_wrapper,
    description="Use this tool to answer questions or find detials and information about a topic using Wikipedia.",
)