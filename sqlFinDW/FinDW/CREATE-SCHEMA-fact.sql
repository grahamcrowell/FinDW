USE FinDW
GO

IF DB_ID('fact') IS NULL
BEGIN
	PRINT 'create schema fact'
	EXEC sp_executesql N'CREATE SCHEMA fact;'
END
GO