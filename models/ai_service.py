import ollama

class AIService:
    
    """
    Service to handle AI interactions using Ollama.
    Acts as an Agent capable of chatting and executing database tools.
    """
    
    def __init__(self, db):
        self.url = "http://localhost:11434/api/generate"
        self.model_name = "llama3.1"
        self.db = db
        
    # Initial system prompt to define the Agent's persona and constraints
        self.chat_history = [
    {
        "role": "system", 
        "content": (
            "Eres un Chef experto y amable. Tu objetivo es dar recetas detalladas.\n"
            "Solo usarás la herramienta 'save_recipe' cuando percibas que el usuario "
            "tiene la intención clara de salvar o guardar la receta actual.\n"
            "Si el usuario solo pregunta o pide cambios, responde con texto normal."
            "Do NOT send technical descriptions like 'type:string'. "
            "Use plain text for ingredients and instructions, one per line."
        )
    }
]
    # Tool definition for Ollama's Function Calling    
        self.tools_definition = [{
            'type': 'function',
            'function': {
                'name': 'save_recipe',
                'description': 'SOLO EJECUTAR SI EL USUARIO DIJO "GUARDA". Guarda la receta confirmada en la base de datos.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'ingredients': {'type': 'string'},
                        'instructions': {'type': 'string'}
                    },
                    'required': ['title', 'ingredients', 'instructions'],
                },
            },
        }]
        
    # Mapping tool names to actual executable methods    
        self.available_functions = {
        "save_recipe": self.db.save_recipe  
            }
            
    def clear_memory(self):
        self.chat_history = [self.chat_history[0]] 
    
    def send_message(self, user_input):
        user_text = user_input.lower()
        self.chat_history.append({"role": "user", "content": user_input})
        
        # --- 1. CHAT MODE ---
        # Disable tools if no saving intent is detected to ensure a more creative/natural response.
        if "guarda" not in user_text and "almacena" not in user_text:
            response = ollama.chat(
                model=self.model_name, 
                messages=self.chat_history
            )
            message = response['message']
            self.chat_history.append(message)
            return message.get('content', '')

        # --- 2. AGENT MODE ---
        # Enable tools so the model can decide if it should call a function.
        response = ollama.chat(
            model=self.model_name, 
            messages=self.chat_history, 
            tools=self.tools_definition
        )
        message = response['message']
        self.chat_history.append(message)

       # Process function calls if the model decides to trigger a tool
        if message.get('tool_calls'):
            for tool in message['tool_calls']:
                function_name = tool['function']['name']
                args = tool['function']['arguments']
                
                if function_name in self.available_functions:
                    
                    # Execute the mapped database function
                    success,db_feedback = self.available_functions[function_name](**args)
                    
                    if success:
                       
                        ingredients = args.get('ingredients', '').replace('\\n', '\n').replace('{', '').replace('}', '').replace('"', '')
                        instructions = args.get('instructions', '').replace('\\n', '\n').replace('{', '').replace('}', '').replace('"', '')

                        return (
                            f"\n✨ {db_feedback.upper()} ✨\n"
                            f"🍴 **Dish:** {args.get('title')}\n\n"
                            f"📝 **Ingredients:**\n{ingredients}\n\n"
                            f"👨‍🍳 **Instructions:**\n{instructions[:150]}..."
                        )

                    else:
                        return f"⚠️ Could not save the recipe. Details: {db_feedback}"

        return message.get('content', "The Chef couldn't process the request.")
    
    
        
