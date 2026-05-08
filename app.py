from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Temporary in-memory storage
bookings = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Hotel Booking App</title>
    <style>
        body {
            font-family: Arial;
            background: #f2f2f2;
            padding: 40px;
        }

        .container {
            background: white;
            padding: 20px;
            width: 450px;
            margin: auto;
            border-radius: 10px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
        }

        button {
            margin-top: 15px;
            width: 100%;
            padding: 10px;
            background: #007BFF;
            color: white;
            border: none;
        }

        table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Hotel Booking</h2>

    <form action="/book" method="POST">
        <input type="text" name="name" placeholder="Guest Name" required>
        <input type="text" name="room" placeholder="Room Type" required>
        <input type="date" name="checkin" required>
        <input type="date" name="checkout" required>

        <button type="submit">Book Room</button>
    </form>

    <h3>Bookings</h3>

    <table>
        <tr>
            <th>Name</th>
            <th>Room</th>
            <th>Check-In</th>
            <th>Check-Out</th>
        </tr>

        {% for booking in bookings %}
        <tr>
            <td>{{ booking.name }}</td>
            <td>{{ booking.room }}</td>
            <td>{{ booking.checkin }}</td>
            <td>{{ booking.checkout }}</td>
        </tr>
        {% endfor %}
    </table>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, bookings=bookings)

@app.route("/book", methods=["POST"])
def book():
    booking = {
        "name": request.form["name"],
        "room": request.form["room"],
        "checkin": request.form["checkin"],
        "checkout": request.form["checkout"]
    }

    bookings.append(booking)

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
