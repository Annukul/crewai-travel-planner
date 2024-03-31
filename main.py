from crewai import Crew

from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

from dotenv import load_dotenv

load_dotenv()


class TripCrew:
    def __init__(self, origin, cities, travel_dates, interests):
        self.origin = origin
        self.cities = cities
        self.travel_dates = travel_dates
        self.interests = interests

    def run(self):
        agents = TravelAgents()
        tasks = TravelTasks()

        export_travel_agent = agents.export_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        plan_itinerary = tasks.plan_itinerary(
            export_travel_agent,
            self.cities,
            self.travel_dates,
            self.interests,
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.travel_dates,
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.interests,
            self.travel_dates,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[export_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    origin = input(dedent("""From where you will you be traveling?"""))
    cities = input(dedent("""What cities are you interested in?"""))
    travel_dates = input(dedent("""What are your travel dates?"""))
    interests = input(dedent("""What are your interests?"""))

    trip_crew = TripCrew(origin, cities, travel_dates, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is your trip plan:")
    print("########################\n")
    print(result)
