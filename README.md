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

pip install streamlit groq python-dotenv

image image
About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
1
@RasikaSondkar
RasikaSondkar
Languages
Python
100.0%
Suggested workflows
Based on your tech stack
Python application logo
Python application
Create and test a Python application.
SLSA Generic generator logo
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
Django logo
Django
Build and Test a Django Project
More workflows
Footer
