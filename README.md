# Chef AI - MVC Recipe Generator

A modular Python application that leverages Local LLMs (via Ollama) to generate creative cooking recipes. Built with a clean **Model-View-Controller (MVC)** architecture to ensure scalability and separation of concerns.



[Image of MVC software architecture pattern diagram]


## 🚀 Features

- **AI-Powered Recipes:** Uses Ollama and Llama3.1 to generate recipes based on user-provided ingredients.
- **Surprise Mode:** Let the AI decide the menu with a random recipe generation.
- **Cloud Storage:** Integrated with Supabase API (HTTPS) for reliable data persistence, bypassing common database port restrictions.
- **Local & Private:** AI processing happens locally on your machine.
- **Robust Architecture:** Uses Abstract Base Classes (ABC) for the View layer, allowing for easy transitions between CLI and GUI in the future.
- **Environment Safety:** Secure credential management using .env files.

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
📦 Installation & Setup
1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd chef_ai
2. **Install required libraries:**
```bash
pip install supabase python-dotenv
3. **Environment Configuration:**
Create a .env file in the root directory and fill in your Supabase credentials:
```bash
SUPABASE_URL=[https://your-project-id.supabase.co](https://your-project-id.supabase.co)
SUPABASE_KEY=your-anon-public-key