import random
import json
import time

# Function to load the keyword-response mapping from a JSON file
def to_load_responses():
    try:
        with open("responses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("responses.json file not found!")
        return []

# Function to save the chat log to a file in different text file 
def log_conversation(log):
    with open("chat_log.txt", "a") as file:
        for entry in log:
            log_entry = f"User ({entry['user']}): {entry['message']}\nAgent ({entry['agent']}): {entry['response']}\n{'-' * 50}\n"
            file.write(log_entry)  # Write to file

# Function  that gives a random disconnections inbetween conversation
def random_disconnect():
    return random.random() < 0.05  # 5% chance of disconnect

# Function to check if the user's input contains required words
def contains_required_words(user_input, required_words):
    user_input = user_input.lower()
    return all(word.lower() in user_input for word in required_words)

# Main function to start the chatbot
def chatbot():
    print("Welcome! Please enter your name:")
    user_name = input("> ")
    print(f"Hello {user_name}! I am Poppleton University Bot, your friendly assistant.")

    # List of possible agent names
    agent_names = ["Geeta", "Shyam", "james", "ram"]
    agent_name = random.choice(agent_names)
    print(f"Your agent today is {agent_name}.")

    # Load responses from JSON file
    responses = to_load_responses()

    if not responses:
        print("No responses loaded, exiting.")
        return

    # Chat log to store the conversation
    chat_log = []

    while True:
        print(f"{user_name}, how can i assist you?")
        user_input = input("> ")

        # Check for exit commands
        if user_input.lower() in ["bye", "quit", "exit"]:
            print(f"Goodbye {user_name}! Have a great day!")
            break

        # Simulate a random disconnection
        if random_disconnect():
            print(f"{agent_name} has disconnected. Please try again later.")
            time.sleep(2)  # Wait a bit before continuing the conversation
            continue

        # Log the user's question
        chat_log.append({"user": user_name, "message": user_input, "agent": agent_name, "response": "..."})

        # Find a matching response from the JSON
        response = None
        for item in responses:
            # Check if any of the user_input words match the user's question
            if any(word.lower() in user_input.lower() for word in item['user_input']):
                if contains_required_words(user_input, item['required_words']):
                    response = item['bot_response']
                    break

        # If no matching response is found, give a random default response
        if response is None:
            response = "I don't understand. Can you clarify little more, or you can visit University website for more details?"

        # Include user's name in some responses
        response = response.replace("{name}", user_name)

        # Log the response
        chat_log[-1]["response"] = response

        print(f"{agent_name}: {response}")

    # Save the chat log to a file (no console output)
    log_conversation(chat_log)

# Main entry point
if __name__ == "__main__":
    chatbot()
