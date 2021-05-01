--
-- file migrations/001_create_tables.py
--


CREATE TABLE countries(
            country_id SERIAL PRIMARY KEY,
            country VARCHAR(50) UNIQUE
        );

CREATE TABLE states(
    state_id SERIAL PRIMARY KEY,
    state VARCHAR (50) UNIQUE,
    country_id INTEGER, 
    CONSTRAINT fk_country
        FOREIGN KEY(country_id) 
            REFERENCES countries(country_id)
        );

CREATE TABLE IF NOT EXISTS users(
    id VARCHAR(70) PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    date_of_birth DATE NOT NULL,
    state_id INTEGER NOT NULL, 
    CONSTRAINT fk_state
        FOREIGN KEY(state_id) 
            REFERENCES states(state_id),
    version INTEGER
);