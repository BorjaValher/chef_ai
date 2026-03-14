# Chef AI - MVC Recipe Generator

A modular Python application that leverages Local LLMs (via Ollama) to generate creative cooking recipes. Built with a clean **Model-View-Controller (MVC)** architecture to ensure scalability and separation of concerns.



![Chef AI MVC Architecture](assets/mvc_diagram.jpg)


## 🚀 Features

- **Agentic AI Intelligence:** Uses Llama 3.1 with **Tool Calling** capabilities. The AI doesn't just chat; it decides when to structure and save recipes to the database.
- **MVC Architecture:** Strict separation of concerns, making the code modular, testable, and scalable.
- **Cloud Storage:** Integrated with Supabase API (HTTPS) for reliable data persistence, bypassing common database port restrictions.
- **Local & Private:** AI processing happens locally on your machine.
- **Robust Architecture:** Uses Abstract Base Classes (ABC) for the View layer, allowing for easy transitions between CLI and GUI in the future.
- **Error Resilience:** Professional error handling with state-feedback between Database, Agent, and UI.

## 🛠️ Architecture

The project follows the **MVC** pattern:
- **Models:** Handles business logic, AI API communication (Ollama), and data structures.
- **Views:** Manages user interaction via an abstract interface (BaseView) implemented for the console.
- **Controllers:** Orchestrates the flow between user inputs, AI responses, and database updates.

## 📋 Prerequisites

1. **Python 3.9+**
2. **Ollama:** [Download Ollama here](https://ollama.com/)
3. **Llama3 Model:** Pull the model before running the app:
   ```bash
   ollama pull llama3.1
4. **Supabase Account:** A project with a "recipes" table

## 📦 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
2. **Install required libraries:**
   ```bash
   pip install supabase python-dotenv
   
3. **Environment Configuration:**
Create a .env file in the root directory and fill in your Supabase credentials:
   ```bash
   SUPABASE_URL=[https://your-project-id.supabase.co](https://your-project-id.supabase.co)
   SUPABASE_KEY=your-anon-public-key