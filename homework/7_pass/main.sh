#!/bin/sh

echo -n 'Введите имя файла: '; read file

if [ -f new_$file ]; then rm new_$file; fi

while read line
do
    echo "$line" | cut -d " " -f 1 >> new_$file
    echo "$line" | cut -d " " -f 2 | md5sum | sed 's/  -//g'>> new_$file
done < $file