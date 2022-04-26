#!/bin/bash

# echo 'Msg'

trap "echo 'Выхода нет'" SIGINT
trap "echo 'Goodbye....:_(((('" EXIT

count=1
while [[ $count -le 5 ]]
do
    echo "msg #$count"
    count=$(( $count + 1 ))
    sleep 1000000000000
done

# trap "echo 'СКОРО РАССВЕEEEТ!!!!!!!!'" SIGINT
trap -- SIGINT
count=1
while [[ $count -le 10 ]]
do
    echo "msg #$count"
    count=$(( $count + 1 ))
    sleep 1000000000000
done