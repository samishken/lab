Bash stands for "Bourne Again Shell": 
- Bourne: A reference to Stephen Bourne, the author of the original Bourne shell 
- Again: A pun on "born-again-Christians" 
- It is a shell program and command language supported by the Free Software Foundation and first developed for the GNU Project by Brian Fox. 
- Designed as a 100% free software alternative for the Bourne shell, it was initially released in 1989.

<br>
- #!/bin/bash
- The shebang #!/bin/bash tells the terminal to use bash to execute the script.
- The part after the #! tells Unix what program to use to run it. 
- If it isn't specified, it will try with bash (or sh, or zsh, or whatever your $SHELL variable is) but if it's there it will use that program. 
- Plus, # is a comment in most languages, so the line gets ignored in the subsequent execution.
<br>


#Append

###### echo Hello world! > hello.txt
vs
###### echo Hello World >> hello.txt


##### wc -w hello.txt
vs
##### wc -w < hello.txt
vs
##### wc -w <<< "Hello there wordcount!!!

##### cat << EOF
I will
write some
text here
EOF >>


# build in command for test
[ hello = hello ]
> echo $?  = 0 (no difference)

[ 1 = 0 ]
> echo $?  = 1 (values are not the same)

# if/Elif/Else

# Array
#### MY_FIRST_LIST=(one two three four five)
> echo $MY_FIRST_LIST = one
> echo ${MY_FIRST_LIST[@]} = one two three four five
> echo ${MY_FIRST_LIST[2]} = three

# For Loop
> for item in ${MY_FIRST_LIST[@]}; do echo -n $item | wc -c; done
--- 3 3 5 4 4 (counts the letters in MY_FIRST_LIST)


# Functions (for repeated codes)


# AWK
> echo one two three > textfile.txt
> awk '{print $1}' textfile.txt
> one
> awk '{print $2}' textfile.txt
> two

> awk -F, '{print $1}' csvtest.csv
> echo "Just get this word: Hello" | awk '{print $5}'
> echo "Just get this word: Hello" | awk -F: '{print $2}' | cut -c2-


# SED
- used to change words in files
> sed 's/fly/grasshopper/g' sedtext.txt 
> sed -i.ORIGINAL 's/fly/grasshopper/g' sedtest.txt
-  change "fly" with "grasshopper" in sedtext.txt file

