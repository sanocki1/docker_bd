## Odpalanie
```bash
docker compose up --build
```

## Endpoint 
http://localhost:5000/

## Wylaczanie
```bash
docker compose down
```
Jesli chcesz usunac wolumeny:
```bash
docker compose down -v
```

## Setup MongoDB replikacja
```bashbash
docker exec -it mongo_kontener1 mongosh

rs.initiate({
_id: "rs0",
  members: [
    { _id: 0, host: "mongo_kontener1:27017", priority: 2 },
    { _id: 1, host: "mongo_kontener2:27017", priority: 1 },
    { _id: 2, host: "mongo_kontener3:27017", priority: 1 }
  ]
 });
 
rs.status()

docker network ls - wyświetla sieci
```

## Testowanie baz
### MySQL
```bash
docker exec -it mysql_kontener bash
mysql -u root -p
q
use wydarzenia;
```
### MongoDB
```bash
docker exec -it mongo_kontener mongosh
use logs_db
db.audit_logs.find()
```