from application import db
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

class Location_exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column('exercises_id', db.Integer, db.ForeignKey('exercises.id'))
    location_id = db.Column('location_id', db.Integer, db.ForeignKey('locations.id'))


class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(240))
    description = db.Column(db.String(240), nullable=False)
    sets = db.Column(db.String(240), nullable=False)
    reps = db.Column(db.String(240), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location_exercises = db.relationship('Location_exercises', backref='exercises')

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(240))
    description = db.Column(db.String(240), nullable=False)
    address = db.Column(db.String(240), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location_exercises = db.relationship('Location_exercises', backref='locations')
