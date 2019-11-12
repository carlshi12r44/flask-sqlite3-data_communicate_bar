from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_posts, get_posts
app = Flask(__name__)

# avoid CORS site scripting
CORS(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        pass
    
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_posts(name, post)

    posts = get_posts()

    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)