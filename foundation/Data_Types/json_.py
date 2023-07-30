

chopin_json = ' { "name":"Frederic Chopin" , "age":39 } '

#The JSON module
import json

#Parse a json string into a python dictionary using the method
chopin = json.loads(chopin_json)

print(chopin["name"])

#Convert a python object to a JSON string by
liszt = {
    "name": "Franz Liszt",
    "age": 74
}

#Can customise this JSON object with further params in the dumps method
liszt_json = json.dumps(liszt)

print(liszt_json)

#List of Valid Python Objects That can be converted
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

