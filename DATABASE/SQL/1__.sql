

-- UPDATE Syntax

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;


-- UPDATE Single Records

    update customers
    set city="samir",postolcode=401503
    where customerID=1;

    -- UPDATE Multiple Records

    UPDATE customers
    set city="Mumbai",postolcode="40321"
    WHERE customerID BETWEEN 10 to 20;

    Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!

    UPDATE Customers
    SET ContactName='Juan';



-- DELETE Syntax

    DELETE FROM table_name WHERE condition;

    --  Be careful when deleting records in a table! Notice the WHERE clause in the DELETE statement. 
    --  The WHERE clause specifies which record(s) should be deleted. 
    --  If you omit the WHERE clause, all records in the table will be deleted!

    The following SQL statement deletes all rows in the "Customers" table, without deleting the table:

    DELETE FROM Customers;