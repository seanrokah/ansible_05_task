from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db
from app.models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists. Please login.')
            return redirect(url_for('main.login'))
        
        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created! You can now login.')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.notes'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.notes'))
        else:
            flash('Login failed. Please check your email and password.')
    
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/notes')
@login_required
def notes():
    notes = Note.query.filter_by(author=current_user).order_by(Note.date_created.desc()).all()
    return render_template('notes.html', notes=notes)

@main.route('/notes/create', methods=['GET', 'POST'])
@login_required
def create_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        note = Note(title=title, content=content, author=current_user)
        db.session.add(note)
        db.session.commit()
        
        flash('Note created successfully!')
        return redirect(url_for('main.notes'))
    
    return render_template('create_note.html')

@main.route('/notes/<int:note_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    
    if note.author != current_user:
        flash('You do not have permission to edit this note.')
        return redirect(url_for('main.notes'))
    
    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        db.session.commit()
        
        flash('Note updated successfully!')
        return redirect(url_for('main.notes'))
    
    return render_template('edit_note.html', note=note)

@main.route('/notes/<int:note_id>/delete')
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    
    if note.author != current_user:
        flash('You do not have permission to delete this note.')
        return redirect(url_for('main.notes'))
    
    db.session.delete(note)
    db.session.commit()
    
    flash('Note deleted successfully!')
    return redirect(url_for('main.notes'))