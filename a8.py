from collections import deque

def bfs(adj_list, start):
    visited = set()
    queue = deque([start])
    print("\nBFS Traversal starting from", start, ":", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def dfs(matrix, start_index, labels, visited):
    print(labels[start_index], end=" ")
    visited[start_index] = True
    for j in range(len(matrix)):
        if matrix[start_index][j] == 1 and not visited[j]:
            dfs(matrix, j, labels, visited)

if __name__ == "__main__":
    locations = ['A', 'B', 'C', 'D', 'E']
    adj_list = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['B', 'C']
    }
    adj_matrix = [
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0]
    ]
    start_node = 'A'
    bfs(adj_list, start_node)
    print("\nDFS Traversal starting from", start_node, ":", end=" ")
    visited_nodes = [False] * len(locations)
    dfs(adj_matrix, locations.index(start_node), locations, visited_nodes)
    print("\n")
