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
             "superfice" : country['area'],
             "langue" : country['languages']
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

# Bonus  Top par langue parlée
# a partir des mêmes données, identifier les 3 langues les plus parlées en Europe (en termes de population totale des pays où elles sont langue officielle).
# créer un tableau langues_europe avec : langue, nombre de pays, population totale concernée.
# sauvegarder ce tableau dans une nouvelle feuille de pays_europe.xlsx.
 
most_language = df.explode('langue')

langues_stats = most_language.groupby('langue').agg(
    nb_pays=('nom', 'count'),
    population_totale=('population', 'sum')
)

langues_stats = langues_stats.nlargest(3,'population_totale')
print(langues_stats)
with pd.ExcelWriter("pays_europe.xlsx",mode="a") as writer:
    langues_stats.to_excel(writer,sheet_name='population',index=True)

# print(langues_stats)
# API : https://restcountries.com/v3.1

