#!/usr/bin/python
# -*- coding: utf-8 -*-

print 'Exercise 12'

#Εισαγωγή Βιβλιοθηκών
import urllib2 
import json
import webbrowser

#Αναζήτηση συνταγής με βάση ένα συγκεκριμένο υλικό-το ψάρι
Yliko_Synt=raw_input("Δώστε το υλικό με το οποίο θέλετε να αναζητήσετε συνταγές:")
response1 = urllib2.urlopen('http://food2fork.com/api/search?key=63901198aa257c2ca3d2f29669b87094&q=fish') #Εισαγωγή σχετικής συνταγής
html1 = response1.read()
html1=html1.replace("<br>","")
html1=html1.strip()
lines1=html1.split("\n")

#Εμφάνιση της συνταγής
header1= lines1[0].split(",")
print "Η σχετική συνταγή έχει τίτλο",header1[3]

#Αναζήτηση μιας μπύρας
response2 = urllib2.urlopen('https://api.punkapi.com/v2/beers/random')#Εισαγωγή τυχαίας μπύρας
html2 = response2.read()
html2=html2.replace("<br>","")
html2=html2.strip()
lines2=html2.split("\n")

#Εμφάνιση της μπύρας
header2= lines2[0].split(",")
print "Η μπύρα έχει τίτλο ",header2[3];

#Καθορισμός πλήκτρου-κλειδιού για την ιστοσελίδα της συνταγής
x=raw_input("Για να δείτε αναλυτικότερα τη συνταγή σας πατήστε F ενώ για έξοδο πατήστε e ")


if x=="F":
     
	#Μετάβαση στην ιστοσελίδα
   x=list(header1[4])
   del x[0:16]
   del x[-1]
   k=''.join(x)
   webbrowser.open(k) 

print "End of Exercise 12"