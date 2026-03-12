from controller.app_controller import AppController
from views.console_view import ConsoleView

if __name__ == "__main__":
    mi_vista = ConsoleView()
    app = AppController(mi_vista)
    app.run()