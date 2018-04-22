docker-compose up
docker run -it --link cassandra_cassandra-1_1:cassandra --rm cassandra cqlsh cassandra