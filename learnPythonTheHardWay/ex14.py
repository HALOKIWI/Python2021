from sys import argv

script, user_name, eheheh = argv
prompt = '>>>> '

print("%s %s, I'm  the %s script. "%(eheheh, user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?. " %(user_name))
lk = input(prompt)
print("Where do you live %s?" %(user_name))
lv = input(prompt)
print("What kind of computer do you have??" )
c = input(prompt)

print("""
Yea you said %r about liking me.
You live in %r, not sure where the fxxk there is.
And you have a %r computer. Great Job.
"""%(lk,  lv, c))