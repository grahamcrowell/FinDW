USE FinDW
GO

;WITH MostRecentStockPrice AS (
    SELECT ISNULL(MAX(DateID),0) AS LastUpdateDateID
        ,stk.Symbol
    FROM Dim.Stock AS stk
    LEFT JOIN Fact.StockPrice AS prc
    ON stk.StockID = prc.StockID
    WHERE stk.StockName != 'Invalid'
    GROUP BY stk.Symbol
)
SELECT *
FROM MostRecentStockPrice