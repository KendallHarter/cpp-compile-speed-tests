#!/bin/bash

cd $(dirname $0)

if (( $# < 1 )); then
   echo "Usage: $0 counts..." >&2
   exit
fi

if [ "${CXX}" == "" ]; then
   echo "Environment variable CXX not set" >&2
   exit
fi

for kind in "lambda" "struct"; do
   for i in "$@"; do
      echo
      echo "> ${kind} $i"
      time python3 ./gen.py $i ${kind} | ${CXX} -x c++ -o /dev/null -
   done
done
