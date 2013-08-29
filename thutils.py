import math
# (C) Tom Hands 2013
# Some utilities useful for python analysis

#subtracts off an integer number of period from a to leave it as a number between 0 and period
def intoPeriod(a, period = 2 * math.pi):
	return a - math.floor(a/period) * period

#Find the difference between 2 numbers over a period - works as a - b
def periodicSubtract(a, b, period = 2 * math.pi):
	a = intoPeriod(a)
	b = intoPeriod(b)
	if b > a:
		a = a + period
	return a - b

#Cumulative frequency of data (for histogram etc)
def cumulativeFreq(data, totalCats, lastCat):
    data.sort() #Order data
    cat = range(totalCats)
    cat.append(totalCats) #Range only generates upto the required value so append an extra one
    cat = np.multiply(float(lastCat)/float(totalCats), cat)
    noBelowCat = [0] * (totalCats + 1)
    n = 0
    tot = 0
    for i in range(totalCats + 1):
        #Spool through data values until leaving the category
        while n < len(data) and data[n] <= cat[i]:
            n = n + 1
            #print(str(n) +", "+str(i))
        noBelowCat[i] = n
    return cat, noBelowCat

#Three dimensional mathematical vector	
class vector():
    x = 0
    y = 0
    z = 0
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, other): #Dot product
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    def __str__(self):
        return "x = " + str(self.x) + " y = " + str(self.y) + " z = " + str(self.z)
    def mag(self):
        return  math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    def magSquare(self):
        return(self.x*self.x + self.y*self.y + self.z*self.z)
    def mul(self, scalar):
        return vector(self.x*scalar, self.y*scalar, self.z*scalar)
    #Returns an array of one component from an array of vectors
    @staticmethod
    def comp(arr, which):
        res = []
	for vect in arr:
            res.append(getattr(vect, which, 0))
	return res
