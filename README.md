# Dictionary

📘 High-End Word Lookup Dictionary
A professional command-line dictionary application built with Python that allows users to instantly search any English word using a free online dictionary API.

This project provides:
Real-time word definitions
Phonetics and pronunciation

Examples
Synonyms and antonyms
Local caching system
Search history tracking
Beautiful terminal UI using Rich

🚀 Features

✅ Real-Time Word Search
Search any English word instantly from a complete online dictionary database.
✅ Beautiful Terminal Interface
Uses the rich library for a professional and colorful UI.
✅ Pronunciation Support
Displays phonetic spelling and audio pronunciation links.
✅ Synonyms & Antonyms
Shows related words for better vocabulary understanding.
✅ Local Cache System
Previously searched words are stored locally for faster future access.
✅ Search History
Every searched word is saved with date and time.
✅ Error Handling
|
|--> Handles:
|--Invalid words
|--Internet connection errors
|--API failures
|--Timeouts

🛠 Technologies Used
-Python 3
-Requests
-Rich
-Free Dictionary API
-API Used:
-Dictionary APIhttps://dictionaryapi.dev

📂 Project Structure
project-folder/
│
├── dictionary.py
├── dictionary_cache.json
├── search_history.txt
└── README.md

⚙ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/high-end-dictionary.git
2️⃣ Open Project Folder
cd high-end-dictionary
3️⃣ Install Required Libraries
pip install requests rich
▶ Running the Application
python dictionary.py

🖥 Example Output

HIGH-END WORD LOOKUP DICTIONARY
Powered by Free Dictionary API

Options:
1. Search a Word
2. View Cached Words
3. Exit

📚 Example Search
Input:
Enter a word to search: innovation
Output Includes:
Definition
Example sentence
Synonyms
Antonyms
Phonetics
Audio pronunciation links

📦 Dependencies
Install manually if needed:
pip install requests
pip install rich

🔒 Cache System
The application automatically stores searched words locally in:
dictionary_cache.json
This improves performance and reduces repeated API calls.

📝 Search History
All searched words are stored in:
search_history.txt

❌ Error Handling
The program handles:
No internet connection
Invalid word search
API server issues
Timeout errors
Empty input

🌟 Future Improvements
Possible future upgrades:
GUI Version using Tkinter or PyQt
Voice pronunciation playback
Multiple language support
Dark/Light themes
Export search history
AI-powered word suggestions

👨‍💻 Author
Developed in Python as a high-end terminal dictionary project.

📜 License
This project is free to use for educational and personal purposes.
