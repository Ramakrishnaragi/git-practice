from flask import Flask
import os

import boto5


>>>>>>> 47ed1c76a49f999356a0083d2b990bcd15daf867
app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask sample application!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
