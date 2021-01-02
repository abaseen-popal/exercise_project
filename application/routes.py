from application import app, db
from application.models import Exercises,Locations,Location_exercises
from flask import render_template, request,redirect, url_for
from application.forms import ExerciseForm, LocationForm, AddingExerciseLocForm, AddingLocToExerciseForm

@app.route("/")
@app.route("/home")
def home():
    all_exercise = Exercises.query.all()
    all_locations = Locations.query.all()
    all_location_exercises = Location_exercises.query.all()
    output = ""
    return render_template("index.html", title="Home", all_exercise=all_exercise, all_locations=all_locations,all_location_exercises=all_location_exercises)

@app.route("/create", methods=["GET","POST"])
def create():
    form = ExerciseForm()
    if request.method == "POST":
        exercise_name = form.exercise_name.data
        description = form.description.data
        sets = form.sets.data
        reps = form.reps.data
        # if form.validate_on_submit():
        new_exercise = Exercises(exercise_name=exercise_name,description=description,sets=sets,reps=reps) 
        db.session.add(new_exercise)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", title="Add Exercise",form=form)


@app.route("/add_location", methods=["GET","POST"])
def add_exe_location():
    form = LocationForm()
    if request.method == "POST":
        # if form.validate_on_submit():
        location_name = form.location_name.data
        description = form.description.data
        address = form.address.data
        new_location = Locations(location_name=location_name,
        description=description,address=address) 
        db.session.add(new_location)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add_location.html", title="Add Location",form=form)


@app.route("/update_exercise/<int:id>", methods= ["GET","POST"])
def update(id):
    form = ExerciseForm()
    exercise = Exercises.query.filter_by(id=id).first()
    if request.method == "POST":
        exercise.description = form.description.data
        exercise.sets = form.sets.data
        exercise.reps = form.reps.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", title="Update Exercise", form=form,exercise=exercise)

@app.route("/update_location/<int:id>", methods= ["GET","POST"])
def update_location(id):
    form = LocationForm()
    locations = Locations.query.filter_by(id=id).first()
    if request.method == "POST":
        locations.location_name = form.location_name.data 
        locations.description = form.description.data
        locations.address = form.address.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update_location.html", title="Update Location", form=form, locations=locations)


@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete(id):
    exercise = Exercises.query.filter_by(id=id).first()
    db.session.delete(exercise)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete_location/<int:id>", methods=["GET","POST"])
def delete_location(id):
    locations = Locations.query.filter_by(id=id).first()
    db.session.delete(locations)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add_location_exercise/<int:id>",methods=["GET","POST"])
def add_location_exercise(id):
    form = AddingExerciseLocForm()
    exe_form = form.exercise_name.data
    exercise_selected = Exercises.query.filter_by(exercise_name=exe_form).first()
    location = Locations.query.filter_by(id=id).first()

    if request.method == "POST":
        adding_together = Location_exercises(exercise_id=exercise_selected.id,location_id=location.id)
        db.session.add(adding_together)
        db.session.commit()
        return redirect(url_for("view_location_exercise", id=id)) 
    return render_template("add_location_exercise.html", title="Adding Exercise", form=form, location=location, exe_form=exe_form, exercise_selected=exercise_selected)

@app.route("/view_location_exercise/<int:id>",methods=["GET","POST"])
def view_location_exercise(id):
    location = Locations.query.filter_by(id=id).first()
    all_location_exercises = Location_exercises.query.filter_by(location_id=location.id)
    all_exercises = Exercises.query.all()
    return render_template("view_location_exercise.html", title="Viewing Exercises", location=location, all_location_exercises=all_location_exercises,all_exercises=all_exercises)

@app.route("/add_loc_exercise/<int:id>",methods=["GET","POST"])
def add_loc_exercise(id):
    form = AddingLocToExerciseForm()
    loc_form = form.location_name.data
    location_selected = Locations.query.filter_by(location_name=loc_form).first()
    exercise = Exercises.query.filter_by(id=id).first()

    if request.method == "POST":
        adding_together = Location_exercises(location_id=location_selected.id,exercise_id=exercise.id)
        db.session.add(adding_together)
        db.session.commit()
        return redirect(url_for("view_loc_exercise",id=id)) 
    return render_template("add_loc_exercise.html", title="Adding Location", form=form, exercise=exercise, loc_form=loc_form, location_selected=location_selected)

@app.route("/view_loc_exercise/<int:id>",methods=["GET","POST"])
def view_loc_exercise(id):
    exercise = Exercises.query.filter_by(id=id).first()
    all_location_exercises = Location_exercises.query.filter_by(exercise_id=exercise.id)
    all_locations = Locations.query.all()
    return render_template("view_loc_exercise.html", title="Viewing Exercises", exercise=exercise, all_location_exercises=all_location_exercises,all_locations=all_locations)
