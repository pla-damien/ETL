import requests
import pandas as pd
import os 
from dotenv import load_dotenv
from requests.exceptions import RequestException, Timeout, ConnectionError

def connect_api(params:str):
    try:
        # Envoi de la requête HTTP GET.
        # timeout=5 signifie : lever une exception Timeout si aucune réponse
        # n'est reçue avant 5 secondes.
        response = requests.get(BASE_URL,params=params)

        # raise_for_status() :
        # - Ne fait rien si le code de statut est 2xx ou 3xx
        # - Lève une exception HTTPError si le code est 4xx ou 5xx
        response.raise_for_status()

        # Tentative de parse du corps de la réponse comme JSON.
        # Si le contenu n'est pas du JSON valide, .json() peut lever ValueError.
        data = response.json()
        return(data)

        # Timeout : le serveur a mis trop de temps à répondre.
    except Timeout:
        print("Timeout : L'API met trop de temps à répondre")

    # ConnectionError : problème de réseau (pas d'accès internet, DNS, etc.).
    except ConnectionError:
        print("Erreur de connexion : Vérifiez votre réseau ou le serveur")

    # HTTPError : erreur HTTP après raise_for_status() (404, 500, etc.).
    except requests.exceptions.HTTPError as e:
        print(f"Erreur HTTP : {e}")
        # response peut contenir plus d'infos (code + corps de la réponse)
        print(f"Code : {response.status_code}")
        print(f"Message : {response.text}")

    # RequestException : exception générique de requests (base pour toutes les autres).
    except RequestException as e:
        print(f"Erreur générale requests : {e}")

    # ValueError : problème lors du parsing JSON (réponse pas au format JSON).
    except ValueError:
        print("La réponse n'est pas du JSON valide")




load_dotenv()
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
# API_KEY = os.getenv('OPENWEATHER_API_KEY')
API_KEY = os.getenv('OPENWEATHER_API_KEY')
print(API_KEY)
# Exercice 5 - API Météo
# Objectif : Récupérer et comparer la météo de plusieurs villes

# Prérequis : Compte OpenWeatherMap avec API key

# Tâches 1. Définir une liste de 10 villes françaises 
liste_ville = ["Lille", "Lyon", "Paris", "Brest", "Rennes",
               "Marseille", "Orleans", "Nantes", "Arras", "Amsterdam"]
# 2. Pour chaque ville, récupérer : - Température actuelle - Température ressentie - Humidité - Description 
ville_meteo = []
for ville in liste_ville:
    params = {
    'q': ville,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'fr'
    }
    print(f"ville : {ville}")
    data = connect_api(params)
    print(data)
    meteo = {"Temperature_actuelle":data['main']['temp'],
        "Temperature_ressentie":data['main']['feels_like'],
        "Humidite":data['main']['humidity'],
        "Description":data['weather'][0]['description'],
    }
    
    ville_meteo.append(meteo)
print(ville_meteo)
# 3. Créer un DataFrame avec ces informations 
df = pd.DataFrame(ville_meteo)
print(df)
# 4. Identifier la ville la plus chaude et la plus froide 
print(f"Ville la plus chaude : {df.nlargest(1,'Temperature_actuelle')}")
print(f"Ville la plus froide : {df.nsmallest(1,'Temperature_actuelle')}")
# 5. Calculer la température moyenne 
print(f"La temperature moyenne est de {df['Temperature_actuelle'].mean()}")
# 6. Sauvegarder dans meteo_villes.csv 7. Bonus : Ajouter une gestion d'erreur si une ville n'est pas trouvée
df.to_csv('meteo_villes.csv')