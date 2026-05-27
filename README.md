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