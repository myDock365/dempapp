from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/extract', methods=['POST'])
def home():
    exception = "First";
    try:
        data = json.loads(request.data)
        model = data["model"]
        document = data["doc"]
        exception = "Got data"
        trainer = Trainer()
        exception = "Got data 1"
        entities = trainer.extract_entities(document, model)
        exception = "Got data 2"
        filtered_entities = Trainer.convert_result(entities.ents)
        exception = "Got data 3"
        return jsonify(filtered_entities)
    except:
        return exception
