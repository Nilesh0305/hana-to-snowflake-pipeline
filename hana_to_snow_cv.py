from hdbcli import dbapi
import pandas as pd

# Connection details (from latest JSON)
HOST = "9a8103fe-919e-4695-a8d2-eee9ecbb675b.hana.prod-ap21.hanacloud.ondemand.com"
PORT = 443

# ✅ Updated RT user
USER = "MYFIRSTPROJECTCONNECTION_HDI_DB_1_DWNMEMLHJGFXFQ1AG3UAD3ASL_RT"

# ✅ Updated password
PASSWORD = r"""C[t4ILs%K#VXWp.t#k)~H%Hq6LQ#S55.NuE;-4_Smb`[hKbb4-`.+#UmHzGCipRoDAL|9W<#QG3t2yH3O!;+EdoW).Dn!u92Ve4{QMR#]#_/fO7Ca=s~3!C0LZ8^dZ:f"""

# Connection
conn = dbapi.connect(
    address=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    encrypt=True,
    sslValidateCertificate=False
)

cursor = conn.cursor()

# Query
query = """
SELECT
    "DAY",
    "TNR",
    "TTYP",
    SUM("DISTINCT_TX") AS "DISTINCT_TX"
FROM "MYFIRSTPROJECTCONNECTION_HDI_DB_1"."CV_TRANSPARENT_EXAMPLE"
GROUP BY "DAY", "TNR", "TTYP"
"""

cursor.execute(query)

# Fetch data
data = cursor.fetchall()

# Column names
columns = [col[0] for col in cursor.description]

# Convert to DataFrame
df = pd.DataFrame(data, columns=columns)

print(df)

# Close connection
cursor.close()
conn.close()