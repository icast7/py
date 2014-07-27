from sys import argv

script, filename = argv

print "Here's your file %r:" % filename

txt = open(filename)
print txt.read()

txt.close()


print "Type the filename again:"
#Get input 
file_again = raw_input(">")
 
txt_again = open(file_again)

print txt_again.read()

txt_again.close()