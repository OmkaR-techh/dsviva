# ---------- DFS using adjacency matrix ----------
def create_matrix_graph(V):
    adj = []
    for i in range(V):
        adj.append([0] * V)
    return adj

def add_edge_matrix(adj, u, v):
    adj[u][v] = 1
    adj[v][u] = 1

def print_matrix(adj):
    print("\nAdjacency Matrix Representation (0 = no edge, 1 = edge):")
    print("   ", end="")
    for j in range(len(adj)):
        print(chr(j + 65), end=" ")
    print()
    for i in range(len(adj)):
        print(chr(i + 65), end=": ")
        for j in range(len(adj)):
            print(adj[i][j], end=" ")
        print()

def dfs_util(adj, u, visited):
    visited[u] = True
    print(chr(u + 65), end=" ")
    for v in range(len(adj)):
        if adj[u][v] == 1 and not visited[v]:
            dfs_util(adj, v, visited)

def dfs(adj, start):
    visited = [False] * len(adj)
    print("\nDFS Traversal (Adjacency Matrix): ", end="")
    dfs_util(adj, start, visited)
    print()


# ---------- BFS using adjacency list ----------
def create_list_graph(V):
    adj = []
    for i in range(V):
        adj.append([])
    return adj

def add_edge_list(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def print_list(adj):
    print("\nAdjacency List Representation:")
    for i in range(len(adj)):
        print(chr(i + 65), ":", end=" ")
        for v in adj[i]:
            print(chr(v + 65), end=" ")
        print()

def bfs(adj, start):
    visited = [False] * len(adj)
    queue = []
    queue.append(start)
    visited[start] = True
    print("\nBFS Traversal (Adjacency List): ", end="")
    while queue:
        u = queue.pop(0)
        print(chr(u + 65), end=" ")
        for v in adj[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
    print()


# ---------- Main ----------
V = 5
matrix_graph = create_matrix_graph(V)
list_graph = create_list_graph(V)

add_edge_matrix(matrix_graph, 0, 1)
add_edge_matrix(matrix_graph, 1, 2)
add_edge_matrix(matrix_graph, 1, 3)
add_edge_matrix(matrix_graph, 2, 3)
add_edge_matrix(matrix_graph, 2, 4)

add_edge_list(list_graph, 0, 1)
add_edge_list(list_graph, 1, 2)
add_edge_list(list_graph, 1, 3)
add_edge_list(list_graph, 2, 3)
add_edge_list(list_graph, 2, 4)

print("Consider the area with locations:\nA - Bus Stop\nB - College\nC - Garden\nD - Hospital\nE - Mall")

print_matrix(matrix_graph)
dfs(matrix_graph, 0)

print_list(list_graph)
bfs(list_graph, 0)
