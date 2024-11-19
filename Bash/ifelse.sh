#!/bin/bash
# [] = test expression
# {1} = postional argument
# {1,,} = ",," allows us to ignore upper and lowercases.

if [ ${1,,} = teddy ]; then
  echo "You work here!"
elif [ ${1,,} = help ]; then
  echo "please enter your username"
else
  echo "wrong username"
fi
