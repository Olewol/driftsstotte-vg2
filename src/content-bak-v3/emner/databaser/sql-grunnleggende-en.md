---
title: "SQL – Basics"
emne: databaser
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://www.w3schools.com/sql/default.asp
  - https://dev.mysql.com/doc/refman/8.0/en/tutorial.html
  - https://www.w3schools.com/sql/
  - https://dev.mysql.com/doc/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
notebooklm: true
video: https://www.youtube.com/watch?v=7S_tz1z_5bA
tags: []
flashcards: https://notebooklm.google.com/notebook/e9134332-9a2e-4991-9a72-2807660c7610
public: true
language: en
original: sql-grunnleggende.md
---

## Introduction

SQL (Structured Query Language) is the standard language for communicating with relational databases. It was standardized by ANSI in 1986 and ISO in 1987, and is used today in MySQL, PostgreSQL, SQLite, Microsoft SQL Server, and many other systems. Although the dialects vary slightly, the core syntax is the same everywhere.

SQL is divided into three main parts:

- **DDL** (Data Definition Language) — create and modify structure: `CREATE`, `ALTER`, `DROP`
- **DML** (Data Manipulation Language) — work with data: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- **DCL** (Data Control Language) — access control: `GRANT`, `REVOKE`

In this article, we focus on DDL and DML — what you need to build and use databases in practice. The four core operations INSERT, SELECT, UPDATE, and DELETE are collectively called **CRUD** (Create, Read, Update, Delete). Access control with DCL is covered in [[databaseadministrasjon-en|database administration]].

---

## Theory

### Tables, Rows, and Columns

A SQL database is built up of tables. Each table has a fixed set of **columns** (fields) that define the structure, and a varying number of **rows** (records) which are the actual data.

```sql
CREATE TABLE equipment (
  id          INT PRIMARY KEY AUTO_INCREMENT,
  name        VARCHAR(100) NOT NULL,
  type        VARCHAR(50),
  serial_no   VARCHAR(50) UNIQUE,
  location    VARCHAR(100)
);
```

Here, `id` is set to `PRIMARY KEY` and `AUTO_INCREMENT`, which means MySQL automatically assigns a unique number for each new row. `NOT NULL` means the field is required. `UNIQUE` means no two rows can have the same value in that field.

### Primary Key and Foreign Key

A **primary key** (PRIMARY KEY) uniquely identifies one row in the table. It cannot be NULL and cannot have duplicates.

A **foreign key** (FOREIGN KEY) points to the primary key in another table and creates a relationship between the tables. The foreign key ensures **referential integrity** — you cannot insert a foreign key value that does not exist in the source table.

```sql
CREATE TABLE room (
  id   INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE equipment (
  id          INT PRIMARY KEY AUTO_INCREMENT,
  name        VARCHAR(100) NOT NULL,
  type        VARCHAR(50),
  serial_no   VARCHAR(50) UNIQUE,
  room_id     INT,
  FOREIGN KEY (room_id) REFERENCES room(id)
);
```

Important: when inserting data with a foreign key, the **parent table** (`room`) must have data before you can insert into the **child table** (`equipment`).

### SELECT — Retrieve Data

`SELECT` is the most used command in SQL. This is the **R** in CRUD — Read data.

```sql
-- Get all columns from equipment
SELECT * FROM equipment;

-- Get only name and location
SELECT name, location FROM equipment;

-- Filter with WHERE
SELECT * FROM equipment WHERE type = 'PC';

-- Sort the result
SELECT * FROM equipment ORDER BY name ASC;

-- Limit the number of rows
SELECT * FROM equipment LIMIT 10;

-- Combine conditions
SELECT * FROM equipment
WHERE type = 'PC'
  AND location = 'Room 201'
ORDER BY name ASC
LIMIT 5;
```

`WHERE` supports comparison operators (`=`, `<>`, `<`, `>`, `<=`, `>=`), logical operators (`AND`, `OR`, `NOT`), and pattern matching with `LIKE`:

```sql
-- Find all equipment with serial numbers starting with 'SN'
SELECT * FROM equipment WHERE serial_no LIKE 'SN%';

-- Find equipment without a registered location
SELECT * FROM equipment WHERE location IS NULL;
```

**Tip:** Avoid `SELECT *` in production and applications — always specify column names for better performance and predictability. See [[databaseadministrasjon-en|database administration]] for more on performance optimization.

### INSERT — Insert Data

```sql
INSERT INTO equipment (name, type, serial_no, location)
VALUES ('Dell OptiPlex 7090', 'PC', 'SN123456', 'Room 201');

-- Insert multiple rows at once
INSERT INTO equipment (name, type, serial_no, location)
VALUES
  ('HP LaserJet Pro', 'Printer', 'SN789012', 'Room 201'),
  ('Cisco Switch 2960', 'Network Equipment', 'SN345678', 'Server Room');
```

### UPDATE — Update Data

