f = "{} {} {} {}"
# f stands for the formatter 


print(f.format(1, 2, 3, 4))
# place the four numbers into f
print(f.format("one", "two", "three", "four"))
# place the four strings into f
print(f.format(True, False, False, True))
# place the boolean variables into f
print(f.format(f, f, f, f))
# place the f into f
print(f.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))