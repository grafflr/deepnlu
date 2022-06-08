<#
    .SYNOPSIS
    Remove Item from Virtual Environment path

    .DESCRIPTION
    Force poetry to remove an internal microservice from a virtual environment path

    .INPUTS
    None. You cannot pipe objects to Add-Extension.

    .OUTPUTS
    None.

    .EXAMPLE
    PS> .\poetry_remove_lib.ps1
#>

param(
  [Parameter(Mandatory = $True)] [System.String] $MssName
)

Write-Host ("Microservice Name: '{0}' " -f $MssName)

$VenvPath = ((poetry env info | Select-String -Pattern Path) -split "Path:").Trim()
$VenvPath = [string]::join("", ($VenvPath.Split("`n")))

if ($VenvPath -eq 'NA') 
{
  Write-Host ("{0} Virtual Environment not installed" -f $MssName)
} 

else 
{
  Write-Host ("Microservice Virtual Environment Path: '{0}' " -f $VenvPath)
  
  Push-Location ${VenvPath}\Lib\site-packages
  Remove-Item -Path $MssName-* -Recurse -Force
  Pop-Location
}
