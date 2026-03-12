import requests
import json

class AIService:
    def __init__(self, model_name="llama3.1"):
        self.url = "http://localhost:11434/api/generate"
        self.model_name = model_name
        
    def generate_recipe_idea(self, ingredients_list):
        if ingredients_list:
            prompt = f"Crea una receta de cocina creativa usando estos ingredientes: {ingredients_list}."
        else:
            prompt = "Crea una receta de cocina creativa y sorprendente. Elige tú los ingredientes."
    
        
        prompt += " Responde con: TÍTULO, INGREDIENTES y PASOS."
        payload = {
            "model": self.model_name, 
            "prompt": f"Crea una receta con: {ingredients_list}",
            "stream": False
        }
        
        try:
            response = requests.post(self.url, json=payload)
            if response.status_code != 200:
                error_detail = response.json().get("error", "Error desconocido")
                return f"Error de Ollama ({response.status_code}): {error_detail}"
        
            return response.json().get("response", "No se pudo generar.")
        except Exception as e:
            return f"Error al conectar con Ollama: {e}" 
       
