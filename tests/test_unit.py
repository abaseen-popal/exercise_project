import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv


from application import app, db
from application.models import Exercises,Locations,Location_exercises


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=getenv("DATABASE_URI"),
            SECRET_KEY=getenv("SECRET_KEY"),
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        test_exercise = Exercises(exercise_name="Test Jumping",description="Test up and down",
        sets="3",reps="12") 
        test_location = Locations(location_name="Test Park",description="Test description",
        address="Test address")
        test_location_exercise= Location_exercises(exercise_id=1,location_id=1)
        db.session.add(test_exercise)
        db.session.add(test_location)
        db.session.add(test_location_exercise)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_add_exe_location_get(self):
        response = self.client.get(url_for('add_exe_location',id=1),follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_update_get(self):
        response = self.client.get(url_for('update',id=1))
        self.assertEqual(response.status_code,200)

    def test_update_location_get(self):
        response = self.client.get(url_for('update_location',id=1),follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_add_location_exercise_get(self):
        response = self.client.get(url_for('add_location_exercise',id=1),follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_view_location_exercise_get(self):
        response = self.client.get(url_for('view_location_exercise',id=1))
        self.assertEqual(response.status_code,200)

    def test_add_loc_exercise_get(self):
        response = self.client.get(url_for('add_loc_exercise',id=1),follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_view_loc_exercise_get(self):
        response = self.client.get(url_for('view_loc_exercise',id=1),follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete',id=1),follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_delete_location_get(self):
        response = self.client.get(url_for('delete_location',id=1),follow_redirects=True)
        self.assertEqual(response.status_code,200)

class TestRead(TestBase):
    def test_read_exercises(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Test Jumping", response.data)

class TestReadLocation(TestBase):
    def test_read_location(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Test Park", response.data)

class TestCreate(TestBase):
    def test_create_exercise(self):
        response = self.client.post(
            url_for("create"),
            data=dict(exercise_name="Create a new exercise",
            description="Test description",sets="3",
            reps="12"),
            follow_redirects=True
        )
        self.assertIn(b"Create a new exercise", response.data)

class TestCreateLocation(TestBase):
    def test_create_location(self):
        response = self.client.post(
            url_for("add_exe_location"),
            data=dict(location_name="Create a new location",
            description="Test description",
            address="Test address"),
            follow_redirects=True
        )
        self.assertIn(b"Create a new location", response.data)

class TestCreateLocationExercise(TestBase):
    def test_create_location_exercise(self):
        response = self.client.post(
            url_for("add_location_exercise",id = 1),
            data=dict(exercise_name="Test Jumping"),
            follow_redirects=True
        )
        self.assertIn(b"Test Jumping", response.data)

class TestCreateExerciseLocation(TestBase):
    def test_create_exercise_location(self):
        response = self.client.post(
            url_for("add_loc_exercise",id = 1),
            data=dict(location_name="Test Park"),
            follow_redirects=True
        )
        self.assertIn(b"Test Park", response.data)

class TestUpdate(TestBase):
    def test_update_exercise(self):
        response = self.client.post(
            url_for("update", id=1),
            data=dict(exercise_name="Update an exercise",
            description="Test Update description",
            sets="3", reps="12"),
            follow_redirects=True
        )
        self.assertIn(b"Test Update description", response.data)

class TestUpdateLocation(TestBase):
    def test_update_location(self):
        response = self.client.post(
            url_for("update_location", id=1),
            data=dict(exercise_name="Update a location",
            description="Test description",
            address="Test Address"),
            follow_redirects=True
        )
        self.assertIn(b"Test description", response.data)

class TestDelete(TestBase):
    def test_delete_exercise(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Test Jumping", response.data)
