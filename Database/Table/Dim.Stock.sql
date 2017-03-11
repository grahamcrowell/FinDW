USE FinDW
GO

IF OBJECT_ID('[Dim].[Stock]') IS NOT NULL
BEGIN
	DROP TABLE [Dim].[Stock];
END

CREATE TABLE [Dim].[Stock]
(
	[StockID] INT IDENTITY(0,1), 
    [StockName] VARCHAR(64) NOT NULL, 
    [Symbol] NVARCHAR(50) NOT NULL, 
    [CID] INT NULL, 
    CONSTRAINT [PK_Stock] PRIMARY KEY ([StockID])
)
