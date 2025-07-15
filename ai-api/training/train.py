import os
import pandas as pd
import requests

# Récupérer l'URL de l'API de données depuis les variables d'environnement
# Le nom du service 'data-api' est utilisé comme nom d'hôte grâce à Docker Compose
DATA_API_URL = os.getenv("DATA_API_URL", "http://data-api:8001") 

def fetch_all_profiles_from_api(page_size: int = 100) -> pd.DataFrame:
    """
    Récupère tous les profils socio-démographiques depuis l'API de données
    en gérant la pagination.

    Args:
        page_size (int): Le nombre d'éléments à récupérer par requête.

    Returns:
        pd.DataFrame: Un DataFrame contenant tous les profils.
    """
    all_profiles = []
    current_page = 0
    
    print(f"Début de la récupération des données depuis {DATA_API_URL}...")

    while True:
        # Calculer le 'skip' pour la pagination
        skip = current_page * page_size
        
        # Construire l'URL avec les paramètres de pagination
        request_url = f"{DATA_API_URL}/profiles/?skip={skip}&limit={page_size}"
        
        try:
            response = requests.get(request_url)
            response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP (4xx ou 5xx)
            
            data = response.json()

            # Si la page est vide, on a atteint la fin
            if not data:
                print("Toutes les données ont été récupérées.")
                break
            
            # Ajouter les données de la page à notre liste
            all_profiles.extend(data)
            print(f"Page {current_page + 1} récupérée ({len(data)} profils).")
            
            current_page += 1

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la communication avec l'API de données : {e}")
            return pd.DataFrame() # Retourner un DataFrame vide en cas d'erreur

    # Convertir la liste de dictionnaires en DataFrame
    return pd.DataFrame(all_profiles)


if __name__ == "__main__":
    # Exemple d'utilisation
    profiles_df = fetch_all_profiles_from_api()
    
    if not profiles_df.empty:
        print("\nAperçu des données récupérées :")
        print(profiles_df.head())
        print(f"\n{len(profiles_df)} profils au total ont été chargés.")
        
        # Ici, tu peux commencer le prétraitement et l'entraînement de ton modèle
        # ...
        # X = profiles_df.drop("income", axis=1)
        # y = profiles_df["income"]
        # ...