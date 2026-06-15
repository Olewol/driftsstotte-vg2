---
title: "Database Administration"
emne: databaser
kompetansemaal:

  - km-04

kilder:

  - ndla
  - <https://ndla.no/subject:1:7e101f30-891d-4076-a70e-1100f9156475/topic:1:a6e7039a-5e1a-4c92-b05b-439f72765366/resource:73797690-3486-444c-bc6d-62725e173e97>
  - <https://dev.mysql.com/doc/refman/8.0/en/optimization.html>
  - <https://www.w3schools.com/sql/>
  - <https://dev.mysql.com/doc/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>

video: <https://www.youtube.com/watch?v=u96rS6Y236M>
notebooklm: true
tags: []
flashcards: <https://notebooklm.google.com/notebook/e9134332-9a2e-4991-9a72-2807660c7610>
public: true
language: en
original: databaseadministrasjon.md
---

## Introduction

DDatabase administration is about keeping a database server secure, available, and efficient over time.
DDFor an operations technician, this is daily work: you create users, grant permissions, take backups, restore data after
Dfailures, and ensure the server is not too slow.

TThis article covers three core areas of MySQL administration:**user access**,**backup and recovery**, and**performance
TToptimization with indexes**. Good database administration is closely linked to [[bruker-og-tilgangsstyring-en|user and
TTaccess management]] in general and is a prerequisite for solid [[backup-og-gjenoppretting-en|backup and recovery]] of
Tthe systems you operate.

---

## Theory

### User Access in MySQL

MySQL handles access control in two steps:

1.**Authentication**— can the user connect to the server? (correct username and password)
2.**Authorization**— what is the user allowed to do? (which databases, tables, and operations)

#### User Identification

IIn MySQL, a user is always identified by the combination `'username'@'host'`. This means
II`app_user@'localhost'`and`app_user@'192.168.1.10'` are two different users, even if they have the same name.
IThis is important for security: you can restrict which machines are allowed to connect.

```sql
-- Create a user that can only connect from localhost
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'StrongPassword123!';

-- Create a user that can connect from an entire subnet
CREATE USER 'report_user'@'192.168.1.%' IDENTIFIED BY 'AnotherPassword456!';
```

#### Granting Permissions with GRANT

```sql
-- Grant all privileges on one database
GRANT ALL PRIVILEGES ON it_inventory.*TO 'app_user'@'localhost';

-- Grant read-only access (SELECT)
GRANT SELECT ON it_inventory.*TO 'report_user'@'192.168.1.%';

-- Grant SELECT and INSERT on one specific table
GRANT SELECT, INSERT ON it_inventory.equipment TO 'stock_user'@'localhost';

-- Activate changes immediately
FLUSH PRIVILEGES;
```

Common privileges:

|| Privilege | What it allows |
|| --- | --- |
|| `SELECT` | Read data |
|| `INSERT` | Insert new rows |
|| `UPDATE` | Modify existing rows |
|| `DELETE` | Delete rows |
|| `CREATE` | Create tables and databases |
|| `DROP` | Delete tables and databases |
|| `ALTER` | Modify table structure |
|| `ALL PRIVILEGES` | All privileges |

#### Revoking Permissions with REVOKE

```sql
-- Remove INSERT privilege
REVOKE INSERT ON it_inventory.equipment FROM 'stock_user'@'localhost';

-- Remove all privileges on a database
REVOKE ALL PRIVILEGES ON it_inventory.*FROM 'report_user'@'192.168.1.%';

FLUSH PRIVILEGES;
```

#### View Current Privileges

```sql
SHOW GRANTS FOR 'app_user'@'localhost';
```

#### Delete a User

```sql
DROP USER 'report_user'@'192.168.1.%';
```

#### Roles (MySQL 8.0+)

FFrom MySQL 8.0, you can use**roles**to group privileges and assign them to many users at once — equivalent to role-based
Faccess control (RBAC).

```sql
-- Create a role
CREATE ROLE 'read_inventory';

-- Assign privileges to the role
GRANT SELECT ON it_inventory.*TO 'read_inventory';

-- Assign the role to a user
GRANT 'read_inventory' TO 'temp_user'@'localhost';

-- Activate the role for the user
SET DEFAULT ROLE 'read_inventory' TO 'temp_user'@'localhost';
```

Roles make it much easier to manage access when many users need the same privileges.

