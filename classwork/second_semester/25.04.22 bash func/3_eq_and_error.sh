#!/bin/bash

function addition {
    if [[ $# -eq 0 ]] || [[ $# -gt 2 ]]
        then
        echo -1
    elif [[ $# -eq 1 ]]
        then
        echo $(( $1 + $1 ))
    else
        echo $(( $1 + $2 ))
    fi
}

# echo "Adding 10 and 15"
# value=$( addition 10 15 )
# echo $value

# echo "Adding nothing"
# value=$( addition )
# echo $value

# echo "Adding 10"
# value=$( addition 10 )
# echo $value

# echo "Adding 10, 15 and 20"
# value=$( addition 10 15 20)
# echo $value