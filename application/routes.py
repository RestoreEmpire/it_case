from flask import render_template, url_for, request, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from application.forms import LoginForm, RegistrationForm, EditProfileForm
from application.models import Article, Users, Positions, Mentors, Stages
from application import app, db




@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods =['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = Users.query.filter_by(username=loginform.username.data).first()
        if user is None or not user.check_password(loginform.password.data):
            flash('Не правильный пароль или имя пользователя')
            return redirect(url_for('login'))
        login_user(user, remember=loginform.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('user')
        return redirect(next_page)
    return render_template('login.html', title = 'Войти', loginform = loginform)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/user')
@login_required
def user():
    post = Positions.query.filter_by(id=current_user.position_id).first()
    mentor = Mentors.query.filter_by(id=current_user.mentors_id).first()
    stage = [(s.id, s.stage, s.description) for s in Stages.query.all()]
    return render_template('user.html', post = post, mentor=mentor, stage=stage)


@app.route('/user/<userpage>')
@login_required
def userpage(userpage):
    user = Users.query.filter_by(username=userpage).first_or_404()
    post = Positions.query.filter_by(id=user.position_id).first()
    mentor = Mentors.query.filter_by(id=user.mentors_id).first()
    return render_template('userpage.html', user=user, post = post, mentor = mentor)

@app.route('/registration', methods =['GET','POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    regform = RegistrationForm()
    if regform.validate_on_submit():
        user = Users(username=regform.username.data, email=regform.email.data)
        user.set_password(regform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляем, вы прошли регистрацию')
        return redirect(url_for('login'))
    return render_template('registration.html',title="Регистрация", regform=regform)


@app.route('/edit', methods =['GET','POST'])
@login_required
def edit():
    form = EditProfileForm(current_user.username)
    user = Users.query.filter_by(username=current_user.username).first()
    form.position.choices = [(g.id, g.position) for g in Positions.query.all()]
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        if current_user.first_name != None:
            form.first_name.data = current_user.first_name
        if current_user.last_name != None:
            form.last_name.data = current_user.last_name
        if current_user.patronym != None:
            form.patronym.data = current_user.patronym
        
    elif form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.position_id = form.position.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.patronym = form.patronym.data
        db.session.commit()
        flash('Данные успешно сохранены')
        return redirect(url_for('edit'))
    return render_template('edit.html', form=form)


@app.route('/test-info')
def test_info():
    form_output = Article.query.order_by(Article.date.desc()).all()
    return render_template('test-info.html', form_output=form_output )


@app.route('/test-info/<int:id>')
def test_info_article(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)


@app.route('/test-form', methods=['POST', 'GET'])
def test_form():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        test_form = Article(title=title, intro=intro, text=text)

        db.session.add(test_form)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('test-form.html')