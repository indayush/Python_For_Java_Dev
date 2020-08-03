# JSON full form - JavaScript Object Notation

import urllib.request
import json

urlForJSONData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
objURL = urllib.request.urlopen(urlForJSONData)
responseCode = objURL.getcode()
print(responseCode)

# Reading the URL JSON Data
jsonRawData = objURL.read()
print("Raw Json Data Fetched.")
# print(jsonRawData)

def parseRawJsonData(jsonRawData):
    print()
    pyObjForJson = json.loads(jsonRawData)
    # print(pyObjForJson)

    # Accessiong Data in Json based on Format of data in it.
    # Get 'title' from the 'metadata' section of the Json data
    
    # Title - 
    if "title" in pyObjForJson["metadata"]:
        print (pyObjForJson["metadata"]["title"])
        '''
        USGS Magnitude 2.5+ Earthquakes, Past Day
        '''

    # Number of events -
    count = pyObjForJson["metadata"]["count"]
    print (str(count) + " events recorded")
    '''
    45 events recorded
    '''

    # for each event, print the place where it occurred
    # Features is an array of places where the Earthquakes occurred.(45 at this time)
    # Get 'place' from the 'properties' section in 'Features' array of the Json data
    for i in pyObjForJson["features"]:
        print (i["properties"]["place"])
        print ("--------------\n")
        
    '''
            230 km SSW of Ambon, Indonesia
            --------------

            Southwest Indian Ridge
            --------------

            8km NE of Alum Rock, CA
            --------------

            108 km SSE of Perryville, Alaska
            --------------

            11 km NW of Clarks Point, Alaska
            --------------

            53 km NNE of Iquique, Chile
            --------------

            31 km SE of Mina, Nevada
            --------------

            15 km SSE of Guánica, Puerto Rico
            --------------

            20 km SSE of Guánica, Puerto Rico
            --------------

            141 km SSW of Kokopo, Papua New Guinea
            --------------

            206 km WSW of Kavieng, Papua New Guinea
            --------------

            40 km SSE of Nikolai, Alaska
            --------------

            45 km NNE of McGrath, Alaska
            --------------

            36 km NNW of Nikolai, Alaska
            --------------

            78 km W of Ovalle, Chile
            --------------

            82 km SSW of Sand Point, Alaska
            --------------

            southern East Pacific Rise
            --------------

            northern Mid-Atlantic Ridge
            --------------

            126 km N of Calama, Chile
            --------------

            88 km SW of Pagar Alam, Indonesia
            --------------

            Vanuatu region
            --------------

            60 km NNW of Petersville, Alaska
            --------------

            159 km WSW of San Antonio de los Cobres, Argentina
            --------------

            34 km NW of Güiria, Venezuela
            --------------

            116 km ENE of Kashgar, China
            --------------

            57 km ESE of Sand Point, Alaska
            --------------

            Mariana Islands region
            --------------

            95 km ESE of Sand Point, Alaska
            --------------

            28 km WSW of Ambunti, Papua New Guinea
            --------------

            10 km NNE of Odessa, Texas
            --------------

            9 km SSE of Tallaboa, Puerto Rico
            --------------

            8 km ENE of Pāhala, Hawaii
            --------------

            211 km SSW of ‘Ohonua, Tonga
            --------------

            30km SE of Bodie, CA
            --------------

            198 km SE of Lorengau, Papua New Guinea
            --------------

            216 km SE of Lorengau, Papua New Guinea
            --------------

            204 km SE of Lorengau, Papua New Guinea
            --------------

            31km SE of Bodie, CA
            --------------

            southeast Indian Ridge
            --------------

            39 km NW of Stanley, Idaho
            --------------

            10 km WSW of Polloc, Philippines
            --------------

            western Texas
            --------------

            65 km W of Tobelo, Indonesia
            --------------

            53 km SSE of Sand Point, Alaska
            --------------

            12 km SSE of Maria Antonia, Puerto Rico
            --------------
    '''

    # Fetching data with some filters via logic
    # print the events that only have a magnitude greater than 4
    # Get 'mag' from the 'properties' section in 'Features' array of the Json data & check if value greater than/equal to 4.0
    for i in pyObjForJson["features"]:
        if i["properties"]["mag"] >= 4.0:
            print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])  # %2.1f gives 11.2 format data. 
            print ("--------------")                                            # i.e. - 2 integers & one decimal value

        '''
            4.2 230 km SSW of Ambon, Indonesia
            --------------
            4.8 Southwest Indian Ridge
            --------------
            4.7 141 km SSW of Kokopo, Papua New Guinea
            --------------
            5.8 206 km WSW of Kavieng, Papua New Guinea
            --------------
            4.1 78 km W of Ovalle, Chile
            --------------
            4.7 southern East Pacific Rise
            --------------
            4.6 northern Mid-Atlantic Ridge
            --------------
            4.4 126 km N of Calama, Chile
            --------------
            4.9 88 km SW of Pagar Alam, Indonesia
            --------------
            5.7 Vanuatu region
            --------------
            4.4 159 km WSW of San Antonio de los Cobres, Argentina
            --------------
            5.0 34 km NW of Güiria, Venezuela
            --------------
            4.6 116 km ENE of Kashgar, China
            --------------
            4.4 Mariana Islands region
            --------------
            4.2 28 km WSW of Ambunti, Papua New Guinea
            --------------
            4.2 8 km ENE of Pāhala, Hawaii
            --------------
            5.6 211 km SSW of ‘Ohonua, Tonga
            --------------
            6.0 198 km SE of Lorengau, Papua New Guinea
            --------------
            4.6 216 km SE of Lorengau, Papua New Guinea
            --------------
            5.7 204 km SE of Lorengau, Papua New Guinea
            --------------
            4.8 southeast Indian Ridge
            --------------
            6.4 10 km WSW of Polloc, Philippines
            --------------
            4.4 65 km W of Tobelo, Indonesia
            --------------
        '''    
    

# Parsing JSON Data for Python - 
if responseCode == 200:
    print("Site Accessed. Parsing JSON Data - ")
    parseRawJsonData(jsonRawData)
else:
    print("Site Accessing failed. Response COde - " + str(responseCode))
