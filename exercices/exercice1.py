import pandas as pd
#Charger le fichier avec Pandas 
df = pd.read_csv('ventes.csv')
# 2. Ajouter une colonne montant_total (quantite × prix_unitaire)
df['montant_total']= df['quantite'] * df['prix_unitaire']
print(df)
# 3. Calculer le total des ventes par vendeur 
par_vendeur = df.groupby('vendeur')['montant_total'].sum()
print(f"Total des ventes par vendeur : {par_vendeur}")

# 4. Calculer le total des ventes par produit 
par_produit = df.groupby('produit')['montant_total'].sum()
print(f"Total des ventes par produits : {par_produit}")
# 5. Identifier le top 3 des ventes (montant le plus élevé)
top3 = df.sort_values('montant_total',ascending=False).head(3)
print(top3)
#  6. Sauvegarder les résultats dans ventes_analysees.csv
df.to_csv(
    'ventes_analysees.csv',
    sep=',',
    encoding='utf-8',
    index=False, # Ne pas inclure l'index
    header=True, # Inclure les en-têtes
    na_rep='NA', # Représentation des NaN
)



