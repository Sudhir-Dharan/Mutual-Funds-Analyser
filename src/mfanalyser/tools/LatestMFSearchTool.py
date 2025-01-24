from crewai_tools import BaseTool
import json
import google.generativeai as genai
import os

class LatestMFSearchTool(BaseTool):
    name: str = "Latest Mutual Fund Search Tool"
    description: str = (
        "Retrieve latest mutual fund data given a list of mutual fund names. Comma separated"
    )

    def _run(self, query: str) -> str:
        """
        This tool formulates a search query based on the user's input and processes the response.
        Args:
            query (str): The user's search query.
        Returns:
            str: The processed search results.
        """
        print(f"Searching for: {query}")
        print(json.dumps(query, indent=4))

        #fetch api key from env
        api_key = os.getenv("GEMINI_API_KEY")

        # Configure the Gemini API
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        try:
            response = model.generate_content(
                f"Search the web for: latest Available Mutual fund data for the funds ({query}) & provide date of the nav, NAV, expense ratio, 1 year return, 3 years return, 5 years return in a table format."
            )
            return response.text

        except Exception as e:
            print(f"An error occurred: {e}")
            return f"Error: {str(e)}"
