# Extract and Load Data From API to PostgreSQL

An example of how to extract data from an API and load the data into postgre database.

----
### Dependencies

- PostgreSQL == 14.1
- Python == 3.10
- Pandas == 1.3.4
- Sqlalchemy == 1.4.27

### Set Environment

First, We'll install our database. You can download from [PostgreSQL](https://www.postgresql.org/download/).

After install postgreSQL you need to create database schema with command below: 


`CREATE SCHEMA IF NOT EXISTS challenge AUTHORIZATION postgres;`

OBS: If you want to use public schema, you'll need to change schema set on constructor in `extract_load.py`

Lastly you'll need to insert your database password defined during postgre installation on `credentials.json` in `files/`
and change the file path defined in `self.__files_path` on constructor in `extract_load.py`

---


