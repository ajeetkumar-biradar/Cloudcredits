from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'files')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/open/<filename>', methods=['GET'])
def open_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return render_template('editor.html', filename=filename, content=content)
    except FileNotFoundError:
        flash('File not found!', 'danger')
        return redirect(url_for('index'))

@app.route('/save', methods=['POST'])
def save_file():
    filename = request.form['filename']
    content = request.form['content']
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        flash(f'{filename} saved successfully!', 'success')
    except Exception as e:
        flash(f'Error saving file: {e}', 'danger')
    return redirect(url_for('index'))

@app.route('/new', methods=['GET', 'POST'])
def new_file():
    if request.method == 'POST':
        filename = request.form['filename']
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            flash('File already exists!', 'warning')
        else:
            with open(file_path, 'w') as f:
                f.write('')
            flash(f'{filename} created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
        flash(f'{filename} deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting file: {e}', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
