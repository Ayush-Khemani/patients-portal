"""
TODO: Implement the Patient class.
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""

import requests
from config import DOCTORS, GENDERS, WARD_NUMBERS , ROOM_NUMBERS, API_CONTROLLER_URL
import patient_db_config as pdb
from uuid import uuid4
from datetime import datetime
from patient_db import PatientDB

class patient:
        def __init__(self, name, gender, age):
                self.patient_id = str(uuid4())  
                self.patient_name = name
                self.patient_age = age
                self.patient_gender = gender
                self.patient_checkin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
                self.patient_checkout = None
                self.patient_ward = None
                self.patient_room = None

        def get_id(self):
            return self.patient_id
        
        def get_name(self):
            return self.patient_name
        
        def validate_name(self, name):
            if not isinstance(name, str):
                raise ValueError("Patient name must be a string")
            return name
        
        def validate_age(self, age):
            if not isinstance(age, int) or age <= 0:
                raise ValueError("Patient age must be a positive integer")
            return age
        
        def validate_gender(self, gender):
            if gender not in GENDERS:
                raise ValueError(f"Invalid gender. Valid options are: {', '.join(GENDERS)}")
            return gender
        
        def set_checkout_info(self, ward, room):
            self.patient_checkout = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.patient_ward = self.validate_ward(ward)
            self.patient_room = self.validate_room(room)

        def validate_ward(self, ward):
            if ward not in WARD_NUMBERS:
                raise ValueError(f"Invalid ward number. Valid options are: {', '.join(map(str, WARD_NUMBERS))}")
            return ward
        
        def validate_room(self, room):
            ward = self.patient_ward
            if ward is None:
                raise ValueError("Cannot validate room without specifying ward")
            if str(room) not in ROOM_NUMBERS[ward]:
                raise ValueError(f"Invalid room number for ward {ward}. Valid options are: {', '.join(ROOM_NUMBERS[ward])}")
            return room
        
        def set_ward(self, ward):
            if(ward in WARD_NUMBERS):
                self.patient_ward = ward
                print("Have set the ward sucessfully")
            else:
                print("No such ward")


        def set_room(self, room):
            try:
                if (self.validate_room(room)):
                    self.patient_room = room
                    print("Room has been updated Sucessfully")
            except Exception as e:
                print(e)

        def get_room(self):
            return self.patient_room
        
        def get_ward(self):
            return self.patient_ward
        
        

        def update_room_and_ward(self, ward, room):
            if (ward in WARD_NUMBERS and room in ROOM_NUMBERS[ward]):
                self.patient_ward = ward
                self.patient_room = room
                print("Room and ward updated successfully.")
            else:
                print("Invalid ward or room number.")


        def commit(self):
            database = PatientDB()
            existing_patient = database.fetch_patient_id_by_name(self.patient_name)
            print(len(existing_patient))
            if (len(existing_patient) == 0):
                database.insert_patient(self.__dict__)
            else:
                print("Patient with the same name already exists.")

                patient_id = existing_patient[0]['patient_id']
                update_dict = self.__dict__
                update_dict['patient_checkin'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_dict['patient_checkout'] = None
                database.update_patient(patient_id, update_dict)