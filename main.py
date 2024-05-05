from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/oferts', methods=['GET'])
def get_oferts():
    try:
        client = MongoClient('localhost', 27017)
        db = client.data
        oferts = db.oferts
        data = list(oferts.find({}, {'_id': 0}))
        client.close()

        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/news', methods=['GET'])
def get_news():
    try:
        client = MongoClient('localhost', 27017)
        db = client.data
        oferts = db.news
        i = request.args.get('i')
        page = request.args.get('p')
        if i:
            data = list(oferts.find({}, {'_id': 0}).limit(int(i)))
        elif page:
            data = list(oferts.find({}, {'_id': 0}).skip(int(page)*9).limit(9))
        else:
            data = list(oferts.find({}, {'_id': 0}))

        client.close()

        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
