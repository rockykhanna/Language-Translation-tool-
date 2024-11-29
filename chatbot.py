import nltk
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by ChatGPT. You can call me Assistant!",]
    ],
    [
        r"how are you ?",
        ["I'm just a program, but I'm here to help you!",]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, provide information, answer questions, and much more!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you. Have a great day!"]
    ],
    # Add more patterns and responses as needed
]

# Create a chatbot instance
def chatbot():
    print("Hello! I am your friendly chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot
if "_name_" == "_main_":
    chatbot()