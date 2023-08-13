#!/usr/bin/env bash

rm ../posts.html
rm ../posts/*

cd posts
python generate.py
cd ../..

# for file in $(find ./ -name "*.html"); do
#   tidy -i $file -o $file
# done
