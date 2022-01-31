
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
    
        c= a.values()
        d=  list(c)
        fg.append(d)



    #Creating Data Frame

  
    

    df_result = pd.DataFrame(fg)
    df_result.columns=['Avaliablity']
    df_result= df_result.join(namedf)
    df_result= df_result.join(numdf)

    df_result['Avaliablity'] = df_result['Avaliablity'].map(lambda x: x.rstrip('In Stock'))
   
    df_result['Avaliablity'] = pd.to_numeric(df_result['Avaliablity'])
    temp = df_result['Avaliablity']
    lit =[]
    for i, row in df_result.iterrows():
        
        if temp[i]>0:
            ti=dt.datetime.now()
            dat=ti[0:10]
            

            t.append(str(ti))
        else:
            t.append(0)

    df_result['Time'] = t
      
    print(df_result)


    #Output stock levels to CSV file
    #df_result.to_csv('Stock_data.csv')
testscript()    