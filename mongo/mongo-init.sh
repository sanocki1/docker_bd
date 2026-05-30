#!/bin/sh
set -e

echo "Czekam na MongoDB..."

until mongosh --host mongo1 --eval "db.adminCommand('ping')" >/dev/null 2>&1; do
  sleep 2
done

echo "MongoDB gotowe, inicjalizuję replica set..."

mongosh --host mongo1 <<EOF
try {
  rs.status()
  print("Replica set już istnieje")
} catch (e) {
  rs.initiate({
    _id: "rs0",
    members: [
      { _id: 0, host: "mongo1:27017", priority: 2 },
      { _id: 1, host: "mongo2:27017", priority: 1 },
      { _id: 2, host: "mongo3:27017", priority: 1 }
    ]
  })
  print("Replica set zainicjalizowany")
}
EOF