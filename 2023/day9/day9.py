# https://adventofcode.com/2023/day/9

input_list = [e.replace('\n', '').split(' ') for e in open('input.txt', 'r')]
input_list = [[int(e) for e in x] for x in input_list]
sequences = input_list.copy()


def workable(liste):
	"""
	Return True if all elements are ints and equals.
	Used to go to the second last subsequence of the list
	"""
	return all(isinstance(liste[i], int) for i in range(len(liste))) and all(
		liste[i + 1] == liste[i] for i in range(len(liste) - 1))


# Part 1 : Get the next number in each sequence
subsequences = [[].copy() for _ in range(len(sequences))]
for i in range(len(sequences)):
	while not workable(sequences[i]):
		sequences[i] = [sequences[i][j + 1] - sequences[i][j] for j in range(len(sequences[i]) - 1)]
		subsequences[i].append(sequences[i])

for i in range(len(subsequences)):
	for j in range(len(subsequences[i])):
		input_list[i][-1] += subsequences[i][j][-1]

# Part 2 : Get the previous number in each sequence
subequences_rev = []
for i in range(len(subsequences)):
	subequences_rev.append(subsequences[i][::-1])
	for j in range(1, len(subequences_rev[i])):
		subequences_rev[i][j].insert(0, subequences_rev[i][j][0] - subequences_rev[i][j - 1][0])
	subequences_rev[i] = subequences_rev[i][::-1]

for i in range(len(subsequences)):
	input_list[i].insert(0, input_list[i][0] - subequences_rev[i][0][0])

print("start 1 :", sum(x[-1] for x in input_list))
print("start 2 :", sum([e[0] for e in input_list]))
