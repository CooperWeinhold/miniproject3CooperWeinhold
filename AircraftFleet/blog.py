
from flask import Blueprint, render_template, request, redirect, url_for
from .db import get_db

bp = Blueprint('fleet', __name__)

@bp.route('/aircraft')
def aircraft():
    db = get_db()
    aircrafts = db.execute('SELECT * FROM aircraft').fetchall()
    return render_template('aircraft/index.html', aircrafts=aircrafts)

@bp.route('/aircraft/add', methods=('GET', 'POST'))
def add_aircraft():
    if request.method == 'POST':
        type = request.form['type']
        registration = request.form['registration']
        flight_hours = request.form['flight_hours']
        db = get_db()
        db.execute(
            'INSERT INTO aircraft (type, registration, flight_hours) VALUES (?, ?, ?)',
            (type, registration, flight_hours)
        )
        db.commit()
        return redirect(url_for('fleet.aircraft'))

    return render_template('aircraft/add.html')

@bp.route('/aircraft/<int:id>/edit', methods=('GET', 'POST'))
def edit_aircraft(id):
    db = get_db()
    aircraft = db.execute('SELECT * FROM aircraft WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        type = request.form['type']
        registration = request.form['registration']
        flight_hours = request.form['flight_hours']
        db.execute(
            'UPDATE aircraft SET type = ?, registration = ?, flight_hours = ? WHERE id = ?',
            (type, registration, flight_hours, id)
        )
        db.commit()
        return redirect(url_for('fleet.aircraft'))

    return render_template('aircraft/edit.html', aircraft=aircraft)

@bp.route('/aircraft/<int:id>/delete', methods=('POST',))
def delete_aircraft(id):
    db = get_db()
    db.execute('DELETE FROM aircraft WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('fleet.aircraft'))
