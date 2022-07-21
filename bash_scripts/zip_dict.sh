#!/bin/bash

#l=
#echo $l
#found=0

for i in {0..100}
do
	found=0
	for pass in $(cat pass.txt)
	do
		unzip -o -P $pass "$(expr 100 - $i).zip"
		if [ $? == 0 ]
		then
			found=1
			break
		fi
	done
	
	echo $found
	if [ $found == 0 ]
	then
		exit 1
	fi	
done
