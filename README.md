Setting Up Env: 
```
sudo make run
pip install -r requirements.txt
cassandra-migrate migrate
```

docker-compose up <br/>
docker run -it --link cassandra_cassandra-1_1:cassandra --rm cassandra cqlsh cassandra

Currently the API and Cassandra are deployed to cloud (Google Computing Engine) and the Transaction Servive could be accessed 
on machine with the following HTTP request (where X.X.X.X - is machine ip address and Y is port): <br>
If you are intended to use deployed version, please ask us for them privately
```
curl -X POST \
  http://X.X.X.X:Y/create_transaction/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: ab108467-ba96-48d2-757e-7b2686ad2c9d' \
  -d '{"attendee_id": 2, "product_id":2, "shop_id":3, "amount":20}'
  ```
