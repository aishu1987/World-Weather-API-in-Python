# World-Weather-API-in-Python
World weather API in python to pull historical data
Past/Historical Weather API
Get worldwide city and town past/historical weather by US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) and city name

Parameter Value Type  Location  Description
extra string  query (Optional)  It allows to request some additional information in the feed return. Possible values are localObsTime, isDayTime, utcDateTime. Two or more values can be passed as comma separated.
date	
2019-03-01
string	query	(Optional) Get weather for a particular date within next 15 day. It supports today, tomorrow and a date in future. The date should be in the yyyy-MM-dd format. E.g:- date=today or date=tomorrow or date=2013-04-21
enddate	
2019-03-31
string	query	(Optional) If you wish to get weather data between two dates, then you need to provide with 'enddate' parameter as well. The date should be in the yyyy-MM-dd format. Example:- 20th July, 2009 then the date will be formatted as 2009-07-20.
includelocation	
string	query	(Optional) Returns the nearest weather point for which the weather data is returned for a given postcode, zipcode and lat/lon values. The possible values are yes or no. By default it is no. E.g:- includeLocation=yes or includeLocation=no
show_comments	
string	query	(Optional) Disables CSV/TAB comments from the output. The possible values are yes or no. By default it is yes. E.g:- show_comments=yes or show_comments=no
tp	
24
string	query	(Optional) Switch between weather forecast time interval from 1 hourly, 3 hourly, 6 hourly, 12 hourly (day/night) or 24 hourly (day average). E.g:- tp=24 or tp=12 or tp=6 or tp=3 or tp=1
callback	
string	query	(Optional) Only to be used for json callback feature. E.g:- callback=function_name
lang	
string	query	(Optional) Returns weather description text in the language of your choice. E.g:- lang=ar (Arabic). Visit Multilingual support page for more information: http://www.worldweatheronline.com/weather-api-multilingual.aspx
