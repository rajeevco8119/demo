import requests
import ast
import json

params = {'user_key':'6367a1d09823a65ea35466cab45fc1d4'}

url = 'https://developers.zomato.com/api/v2.1/'
class Zomato:
    def __init__(self, params):
        self.user_key = params

    def getCategory(self):
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(url+"categories",headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        categories = {}
        for category in a['categories']:
            categories.update({category['categories']['id']: category['categories']['name']})
        return categories

    def get_city_details(self,city_name):
        headers = {'Accept': 'application/json', 'user-key': self.user_key,'q':city_name}
        r = (requests.get(url + "cities?q=" + headers['q'], headers=headers).content)
        return r.decode("utf-8")

    def restaurant_search(self, query="", latitude="", longitude="", cuisines="", limit=5):
        if str(limit).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(
            url + "search?q=" + str(query) + "&count=" + str(limit) + "&lat=" + str(latitude) + "&lon=" + str(
                longitude) + "&cuisines=" + str(cuisines), headers=headers).content).decode("utf-8")
        return r

    def get_cuisines(self, city_ID):
        self.is_valid_city_id(city_ID)
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(url + "cuisines?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        return r

    def get_nearby_restaurants(self, latitude, longitude):
        """
        Takes the latitude and longitude as inputs.
        Returns a dictionary of Restaurant IDs and their corresponding Zomato URLs.
        """
        try:
            float(latitude)
            float(longitude)
        except ValueError:
            raise ValueError('InvalidLatitudeOrLongitude')

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(url + "geocode?lat=" + str(latitude) + "&lon=" + str(longitude),
                          headers=headers).content).decode("utf-8")
        return r

    def is_key_invalid(self, a):

        if 'code' in a:
            if a['code'] == 403:
                raise ValueError('InvalidKey')

    def is_rate_exceeded(self, a):
        if 'code' in a:
            if a['code'] == 440:
                raise Exception('ApiLimitExceeded')


    def is_valid_city_id(self, city_ID):
        city_ID = str(city_ID)
        if city_ID.isnumeric() == False:
            raise ValueError('InvalidCityId')


    def get_restaurant(self, restaurant_ID):
        """
        Takes Restaurant ID as input.
        Returns a dictionary of restaurant details.
        """

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(url + "restaurant?res_id=" + str(restaurant_ID), headers=headers).content).decode(
            "utf-8")

        a = json.loads(r)
        restaurant_details = {}
        restaurant_details.update({"name": a['name']})
        restaurant_details.update({"url": a['url']})
        restaurant_details.update({"location": a['location']['address']})
        restaurant_details.update({"city": a['location']['city']})
        restaurant_details.update({"city_ID": a['location']['city_id']})
        restaurant_details.update({"user_rating": a['user_rating']['aggregate_rating']})
        return restaurant_details

# test data

# object1 = Zomato(params['user_key']).getCategory()
# print(json.dumps(object1,indent=2))

# object2 = Zomato(params['user_key']).get_city_details('New York City')
# json_object = json.loads(object2)
# print(json_object['location_suggestions'][0]['name']+":"+str(json_object['location_suggestions'][0]['id']))

### NYC id = 280, Amritsar id: 22
# city = 'Amritsar'
# object3 = Zomato(params['user_key']).restaurant_search('Amritsar')
# json_object3 = json.loads(object3)
# print(json.dumps(json_object3,indent=2))

# object4 = Zomato(params['user_key']).get_cuisines(json.loads(Zomato(params['user_key']).get_city_details('New York City'))['location_suggestions'][0]['id'])
# json_object3 = json.loads(object4)
# print(json.dumps(json_object3,indent=2))

# latitude = '28.6139'
# longitude = '77.2090'
# object5 = Zomato(params['user_key']).get_nearby_restaurants(latitude,longitude)
# json_object5 = json.loads(object5)
# json.dumps(json_object5,indent=2)
# print(json_object5)

# restaurant_id = '122807'
# object6 = Zomato(params['user_key']).get_restaurant(restaurant_id)
# print(json.dumps(object6,indent=2))