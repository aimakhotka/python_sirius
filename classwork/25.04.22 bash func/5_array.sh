#!/bin/bash

function my_func {
    echo "The parameters are: $@"
    arr=("$@")
    echo "The received array: ${arr[*]}"
}

array=( 1 2 3 4 5 )
echo "Our array: ${array[*]}"
my_func ${array[*]}