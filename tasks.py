from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Plan a 7-day travel itinerary
            **Description**: Expand the city guide into a full 7-day travel itinerary with detailed per-day plans, 
                             including weather forcast, where to eat, packing suggestions, and budget breakdown.
                             You MUST suggest actual places to visit, actual hotels to stay, and actual restaurants to eat.
                             This itinerary should cover all aspects of the trip, from arrival to departure, integrating the city guide 
                             information with practical travel logistics.

            **Parameters**: 
			- City: {city}
            - Travel Dates: {travel_dates}
            - Interests: {interests}
            
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify the best city for the trip
            **Description**: Analyze and select the best city for the trip based 
                            on specific criteria such as weather patterns, seasonal
                            events, and travel costs. This task involves comparing
                            multiple cities, considering factors like current weather
                            conditions, upcoming cultural or seasonal events, and
                            overall travel expenses. 
                                                            
                            Make sure you stay inside the country that the user requests.
                            
                            Your final answer must be a detailed
                            report on the chosen city, and everything you found out
                            about it, including the actual flight costs, weather 
                            forecast and attractions.

            **Parameters**: 
			- Origin: {origin}
            - Cities: {cities}
            - Interests: {interests}
            - Travel Dates: {travel_dates}
            
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def gather_city_info(self, agent, city, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
            **Task**: Gather in-depth information about the city
            **Description**: As a local expert on this city you must compile an 
                            in-depth guide for someone traveling there and wanting 
                            to have THE BEST trip ever!
                            Gather information about  key attractions, local customs,
                            special events, and daily activity recommendations.
                            Find the best spots to go to, the kind of place only a
                            local would know.
                            This guide should provide a thorough overview of what 
                            the city has to offer, including hidden gems, cultural
                            hotspots, must-visit landmarks, weather forecasts, and
                            high level costs.
                                                        
                            Make sure you only offer suggestions inside of the country.
                            
                            The final answer must be a comprehensive city guide, 
                            rich in cultural insights and practical tips, 
                            tailored to enhance the travel experience.


            **Parameters**: 
			- City: {city}
            - Interests: {interests}
            - Travel Dates: {travel_dates}
            
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )
