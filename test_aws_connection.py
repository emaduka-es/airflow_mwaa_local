import psycopg2

dbname = 'es_dl'
# user =  username
# password = password
host = 'marina-dev.cokvj8a8m59a.us-west-2.redshift.amazonaws.com:5439/'
port = '5439'

try:
    # connect to redshift cluster
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cur = conn.cursor()

    query = " SELECT * FROM marina.applicant a LIMIT 10;"

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

except psycopg2.Error as e:
    print("Error: Could not connect to Redshift")
    print(e)

