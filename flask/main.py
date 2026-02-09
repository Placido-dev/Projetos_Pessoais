from flask import Flask, make_response, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def get():
    return make_response(
        jsonify(
            mensagem='Lista de users.'
        )
    )

if __name__ == '__main__':
    app.run()