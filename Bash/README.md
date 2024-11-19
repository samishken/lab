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
