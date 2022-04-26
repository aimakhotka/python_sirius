#!/bin/bash

function add_ten {
    read -p "Enter value: " value
    echo $(( $value + 10 ))
}

result=$( add_ten )
echo "Value is $result"

# count=1
# while [ $count -le 5 ]
#     do
#     myfunc
#     count=$(( $count + 1 ))
#     done