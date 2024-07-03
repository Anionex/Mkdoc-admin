# https://github.com/Anionex/Mkdoc-admin
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
from config import *
import os
import re
join = os.path.join

app = Flask(__name__)

@app.route('/') 
def index():
    return redirect(url_for('handle_files', subpath="/index.md"))

def get_dir_list(dir):
    try:
        contents = []
        for item in os.listdir(dir):
            print(item)
            if(os.path.isdir(os.path.join(dir,item))):  # 别忘记join，否则会导致isdir失效
                contents.append({"type": "folder", "name": item})
            else:
                # contents.append({"type": "file", "name": item})
                # show only .md and
                if item.endswith(".md"):
                    contents.append({"type": "file", "name": item})
        # for item in contents:
        #     print(item)
        return contents
    except FileNotFoundError:
        return []
    
# 功能： 返回上一级目录
def pre_directory(path):
    # 如果路径为空，返回当前目录的父目录
    if not path:
        return ""

    # 标准化路径，去掉末尾的斜杠并解析相对路径
    normalized_path = os.path.normpath(path)

    # 如果路径是一个文件，则获取其所在目录
    if os.path.isfile(os.path.join(FILE_ROOT_DIR, normalized_path)):
        normalized_path = os.path.dirname(normalized_path)
        
    # 获取父目录
    parent_dir = os.path.dirname(normalized_path)

    # 返回父目录
    print(f"now_dir and pre_dir: {path}, {parent_dir}")
    return os.path.normpath(parent_dir).replace("\\", "/")
    

def get_js_file_list(dir):
    try:
        js_files = []
        # print(dir)
        # print(os.listdir(dir))
        for item in os.listdir(dir):
            if item.endswith(".js"):
                with open(os.path.join(dir, item), "r", encoding="utf-8") as f:
                    js_files.append({"name": item, "content": f.read()})
        return js_files
    except FileNotFoundError:
        return []  

@app.route('/<path:subpath>', methods=['GET', 'POST'])
def handle_files(subpath):
    subpath = os.path.normpath(subpath)
    file_path = os.path.join(FILE_ROOT_DIR, subpath)

    if not file_path.startswith(FILE_ROOT_DIR):
        return "Invalid path", 400

    items = get_dir_list(file_path if os.path.isdir(file_path) else os.path.dirname(file_path))

    if request.method == 'POST':
        content = request.form['content']
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        return redirect(url_for('handle_files', subpath=subpath))
    
    content = ""
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "Select a file to edit"

    my_dir = (os.path.dirname(subpath)) if not os.path.isdir(file_path) else subpath
    my_dir = my_dir.replace('\\','/')
    return render_template('index.html', js_file_list=get_js_file_list(JS_DIR), content=content, subpath=subpath, items=items, dir=my_dir, pre_dir=pre_directory(subpath))

# fixme: file add to previous dir, but sometimes add correctly
@app.route('/<path:subpath>/add_file', methods=['POST'])
def add_file(subpath):
    file_path = os.path.join(FILE_ROOT_DIR, subpath) # 文件或目录的绝对路径
    relative_dir = (os.path.dirname(file_path)).replace(FILE_ROOT_DIR, "") if not os.path.isdir(file_path) else subpath
    abs_dir = join(FILE_ROOT_DIR, relative_dir)
    
    # default .md file
    content = request.form['content']
    # review: regex
    filename = content + '.md' if not re.search(r'\.[a-zA-Z0-9]+$', content) else content

    abs_new_file_path = join(abs_dir, filename)
    relative_new_file_path = join(relative_dir, filename)

    if os.path.exists(abs_dir) and not os.path.exists(abs_new_file_path):
        with open(abs_new_file_path, "w", encoding="utf-8") as f:
            print(" ", file=f)
    print("new file path is ", relative_new_file_path)

    return redirect(url_for('handle_files', subpath=relative_new_file_path))


@app.route('/<path:subpath>/delete_file', methods=['POST'])
def delete_file(subpath):
    relative_file_path = request.form['filePath']
    abs_file_path = join(FILE_ROOT_DIR, relative_file_path.lstrip('/'))
    relative_dir = (os.path.dirname(abs_file_path)).replace(FILE_ROOT_DIR, "") if not os.path.isdir(abs_file_path) else subpath
    print(f'{abs_file_path} has not been deleted successfully.')
    if os.path.exists(abs_file_path) and not os.path.isdir(abs_file_path):
        os.remove(abs_file_path)
        print(f'{relative_file_path} has been deleted successfully.')
    return redirect(url_for('handle_files', subpath=relative_dir))
import json
@app.route('/api/get_some_data', methods=['GET'])
@cross_origin()
def get_json_file():
    # 创建一个示例数据字典
    data = {
        "to": "Tove",
        "from": "Jani",
        "heading": "Reminder",
        "body": "Don't forget me this weekend!"
    }

    
    # 返回JSON响应
    return jsonify(data)

@app.route('/api/save_current_file', methods=['POST'])  # 涉及到服务器上内容的更改，所以使用post
@cross_origin()
def save_current_file():
    """
    保存当前文件内容的接口

    请求方法:
        POST

    请求参数:
        - rel_file_path (str): 文件的相对路径
        - content (str): 要保存的文件内容

    返回:
        JSON 响应，包含操作的状态和消息
    """
    data = request.json
    print("data: ", data)
    rel_file_path = str(data.get('rel_file_path'))
    content = data.get('content')
    print(f"rel_file_path: {rel_file_path}")
    # 运用今天学到的防御性编程的技巧, 增加程序的健壮性
    
    abs_file_path = os.path.join(FILE_ROOT_DIR, rel_file_path.strip('/'))
    print(f"abs_file_path: {abs_file_path}")
    if os.path.exists(abs_file_path) and os.path.isfile(abs_file_path):
        with open(abs_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("file has been saved")
        
        response = {
            "status": "success",
            "message": "File saved successfully"
        }
        
        return jsonify(response)
    else:
        response = {
            "status": "failed",
            "message": "filed to save file"
        }
        return response, 500

if __name__ == '__main__':
    app.run(debug=True)