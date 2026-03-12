from abc import ABC, abstractmethod

class BaseView(ABC):
    @abstractmethod
    def show_menu(self):
        """Muestra el menú principal y retorna la opción elegida."""
        pass

    @abstractmethod
    def get_ingredients_input(self):
        """Pide al usuario los ingredientes."""
        pass

    @abstractmethod
    def display_recipe(self, recipe_data):
        """Muestra la receta (ya sea un dict o un string)."""
        pass

    @abstractmethod
    def show_message(self, message):
        """Muestra un mensaje informativo o de error."""
        pass