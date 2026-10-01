from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts.html')
def posts():
    return render_template('posts.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/privacy.html')
def privacy():
    return render_template('privacy.html')

@app.route('/posts/<name>.html')
def individual_posts(name):
    return render_template(f'posts/{name}.html')

if __name__ == '__main__':
    app.run(debug=True)