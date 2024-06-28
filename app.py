from flask import Flask, render_template, request, redirect, url_for    
from config import *
import os
import re

app = Flask(__name__)

@app.route('/') 
def index():
    return redirect(url_for('handle_files', subpath="/index.md"))

def get_dir_list(dir):
    try:
        contents = []
        for item in os.listdir(dir):
            print(item)
            if(os.path.isdir(os.path.join(dir,item))):
                contents.append({"type": "folder", "name": item})
            else:
                contents.append({"type": "file", "name": item})
        # for item in contents:
        #     print(item)
        return contents
    except FileNotFoundError:
        return []

def pre_directory(path):
    print(f"matching... path:", path)
    pattern = r'^(.*)/[^/]+$'
    match = re.match(pattern, path)
    if match:
        return match.group(1)
    else:
        return ""  # 如果路径没有匹配到则返回原路径
    

@app.route('/<path:subpath>', methods=['GET', 'POST'])
def handle_files(subpath):
    file_path = os.path.join(FILE_ROOT_DIR, subpath)
    # 或者当前文件所在目录的子目录和文件信息列表
    items = get_dir_list(file_path if os.path.isdir(file_path)  else os.path.dirname(file_path))

    if request.method == 'POST':
        content = request.form['content']
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        return redirect(url_for('handle_files', subpath=subpath))
    
    content = ""
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    else:
        content = f"Select a file to edit"
    my_dir = os.path.dirname(file_path).replace("docs","") if not os.path.isdir(file_path) else subpath
    print(f"this is my_dir: ", my_dir)
    return render_template('index.html', content = content, subpath=subpath, items = items, dir=my_dir, pre_dir=pre_directory(subpath))
if __name__ == '__main__':
    app.run(debug=True)