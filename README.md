# Patients Portal

## Introduction

Patient Portal is a basic Patient management system, where the user (ie. receptionist) should do the folowing tasks:
- **List Patients:**
- **List Patients with a given name:**
- **Read a Patient with certain id:**
- **Create a Patient:**
- **Update the data of a Patient:**
- **Delete a Patient:**

## Prerequisites

- Install **Python** (recommended version >= 3.10)
- Install **Gitbash** (Optional)

## Installation Steps

Follow these steps to install the repository requirements:

1. **Fork this Repository**
Click on button:
![image](https://github.com/amhkhowaja/patients-portal-for-students/assets/63882136/be42fa88-157b-44b8-a1f4-31a2083dd983)

Then,
Rename the repo name to *patients-portal* and click Create Fork.

2. **Clone the Repository from your list of repositories:**

```bash
git clone https://github.com/<your-username>/patients-portal.git
```

3. **Navigate to the Repository:**
```bash
cd patient-portal
```

4. **Create a virtual environment**
```bash
python -m venv venv
```

5. **Activate the virtual environment**

*In linux (gitbash)*

```bash
source venv/bin/activate
```

*In windows*
```bash
.\\venv\Scripts\activate.bat
```

6. **Install python packages to run the application**
```bash
python -m pip install -r requirements.txt
```

## Development

You can check the whole repository to check how the workflow works.

Here is the breakdown:

- (`src`) directory contains the main source code
    1. (`src/patient.py`) will contain the Patient class for the behaviour of patients. The patient object should be used for testing the application. 
    **Details implementations are in the file.**
    2. (`src/patient_db.py`) contains the business logic of sqlalchemy database operations. The module can be imported for the database operation.
    3. (`src/config.py`) contains basic hardcoded configurations. This needs to be imported for the business logic.
    4. (`src/patient_db_config.py`) is a script which creates the (`patient.db`) file and configure the database schema.
    5. (`src/api_controller.py`) will contain the class for the HTTP REST API controller server. There are predefined routes, so that when the Client sends the request. the server should validate the data and fetch/store the data to the database.
    **You need to implement only the methods**

- (`tests`) directory contains the tests for your application.

- (`requirements.txt`) contains the packages needs to be installed for the application to run. you can append a 3pp (3rd Party Package) in this file if you have used any.

## Testing the APIs
You can use the git bash to execute these shell commands if you don't have the linux or wsl.

In Terminal :

First Run the flask server by running the API_CONTROLLER (`src/api_controller.py`) directly or using linux command:
```bash
python src/api_controller.py
```
Once the Flask server is running, open a new terminal and keep the server running in the first one.

Then,
```bash
cd tests
```

Then,
```bash
bash create_patient.sh
```

If it returns the patient_id in the response then meaning that Patient has been created successfully and added to the database.

Then for listing the created patients,
```bash
bash list_patients.sh
```

Then for listing the created patients with \*name\* as parameter,
```bash
bash list_patient_by_name.sh
```

Then for getting a patient details with certain id,
```bash
bash get_certain_patient.sh
```

Then, to update the patient,
```bash
bash update_patient.sh
```

Finally, to delete the created patient,
```bash
bash delete_patient.sh
```
## Testing the Final Application
This is E2E test case, which is going to test the functionality of the patient portal:

It creates the patient object from the Patient class and commits the patient to the database using the client request.

Test 1 (basic):
Simple test case for the creating the patient object and commiting it.

Test 2 (validation of room and ward):
it is invoked after Test 1 for the same patient. Therefore you need to think of the business logic for the commit method in patient.py that when the first patient is created, it can not be created again therefore it has to be updated using (PUT) request. 

```bash
python src/test_application.py
```

## You can Refer:

Flask Documentation: https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing

Flask Cheatsheet: https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf

Swagger Editor (Playground): https://editor.swagger.io/

Python OOP : https://docs.python.org/3/tutorial/classes.html


## Feedback

If you need more clarification, please ping me. I will update the readme file.
