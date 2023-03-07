file = "grafo.txt"
with open(file, 'r') as f:
    lines = f.readlines()

dic = {}
for line in lines:
    line = line.strip().split(" ")
    head, tail = line[0], line[1:]
    # print(f"key: {head} => value: {tail}")
    dic[head] = tail

# export this function and use it in another module
def get_neighbors(node):
    return dic[node]

if __name__ == "__main__":
    print(get_neighbors("A"))
