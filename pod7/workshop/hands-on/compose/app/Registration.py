from flask import Flask, render_template, request, redirect, url_for # type:ignore
from flask_sqlalchemy import SQLAlchemy # type:ignore
from werkzeug.security import generate_password_hash, check_password_hash # type:ignore

app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:user-password@db/app' # host of db should be the name of the service in the compose file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Create a model to store user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Store hashed password

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

# Route for displaying the form and handling form submissions
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Save the user data to the database
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the result page or a success page
        return redirect(url_for('result', name=name))

    return render_template('index.html')

# Route for displaying the result after the form submission
@app.route('/result')
def result():
    # Get the user's name from the query parameters
    name = request.args.get('name')
    return render_template('result.html', name=name)

if __name__ == '__main__':
    # Create the database and the User table
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=8080, debug=True)