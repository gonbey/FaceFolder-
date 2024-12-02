from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 人物グループのデータ（実際のアプリケーションではデータベースを使用）
person_groups = {}

@app.route('/api/person-groups', methods=['GET'])
def get_person_groups():
    return jsonify(list(person_groups.values()))

@app.route('/api/person-groups', methods=['POST'])
def create_person_group():
    data = request.json
    group_id = len(person_groups) + 1
    person_groups[group_id] = {
        'id': group_id,
        'name': data.get('name', f'Person {group_id}'),
        'faces': []
    }
    return jsonify(person_groups[group_id])

if __name__ == '__main__':
    app.run(debug=True, port=5000) 