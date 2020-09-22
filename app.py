from myproject import db, app
from flask import render_template, request, url_for, flash, abort, redirect
from flask_login import login_user, login_required, logout_user
from myproject.models import student, recruiter, company
from myproject.forms import loginForm, registrationForm, companyappr,predicform
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd



@app.route("/")
#this route is will (STUDENT,COMPANY,RECRUITER TABS IN PANEL)
def home():
    return render_template('home.html')

@app.route("/welcome/studant")
# welcome(name of user) and nav of selected field

def welcome_stud():
    return render_template('welcome_stud.html')

@app.route("/welcome/recruiter")
# welcome(name of user) and nav of selected field
def welcome_rec():
    return render_template('welcome_rec.html')

@app.route("/welcome/company")
# welcome(name of user) and nav of selected field
def welcome_comp():
    return render_template('welcome_comp.html')

@app.route("/logout")
# logout for all users
def logout():
    logout_user()
    flash("you are logged out !!")
    return redirect(url_for('home'))

@app.route("/login/student",methods=['POST','GET'])
    #login for student username and password
def studlogin():
    form_new = loginForm()
    if form_new.validate_on_submit():
        stud = student.query.filter_by(username=form_new.username.data).first()
        if stud.check_password_stud(form_new.password.data):
            login_user(stud)
            flash("logged in succesfully!!!")
            return redirect(url_for('welcome_stud'))
        
    return render_template('login_stud.html',form_new=form_new)


@app.route("/login/recruiter",methods=['GET','POST'])
# login for student username and password
def reclogin():
    form = loginForm()
    if form.validate_on_submit():
        rec = recruiter.query.filter_by(username=form.username.data).first()
        if rec.check_password_rec(form.password.data):
            login_user(rec)
            return redirect(url_for('welcome_rec'))

    return render_template('login_rec.html')


@app.route("/login/company",methods=['GET','POST'])
# login for student username and password
def complogin():
    form = loginForm()
    if form.validate_on_submit():
        comp = company.query.filter_by(username=form.username.data).first()
        if comp.check_password_comp(form.password.data):
            login_user(comp)
            return redirect(url_for('welcome_comp'))

    return render_template('login_comp.html')

@app.route("/register/student",methods=['GET','POST'])
#register student
def register_stud():
    form = registrationForm()
    if form.validate_on_submit():
        
        stud = student(username=form.username.data,password=form.password.data)
        db.session.add(stud)
        db.session.commit()
        flash("thanks for registering")
        return redirect(url_for('studlogin'))
    
    return render_template('register_stud.html',form=form)


@app.route("/register/recruiment",methods=['GET','POST'])
# register student
def register_rec():
    form = registrationForm()
    if form.validate_on_submit():
        rec = recruiter(username=form.username.data, password=form.password.data)
        db.session.add(rec)
        db.session.commit()
        flash("thanks for registering")
        return redirect(url_for('reclogin'))

    return render_template('register_rec.html',form=form)


@app.route("/register/company",methods=['GET','POST'])
# register student
def register_comp():
    form = registrationForm()
    if form.validate_on_submit():
        comp = company(username=form.username.data, password=form.password.data)
        db.session.add(comp)
        db.session.commit()
        flash("thanks for registering")
        return redirect(url_for('complogin'))

    return render_template('register_comp.html',form=form)


#append companyname : companyinfo
@app.route("/prediction/student",methods=['GET', 'POST'])
def prediction_stud():
    form = predicform
    if form.validate_on_submit():
        label01=form.label1.data
        label02=form.label2.data
        label03=form.label3.data
        label04=form.label4.data
        label05=form.label5.data
        label06=form.label6.data
        label07=form.label7.data
        label08=form.label8.data
        label09=form.label9.data
        pd.DataFrame([label01,label02,label03,label04,label05,label06,label07,label08,label09], columns=['col1','col2','col3','col4','col5','col6','col7','col8','col9'],dtype=float)







if __name__=='__main__':
    app.run(debug=True)

                        
                        
        
