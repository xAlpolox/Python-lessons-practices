""" import xml.parsers.expat

def start_element(name, attrs):
    print('Start elemnt:', name, attrs)

def end_element( name):
    print('End element:', name)

def characters(data):
    print( 'Characters: ', repr(data))

p= xml.parsers.expat.ParserCreate()
p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = characters """

#xmlExample= """<?xml version="1.0"?><army id="Rebel Alliance">
#<echoTree name="Luke Skywalker">Jedi in training</echoTree>
#<echoSeven name="Han Solo">Smuggler</echoSeven></army>"""

#p.Parse(xmlExample,1)

import json

sampleJSON= json.dumps([
   "rebels",
   {
      "firstName": "Luke",
      "lastName": "Skywalker"
   },
   {
      "firstName": "Han",
      "lastName": "Solo"
   },
   {
      "firstName": "Wedge",
      "lastName": "Antilles"
   }
], separators=(',',':'))

json_Decoder= json.loads(sampleJSON)

#print('Original JSON: ',sampleJSON)
#print('Decoded JSON: ',json_Decoder)
for elements in json_Decoder:
    print(elements)