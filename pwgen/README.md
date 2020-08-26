# Password Generator

## How to use:
The program has one required argument, the desired password length, and an optional one, to turn off symbols in passwords

The commands are entered as such:
  * python pwgen.py [password length]  **or**
  * python pwgen.py --symbols [default True] [password length]
  
--symbols or -s can be used to toggle off symbols in the generated passwords.

The password length cannot be less than 3 (w/ no symbols) or 4 (w/ symbols).
This is due to how the passwords are initially generated. 
Obviously, no program should allow you to make passwords that short.

Currently, setuptools has not been added to this script, when added the syntax will be:
  * pwgen -s [pw length]
