'''import mysql.connector

db_config = {
    'user': 'admin',
    'password': 'admin',
    'host': 'mysql-idea4rc-service.datamesh.svc.cluster.local', 
    'database': 'idea4rc',
}

connection = mysql.connector.connect(**db_config)

print("Is database connected: " + str(connection.is_connected()))
'''

import requests
import json
import omop

def get_json_data():
  response = requests.get("http://localhost:3000/pacientes/1")
  return response.json()

def convert_json_to_cdm(json_data):
  patient = omop.Patient()
  patient.set_id(json_data["id"])
  patient.set_name(json_data["nombre"])
  patient.set_surnames(json_data["apellidos"])
  patient.set_gender(json_data["sexo"])
  return patient

def save_cdm_to_postgres(cdm_data):
  connection = omop.connect_to_postgres("postgres://postgres:password@localhost:5432/omop")
  omop.save_patient(connection, cdm_data)

def main():
  json_data = get_json_data()
  cdm_data = convert_json_to_cdm(json_data)
  save_cdm_to_postgres(cdm_data)

if __name__ == "__main__":
  main()
