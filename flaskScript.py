# network framework
from flask import Flask, jsonify
# including Twitter data obtaining script
import getTrends
app = Flask(__name__)

@app.route("/")
def getTrends():
    getPolarities()

if __name__ == "__main__":
    app.run()
