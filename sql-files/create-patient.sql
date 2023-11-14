CREATE TABLE Patient (
    id VARCHAR(50) PRIMARY KEY,
    active BOOLEAN,

    identifier_system VARCHAR(100),
    identifier_value VARCHAR(50),

    gender VARCHAR(10),
    birthDate DATE,
    name_family VARCHAR(50),
    name_given VARCHAR(50),

    address_use VARCHAR(20),
    address_line VARCHAR(100),
    address_city VARCHAR(50),
    address_state VARCHAR(2),
    address_postalCode VARCHAR(10),

    phone_number VARCHAR(20),
    email VARCHAR(50),

);