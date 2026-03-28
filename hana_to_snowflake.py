from hdbcli import dbapi

conn = dbapi.connect(
    address="9a8103fe-919e-4695-a8d2-eee9ecbb675b.hana.prod-ap21.hanacloud.ondemand.com",
    port=443,
    user="DBADMIN",
    password="myHanaDb@2026",
    encrypt=True,
    sslValidateCertificate=False
)

cursor = conn.cursor()

cursor.execute("SELECT CURRENT_DATE FROM DUMMY")

print(cursor.fetchall())

cursor.close()
conn.close()