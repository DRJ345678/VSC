str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)
piece = str[ipos+2:]
print(piece)
#print(piece+42.0) # will fail because piece is a string
value = float(piece)
print(value)
print(value+42.0)