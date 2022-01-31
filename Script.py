
from dataclasses import replace
from os import remove
from re import T
import pandas as pd
import datetime as dt
from modified_api import  MouserPartSearchRequest


def testscript():
    # API Keys File 
    API_KEYS_FILE = 'mouser_api_keys.yaml'

    #list declerations
    args = []
    a = []
    fg =[]
    t=[]
    t2=[]



    #Dataframe declarations
    df = pd.read_excel(r'C:\Users\HaylesJ\Documents\GitHub\MouserStockTracker\test_data.xlsx','Sheet1')
    namedf = df['Name']
    numdf = df['MouserPartNumber']
    b= df['MouserPartNumber']


    #Function to Call API
    def test(number):
        request = MouserPartSearchRequest('partnumber', API_KEYS_FILE, *args)    
        request.part_search(number)           
        a= request.print_clean_response()
        
        return a





    #iterating test function with part nums
    for i ,  row in df.iterrows():
        a = test(b[i])
        #print(a)
    
        c= a.values()
        d=  list(c)
        fg.append(d)
        



    #Creating Data Frame

  
    

    df_result = pd.DataFrame(fg)
    df_result.columns=['Avaliablity']
    df_result= df_result.join(namedf)
    df_result= df_result.join(numdf)

    df_result['Avaliablity'] = df_result['Avaliablity'].map(lambda x: x.rstrip('In Stock'))
   
    
    temp = df_result['Avaliablity']
    
    for i, row in df_result.iterrows():
        ti= str( dt.datetime.now())
        dat=ti[0:10]
        tim= ti[11:16]
            
        if temp[i] =="None":
            t.append(0)
            t2.append(0)
            

           
        else:
            t.append(str(dat))
            t2.append(str(tim))

    df_result['Date'] = t
    df_result['Time'] = t2
    

    #Output stock levels to CSV file
    df_result.to_csv('Stock_data.csv')
testscript()    