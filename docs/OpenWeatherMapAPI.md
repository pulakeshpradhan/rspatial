```python
import requests

params = {
    "lat":28.62,
    "lon":77.2,
    "appid":"26ea0a994f700ae86a2e74cf1a39b5ce",
    "units":"metric"
    
}
#url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
url = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(url,params=params)
response
```




    <Response [200]>




```python
data = response.json()
data
```




    {'coord': {'lon': 77.2, 'lat': 28.62},
     'weather': [{'id': 721,
       'main': 'Haze',
       'description': 'haze',
       'icon': '50d'}],
     'base': 'stations',
     'main': {'temp': 30.03,
      'feels_like': 29.4,
      'temp_min': 30.03,
      'temp_max': 30.03,
      'pressure': 1011,
      'humidity': 37,
      'sea_level': 1011,
      'grnd_level': 985},
     'visibility': 3500,
     'wind': {'speed': 2.06, 'deg': 240},
     'clouds': {'all': 20},
     'dt': 1760510172,
     'sys': {'type': 1,
      'id': 9165,
      'country': 'IN',
      'sunrise': 1760489503,
      'sunset': 1760530918},
     'timezone': 19800,
     'id': 1260877,
     'name': 'Parliament House, Delhi',
     'cod': 200}




```python
from datetime import datetime, timedelta

timezone_offset = data['timezone']
localtime = datetime.utcfromtimestamp(data['dt'])+timedelta(seconds=timezone_offset)
date_str = localtime.strftime("%Y-%m-%d")
time_str = localtime.strftime("%H:%M:%S")

print ("Date: ", date_str)
print ("Time: ", time_str)
print ("Location: ", data["name"])
print ("Temperaure: ", data["main"]["temp"])
```

    Date:  2025-10-15
    Time:  12:06:12
    Location:  Parliament House, Delhi
    Temperaure:  30.03
    

    C:\Users\sukan\AppData\Local\Temp\ipykernel_30060\3680212285.py:4: DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
      localtime = datetime.utcfromtimestamp(data['dt'])+timedelta(seconds=timezone_offset)
    


```python

```


<iframe width="560" height="315" src="https://www.youtube.com/embed/njfa48cIM9c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


<iframe width="560" height="315" src="https://www.youtube.com/embed/njfa48cIM9c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
