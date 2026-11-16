#!/bin/bash

for i in {1..500}
do
	curl -s http://localhost:83
done > logs.txt


echo "Hello 1 :"
grep -c "Hello 1" logs.txt

echo "Hello 2 :"
grep -c "Hello 2" logs.txt

