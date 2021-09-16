"""
README part ************************************************************************************************************************************************************************************
A Python program to build a diophaintine equation solver program in python
Eventually i am going to just read from a data file at least i think not sure yet. 
Example of how you input into the command line and eventually from file if i do go thru with making this feature. (debating as is it really easiler to input in a file rather then terminal screen )
x^2+z+y = 14  # diophaintine equation
x z y         # variables 
0 1 2         # start range of variables
30 400 5000   # end range of variables
1  10  100    # incremental jumps for variables
Delimited  by a new line or a chosen delimiter for each set of equations in file
Currently you just manually type the info into the commandline to build the dioequ.py file which contains the individual diophaintine equation programs delimited by $$$$$$$$$$$$$.
Please feel free to modify anyway you want and improve on it.
The reason why i wanted to write it is python has bignum built in if your like me in the olden days 
you had problems just using standard data types because you can only go so high before overflows and other stuff causes problems.
Now since bignum is built into this language and parsing is actually much easier as well it a simply way to code up what would take c, java ,...etc parsing a lot of lines of code more.
Its more practical to cook up a program for distributive diophaintine equation solving using this small program.
So the guys that have the more resources i like to see you run it on bunches of computers after all this generates programs that run in P time.
Well P in the start and end ranges used and number of variables. Which seems for huge server rooms you see alot more neat stuff.
Google and other places are better suited to solve hard polynomial time algorithms fast 
Obviously NP is not going to work well on any server rooms but P will
Exploring is the fun side to computational mathematics :)
And i don't see many diophaintine solvers out there that are as general as this.
I see how i can make the incremental jumps a little more general with lamda functions so then you really can search in any ranges and any patterns in those ranges for solutions.
But for now this covers the 90% 
************************************************************************************************************************************************************************************************
"""


equ = raw_input("Enter your diophaintine equation: \n") ; 
equname = equ ;
vars = raw_input( "Enter the distinct variable symbols used in diophaintine equation in left to right first occurence order: \n " ) ;
varss = vars.split(" ") ;

print( "Example x^2+y^3+z=35 you enter 2 3 4 for these start values  x=2 , y=3, z=4\n" ) ;
print( "Example z^2+y^3+x=35 you enter 2 3 4 for these start values  x=4 , y=3, z=2\n" ) ;
print( "Remember input first occuring variable in equation then second , third , so on!\n") ;

startr = raw_input("Enter the starting range of each variable  \n") ;
endr = raw_input("Now enter end ranges using same convention as start ranges\n" ) ;

jmps = raw_input( "Enter the jump patterns to increment each variable by using order convention for variables above: \n " ) ;
jmpss = jmps.split(" ") ;


startrr = startr.split(" ") ;
endrr = endr.split(" ") ;


tab=""
checkingvalue="" ;
jmpattern = "1" ;

equ = equ.replace("^", "**") ;
print equ
print equ.find("=") ;
i = equ.find("=") ;
print i
checkingvalue=equ[i+1:len(equ)]
equ = equ[0:i] ;
print( equ );

for i in xrange(0,len(varss)):
	equ = equ.replace( varss[i] , "i"+ str(i) ) ; 

varct=0;
f= open("dioequ.py" , "a+")


varct = len(varss)
print( str(varct) ) ;

f.write("\n") ;
f.write( "#### " + equname ) ;
f.write("\n") ;

for i in xrange(0,varct):
	f.write( "i"+str(i)+" = "+ startrr[i]  +" ;\n" ) ;

for i in xrange(0,varct):
	f.write( tab + "while( i"+str(i)+ " < "+ endrr[i] +" ):\n" ) ;
	tab+="\t" ;

f.write( tab + "if " + equ + " == " + checkingvalue + " : \n " ) ;

f.write( tab + "\tprint( " ) ;
for i in xrange(0,varct-1):
	f.write(  "i"+str(i) + " ,  " ) ;

f.write( "i"+str(varct-1) + " ); \n" ) ; 
f.write( tab + "i"+str(varct-1) + "+=" + jmpss[varct-1] + ";\n" ) ;

tab=tab[0:len(tab)-1];

for x in range(varct-1, 0,-1):
	f.write( tab + "i"+ str(x) + "=" + startrr[x]  +";\n" ) ;
	f.write( tab + "i"+ str(x-1) + "+=" + jmpss[x-1] +";\n" ) ;
	tab=tab[0:len(tab)-1];



f.write("\n") ;
f.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n" ) ; #write 30 $ symbols to delimit where the different diophiantine equations are!

f.close() ;
