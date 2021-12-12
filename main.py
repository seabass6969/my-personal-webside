from flask import Flask, render_template

app = Flask(__name__)

projectname = ["my webside", "google"]
projecturl = ["https://heroku.com", "https://google.com"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html', Projectname=projectname, Projecturl=projecturl, longest=len(projectname))

@app.route('/about')
def blog():
    return render_template('about.html')
# @app.route('/test')
# def test():
#     return "test"

if __name__ == '__main__':
    app.run(debug=False)
