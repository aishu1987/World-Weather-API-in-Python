import requests, json, pandas


#wdir='D:\Jupyter_Notebooks'
# Enter your API key here 
api_key = open("D:\Jupyter_Notebooks\weather_data\config\key.txt",'r').read()
# base_url variable to store url 
base_url = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx"
# Give city name 
#zipcode = "35810"
#Give format
formattype = "json"
#Give startdate
#startdate = "2019-01-01"
#Give enddate
#enddate = "2019-02-06"
#Give interval parameter
tp = "3"

# reading the date range data
df = pandas.read_csv("D:\Jupyter_Notebooks\weather_data\config\dates.csv")

#reading the zipcode file
zipcode = pandas.read_csv("D:\Jupyter_Notebooks\weather_data\config\zipcodes.csv")

#print(zipcode)
#for i in zipcodes:
#    print(i)
   
for a in range(len(zipcode.index)):
    z = str(zipcode.zipcodes.iloc[a])
    print(z)
    myfile = open("D:\Jupyter_Notebooks\weather_data\out\complete_url_list_{}.txt".format(z),'w')
    for i in range(len(df.index)):
        startdate = str(df.startdate.iloc[i])
        enddate = str(df.enddate.iloc[i])
        complete_url = base_url + "?key=" + api_key + "&q=" + z + "&format=" + formattype + "&date=" +\
                       startdate + "&enddate=" + enddate + "&tp=" + tp
        myfile.writelines(complete_url+"\n")
    #print(complete_url)
    myfile.close()
    
    
    
    url_list = open("D:\Jupyter_Notebooks\weather_data\out\complete_url_list_{}.txt".format(z),'r')
    lines = url_list.readlines()
    print(lines[1:3])
    
    x = []
    outfile = open('D:\Jupyter_Notebooks\weather_data\data\{}.json'.format(z), 'w')
    for j in lines :
        response= requests.get(j)
        x.append(response.json())
        #json.dump(x, outfile, indent = 2, sort_keys= True)
    json.dump(x,outfile)
    outfile.close()