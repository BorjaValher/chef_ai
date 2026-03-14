from datetime import datetime
from views.console_view import ConsoleView
from views.base_view import BaseView
from models.ai_service import AIService
from models.database import Database

class AppController:
    def __init__(self, model_ai, db, view):
        self.ai = model_ai
        self.db = db
        self.view = view
        self.db = Database()
        
        
    def run(self):
        while True:
            choice = self.view.show_menu()
            
            if choice == '1':
                try:
                    recipes = self.db.fetch_all()
                    self.view.display_recipes(recipes)
                except Exception as e:
                    self.view.show_message(f"⚠️ {e}")
                
                self.view.wait_for_enter()
                    
            if choice == '2':
                self.view.show_message("\n--- 👨‍🍳 MODE AGENT CHEF ---")
                self.ai.clear_memory()
                
                while True:
                    user_input = self.view.get_user_input()
                    
                    if user_input.lower() in ['salir', 'exit']:
                        break
                    
                    self.view.show_message("👨‍🍳 Thinking...")
                    
                    respuesta = self.ai.send_message(user_input)
                    
                    self.view.show_message(f"\n👨‍🍳 Chef AI: {respuesta}")
                
            elif choice == '3':
                self.view.show_message("Goodbye!")
                break
            else:
                self.view.show_message("Invalid option.")