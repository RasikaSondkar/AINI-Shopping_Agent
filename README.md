🤖 AINI – Smart Shopping Assistant
AINI is an AI-powered shopping assistant that helps users compare electronics products and receive intelligent recommendations through a conversational interface.

The system combines rule-based product comparison with AI reasoning to provide helpful responses.

🚀 Features
Product comparison across multiple stores
AI reasoning using Groq LLM
Conversation memory for contextual responses
Multi-model routing (tool vs AI decision)
Confidence score for responses
Query logging system
Chat-style interface built with Streamlit
🧠 Supported Products
Laptop
Smartphone
Headphones
Smartwatch
🏗️ System Architecture
User Query
↓
Router System (detect query type)
↓
Tool Execution or AI Reasoning
↓
Response Generation
↓
Logging + Confidence Score

📂 Project Structure
AINI_Shopping_Agent │ ├── app.py
├── ai_layer.py
├── router.py
├── logger.py
├── data.py
├── memory.py
├── score.py
├── utils.py
├── logs.json

⚙️ Installation
Clone the repository

git clone https://github.com/yourusername/AINI_Shopping_Agent.git

Navigate to the project folder

cd AINI_Shopping_Agent

Install dependencies

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e1c33a5c-ecc4-401f-a6db-445bcef53a56" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/948ee01f-06a3-4422-89d0-1173e3c87d7e" />



pip install streamlit groq python-dotenv

