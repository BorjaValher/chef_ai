from views.console_view import ConsoleView
from models.ai_service import AIService

class AppController:
    def __init__(self):
        self.view = ConsoleView()
        self.ai = AIService(model_name="llama3.1")
        
    def run(self):
        while True:
            choice = self.view.show_menu()
            
            if choice == '1':
                self.view.show_message("Función de BD en construcción...")
                
            elif choice == '2':
                ingredients = self.view.get_ingredients_input()
                self.view.show_message("Consultando a Ollama, espera un momento...")
                
                ai_recipe = self.ai.generate_recipe_idea(ingredients)
                
                self.view.display_recipe(ai_recipe)
                
            elif choice == '3':
                self.view.show_message("¡Hasta luego!")
                break
            else:
                self.view.show_message("Opción no válida.")