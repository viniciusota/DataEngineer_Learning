import boto3
import json
from fake_web_events import Simulation

# Conexão com o Firehose utilizando aws cli e boto3:
client = boto3.client('firehose')



# Função para salvar os eventos gerados no firehose:
def put_record(event):
    data = json.dumps(event) + "\n"
    response = client.put_record(
        DeliveryStreamName='kinesis-firehose-vini',
        Record={"Data": data}
    )
    print(event)
    return response

# Simula eventos de uma pagina web
simulation = Simulation(user_pool_size=100, sessions_per_day=10000)
events = simulation.run(duration_seconds=300)

for event in events:
    put_record(event)



