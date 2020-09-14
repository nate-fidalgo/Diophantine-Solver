# recreational-math
This program is used to search for solutions to any types of diophaintine equation in any number of variables.
The search pattern can be a brute force run thru a given start range to ending range.
Or one can set a custom search pattern where one searches a special pattern of numbers for solutions to the diophaintine equation.
Another really neat feature is that because pythonV3 has bignum libraries builtin to there interperter this program is not restricted to any size ranges to check.
<br>
Very neat program for people that have many computers , cpu/cores or has abilities to setup distributive computation 
This program can act as a way to quickly compute distributively diophaintine equations or explore new patterns of search to find solutions!!!
<br>
Python is a great language and usually comes installed by default on linux/unix systems 
<br>All that is required is diopy.py file and to run it type `python diopy.py` at the terminal then enter the information in the format below
<br>
<pre>
<code>
x^2+z+y = 14  # diophaintine equation to solve
x z y         # variables in the order they first appear left to right in above equation
0 1 2         # start range of the x z y variables
30 400 5000   # end range of the x z y variables
1  10  100    # incremental jumps for the x z y variables
</code>
</pre>
<br>
<code>The incremental jumps mean variables will increment like i+=1 , z+=10 , y+=100 one can make more complex type of jump patterns/searches </code>
