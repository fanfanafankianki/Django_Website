from celery import Celery
import pika
import random
import string

  # INSTALL amqp tools               > apt-get update > apt-get install amqp-tools 
  # amqp-declare-queue -u amqp://user:password@my_rb:5672/my_vhost -q moja_kolejka
  # amqp-publish -u amqp://user:password@my_rb:5672/my_vhost -r moja_kolejka -b 'Testowa wiadomosc’
  #
  #GO INTO RABBITMQ CONTAINER       > docker exec -it RABBITMQ_CONTAINER /bin/bash
  #check ques                       > rabbitmqctl list_queues -p my_vhost
  #GET QUEUE                        > rabbitmqadmin --username=user --password=password get queue=moja_kolejka --vhost=my_vhost
  #DELETE QUEUE                     > rabbitmqadmin --username=user --password=password -V my_vhost delete queue name=moja_kolejka

rmq_config = {
    "host": "myrb",
    "user": "user",
    "password": "password",
    "port": "5672",
    "vh": "my_vhost"
}

app = Celery('myapp')

def create_queue_and_send_message(queue_name,name,description,imagePath):
    #save(id,name,description,imagePath)
    message_body=f'{name}&&{description}&&{imagePath}'
    credentials = pika.PlainCredentials(rmq_config['user'], rmq_config['password'])
    connection_params = pika.ConnectionParameters(
        host=rmq_config['host'],
        port=int(rmq_config['port']),
        virtual_host=rmq_config['vh'],
        credentials=credentials
    )
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message_body)
    connection.close()


def consume_messages(queue_name):
    array=[]
    credentials = pika.PlainCredentials(rmq_config['user'], rmq_config['password'])
    connection_params = pika.ConnectionParameters(
        host=rmq_config['host'],
        port=int(rmq_config['port']),
        virtual_host=rmq_config['vh'],
        credentials=credentials
    )
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
        if method_frame:
            formatted = body.decode('utf-8')
            element1 = formatted.split("&&")[0]
            element2 = formatted.split("&&")[1]
            element3 = formatted.split("&&")[2]
            created_array = [element1, element2, element3]
            array.append(created_array)
            print("created_array")
            print(created_array)
            print("created_array")
        else:
            print('Brak wiadomości w kolejce.')
            break  # Zakończ pętlę gdy kolejka jest pusta

    connection.close()
    return array
