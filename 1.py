'''
Python challenge p.1
The hint:
  k -> m
  o -> q
  e -> g
which looks like a mapping, until you realize
that it leaves too many nonsense letters (even
if it's bidirectional).  but if we note instead
that m is exactly 2 letters in front of k, as q 
is to o, and g is to e...
'''

text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

result = '' 
# Lists of alphanumeric a-z, A-Z
Alphas = [chr(i) for i in range(65,91)]
alphas = [chr(i) for i in range(97,123)]

for letter in text:
  # Calculate once for efficiency
  numrepr = ord(letter)
  # If it's an alphanumeric...
  if letter in alphas or letter in Alphas:
    # Take care of wrapping around the sequence
    if ( numrepr + 3 ) > 123: 
      result += chr( 97 + (numrepr + 2)%123 )
    else:
      result += chr( numrepr + 2 )
  # Otherwise, it's a special character and we don't
  # want to remap those.
  else:
    result += letter

# Print the result.
print(text)
print(result)
