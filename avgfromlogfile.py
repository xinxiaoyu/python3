with open(r'D:/log/log.2019-5-12', 'r') as f:
	for line in f:
		line_new = re.split(r"[:\s]", line)
		task_name.append(line_new[7])

		
task_all = set(task_name)
tasks = len(task_all)


num = 0
for i in task_all:
	with open(r'D:/log/log.2019-5-12', 'r') as f1:
		for j in f1:
			j2 = re.split(r'[:\s]', j)
			if i in j2:
				task_time.extend((j2[0], j2[1], j2[2], j2[3]))

		t1 = datetime.datetime(int(task_time[-4][0:4]), int(task_time[-4][4:6]), \
			int(task_time[-4][6:8]), int(task_time[-3]), int(task_time[-2]), int(task_time[-1]))
		t2 = datetime.datetime(int(task_time[0][0:4]), int(task_time[0][4:6]),  \
			int(task_time[0][6:8]), int(task_time[1]), int(task_time[2]), int(task_time[3]))
		time_res = (t1 - t2).seconds
		num += time_res
		task_time = []

res_avg = num / tasks
print(res_avg)
