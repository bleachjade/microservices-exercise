
import pika, json

params = pika.URLParameters('amqps://kpsgfwzg:aqq0NUELhecCOJ9dxg0JGRMmLmXvPLnD@clam.rmq.cloudamqp.com/kpsgfwzg')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)