USE FinDW
GO


IF OBJECT_ID('Dim.Account') IS NOT NULL
BEGIN
	PRINT 'drop Dim.Account'
	DROP TABLE Dim.Account;
END
GO

BEGIN
PRINT 'create Dim.Account'
CREATE TABLE Dim.Account(
	AccountID int IDENTITY(0,1)
	,AccountName varchar(64) NOT NULL
	,CONSTRAINT PK_DimAccount PRIMARY KEY CLUSTERED (AccountID ASC)
	);
END
GO