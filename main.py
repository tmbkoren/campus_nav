import tkinter as tk
from PIL import Image, ImageTk
from data import getCampusMap, getEdges, getHelpCoords, getIntersectionNodes
import networkx as nx

def main():
    # Load and display the campus image as background
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack()

    # Replace with your campus image path
    campus_image = Image.open("img/campus_map_horizontal.png")
    bg_image = ImageTk.PhotoImage(campus_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

    # Create NetworkX graph for pathfinding
    G = nx.Graph()

    # Sample node and edge setup
    helpCoords = getHelpCoords()
    campusMap = getCampusMap()
    intersection_nodes = getIntersectionNodes()
    mergedMap = dict()
    mergedMap.update(campusMap)
    mergedMap.update(intersection_nodes)
    edges = getEdges()

    # Add nodes and edges to NetworkX graph
    for node, (x, y) in helpCoords.items():
        G.add_node(node, pos=(x, y))
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")  # Draw nodes on canvas

    for node, (x, y, display) in mergedMap.items():
        G.add_node(node, pos=(x, y))
        if display: 
            canvas.create_oval(x-10, y-10, x+10, y+10, fill="red")
        else: 
            canvas.create_oval(x-7, y-7, x+7, y+7, fill="pink")

    edgeColors = ("red", "green", "blue")
    currentColor = 0

    for edge in edges:
        G.add_edge(*edge)
        print(edge, edgeColors[currentColor % 3])
        x1, y1, display1 = mergedMap[edge[0]]
        x2, y2, display2 = mergedMap[edge[1]]
        line = canvas.create_line(x1, y1, x2, y2, fill=edgeColors[currentColor % 3], width=3, tags=edge)  # Draw edges on canvas
        currentColor += 1

    def highlight_edge(edge):
        canvas.itemconfig(edge, fill="yellow", width=5)

    # Pathfinding with visualization
    def find_path():
        path = nx.shortest_path(
            G, source="Nutwood Parking Structure", target="Pollak Library")  # Example path
        for i in range(len(path)-1):
            node1, node2 = path[i], path[i+1]
            x1, y1, display1 = mergedMap[node1]
            x2, y2, display2 = mergedMap[node2]
            canvas.create_line(x1, y1, x2, y2, fill="red",
                            width=7)  # Highlight path

    # Trigger pathfinding
    #find_path()

    runBtn = tk.Button(root, text="Find Path", command=find_path, bg="blue", fg="white", font=("Arial", 12)).place(x=10, y=10)

    root.mainloop()

if __name__ == "__main__":
    main()