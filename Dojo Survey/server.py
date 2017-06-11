from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'Macbook'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    favLanguage = request.form['favLanguage']
    comment = request.form['comment']

    if len(name) < 2:
        flash('Name needs to be at least 2 characters.')

    if len(comment) > 120 or len(comment) < 1:
        flash('Comment needs to be filled in and have less than 120 characters.')

    if '_flashes' in session:
        return redirect('/')

    return render_template('result.html', name=name, location=location, favLanguage = favLanguage, comment=comment)

@app.route('/clear')
def clear():
    return redirect('')


app.run(debug=True) # run our server
