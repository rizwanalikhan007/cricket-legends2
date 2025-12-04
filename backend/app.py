from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('cricketers.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/search', methods=['GET'])
def search_cricketer():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])

    conn = get_db_connection()
    # Search by name, case-insensitive partial match
    sql = "SELECT * FROM cricketers WHERE name LIKE ?"
    cricketers = conn.execute(sql, ('%' + query + '%',)).fetchall()
    conn.close()

    results = []
    for row in cricketers:
        results.append({
            'id': row['id'],
            'name': row['name'],
            'country': row['country'],
            'role': row['role'],
            'history': row['history'],
            'image_url': row['image_url']
        })
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
