from flask import Flask, render_template, request, redirect, url_for
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def close_db_connection(conn):
    conn.close()

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, poem TEXT NOT NULL, content TEXT NOT NULL, author TEXT NOT NULL)')
    conn.close()

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.before_request
def before_request():
    init_db()

@app.context_processor
def inject_globals():
    return {
        "hobby": [
            "book",
            "movie",
            "walk",
            "tea party",
            "drawing",
            "board games",
            "no time to relax!!!"
        ]
    }

@app.route('/<int:post_id>')
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return render_template('post.html', post=post)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        poem = request.form['poem']
        content = request.form['content']
        author = request.form['author']

        conn = get_db_connection()
        conn.execute('INSERT INTO posts (poem, content, author) VALUES (?, ?, ?)', (poem, content, author))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add_post.html')

if __name__ == '__main__':
   app.run(debug = True)