#!/bin/bash
#works for mac
RED="\x1B[0;31m"
GREEN="\x1B[0;32m"
NC="\x1B[0m"

for i in {1..100}; do
    filepath="./testcases/testcase-$i.txt"
    if ! test -e $filepath; then
        continue
    fi

    expected=`head -n 1 $filepath`
    output=`./main.py --input $filepath`
    errorcode=$?

    if [[ "$errorcode" == "0" ]]; then
        num1=`echo "${output:37}" | xargs`
    else
        num1=`echo "${output:0:5}" | xargs`
    fi
    num2=`echo "${expected:1}" | xargs`

    if [[ "$num1" == "$num2" ]]; then
        result="PASS"
        color=$GREEN
    else
        result="FAIL"
        color=$RED
    fi
    echo -e "${output}     \t[${color}${result}${NC}] TC:$i"
done