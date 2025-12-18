from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
# from tavily import TavilyClient

load_dotenv()
# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that search over internet
#     Args:
#      query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching form {query}")
#     return tavily.search(query=query)

llm = ChatOpenAI(
        temperature=0,
        model="openai/gpt-oss-20b",
        base_url="http://192.168.1.190:1234/v1"
    )
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()