```sql
-- Update the location for a specific piece of equipment
UPDATE equipment
SET location = 'Room 202'
WHERE id = 1;

-- Update multiple fields at once
UPDATE equipment
SET location = 'Room 301', type = 'Desktop PC'
WHERE serial_no = 'SN123456';
```

**Warning:** Always use `WHERE` with `UPDATE`. Without `WHERE`, all rows in the table are updated.

### DELETE — Delete Data

```sql
-- Delete one row
DELETE FROM equipment WHERE id = 3;

-- Delete all PCs from one room
DELETE FROM equipment
WHERE type = 'PC' AND location = 'Room 201';
```

**Warning:** Again — `DELETE` without `WHERE` deletes all rows in the table.

### Table Aliases for Readability

When working with JOIN and long table names, it is good practice to use aliases to make SQL code shorter and clearer:

```sql
-- Without alias (verbose)
SELECT equipment.name, equipment.type, room.name AS room_name
FROM equipment INNER JOIN room ON equipment.room_id = room.id;

-- With alias (cleaner)
SELECT e.name, e.type, r.name AS room_name
FROM equipment AS e
INNER JOIN room AS r ON e.room_id = r.id;
```

### JOIN — Combine Tables

JOIN is used to retrieve data from two or more tables based on a relationship between them.

#### INNER JOIN

Returns only rows that have matches in **both** tables.

```sql
SELECT equipment.name, equipment.type, room.name AS room_name
FROM equipment
INNER JOIN room ON equipment.room_id = room.id;
```

Result: only equipment that is linked to a room.

#### LEFT JOIN

Returns **all rows from the left table**, plus matching rows from the right. Rows without a match get `NULL` in the right column.

```sql
SELECT equipment.name, equipment.type, room.name AS room_name
FROM equipment
LEFT JOIN room ON equipment.room_id = room.id;
```

Result: all equipment is displayed, including equipment not linked to any room (`room_name` will then be `NULL`).

**Rule of thumb:** Use `INNER JOIN` when you only want complete relationships. Use `LEFT JOIN` when you want to keep all rows from one table even if there is no match.

---

## Example / Lab

### Lab: Build an IT Inventory Database

In this lab, you create a simple database for keeping track of IT equipment at a school.

**Step 1: Create the database and select it**

```sql
CREATE DATABASE it_inventory;
USE it_inventory;
```

**Step 2: Create the table for rooms**

```sql
CREATE TABLE room (
  id   INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL
);
```

**Step 3: Create the equipment table with foreign key**

```sql
CREATE TABLE equipment (
  id          INT PRIMARY KEY AUTO_INCREMENT,
  name        VARCHAR(100) NOT NULL,
  type        VARCHAR(50),
  serial_no   VARCHAR(50) UNIQUE,
  location    VARCHAR(100),
  room_id     INT,
  FOREIGN KEY (room_id) REFERENCES room(id)
);
```

**Step 4: Insert test data**

```sql
INSERT INTO room (name) VALUES ('Room 201'), ('Room 202'), ('Server Room');

INSERT INTO equipment (name, type, serial_no, location, room_id)
VALUES
  ('Dell OptiPlex 7090', 'PC', 'SN123456', 'Room 201', 1),
  ('HP LaserJet Pro', 'Printer', 'SN789012', 'Room 201', 1),
  ('Cisco Switch 2960', 'Network Equipment', 'SN345678', 'Server Room', 3),
  ('Lenovo ThinkPad E15', 'Laptop', 'SN901234', 'Room 202', 2),
  ('Dell OptiPlex 3090', 'PC', 'SN567890', 'Room 202', 2);
```

**Step 5: Run queries**

```sql
-- Show all PC equipment
SELECT * FROM equipment WHERE type = 'PC';

-- Show equipment with room name (INNER JOIN)
SELECT equipment.name, equipment.type, equipment.serial_no, room.name AS room_name
FROM equipment
INNER JOIN room ON equipment.room_id = room.id
ORDER BY room.name, equipment.name;

-- Count number of units per type
SELECT type, COUNT(*) AS count
FROM equipment
GROUP BY type
ORDER BY count DESC;

-- Show all equipment, including equipment without a room (LEFT JOIN)
SELECT equipment.name, equipment.type, room.name AS room_name
FROM equipment
LEFT JOIN room ON equipment.room_id = room.id;
```

**Step 6: Update and clean up**

```sql
-- Move a laptop to the server room
UPDATE equipment SET room_id = 3, location = 'Server Room'
WHERE serial_no = 'SN901234';

-- Delete old equipment
DELETE FROM equipment WHERE serial_no = 'SN567890';
```

---

## Study Guide

### SQL Basics — Core Content

SQL is the standard language for relational databases and is divided into three categories: DDL (structure), DML (data), and DCL (access). VG2 IT focuses primarily on DDL and DML.

