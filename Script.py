from urllib import request
import click
import json
from modified_api import  MouserPartSearchRequest

# API Keys File (Default)
API_KEYS_FILE = 'mouser_api_keys.yaml'

args = []

def test(request_type, operation, number):


    if request_type == 'search':
        request = MouserPartSearchRequest(operation, API_KEYS_FILE, *args)

        
        if operation == 'partnumber':
            if not number:
                print('[ERROR]\tMissing Mouser Part Number')
            else:
                # Run request
                 search = request.part_search(number)
                 # Print body
                 #print('[BODY]')
                 #print(json.dumps(request.body, indent=4, sort_keys=True))
                 if search:
                    # Print result
                    #print('[DATA]')
                     a= request.print_clean_response()
    return a


b=test('search','partnumber','581-SCPB08A355SNA')
print(b)
