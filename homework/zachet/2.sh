#!/bin/bash

echo -n 'Введите имя файла: '; read file

while read line
do
sum=$(( $sum + $line ))
done < $file

echo "Результат: " $sum