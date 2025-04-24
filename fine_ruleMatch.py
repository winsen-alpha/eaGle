f = open('id_to_uuid.txt', 'r')
l = {}
for line in f:
	l[line.strip('\n').split(' ')[1]] = int(line.strip('\n').split(' ')[0])
f.close()

f = open('fine_rules.txt', 'r')
fw = open('fine_rules_id.txt', 'w')
for line in f:
	fw.write(str(l[line.strip('\n').split(' ')[0]])+' '+line.strip('\n').split(' ')[1]+'\n')

f.close()
fw.close()


	
f = open('coarse_rules.txt', 'r')
fw = open('coarse_rules_id.txt', 'w')
for line in f:
	fw.write(str(l[line.strip('\n').split(' ')[0]])+' '+line.strip('\n').split(' ')[1]+'\n')

f.close()
fw.close()

