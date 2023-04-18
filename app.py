from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///jay.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ragister(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.naam} - {self.city}"

# other routes here 

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/index.html')
def indexp():
    return render_template('/index.html')

@app.route('/project.html')
def project():
    return render_template('/project.html')

@app.route('/Dj.html')
def dj():
    return render_template('/Dj.html')

@app.route('/booking.html')
def booking():
    return render_template('/booking.html')

@app.route('/blogs.html')
def blogs():
    return render_template('/blogs.html')

@app.route('/achievement.html')
def achivement():
    return render_template('/achievement.html')

@app.route('/Sign.html')
def Sign():
    return render_template('/Sign.html')

@app.route('/About.html')
def About():
    return render_template('/About.html')

@app.route('/Social_media.html')
def Social_media():
    return render_template('/Social_media.html')


    
    



@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['email']
    password = request.form['psw']
    # Write the username and password to a file
    with open('user_data.txt', 'a') as f:
        f.write(f'{username}, {password}\n')
    
    # Process the username and password as needed
    
    return f'Successfully Submitted'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['uname']
    password = request.form['word']
    # Write the username and password to a file
    with open('Login_data.txt', 'a') as f:
        f.write(f'{username}, {password}\n')
        code = random.randint(1000, 9999)
    
    # Process the username and password as needed
    
    return render_template('usrlog.html', code=code)




@app.route('/Ragister.html', methods=['GET', 'POST'])
def Ragister():
    if request.method == "POST":
        title = request.form['name1']
        ucity = request.form['cityn']
        result = ragister(naam=title, city=ucity, password="dashrath")
        db.session.add(result)
        db.session.commit()
    allragistration = ragister.query.all()
    print(allragistration)
    return render_template('Ragister.html', allragistration=allragistration)
    
def run_gevent():
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()   

if "__name__"=="__main__":
        app.run(debug=True)

