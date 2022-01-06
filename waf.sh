#!/bin/bash

if [$1 == " "]
then

echo "=============================="
echo " wafpratico.py dominio.com.br"
echo "=============================="

else

for sub in $(cat other);do host $sub.$1 | grep "has address" | cut -d " " -f 1;done > lista
for i in $(cat lista);do echo "$i" | wafw00f $i | grep "is behind" | cut -d " " -f 7,8,9,10;done

fi
