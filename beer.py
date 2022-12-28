
import requests
import argparse

req = requests.get('https://api.punkapi.com/v2/beers')

def main(args):
   print("Beers preffered for your dish are:\n")

   beers = get_beers(args.dish)

   for beer in beers:
      print(beer)

   print("\n Bon appetit!")

def get_beers(food):
   find_beers=0
   beers = []
   
   for  element in range(24):
      join_food=" ".join(req.json()[element]["food_pairing"])
      if join_food.find(food)>=0:
         # print(join_food)
         find_beers+=1
         beers.append(req.json()[element]["name"])
      elif element==23 and find_beers==0:
         beers = []
   return beers 

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument("dish",type=str, help="Give me the name of the food ")
   args = parser.parse_args()

   main(args)