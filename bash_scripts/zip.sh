#!/bin/bash

for i in {0..3000}
do
	unzip "flag$(expr 3000 - $i).zip"
done
