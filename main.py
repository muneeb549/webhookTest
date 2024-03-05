from flask import Flask, request

app = Flask(__name__)

app.route("/webhook", methods=["POST"])
def hook():
    print(request.json)
    return "success"


if __name__ == "__main__":
    app.run()
