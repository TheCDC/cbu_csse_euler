from collections import Counter

def map_from_lines(all_lines) -> dict: 
	m = dict()
	for line in all_lines.split("\n"):
		for i in line:
			m[i] = m.get(i, set()) | set(line.split(i)[1])
	return m

def counters_from_dict(dictionary) -> Counter:
	ins = Counter()
	outs = Counter()
	for k, v in dictionary.items():
		outs[k] += len(v)
	return outs

def main():
	with open("p079_keylog.txt") as f:
		content = f.read()
		m = map_from_lines(content)
		outs = counters_from_dict(m)
		print(outs.most_common()[0])

if __name__ == "__main__":
	main()