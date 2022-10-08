#!bin/bash -e

set -x

ALGORITHMS="algorithms"
DATA_STRUCTURES="data_structures"

pytest --cov=${ALGORITHMS} --cov=${DATA_STRUCTURES} --cov-fail-under=100 --cov-report=term-missing --cov-report=xml
