import requests
import pandas as pd

BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_URL = f"{BASE_URL}/users"
POST_URL = f"{BASE_URL}/posts"
COMMENT_URL = f"{BASE_URL}/comments" 

# Objectif : Récupérer et analyser des données

# Tâches

# Récupérer tous les utilisateurs (/users)
responce = requests.get(f"{USERS_URL}")
print(responce)
users = responce.json()
print(users)

# Afficher le nom et l'email de chaque utilisateur
for user in users:
    print(f"Nom : {user['name']} ,email : {user['email']}")

# Récupérer tous les posts de l'utilisateur avec userId=1
params = {
     "userId": 1
}
responce = requests.get(POST_URL, params=params)
print(responce)
posts = responce.json()
print(posts)

# Compter combien de posts chaque utilisateur a créé
for user in users:
    params = {
     "userId": user['id']
    }
    responce = requests.get(POST_URL, params=params)
    nb =  responce.json()
    print(f"L'utilisateur {user['id']} a effectué {len(nb)}")

# Récupérer les commentaires du post id=1
params = {
    "postId": 1
}
responce = requests.get(COMMENT_URL, params=params)
print(responce)
comments = responce.json()
print(comments)

# Créer un DataFrame Pandas avec :
# Colonnes : post_id, post_title, nombre_commentaires
# Pour les 10 premiers posts
compteur = 0 
post_id = []
post_title = []
nb_comment = []
for post in posts :
    if compteur < 10:
        post_id.append(post['id'])
        post_title.append(post['title'])
        compteur +=1
        params = {
        "postId": post['id']
        }
        responce = requests.get(COMMENT_URL, params=params)
        comments = responce.json()
        nb_comment.append(len(comments))
print(comments)
items = {f"post_id" : post_id,"post_title" :post_title,"nombre_commentaires" : nb_comment }
df = pd.DataFrame(items)
print(df)


# Astuce : Utiliser des boucles et pd.DataFrame()