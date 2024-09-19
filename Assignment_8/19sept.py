import json
import pymongo

def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)

def get_city_country_mapping():
    """Return a mapping of cities to their respective countries."""
    return {
        "newyork": "usa",
        "dallas": "usa",
        "beijing": "china",
        "colombo": "sri_lanka",
        "hongkong": "china",
        "kandy": "sri_lanka",
        "wuhan": "china",
        "chicago": "usa"
    }

def connect_to_mongo(db_name, collection_name):
    """Establish a connection to the MongoDB database."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    return db[collection_name]

def calculate_total_price(ticket, visa_rates, city_country_mapping):
    """Calculate the total price for a ticket."""
    location = ticket['visa_stamped_location'][-1]
    country = city_country_mapping.get(location)
    if country:
        visa_cost = visa_rates[country]
        return visa_cost + int(ticket['ticket_price'])
    return None

def print_passenger_details(tickets, visa_rates, city_country_mapping):
    """Print the details of each passenger and their total price."""
    print('Passenger Details')
    for ticket in tickets:
        total = calculate_total_price(ticket, visa_rates, city_country_mapping)
        if total is not None:
            print(f"Passenger {ticket['ticket_id']}: Name: {ticket['passenger_name']}, Total Price: {total}")

def main():
    data = load_data("data.json")
    city_country_mapping = get_city_country_mapping()
    tickets_collection = connect_to_mongo("Passenger_Management_System", "tickets")
    
    tickets = list(tickets_collection.find({}))
    print_passenger_details(tickets, data['visa_rates'], city_country_mapping)

if __name__ == "__main__":
    main()
