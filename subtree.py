child = {}
father = {}
in_degree = {}
out_degree = {}
score = {}
num = {}
misuse_radio = 1
decay_radio = 0.5
normal_radio = 1.2


# 1. Check if a circle exists in the graph
############################################
def circle_check():
	while True:
		flag = 0
		temp = []
		for i in in_degree.keys():
			if in_degree[i] == 0:
				flag = 1
				temp.append(i)
				for j in child[i].keys():
					in_degree[j] -= 1
		for i in temp:
			in_degree.pop(i, None)
		if flag == 0 and len(in_degree.keys()) > 0:
			return 'circle exist'
		if len(in_degree.keys()) == 0:
			return 'circle not exist'


# 2. Load the topo and anomaly score of the provenance graph
############################################
def setup():
	f3 = open('edges.txt', 'r')
	for line in f3:
		src_node = int(line.strip('\n').split(' ')[0])
		dst_node = int(line.strip('\n').split(' ')[1])
		if not src_node in in_degree.keys():
			in_degree[src_node] = 0
			out_degree[src_node] = 0
			child[src_node] = {}
			father[src_node] = {}
		if not dst_node in in_degree.keys():
			in_degree[dst_node] = 0
			out_degree[dst_node] = 0
			child[dst_node] = {}
			father[dst_node] = {}
		if not src_node in father[dst_node].keys(): in_degree[dst_node] += 1
		if not dst_node in child[src_node].keys(): out_degree[src_node] += 1
		child[src_node][dst_node] = 1
		father[dst_node][src_node] = 1
	f3.close()



	f2 = open('anomaly_score.txt', 'r')
	for line in f2:
		node_id = int(line.strip('\n').split(' ')[0])
		temp_score = float(line.strip('\n').split(' ')[1])
		score[node_id] = temp_score - normal_radio
	f2.close()

	f = open('fine_rules_id.txt', 'r')
	for line in f:
		node_id = int(line.strip('\n'))
		score[node_id] += misuse_radio
	f.close()
	
	return 1
	

# 3. Compute the final anomaly score of each node
############################################
def score_iter():
	for i in out_degree.keys():
		if score[i] > 0.5:
			num[i] = 1
		else:
			num[i] = 0

	# Compute the final anomaly score
	while True:
		if len(out_degree.keys()) == 0: break
		temp = []
		for i in out_degree.keys():
			if out_degree[i] > 0: continue
			for j in father[i].keys():
				score[j] += decay_radio*score[i]
				num[j] += decay_radio*num[i]
				out_degree[j] -= 1
			temp.append(i)
		for i in temp:	
			out_degree.pop(i, None)
	
	maxm = 0
	maxi = 0
	# Find the node with biggest anomaly score
	for i in child.keys():
		if score[i] + num[i] > maxm:
			maxm = score[i] + num[i]
			maxi = i
	print(maxi, maxm)
	ans = {}
	ans[maxi] = 1
	ans_temp = {}
	ans_temp[maxi] = 1
	while True:
		ans_temp2 = {}
		for i in ans_temp.keys():
			for j in child[i].keys():
				ans[j] = 1
				ans_temp2[j] = 1

		ans_temp = {}
		for i in ans_temp2.keys():
			ans_temp[i] = 1
		if len(ans_temp.keys()) == 0: break
	
	print(len(child[maxi].keys()))

	# Pruning
	print('before prune', len(ans.keys()))
	cnt = 0
	for i in ans.keys():
		cnt += 1
		if cnt > 10: break
		print(score[i], num[i], len(child[i].keys()))

	temp = []
	for i in ans.keys():
		if score[i] <= 0: temp.append(i)
	for i in temp:
		ans.pop(i, None)
	print('after prune', len(ans.keys()))
	

	# Output the topo of anomaly subtree
	fw = open('anomaly_tree.txt', 'w')
	for i in ans.keys():
		for j in child[i].keys():
			fw.write(str(i) + ' ' + str(j) + '\n')	
	fw.close()

	return 1
	



setup()
a = circle_check()
print(a)
if a == 'circle exist':
	exit(0)
score_iter()


