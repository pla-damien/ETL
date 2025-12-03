import pandas as pd
#Charger les données avec Pandas
df = pd.read_excel('ventes_janvier.xlsx')

# 2. Nettoyer : - Supprimer les doublons 
df.drop_duplicates()

# - Remplir les valeurs manquantes de region par "Non spécifié" 
df['region'] = df['region'].fillna('Non spécifié')
# - Convertir date en datetime 
df['date'] = pd.to_datetime(df['date'])

# 3. Transformer : - Créer montant_total = quantite × prix_unitaire 
df['montant_total'] = df['quantite'] * df['prix_unitaire'] 
print(df)
# - Extraire le jour et jour_semaine de la date 
df['jour']= df['date'].dt.day
df['jour_semaine']=df['date'].dt.day_name()
print(df)
# 4. Analyser : - Total des ventes par région 
par_region = df.groupby('region')['quantite'].sum()
print(par_region)
# - Produit le plus vendu (en quantité) 
produit1 = df.groupby('produit')['quantite'].sum().nlargest(1)
print(produit1)
# - Jour de la semaine avec le plus de ventes 
jour1 = df.groupby('jour_semaine')['quantite'].sum().nlargest(1)
print(jour1)
# 5. Créer un fichier Excel avec 3 feuilles : 
# - Feuille "Données" : Données nettoyées - Feuille "Par région" : Agrégation par région - Feuille "Par produit" : Agrégation par produit
with pd.ExcelWriter('ventes_analyse.xlsx') as writer :
    df.to_excel(writer,sheet_name='Données',index = False)
    par_region.to_excel(writer,sheet_name='Par région',index = False)
    produit1.to_excel(writer,sheet_name='Par produit',index = False)