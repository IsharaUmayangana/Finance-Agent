from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

load_dotenv()

def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [get_company_symbol, YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data", "Use the `get_company_symbol` tool to find the symbol for a company before using YFinanceTools.",
    "If the company is not in the `get_company_symbol` tool, use 'Unknown' as the symbol."],
    debug_mode=True
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for TESLA and Phidata")