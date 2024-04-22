from patient import Patient
import requests

patient1 = Patient("Fahad", "Male", 25)

uri = "http://127.0.0.1:5000"

def get_patient_by_id(uri, id):
    uri = f"{uri}/patients/{id}"
    response = requests.get(uri)
    return response.json()

def test_one():
    try:
        patient1.set_room(32)
        patient1.set_ward(3)
        patient1.commit()
        response = get_patient_by_id(uri, patient1.get_id())
        if response['patient_id'] == patient1.get_id() and response["patient_name"] == patient1.get_name():
            print("test one passed")
        else :
            print("test one failed")
    except Exception as e:
        print("test one failed, raised exception: ", e)

def test_two():
    try:
        patient1.set_ward(2)
        patient1.set_room(23)
        patient1.commit()
        response = get_patient_by_id(uri, patient1.get_id())
        if response['patient_id'] == patient1.get_id() and response["patient_name"] == patient1.get_name():
            if int(response["patient_room"]) == int(patient1.get_room()) and int(response["patient_ward"]) == int(patient1.get_ward()):
                print("test two passed")
            else:
                print(response['patient_room'], response['patient_ward'])
                print(patient1.get_room(), patient1.get_ward())
                print("test two failed.")
        else :
            print("test two failed..")
    except Exception as e:
        print("test two failed, raised exception: ", e)

test_one()
test_two()



