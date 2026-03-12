# Chef AI - MVC Recipe Generator

A modular Python application that leverages Local LLMs (via Ollama) to generate creative cooking recipes. Built with a clean **Model-View-Controller (MVC)** architecture to ensure scalability and separation of concerns.



[Image of MVC software architecture pattern diagram]


## 🚀 Features

- **AI-Powered Recipes:** Uses Ollama and Llama3 to generate recipes based on user-provided ingredients.
- **Surprise Mode:** Let the AI decide the menu with a random recipe generation.
- **Local & Private:** No API keys required. Everything runs locally on your machine.
- **Structured Data:** Configured to handle AI responses in JSON format for future database integration.

## 🛠️ Architecture

The project follows the **MVC** pattern:
- **Models:** Handles business logic, AI API communication (Ollama), and data structures.
- **Views:** Manages the Command Line Interface (CLI) and user interactions.
- **Controllers:** Orchestrates the flow between the user input and the AI service.

## 📋 Prerequisites

1. **Python 3.9+**
2. **Ollama:** [Download Ollama here](https://ollama.com/)
3. **Llama3 Model:** Pull the model before running the app:
   ```bash
   ollama pull llama3