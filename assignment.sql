use project;
SELECT * FROM employees WHERE is_active = 1;
INSERT INTO employees (username, first_name, last_name, email, gender, doj, department, is_active, language, address) 
VALUES ('asjskl', 'naman', 'Employee', 'new_employee@example.com', 'Male', '2024-10-29', 'Support', True, 'English', '123 New Address');
UPDATE employees 
SET department = 'Sales', 
    email = 'updated_email@example.com' 
WHERE id = 1;  
UPDATE employees 
SET is_active = False 
WHERE id = 34; 
select * from employees where id= 34; 







