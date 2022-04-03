input = open("data.in")
output = open("data.out", "w")


def wordAcceptance(transition, s, f, word):
    global path
    node = s

    for letter in word:
        if (node, letter) in transition:
            node = transition[(node, letter)]
            path.append(node)
        else:
            return "rejected"

    if node in f:
        return path

    return "rejected"


txt = input.read().splitlines()
aux = txt[0].split()

n = int(aux[0])
m = int(aux[1])
transition = {}

for index in range(1, m + 1):
    aux = txt[index].split()
    transition[(int(aux[0]), aux[2])] = int(aux[1])

s = int(txt[m + 1])

aux = txt[m + 2].split()
nf = int(aux[0])
f = [int(x) for x in aux[1:]]

ni = int(txt[m + 3])
words = [txt[m + 4 + index] for index in range(ni)]

input.close()

for word in words:
    path = [s]
    var = wordAcceptance(transition, s, f, word)
    if var == "rejected":
        output.write(word + " is not accepted by this DFA" + "\n")
    else:
        output.write(word + " is accepted by this DFA" + "\n")
        path = [str(x) for x in path]
        output.write("path: " + " ".join(path) + "\n")

output.close()
