with open('run_of_60_m.txt') as run:
    k = run.read().splitlines()

fst_m = {}
fst_w = {}
f = open('run_of_60_mark.txt', 'w')

for i in k:
    j = i.split()
    s = float(j[3])
    if j[0] == '6':
        if j[1] == 'm':
            if s <= 9.9:
                f.write(i + ': 5\n')
                fst_m[s] = [j[0], j[2]]
            if s > 9.9 and s <= 10.4:
                f.write(i + ': 4\n')
                fst_m[s] = [j[0], j[2]]
            if s > 10.4 and s <= 11.1:
                f.write(i + ': 3\n')
                fst_m[s] = [j[0], j[2]]
            if s > 11.1:
                f.write(i + ': 2\n')
                fst_m[s] = [j[0], j[2]]
        if j[1] == 'w':
            if s <= 10.3:
                f.write(i + ': 5\n')
                fst_w[s] = [j[0], j[2]]
            if s > 10.6 and s <= 10.3:
                f.write(i + ': 4\n')
                fst_w[s] = [j[0], j[2]]
            if s > 10.3 and s <= 11.2:
                f.write(i + ': 3\n')
                fst_w[s] = [j[0], j[2]]
            if s > 11.2:
                f.write(i + ': 2\n')
                fst_w[s] = [j[0], j[2]]
    if j[0] == '7':
        if j[1] == 'm':
            if s <= 9.4:
                f.write(i + ': 5\n')
                fst_m[s] = [j[0], j[2]]
            if s > 9.4 and s <= 10.2:
                f.write(i + ': 4\n')
                fst_m[s] = [j[0], j[2]]
            if s > 10.2 and s <= 11.0:
                f.write(i + ': 3\n')
                fst_m[s] = [j[0], j[2]]
            if s > 11.0:
                f.write(i + ': 2\n')
                fst_m[s] = [j[0], j[2]]
        if j[1] == 'w':
            if s <= 9.8:
                f.write(i + ': 5\n')
                fst_w[s] = [j[0], j[2]]
            if s > 9.8 and s <= 10.6:
                f.write(i + ': 4\n')
                fst_w[s] = [j[0], j[2]]
            if s > 10.6 and s <= 11.4:
                f.write(i + ': 3\n')
                fst_w[s] = [j[0], j[2]]
            if s > 11.4:
                f.write(i + ': 2\n')
                fst_w[s] = [j[0], j[2]]
print(max(fst_m.keys()),'секунд:', ' класс, '.join(fst_m.get(max(fst_m.keys()))))
print(max(fst_w.keys()),'секунд:', ' класс, '.join(fst_w.get(max(fst_w.keys()))))
f.close()
