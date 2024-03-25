# Student API with Flask ‍
This is a basic Flask application that implements a simple Student API. You can use this API to manage student data (CRUD operations: Create, Read, Update, Delete).

## Prerequisites:
- Python 3.x (https://www.python.org/downloads/)
- Flask (https://flask.palletsprojects.com/)
- APIDOG for testing (https://apidog.com)

## Running the Application:
1. Clone or download this repository ```git clone https://github.com/vjabhi000985/python-flask-api.git```
2. Install the required dependencies: ```pip install flask json```
3. Run the Flask application: ```python student_api.py```

This will start the Flask development server, typically running on http://127.0.0.1:5000 by default.

## Testing Endpoints:

### Test Case 1: Get All Students (GET /students)
  - In the Apidog editor, navigate to the GET /students endpoint.
  - Click "Send". You should see a response with a JSON array containing all student objects (refer to screenshot.

### Test Case 2: Get Student by ID (GET /students/<int:roll>)
  - Navigate to the GET /students/{roll} endpoint (replace {roll} with a valid student ID).
  - Click "Send". You should see a response with the details of the specific student if it exists. Otherwise, expect a 404 Not Found error. 

### Test Case 3: Create a New Student (POST /students)
  - Navigate to the POST /students endpoint.
  - Click on the "Body" tab and select "JSON".
  - Paste the following JSON data into the body, replacing placeholders with desired values:
  ``` JSON
 {
   "name": "John Doe",
   "branch": "Computer Science"
 }
 # Use code with caution.
 ```
 - Click "Send". You should receive a status code 201 Created and a Location header pointing to the newly created student's resource URL.

### Test Case 4: Update a Student (PUT /students/<int:roll>)
  - Navigate to the PUT /students/{roll} endpoint (replace {roll} with a valid student ID).
  - In the Body tab, provide updated student information in JSON format (e.g., update the name).
  - Click "Send". You should receive a status code 200 OK and the updated student data in the response.

### Test Case 5: Delete a Student (DELETE /students/<int:roll>)
  - Navigate to the DELETE /students/{roll} endpoint (replace {roll} with a valid student ID).
  - Click "Send". You should receive a status code 200 OK with the deleted student's information in the response (optional, depending on your implementation).
