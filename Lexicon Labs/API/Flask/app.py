from flask import Flask, request, jsonify, render_template, redirect
import os, json
from datetime import datetime

app = Flask(__name__)

'''
Basic Routing:
Create a Flask application with three routes:
Route 1: Display a welcome message on the home page.
Route 2: Display information about yourself on a separate page.
Route 3: Create a custom 404 error page.
'''
@app.route('/', methods=['GET'])
def home():
        return render_template('welcome.html')
@app.route('/about', methods=['GET'])
def about():
        return render_template('me.html')

@app.errorhandler(404)
def page_not_found(e):
        return render_template('error404.html')

'''
Form Handling:
Create a form with Flask that takes user input (e.g., name, email) and 
displays it on a new page after submission.
'''

@app.route('/form', methods=['GET', 'POST'])
def form():
        if request.method == 'POST':
            firstName = request.form.get('firstName')
            lastName = request.form.get('lastName')
            return render_template('greet.html', firstName=firstName, lastName=lastName)
        return render_template('form.html')

'''
File Upload:
Create a Flask route that allows users to upload files. Save the uploaded files on the server 
and display a list of uploaded files on another page.
'''

@app.route('/uploadbook', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        for i in range(len(request.files)):
            uploaded_file = request.files[f'file{i+1}']
            destination  = os.path.join('uploads/', uploaded_file.filename)
            uploaded_file.save(destination)
        return render_template('showuploads.html', list=os.listdir('./uploads'))
    return render_template('uploadbook.html')

@app.route('/showuploads', methods = ['GET']) 
def show_uploads():
    return render_template('showuploads.html', list=os.listdir('./uploads'))

@app.route('/uploads', methods=['GET'])
def showDirectory():
    list = os.listdir('./uploads')
    data = {"message":"This is a GET request", "content": list}
    return jsonify(data)



# Delete file through restAPI:

@app.route('/uploads/<string:file_name>/delete', methods=['DELETE'])
def delete_file1(file_name):
    if file_name not in os.listdir('./uploads'):
        return render_template('error404.html')
    deleted_file = file_name
    os.remove(f'./uploads/{file_name}')
    list = os.listdir('./uploads')
    data = {"message":"This is a DELETE request", "file_name": file_name ,"content": list, "headers": str(request.headers)}
    return jsonify(data)

# Delete file from website:

@app.route('/uploads/<string:file_name>', methods=['GET','DELETE'])
def delete_file(file_name):
    if file_name not in os.listdir('./uploads'):
        return render_template('error404.html')
    os.remove(f'./uploads/{file_name}')
    list = os.listdir('./uploads')
    return redirect('/showuploads')

'''
API Endpoint:
Create a simple RESTful API using Flask. Implement endpoints for GET, POST, and DELETE operations 
on a resource (e.g., a list of tasks).
'''
# Tasklist management through website:

def read_json(file_name) :
    with open(file_name, 'r+', encoding='utf-8') as file:
         file_contents = json.load(file)
         return file_contents
    
def write_json(file_name, contents):
    with open(file_name, 'w', encoding='utf-8') as file:
        updated_contens = json.dumps(contents, indent=4)
        file.write(updated_contens)

def single_task_json(dict, field_id):
    dirname = os.getcwd()
    filename = os.path.join(dirname + '/tasks/', f'{dict[field_id]}')
    with open(filename,'w') as file:
        json.dump(dict, file, indent = 4)

@app.route('/tasklist', methods=['GET', 'POST'])
def add_task():
    tasks = read_json('tasks.json')
    if request.method == 'POST':
        id = len(tasks["Tasks"])+1
        now = datetime.now()
        content = request.form.get('content')

        new_task = {"task_id":f"{id}",
        "content": f"{content}",
        "date_time": f"{now}"
        }
        #single_task_json(new_task, "task_id")
        tasks["Tasks"].append(new_task)
        write_json('tasks.json', tasks)
        return redirect('/tasklist')
    return render_template('tasklist.html', tasks= tasks["Tasks"])
 
@app.route('/tasks/<int:task_id>/edit', methods=['GET','POST'])
def update_task(task_id):
    tasks = read_json('tasks.json')
    if request.method == 'POST':
        now = datetime.now()
        new_content = request.form.get('new-content')
        tasks["Tasks"][task_id-1]["content"]= new_content
        tasks["Tasks"][task_id-1]["date_time"]= f"{now}"
        write_json('tasks.json', tasks)
        return redirect('/tasklist')
    return update(task_id, tasks["Tasks"][task_id-1]["content"])


@app.route('/edittask/<int:task_id>&<string:content>', methods = ['GET']) 
def update(task_id, content):
    return render_template('edittask.html', task_id = task_id, content = content )

@app.route('/tasks/<int:task_id>', methods=['GET', 'DELETE'])
def delete_task(task_id):
    '''
    os.remove(f'./tasks/{task_id}')
    integer=1
    for file_name in sorted(os.listdir('./tasks')):
        content = read_json(f'./tasks/{file_name}')
        content["task_id"] = integer
        write_json(f'./tasks/{file_name}', content)

        os.rename(f'./tasks/{file_name}', f'./tasks/{integer}')
        integer = integer + 1
    '''    
    tasks = read_json('tasks.json')
    del tasks["Tasks"][task_id-1]
    integer = 1
    for task in tasks["Tasks"]:
         task["task_id"]= integer
         integer = integer + 1
    write_json('tasks.json', tasks)
    return redirect('/tasklist')

# Tasklist management through restAPI:

@app.route('/addtask', methods=['POST'])
def restAPI_add_task():
    tasks = read_json('tasks.json')
    last_task_id = len(tasks["Tasks"])
    now = datetime.now()
    posted_tasks = []

    for content in request.form.getlist('content'):
        task_id = last_task_id + 1
        last_task_id = last_task_id + 1
        
        new_task = {"task_id":f"{task_id}","content": f"{content}","date_time": f"{now}"}
        posted_tasks.append(new_task)
        tasks["Tasks"].append(new_task)

    write_json('tasks.json', tasks)
    return jsonify({"message":"This is an POST request", "new_tasks": posted_tasks})


@app.route('/tasks/<int:task_id>/edit', methods=['PATCH'])
def restAPI_update_task(task_id):
    tasks = read_json('tasks.json')
    now = datetime.now()
    new_content = request.form.get('content')
    tasks["Tasks"][task_id-1]["content"]= new_content
    tasks["Tasks"][task_id-1]["date_time"]= f"{now}"
    write_json('tasks.json', tasks)
    return jsonify({"message":"This is an PATCH request", "task_id": task_id, "new_content": new_content, "date_time":now})

@app.route('/tasks/<int:task_id>/delete', methods=['DELETE'])
def restAPI_delete_task(task_id):
    tasks = read_json('tasks.json')
    delete_task = tasks["Tasks"][task_id-1]
    del tasks["Tasks"][task_id-1]
    integer = 1
    for task in tasks["Tasks"]:
         task["task_id"]= integer
         integer = integer + 1
    write_json('tasks.json', tasks)
    return jsonify({"message":"This is an DELETE request", "task_id": task_id, "content": delete_task["content"], "date_time": delete_task["date_time"]})


if __name__ == '__main__' :
    app.run(debug=True)
