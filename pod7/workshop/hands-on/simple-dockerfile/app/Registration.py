from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

# Route for displaying the form and handling form submissions
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the form
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Redirect to /result with the user input as a query parameter
        return redirect(url_for('result', name=name))
    return render_template('index.html')

# Route for displaying the result after the form submission
@app.route('/result')
def result():
    # Get the user input from the query parameters
    name  = request.args.get('name')
    return render_template('result.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)