***Principle of Least Privilege:**Always give users only the privileges they absolutely need to perform their task.
**An application user who only reads data does not need `DELETE`or`DROP`. This limits the damage scope in case of errors
*or compromise.

---

### Backup with mysqldump

``mysqldump` is the simplest tool for taking a**logical backup**of MySQL databases.
`It exports the database structure and data as SQL statements that can be re-run to restore the database.

Logical backup is portable: you can restore to another machine, another operating system, or a newer version of MySQL.

#### Taking a Backup

```bash

# Backup of one database

mysqldump -u root -p it_inventory > it_inventory_backup.sql

## Backup with date in the filename

mysqldump -u root -p it_inventory > "it_inventory_$(date +%Y-%m-%d).sql"

## Backup of all databases on the server

mysqldump -u root -p --all-databases > all_databases_backup.sql

## Backup with compression (saves disk space)

mysqldump -u root -p it_inventory | gzip > it_inventory_backup.sql.gz
```

#### Restoring from Backup

```bash

## Restore to an existing database

mysql -u root -p it_inventory < it_inventory_backup.sql

## Create new database and restore

mysql -u root -p -e "CREATE DATABASE it_inventory_restore;"
mysql -u root -p it_inventory_restore < it_inventory_backup.sql

## Restore from compressed backup

gunzip < it_inventory_backup.sql.gz | mysql -u root -p it_inventory
```

#### Scheduling Automatic Backup with cron (Linux)

```bash

## Open crontab

crontab -e

## Run backup every day at 02:00

0 2***mysqldump -u root -pYourPassword it_inventory > /backup/it_inventory_$(date +\%Y-\%m-\%d).sql
```

BBackup files should be stored on a separate disk or external location — a backup on the same disk as the database is not
Ba real backup.

***Always test recovery (Recovery Testing).**A backup you have never tested is not a backup you can rely on.
**Set aside time regularly to restore to a test database and verify that the data is intact.
*See [[backup-og-gjenoppretting-en|backup and recovery]] for general principles that apply across systems.

---

### Indexes and Performance Optimization

#### What is an Index?

AAn index is a data structure (typically a B-tree) that makes lookups in a column faster, at the cost of slightly more
AAdisk space and slightly slower inserts/updates. Primary keys and columns with `UNIQUE`automatically get an index.
AOther columns that are used frequently in`WHERE` clauses should be added manually.

```sql
-- Create an index on the type column
CREATE INDEX idx_type ON equipment(type);

-- Create an index on two columns (composite index)
CREATE INDEX idx_type_location ON equipment(type, location);

-- Show all indexes on a table
SHOW INDEX FROM equipment;

-- Delete an index
DROP INDEX idx_type ON equipment;
```

#### EXPLAIN — Analyze Queries

``EXPLAIN`shows you how MySQL plans to execute a query. It is the most important tool for finding bottlenecks.
`Always use`EXPLAIN` before adding new indexes — it helps you understand whether an index is actually needed.

```sql
EXPLAIN SELECT*FROM equipment WHERE type = 'PC';
```

Important columns in EXPLAIN output:

|| Column | What it means |
|| --- | --- |
|| `type` | The type of lookup:`ALL`= full table scan (bad),`ref`/`eq_ref` = index lookup (good) |
|| `key` | Which index is used (NULL means no index) |
|| `rows` | Estimated number of rows MySQL must read |
|| `Extra` | Additional information, e.g.,`Using filesort`(needs sorting) or`Using index` (good) |

Example of a bad query (full scan):

```sql
type: ALL, key: NULL, rows: 10000
```

After adding an index:

```sql
type: ref, key: idx_type, rows: 42
```

#### Slow Query Log

MMySQL can log all queries that take longer than a defined threshold. This is a valuable tool for identifying performance
Mbottlenecks in production environments.

```sql
-- Check if slow query log is enabled
SHOW VARIABLES LIKE 'slow_query_log%';

-- Enable in MySQL configuration (/etc/mysql/my.cnf):
-- slow_query_log = 1
-- slow_query_log_file = /var/log/mysql/slow.log
-- long_query_time = 2
```

#### Practical Performance Tips

**Use correct data types.**An `INT`is faster to search than a`VARCHAR`. Use `DATE`for dates, not`VARCHAR`.

