from .base_view import BaseView

class ConsoleView:
    def show_menu(self):
        print("\n--- AI RECIPE APPLICATION ---")
        print("1. Browse Database Recipes")
        print("2. Create New Recipe with AI")
        print("3. Exit")
        return input("Select an option: ")
    
    def display_recipes(self, recipes):
        """Displays a list of recipe dictionaries formatted for the console."""
        if not recipes:
            print("\nNo recipes found yet.")
            return

        print("\n--- My Saved Recipes ---")
        for idx, r in enumerate(recipes, 1):
            print(f"\n{idx}. 📖 TITLE: {r['title']}")
            print(f"   🧂 INGREDIENTS: {r['ingredients']}")
            print(f"   📝 INSTRUCTIONS: {r['instructions']}...")
            print("-" * 30)
            
    def get_user_input(self, prompt="\n👤 You: "):
        """Centralizes input gathering."""
        return input(prompt)
    

    def display_recipe(self, recipe_text):
        print("\n--- RECIPE ---")
        print(recipe_text)
        print("--------------")

    def show_message(self, message):
        print(f"\n[!] {message}")
        
    def wait_for_enter(self):
        input("\nPress enter to continue...")
        