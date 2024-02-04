from django.db import connection




#TABLE SCHEMA = CREATE TABLE customers (firstname text, lastname text); #SET IN init.db file
# psql -h localhost -U postgres
# \c testing_db
# SELECT * FROM angular;
# \q
#truncate angular;  EMPTY TABLE





 #OBJECT EXAMPLE: {'name': 'ghghgh', 'imagePath': 'ghgh', 'description': 'ghghgh', 'products': []}
  # print(f'Name={name},image_path={image_path},description={description},products={products}')


def add_to_database(name,description,imagePath):
  #save(id,name,description,imagePath)
    with connection.cursor() as cursor:
        command = "INSERT INTO angular (name,description,imagePath) VALUES (%s, %s, %s)"
        cursor.execute(command, (name,description,imagePath))

def drop():
    with connection.cursor() as cursor:
        command = "truncate angular;"
        cursor.execute(command)

def get():
    with connection.cursor() as cursor:
        command = "SELECT * FROM angular;"
        cursor.execute(command)
        result = cursor.fetchall()
    return result