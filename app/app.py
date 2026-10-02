from flask import Flask, render_template, request

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

@app.route("/registration.html", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password != confirm:
            return render_template('failure.html')
        else:
            return render_template('success.html', username=username, email=email)
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)

