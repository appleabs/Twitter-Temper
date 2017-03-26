import json, requests, xml.etree.ElementTree

with open('woeid-to-a3.json') as data_file:
    data = json.load(data_file)

print(data)
