from flask import Flask, jsonify, request

app = Flask(__name__)

# route
@app.route('/')
def hello():
    name_params = request.args.get("name")
    return jsonify(data=f"Hello From Flask Api {name_params}")
