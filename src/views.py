from flask import(
    render_template,
    request,
    redirect,
    url_for,
    jsonify
)

def index():
    return render_template('index.html')
