class Database:
    def __init__(self, db_name=None):
        print(f"[DEBUG] Base de datos '{db_name}' inicializada (Modo Simulación)")

    def save_recipe(self, title, ingredients, instructions):
        print(f"[DEBUG] Guardando en el vacío: {title}")
        return 1

    def get_all_recipes(self):
        print("[DEBUG] Consultando recetas... (No hay nada aún)")
        return []