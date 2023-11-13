import pprint

# Sample dictionary
person_data = {
    'name': 'John Doe',
    'address': '123 Main St, City1, City2',
    'date_of_birth': '1990-05-15'
}

# New values to concatenate with the 'address' key
city2 = 'City2Updated'
city1 = 'City1Updated'

# Using an f-string to concatenate the 'address' key with new values
person_data['address'] = f"{person_data['address']}, {city2}, {city1}"

pprint.pprint(person_data)
