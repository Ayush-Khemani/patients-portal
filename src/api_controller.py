"""Patient API Controller"""

from flask import Flask, request, jsonify
from patient_db import PatientDB
from patient import patient


class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()
        self.run()

    def setup_routes(self):
        """
        Sets up the routes for the API endpoints.
        """
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)


    """
    TODO:
    Implement the following methods,
    use the self.patient_db object to interact with the database.

    Every method in this class should return a JSON response with status code
    Status code should be 200 if the operation was successful,
    Status code should be 400 if there was a client error,
    """

    def create_patient(self):
        request_body = request.json
        patient_id = self.patient_db.insert_patient(request_body)
        # print(patient_id)
        if patient_id:
            response_body = {"patient_id": patient_id}
            status_code = 200
        else:
            response_body = {"error": "Failed to create patient"}
            status_code = 400
        return jsonify(response_body), status_code

    def get_patients(self):
        patients = self.patient_db.select_all_patients()
        if patients is not None:

            patient_ids = [patient["patient_id"] for patient in patients]
            return jsonify({"patient_ids": patient_ids}), 200
        else:
            return jsonify({"error": "Failed to retrieve patients"}), 400
    
    def get_patient(self, patient_id):
        patient = self.patient_db.select_patient(patient_id)
        if patient is not None:
            return jsonify(patient), 200
        else:
            return jsonify({"error": f"Patient with ID {patient_id} not found"}), 404

    def update_patient(self, patient_id):
        request_body = request.json
        updated_rows = self.patient_db.update_patient(patient_id, request_body)
        if updated_rows is not None and updated_rows > 0:
            return jsonify({"message": "Patient updated successfully"}), 200
        elif updated_rows == 0:
            return jsonify({"error": f"Patient with ID {patient_id} not found"}), 404
        else:
            return jsonify({"error": "Failed to update patient"}), 400


    def delete_patient(self, patient_id):
        deleted_rows = self.patient_db.delete_patient(patient_id)
        if deleted_rows is not None and deleted_rows > 0:
            return jsonify({"message": "Patient deleted successfully"}), 200
        elif deleted_rows == 0:
            return jsonify({"error": f"Patient with ID {patient_id} not found"}), 404
        else:
            return jsonify({"error": "Failed to delete patient"}), 400


    def run(self):
        """
        Runs the Flask application.
        """
        self.app.run()


PatientAPIController()
