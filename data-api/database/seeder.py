import pandas as pd
from os.path import join
from datetime import datetime

from database.engine import engine

df_path = join("data", "processed", "adult.csv")


def seed_table(df_path, table_name):
    """
    Insère toutes les lignes du DataFrame dans la table soc_dem_profiles.
    Les colonnes du DataFrame doivent correspondre à celles de la table.
    """
    try:
        df = pd.read_csv(df_path)
        if "created_at" not in df.columns:
            df["created_at"] = datetime.now()
        if "was_used_for_training" not in df.columns:
            df["was_used_for_training"] = False
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False,
            method="multi",
        )
        print(f"✅ {len(df)} lignes insérées dans soc_dem_profiles")
    except Exception as e:
        print(f"❌ Erreur lors de l'insertion dans soc_dem_profiles: {e}")


if __name__ == "__main__":
    print(f"{' Seeding ':=^60}")
    seed_table(df_path=df_path, table_name="soc_dem_profiles")
    print(f"{' Fin du seeding ':=^60}")
