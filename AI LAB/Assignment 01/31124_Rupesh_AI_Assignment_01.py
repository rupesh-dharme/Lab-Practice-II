# Implementation of Graph data structure
class Graph:
    def __init__(self):
        self.graph = {} # Dictionary to store adjecency list representation

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def print_graph(self):
        for key in sorted(list(self.graph.keys())):
            print(key, '->', self.graph[key])

    def bfs(self, start):
        visited = [] # visited nodes
        queue = [start] # FIFO Data structure
        while queue:
            vertex = queue.pop(0) # Visiting queue from front
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(self.graph[vertex])
        return visited

    def dfs(self, start):
        visited = [] # visited nodes
        stack = [start] # LIFO data structure
        while stack:
            vertex = stack.pop() # Last element 
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(self.graph[vertex]) # Adding adjecent to stack
        return visited

    def recursive_search(self, start, visited): # Recursive DFS helper
        visited.append(start)
        for vertex in self.graph[start]:
            if vertex not in visited:
                self.recursive_search(vertex, visited) # Recursively calling adjecent nodes
        return visited
    
    def dfs_recursive(self, start): # DFS recursive
        return self.recursive_search(start, [])


def create_graph():
    g = Graph() # Instance of Graph

    prompt = "Enter the number of vertices: "
    n = int(input(prompt))
    for _ in range(n): # loop to add vertices
        prompt = "Enter the vertex: "
        vertex = input(prompt)
        g.add_vertex(vertex)

    prompt = "Enter the number of edges: "
    m = int(input(prompt))
    for _ in range(m): # loop to add edges
        prompt = "Enter the edge: "
        edge = input(prompt)
        edge = edge.split(' ')
        g.add_edge(edge[0], edge[1])
    return g


if __name__ == '__main__':
    while True:
        g = create_graph()
        while True:
            choice = input("Enter the choice:\n 1. BFS\n 2. DFS\n 3. Recursive DFS\n 4. clear\n 5. exit\n")
            if choice == '1':
                start = input("Enter the start vertex: ")
                print(g.bfs(start))
            elif choice == '2':
                start = input("Enter the start vertex: ")
                print(g.dfs(start))
            elif choice == '3':
                start = input("Enter the start vertex: ")
                print(g.dfs_recursive(start))
            elif choice == '4':
                g.graph.clear()
                break
            elif choice == '5':
                break
        if choice == '5':
            print('Thank you')
            break