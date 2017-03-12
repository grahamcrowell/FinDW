USE FinDW
GO

IF(OBJECT_ID('dbo.ufnIDToDate','FN') IS NOT NULL)
BEGIN
	PRINT 'drop FUNCTION dbo.ufnIDToDate';
	DROP FUNCTION dbo.ufnIDToDate;
END
GO

CREATE FUNCTION dbo.ufnIDToDate(@DateID INT)
RETURNS DATETIME
-- optimive 2016 in-memory tables with native compilation
AS
BEGIN
    RETURN(CONVERT(DATETIME,CONVERT(CHAR(8), @DateID)));
END