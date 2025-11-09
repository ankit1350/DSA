# ---- Pizza Delivery Shortest Time using Dijkstra (No heapq) ----

graph = {}  # adjacency list with time

def add_location(loc):
    if loc not in graph:
        graph[loc] = []
        print("Location", loc, "added.")
    else:
        print("Location already exists.")

def add_route(u, v, t):
    t = int(t)
    if u in graph and v in graph:
        graph[u].append([v, t])
        graph[v].append([u, t])
        print("Route added between", u, "and", v, "with time", t)
    else:
        print("Add both locations first!")

def display_graph():
    print("\nGraph (Adjacency List with Time):")
    for node in graph:
        print(node, "→", graph[node])

# ---- Manual Dijkstra (no heapq, no set) ----
def dijkstra(start):
    visited = []
    dist = {}
    for node in graph:
        dist[node] = 999999  # infinity
    dist[start] = 0

    while len(visited) < len(graph):
        # Find node with smallest distance not yet visited
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or dist[node] < dist[min_node]:
                    min_node = node

        # Update distances for neighbours
        for neighbour, time in graph[min_node]:
            new_dist = dist[min_node] + time
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist

        visited.append(min_node)

    print("\nMinimum Delivery Time from", start)
    for node in dist:
        print(f"{start} → {node} : {dist[node]} mins")

# ---- Menu ----
while True:
    print("\n--- PIZZA DELIVERY MENU ---")
    print("1. Add Location")
    print("2. Add Route with Time")
    print("3. Display Graph")
    print("4. Find Minimum Delivery Time")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        loc = input("Enter location name: ").upper()
        add_location(loc)
    elif ch == '2':
        u = input("Enter first location: ").upper()
        v = input("Enter second location: ").upper()
        t = input("Enter time between them: ")
        add_route(u, v, t)
    elif ch == '3':
        display_graph()
    elif ch == '4':
        if len(graph) == 0:
            print("No locations added!")
        else:
            start = input("Enter starting location (Pizza Shop): ").upper()
            if start in graph:
                dijkstra(start)
            else:
                print("Invalid starting location!")
    elif ch == '5':
        print("Exiting program... 🍕")
        break
    else:
        print("Invalid choice! Please try again.")
