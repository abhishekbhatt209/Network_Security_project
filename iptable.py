import iptc 
import sys
rule = iptc.Rule()
f = open("src_ip.txt","r")
ip_addres = [ip.replace("\n","") for ip in f.readlines()]
print(ip_addres)
#rule.dst = ""
print('''
******************************************

	Enter 1 for WHITE-LIST
	Enter 2 for BLACK-LIST

******************************************
	''')
c = int(input("Enter Your Choice: "))
#c = int(sys.argv[1])
#print("choice" ,c)
for ip_add in ip_addres:
	rule.src = ip_add
	print("adding rule for : ",ip_add)
	#c = int(input("Enter Your Choice : "))
	if c == 1:
		target = iptc.Target(rule,"ACCEPT")
		rule.target = target
		chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
		chain.insert_rule(rule)

	elif c == 2:
		target = iptc.Target(rule,"DROP")
		rule.target = target
		chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
		chain.insert_rule(rule)
	else:
		print("Worng input")

