#!/bin/bash

function add_arg {
    echo $(( $1 + $2 ))
}

result=$( add_arg 10 $1 )
echo "Value is $result"