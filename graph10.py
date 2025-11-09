# ---- Graph Traversal using BFS and DFS ----
# ---- Simple Exam-Safe Menu-Driven Program ----

graph = {}   # adjacency list

# Function to add edge (connection)
def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

# ---- DFS using manual stack ----
def dfs(start):
    visited = []
    stack = [start]
    print("\nDFS Traversal:")
    while len(stack) > 0:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            # push neighbors in reverse to maintain order
            for neighbour in graph[node][::-1]:
                if neighbour not in visited:
                    stack.append(neighbour)
    print()

# ---- BFS using manual queue ----
def bfs(start):
    visited = []
    queue = [start]
    visited.append(start)
    print("\nBFS Traversal:")
    while len(queue) > 0:
        node = queue[0]
        print(node, end=' ')
        queue = queue[1:]   # manually remove first element
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()

# ---- Menu ----
while True:
    print("\n--- GRAPH TRAVERSAL MENU ---")
    print("1. Add Connection (Edge)")
    print("2. Display Graph")
    print("3. Perform DFS")
    print("4. Perform BFS")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        u = input("Enter first location: ").upper()
        v = input("Enter second location: ").upper()
        add_edge(u, v)
        print("Connection added between", u, "and", v)
    elif ch == '2':
        print("\nGraph (Adjacency List):")
        for node in graph:
            print(node, "→", graph[node])
    elif ch == '3':
        if len(graph) == 0:
            print("Graph is empty!")
        else:
            start = input("Enter starting location: ").upper()
            if start in graph:
                dfs(start)
            else:
                print("Invalid location!")
    elif ch == '4':
        if len(graph) == 0:
            print("Graph is empty!")
        else:
            start = input("Enter starting location: ").upper()
            if start in graph:
                bfs(start)
            else:
                print("Invalid location!")
    elif ch == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
