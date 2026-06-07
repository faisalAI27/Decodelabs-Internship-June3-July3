# Project 1: Rule-Based AI Chatbot
# Batch 2026 | DecodeLabs
# This chatbot uses predefined rules, if-else logic, dictionary lookup,
# input sanitization, and a continuous loop.

import string


BOT_NAME = "DecodeBot"

# Exit commands
EXIT_COMMANDS = ["bye", "exit", "quit", "stop"]

# Predefined responses using dictionary/hash map
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! How are you doing?",
    "good morning": "Good morning! I hope you have a productive day.",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! How was your day?",
    "how are you": "I am doing great. Thanks for asking!",
    "what is your name": f"My name is {BOT_NAME}. I am a rule-based AI chatbot.",
    "who are you": f"I am {BOT_NAME}, a simple chatbot built using Python rules.",
    "who made you": "I was created by an AI engineering intern as part of Project 1.",
    "what can you do": "I can respond to predefined questions, greetings, and exit commands.",
    "help": "You can ask me things like 'hello', 'what is your name', 'what is ai', or type 'bye' to exit.",
    "thank you": "You are welcome!",
    "thanks": "No problem! Happy to help.",
    "bye": "Goodbye! Have a great day.",
    "exit": "Goodbye! Exiting the chatbot now.",
    "quit": "Goodbye! See you again.",
    "stop": "Okay, stopping the chatbot."
}


def clean_user_input(user_input):
    """
    This function cleans the user's input.
    Example:
    '  HELLO!!!  ' becomes 'hello'
    """

    # Convert input to lowercase
    user_input = user_input.lower()

    # Remove extra spaces from start and end
    user_input = user_input.strip()

    # Remove punctuation like ?, !, .
    user_input = user_input.translate(str.maketrans("", "", string.punctuation))

    return user_input


def get_bot_response(clean_input):
    """
    This function decides what response the chatbot should give.
    It uses if-else logic and dictionary lookup.
    """

    # First check exact predefined responses
    if clean_input in responses:
        return responses[clean_input]

    # Keyword-based nested conditions for smarter responses
    elif "ai" in clean_input or "artificial intelligence" in clean_input:
        return "AI means making machines perform tasks that normally require human intelligence."

    elif "python" in clean_input:
        return "Python is a popular programming language used in AI, automation, and data science."

    elif "machine learning" in clean_input:
        return "Machine learning is a part of AI where machines learn patterns from data."

    elif "deep learning" in clean_input:
        return "Deep learning uses neural networks to solve complex problems like image recognition and language understanding."

    elif "project" in clean_input:
        return "This project is about building a rule-based AI chatbot using Python control flow."

    elif "internship" in clean_input:
        return "Internships are a great way to gain practical experience and improve your skills."

    elif "your purpose" in clean_input:
        return "My purpose is to demonstrate how rule-based AI works using simple programming logic."

    # Fallback response if chatbot does not understand
    else:
        return "Sorry, I do not understand that. Type 'help' to see what you can ask."


def run_chatbot():
    """
    Main function that runs the chatbot continuously.
    """

    print("=" * 50)
    print(f"{BOT_NAME}: Hello! I am your Rule-Based AI Chatbot.")
    print(f"{BOT_NAME}: Type 'help' to see what you can ask.")
    print(f"{BOT_NAME}: Type 'bye', 'exit', 'quit', or 'stop' to end the chat.")
    print("=" * 50)

    while True:
        # Take user input
        user_input = input("You: ")

        # Clean the input
        clean_input = clean_user_input(user_input)

        # Handle empty input
        if clean_input == "":
            print(f"{BOT_NAME}: Please type something.")
            continue

        # Get chatbot response
        response = get_bot_response(clean_input)

        # Print chatbot response
        print(f"{BOT_NAME}: {response}")

        # Exit condition
        if clean_input in EXIT_COMMANDS:
            break


# Start the chatbot
run_chatbot()