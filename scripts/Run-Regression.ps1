<#
    .SYNOPSIS
    Run the deepNLU Regression Test

    .DESCRIPTION
    Run the deepNLU regression test on one-or-more file names

    .INPUTS
    None. You cannot pipe objects to Add-Extension.

    .OUTPUTS
    for certain tests will output files

    .EXAMPLE
    PS> .\Run-Regression.ps1 

    .EXAMPLE
    PS> .\Run-Regression.ps1 -FileName 145

    .EXAMPLE
    PS> .\Run-Regression.ps1 -FileName 145 -LineNumber 0
#>

param(
  [Parameter(Mandatory = $False)] [System.String] $FileName
)

if ($FileName -eq $null -OR $FileName -eq '') {
  $FileName = "*"
  Write-Host("Testing all Files")
}


$env:REGRESSION_FILENAME = $FileName

poetry run python .\regression\router.py

## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
## Purpose:         deepNLU Regression Test
## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
## Sample Usage     Run all tests
##                  .\Run-Regression.ps1
##
##                  Run a Specific Test
##                  .\Run-Regression.ps1 -FileName 22
## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
