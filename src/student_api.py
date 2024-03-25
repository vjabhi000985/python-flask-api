import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Test data
students = [
    {'roll': 1, 'name': 'Abhijit Kumar', 'branch': 'CS'},
    {'roll': 2, 'name': 'Abhishek Nath', 'branch': 'CS'},
    {'roll': 3, 'name': 'Ashutosh Nath', 'branch': 'IT'},
    {'roll': 4, 'name': 'Bittu Kumar', 'branch': 'EDU'},
    {'roll': 5, 'name': 'Disha Das', 'branch': 'MKT'},
]

# specify a test roll number.
nextStudentRoll = 6


#  --- Helper functions ---
def load_data():
    global students
    with open('students.json') as f:
        students = json.load(f)


def save_data():
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)


def get_student(roll):
    return next((s for s in students if s['roll'] == roll), None)


def student_is_valid(student):
    return 'name' in student


# --- API Endpoints ---
@app.route('/')
def home():
    return "<h1>Hi, This is my first api app using flask!</h1>"


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


@app.route('/students/<int:roll>', methods=['GET'])
def get_student_by_id(roll: int):
    student = get_student(roll)

    if student is None:
        return jsonify({'error': 'Student does not exist.'}), 404
    return jsonify(student)


@app.route('/students', methods=['POST'])
def create_student():
    global nextStudentRoll
    student = request.get_json()

    if not student_is_valid(student):
        return jsonify({'error': 'Invalid student properties.'}), 400

    student['roll'] = nextStudentRoll
    nextStudentRoll += 1
    students.append(student)
    save_data()

    return '', 201, {'location': f'/students/{student["roll"]}'}  # Return empty response with location header


@app.route('/students/<int:roll>', methods=['PUT'])
def update_student(roll: int):
    student = get_student(roll)
    if student is None:
        return jsonify({'error': 'Student does not exist.'}), 404

    updated_student = request.get_json()
    if not student_is_valid(updated_student):
        return jsonify({'error': 'Invalid student properties.'}), 400

    student.update(updated_student)
    save_data()

    return jsonify(student)


@app.route('/students/<int:roll>', methods=['DELETE'])
def delete_student(roll: int):
    global students
    student = get_student(roll)

    if student is None:
        return jsonify({'error': 'Student does not exist.'}), 404

    students = [s for s in students if s['roll'] != roll]
    save_data()

    return jsonify(student), 200


if __name__ == "__main__":
    app.run(debug=True)