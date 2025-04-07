import pandas as pd
import matplotlib.pyplot as plt
print("____________________________partie1_________________________________")
#partie1
# Chargement du fichier CSV
df = pd.read_csv("dataset/Students_Grading_Dataset.csv")
# Afficher les 5 premières lignes
print("Aperçu des données :")
print(df.head())
print("____________________________partie2_________________________________")
#partie2
# Informations sur les colonnes
print("\nInformations sur le dataset :")
print(df.info())
# Valeurs manquantes par colonne
print("\nValeurs manquantes :")
print(df.isnull().sum())
# Statistiques descriptives pour les colonnes numériques
print("\nStatistiques descriptives :")
print(df.describe())
print("____________________________partie3_________________________________")
#partie3
# Histogramme de la note finale
if 'Final_Score' in df.columns:
    plt.figure(figsize=(8,5))
    plt.hist(df['Final_Score'], bins=10, color='skyblue', edgecolor='black')
    plt.title("Distribution des notes finales")
    plt.xlabel("Note")
    plt.ylabel("Nombre d'étudiants")
    plt.grid(True)
    plt.show()
print("____________________________partie4_________________________________")
#partie4
# Analyse de la moyenne des notes finales par genre
if 'Gender' in df.columns and 'Final_Score' in df.columns:
    gender_avg = df.groupby('Gender')['Final_Score'].mean()
    print("\nMoyenne des notes finales par genre :")
    print(gender_avg)
    gender_avg.plot(kind='bar', color=['skyblue', 'pink'])
    plt.title("Moyenne des notes finales par genre")
    plt.ylabel("Note moyenne")
    plt.xlabel("Genre")
    plt.grid(axis='y')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
print("____________________________partie5_________________________________")
#partie5
# Matrice de corrélation
plt.figure(figsize=(10,8))
correlation = df.corr(numeric_only=True)

plt.imshow(correlation, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.title("Matrice de corrélation")
plt.xticks(range(len(correlation)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation)), correlation.columns)
plt.tight_layout()
plt.show()

# Optionnel : afficher la table numérique
print("\nMatrice de corrélation :")
print(correlation)
print("____________________________partie6_________________________________")
#partie6
# Détection automatique des colonnes de matière
subject_columns = [col for col in df.columns if 'Final_Score' in col and col != 'Grade']
print("\nColonnes de matière détectées :", subject_columns)
# Moyenne par matière
subject_means = df[subject_columns].mean()
# Affichage en barres
subject_means.plot(kind='bar', color='lightgreen')
plt.title("Moyenne des notes par matière")
plt.ylabel("Note moyenne")
plt.xlabel("Matière")
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("____________________________partie7_________________________________")
#partie7
# Top 5 étudiants
top_students = df.sort_values(by='Final_Score', ascending=False).head(5)
print("\nTop 5 des meilleurs étudiants :")
print(top_students[['Name', 'Final_Score']] if 'Name' in df.columns else top_students.head())
# Flop 5 étudiants
bottom_students = df.sort_values(by='Final_Score').head(5)
print("\nTop 5 des moins bons étudiants :")
print(bottom_students[['Name', 'Grade']] if 'Name' in df.columns else bottom_students.head())
print("____________________________partie8_________________________________")
#partie8
#Détection des colonnes d'évaluations intermédiaires (par exemple: Grade 1, Grade 2, Grade 3)
eval_columns = [col for col in df.columns if 'Final_Score' in col and col != 'Grade']
print("\nÉvaluations détectées :", eval_columns)
# Tracer l'évolution des notes pour un échantillon d'étudiants (ex: 10)
sample_df = df[eval_columns].head(10)
plt.figure(figsize=(10, 6))
for i in range(len(sample_df)):
    plt.plot(eval_columns, sample_df.iloc[i], marker='o', label=f'Étudiant {i + 1}')
plt.title("Évolution des notes pour les 10 premiers étudiants")
plt.xlabel("Évaluations")
plt.ylabel("Note")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.show()

# Moyenne par évaluation dans le temps
mean_progress = df[eval_columns].mean()
mean_progress.plot(kind='line', marker='o', color='orange')
plt.title("Évolution moyenne des notes sur toutes les évaluations")
plt.xlabel("Évaluation")
plt.ylabel("Note moyenne")
plt.grid(True)
plt.tight_layout()
plt.show()

