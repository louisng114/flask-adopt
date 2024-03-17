from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import NewPetForm, PetEditForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

if __name__ == '__main__':
    app.run(debug=True)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route("/")
def home_page():
    """render homepage"""
    pets = Pet.query.all()

    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def new_pet_page_and_handle():
    """render new pet page and handle form data"""
    form = NewPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    
    else:
        return render_template("new_pet_form.html", form=form)

@app.route("/pets/<int:pet_id>")
def pet_details_page(pet_id):
    pet = Pet.query.get(pet_id)

    return render_template("pet_details.html", pet=pet)

@app.route("/pets/<int:pet_id>/edit", methods=["GET", "POST"])
def pet_edit_page_and_handle(pet_id):
    pet = Pet.query.get(pet_id)
    form = PetEditForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        return redirect(f"/pets/{pet_id}")

    else:
        return render_template("pet_edit_form.html", pet=pet, form=form)






