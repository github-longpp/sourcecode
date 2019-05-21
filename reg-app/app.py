from flask import *
app = Flask(__name__)
import mlab
from reg import Registration

mlab.connect()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if  request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']
        yob = form['yob']
        gender = form['gender']
        city = form['city']

        print(first_name, last_name, email, yob, gender, city)
        reg = Registration(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            yob=yob,
                            gender=gender,
                            city=city)
        reg.save()
        return "Register"

if __name__ == '__main__':
  app.run(debug=True)