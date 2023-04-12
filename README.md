# Kafka Cluster com KRaft no Docker Compose

O objetivo desse repositório é permitir a execução de um cluster Kafka utilizando o KRaft ao invés do Zookeeper, o uso do Kafka UI para facilitar a interação do usuário com o cluster. Além de um simples producer para testar o cluster.

Acesse o post no Medium em que falo mais sobre esse código. 
https://medium.com/@cmendesfirmino/criando-um-cluster-kafka-com-o-kraft-adeus-zookeeper-e-docker-compose-fa47fe616104

## Etapas de execução

- Para iniciar o cluster.

```bash
docker-compose up
```

- Para executar o producer, executar os passos abaixo:
```bash
pip install -m venv .venv
source .venv/bin/activate

pip install sseclient
pip install kafka-python

python producer/wikimedia.py
```

- Para conectar o Kafka-UI
http://localhost:8080

