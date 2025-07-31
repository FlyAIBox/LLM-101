import os
from langchain.tools import tool
from serpapi import search
from typing import List
from dotenv import load_dotenv

load_dotenv()

def get_hotel_details(dictionary):
    name = dictionary['name']
    rate = dictionary['rate_per_night'] if 'rate_per_night' in dictionary else 'NA'
    overall_rating = dictionary['overall_rating'] if 'overall_rating' in dictionary else 'NA'
    return {'property_name' : name, 'rate_per_night': rate, 'rating' : overall_rating}

def get_flight_details(dictionary):
    airlines = [flight['airline'] for flight in dictionary['flights']]
    layover_stations = dictionary['layovers'] if 'layovers' in dictionary.keys() else 'NA'
    total_duration = dictionary['total_duration'] 
    price = dictionary['price'] if 'price' in dictionary.keys() else 'Not Provided'
    return {'airlines': airlines,
            'layover': layover_stations,
            'Duration': total_duration,
            'price': price}

@tool('hotel-search')
def hotel_search(place : str, 
                 check_in_date : str, 
                 check_out_date : str, 
                 country_location :str, 
                 number_of_adults : int,
                 number_of_children : int = 0,
                 children_ages : List[int] = None,
                 property_types : int = None,
                 min_price : int = None,
                 max_price : int = None):
    
    '''
    Searches for hotels at the destination location. Use first two letter for country location eg., in, uk, us
    Returns: It returns a dict containing the following -
             place: Location of the properties, property_name : Name of the property, rate : rate per night in INR, rating : overall rating by the customers
    '''
    params = {
        "engine": "google_hotels",
        "q": place,
        "check_in_date": check_in_date,
        "check_out_date":check_out_date,
        "adults": number_of_adults,
        "children": number_of_children,
        "children_ages" : children_ages,
        "property_types" : property_types,
        "currency": "INR",
        "gl": country_location,
        "hl": "en",
        "max_price" : max_price,
        "min_price" : min_price,
        "api_key": os.getenv('SERP_API_KEY')
    }

    results = search(params)
    return_dict = list(map(get_hotel_details, results['properties']))[:4]
    return {'place' : place, 'hotel_details': return_dict}


@tool('flight-search')
def flight_search(
        departure_id: str,
        arrival_id: str,
        outbound_date: str,
        return_date: str = None,
        currency: str = "INR",
    ):
    
    '''
    Searches for flights based on the provided criteria using a flight search engine. Provide IATA ids for the locations.
    Returns:
        dict: A dictionary containing the search results from the flight search engine. 
              airlines : List of airlines at each point departure to layovers to arrival 
              layover : list of layovers, NA if direct flight
              Duration : Total duration in minutes
              price : price in INR
    '''
    params = {
    "engine": "google_flights",
    "departure_id": departure_id,
    "arrival_id": arrival_id,
    "outbound_date": outbound_date,
    "return_date": return_date,
    "currency": currency,
    "hl": "en",
    "type": 2 if return_date == None else 1,
    "api_key": os.getenv('SERP_API_KEY')
    }

    results = search(params)
    return_dict = list(map(get_flight_details, dict(results)['other_flights']))
    return {'Departure': departure_id, 'Arrival':arrival_id, 'flight_details':return_dict}

@tool("final_answer")
def final_answer(
    answer: str
):
    """Returns a natural language response to the user in `answer`, and a
    `source` which provides citations for where this information came from.
    """
    return ""

tools = [hotel_search, flight_search, final_answer]