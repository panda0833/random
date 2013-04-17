#length of one, two, three, four... nineteen 
words_len = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8 ]

#length of twenty, thirty, fourty... ninety
words_teens_len = [6, 6, 6, 5, 5, 7, 6, 6]

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

# all 'hundred' from 100 to 999 
c =  h_len * 100 * 9 

# all 1 to 99 for each hundred (100s, 200s, etc) 
c = c + (a+b)*9

# all ones, twos, threes beginning the 100s like
# one hundred, one hundred and one, two hundred, two hundred and one
c = c + sum(words_len[0:9]) * 100 * 9

# all 'and' in hundreds such as one hundred 'and' one,
# one hundred 'and' two, etc
c = c + 99 * 9 * a_len

# one thousand
d = len('one') + len('thousand')

print a + b + c + d 

