
rules = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am a chatbot created to assist you.",
    "bye": "Goodbye! Have a nice day!",
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
    "help": "Sure, I'm here to help! What do you need assistance with?",
    "what can you do": "I can answer your questions and provide information based on predefined rules.",
    
}


def chatbot_response(user_input):
    user_input = user_input.lower()  
    for key in rules:
        if key in user_input:
            return rules[key]
    return "I'm sorry, I don't understand that."


def main():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
