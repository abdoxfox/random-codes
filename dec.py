#       ______________________________________
#    | just for fun
#    | resversed script from node js to python
#      _______________________________________

import base64,json
import re,sys

def frombase64(bas64chrs,padding,encodeddata):
	if not bas64chrs:
		bas64chrs='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	if not padding:
		padding ="="
	result =''
	encoded = ''
	base64inv ={'0':0,'1':1,'2':2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
	
	for i in range(len(bas64chrs)):
		base64inv[bas64chrs[i]] = i
	
	encoded = encodeddata
	onePadding = encoded[-1]
	twoPadding = encoded[-2]
	
	if (onePadding == twoPadding) and (onePadding==padding):
		padding = 'AA'
	
	elif (onePadding != twoPadding) and (onePadding==padding):
		padding="A"
	else:
		padding =''
		
	
	encoded = encoded[0:len(encoded)-len(padding)] + padding
	v = 0
	for xd in range(len(encoded)):
		if v>=len(encoded):
			break
		dn = base64inv[encoded[v]]
		en = base64inv[encoded[v+1]]
		fn  = base64inv[encoded[v+2]]
		gn = base64inv[encoded[v+3]]
		d = dn <<18
		e = en << 12
		f = fn <<6
		g = gn
		n = d+e+f+g
		a = (n >> 16) & 255
		b = (n >> 8) & 255
		c = n & 255
		z = chr(a);y=chr(b);w=chr(c)
		result += z+y+ w
		v+=4
		
	return result[:len(result)-len(padding)]

def reverseString(strg):
	return strg[::-1]		
		

def xordecrypt(key,data):
	predata =''
	result = ''
	k = 0
	for c in range(0,len(data)):
		
		if k >= len(data):
			break
		predata += chr(ord(bytes.fromhex(data[k:k+2])))
		k+=2
		
		
	b= 0
	for d in range(len(predata)):
		if b>= len(key):
			b=0
		result += chr(ord(predata[d]) ^ ord(key[b]))
		b+=1
	
	return result

def customb64(arg):
	return frombase64("RkLC2QaVMPYgGJW/A4f7qzDb9e+t6Hr0Zp8OlNyjuxKcTw1o5EIimhBn3UvdSFXs?", "?",arg)

with open('/sdcard/decrypt.txt','r') as file:
		jsond = json.loads(file.read())
try:
    salt = jsond["configSalt"]
except:
    salt = "EVZJNI"


for k ,v in jsond.items():
	try:
	    print(f"{k} : {xordecrypt(salt,customb64(reverseString(v)))}")
	except:
	    
	    print(f"{k} : {v}")
	
	
