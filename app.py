from flask import Flask, request, jsonify

app = Flask(__name__)

def simple_bot(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hello!"
    elif user_input == "how are you":
        return "How can I help you today?"
    else:
        return "I only understand 'hello' and 'how are you'."

@app.route('/chat', methods=['GET'])
def chat():
    user_message = request.args.get('message')
    if not user_message:
        return jsonify({"error": "Please provide a message."}), 400
    
    bot_response = simple_bot(user_message)
    return jsonify({"bot": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
