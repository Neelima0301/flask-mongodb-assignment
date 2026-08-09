# Flask MongoDB Form Project

This is my Flask project where I made a simple form.

When the form is submitted, the data is saved in MongoDB Atlas.

I also made an `/api` route which reads data from `data.json` and returns it.

## I used

- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML
- JSON
- python-dotenv

## Files in my project

- `app.py` - Flask application
- `data.json` - data used for the API
- `index.html` - form page
- `success.html` - page shown after successful submission
- `.env.example` - example for the MongoDB connection
- `.gitignore` - files that should not be uploaded
- `requirements.txt` - required Python packages

The HTML files are inside the `templates` folder.

## How I run the project

First I activate my virtual environment.

Then I install the required packages using:

pip install -r requirements.txt

I have a `.env` file in my project folder which contains my MongoDB connection string.

After that I run:

python app.py

Then I open this in my browser:

http://127.0.0.1:5000

## How the form works

I enter the details in the form and click the submit button.

Flask receives the form data and saves it in MongoDB Atlas.

then the data is saved successfully, it opens the success page.

and If there is any error, the error is shown on the same page.

## API

The `/api` route reads the data from `data.json` and returns it.

## Note

I have not included my `.env` file because it contains my MongoDB connection string.
