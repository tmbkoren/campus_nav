import tkinter as tk
from PIL import Image, ImageTk
from data import getCampusMap
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
    nodes = {"A": (100, 100), "B": (200, 200), "C": (300, 150), "D": (1000, 1000)}
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("A", "C"), ("A", "D")]

    # Add nodes and edges to NetworkX graph
    for node, (x, y) in nodes.items():
        G.add_node(node, pos=(x, y))
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")  # Draw nodes on canvas

    for edge in edges:
        G.add_edge(*edge)
        x1, y1 = nodes[edge[0]]
        x2, y2 = nodes[edge[1]]
        line = canvas.create_line(x1, y1, x2, y2, fill="gray")

    # Pathfinding with visualization
    def find_path():
        path = nx.shortest_path(G, source="A", target="D")  # Example path
        for i in range(len(path)-1):
            node1, node2 = path[i], path[i+1]
            x1, y1 = nodes[node1]
            x2, y2 = nodes[node2]
            canvas.create_line(x1, y1, x2, y2, fill="red",
                            width=2)  # Highlight path

    # Trigger pathfinding
    #find_path()

    runBtn = tk.Button(root, text="Find Path", command=find_path, bg="blue", fg="white", font=("Arial", 12)).place(x=10, y=10)

    root.mainloop()

if __name__ == "__main__":
    main()