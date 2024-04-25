# Importing libraries
import random
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time

# Defining the class to represent the city
class City:
    def __init__(self):
        self.vertices = {}  # Dictionary to store vertices (streets)
        self.edges = {}     # Dictionary to store edges (roads)
    #To add a street to the city
    def addStreet(self, streetName):
        if streetName not in self.vertices:
            self.vertices[streetName] = []
    #To add a road connecting two streets
    def addRoad(self, roadID, source, destination, length):
        if source not in self.vertices:
            self.addStreet(source)
        if destination not in self.vertices:
            self.addStreet(destination)
        self.edges[roadID] = (source, destination, length)
        self.vertices[source].append((destination, length))  # Directed graph
    #To find the shortest path between two streets using Dijkstra's algorithm
    def dijkstra(self, start, end):
        startTime = time.time()
        pq = [(0, start)] # Priority queue
        visited = set() #keeping track of visited vertices
        distances = {v: float('inf') for v in self.vertices} #To store distances 
        distances[start] = 0 # Distance from source to itself is 0
        path = {start: []} # Dictionary to store shortest path
        # Dijkstra's algorithm
        while pq:
            dist, node = heapq.heappop(pq) # Pop the vertex with the smallest distance
            if node == end:
                pathStr = "->".join(path[node] + [node])
                endTime = time.time()
                return distances[end], pathStr, endTime - startTime # Return shortest distance, path, and time taken
            if node in visited:
                continue
            visited.add(node)
            for neighbor, length in self.vertices[node]:
                if neighbor not in visited:
                    newDist = dist + length
                    if newDist < distances[neighbor]:
                        distances[neighbor] = newDist
                        heapq.heappush(pq, (newDist, neighbor)) # Push neighbor into priority queue
                        path[neighbor] = path[node] + [node] # Update shortest path

        endTime = time.time()
        return float('inf'), None, endTime - startTime # Return infinity distance if no path found

# Function to generate a random connected graph with the first 30 street names
def generateGraphWithStreetNames():
    city = City()
    streetNames = """
    Abdullah Omran Taryam Street
    Al 'Oud Street
    Al Ba' Street
    Al Bajada Street
    Al Baqat Street
    Al Bashiq Street
    Al Bayhaqi Street
    Al Bayyin Street
    Al Bazigh Street
    Al Bazighah Street
    Al Da'ali Street
    Al Da'oumah Street
    Al Da'thour Street
    Al Dabagh Street
    Al Dajaya Street
    Al Dajeej Street
    Al Falaq Street
    Al Fay Forest Park
    Al Faylaq Street
    Al Ghazal Street
    Al Ghiraybi Street
    Al Ghouj Street
    Al Hayf Street
    Al Jawdhar Street
    Al Makhtout Street
    Al Maqeed Street
    Al Mardas Street
    Al Maryah Street
    Al Matla'i Street
    Al Mukhadram Street
    """
    # Split street names
    streetNames = [name.strip() for name in streetNames.split("\n") if name.strip()]
    numVertices = len(streetNames)
    for i, streetName in enumerate(streetNames):
        numConnections = random.randint(2, 4)  # Random number of connections per street (2 to 4)
        for _ in range(numConnections):
            destination = random.choice(streetNames)
            if destination != streetName:
                length = random.randint(50, 150)  # Set distance between streets to range from 50 to 150
                roadId = f"Road_{i}_{destination}"
                city.addRoad(roadId, streetName, destination, length)
    return city

# Function to place houses randomly on streets
def placeHouses(city, numHouses):
    houses = []
    streetNames = list(city.vertices.keys())
    for _ in range(numHouses):
        streetName = random.choice(streetNames)
        houseId = f"House {len(houses)+1}"
        houses.append((houseId, streetName))
    return houses

if __name__ == "__main__":
    alreemCity = generateGraphWithStreetNames()
    numHouses = 6
    houses = placeHouses(alreemCity, numHouses)

    # Randomly select two houses
    house1, house2 = random.sample(houses, 2)
    houseId1, streetName1 = house1
    houseId2, streetName2 = house2

    # Calculate shortest path between the selected houses and track time taken
    shortestDistance, path, timeTaken = alreemCity.dijkstra(streetName1, streetName2)
    print(f"Shortest distance from {houseId1} to {houseId2}: {shortestDistance} units")
    print(f"Steps: {path}")
    print(f"Time taken: {timeTaken} seconds")

    # Collecting data for time complexity
    inputSizes = []  # List to store input sizes (number of streets)
    timeComplexity = []  # List to store time complexity

    for i in range(10, 100, 10):  # Varying input sizes from 10 to 90
        alreemCity = generateGraphWithStreetNames()
        numHouses = 6  # Ensure only 6 houses are placed
        houses = placeHouses(alreemCity, numHouses)

        # Calculate time taken and track input size
        shortestDistance, path, timeTaken = alreemCity.dijkstra(streetName1, streetName2)
        inputSizes.append(len(alreemCity.vertices))  # Number of streets
        timeComplexity.append(timeTaken)

    # Plotting time complexity graph
    plt.figure(figsize=(8, 6))
    plt.plot(inputSizes, timeComplexity, marker='o', label='Time Complexity')
    plt.title('Time Complexity of Dijkstra\'s Algorithm')
    plt.xlabel('Number of Streets')
    plt.ylabel('Time taken (seconds)')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Visualize the city graph with selected houses
    G = nx.DiGraph()
    for roadId, (source, destination, length) in alreemCity.edges.items():
        G.add_edge(source, destination, weight=length)

    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, seed=42)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=8, font_weight="bold", edge_color="gray", width=2, arrowsize=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), font_color='red', font_size=8)
    nx.draw_networkx_nodes(G, pos, nodelist=[house[1] for house in houses], node_size=700, node_color="#CD853F", node_shape="^")  # Draw houses with triangle shape
    for houseId, streetName in houses:
        offset = 0.05  # Offset value to adjust position
        x, y = pos[streetName]
        plt.text(x + offset, y + offset, houseId, fontsize=8, ha='center', va='center')  # Add house labels with offset
    plt.title("Alreem Island Road Network")
    plt.show()

