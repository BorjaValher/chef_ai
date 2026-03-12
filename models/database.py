import psycopg2
import os
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

class Database:
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.client = create_client(url, key)
        print("[✅] Conectado a Supabase vía API (Puerto 443)")
        
        

    def save_recipe(self, title, ingredients, instructions):
        try:
            data = {
                "title": title,
                "ingredients": ingredients,
                "instructions": instructions
            }
            # Insertamos en la tabla 'recipes'
            response = self.client.table("recipes").insert(data).execute()
            return True
        except Exception as e:
            print(f"❌ Error API: {e}")
            return False


    def fetch_all(self):
        """Trae todas las recetas de la nube usando la API."""
        try:
            # .select("*") trae todas las columnas
            # .order("created_at", desc=True) las ordena de más nueva a más vieja
            response = self.client.table("recipes").select("*").order("created_at", desc=True).execute()
            
            # La API nos devuelve una lista de diccionarios directamente
            return response.data 
        except Exception as e:
            print(f"❌ Error al recuperar recetas: {e}")
            return []