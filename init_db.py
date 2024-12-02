import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("comments.db")

# Créer la table 'comments' si elle n'existe pas
conn.execute("""
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL
);
""")

print("La table 'comments' a été créée avec succès.")

# Fermer la connexion
conn.close()
