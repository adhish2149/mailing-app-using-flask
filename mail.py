from flask import Flask,render_template,request,url_for,redirect
from flask_mail import Mail,Message
 



app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "mprojects834@gmail.com"
app.config['MAIL_PASSWORD'] = "m@prj#ADH"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = ('MAIL FROM ADH','mprojects834@gmail.com')

mail = Mail(app)

@app.route('/')
def index():
    return render_template("e-mail.html")
           
@app.route('/send_message',methods = ['GET','POST'])
def send_message():
    if request.method == 'POST':
        email = request.form['email']
        sub = request.form['subject']
        mes = request.form['message']
        
        message = Message(sub,recipients= [email])
        message.body = mes
        mail.send(message)
        success = "message delivered"
        
        return render_template("return.html",success = success)
    

if __name__ == "__main__":
    app.run(debug = True)