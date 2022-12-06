
import webbrowser
import requests
import argparse

# webbrowser.open('https://api.punkapi.com/v2/beers')

req = requests.get('https://api.punkapi.com/v2/beers')

parser = argparse.ArgumentParser()
parser.add_argument("danie",type=str,help="Give me the name of the food ")
args = parser.parse_args()

print("Beers preffered for your dish are:\n")

find_beers=0
for  element in range(24):
    join_food=" ".join(req.json()[element]["food_pairing"])
    if join_food.find(args.danie)>=0:
       find_beers+=1
       print(req.json()[element]["name"])
    elif element==23 and find_beers==0:
       print("I don't have this food on my list, try anther dish")    

print("\n Bon appetit!")