# POSTOLACHE ALEXANDRU-GABRIEL 321CB 
import sys
#function which makes a vector of numbers from a string
def getFinalStates(s):
#the nr of words is given by the nr of " " +1
	number = s.count(" ") + 1
	words = s.split(" ")
	for i in range(0,number):
		fStates.append(int(words[i]))#string to int
	return fStates

def readTM(l):	
#we will split it in rows
	nrLines = l.count("\n") + 1
	lines = l.split("\n")
	fct = lines[0]
	words = lines[1]
	nrStates = int(lines[2])
	if (lines[3]=="-"):
		fStates = 0	#no final states
	else:
		fStates = getFinalStates(lines[3])
	for i in range(4,nrLines):
		tranzitions.append(lines[i])	
#in pyhton we can return more var as a tuplet
	return (fct, words, nrStates, fStates, tranzitions)

#we search for our transition
def searchT(t, state, input):
	k = 0
	nr =0
	found = 0
	for i in t:
		d = i.split(" ")
		nr = nr+1
		if (d[0]==state and input==d[1]):
			k = nr-1#we found our tranzition
			found = 1
	if(found == 0):
		 return "False"
	return t[k]


def step(u, q, v):
	t = searchT(TM[4], q, v[0])
#when we don't find a tranzition
	if (t=="False"):
		return False
	d = t.split(" ")
	q = d[2]
	v = d[3] + v[1:]
	if (d[4]=='R'):#move the cursor to right
		u = u + v[0]
		v = v[1:]
		if (v == ""):#when u or v is finnished they become #
			v = v + "#"
	if (d[4] == 'L'):#to left
		v = u[len(u)-1] + v
		u = u[:-1]
		if (u == ""):
			u = u + "#"
	return(u, q, v)


def applyStep(s):
	nr = s.count(" ") + 1
	d=s.split(" ")#we split the input in words
	res = " "
	for i in range(0,nr):#for every word
		#exclude the ()
		d[i] = d[i][:-1]
		d[i] = d[i][1:]
		sd = d[i].split(",")
		u = sd[0]
		q = sd[1]
		v = sd[2]
		conf = step(u, q, v)
		if(conf != False):
			res = res + "("+conf[0]+","+conf[1]+","+conf[2]+") "
		else:
			res = res + "False "
#delete the spaces
	res = res[1:]
	res = res[:-1]
	print(res)	


def accept(M, word):
#u, c, v are in the starting point
	u = "#"
	c = "0"
	v = word
	lastState = 0
	t = (u, c, v) 
	while t!=False:
		lastState = t[1]
#we will run step untill it stops
		t = step(t[0], t[1], t[2])
	if M[3] == 0:#we have no final states
		return False
#it's accepted if the lastState is one of the final states
	if int(lastState) in M[3]:
		return True
	else:
		return False


def applyAccept(TM):
#for every word we will run the TM
	nr = TM[1].count(" ") + 1
	d = TM[1].split(" ")
	s = ""
	for i in range(0, nr):
		if(accept(TM, d[i]) == True):
			s = s + " True"
		if(accept(TM, d[i]) == False):
			s = s + " False"
	s = s[1:]
	print(s)


def k_accept(k, M, w):
	nr = 0
	t = ("#", "0", w)
	lastState = "0"
	while t!=False:#untill we can run step
		lastState = t[1]
		#nr = nr + 1
#if the number of times in which we ran step is bigger
#than k than it means it wasn't accepted in k steps
		if nr > k:
			return False
		nr = nr + 1 
		t = step(t[0], t[1], t[2])
	if M[3] == 0:
		return False
	if int(lastState) in M[3]:
		return True
	else:
		return False


def applyK_accept(M):
	nr = M[1].count(" ") + 1
	d = M[1].split(" ")
	s = ""
	for i in range(0, nr):
#k and word are separated by ',''
		v = d[i].split(",")
		if(k_accept(int(v[1]), M, v[0]) == True):
			s = s + " True"
		if(k_accept(int(v[1]), M, v[0]) == False):
			s = s + " False"
	s = s[1:]
	print(s)


#main
#reads all the input in the same string
l = sys.stdin.read()
#we declare the variables from the truplu
nrStates = 0#number of states
fct = " "
words = " "
fStates = []
tranzitions = []
TM = ()
TM = readTM(l)
#based on the first word we know what function to apply
if (TM[0] == "step"):
	applyStep(TM[1])
if (TM[0] == "accept"):
	applyAccept(TM)
if (TM[0] == "k_accept"):
	applyK_accept(TM)
