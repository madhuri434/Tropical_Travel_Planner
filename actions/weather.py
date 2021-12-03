import requests

def Weather(city):
      api_address='http://api.openweathermap.org/data/2.5/weather?appid=6b4bdb97208d713ee0e88855b8c12fe0&q='
      # city = input('Enter the City Name : ')
      url = api_address + city
      json_data = requests.get(url).json()
      format_add = json_data['main']
      print(format_add)
      print("Weather is {0} Temperature is minimum {1} celcius and maximum is {2} celcius".format(json_data['weather'][0]['main'],int(format_add['temp_min']-273), int(format_add['temp_max']-272)))
      return format_add