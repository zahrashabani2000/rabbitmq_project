import pika, json, os, django
os.environ.setdefault("DJANGO_SETTING_MODULE", "admin.settings")
dajngo.setup()

from products.models import Product

params = pika.URLParameters('amqps://guaeccua:muAiHT_V_Gf9NXww-tvD7grP7zry-foX@rattlesnake.rmq.cloudamqp.com/guaeccua')

connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recive in rabbitpro')
    data = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.like = product.likes +1
    product.save()
    print('Produck likes increased')


channel.basic.consume(queue='admin', on_massage_callback=callable)

print('Started consuming')

channel.start_consuming()

channel.close()