# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from db import DatabaseConnection

app = Flask(__name__)
app.secret_key = "mayank1777"

db = DatabaseConnection(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if db.authenticate_user(username, password):
            flash("Logged in successfully!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials. Please try again.", "danger")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Car routes and methods
@app.route("/cars")
def car_list():
    cars = db.all_cars()
    return render_template("car_list.html", cars=cars)

@app.route("/cars/add", methods=["GET", "POST"])
def add_car():
    if request.method == "POST":
        model = request.form["model"]
        year = request.form["year"]
        type_ = request.form["type"]
        category = request.form["category"]
        daily_rate = request.form["daily_rate"]
        weekly_rate = request.form["weekly_rate"]
        owner_type = request.form["owner_type"]
        owner_name = request.form["owner_name"]
        capacity = request.form["capacity"]
        transmission_type = request.form["transmission_type"]
        fuel_type = request.form["fuel_type"]
        mileage = request.form["mileage"]

        car_id = db.add_car(model, year, type_, category, daily_rate, weekly_rate, owner_type, owner_name, capacity, transmission_type, fuel_type, mileage)
        if car_id:
            flash("Car added successfully!", "success")
            return redirect(url_for("car_list"))
        else:
            flash("Error adding car. Please try again.", "danger")

    return render_template("add_car.html")

@app.route("/cars/edit/<int:car_id>", methods=["GET", "POST"])
def edit_car(car_id):
    if request.method == "POST":
        model = request.form["model"]
        year = request.form["year"]
        type_ = request.form["type"]
        category = request.form["category"]
        daily_rate = request.form["daily_rate"]
        weekly_rate = request.form["weekly_rate"]
        owner_type = request.form["owner_type"]
        owner_name = request.form["owner_name"]
        capacity = request.form["capacity"]
        transmission_type = request.form["transmission_type"]
        fuel_type = request.form["fuel_type"]
        mileage = request.form["mileage"]

        db.edit_car(car_id, model, year, type_, category, daily_rate, weekly_rate, owner_type, owner_name, capacity, transmission_type, fuel_type, mileage)
        flash("Car updated successfully!", "success")
        return redirect(url_for("car_list"))

    car = db.edit_car(car_id)
    if car:
        return render_template("edit_car.html", car=car)
    else:
        flash("Car not found.", "danger")
        return redirect(url_for("car_list"))

@app.route("/cars/delete/<int:car_id>")
def delete_car(car_id):
    db.delete_car(car_id)
    flash("Car deleted successfully!", "success")
    return redirect(url_for("car_list"))

@app.route("/cars/delete_all")
def delete_all_cars():
    db.delete_all_cars()
    flash("All cars deleted successfully!", "success")
    return redirect(url_for("car_list"))

# Customer routes and methods
@app.route("/customers")
def customer_list():
    customers = db.all_customers()
    return render_template("customer_list.html", customers=customers)

@app.route("/customers/add", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        is_business = request.form.get("is_business") == "on"

        customer_id = db.add_customer(name, phone, is_business)
        if customer_id:
            flash("Customer added successfully!", "success")
            return redirect(url_for("customer_list"))
        else:
            flash("Error adding customer. Please try again.", "danger")

    return render_template("add_customer.html")


@app.route("/customers/edit/<int:customer_id>", methods=["GET", "POST"])
def edit_customer(customer_id):
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        is_business = request.form.get("is_business") == "on"

        db.edit_customer(customer_id, name, phone, is_business)
        flash("Customer updated successfully!", "success")
        return redirect(url_for("customer_list"))

    customer = db.edit_customer(customer_id)
    if customer:
        return render_template("edit_customer.html", customer=customer)
    else:
        flash("Customer not found.", "danger")
        return redirect(url_for("customer_list"))


@app.route("/customers/delete/<int:customer_id>")
def delete_customer(customer_id):
    db.delete_customer(customer_id)
    flash("Customer deleted successfully!", "success")
    return redirect(url_for("customer_list"))

@app.route("/customers/delete_all")
def delete_all_customers():
    db.delete_all_customers()
    flash("All customers deleted successfully!", "success")
    return redirect(url_for("customer_list"))


# Rental routes and methods
@app.route("/rentals")
def rental_list():
    rentals = db.all_rentals()
    return render_template("rental_list.html", rentals=rentals)


@app.route("/rentals/add", methods=["GET", "POST"])
def add_rental():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        car_id = request.form["car_id"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        rental_id = db.add_rental(customer_id, car_id, start_date, end_date)
        if rental_id:
            flash("Rental added successfully!", "success")
            return redirect(url_for("rental_list"))
        else:
            flash("Error adding rental. Please try again.", "danger")

    return render_template("add_rental.html")


@app.route("/rentals/edit/<int:rental_id>", methods=["GET", "POST"])
def edit_rental(rental_id):
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        car_id = request.form["car_id"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        db.edit_rental(rental_id, customer_id, car_id, start_date, end_date)
        flash("Rental updated successfully!", "success")
        return redirect(url_for("rental_list"))

    rental = db.edit_rental(rental_id)
    if rental:
        return render_template("edit_rental.html", rental=rental)
    else:
        flash("Rental not found.", "danger")
        return redirect(url_for("rental_list"))


@app.route("/rentals/delete/<int:rental_id>")
def delete_rental(rental_id):
    db.delete_rental(rental_id)
    flash("Rental deleted successfully!", "success")
    return redirect(url_for("rental_list"))


@app.route("/rentals/delete_all")
def delete_all_rentals():
    db.delete_all_rentals()
    flash("All rentals deleted successfully!", "success")
    return redirect(url_for("rental_list"))


# Non-availability routes and methods
@app.route("/nonavailability")
def nonavailability_list():
    non_availabilities = db.all_nonavailabilities()
    return render_template("nonavailability_list.html", non_availabilities=non_availabilities)


@app.route("/nonavailability/add", methods=["GET", "POST"])
def add_nonavailability():
    if request.method == "POST":
        car_id = request.form["car_id"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        nonavailability_id = db.add_nonavailability(car_id, start_date, end_date)
        if nonavailability_id:
            flash("Non-availability added successfully!", "success")
            return redirect(url_for("nonavailability_list"))
        else:
            flash("Error adding non-availability. Please try again.", "danger")

    return render_template("add_nonavailability.html")


@app.route("/nonavailability/edit/<int:nonavailability_id>", methods=["GET", "POST"])
def edit_nonavailability(nonavailability_id):
    if request.method == "POST":
        car_id = request.form["car_id"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        db.edit_nonavailability(nonavailability_id, car_id, start_date, end_date)
        flash("Non-availability updated successfully!", "success")
        return redirect(url_for("nonavailability_list"))

    nonavailability = db.edit_nonavailability(nonavailability_id)
    if nonavailability:
        return render_template("edit_nonavailability.html", nonavailability=nonavailability)
    else:
        flash("Non-availability not found.", "danger")
        return redirect(url_for("nonavailability_list"))

@app.route("/nonavailability/delete/int:nonavailability_id")
def delete_nonavailability(nonavailability_id):
    db.delete_nonavailability(nonavailability_id)
    flash("Non-availability deleted successfully!", "success")
    return redirect(url_for("nonavailability_list"))

@app.route("/nonavailability/delete_all")
def delete_all_nonavailability():
    db.delete_all_nonavailabilities()
    flash("All non-availabilities deleted successfully!", "success")
    return redirect(url_for("nonavailability_list"))


if __name__ == "__main__":
    app.run(debug=True)

