
INSERT INTO users (first_name, last_name, email, phone, address_line1, city, state, pincode)
VALUES
('Aman','Kumar','aman@example.com','9999999991','Flat 1','Bengaluru','Karnataka','560001'),
('Bina','Shah','bina@example.com','9999999992','Flat 2','Mumbai','Maharashtra','400001'),
('Chirag','Patel','chirag@example.com','9999999993','Flat 3','Ahmedabad','Gujarat','380001');

INSERT INTO employment_info (user_id, company_name, designation, start_date, end_date, is_current)
VALUES
(1,'HDFC Life','Analyst','2022-01-01',NULL,TRUE),
(2,'ICICI Bank','Associate','2021-05-01',NULL,TRUE),
(3,'HDFC Life','Manager','2019-02-15',NULL,TRUE);

INSERT INTO user_bank_info (user_id, bank_name, account_number, ifsc, account_type)
VALUES
(1,'HDFC','1111111111','HDFC0001','Savings'),
(2,'ICICI','2222222222','ICIC0002','Savings'),
(3,'HDFC','3333333333','HDFC0003','Current');
