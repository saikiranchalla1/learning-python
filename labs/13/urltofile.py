import argparse

import requests
import datetime
import json
import csv
class HTTPRequestExtractor: 
    parser =argparse.ArgumentParser(description='Search keyword or file on Google')

    parser.add_argument('-u',
    dest='url', action='store', required=True,
    help='Parse url. Enter url')
    
    # # dest will be the name of argument, store keep the arg 
    # parser.add_argument('-t',
    # dest='text', action='store_true',default=True, 
    # help='Parse as text file')
   
    # parser.add_argument('-c',
    # dest='csv', action='store_true', 
    # help='Parse as csv file')
    
    # parser.add_argument('-j',
    # dest='json', action='store_true', 
    # help='Parse as JSON file')
    args=parser.parse_args() # after all args are added, parse 
    def get_url(url):
        try:
            r=requests.get(url)
            return r.text
        except requests.exceptions.RequestException as e:
            # TODO: print exception error message and HTTP error code            
            raise e
            
    def write_file(content):
        today = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        
        file_name = 'Output_'+today+'.txt'

        with open(file_name,'w') as f:
            f.write(content)
    if args.url is not None:
        http_res = get_url(args.url)
        write_file(http_res)

        