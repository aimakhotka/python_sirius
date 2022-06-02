#!/bin/sh
rm new_test

while read line
do
    echo "$line" | cut -d " " -f 1 >> new_test
    echo "$line" | cut -d " " -f 2 | md5sum | sed 's/  -//g'>> new_test
done < test