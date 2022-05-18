from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/extract', methods=['POST'])
def home():
    data = json.loads(request.data)
    model = data["model"]
    document = data["doc"]

    trainer = Trainer()
    entities = trainer.extract_entities(document, model)
    filtered_entities = Trainer.convert_result(entities.ents)
    return jsonify(filtered_entities)
