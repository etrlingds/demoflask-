from flask import Flask, request
from flask_cors import CORS
import poe
import random

app = Flask(__name__)
CORS(app)
# "MapZ1hFIM76nH7v9F8QdXg%3D%3D", "wqxFkA5k-MdmkgYS7QYGdQ%3D%3D", "IEZxMFpuIVGTlD3m3gkcaw%3D%3D", ["6RI6NsCkv9MD49f5YsRIkg%3D%3D", "LnTckboQ91ohf1r89ttlEw%3D%3D" ,
TOKENS =  ["LYPYy4iSLUe7a_Cfyhfx3Q%3D%3D"]

# Replace with the desired model ID
MODEL_ID = "capybara"

@app.route("/send_message", methods=["POST"])
def send_message():
    # Get the message from the request body
    data = request.get_json()
    message = data["message"]

    # Randomly select a token from the list of tokens
    token = random.choice(TOKENS)

    # Set up the POE API client
    client = poe.Client(token)

    # Send the message and get the response
    response_text = ""
    for chunk in client.send_message(MODEL_ID, message):
        response_text += chunk["text_new"]

    return response_text

if __name__ == "__main__":
    app.run(port=8000)
