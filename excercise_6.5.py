text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(' ')
num= float(text[pos:])
print(num)
