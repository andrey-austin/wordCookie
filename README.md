# wordCookie
This simple program will give you all the possible words for the game wordcookie. Works on 3-15 letter words.

REQUIREMENTS: pyenchant 

Install via pip

#Install on windows 

pip install pyenchant


#Install on mac 

brew update

brew install enchant


If you are using MacPorts you can also install the enchant2 package. Please make sure to add the port variants for the spellers you’d like to use. For example, to build the enchant library for aspell and hunspell, use:

sudo port install enchant2 +aspell +hunspell +applespell
  
  
An other way to use pyenchant is to install MinGW (for instance with Chocolatey), then use pacman to install the libenchant and all its dependencies.
In that case, you can ask pip to not use the wheel by running it like this:

pip install --no-binary pyenchant


Troubleshooting
To have a clue about what is wrong, you can set the PYENCHANT_VERBOSE_FIND environment variable to any non-empty value and run:

python -c 'import enchant'

pyenchant documentation found here: https://pypi.org/project/pyenchant/


wordCookie install:

git clone https://github.com/andrey-austin/wordCookie.git

Move into directory:
cd wordCookie

Make executable:
chmod +x wordcookie.py

Run wordcookie:
type: python into the terminal, followed by the script name, then the word/letters you want to find. See example below.

python wordcookie.py word
