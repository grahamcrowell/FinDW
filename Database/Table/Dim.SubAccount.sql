﻿USE FinDW
GO

IF OBJECT_ID('[Dim].[SubAccount]') IS NOT NULL
BEGIN
	DROP TABLE [Dim].[SubAccount];
END

CREATE TABLE [Dim].[SubAccount]
(
	[SubAccountID] INT IDENTITY(0,1), 
    [SubAccountName] NVARCHAR(50) NOT NULL, 
    CONSTRAINT [PK_SubAccount] PRIMARY KEY (SubAccountID)
)

GO
