#!/bin/bash

echo -n "Введите первое число: "; read one
echo -n "Введите второе число: "; read two
echo -n "Введите символ: "; read symbol

case $symbol in 
    "+") echo "Результат: " $(($one + $two)) ;;
    "-") echo "Результат: " $(($one - $two)) ;;
    *) echo "Input Error" ;;
esac
