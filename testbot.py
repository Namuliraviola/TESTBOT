def simple_bot():
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hello!")
        user_input = input("You: ").lower()

        if user_input == "how are you":
            print("Bot: How can I help you today?")
        else:
            print("Bot: I only understand 'how are you' after 'hello'.")
    else:
        print("Bot: I only respond to 'hello'.")

simple_bot()
