#!/bin/bash

case ${1,,} in
  teddy | admin)
    echo "Hello, to your office"
    ;;
  help)
    echo "enter your username"
    ;;
  *)
    echo "wrong username"
esac
