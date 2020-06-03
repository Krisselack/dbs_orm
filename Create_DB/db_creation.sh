sudo -u postgres createuser #already exists
sudo -u postgres psql
alter user postgres with encrypted password 'postgres';

sudo -u postgres dropdb postgres

cd ~/wd/fhwn/db_systeme/dbs_orm/Create_DB$
psql -U postgres -h 127.0.0.1
sudo -u postgres createdb postgres
psql -U postgres -h 127.0.0.1 postgres < orm_db.sql

# Das musste im sql-file so auskommentiert werden, da andere postgres-version
# -- SET default_table_access_method = heap;
