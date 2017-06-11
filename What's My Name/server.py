from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def landingpage():
  return render_template("index.html")


@app.route('/process', methods=['POST'])
def processpage():
   print "Got Post Info"
   print request.form
   name = request.form['name']
   return render_template("process.html", name=name)


app.run(debug=True)
