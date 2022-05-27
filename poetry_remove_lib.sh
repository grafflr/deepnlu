#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage ${0} <service-name> "
    exit 1
fi

echo "Microservice Name: ${1}"

VENV_PATH=`poetry env info | grep "Path"` 

echo ${VENV_PATH}

echo "Replacing Path"
## Replace Path:
VENV=${VENV_PATH//Path:/}

echo "Trimming"
## Trim
VENV=${VENV##*( )}

echo ${VENV}

if [ "${VENV}" = "NA" ]; then
    echo "${1} Virtual Environment not installed."
    exit 1
fi

##echo "rm -rf ${VENV}/lib/python*/site-packages/${1}*"
pushd ${VENV}/lib/python*/site-packages
rm -rf ${1}*
popd

echo "Microservice Name: ${1} in ${VENV} is removed."
