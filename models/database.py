import os
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

class Database:
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.client = create_client(url, key)
        
    def save_recipe(self, title, ingredients, instructions):
        try:
            data = {
                "title": title,
                "ingredients": ingredients,
                "instructions": instructions
            }
            self.client.table("recipes").insert(data).execute()
            return True, "Recipe saved successfully."
        except Exception as e:
            return False, f"Failed to connect to the database: {e}"


    def fetch_all(self):
        try:
            response = self.client.table("recipes").select("*").order("created_at", desc=True).execute()
            return response.data
        except Exception as e:
            raise Exception(f"Unable to fetch recipes: {e}")