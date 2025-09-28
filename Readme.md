# Steppe Beats Analytics

> Educational analytics project for the fictional company **Steppe Beats** — an international online retailer of digital music operating across several countries.

---

## Company
**Steppe Beats** is an online store for tracks and albums. Each customer has a dedicated support representative, and all sales are recorded through invoices.

## Project description (in short)
We perform SQL-based analytics on the **Chinook (PostgreSQL)** database: sales by country and customer, popularity of genres and artists, revenue trends, and support staff efficiency. Queries and results are reproducible; later we plan to add a web-based dashboard for visualization.

## Main analytics screenshot
Replace the placeholder with your own screenshot from pgAdmin or your dashboard:  
![Main analytics](img/tableRowsData.png)

---

## How to run the project 

### 1) Prepare the database (PostgreSQL)
Create the database:
```sql
CREATE DATABASE chinook;
