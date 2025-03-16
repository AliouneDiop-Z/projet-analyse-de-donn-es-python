import pandas as pd  # Importation de la bibliothèque pandas pour manipuler les données
import matplotlib.pyplot as plt  # Importation de matplotlib pour créer des visualisations

# Chargement des données depuis le fichier CSV
# J'ai trouvé la commande read_csv dans la documentation officielle de pandas : https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# Cette fonction permet de lire un fichier CSV et de le transformer en DataFrame, une structure de données tabulaire très utilisée en data science
file_path = r'C:\Users\aliox\Downloads\ndb_events_data.csv'  # Chemin du fichier CSV contenant les ventes de NDB Events
df = pd.read_csv(file_path, encoding='utf-8')  # Lecture du fichier avec encodage UTF-8 pour éviter les erreurs liées aux caractères spéciaux
print(df.columns)  # Affiche les noms de colonnes exacts pour voir s'il y a une erreur

# Affichage des premières lignes du fichier pour vérifier le bon chargement des données
print(df.head())  # head() affiche les 5 premières lignes du DataFrame, pratique pour avoir un aperçu rapide des données

# Calcul des statistiques de base sur le chiffre d'affaires
# J'ai trouvé la fonction describe() en cherchant "statistiques pandas DataFrame" sur Google
# Elle permet d'obtenir des statistiques comme la moyenne, le min, le max et les quartiles
stats = df["Chiffre d'affaires (€)"].describe()
print(list(df.columns))

print(stats)

# Tri des produits/services en fonction du chiffre d'affaires généré, du plus élevé au plus faible
# J'ai découvert sort_values() avec pandas et en lisant cette page : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
df_sorted = df.sort_values(by="Chiffre d'affaires (€)", ascending=False)  # Correction ici
print(df_sorted.head())  # Affichage des 5 meilleures ventes

# Regroupement des données par type de produit/service et somme du chiffre d'affaires
# J'ai appris groupby() en regardant un tuto sur YouTube de Data School : https://www.youtube.com/shorts/J-d-AzyNTTI  https://www.youtube.com/watch?v=qy0fDqoMJx8
revenus_par_type = df.groupby('Type de service')["Chiffre d'affaires (€)"].sum()


# Création d'un graphique en barres pour visualiser le chiffre d'affaires par type de produit/service
plt.figure(figsize=(10, 6))  # Définition de la taille du graphique
revenus_par_type.plot(kind='bar', color='skyblue')  # Création d'un graphique en barres avec une couleur bleue claire

# Ajout des labels pour mieux comprendre l'axe des X et Y
plt.xlabel("Type de produit/service")  # xlabel() définit le nom de l'axe horizontal (X), ici on indique qu'il représente les types de produits/services
plt.ylabel("Chiffre d'affaires (€)")  # ylabel() définit le nom de l'axe vertical (Y), ici pour indiquer qu'on mesure le chiffre d'affaires en euros
plt.title("Chiffre d'affaires par Type de produit/service")  # Ajout d'un titre au graphique
plt.xticks(rotation=45)  # Rotation des noms sur l'axe X pour qu'ils soient lisibles
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Ajout d'une grille horizontale pour mieux voir les différences de CA
plt.show()  # Affichage du graphique

# Regroupement des données par ville et somme du chiffre d'affaires
revenus_par_ville = df.groupby('Ville')["Chiffre d'affaires (€)"].sum()

# Création d'un graphique en secteurs (camembert) pour voir la répartition du CA par ville
plt.figure(figsize=(8, 8))  # Taille du graphique
revenus_par_ville.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='coolwarm', legend=True)
plt.title("Répartition du chiffre d'affaires par ville")  # Ajout d'un titre
plt.ylabel("")  # Suppression du label Y qui n'est pas pertinent pour un camembert
plt.show()

# Affichage des 5 produits/services les plus rentables
print("Top 5 des produits/services les plus rentables :")
print(df_sorted.head(5))  # head(5) permet de voir uniquement les 5 premiers résultats du tri effectué précédemment


#conclusion 


#Concentration du chiffre d'affaires

#Paris et Argenteuil génèrent ensemble plus de 73% du chiffre d'affaires total, alors que Nanterre reste en retrait ( 26,9% ).
# Une analyse plus poussée des facteurs influençant ce résultat est nécessaire plusieurs hypothése s'offre a nous :Moins de ventes à Nanterre ?Des prix plus bas ? moins d'événements organisés ?

#Rentabilité des services

#Les animations sont clairement le moteur principal du chiffre d'affaires, bien loin devant les autres services.Les structures gonflables et mascottes génèrent aussi des revenus intéressants.
# En revanche, la buvette sucrée & salée est peu rentable , ce qui pourrait être dû à un faible volume de ventes ou des marges trop faibles .

#Aperçu des transactions

#la transaction la plus élevée atteint 1250 € , ce qui indique un potentiel de ventes importants.À l'inverse, la transaction minimale est de 48 € , ce qui suggère des disparités importantes entre les différents types de ventes.

#Recommandations pour la prise de décision

#Optimiser les performances à Nanterre : Analyser les raisons du faible chiffre d'affaires et ajuster la stratégie locale (prix, communication, événements…).
#Miser sur les animations : Renforcer leur promotion et augmenter éventuellement les tarifs en fonction de la demande.
#Maximiser la rentabilité des ventes de buvette : Revoir la tarification ou la diversité de l'offre pour augmenter le chiffre d'affaires.
#Approfondir l'analyse : Croiser ces résultats avec d'autres indicateurs comme la fréquentation des événements, les coûts opérationnels et la satisfaction client.

