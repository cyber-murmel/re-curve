#re-curve
This program is capable of drawin nice fractals with python.
###preparation
The requirement for this function is a running graphic envronment (X) an havin tk-inter installed.
for Debian, Mint, Ubuntu:
```sudo apt-get install python python-tk idle python-pmw python-imaging```
For ervery other system check out the tkinter [How to install](http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter) webpage.
###use
The re_curve.py script is executed from command line with several optional arguments.
```
* -c --curve    enter the name of the curve you want to be drawn
* -b --base     defines the length of a basic element in pixels
* -g --gens     define the number of genearions you want to be shown
* -s --speed    define the turtle speed (1-10; 0 is fastes)
* -r --rainbow  activate the rainbow mode
* -f --file     give a path where the curve will be written to as a postscript file
```
