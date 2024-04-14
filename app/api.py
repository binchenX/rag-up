from flask import Flask, jsonify, request, redirect
import requests
from urllib.parse import urljoin
from flask_cors import CORS
import logging
import sys
from model import init_index
from model import init_conversation
from model import chat
from config import *

app = Flask(__name__)
CORS(app)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@app.route("/api/question", methods=["POST"])
def post_question():
    json = request.get_json(silent=True)
    question = json["question"]
    logging.info("post question `%s`", question)

    resp = chat(question)
    data = {"answer": resp}

    return jsonify(data), 200


@app.route("/api/chat", methods=["POST"])
def generate_answer():
    """
    Process a POST request with a question and return the answer.

    The API is compatible with ollman's API, but only respect "prompt" field.
    This endpoint is created so that it works with the open-webui.

    only messages[1].content is used as a question. all other fields are ignored..

    curl http://localhost:11434/api/chat -d '{
     "model": "llama2",
     "messages": [
        {
      "role": "user",
      "content": "why is the sky blue?"
        }
        ],
     "stream": false
    }'

    https://github.com/ollama/ollama/blob/main/docs/api.md

    Returns:
        A JSON response containing the answer.
    """
    json = request.get_json(silent=True)
    question = json["messages"][0]["content"]
    logging.info("post question `%s`", question)

    resp = chat(question)
    data = {"response": resp}

    return jsonify(data), 200


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>", methods=["GET", "POST"])
def catch_all(path):
    """
    For all the GET and POST request other than GET /api/question, forward the request to the model and return the response.

    Args:
        path (str): The path of the request.

    Returns:
        tuple: A tuple containing the response content, status code, and headers.
    """
    if request.path != "/api/question" or request.method != "POST":
        # Forward the request to the model and get the response
        response = requests.request(
            method=request.method,
            url=urljoin(MODEL_URL, request.path),
            headers=request.headers,
            data=request.get_data(),
            params=request.args,
            cookies=request.cookies,
            allow_redirects=False,
        )

        # Return the response from the model
        return (response.content, response.status_code, response.headers.items())
    else:
        return post_question()


if __name__ == "__main__":
    init_index()
    init_conversation()
    app.run(host="0.0.0.0", port=HTTP_PORT, debug=True)
