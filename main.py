from controller.app_controller import AppController
from views.console_view import ConsoleView
from models.ai_service import AIService
from models.database import Database

if __name__ == "__main__":
    mi_vista = ConsoleView()
    
    try:
        mi_db = Database() 
        mi_vista.show_message("✅ Database initialized successfully.")
    
        mi_ia = AIService(mi_db)
        app = AppController(model_ai=mi_ia, db=mi_db, view=mi_vista)
        app.run()

    except Exception as e:
        mi_vista.show_message(f"❌ Error during initialization: {e}")
        exit(1)
    
    