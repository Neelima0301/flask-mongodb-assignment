# Flask MongoDB Assignment

This project is part of my Flask and GitHub assignment. In this assignment, I worked with Flask, GitHub branches, JSON, MongoDB Atlas and a To-Do form.

I completed the work by creating different branches, making the required changes, merging the branches and working with Git reset and rebase.

## Technologies I Used

* Python
* Flask
* MongoDB Atlas
* PyMongo
* HTML
* JSON
* Git
* GitHub

## Project Files

* `app.py` - Main Flask application
* `data.json` - JSON data used by the `/api` route
* `templates/index.html` - Student form
* `templates/success.html` - Success page
* `templates/todo.html` - To-Do form
* `.env.example` - Example for MongoDB connection
* `.gitignore` - Files to ignore in Git
* `requirements.txt` - Required Python packages
* `README.md` - Project information

## Question 1 - GitHub Repository and Flask Project

I created a GitHub repository and cloned it to my local system using SSH.

I created a branch using my username and added the Flask project files to the branch.

After committing the changes, I merged the branch into the main branch.

The Flask project also contains an `/api` route which reads the data from `data.json` and returns it as JSON.

## Question 2 - JSON Update and Branch Merge

I created a new branch named:

```text
Neelima_new
```

I updated the JSON file used by the `/api` route in this branch.

After making the changes, I merged the branch into the main branch.

The changes were committed and pushed to the GitHub repository.

## Question 3 - To-Do Page and MongoDB Backend

I created two branches from the main branch:

```text
master_1
master_2
```

### master_1

In the `master_1` branch, I created the To-Do page.

The form contains:

* Item Name
* Item Description

### master_2

In the `master_2` branch, I created the backend route:

```text
/submittodoitem
```

This route accepts the To-Do item name and description using a POST request and stores the data in MongoDB Atlas.

I then merged the changes from both branches into the main branch.

## Question 4 - To-Do Item ID, UUID and Hash

In the `master_1` branch, I added the following fields to the To-Do form:

* Item ID
* Item UUID
* Item Hash

I added and committed these fields separately in the required order.

The commits were made as:

1. Add Item ID field
2. Add Item UUID field
3. Add Item Hash field

The changes were then merged into the main branch.

### Git Reset

After merging, I used `git reset --soft` to roll back the main branch to the commit where only the Item ID field was added.

The changes were kept staged and I committed the required state again.

### Git Rebase

I then rebased the updated changes from the main branch into the `master_1` branch.

I preserved the individual commits for Item ID, Item UUID and Item Hash instead of combining them into one commit.

## MongoDB

The Flask application uses MongoDB Atlas to store the submitted To-Do items.

The database used in the project is:

```text
studentDB
```

The collections used are:

```text
students
todoitems
```

Each To-Do item contains:

```text
itemId
itemUuid
itemHash
itemName
itemDescription
```

The Item UUID is generated using Python's UUID library.

The Item Hash is generated using SHA-256.

## API Routes

The main routes used in the project are:

```text
/                  - Student form
/success           - Success page
/api               - Returns data from data.json
/todo              - To-Do page
/api/todos         - Returns To-Do items from MongoDB
/submittodoitem    - Stores a To-Do item in MongoDB
```

## How I Run the Project

First, I install the required packages:

```bash
pip install -r requirements.txt
```

I keep my MongoDB connection string in a `.env` file using:

```text
MONGO_URI=your_mongodb_connection_string
```

Then I run the Flask application:

```bash
python app.py
```

The application can be opened at:

```text
http://127.0.0.1:5000
```

## Note

I have not included my `.env` file in the submission because it contains my MongoDB connection string.

The `.env.example` file is included as an example.


## Additional Git Evidence

### Question 2 - Merge Conflict Resolution

To demonstrate the required merge conflict resolution, I created a controlled conflict in `data.json`.

The conflict occurred because `data.json` was modified in both the current branch and the `Neelima_new` branch.

The merge command was:

```bash
git merge Neelima_new
```

Git reported the conflict:

```text
Auto-merging data.json
CONFLICT (content): Merge conflict in data.json
Automatic merge failed; fix conflicts and then commit the result.
```

The conflict markers in `data.json` showed changes from both branches:

```text
[HEAD version]
        "course": "Information Technology"

[Neelima_new version]
        "course": "Computer Science"
    },
    {
        "id": 3,
        "name": "Student 3",
        "course": "Data Science"
```

As required, I resolved the conflict by accepting the changes from the `Neelima_new` branch:

```bash
git checkout --theirs data.json
git add data.json
git commit -m "Merge Neelima_new and resolve data.json conflict"
```

The final `data.json` contained the changes from `Neelima_new`:

```json
[
    {
        "id": 1,
        "name": "Neelima",
        "course": "MCA"
    },
    {
        "id": 2,
        "name": "Student 2",
        "course": "Computer Science"
    },
    {
        "id": 3,
        "name": "Student 3",
        "course": "Data Science"
    }
]
```

The merge was completed successfully and the working tree was clean.

### Question 5 - Git Reset --soft Evidence

I demonstrated the `git reset --soft` operation using a separate evidence branch.

The command used was:

```bash
git reset --soft 531bdf9
```

Immediately after the reset, `git status` showed that the changes were still staged:


```text
Changes to be committed:

        modified:   app.py
        modified:   templates/todo.html
```

This demonstrates that `git reset --soft` keeps changes staged.

I then recommitted the staged changes:

```bash
git commit -m "Recommit changes after soft reset"
```

### Git Rebase Evidence

I verified the rebase operation using:

```bash
git reflog --all --grep-reflog="rebase"
```

The reflog showed the rebase start, continuation and completion.

The `master_1` history preserved the individual commits for the Item ID, Item UUID and Item Hash changes.

### GitHub Repository Verification

The completed project was pushed to the `master_1` branch of my GitHub repository.

Repository:

https://github.com/Neelima0301/flask-mongodb-assignment

Final branch:

```text
master_1
```

Final commit:

```text
61103d6 Complete assignment requirements and production improvements
```

The final Git status was:

```text
On branch master_1
Your branch is up to date with 'origin/master_1'.

nothing to commit, working tree clean
```

### Submission Files Verification

The submission contains the required project files:

```text
app.py
data.json
README.md
.env.example
.gitignore
requirements.txt
templates/index.html
templates/todo.html
templates/success.html
```

The `.env` file containing the MongoDB connection string is not included in the submission.
