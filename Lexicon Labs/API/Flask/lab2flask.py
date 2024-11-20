from flask import Flask, request, jsonify, render_template

'''
API Endpoint:
Create a simple RESTful API using Flask. Implement endpoints for GET, POST, and DELETE operations on a resource (e.g., a list of tasks).
'''

app = Flask(__name__)

@app.route('/')
def home():
        return "Hello World"

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
        if request.method == 'GET':
                data = {"message":"This is a GET request", "content": None}
                return jsonify(data)
        elif request.method == 'POST':
                content = request.json
                return jsonify({"message":"Recieved your data!", "yourContent": content})
        
# Put and Patch
@app.route('/api/update/<int:item_id>', methods=['PUT', 'PATCH'])
def update_item(item_id):
        content = request.json
        if request.method == 'PUT':
                return jsonify({"message":"Item updated with new data", "itemID": item_id, "newData": content})
        
        elif request.method == 'PATCH':
                return jsonify({"message":"Item partially updated", "itemID": item_id, "updatedData": content})

@app.route('/form', methods=['GET', 'POST'])
def form():
        if request.method == 'POST':
                name = request.form.get(['firstName', 'lastName'], 'GUEST')
                return render_template('greet.html', name=name)
        
        return render_template('form.html')

if __name__ == '__main__' :
        app.run(debug=True)
        
'''
@app.route('/tasks', methods=['GET'])
def get_tasks():
        #TODO

@app.route('/tasks', methods=['POST'])
def add_task():
        #TODO
    
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
        #TODO
    
if __name__ == '__main__':
    app.run(debug=True)
'''

