USE FinDW
GO

UPDATE Dim.Date 
SET isTradeDate = 1
FROM Dim.Date AS dt
GO

UPDATE Dim.Date 
SET isTradeDate = 0
FROM Dim.Date AS dt
WHERE DATEPART(weekday, date) IN (1,7)
GO
