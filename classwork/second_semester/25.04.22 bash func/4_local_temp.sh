#!/bin/bash

function my_func {
    # value=$(( $value + 10 ))
    local temp=$(( $value + 10 ))
    echo "Local temp: $temp"
}

read -p "Enter value: " value
temp=50
my_func
echo "But the value is $value"
echo "Global temp: $temp"