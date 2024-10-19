import requests

print("--------Welcome to Anveshi's weather checker--------")

city_name = input("Enter city name : ")
API_key = "fd7d60de38b0abf266d0fc8be7886f39"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code==200 : 
    data = response.json()
    print('weather is' ,data ['weather'][0]['description'])
    print('current temperature is ' ,data ['main']['temp'])
    print('current temperature feels like' ,data ['main']['feels_like'])
    print('Humidity is ' ,data ['main']['humidity'])



    