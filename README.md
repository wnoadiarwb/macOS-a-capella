# macOS-a-capella
This python project allows a mac computer to randomly generate phonetic compositions, which can be read (or "sung") by the built-in macOS North American English speech synthesizer. 

# Usage
(Presuming you have python installed) run the python program <i>sing</i>; I use terminal with the following commands:\
``$ cd [path to python project]``\
``$ python sing.py --live``\ 
The --live argument causes your mac to immediately sing the resultant file.\  
**Optionally** Manually tell your mac to read the output file. This can be done in terminal with:\
``$ python sing.py``\ 
and ``$ say -f out.txt`` or by opening out.txt, right clicking, and selecting speech>start speaking.\  


# Resources
A programming guide for the macOS speech synthesis API can be found here: http://mirror.informatimago.com/next/developer.apple.com/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/SpeechSynthesisProgrammingGuide.pdf \
Install Python here:\
https://www.python.org/downloads/mac-osx/
