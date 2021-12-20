from flask import Flask, render_template

app = Flask(__name__)

# all the variables
# projectname = ["my webside", "google"]
projecturl = ["https://google.com"]
projectname = ["No stuff yet"]
abouttext = "This is my blog. I am just a little boy. Please don't bully me."

# start here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html', Projectname=projectname, Projecturl=projecturl, longest=len(projectname))

@app.route('/about')
def blog():
    return render_template('about.html', textontext=abouttext)
# @app.route('/test')
# def test():
#     return "test"

if __name__ == '__main__':
    app.run(debug=False)
