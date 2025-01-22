# Flask Sample App with Tests


### Getting Started
To get the Flask app up and running on your local machine, follow these steps:

1. Clone the Repository:

git clone <repository_url>
cd sample-flask-app <br>

2. Set Up a Virtual Environment:

It's recommended to create a virtual environment to isolate project dependencies. <br>

`python -m venv venv` 
`source venv/bin/activate`  # On Windows, use venv\Scripts\activate <br>

3. Install Dependencies:
Install the necessary dependencies using pip: <br>

`pip install -r requirements.txt`

4. Run the Application:

Start the Flask application: <br>

`python run.py`
The app will be available at http://localhost:5000. <br>

5. Run Tests:

To run the unit tests, execute the following command: <br>

`python -m unittest discover tests`