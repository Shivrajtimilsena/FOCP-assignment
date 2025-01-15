POPPLETON UNIVERSITY CHATBOT

The Poppleton University Chatbot is a simple Python-based conversational assistant designed to help prospective students interact with the university.
The chatbot responds to user queries based on predefined responses stored in a JSON file. 
It can also handle random or fallback responses for unrecognized queries.

FEATURES

1) JSON-Driven Responses: Responses and keywords are stored in an external JSON file for easy customization.

2) Dynamic Keyword Matching: The chatbot identifies keywords and required words in user input to provide accurate responses.

3) Random Fallback Responses: If no suitable response is found, the chatbot provides a random fallback response.

4) Exit Commands: Users can exit the chat by typing "exit" or "quit."

5) Error Handling: The program handles missing or invalid JSON files gracefully.

6) Type "exit" or "quit" to end the conversation.


CODE STRUCTURE

1) main.py = the main python script containing the chatbot logic

2) resposes.json = The JSON file has some predefined responses with keywords.


TROUBLESHOOTING

1) File Not Found: Ensure responses.json exists in the same directory main.py

2) Empty Responses: Verify the JSON file has valid responses and matches the required structure.

3) Python Errors: Ensure you are using Python 3.7 or higher and that all modules (e.g., json, re, random) are available.

*NOTES*
There is a Chat log in "chat_log.txt" file which record the conversation history of every users.
