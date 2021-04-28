from flask import Flask, request, render_template, redirect, url_for

import pymysql 

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

connection = pymysql.connect(host="localhost", 
                            user="root", 
                            passwd="123456**oK**", 
                            database="merchstop")
cursor = connection.cursor()

@app.route("/", methods=["GET","POST"])
def Index():
    return render_template('index.html')

@app.route("/men-summer/", methods=["GET","POST"])
def Men():
    return render_template('mensummer.html')

@app.route("/women-summer/", methods=["GET","POST"])
def Women():
    return render_template('womensummer.html')

@app.route("/contact-us/", methods=["GET","POST"])
def ContactUs():
    if request.method == "POST":
        name_value = request.form["name"]
        subject_value = request.form["subject"]
        email_value = request.form["email"]
        message_value = request.form["message"]
        cursor.execute("insert into FEEDBACK(name,subject,email,feedback) values(%s,%s,%s,%s)",(name_value,subject_value,email_value,message_value))
        connection.commit() 
    return render_template('contactus.html')

if __name__ == "__main__":
    app.run(debug=True)