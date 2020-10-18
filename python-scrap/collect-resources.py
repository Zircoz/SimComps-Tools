import pymongo
import requests
import json

client = pymongo.MongoClient("mongodb+srv://zircoz:zecopeco@cluster0.rtbr2.gcp.mongodb.net/SimComps?retryWrites=true&w=majority&authMechanism=SCRAM-SHA-1")
encyclo_db = client['SimComps']
encyclo_collection = encyclo_db['EncyclopediaResources']

url = "https://www.simcompanies.com/api/v3/en/encyclopedia/resources/"
res = requests.get(url)
if res.status_code==200:
	resource_data = json.loads(res.content)
	resor = [dat for dat in resource_data]
	print(resor)
	inserts = encyclo_collection.insert_many([dat for dat in resource_data])
	print('{} records were inserted into DB.'.format(len(inserts.inserted_ids)))
	
