class ConsoleView:
    def show_menu(self):
        print("\n--- APLICACIÓN DE RECETAS CON IA ---")
        print("1. Buscar receta en la Base de Datos")
        print("2. Inventar receta con IA (Ollama)")
        print("3. Salir")
        return input("Elige una opción: ")
    
    def get_ingredients_input(self):
        return input("Introduce los ingredientes que tienes (separados por coma): ")

    def display_recipe(self, recipe_text):
        print("\n--- RECETA ---")
        print(recipe_text)
        print("--------------")

    def show_message(self, message):
        print(f"\n[!] {message}")