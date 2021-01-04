import unittest
import time
from flask import url_for
from urllib.request import urlopen
from os import getenv


from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Exercises,Locations,Location_exercises

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
        app.config['SECRET_KEY'] = getenv("SECRET_KEY")
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/Abase/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAddExercise(TestBase):

    def test_add_exercise(self):


        # Click create exercise link
        self.driver.find_element_by_xpath("/html/body/a[2]").click()
        time.sleep(1)

        # Fill in exercise form
        self.driver.find_element_by_xpath('//*[@id="exercise_name"]').send_keys('int testing name')
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('int testing description')
        self.driver.find_element_by_xpath('//*[@id="sets"]').send_keys('int testing sets')
        self.driver.find_element_by_xpath('//*[@id="reps"]').send_keys('int testing reps')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to home page
        assert url_for('home') in self.driver.current_url
        assert Exercises.query.filter_by(id=1).first().exercise_name == 'int testing name'

    def test_add_location(self):
        # Click create location link
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        time.sleep(1)

        # Fill in location form
        self.driver.find_element_by_xpath('//*[@id="location_name"]').send_keys('int testing location name')
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('int testing description')
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys('int testing address')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to home page
        assert url_for('home') in self.driver.current_url

    # def test_Update_location(self):


    #     # Click create location link
    #     self.driver.find_element_by_xpath("/html/body/div[2]/form[1]/input").click()
    #     time.sleep(1)

    #     # Fill in location form
    #     self.driver.find_element_by_xpath('//*[@id="location_name"]').send_keys('int testing location update')
    #     self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('int testing description update')
    #     self.driver.find_element_by_xpath('//*[@id="address"]').send_keys('int testing address update')
    #     self.driver.find_element_by_xpath('//*[@id="submit"]').click()
    #     time.sleep(1)

    #     # Assert that browser redirects to home page
    #     assert url_for('home') in self.driver.current_url
    #     assert Locations.query.filter_by(id=1).first().location_name == 'int testing location update'

    # def test_update_exercise(self):
    #     # Click create exercise link
    #     self.driver.find_element_by_xpath("/html/body/div[1]/form[1]/input").click()
    #     time.sleep(1)

    #     # Fill in exercise form
    #     self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('int testing update description')
    #     self.driver.find_element_by_xpath('//*[@id="sets"]').send_keys('int testing update sets')
    #     self.driver.find_element_by_xpath('//*[@id="reps"]').send_keys('int testing update reps')
    #     self.driver.find_element_by_xpath('//*[@id="submit"]').click()
    #     time.sleep(1)

    #     # Assert that browser redirects to home page
    #     assert url_for('home') in self.driver.current_url

    # def test_add_loc_exercise(self):
    #     # Click create exercise link
    #     self.driver.find_element_by_xpath("/html/body/div[1]/form[2]/input").click()
    #     time.sleep(1)

    #     # Fill in exercise form
    #     self.driver.find_element_by_xpath('//*[@id="location_name"]').send_keys('int testing adding location to exercise')
    #     self.driver.find_element_by_xpath('//*[@id="submit"]').click()
    #     time.sleep(1)

    #     # Assert that browser redirects to home page
    #     assert url_for('view_loc_exercise') in self.driver.current_url

    # def test_add_exercise_loc(self):
    #     # Click create exercise link
    #     self.driver.find_element_by_xpath("/html/body/div[2]/form[3]/input").click()
    #     time.sleep(1)

    #     # Fill in exercise form
    #     self.driver.find_element_by_xpath('//*[@id="exercise_name"]').send_keys('int testing adding exercise to location')
    #     self.driver.find_element_by_xpath('//*[@id="submit"]').click()
    #     time.sleep(1)

    #     # Assert that browser redirects to home page
    #     assert url_for('view_location_exercise') in self.driver.current_url


if __name__ == '__main__':
    unittest.main(port=5000)