
import requests
import argparse
import whisper

from pathlib import Path

req = requests.get('https://api.punkapi.com/v2/beers')

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--dish', type=str)
group.add_argument('--audio_file', type=Path)


# parser.add_argument("dish",type=str,help="Give me the name of the food ")
args = parser.parse_args()

print("Beers preffered for your dish are:\n")

if not args.dish:
   model = whisper.load_model("base")
   result = model.transcribe(str(args.audio_file))
   args.dish = result["text"]

find_beers=0
for  element in range(24):
    join_food=" ".join(req.json()[element]["food_pairing"])
    if join_food.find(args.dish)>=0:
       find_beers+=1
       print(req.json()[element]["name"])
    elif element==23 and find_beers==0:
       print("I don't have this food on my list, try anther dish")    

print("\n Bon appetit!")