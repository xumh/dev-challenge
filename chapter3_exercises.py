# Exercises for chapter 3:
# Name: Mengtan
# 3.1, 3.2 NameError: name 'repeat_lyrics' is not defined
def repeat_lyrics():
	print_lyrics()
	print_lyrics()
def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."
repeat_lyrics()
# 3.3
def right_justify(s):
    print " "*(70-len(s))+s
    
right_justify('allen')
# 3.4.1-4
def do_twice(f, value):
    f(value)
    f(value)

def print_twice(anything):
    print anything
    print anything
do_twice(print_twice, 'spam')
# 3.4.5
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)
    
do_four(print_twice, 'spa')
# 3.5
def grid():
	sp = '|', " "*4,'|', " "*4,'|'
	jia = "+", "-"*4,"+", "-"*4,"+"
	print jia
	print_twice(sp)
	print_twice(sp)
	print jia
	print_twice(sp)
	print_twice(sp)
	print jia
    
grid()	