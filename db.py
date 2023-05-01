import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self, app):
        try:
            self.connection = mysql.connector.connect(
                host="academicmysql.mysql.database.azure.com", port="3306", user="mxv8999", password="Mayank1777",
                database="mxv8999"

            )
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def authenticate_user(self, username, password):
        if username == "root" and password == "admin":
            return True
        return False


    def all_cars(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM cars"
            cursor.execute(query)
            cars = cursor.fetchall()
            cursor.close()
            return cars
        except Error as e:
            print(f"Error fetching all cars: {e}")

    def edit_car(self, car_id, model, year, type_, category, daily_rate, weekly_rate, owner_type, owner_name, capacity,
                 transmission_type, fuel_type, mileage):
        try:
            cursor = self.connection.cursor()
            query = """UPDATE cars SET model = %s, year = %s, type = %s, category = %s, daily_rate = %s, weekly_rate = %s, owner_type = %s, owner_name = %s, capacity = %s, transmission_type = %s, fuel_type = %s, mileage = %s WHERE id = %s"""
            cursor.execute(query, (
            model, year, type_, category, daily_rate, weekly_rate, owner_type, owner_name, capacity, transmission_type,
            fuel_type, mileage, car_id))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error editing car: {e}")

    def add_car(self, model, year, type_, category, daily_rate, weekly_rate, owner_type, owner_name, capacity,
                transmission_type, fuel_type, mileage):
        try:
            cursor = self.connection.cursor()
            query = """INSERT INTO cars (model, year, type, category, daily_rate, weekly_rate, owner_type, owner_name, capacity, transmission_type, fuel_type, mileage)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (
            model, year, type_, category, daily_rate, weekly_rate, owner_type, owner_name, capacity, transmission_type,
            fuel_type, mileage))
            self.connection.commit()
            car_id = cursor.lastrowid
            cursor.close()
            return car_id
        except Error as e:
            print(f"Error adding car: {e}")

    def delete_car(self, car_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM cars WHERE id = %s"
            cursor.execute(query, (car_id,))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error deleting car: {e}")

    def delete_all_cars(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM cars")
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error deleting all cars: {e}")

    # Rental methods
    def all_rentals(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM rentals"
            cursor.execute(query)
            rentals = cursor.fetchall()
            cursor.close()
            return rentals
        except Error as e:
            print(f"Error fetching all rentals: {e}")

    def edit_rental(self, rental_id, rental_type, no_of_days, no_of_weeks, start_date, return_date, amount_due, customer_id, car_id):
        try:
            cursor = self.connection.cursor()
            query = """UPDATE rentals SET rental_type = %s, no_of_days = %s, no_of_weeks = %s, start_date = %s, return_date = %s, amount_due = %s, customer_id = %s, car_id = %s WHERE id = %s"""
            cursor.execute(query, (rental_type, no_of_days, no_of_weeks, start_date, return_date, amount_due, customer_id, car_id, rental_id))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error editing rental: {e}")

    def add_rental(self, rental_type, no_of_days, no_of_weeks, start_date, return_date, amount_due, customer_id, car_id):
        try:
            cursor = self.connection.cursor()
            query = """INSERT INTO rentals (rental_type, no_of_days, no_of_weeks, start_date, return_date, amount_due, customer_id, car_id)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (rental_type, no_of_days, no_of_weeks, start_date, return_date, amount_due, customer_id, car_id))
            self.connection.commit()
            rental_id = cursor.lastrowid
            cursor.close()
            return rental_id
        except Error as e:
            print(f"Error adding rental: {e}")

    def delete_rental(self, rental_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM rentals WHERE id = %s"
            cursor.execute(query, (rental_id,))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error deleting rental: {e}")

    def delete_all_rentals(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM rentals")
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error deleting all rentals: {e}")

    # Nonavailability methods
    def all_nonavailabilities(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM nonavailability"
            cursor.execute(query)
            nonavailabilities = cursor.fetchall()
            cursor.close()
            return nonavailabilities
        except Error as e:
            print(f"Error fetching all nonavailabilities: {e}")

    def edit_nonavailability(self, id, car_id, start_date, end_date):
        try:
            cursor = self.connection.cursor()
            query = """UPDATE nonavailability SET car_id = %s, start_date = %s, end_date = %s WHERE id = %s"""
            cursor.execute(query, (car_id, start_date, end_date, id))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error editing nonavailability: {e}")

    def add_nonavailability(self, car_id, start_date, end_date):
        try:
            cursor = self.connection.cursor()
            query = """INSERT INTO nonavailability (car_id, start_date, end_date)
                               VALUES (%s, %s, %s)"""
            cursor.execute(query, (car_id, start_date, end_date))
            self.connection.commit()
            nonavailability_id = cursor.lastrowid
            cursor.close()
            return nonavailability_id
        except Error as e:
            print(f"Error adding nonavailability: {e}")

    def delete_nonavailability(self, id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM nonavailability WHERE id = %s"
            cursor.execute(query, (id,))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error deleting nonavailability: {e}")

    def delete_all_nonavailabilities(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM nonavailability")
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error deleting all nonavailabilities: {e}")

    def all_customers(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM customers"
            cursor.execute(query)
            customers = cursor.fetchall()
            cursor.close()
            return customers
        except Error as e:
            print(f"Error fetching all customers: {e}")

    def edit_customer(self, id, name, phone, is_business):
        try:
            cursor = self.connection.cursor()
            query = """UPDATE customers SET name = %s, phone = %s, is_business = %s WHERE id = %s"""
            cursor.execute(query, (name, phone, is_business, id))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error updating customer: {e}")

    def add_customer(self, name, phone, is_business):
        try:
            cursor = self.connection.cursor()
            query = """INSERT INTO customers (name, phone, is_business) VALUES (%s, %s, %s)"""
            cursor.execute(query, (name, phone, is_business))
            self.connection.commit()
            customer_id = cursor.lastrowid
            cursor.close()
            return customer_id
        except Error as e:
            print(f"Error adding customer: {e}")

    def delete_customer(self, id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM customers WHERE id = %s"
            cursor.execute(query, (id,))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error deleting customer: {e}")

    def delete_all_customers(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM customers")
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error deleting all customers: {e}")


