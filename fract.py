from PIL import Image
import cmath
import time

screenSize = 1000
img = Image.new('RGB', (screenSize, screenSize))
maxIter = 500

def fonc(z, c):
	a = z.real*z.real - z.imag*z.imag + c.real
	b = 2*z.real*z.imag + c.imag
	return a, b

def manderbrot(x, y): #x et y sont les coordonnées de c
	x = -2 + 4*x/screenSize
	y = -2 + 4*y/screenSize
	c = complex(x, y)
	i = 0
	z = complex(0, 0)
	while (i < maxIter):
		a, b = fonc(z, c)
		z = complex(a, b)
		i += 1
		#p = pow(pow((a - 1/4), 2) + b*b, 1/2)
		#if (x < p - 2*p*p + 1/4):
		#	return (-1)
		if (a*a + b*b > 4):#si le module est superieur a 2 alors la suite est croissante
			return (i)
	return (-1)

def julia(x, y):
	x = -2 + 4*x/screenSize
	y = -2 + 4*y/screenSize
	c = complex(0, 3/4)
	i = 0
	z = complex(x, y)
	while (i < maxIter):
		a, b = fonc(z, c)
		z = complex(a, b)
		i += 1
		#p = pow(pow((a - 1/4), 2) + b*b, 1/2)
		#if (x < p - 2*p*p + 1/4):
		#	return (-1)
		if (a*a + b*b > 4):#si le module est superieur a 2 alors la suite est croissante
			return (i)
	return (-1)

def newton(x, y):
	x = -2 + 4*x/screenSize
	y = -2 + 4*y/screenSize
	c = complex(0, -3/4)
	i = 0
	z = complex(x, y)
	while (i < maxIter):
		a, b = fonc(z, c)
		z = complex(a, b)
		i += 1
		#p = pow(pow((a - 1/4), 2) + b*b, 1/2)
		#if (x < p - 2*p*p + 1/4):
		#	return (-1)
		if (a*a + b*b > 4):#si le module est superieur a 2 alors la suite est croissante
			return (i)
	return (-1)


def main():
	t = time.time()
	x, y = 0, 0
	while (x < screenSize):
		y = 0
		while (y < screenSize):
			r = manderbrot(x,y)
			if (r == -1):
				img.putpixel((x,y), (0,0,0))
			else:
				img.putpixel((x,y), (r*10,r*5,r*1))
			y += 1
		x += 1
	print(time.time()-t)



main()

img.save('fract.png')
img.show()