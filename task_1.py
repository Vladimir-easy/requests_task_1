from pprint import pprint
import requests

def get_heroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    all_heroes_json = response.json()
    new_dict = {}
    for item in all_heroes_json:
        if item["name"] == "Hulk":
            if "intelligence" in item["powerstats"]:
                new_dict["Hulk"] = item['powerstats']['intelligence']
        if item["name"] == "Captain America":
            if "intelligence" in item["powerstats"]:
                new_dict["Captain America"] = item['powerstats']['intelligence']      
        if item["name"] == "Thanos":
            if "intelligence" in item["powerstats"]:
                new_dict["Thanos"] = item['powerstats']['intelligence'] 
                
    new_list = []
    for item in (new_dict.values()):
        new_list.append(item)   
        
    for item in new_dict:
        if new_dict[item] == max(new_list):
            print(f"Самым главным умником оказался: {item}")

if __name__ == "__main__":  
    get_heroes()
    
