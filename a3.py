# a3.py
# Kathryn Zimmerman kpz8, Max Senkovsky mgs253
# 10/6/2014
""" Functions for Assignment A3"""
import colormodel
import math

def complement_rgb(rgb):
   """Returns: the complement of color rgb.
   
   Precondition: rgb is an RGB object"""

   assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
 
   return colormodel.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def truncate5(value):
   """Returns: value, as a string, using exactly 5 characters.

   The truncated value will have one of the forms:
      ddd.d      Example:  360.1
      dd.dd      Example:  29.53
      d.ddd      Examples: 4.003,  0.001,  and 0.000
   
   Precondition: value is a number (int or float), 0 <= value <= 999."""
   
   assert type(value) == int or float, value + 'is not an int or float'
   assert 0 <= value and value <= 999, value + ' is not in range'
   

   if type(value) == int:
      value = float(value)
   if value < 0.001:
      value = 0.0

   s = str(value) + '00'

   return s[:5]    


def round5(value):
   """ Returns: value, but expand or round to be (if necessary) exactly 5 characters.
   
   Examples:
      Round 1.3546  to  1.355.
      Round 1.3544  to  1.354.
      Round 21.9954 to  22.00.
      Round 21.994  to  21.99.
      Round 130.59  to  130.6.
      Round 130.54  to  130.5.
      Round 1       to  1.000.
   
   Precondition: value is a number (int or float), 0 <= value <= 360."""
   
   assert type(value) == int or float, value + 'is not an int or float'
   assert 0 <= value and value <= 360, value + ' is not in range'
   
   if type(value) == int:
      value = float(value)
      
   if str(value).index('.') == 1:
      value = round(value,3)
      
   if str(value).index('.') == 2:
      value = round(value,2)
      
   if str(value).index('.') == 3:
      value = round(value,1)
  
   return truncate5(value)
   

def round5_cmyk(cmyk):
   """Returns: String representation of cmyk in the form "(C, M, Y, K)".
   
   In the output, each of C, M, Y, and K should be exactly 5 characters long.
   Hence the output of this function is not the same as str(cmyk)
   
   Precondition: cmyk is an CMYK object."""
   
   assert (type(cmyk) == colormodel.CMYK), 'Value '+ `cmyk`+' is not a CMYK object' 

   return '(' + round5(cmyk.cyan) + ', ' + round5(cmyk.magenta) + ', '\
         + round5(cmyk.yellow) + ', ' + round5(cmyk.black) + ')'


def round5_hsv(hsv):
   """Returns: String representation of hsv in the form "(H, S, V)".
   
   In the output, each of H, S, and V should be exactly 5 characters long.
   Hence the output of this function is not the same as str(hsv)

   Precondition: hsv is an HSV object."""
   
   assert (type(hsv) == colormodel.HSV), 'Value '+ `hsv`+' is not a HSV object'

   return '(' + round5(hsv.hue) + ', ' + round5(hsv.saturation) + ', ' \
         + round5(hsv.value) + ')'
   

def rgb_to_cmyk(rgb):
   """Returns: color rgb in space CMYK, with the most black possible.

   Formulae from http://www.easyrgb.com/index.php?X=MATH.

   Precondition: rgb is an RGB object"""
   
   assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
   
   R = (rgb.red)/255.0
   G = (rgb.green)/255.0
   B = (rgb.blue)/255.0
   Cp = 1 - R
   Mp = 1 - G
   Yp = 1 - B
   if Cp == Mp == Yp == 1:
      return colormodel.CMYK(0, 0, 0, 100)
   
   K = (min(Cp, Mp, Yp))
   C = 100*((Cp - K)/(1 - K))
   M = 100*((Mp - K)/(1 - K))
   Y = 100*((Yp - K)/(1 - K))
   K = 100*K

   return colormodel.CMYK(C, M, Y, K)


def cmyk_to_rgb(cmyk):
   """Returns : color CMYK in space RGB.

   Formulae from http://www.easyrgb.com/index.php?X=MATH.
   
   Precondition: cmyk is an CMYK object."""
   
   assert (type(cmyk) == colormodel.CMYK), 'Value '+ `cmyk`+' is not a CMYK object'
   
   C = (cmyk.cyan)/100.0
   M = (cmyk.magenta)/100.0
   Y = (cmyk.yellow)/100.0
   K = (cmyk.black)/100.0
   R = 255*(1 - C)*(1 - K)
   G = 255*(1 - M)*(1 - K)
   B = 255*(1 - Y)*(1 - K)
   R = round(R)
   G = round(G)
   B = round(B)

   return colormodel.RGB(int(R), int(G), int(B))


def rgb_to_hsv(rgb):
   """Return: color rgb in HSV color space.

   Formulae from wikipedia.org/wiki/HSV_color_space.
   
   Precondition: rgb is an RGB object"""
   
   assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
   
   R = (rgb.red)/255.0
   G = (rgb.green)/255.0
   B = (rgb.blue)/255.0
   MAX = max(R,G,B)
   MIN = min(R,G,B)
   
   if MAX == MIN:
      H = 0
   elif MAX == R and G >= B:
      H = 60.0 * (G - B) / (MAX - MIN)
   elif MAX == R and G < B:
      H = 60.0 * (G - B) / (MAX - MIN) + 360.0
   elif MAX == G:
      H = 60.0 * (B - R) / (MAX - MIN) + 120.0
   elif MAX == B:
      H = 60.0 * (R - G) / (MAX - MIN) + 240.0
   if MAX == 0:
      S = 0
   else:
      S = 1 - MIN/MAX
   
   V = MAX
   
   return colormodel.HSV(H, S, V)


def hsv_to_rgb(hsv):
   """Returns: color in RGB color space.
   
   Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
   
   Precondition: hsv is an HSV object."""
   
   assert (type(hsv) == colormodel.HSV), 'Value '+ `hsv`+' is not a HSV object'
   
   H = hsv.hue
   S = hsv.saturation
   V = hsv.value
   Hi = math.floor(H/60)
   f = (H/60) - Hi
   p = V*(1-S)
   q = V*(1-f*S)
   t = V*(1-(1-f)*S)
   if Hi == 0:
      R = V
      G = t
      B = p
   elif Hi == 1:
      R = q
      G = V
      B = p
   elif Hi == 2:
      R = p
      G = V
      B = t
   elif Hi == 3:
      R = p
      G = q
      B = V
   elif Hi == 4:
      R = t
      G = p
      B = V
   elif Hi == 5:
      R = V
      G = p
      B = q
   
   R = round(255*R)
   G = round(255*G)
   B = round(255*B)
   
   return colormodel.RGB(int(R),int(G),int(B))
