#!/bin/bash

git add .
git commit -m "${1:-update}"
git push https://github.com/mitansh108/DSA.git main
