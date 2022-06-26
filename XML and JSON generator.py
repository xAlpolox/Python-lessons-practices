""" from xml.etree.ElementTree import Element, SubElement, tostring

root = Element('rebels')
x = 0
while x < 10:
    
    rebel= SubElement(root, 'rebel')
    firstName= SubElement(rebel, 'firstName')
    lastName= SubElement(rebel, 'lastElement')
    firstName.text= 'Luke'
    lastName.text= 'Skywalker'
    x+=1
print(tostring(root))
 """
 
import json
from pickle import TRUE
straightJSON= json.dumps(['rebels',
                            {'firstName':'Luke', 'lastName':'Skywalker'}],
                             separators=(',',':'))

prettyJSON= json.dumps(['rebels',
                            {'firstName':'Luke', 'lastName':'Skywalker'}],
                            sort_keys=TRUE,
                            indent=3)
                            

print('straightJSON output:\n', straightJSON)
print('prettyJSON output:\n', prettyJSON)
f= open('json_generated_file', 'w')
f.write(prettyJSON)
f.close()
