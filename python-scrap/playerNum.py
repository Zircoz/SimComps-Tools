import requests
import json
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#import pprint
from datetime import datetime 
#Authorize API
def edit_spreadsheet(comp_num):
    scope = ['https://www.googleapi.com/auth/drive',
             'https://www.googleapis.com/auth/drive.file'
             ]

    file_name = 'client_key.json'
    gc = gspread.service_account(filename=file_name)
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1PdUZ8GwVdiTE54oguK9unwpyL13KK36p6MT2HCdDnJ0/edit#gid=528563174')
    worksh = sh.worksheet("DailyCompaniesCount")
    now = datetime.now()
    #sheet = client.open('Python Sheet').DailyCompaniesCount
    row = [now.strftime("%d/%m/%Y %H:%M:%S"), str(comp_num)]
    index = 2
    worksh.insert_row(row, index)
'''
def num_of_companies():
    base_url = "https://www.simcompanies.com/api/v3/encyclopedia/ranking/"
    companies = 0
    #file = open("playerNumbersSimComps.txt", "w")

    page, flag=0, True
    while(flag):
        fetch_url = base_url+str(page)+'/'
        res = requests.get(fetch_url)
        fetched_data = json.loads(res.content)
        if(len(fetched_data)>0):
            companies+=len(fetched_data)
            print("page", page, len(fetched_data), "companies")
            page+=1
        else:
            flag=False
    print("total companies", companies)
    #edit_spreadsheet(companies)

#calling whole func
#num_of_companies()
'''
def num_of_companies():
    base_url = "https://www.simcompanies.com/api/v3/encyclopedia/ranking/"
    companies = 0
    #file = open("playerNumbersSimComps.txt", "w")
    page_down, page_up = 0, 400
    flag = True
    while(flag):
        page = page_down+((page_up-page_down)//2)
        fetch_url = base_url+str(page)+'/'
        res = requests.get(fetch_url)
        #print(res.content)
        fetched_data_length = len(json.loads(res.content))
        print("fetchedDataLength", fetched_data_length)
        print("page", page)
        if fetched_data_length==0:
            print("inside if", page)
            page_up = page
        elif fetched_data_length==50:
            print("inside elif", page)
            page_down = page
        else:
            print("inside else", page)
            companies = companies + (page*50) + fetched_data_length
            #print("page", page)
            #print("data length", fetched_data_length)
            flag=False
    print("total companies", companies)
    edit_spreadsheet(companies)
num_of_companies()
