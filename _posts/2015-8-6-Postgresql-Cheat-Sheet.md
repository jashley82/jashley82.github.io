---
layout: post
title: Postgresql Cheat Sheet
---

Create a User from the Command Line

```bash
sudo -u postgres createuser -s userName
```

Create a Role

```sql
create role userName with createdb login password 'password1';
```

Grant all Permissions to a User

```sql
GRANT ALL PRIVILEGES ON table TO userName;
```

Backup a Database from the Command Line

```bash
pg_dump dbName > dbName.sql
```

Backup all Databases from the Command Line

```bash
pg_dumpall > pgbackup.sql
```

Restore a Database from the Command Line

```bash
psql dbName < pgbackup.sql
```

Copy a Database from Host A to Host B from the Command Line

```bash
pg_dump -h hostA dbName | psql -h hostB dbName
```

Create a Compressed Dump from the Command Line

```bash
pg_dump dbName | gzip > pgbackup.sql.gz
```

Create a Compressed Dump from the Command Line

```bash
cat pgbackup.sql.gz | gunzip | psql dbName
```

Create Database

```sql
CREATE DATABASE dbName;
```

Create Table

```sql
CREATE TABLE tableName (
  id serial PRIMARY KEY,
  name varchar(50) UNIQUE NOT NULL,
  dateCreated timestamp DEFAULT current_timestamp
);
```

Create an Index

```sql
CREATE UNIQUE INDEX indexName ON tableName (columnNames);
```

Reindex

```sql
REINDEX DATABASE dbName;
```

Get all columns and rows from a table

```sql
SELECT * FROM table;
```

Add a new row

```sql
INSERT INTO table (column1,column2)
VALUES (1, 'one');
```

Update a row

```sql
UPDATE table SET foo = 'bar' WHERE id = 1;
```

Delete a row

```sql
DELETE FROM table WHERE id = 1;
```
