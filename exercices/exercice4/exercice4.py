import requests
import json
import pandas as pd
import openpyxl
# Objectif : Analyser les données des pays

# Tâches 1. Récupérer tous les pays d'Europe 
BASE_URL = "https://restcountries.com/v3.1/subregion/Europe"

responce = requests.get(BASE_URL)
print(f"Status: {responce.status_code}")

data = responce.json()
print(data)
# 2. Créer un DataFrame avec : nom, capitale, population, superficie 
list_country = []

for country in data:
    pays1 = {"nom" :country['name']['common'],
             "capitale" : country['capital'][0],
             "population" : country['population'],
             "superfice" : country['area']
             }
    list_country.append(pays1)
print(list_country)
df = pd.DataFrame(list_country)
print(df)
# # 3. Calculer la densité de population (population / superficie) 
print(type(df['population']))
df['densite'] = df['population'] / df['superfice']
print(df)
# 4. Identifier les 5 pays les plus peuplés d'Europe 
top5 = df.nlargest(5,'population')
print(top5)
# 5. Calculer la population totale de l'Europe 
pop_total = df['population'].sum()
print(f"Population total de l'europ : {pop_total}")
# 6. Trouver le pays avec la plus grande densité 
pays_max = df.nlargest(1,'densite')
print(pays_max)
# 7. Sauvegarder les résultats dans pays_europe.xlsx
with pd.ExcelWriter("pays_europe.xlsx") as writer:
    df.to_excel(writer,index=False)


# API : https://restcountries.com/v3.1

