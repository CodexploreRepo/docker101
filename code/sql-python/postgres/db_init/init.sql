CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL
);

INSERT INTO students (firstname, surname)
VALUES ('John', 'Andersen'), ('Ha Quan', 'Nguyen');  