#!/usr/bin/python
# -*- coding: utf-8 -*-

print 'Exercise 1'
     
keimeno= raw_input("Πληκτρολογίστε το κείμενό σας:")

#Έλεγχος ότι ο χρήστης θα μας εισάγει το κείμενο του	 
while (keimeno==0):
     
	 keimeno= raw_input("Πληκτρολογίστε το κείμενο σας:")

x=list(keimeno)

yparxei_th=False 

#Καθορισμός του ορίου που θα ψάξουμε για θαυμαστικά που είναι το μέγεθος του κειμένου πλην 1 επειδή θα χρησιμοποιηθούν οι δείκτες της λίστας
y=len(keimeno)-1

while (y>=0): #Εκκίνηση ελέγχου από το τέλος για να εξασφαλίσουμε τα θαυμαστικά στο τέλος
  if x[y]!= "!":
     yparxei_th=True #Δεν βρήκε θαυμαστικό 
  elif yparxei_th:
    #Βρήκε θαυμαστικό
      del x[y]
  y=y-1
 
teliko_keimeno=' '.join(x) #μετατρέπουμε την λίστα ξανά στο τελικό κείμενο του χρήστη με σβησμένα τα θαυμαστικά

print teliko_keimeno
print "End of Exercise 1"