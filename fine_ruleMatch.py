# 1. Load the mapping relationship of nodes_Name and nodes_ID
############################################
f = open('id_to_uuid.txt', 'r')
l = {}
for line in f:
	l[line.strip('\n').split(' ')[1]] = int(line.strip('\n').split(' ')[0])
f.close()

# 2. Fine rules matching
############################################
f = open('fine_rules.txt', 'r')
fw = open('fine_rules_id.txt', 'w')
for line in f:
	fw.write(str(l[line.strip('\n').split(' ')[0]])+' '+line.strip('\n').split(' ')[1]+'\n')

f.close()
fw.close()


# 3. Coarse rules matching
############################################
f = open('coarse_rules.txt', 'r')
fw = open('coarse_rules_id.txt', 'w')
for line in f:
	fw.write(str(l[line.strip('\n').split(' ')[0]])+' '+line.strip('\n').split(' ')[1]+'\n')

f.close()
fw.close()

