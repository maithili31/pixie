from flask import Flask , render_template, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://mishramaithili2931:JHfG5zNP3U13pOuY@cluster0.0qyvqqb.mongodb.net/pixie"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find()
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html",context = {"myChats":myChats})

@app.route("/api", methods=["GET","POST"])
def qa():

    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat=mongo.db.chats.find_one("question", question)
        data = {"result":f" Answer of {question}"}
        print(chat)
        if chat:
            data = {"result":f"{chat['answer']}"}
        return jsonify(data)
    
    # return render_template("index.html")
    data = {"result":"Greetings! How can I assist you today?"}
    
    return jsonify(data)
    

app.run(debug=True)