from flask import Flask, render_template
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')

def  hello_world():
     return render_template('index.html', name="Jay")
app.run(debug=True)
