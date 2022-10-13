#BFS in a graph

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		self.distance = -1
		self.color = 'black'

	def addNeighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	
	def addVertex(self, vertex):
		if isinstace(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True

		else:
			return False

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for k, v in self.vertices.items():
				if k == u:
					v.add_neighbor(v)
      				if k == v:
					v.add_neighbor(u)
			return True
		else:
			return False

	def print_graph(self):
		for k in sorted(list(self.vertices.keys())):
			print(k + str(self.vertices[k].neighbors) + " "
				str(self.vertices[k].distance)

	def breadthFirstSearch(self, vert):
		q = list() # q = []
		vert.distance = 0
		vert.color = 'red'
		
		for v in vert.neighbors:
			self.vertices[v].distance = vert.distance + 1
			q.append(v)

		while len(q) > 0:
			u = q.pop(0)
			node_u = self.vertices[u]
			node_u.color = 'red'

			for v in node_u.neighbors:
				node_v = self.vertices[v]
				if node_v.color == 'black':
					q.append(v)
					if node_v.distance > node_u.distance + 1:
						node_v.distance = node_u.distance + 1



