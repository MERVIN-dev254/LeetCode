1. x = 1 if condition else 0 

2. Use underscores to make large numbers more readable
   10_000_000_000

3. string formatting
   print(f'{total:,}')   #total is a numeric variable  ==> 1,000,000

4. Context managers to open and close files, threads (locks), database connections #anything when managing resources
   ... with open('text.txt', 'r') as f:
		.....
		.........
   the context manager will manage and close the file for you. You dont need to remember to close it

5. Use enumerate when you need a counter when you're traversing a list
   names = ['Grace', 'Ivy', 'Marvin']
   for index, value in enumerate(names, start=1):
        print(index, value)

6. Use zip, to loop over 2 or more lists at once
   Stops after shortest list is exhausted
   names = ['Grace', 'Ivy', 'Marvin']
   names = ['Ateka', 'Akinyi', 'Otieno']

   #do it this way
   for fname, lname in zip(fnames, lnames):  #for value in zip(fnames, lnames) ==> tuple ('Grace', 'Ateka')
   ......... print(f'{fname} has second name {lname}')

7. Unpacking
   1. a, b = (1,2)
   
   2. a, _ = (1,2) #when u r not using b
   
   3. a, b, *c = (1,2,3,4,5,6)  #set c to the rest of the values # *_ ==> ignore the rest of the values

   4. a, b, *c, d = (1,2,3,4,5,6) #set d to last value, a==> first, b ==> second, c ==> the rest of the vals

8. Get & Set attributes on class objects
	class Person():
 		pass.........
        p = Person()

       # p.fname = "..."
       # p.lname = "...."

       setattr(p, 'first', 'Corey')  #setattr(object, attribute, value)
       
	first = getattr(p, first)
      #Dynamic loop set up

       p = Person()
       .....p_info = {'fname':'Jack', 'lname':'Sparrow'}
		for k, v in p_info.items():
			setattr(p, k, v)

        ...... for k in p_info.keys():
			print(getattr(p, k))

9. Inputting secret information
 	.......from getpass import getpass
	uname = input('Username:')
	pwd = input('Password:') #wrong way
        pwd = getpass('Password:') #use this instead

10. Python with -m option

     ......python -m venv my_env
	....# -m runs the module specified after -m
		.....#-m searches for the specified module in sys.path and runs it


11. Find valid attributes and methods
    ...import module
		...from datetime import datetime
 			.....dir(datetime) ==> returns all attributes and methods


	
	

    