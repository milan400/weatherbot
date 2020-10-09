import requests, json


def lambda_handler(event, context):
    
    if(event["currentIntent"]["name"]=='TodaysWeather'):

    	entity = event["currentIntent"]["slots"]["location"].title()
    
    	api_key = "place your key here"
    	base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    	city_name = entity
    	
    	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    	response = requests.get(complete_url)
    	x = response.json()
    	weather = x['weather'][0]['description']
    
    	return{
            "sessionAttributes": event['sessionAttributes'],
            "dialogAction":{
                "type":"Close",
                "fulfillmentState": "Fulfilled",
                "message":{
                    "contentType":"PlainText",
                    "content": weather
                }
            }
        }
