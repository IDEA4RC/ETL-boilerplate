import mysql.connector

db_config = {
    'user': 'admin',
    'password': 'admin',
    'host': 'mysql-idea4rc-service.datamesh.svc.cluster.local', 
    'database': 'idea4rc',
}

connection = mysql.connector.connect(**db_config)

print("Is database connected: " + str(connection.is_connected()))