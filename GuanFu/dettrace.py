import gdb 
gdb.execute("set logging on")
gdb.execute("set height 0")

f = open("dettrace.map", 'r')
for line in f:
	gdb.execute("b " + line[19:len(line)-1]);
f.close()

gdb.execute("run date");

while 1:
	gdb.execute("bt");
	gdb.execute("c");
