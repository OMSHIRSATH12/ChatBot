import re

# -----------------------------
# RULES: Define your chatbot's responses here
# -----------------------------
rules = {
    r'hi|hello|hey': "Hello! 👋 How can I help you?",
    r'how are you': "I'm just a bot, but I'm doing great! 😊",
    r'what is your name': "I’m CodBot — your friendly chatbot! 🤖",
    r'bye|exit|quit': "Goodbye! Have a nice day! 👋"
}

def chatbot():
    """Main function to run the chatbot."""
    print("Welcome! Type 'bye' or 'quit' to exit.")
    while True:
        user_input = input("You: ").lower().strip()
        matched = False
        
        # Search for matching patterns in the user's input
        for pattern, response in rules.items():
            if re.search(pattern, user_input):
                print(f"Bot: {response}")
                matched = True
                if "goodbye" in response.lower():
                    exit()
                break

        if not matched:
            print("Bot: Sorry, I didn't understand that. 🤷‍♂️")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

