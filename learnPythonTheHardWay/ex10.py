#know the escape sequences
#\\ Backslash (\)
#\' Single-quote (') \" Double-quote (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only) \r ASCII carriage return (CR)
#\t ASCII horizontal tab (TAB)
#\uxxxx Character with 16-bit hex value xxxx (Unicode only) \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only) \v ASCII vertical tab (VT)
#\ooo Character with octal value oo
#\xhh Character with hex value hh
#double quote and single quotes are the same
#%s uses the str function and %r uses the repr function
#%s is just plain text, %r is text with '' around it
tabby_cat = "\t I'm tabbed in."
persion_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''


# the following codes print out the variables 
print(tabby_cat)
print(persion_cat)
print(backslash_cat)
print(fat_cat)

# Study drill 3
c = '''
\'hello everyone\'
\\ my name is you\\
I'm trying to test the function \b
and \a
Thank you very much
'''

print(c)