Param 
(
    [parameter(Mandatory = $false)]
    [ValidateSet('STDBDECSUP01','STDBDECSUP02','STDBDECSUP03','SPDBDECSUP04','PC')]
    [string] $DeploymentSqlServer
)
Set-Location -Path $PSScriptRoot

# # # # these if's are ran when [parameter(Mandatory = $false)]
$DefaultDeploymentServer = "localhost";
if($DeploymentSqlServer -eq "")
{
    $LocalDeploymentUserInput = Read-Host -Prompt ("`nNo deployment server specified.`n`tDefault to local machine ({0})?  Y/n" -f $DefaultDeploymentServer)
    $LocalDeployment = ($LocalDeploymentUserInput -eq "Y")
}
if($LocalDeployment -eq $true)
{
    $DeploymentSqlServer = $env:ComputerName
    $DeploymentSqlServer = $DefaultDeploymentServer
}


Write-Host ("`n`n(re)Deploying DDL SQL scripts at:`n`t{1}`n to Sql Server: `n`t{0}" -f $DeploymentSqlServer, $PSScriptRoot) 


function ExecuteSqlScript ($sqlScriptFullPath) 
{    
    Write-Host "`t`texecute: "$sqlScriptFullPath" to: "$DeploymentSqlServer
    SQLCMD -Slocalhost -E -i $sqlScriptFullPath
}

function ExecuteSqlScriptFolders ([System.Collections.ArrayList]$sqlScriptFolders) 
{
    $rootPath = Get-Location
    Write-Host "root: "$rootPath
    foreach ($folder in $sqlScriptFolders) 
    {
        write-host "`n`tfolder: "$folder
        $absPath = Join-Path -Path $rootPath -ChildPath $folder
        $sqlScriptNames = Get-ChildItem -Path $absPath -File
        $sqlScriptPaths = New-Object System.Collections.ArrayList
        foreach($sqlScriptName in $sqlScriptNames)
        {
            Write-Host ("`t`t{0}" -f $sqlScriptName)
            $sqlScriptPath = Join-Path -Path $absPath -ChildPath $sqlScriptName
            [void]$sqlScriptPaths.Add($sqlScriptPath)
            ExecuteSqlScript($sqlScriptPath)
        }
    }
}



# hard-code ordered deployment scripts
$sqlScriptFolders = New-Object System.Collections.ArrayList

# current folder
[void]$sqlScriptFolders.Add("")
[void]$sqlScriptFolders.Add("Schema")
[void]$sqlScriptFolders.Add("Table")
[void]$sqlScriptFolders.Add("View")
[void]$sqlScriptFolders.Add("PostDeploymentScripts")

ExecuteSqlScriptFolders ($sqlScriptFolders)

