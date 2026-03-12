from datetime import datetime
from views.console_view import ConsoleView
from views.base_view import BaseView
from models.ai_service import AIService
from models.database import Database

class AppController:
    def __init__(self, view):
        self.view = view
        self.ai = AIService(model_name="llama3.1")
        self.db = Database()
        
    def run(self):
        while True:
            choice = self.view.show_menu()
            
            if choice == '1':
                self.view.show_message("\n--- Mis Recetas Guardadas ---")
                recipes = self.db.fetch_all()
                if not recipes:
                    self.view.show_message("No hay recetas guardadas todavía. ¡Genera una primero!")
                else:
                    for idx, r in enumerate(recipes, 1):
                        # r es un diccionario, así que usamos las llaves de tu tabla
                        print(f"\n{idx}. 📖 TÍTULO: {r['title']}")
                        print(f"   🧂 INGREDIENTES: {r['ingredients']}")
                        print(f"   📝 INSTRUCCIONES: {r['instructions'][:100]}...") # Mostramos solo el principio
                        print("-" * 30)
                    
                    input("\nPresiona Enter para volver al menú...")
                    
            elif choice == '2':
                ingredients = self.view.get_ingredients_input()
                self.view.show_message("Consultando a Ollama, espera un momento...")
                
                ai_recipe = self.ai.generate_recipe_idea(ingredients)
                
                self.view.display_recipe(ai_recipe)
                
                save_choice = input("\nSave to Supabase? (y/n): ").lower()
                if save_choice == 'y':
                    # 1. Extraemos un título rápido del primer renglón del texto de la IA
                    # Si la IA puso "Título: Pasta", nos quedamos con eso.
                    lines = ai_recipe.strip().split('\n')
                    suggested_title = lines[0][:50] if lines else "Nueva Receta"
    
                    # 2. Por ahora, como no tenemos los ingredientes separados:
                    ingredients_placeholder = "Ver en instrucciones"
    
                    # 3. Llamamos al método pasando los 3 campos obligatorios
                    success = self.db.save_recipe(suggested_title, ingredients_placeholder, ai_recipe)
                        
                    if success:
                        self.view.show_message("Recipe saved in the cloud! 🚀")
                    else:
                        self.view.show_message("Error: Could not save to cloud.")
                        # Manejar esto mas adelante
                
            elif choice == '3':
                self.view.show_message("¡Hasta luego!")
                break
            else:
                self.view.show_message("Opción no válida.")