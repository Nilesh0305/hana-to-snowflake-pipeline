from hdbcli import dbapi
import pandas as pd
import snowflake.connector  # ✅ FIX 1

# ---------------------------
# HANA CONNECTION
# ---------------------------
HOST = "9a8103fe-919e-4695-a8d2-eee9ecbb675b.hana.prod-ap21.hanacloud.ondemand.com"
PORT = 443
USER = "MYFIRSTPROJECTCONNECTION_HDI_DB_1_DWNMEMLHJGFXFQ1AG3UAD3ASL_RT"

PASSWORD = r"""C[t4ILs%K#VXWp.t#k)~H%Hq6LQ#S55.NuE;-4_Smb`[hKbb4-`.+#UmHzGCipRoDAL|9W<#QG3t2yH3O!;+EdoW).Dn!u92Ve4{QMR#]#_/fO7Ca=s~3!C0LZ8^dZ:f"""

hana_conn = dbapi.connect(
    address=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    encrypt=True,
    sslValidateCertificate=False
)

hana_cursor = hana_conn.cursor()

query = """
SELECT
    "DAY",
    "TNR",
    SUM("DISTINCT_TX") AS "ROW_COUNT"
FROM "MYFIRSTPROJECTCONNECTION_HDI_DB_1"."CV_TRANSPARENT_EXAMPLE"
GROUP BY "DAY", "TNR"
"""

hana_cursor.execute(query)

columns = [col[0] for col in hana_cursor.description]
data = hana_cursor.fetchall()

df = pd.DataFrame(data, columns=columns)

print("Data from HANA:")
print(df)

# ---------------------------
# SNOWFLAKE CONNECTION
# ---------------------------
sf_conn = snowflake.connector.connect(
    user="NileshNK91",
    password="Snowpark@2026NK",
    account="ihsnorr-np09224",
    warehouse="COMPUTE_WH",
    database="MY_DB",
    schema="RAW"
)

sf_cursor = sf_conn.cursor()  # ✅ FIX 2

# ✅ FIX 3 + FIX 4
insert_query = """
INSERT INTO CV_SALES_DATA (DAY, TNR, ROW_COUNT)
VALUES (%s, %s, %s)
"""

for row in df.itertuples(index=False):
    sf_cursor.execute(insert_query, tuple(row))

sf_conn.commit()

print("✅ Data loaded into Snowflake successfully")

# Close connections
hana_cursor.close()
hana_conn.close()
sf_cursor.close()
sf_conn.close()