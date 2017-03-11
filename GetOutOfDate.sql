USE FinDW
GO

;WITH x AS (
SELECT ISNULL(MAX(DateID),0) AS LastUpdateDateID
    ,stk.StockID
FROM Dim.Stock AS stk
LEFT JOIN Fact.StockPrice AS prc
ON stk.StockID = prc.StockID
GROUP BY stk.StockID
)
SELECT *
FROM x