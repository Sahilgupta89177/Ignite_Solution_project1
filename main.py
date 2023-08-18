from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'templete/index.html')

@app.route('/hello', methods=['GET'])
def hello_world():
    language = request.args.get('language', 'English')
    if language == 'French':
        return 'Bonjour le monde'
    elif language == 'Hindi':
        return 'Namastey sansar'
    else:
        return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
