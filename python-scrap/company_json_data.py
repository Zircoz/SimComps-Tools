names_file = open("namesSimcomps24072020.txt", "r+") #close
failed_file = open("failedname.txt", "w")
#data_file = open("SimComps10072020.txt", "w") #testDump and close

import json
import time
#import grequests
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
failed_list = ['https://www.simcompanies.com/api/v2/players-by-company/COLOSSIAM-House/', 'https://www.simcompanies.com/api/v2/players-by-company/DBRMAX-Company/']




def make_url_list():
    '''
    base_url = "https://www.simcompanies.com/api/v2/players-by-company/"
    name_list = list()
    for line in name_file:
        line = '-'.join(line.split(' '))
        fetch_url = base_url+line[:-1]+'/'
        name_list.append(fetch_url)
    	'''
    return failed_list
#print(requests.get(base_url).content)
#data = list()
#for line in names_file:
#line = '-'.join(line.split(' '))
#print(type(line))
#fetch_url = base_url+line[:-1]+'/'
#print(fetch_url)
'''
'''
links = make_url_list()
total_links = len(links)
start_time = time.time()
#reqs = (grequests.get(link) for link in links)
#resp = grequests.imap(reqs, grequests.Pool(15))
#c = 0
def edit_spreadsheet(name, compID):
    scope = ['https://www.googleapi.com/auth/drive',
             'https://www.googleapis.com/auth/drive.file'
             ]

    file_name = 'client_key.json'
    gc = gspread.service_account(filename=file_name)
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1PdUZ8GwVdiTE54oguK9unwpyL13KK36p6MT2HCdDnJ0/edit#gid=528563174')
    worksh = sh.worksheet("IDList")
    #sheet = client.open('Python Sheet').DailyCompaniesCount
    row = [name, compID]
    index = 2
    worksh.insert_row(row, index)

'''
for r in resp:
    dat = json.loads(r.content)
    data.append(dat)
    c+=1
    print("data dumps collected:", c,"out of ", total_links, '\r', end='')
    #print(dat)
print("--- %s seconds ---" %(time.time() - start_time))
data_file.write(json.dump(data))
data_file.close()
names_file.close()
#r = requests.get(fetch_url)
#data.append(json.loads(r.content))
    #time.sleep(5)
'''
count=0
failedLinks = []
for url in links:
    try:
        
        res = requests.get(url)
        data = json.loads(res.content)
        ID = data['player']['id']
        playerName = data['player']['company']
        edit_spreadsheet(playerName, ID)
        count+=1
        print(playerName, "scrapped", '\r', end='')
    except:
        failedLinks.append(url)
        continue
print("Failed links are:")
print(failedLinks)
failed_file.write(failedLinks)
names_file.close()
failed_file.close()


'''
url = "https://www.simcompanies.com/api/v2/players-by-company/ManJos-Pvt.-Ltd./"
res = requests.get(url)
data = json.loads(res.content)
print(data['player']['id'])
print(type(data['player']['id']))
'''
