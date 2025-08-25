
from flask import Flask,render_template,url_for,redirect,request,flash
from flask_login import login_user, LoginManager,current_user,logout_user, login_required
from Forms import * 
from models import *
from flask_bcrypt import Bcrypt
import secrets
import os
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
# from bs4 import BeautifulSoup as bs
from flask_colorpicker import colorpicker



#Did latest commit with the requirement file

#Change App
app = Flask(__name__)
app.config['SECRET_KEY'] = "sdsdjfe832j2rj_32j"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///techxicons_db.db"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle':280}
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOADED"] = 'static/uploads'

db.init_app(app)

login_manager = LoginManager(app)

# Log in
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

application=app
ALLOWED_EXTENSIONS = {"txt", "xlxs",'docx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file has an allowed extension
def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_file(file):

        filename = secure_filename(file)

        _img_name, _ext = os.path.splitext(file.filename)
        gen_random = secrets.token_hex(8)
        new_file_name = gen_random + _ext

        if file.filename == '':
            return 'No selected file'

        if file.filename and allowed_files(file):
            file_saved = file.save(os.path.join(app.config["UPLOADED"],new_file_name))
            flash(f"File Upload Successful!!", "success")
            return new_file_name

        else:
            return f"Allowed are [.txt, .xls,.docx, .pdf, .png, .jpg, .jpeg, .gif] only"


def createall(db_):
    db_.create_all()

encry_pw = Bcrypt()

@app.context_processor
def inject_ser():
    # ser = Serializer(app.config['SECRET_KEY'])  # Define or retrieve the value for 'ser'
    # count_jobs = count_ads()

    return dict()

@app.route("/", methods=['POST','GET'])
def home():
    contact_form = Contact_Form()

    return render_template("index.html", title="Home", contact_form=contact_form)


@app.route("/contact", methods=["POST", "GET"])
def contact_us():
    # print("DEBUG EMAIL: ",os.environ.get("EMAIL_INFO"))
    contact_form = Contact_Form()
    if request.method == "POST":
        if contact_form.validate_on_submit():
            def send_link():
                app.config["MAIL_SERVER"] = "techxolutions.com"
                app.config["MAIL_PORT"] = 465
                app.config["MAIL_USE_TLS"] = True
                em = app.config["MAIL_USERNAME"] = os.environ.get("EMAIL")
                app.config["MAIL_PASSWORD"] = os.environ.get("TX_PWD")

                # print("DEBUG EMAIL1: ",em)
                # print("DEBUG EMAILP: ",app.config["MAIL_PASSWORD"])

                mail = Mail(app)

                msg = Message(contact_form.subject.data, sender=contact_form.email.data, recipients=[em])
                msg.body = f"""{contact_form.message.data}\n
{contact_form.email.data}\n
<p style="font-size:25px;color:red">This is a Test</p>
                    """

                # try:
                mail.send(msg)
                flash("Your Message has been Successfully Sent!!", "success")
                return "Email Sent"
                # except Exception as e:
                #     # print(e)
                #     flash(f'Ooops Something went wrong!! Please Retry', 'error')
                #     return "The mail was not sent"

                # Send the pwd reset request to the above email
            send_link()

            #print("Posted")
        else:
            for error in contact_form.errors:
                print('Form Error: ',error)
            flash("Ooops!! Please be sure to fill both email & message fields, correctly","error")

    # return render_template("contact.html",contact_form=contact_form)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
