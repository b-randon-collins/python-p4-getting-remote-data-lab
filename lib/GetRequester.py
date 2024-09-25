import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):

        response = requests.get(self.url)
        return response.content

    def load_json(self):
        
        response = self.get_response_body()
        return json.loads(response)


get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
#=> [{"name"=>"Daniel", "occupation"=>"LG Fridge Salesman"}, {"name"=>"Joe", "occupation"=>"WiFi Fixer"}, {"name"=>"Avi", "occupation"=>"DJ"}, {"name"=>"Howard", "occupation"=>"Mountain Legend"}]
print(get_requester.load_json())
