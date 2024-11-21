#!/bin/bash

showname(){
    echo hello $1
    if [ ${1,,} = teddy ]; then
        return 0
    else
        return 1
    fi 
}
showname $1
if [ $? = 1 ]; then
    echo "Someone unknow called the function" 
fi
