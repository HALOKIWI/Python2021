from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" %(from_file, to_file))

indata = in_file = open(from_file).read()

print("The input file is %d bytes long" %len(indata))

print("Does the output file exist? %r" %exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input();
out_file = open(to_file, 'w')
out_file.write(indata)


print("Alright, all done.")
out_file.close()

#as a file is opened in write, it is locked for editing. so if you dont close , you cant ahve access to the file outside the program while it's open in python


