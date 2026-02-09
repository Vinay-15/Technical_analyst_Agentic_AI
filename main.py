from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
import json
from tools import wiki_tool, analyze_trends, generate_citation, fact_check, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


parser = PydanticOutputParser(pydantic_object=ResearchResponse)
prompt = ChatPromptTemplate.from_messages([
    ("system", '''You are a research assistant that provides a detailed information on a given topic.
     Available tools:
    - Wikipedia: Search Wikipedia for information
     **Instructions:**
    1. first check if it exists in Wikipedia then provide the response, check evrything in wikipedia firste
    3. ALWAYS provide a final answer in this exact JSON format, even if tools fail:
{format_instructions}'''),
    ("placeholder", "{chat_history}"),
    ("user", "{query}"),
    ("placeholder", "{agent_scratchpad}"),]).partial(format_instructions=parser.get_format_instructions())



tool = [wiki_tool, analyze_trends, generate_citation, fact_check, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tool)

executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tool, verbose=True, max_iterations=3, handle_parsing_errors=True,return_intermediate_steps=True)
query = input("What can I help you Research? ")
response = executor.invoke({"query": query})
print(response["output"])


try:
    output_dict = json.loads(response["output"])
    print(f"\nTopic: {output_dict['topic']}")
    print(f"\nSummary: {output_dict['summary']}")
    print(f"\nSources: {output_dict['sources']}")
    print(f"\nTools Used: {output_dict['tools_used']}")
    
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
    print(f"Raw output: {response['output']}")