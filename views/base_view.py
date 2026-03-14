from abc import ABC, abstractmethod

class BaseView(ABC):
    @abstractmethod
    def show_menu(self):
        pass
    @abstractmethod
    def get_user_input(self):
        pass
    
    @abstractmethod
    def display_recipe(self, recipe_data):
        pass

    @abstractmethod
    def show_message(self, message):
        pass