from flask import Flask, render_template, request, redirect, url_for    
from config import *
import os

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/<path:subpath>', methods=['GET', 'POST'])
def init_content(subpath):
    file_path = os.path.join(FILE_ROOT_DIR, subpath)

    if request.method == 'POST':
        content = request.form['content']
        content = content.replace('\r\n', '\n').replace('\r', '\n')

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return redirect(url_for('init_content', subpath=subpath))
    
    if os.path.exists(file_path):
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    else:
        content = f"Not a file or it's a dir: {file_path}"
    return render_template('index.html', content = content, subpath=subpath)
if __name__ == '__main__':
    app.run(debug=True)