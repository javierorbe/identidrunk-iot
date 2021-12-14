-- Import uuid generator
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create user table with uuid insertable
CREATE TABLE person (
    id uuid PRIMARY KEY,
    username VARCHAR (50) UNIQUE NOT NULL
);

-- Create test table with id auto-generated
CREATE TABLE test (
    id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
    person_id uuid NOT NULL,
    alcohol_level DECIMAL NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_person FOREIGN KEY(person_id) REFERENCES person(id)
);

-- Init some people
INSERT INTO person (id, username)
VALUES 
('ccb08b86-dbd9-4c8a-93ea-a7fa79d22a52', 'Ramon'),
('8151c335-ea33-46ab-82bc-c7901b4c86fb', 'Jaime');