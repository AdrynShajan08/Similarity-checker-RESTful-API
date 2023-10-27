from flask import Flask, request, jsonify
from utils import calculate_similarity

app = Flask(__name__)

@app.route('/similarity', methods=['POST'])
def similarity():
    data = request.get_json()
    doc1 = data['doc1']
    doc2 = data['doc2']
    similarity_score = calculate_similarity(doc1, doc2)
    return jsonify({'similarity_score': similarity_score})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
