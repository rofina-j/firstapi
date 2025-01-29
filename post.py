from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # Your MySQL host
app.config['MYSQL_USER'] = 'root'       # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'Rofin@04'  # Your MySQL password
app.config['MYSQL_DB'] = 'test1'   

# Initialize MySQL
mysql = MySQL(app)

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Example route to insert data into MySQL.
    """
    try:
        # Get data from the request
        name = request.json['name']
        email = request.json['email']
        city = request.json['city']
        gender = request.json['gender']

        # Establish connection and execute query
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user_details (name, email,city,gender) VALUES (%s, %s,%s,%s)", (name, email,city,gender))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'User added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/user', methods=['PUT'])
def update_user():
    try:
        data = request.json
        name = data['name']
        city = data['city']

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE user_details SET city = %s WHERE name = %s", 
                       (city, name))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/users', methods=['DELETE'])
def delete_user():
    try:
        name = request.json['name']
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM user_details WHERE name = %s", (name,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500





@app.route('/userd', methods=['GET'])
def get_user_details():
    try:
        name = request.args.get('name')
        

        cursor = mysql.connection.cursor()

        # Fetch by name
        if name:
            cursor.execute("SELECT name, gender FROM user_details WHERE name = %s", (name,))
            user = cursor.fetchone()
            cursor.close()

            if user:
                result = {'name': user[0], 'gender': user[2]}
                return jsonify(result), 200
            else:
                return jsonify({"message": "User not found"}), 404

        # Fetch count by gender
        elif gender:
            cursor.execute("SELECT COUNT(*) FROM users WHERE gender = %s", (gender,))
            count = cursor.fetchone()[0]
            cursor.close()
            return jsonify({"count": count}), 200

        else:
            return jsonify({"error": "Invalid query parameter"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/city-stats', methods=['GET'])
def get_city_stats():
    try:
        min_age = request.args.get('min_age', type=int)
        max_age = request.args.get('max_age', type=int)

        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT city, COUNT(*) 
            FROM user_details
            WHERE age BETWEEN %s AND %s 
            GROUP BY city
        """, (min_age, max_age))
        stats = cursor.fetchall()
        cursor.close()

        result = {city: count for city, count in stats}
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
