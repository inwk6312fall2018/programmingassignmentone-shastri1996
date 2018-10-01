config=open("running-config.cfg")
for line in config:
	line=line.strip()
	line=line.split()
	print(line)
