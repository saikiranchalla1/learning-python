import argparse

import requests


parser =argparse.ArgumentParser(description='Search keyword or file on Google')
parser.add_argument('-f',
dest='file', action='store-true',
help='Search file on Google')
parser.add_argument('-w',
dest='word', action='store',
help='Search by keyword. Enter the word to search')
args=parser.parse_args()
# dest will be the name of argument, store keep the arg 
if args.file:
    print('Not yet implemented')

def google_search(keyword):
    r=requests.get('http://www.google.com/search?q=' + keyword) 
    return r.text
if args.word is not None:
    print(google_search(args.word))
    