#!/bin/sh

# <
#     .SYNOPSIS
#     Run the deepNLU Regression Test

#     .DESCRIPTION
#     Run the deepNLU regression test on one-or-more file names

#     .INPUTS
#     None. You cannot pipe objects to Add-Extension.

#     .OUTPUTS
#     for certain tests will output files

#     .EXAMPLE
#     PS> .\Run-Regression.ps1 

#     .EXAMPLE
#     PS> .\Run-Regression.ps1 -FileName 145

#     .EXAMPLE
#     PS> .\Run-Regression.ps1 -FileName 145 -LineNumber 0
# >


#param(
#  [Parameter(Mandatory = $False)] [System.String] $FileName
#)




# You must be in the deepnlu directory before running the ./resources/scripts/run_regression.sh command

echo "current directory"
echo $PWD

export REGRESSION_FILENAME=$1
export TEST_CASE_LOCATION="$PWD/resources/regression/cases"
export TEST_ONTO_LOCATION="$PWD/resources/regression/ontologies"

echo $REGRESSION_FILENAME

if test -z $REGRESSION_FILENAME;
then
  export REGRESSION_FILENAME="*"
  echo "Testing all Files" 
fi

echo ""
echo $REGRESSION_FILENAME

poetry run python $PWD/regression/router.py

## ---------------------------------------------------------------------------------------------------------------------------------------------------------
## Purpose:         deepNLU Regression Test
## ---------------------------------------------------------------------------------------------------------------------------------------------------------
## Sample Usage     Run all tests
##                  ./resources/scripts/run_regression.sh
##
##                  Run a Specific Test
##                  ./resources/scriptsrun_regression.sh -FileName 22
## ---------------------------------------------------------------------------------------------------------------------------------------------------------
