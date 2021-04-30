--
-- file migrations/002_init_tables.py
--

INSERT INTO countries(country) VALUES ('Nigeria'), ('Ghana');


INSERT INTO states(state, country_id) VALUES
    ('Abia', 1),
    ('Abuja', 1), 
    ('Adamawa', 1), 
    ('Akwa Ibom', 1),
    ('Anambra', 1),
    ('Bauchi', 1), 
    ('Bayelsa', 1), 
    ('Benue', 1), 
    ('Borno', 1), 
    ('Cross River', 1), 
    ('Delta', 1), 
    ('Ebonyi', 1), 
    ('Edo', 1),   
    ('Ekiti', 1), 
    ('Enugu', 1), 
    ('Gombe', 1), 
    ('Imo', 1),
    ('Jigawa', 1),
    ('Kaduna', 1),
    ('Kano', 1),
    ('Katsina', 1),
    ('Kebbi', 1),
    ('Kogi', 1),
    ('Kwara', 1),
    ('Lagos', 1),
    ('Nasarawa', 1),
    ('Niger', 1),
    ('Ogun', 1),
    ('Ondo', 1),
    ('Osun', 1),
    ('Oyo', 1),
    ('Plateau', 1),
    ('Rivers', 1),
    ('Sokoto', 1),
    ('Taraba', 1),
    ('Yobe', 1),
    ('Zamfara', 1);