```sql
-- Bad: store dates as text
ALTER TABLE equipment ADD COLUMN purchase_date VARCHAR(20);

-- Good: use DATE
ALTER TABLE equipment ADD COLUMN purchase_date DATE;
```

**Avoid SELECT \*in production.**Only fetch the columns you actually need.

```sql
-- Slower: fetches all columns
SELECT*FROM equipment WHERE type = 'PC';

-- Faster: fetches only what is needed
SELECT id, name, serial_number FROM equipment WHERE type = 'PC';
```

*## Limit result sets with LIMIT.

```sql
SELECT*FROM log ORDER BY timestamp DESC LIMIT 100;
```

**Index columns used in WHERE, JOIN, and ORDER BY.**These are the most common bottlenecks.

---

## Example / Lab

### Lab: Manage User Access and Take Backup

*## Step 1: Create users with different permissions

```sql
-- Operations staff: full access
CREATE USER 'ops_admin'@'localhost' IDENTIFIED BY 'Admin2024!';
GRANT ALL PRIVILEGES ON it_inventory.*TO 'ops_admin'@'localhost';

-- Teachers: read only
CREATE USER 'teacher'@'localhost' IDENTIFIED BY 'Teacher2024!';
GRANT SELECT ON it_inventory.*TO 'teacher'@'localhost';

-- Application user: read and update, not delete
CREATE USER 'app'@'localhost' IDENTIFIED BY 'App2024!';
GRANT SELECT, INSERT, UPDATE ON it_inventory.*TO 'app'@'localhost';

FLUSH PRIVILEGES;
```

*## Step 2: Verify the permissions

```sql
SHOW GRANTS FOR 'teacher'@'localhost';
SHOW GRANTS FOR 'app'@'localhost';
```

*## Step 3: Take backup from the terminal

```bash
mysqldump -u root -p it_inventory > it_inventory_backup.sql
```

*## Step 4: Check that the backup file contains SQL

```bash
head -30 it_inventory_backup.sql
```

You should see CREATE TABLE and INSERT statements.

*## Step 5: Test recovery

```bash
mysql -u root -p -e "CREATE DATABASE it_inventory_test;"
mysql -u root -p it_inventory_test < it_inventory_backup.sql
mysql -u root -p -e "USE it_inventory_test; SELECT*FROM equipment;"
```

*## Step 6: Add an index and use EXPLAIN

```sql
-- Run EXPLAIN without index
EXPLAIN SELECT*FROM equipment WHERE type = 'PC';

-- Add index
CREATE INDEX idx_type ON equipment(type);

-- Run EXPLAIN again and compare
EXPLAIN SELECT*FROM equipment WHERE type = 'PC';
```

---

## Study Guide

### Database Administration — Core Content

DDatabase administration in MySQL covers three main areas of responsibility that an operations technician encounters in
Ddaily work.

*## User access and security
MMySQL identifies users with the combination `'username'@'host'`, which gives granular control over who connects from
MMwhich machine. Access control happens in two steps: authentication (is it the right user?) and authorization (what are
MMthey allowed to do?). The principle of least privilege is crucial: never grant more than what is needed.
MFrom MySQL 8.0, roles (RBAC) can be used to simplify administration where many users need the same privileges.

Key commands: `CREATE USER`, `GRANT`, `REVOKE`, `FLUSH PRIVILEGES`, `SHOW GRANTS`, `DROP USER`, `CREATE ROLE`.

*## Backup and recovery
``mysqldump` creates a logical backup as SQL statements — portable, readable, and version-independent.
``Backups should be automated with cron and stored outside the database server. Equally important as taking backups is
`regularly*testing recovery*. An untested backup is not a reliable backup.

*## Performance optimization
IIndexes (B-tree structures) make lookups dramatically faster in large tables, but cost a little on inserts and updates.
II`EXPLAIN` is the primary tool for analyzing query plans and finding missing indexes.
IIFull table scan (`type: ALL`) is a sign that an index is missing. The Slow Query Log helps you discover bottlenecks in
Iproduction. Good habits: correct data types, avoid `SELECT*`, use `LIMIT`.

*## Connections to other topics
DDatabase administration builds on principles from [[bruker-og-tilgangsstyring-en|user and access management]] and is
DDpart of the overall [[backup-og-gjenoppretting-en|backup and recovery]] responsibility in an operations organization.
D[[sql-grunnleggende-en|SQL basics]] provides the foundation for understanding the queries you optimize.

---

## FAQ

