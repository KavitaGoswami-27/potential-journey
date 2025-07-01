from flask import Flask, render_template, request, jsonify
from sort_selector import intelligent_sort

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sort", methods=["POST"])
def sort():
    data = request.get_json()
    input_list = data.get("input")
    result = intelligent_sort(input_list)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)