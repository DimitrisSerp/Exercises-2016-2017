#!/usr/bin/python
# -*- coding: utf-8 -*-

print 'Exercise 3'
     
keimeno= raw_input("Πληκτρολογίστε το κείμενό σας:")

#Έλεγχος ότι ο χρήστης θα μας εισάγει το κείμενο του	 
while (keimeno==0):
     
	 keimeno= raw_input("Πληκτρολογίστε το κείμενο σας:")

x=list(keimeno)

y=len(keimeno)-1


metr=0 #Μετρητής που θα μετράει πόσες φορές συναντήσε 0 στη λίστα

for i in range (0,y):
     
     if x[i]== "0":
	     del x[i]
	     metr=metr+1
	     
		 for j in range (1,metr): #Όσες φορές έσβησε μηδενικά από την λίστα τόσες φορες θα προσθέσει μηδενικά στο τέλος της
		      
		      x.extend([0])
	

print x
print "End of Exercise 3"






