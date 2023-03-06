name = input("Enter File:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
hours = list()
counts = dict()
for line in handle:
    line = line.split()
    if len(line) < 1 or line[0] != 'From' :
        continue
    time = line[5].split(':')
    #print(time)
    hours.append(time[0])
    #print(hours)
for hour in hours :
    counts[hour] = counts.get(hour,0) + 1
    #print(counts)
for k,v in sorted(counts.items()):
    print(k,v)