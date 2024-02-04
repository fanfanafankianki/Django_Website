from .Rabbit.rabbitmq import create_queue_and_send_message
from .Rabbit.rabbitmq import consume_messages
from .Postgress.postgress import add_to_database
from .Postgress.postgress import drop
from .Postgress.postgress import get
from .Memcached.memcached import get_with_memcached
from .Memcached.memcached import addToMemcached
import random
import string



def save(name,description,imagePath): 
    queue='kolejka'
    create_queue_and_send_message(queue, name, imagePath, description)
    arrayFromRabbit=consume_messages(queue)
    print("arra")
    print(arrayFromRabbit)
    print("arra")
    for data in arrayFromRabbit:
        name = data[0]
        imagePath = data[1]
        description = data[2]
        add_to_database(name,description,imagePath)

def get_all_records():
   print("Try to get from memcached")
   getFromMemcached=get_with_memcached()
   if getFromMemcached:
       print("getFromMemcached")
       print(getFromMemcached)
       print("getFromMemcached")
       return getFromMemcached
   else:
        print("Fetched not from memcached")
        dataFromDatabase = get()
        addToMemcached(dataFromDatabase)
        return dataFromDatabase

    
def dropDatabase():
    drop()
