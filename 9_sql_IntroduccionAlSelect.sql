/*SELECT * FROM SalesLT.Product;*/
/*SELECT Name, StandardCost, ListPrice from SalesLT.Product;*/
/*SELECT Name AS ProductName, (ListPrice - StandardCost) AS Markup from SalesLT.Product;*/
/*SELECT ProductNumber, Color, Size, (Color +','+ Size) AS ProductDetails FROM SalesLT.Product;*/

SELECT * FROM SalesLT.Product;

SELECT Name, TRY_CAST(Size as Integer) AS NumericSize FROM SalesLT.Product;

SELECT Name, ISNULL(TRY_CAST(Size AS Integer),0) AS NumericSize FROM SalesLT.Product;

SELECT ProductNumber, (ISNULL(Color, '') + ','+ ISNULL(Size, '')) AS ProductDetails FROM SalesLT.Product;

SELECT Name, NULLIF(Color, 'Multi') AS SingeColor FROM SalesLT.Product;

SELECT Name, COALESCE(SellEndDate, SellStartDate) AS StatusLastUpdate FROM SalesLT.Product;

SELECT Name,
CASE    
    WHEN SellEndDate is NULL THEN 'Currntly for sale'    
    ELSE 'No Longer available'
END AS SalesStatus
FROM SalesLT.Product;

SELECT Name,    
CASE Size        
    WHEN 'S' THEN 'Small'        
    WHEN 'M' THEN 'Medium'        
    WHEN 'L' THEN 'Large'        
    WHEN 'XL' THEN 'Extra-Large'        
    ELSE ISNULL(Size, 'n/a')    
END AS ProductSize
FROM SalesLT.Product;


