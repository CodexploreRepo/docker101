# Postgres

- Pull Docker image: `docker pull postgres:16.1-alpine`
  - `16.1`: version
  - `alpine`: is a Small. Simple. Secure. Linux
- Run `docker run --name <name_of_container> -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:16.1-alpine`
- Access Postgres container via exec SHELL Commands

```Shell
docker exec -it postgres16 /bin/sh
# inside the postgres container, we can use createdb cmd to create a new database called simplebank
/  createdb --username=root --owner=root simple_bank
# login to simplebank db via "psql" command inside the container
/  psql simple_bank
psql (16.1)
Type "help" for help.

simple_bank=# \q

/  dropdb simple_bank
/  exit

```

- Access Postgres CLI `psql` via exec: `docker exec -it <name_of_container> psql -U root`

  - Note: if access the running container via localhost, so the password is not required
  - `psql` running postgres sql commands
  - `-U root` running as root user

  ```shell
  # create simple_bank db vs exec psql
  docker exec -it postgres16 createdb --username=root --owner=root simple_bank
  # Option 1:
  # Access the simple_bank db
  docker exec -it postgres16 psql -U root simple_bank
  psql (16.1)
  Type "help" for help.

  simple_bank=#

  # Option 2: login to psql CLI
  docker exec -it postgres16 psql -U root
  -------------------------------
  psql (16.1)
  Type "help" for help.

  root: select now();
              now
  -------------------------------
  2023-12-23 14:58:15.391689+00
  (1 row)
  ```

  - Type `\q` to exit the **psql**

- Access postgres container via [TablePlus](https://tableplus.com/) with connection details
  - Press "+" icon and choose Postgres
  - Name: `postgres16`
  - Host: `localhost`; Port: `5432`
  - User: `root`, Password: `secret`
  - DB: `root` if we did not specify when starting the container, the default db is `root` user
