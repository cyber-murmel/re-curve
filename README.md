<h1>re-curve</h1>
This program is capable of drawing nice fractals with python.
<h3>preparation</h3>
The requirement for this function is a running graphic envronment (X) an havin tk-inter installed.
for Debian, Mint, Ubuntu:
```sudo apt-get install python python-tk idle python-pmw python-imaging```
For every other system check out the tkinter [How to install](http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter) webpage.
<h3>commandline syntax</h3>
The re_curve.py script is executed from command line with several optional arguments.
```
./re_curve.py [-c] curve [-b] base [-g] gens [-s] speed [-r] [-f] filepath
* -c --curve    enter the name of the curve you want to be drawn
* -b --base     defines the length of a basic element in pixels
* -g --gens     define the number of genearions you want to be shown
* -s --speed    define the turtle speed (1-10; 0 is fastes)
* -r --rainbow  activate the rainbow mode
* -f --file     give a path where the curve will be written to as a postscript file
```
