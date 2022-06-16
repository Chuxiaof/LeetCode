# Write your MySQL query statement below
# Approach 1
SELECT Person.FirstName, Person.LastName, Address.City, Address.State 
FROM Person NATURAL LEFT JOIN Address;

# Approach 2
SELECT A.Name as Customers from Customers A
LEFT JOIN Orders B on  a.Id = B.CustomerId
WHERE CustomerId is NULL