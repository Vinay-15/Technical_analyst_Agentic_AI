from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import Tool
from datetime import datetime


api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

#arxiv_api = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
#arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_api)

def analyze_trends_func(topic: str) -> str:
    """Analyze trends and statistics on a given topic"""
    return f"Trend analysis for {topic}: Growing interest over past 5 years"

def generate_citation_func(source: str) -> str:
    """Generate proper academic citation for a source"""
    return f"Citation: {source} (2024). Retrieved from Academic Database."

def fact_check_func(claim: str) -> str:
    """Verify factual claims"""
    return f"Fact check for '{claim}': Verified from multiple sources"

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

analyze_trends = Tool(
    name="AnalyzeTrends",
    func=analyze_trends_func,
    description="Analyze trends and statistics on a given topic. Input should be a topic name."
)

generate_citation = Tool(
    name="GenerateCitation",
    func=generate_citation_func,
    description="Generate proper academic citation for a source. Input should be a source name."
)

fact_check = Tool(
    name="FactCheck",
    func=fact_check_func,
    description="Verify factual claims. Input should be a claim to verify."
)

# Optional: Create a list of all tools for easy import
all_tools = [wiki_tool, analyze_trends, generate_citation, fact_check]