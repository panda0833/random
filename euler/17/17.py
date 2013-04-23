words_to_19 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
words_len = map(lambda x: len(x), words_to_19)

words_teens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#words_teens_len = [6, 6, 6, 5, 5, 7, 6, 6]
words_teens_len = map(lambda x: len(x), words_teens)

#length of 'hundred'
h_len = 7

#length of 'and'
a_len = 3

# sum 1 to 19
a = sum(words_len)

# sum 20 to 99

# twenty, thirty, fourty...
b = sum(words_teens_len)

# twenty one, twenty two... thirty one, thirty two... ...
b = b*10 + sum(words_len[0:9])*8 

# sum 100 to 999

# all ones, twos, threes beginning the 100s like
# one hundred, one hundred and one, two hundred, two hundred and one
c = sum(words_len[0:9]) * 100

# all 'hundred' from 100 to 999 
c = c + h_len * 100 * 9 

# all 'and' in hundreds such as one hundred 'and' one,
# one hundred 'and' two, etc
c = c + 99 * 9 * a_len

# all 1 to 99 for each hundred (100s, 200s, etc) 
c = c + (a+b)*9

# one thousand
d = len('one') + len('thousand')

print a + b + c + d 

