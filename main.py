import psycopg2
import pandas as pd

#мой данные
conn = psycopg2.connect(
    dbname="chinook",      
    user="postgres",       
    password="kazuma", 
    host="localhost",       
    port="5433"             
)

cur = conn.cursor()

#Пример
queries = {
    "top_countries": """
        SELECT i."BillingCountry" AS country,
               SUM(il."UnitPrice" * il."Quantity") AS revenue
        FROM "Invoice" i
        JOIN "InvoiceLine" il ON il."InvoiceId" = i."InvoiceId"
        GROUP BY country
        ORDER BY revenue DESC
        LIMIT 10;
    """,
    "top_customers": """
        SELECT c."CustomerId",
               c."FirstName" || ' ' || c."LastName" AS customer,
               SUM(il."UnitPrice" * il."Quantity") AS revenue
        FROM "Customer" c
        JOIN "Invoice" i ON i."CustomerId" = c."CustomerId"
        JOIN "InvoiceLine" il ON il."InvoiceId" = i."InvoiceId"
        GROUP BY c."CustomerId", customer
        ORDER BY revenue DESC
        LIMIT 10;
    """
}

results = {}
for name, sql in queries.items():
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    results[name] = df
    print(f"\n=== {name.upper()} ===")
    print(df)

    df.to_csv(f"{name}.csv", index=False)
    df.to_excel(f"{name}.xlsx", index=False)

cur.close()
conn.close()