*## What are the two stages of MySQL's access control?
AAuthentication (is the username and password correct?) and authorization (what is this user allowed to do?).
ABoth must be approved for an operation to go through.

*## Why is the format `'user'@'host'` important in MySQL?
BBecause the same username from different machines can have completely different permissions.
BB`admin@localhost`and`admin@'192.168.1.5'` are separate accounts. This gives precise control over network access to the
Bdatabase.

*## What is the principle of least privilege, and why does it apply to databases?
GGive users only the privileges they need for their task — no more. A report user needs `SELECT`, not `DELETE`.
GIf an account is compromised or a mistake is made, the damage is limited.

*## What is the difference between logical and physical backup?
LLogical backup (mysqldump) exports data as SQL statements — portable and readable but slower to restore for large
LLdatabases. Physical backup copies the actual data files on disk — faster recovery, but not necessarily compatible
Lacross MySQL versions.

*## Why should I test recovery, not just take backups?
AA backup file can be corrupt, incomplete, or written incorrectly. If you never test recovery, you do not know if it
Aactually works — you will find out at the worst possible moment during a real incident.

*## What does `EXPLAIN` tell me, and when do I use it?
EEXPLAIN shows MySQL's plan for executing a query: which index is used, estimated number of rows read, and whether there
Eis a full table scan. Use it when a query is slow, or before adding an index, to understand what is actually happening.

*## What is a Slow Query Log?
AA MySQL feature that logs all queries that take longer than a defined threshold (e.g., 2 seconds).
AIndispensable in production for finding performance bottlenecks without having to monitor manually.

*## What is RBAC, and how does MySQL support it?
RRole-based access control (RBAC) means privileges are assigned to roles, and roles are assigned to users — not
RRprivileges directly to each user. From MySQL 8.0, use `CREATE ROLE`and`GRANT role TO user`.
RMakes it much easier to manage many users with similar access needs.

---

## Quiz

<details><summary>Question 1: What are the two stages of MySQL's access control?</summary>

***Answer:**Authentication (verifies who the user is — username and password) and authorization (determines what the user
*is allowed to do — which databases, tables, and operations).

</details>

<details><summary>Question 2: Why does MySQL use the format 'username'@'host' to identify users?</summary>

***Answer:**Because the same username from different machines can have different permissions.
**`admin@'localhost'`and`admin@'192.168.1.5'` are two separate users with potentially completely different access rights.
*This provides granular control over who can connect from where.

</details>

<details><summary>Question 3: What is the difference between logical and physical backup?</summary>

***Answer:**Logical backup (like mysqldump) exports data as SQL statements — portable, readable, and version-independent.
**Physical backup copies the actual data files on disk — faster to restore for large databases, but not necessarily
*compatible across versions.

</details>

<details><summary>Question 4: What does EXPLAIN tell you, and when do you use it?</summary>

***Answer:**EXPLAIN shows MySQL's plan for executing a query — which index is used, how many rows are estimated to be
**read, and whether there is a full table scan. You use it when a query is slow, to find out if an index is missing or if
*the query can be written more efficiently.

</details>

<<details><summary>Question 5: What happens to existing data if you restore a mysqldump backup to a database that already
<has tables?</summary>

***Answer:**mysqldump typically includes DROP TABLE IF EXISTS before CREATE TABLE, so existing tables are deleted and
**replaced. You lose data that was in the database before. Always use an empty database or a dedicated restoration
*database if you want to keep existing data.

</details>

---

## Resources

- [MySQL 8.0: Access Control](<https://dev.mysql.com/doc/refman/8.0/en/access-control.html>)
- [MySQL 8.0: Backup and Recovery](<https://dev.mysql.com/doc/refman/8.0/en/backup-and-recovery.html>)
- [MySQL 8.0: Optimization](<https://dev.mysql.com/doc/refman/8.0/en/optimization.html>)
- [PostgreSQL: Backup and Restore](<https://www.postgresql.org/docs/current/backup.html>)
- [NDLA: Database Administration](<https://ndla.no/subject:1:7e101f30-891d-4076-a70e-1100f9156475/topic:1:a6e7039a-5e1a-4c92-b05b-439f72765366/resource:73797690-3486-444c-bc6d-62725e173e97>)
- [YouTube: MySQL Administration and User Management — Database Star (12 min)](<https://www.youtube.com/watch?v=u96rS6Y236M>)
