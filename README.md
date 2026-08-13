# Flask MongoDB Assignment

This is my Flask and MongoDB assignment. In this project, I worked with Flask, MongoDB Atlas, HTML, JSON, Git and GitHub.

I also worked with Git branches, merging, merge conflicts, Git reset and Git rebase as required in the assignment.

## Technologies Used

- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML
- JSON
- Git
- GitHub

## Project Files

- app.py - Main Flask application
- data.json - JSON data used by the /api route
- templates/index.html - Student registration form
- templates/todo.html - To-Do form
- templates/success.html - Success page
- .env.example - Example MongoDB connection string
- .gitignore - Files ignored by Git
- requirements.txt - Required Python packages
- README.md - Project information

---

## Question 1 - GitHub Repository and Flask Project

First, I created the GitHub repository and cloned it to my computer using Git.

I created a branch named:

Neelima0301

I added the Flask project files and committed the changes.

The Flask application contains an /api route. This route reads the data from data.json and returns the data as JSON.

After completing the work, I merged the branch into the main branch.

---

## Question 2 - JSON Update and Branch Merge

For Question 2, I created a branch named:

Neelima_new

I updated data.json in this branch by adding the required student information.

After that, I merged the branch into the main branch.

### Merge Conflict Evidence

I also demonstrated a real merge conflict in data.json using a separate branch:

q2-real-conflict

The merge conflict was resolved and committed with:

e3edd2d Merge Neelima_new and resolve data.json conflict

The reflog also records the merge commit:

e3edd2d HEAD@{Wed Aug 12 19:54:16 2026}: commit (merge): Merge Neelima_new and resolve data.json conflict

I resolved the conflict in data.json, added the resolved file and completed the merge commit.

---

## Question 3 - To-Do Page and MongoDB Backend

For Question 3, I created two branches:

master_1
master_2

### master_1

I worked on the To-Do page in master_1.

The To-Do form contains:

- Item Name
- Item Description

The Item ID, Item UUID and Item Hash are generated automatically by the Flask backend.

### master_2

I worked on the backend in master_2.

The backend route is:

/submittodoitem

This route accepts the To-Do item name and description and stores the item in MongoDB Atlas.

The To-Do items are stored in the todoitems collection.

I also added an API route to retrieve the stored To-Do items:

/api/todos

---

## Question 4 - Item ID, UUID and Hash

For Question 4, I worked with the Item ID, Item UUID and Item Hash changes using separate Git commits.

The relevant commits in my Git history include:

531bdf9 Add Item ID field
4cc8270 Add Item UUID field
ff4ede8 Add generated Item ID UUID and Hash

These changes were made through separate Git commits during the assignment work.

In the final application, the Item ID, UUID and Hash are generated automatically by the Flask backend when a To-Do item is submitted.

The generated fields are:

itemId
itemUuid
itemHash

The UUID is generated using Python's uuid library.

The Item Hash is generated using SHA-256.

The final To-Do document also contains:

itemName
itemDescription

Therefore, a stored To-Do item contains:

itemId
itemUuid
itemHash
itemName
itemDescription

---

## Git Reset --soft Evidence

I demonstrated the git reset --soft operation using a separate evidence branch:

q5-soft-reset-evidence

The reflog records the reset operation:

531bdf9 refs/heads/q5-soft-reset-evidence@{Wed Aug 12 19:56:04 2026}: reset: moving to 531bdf9
531bdf9 HEAD@{Wed Aug 12 19:56:04 2026}: reset: moving to 531bdf9

After the reset, I recommitted the changes with:

02443d2 Recommit changes after soft reset

This demonstrates that I used git reset --soft and then recommitted the staged changes.

---

## Git Rebase Evidence

I also demonstrated Git rebase and verified the operation using the Git reflog.

The reflog records the rebase process:

10cdeb3 HEAD@{Tue Aug 11 18:44:14 2026}: rebase (start): checkout main
4cc8270 HEAD@{Tue Aug 11 18:50:58 2026}: rebase (continue): Add Item UUID field
4cc8270 HEAD@{Tue Aug 11 18:54:55 2026}: rebase (finish): returning to refs/heads/master_1

This shows the start, continuation and completion of the rebase operation.

---

## MongoDB Atlas

I used MongoDB Atlas to store the student information and To-Do items.

The database name is:

studentDB

The collections used by the application are:

students
todoitems

The students collection stores student information submitted through the student form.

The todoitems collection stores To-Do items with:

itemId
itemUuid
itemHash
itemName
itemDescription

The MongoDB connection string is stored in the local .env file and is not included in the submission.

---

## Flask Routes

The main routes in my application are:

/                  - Student registration form
/submit            - Submit student information
/success           - Success page
/api               - Returns data from data.json
/todo              - To-Do page
/submittodoitem    - Submit a To-Do item
/api/todos         - Get To-Do items from MongoDB
/health            - Check application and MongoDB health

---

## Input Validation and Error Handling

I added basic input validation to the Flask application.

The application checks that required text fields are not empty and also applies maximum length limits.

MongoDB errors and unexpected application errors are handled with appropriate error responses and logging.

The /health route can be used to check whether the application can connect to MongoDB.

---

## requirements.txt

The project uses the following Python packages:

Flask==3.1.3
pymongo==4.17.0
python-dotenv==1.2.2

---

## .gitignore

The .gitignore file contains:

.env
venv/
__pycache__/
*.pyc

The .env file is ignored because it contains my private MongoDB connection string.

---

## .env.example

I included .env.example with a sample MongoDB connection string:

MONGO_URI=mongodb+srv://USERNAME:PASSWORD@cluster0.xxxxx.mongodb.net/?appName=Cluster0

The actual .env file is not included in the submission.

---

## GitHub Repository

My GitHub repository is:

https://github.com/Neelima0301/flask-mongodb-assignment

The final working branch is:

master_1

The latest README update was committed to the local master_1 branch.

---

## How to Run the Project

First, install the required Python packages:

pip install -r requirements.txt

Create a .env file in the project folder and add the MongoDB connection string:

MONGO_URI=your_mongodb_connection_string

Then run the Flask application:

python app.py

The application runs at:

http://127.0.0.1:5000

The To-Do page can be opened at:

http://127.0.0.1:5000/todo

---

## Submission Files

The submission contains the required project files:

app.py
data.json
README.md
.env.example
.gitignore
requirements.txt
templates/index.html
templates/todo.html
templates/success.html

The actual .env file is not included because it contains my private MongoDB connection string.

---

## Final Git Status

The final project should be checked before submission using:

git status

The expected result is:

On branch master_1
nothing to commit, working tree clean

The final master_1 branch should also be pushed to GitHub before submitting the assignment.