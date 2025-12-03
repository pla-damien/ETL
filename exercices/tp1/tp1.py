import pandas as pd
from pathlib import Path
## TP 1 - Pipeline CSV vers Excel

# **Objectif** : Créer un pipeline de traitement automatisé

# **Contexte** : Vous recevez quotidiennement des fichiers CSV de différentes sources (magasins) et devez les consolider dans un rapport Excel.

# **Fichiers d'entrée** : `magasin_A.csv`, `magasin_B.csv`, `magasin_C.csv`

# **Colonnes** : date, produit, quantite, prix_unitaire, vendeur

# **Pipeline à construire** :
# 1. Charger tous les fichiers CSV
dfA = pd.read_csv('magasin_A.csv')
dfB = pd.read_csv('magasin_B.csv')
dfC= pd.read_csv('magasin_C.csv')

dataframe = []
for file in Path(".").rglob("*.csv"):
    df = pd.read_csv(file)
    magasin = file.split("_")[1].split(".")[0]
    
    df['magasin'] = magasin
    dataframe.append(df)

    print(file)

df_all = pd.concat(dataframe,ignore_index=True)

# 2. Ajouter une colonne `magasin` (A, B ou C)
dfA['magasin'] = "A"
dfB['magasin'] = "B"
dfC['magasin'] = "C"

# 3. Concaténer tous les DataFrames
df_all = pd.concat([dfA,dfB,dfC],ignore_index=True)
print(df_all)
# 4. Nettoyer (doublons, valeurs manquantes)
df_all = df_all.drop_duplicates()
# 5. Calculer `montant_total`
df_all['montant_total'] = df_all['quantite'] * df_all['prix_unitaire']
print(df_all)
# 6. Créer un rapport Excel avec :
#    - Feuille "Consolidé" : Toutes les données


#    - Feuille "Par magasin" : Totaux par magasin
df_toto_mag = df_all.groupby('magasin')['montant_total'].sum()
print(df_toto_mag)
#    - Feuille "Par vendeur" : Performance des vendeurs
df_toto_vendeur = df_all.groupby('magasin','vendeur')['montant_total'].sum()
print(df_toto_vendeur)
#    - Feuille "Top produits" : 10 produits les plus vendus
df_top_produit = df_all.groupby('produit')['quantite'].sum().sort_values(ascending=False).head(10)
print(df_top_produit)

with pd.ExcelWriter('ventes_analyse.xlsx') as writer :
    df_all.to_excel(writer,sheet_name='Consolidé',index = True)
    df_toto_mag.to_excel(writer,sheet_name='Par magasin',index = True)
    df_toto_vendeur.to_excel(writer,sheet_name='Par vendeur',index = True)
    df_top_produit.to_excel(writer,sheet_name='Top produits',index = True)