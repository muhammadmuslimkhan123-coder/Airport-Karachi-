from flask import Flask, render_template, request

app = Flask(__name__)

flights = [
    {"id": 1, "from": "Karachi", "to": "Lahore", "time": "10:00 AM", "price": 15000},
    {"id": 2, "from": "Karachi", "to": "Islamabad", "time": "02:00 PM", "price": 18000},
    {"id": 3, "from": "Lahore", "to": "Karachi", "time": "06:00 PM", "price": 16000},
]


@app.route("/")
def home():
    return render_template("index.html", flights=flights)


@app.route("/book/<int:flight_id>", methods=["GET", "POST"])
def book(flight_id):
    flight = next((f for f in flights if f["id"] == flight_id), None)

    if flight is None:
        return "Flight not found", 404

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        return render_template(
            "success.html",
            name=name,
            email=email,
            flight=flight
        )

    return render_template("book.html", flight=flight)


if __name__ == "__main__":
    app.run(debug=True)
