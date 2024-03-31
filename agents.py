from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools


class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")

    def export_travel_agent(self):
        return Agent(
            role="Expert travel agent",
            backstory=dedent(
                f"""Expert in travel planning with over 10 years of experience in the travel industry"""
            ),
            goal=dedent(
                f"""Create a 7-day itinerary with detailed per-day lans, including budget, packing suggestions, and safety tips """
            ),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City selection expert",
            backstory=dedent(
                f"""Expert at analyzing travel data and trends to recommend the best cities for travellers"""
            ),
            goal=dedent(
                f"""Select the best cities based on weather, season, prices, and traveller interests"""
            ),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local tour guide",
            backstory=dedent(
                f"""Knowledgeable local tour guide with extensive information about the city, it's history, culture, and attractions"""
            ),
            goal=dedent(f"""Provide the BEST nsights about the selected city"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
