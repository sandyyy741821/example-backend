from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
#CORS(app, origins=["https://example.com", "https://sub.example.com"], supports_credentials=True)

CORS(app, resources={r"/api": {"origins": "https://sub.example.com"}})  

# @app.route('/api', methods=['GET'])
# def api():
#     return jsonify({"message": "Hello from sub.example.com!"})

@app.route('/api', methods=['POST'])
def greet_user():
    data = request.get_json()  
    name = data.get('name', '')  
    if name:
        response_message = f"Hello {name}, how can I help you?"
    else:
        response_message = "Hello, how can I help you?"
    
    return jsonify({"message": response_message})

if __name__ == "__main__":
    app.run(
        host='sub.example.com', 
        port=5000,
        ssl_context=('example.com+2-cert.pem', 'example.com+2-key.pem')
    )
