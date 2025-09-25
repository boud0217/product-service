import uvicorn
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    # Charger les variables d'environnement
    load_dotenv()
    
    # Récupérer le port depuis les variables d'environnement ou utiliser 3030 par défaut
    port = int(os.getenv("PORT", "3030"))
    
    # Lancer le serveur
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)