**Table structure and keys**
Tables consist of columns (structure) and rows (data). The primary key uniquely identifies each row and cannot be NULL. The foreign key links tables together and ensures referential integrity — you cannot point to a row that does not exist. `AUTO_INCREMENT` makes MySQL assign the primary key value automatically.

**CRUD — the four core operations**

- `INSERT` — add new rows (Create)
- `SELECT` — retrieve and filter data (Read)
- `UPDATE` — modify existing rows (Update)
- `DELETE` — remove rows (Delete)

Critical rule for `UPDATE` and `DELETE`: always use `WHERE`. Without `WHERE`, all rows in the table are affected — a common and dangerous mistake.

**SELECT and filtering**
`WHERE` filters rows with comparison operators, `AND`/`OR`/`NOT`, and `LIKE` for pattern matching. `ORDER BY` sorts, `LIMIT` limits the number of rows. Avoid `SELECT *` — specify columns explicitly.

**JOIN — combining tables**
`INNER JOIN` gives only rows with matches in both tables. `LEFT JOIN` gives all rows from the left table, with `NULL` where the right table lacks matches. Use aliases (`AS e`, `AS r`) for more readable code when JOINing many tables.

**Connections to other topics**
The SQL knowledge from this article is actively used in [[databaseadministrasjon-en|database administration]] where you optimize queries with indexes and `EXPLAIN`. The DCL part of SQL (GRANT, REVOKE) is covered there.

---

## FAQ

**What does CRUD mean?**
Create, Read, Update, Delete — the four basic operations for data manipulation. In SQL, this corresponds to INSERT, SELECT, UPDATE, and DELETE.

**What is the difference between a primary key and a foreign key?**
A primary key uniquely identifies one row in its own table and cannot be NULL. A foreign key is a column in one table that points to the primary key in another table, and is used to link tables together.

**What happens if you run UPDATE or DELETE without WHERE?**
All rows in the table are affected. With `UPDATE`, all rows are changed to the new value. With `DELETE`, all rows are deleted. Always use `WHERE` to limit which rows are changed — this is one of the most common and dangerous mistakes in SQL.

**What is the difference between INNER JOIN and LEFT JOIN?**
`INNER JOIN` returns only rows that have matches in both tables. `LEFT JOIN` returns all rows from the left table and fills in `NULL` for columns from the right table where there is no match.

**What does AUTO_INCREMENT mean in a column definition?**
MySQL automatically assigns the next available integer as the value when a new row is inserted, without you needing to specify the value manually. Typically used on primary key columns of type INT.

**Why must you insert data into the parent table before the child table when using foreign keys?**
The foreign key ensures referential integrity — the value in the foreign key column must exist as a primary key in the parent table. If the parent row does not exist, MySQL will reject the insertion with an error message.

**What are table aliases, and why should I use them?**
Aliases (`FROM equipment AS e`) give tables shorter names in a query. They make SQL code more readable and less error-prone, especially when JOINing multiple tables where you would otherwise have to write the full table name many times.

**What is a query?**
A request written in SQL to retrieve, filter, or modify specific data in the database system. `SELECT * FROM equipment WHERE type = 'PC'` is an example of a query that retrieves all PCs from the equipment table.

---

## Quiz

<details><summary>Question 1: What is the difference between a primary key and a foreign key?</summary>

**Answer:** A primary key uniquely identifies one row in its own table and cannot be NULL. A foreign key is a column in one table that points to the primary key in another table, and is used to link tables together.

</details>

<details><summary>Question 2: What happens if you run UPDATE without WHERE?</summary>

**Answer:** All rows in the table are updated with the new value. This is a common and dangerous mistake — always use WHERE to limit which rows are modified.

</details>

<details><summary>Question 3: What is the difference between INNER JOIN and LEFT JOIN?</summary>

**Answer:** INNER JOIN returns only rows that have matches in both tables. LEFT JOIN returns all rows from the left table, and fills in NULL for columns from the right table where there is no match.

</details>

<details><summary>Question 4: What does AUTO_INCREMENT mean in a column definition?</summary>

**Answer:** MySQL automatically assigns the next available integer as the value when a new row is inserted, without you needing to specify the value manually. Typically used on primary key columns of type INT.

</details>

<details><summary>Question 5: Why must you insert data into the parent table before the child table when using foreign keys?</summary>

**Answer:** The foreign key ensures referential integrity — the value in the foreign key column must exist as a primary key in the parent table. If the parent row does not exist, MySQL will reject the insertion with an error message.

</details>

---

## Resources

- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/default.asp)
- [W3Schools: SQL JOIN](https://www.w3schools.com/sql/sql_join.asp)
- [MySQL 8.0 Official Tutorial](https://dev.mysql.com/doc/refman/8.0/en/tutorial.html)
- [NDLA: Inserting Data into a Database](https://ndla.no/r/konseptutvikling-og-programmering-im-ikm-vg1/legge-inn-data-i-en-database/22e4bdf1fd)
