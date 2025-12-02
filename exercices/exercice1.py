import pandas as pd


def write_rapport(chaine):
    with open("rapport.txt","a") as f:
        f.write(chaine)
    f.close()

#Charger le fichier avec Pandas 
df = pd.read_csv('ventes.csv')
# 2. Ajouter une colonne montant_total (quantite × prix_unitaire)
df['montant_total']= df['quantite'] * df['prix_unitaire']
print(df)
# 3. Calculer le total des ventes par vendeur 
par_vendeur = df.groupby('vendeur')['montant_total'].sum()
print(f"Total des ventes par vendeur : {par_vendeur}")
rapport = f"Total des ventes par vendeur : {par_vendeur}"

# 4. Calculer le total des ventes par produit 
par_produit = df.groupby('produit')['quantite'].sum()
print(f"Total des ventes par produits : {par_produit}")
rapport = rapport + f"Total des ventes par produits : {par_produit} "

# 5. Identifier le top 3 des ventes (montant le plus élevé)
top3 = df.sort_values('montant_total',ascending=False).head(3)
print(top3)
rapport = rapport + f"{top3}"
#  6. Sauvegarder les résultats dans ventes_analysees.csv
df.to_csv(
    'ventes_analysees.csv',
    sep=',',
    encoding='utf-8',
    index=False, # Ne pas inclure l'index
    header=True, # Inclure les en-têtes
    na_rep='NA', # Représentation des NaN
)


#bonus : on vas creer un rapport (fichier texte par exemple) pour mettre les reponses aux question 2,3 et 4 
write_rapport(rapport)



