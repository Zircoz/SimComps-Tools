#https://www.simcompanies.com/api/v3/encyclopedia/ranking/0/
import requests
import json
import time
'''
base_url = "https://www.simcompanies.com/api/v3/encyclopedia/ranking/"
def make_links_list():
    i, flag = 0, True
    links = list()
    while(flag):
        links.append(base_url+str(i)+"/")
        
    

'''

base_url = "https://www.simcompanies.com/api/v3/encyclopedia/ranking/"
#0-179
company=0
def extract_names(data, file):
    for i in range(0, len(data)):
        file.write(data[i]['company']+"\n")
        #print(data[i]['company'])
        
        

names_file = open("namesSimcomps24072020.txt","w")
i=0
flag=True
while(flag):
    #companies = 0
    fetch_url = base_url+str(i)+'/'
    r = requests.get(fetch_url)
    fetched_data = json.loads(r.content)
    if len(fetched_data)>0:
        company+=len(fetched_data)
        extract_names(fetched_data, names_file)
        print(company, " company's names recorded", '\r', end='')
        i+=1
    else:
        flag=False
        #time.sleep(0.5)
names_file.close()

        
        
        
