from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)


@app.route('/api/ofers', methods=['GET'])
def get_oferts():
    try:
        client = MongoClient('localhost', 27017)
        db = client.data
        oferts = db.oferts
        data = list(oferts.find({}, {'contents': 0}))
        client.close()

        for d in data:
            d['_id'] = str(d['_id'])

        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/ofers/<string:id>', methods=['GET'])
def get_ofer(id):
    try:
        client = MongoClient('localhost', 27017)
        db = client.data
        ofer = db.oferts
        data = ofer.find_one({'_id': ObjectId(id)})
        client.close()

        if data:
            return jsonify(data.get('contents')), 200
        else:
            return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/api/news', methods=['GET'])
def get_news():
    try:
        client = MongoClient('localhost', 27017)
        db = client.data
        oferts = db.news
        i = request.args.get('i')
        page = request.args.get('p')
        if i:
            data = list(oferts.find().limit(int(i)))
        elif page:
            data = list(oferts.find().skip(int(page) * 9).limit(9))
        else:
            data = list(oferts.find().limit(9))

        for d in data:
            d['_id'] = str(d['_id'])

        client.close()

        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
