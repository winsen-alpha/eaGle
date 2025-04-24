des = {}
f = open('fine_rules_id.txt', 'r')
for line in f:
	des[line.strip('\n').split(' ')[0]] = line.strip('\n').split(' ')[1]
f.close()

f = open('coarse_rules_id.txt', 'r')
for line in f:
	des[line.strip('\n').split(' ')[0]] = line.strip('\n').split(' ')[1]
f.close()


f = open('anomaly_tree.txt', 'r')
fw = open('ans.txt', 'w')
for line in f:
	nodes= line.strip('\n').split(' ')
	fw.write(line.strip('\n'))
	if nodes[0] in des.keys():  fw.write(' ' + des[nodes[0]])
	if nodes[1] in des.keys():  fw.write(' ' + des[nodes[1]])
	fw.write('\n')
f.close()
fw.close()

