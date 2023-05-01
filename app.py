import hashlib
from flask import Flask, request, render_template

app = Flask(__name__)

def compute_hash(data):
    data = data.encode('utf-8')
    block_hash = hashlib.sha256(data).hexdigest()
    return block_hash

def compute_file_hash(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        file_hash = hashlib.sha256(data).hexdigest()
    return file_hash

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            filename = file.filename
            file.save(filename)
            file_hash = compute_file_hash(filename)
            return render_template('index.html', filename=filename, file_hash=file_hash)
        else:
            data = request.form['text']
            block_hash = compute_hash(data)
            return render_template('index.html', text=data, block_hash=block_hash)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



# pip install flask and pip must be updated with python version3