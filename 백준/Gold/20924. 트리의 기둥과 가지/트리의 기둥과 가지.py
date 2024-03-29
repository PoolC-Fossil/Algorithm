import sys
sys.setrecursionlimit(10**6)
n, root = map(int, input().split())
graph = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
vi = set()
branch = [0] * (n+1)
giga = -1
def make_tree(idx, val):
    vi.add(idx)
    for ch in graph[idx]:
        if ch[0] in vi:
            tree[ch[0]].append(idx)
            continue
        make_tree(ch[0], val + ch[1])
    branch[idx] = val    
def find_giga(idx):
    if len(tree[idx]) >= 2:
        return idx
    for ch in tree[idx]:
        return find_giga(ch)
    return idx
make_tree(root, 0)
giga = find_giga(root)
print(branch[giga], max(branch)-branch[giga])