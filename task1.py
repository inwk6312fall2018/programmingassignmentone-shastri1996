config=open("running-config.cfg")
temp_lst=[]
interface_name=[]
nameif=[]
nameif_new=[]
vlan=[]
ip=[]
id_dict={}
values=[]
for line in config:
	line=line.strip()
	line=line.split()
	temp_lst.append(line)

def extract_int_name(lst):
	for i in lst:
		for j in range(len(i)):
			if i[j]=="interface":
				interface_name.append(i[j+1])
	return(interface_name)
extract_int_name(temp_lst)
print("\n")
"""
for line in config:
	line=line.strip()
#	print(line)
	for word in line.split("!"):
		nameif.append(word)
print(nameif)
"""

def nameif_extract(lst):
	for i in lst:
		for j in i:
			if "nameif" in j:
				nameif.append(i)
	return(nameif)
nameif_extract(temp_lst)

#print(len(interface_name))
#print(len(nameif))
def nameif_formatting(nameif):
	for i in nameif:
		#print(i[1])
		if i[1]=="nameif":
			nameif_new.append("___Name Not Given___")
		else:
			nameif_new.append(i[1])
	return(nameif_new)
nameif_formatting(nameif)


def zipping(x,y):
	zipped=list(zip(x,y))
	return(zipped)
print("Tuples of interface and names-->>\n",zipping(interface_name,nameif_new))

def vlan_extract(temp_lst):
	for i in temp_lst:
		for j in i:
			if j=="vlan":
				vlan.append(i[1])
	return(vlan)
vlan_extract(temp_lst)
def ipadd(temp_lst):
	for i in temp_lst:
		if "ip" in i and "address" in i:
			ip.append(i)
	return(ip)	
ipadd(temp_lst)


def combine(x,y,z):
	values=list(zip(x,y,z))
	return(values)
combine(nameif_new,vlan,ip)


def keys(interface_name):
	for i in interface_name:
		return(i)


def value(values):
	for i in values:
		return(i)

def dict(x,y):
	id_dict[x]=y
dict(keys(interface_name),value(values))
print(id_dict)
