import tkinter as tk
from PIL import Image, ImageTk
from data import getCampusMap, getEdges, getHelpCoords, getIntersectionNodes
import networkx as nx
import heapq


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
        # Draw nodes on canvas
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")

    for node, (x, y, display) in mergedMap.items():
        G.add_node(node, pos=(x, y))
        if display:
            canvas.create_oval(x-10, y-10, x+10, y+10, fill="red")
        #else:
        #    canvas.create_oval(x-7, y-7, x+7, y+7, fill="pink")

    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)
        x1, y1, _ = mergedMap[u]
        x2, y2, _ = mergedMap[v]
        edge_tag = f"{u}_{v}"
        line_id = canvas.create_line(x1, y1, x2, y2, fill="blue", width=5, tags=edge_tag)

        # Bind click event to each edge to toggle its state
        canvas.tag_bind(line_id, "<Button-1>", lambda event,
                        u=u, v=v: toggle_edge(u, v))

    def highlight_node(node, color="yellow"):
        x, y = G.nodes[node]["pos"]
        canvas.create_oval(x-5, y-5, x+5, y+5, fill=color, tags=node)


    def highlight_edge(u, v, color="red"):
        x1, y1 = G.nodes[u]["pos"]
        x2, y2 = G.nodes[v]["pos"]
        line_tag = f"{u}_{v}"
        canvas.create_line(x1, y1, x2, y2, fill=color, width=3, tags=line_tag)

    def reset_graph():
        for edge in G.edges():
            highlight_edge(*edge, "blue")
    
    def toggle_edge(u, v):
        print(f"Toggle edge: {u} -> {v}")
        edge_tag = f"{u}_{v}"
        if G.has_edge(u, v):
            # Disable the edge: remove it from the graph and visually gray it out
            G.remove_edge(u, v)
            canvas.itemconfig(edge_tag, fill="lightgray", dash=(4, 2), width=7)
        else:
            # Enable the edge: add it back to the graph and color it
            G.add_edge(u, v, weight=1)  # Specify the original weight if needed
            canvas.itemconfig(edge_tag, fill="blue", dash=(),
                              width=7)  # Remove dashes


    def custom_bfs(graph, start, target):
        print(graph)
        queue = [(start, [start])]
        visited = set()

        def step():
            if queue:
                current_node, path = queue.pop(0)
                if current_node in visited:
                    canvas.after(500, step)
                    return

                visited.add(current_node)
                #highlight_node(current_node, "yellow")  # Visual highlight

                if current_node == target:
                    for i in range(len(path) - 1):
                        highlight_edge(path[i], path[i + 1], "green")
                    return

                for neighbor in graph.neighbors(current_node):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
                        highlight_edge(current_node, neighbor, "red")

                canvas.after(500, step)

        step()

    def custom_dfs(graph, start, target):
        stack = [(start, [start])]
        visited = set()

        def step():
            if stack:
                current_node, path = stack.pop()
                if current_node in visited:
                    canvas.after(500, step)
                    return

                visited.add(current_node)
                #highlight_node(current_node, "yellow")

                if current_node == target:
                    for i in range(len(path) - 1):
                        highlight_edge(path[i], path[i + 1], "green")
                    return

                for neighbor in graph.neighbors(current_node):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
                        highlight_edge(current_node, neighbor, "red")

                canvas.after(500, step)

        step()

    def custom_dijkstra(graph, start, target):
        queue = [(0, start, [start])]
        distances = {node: float('inf') for node in graph.nodes()}
        distances[start] = 0
        visited = set()

        def step():
            if queue:
                current_dist, current_node, path = heapq.heappop(queue)
                if current_node in visited:
                    canvas.after(500, step)
                    return

                visited.add(current_node)
                highlight_node(current_node, "yellow")

                if current_node == target:
                    for i in range(len(path) - 1):
                        highlight_edge(path[i], path[i + 1], "green")
                    return

                for neighbor in graph.neighbors(current_node):
                    edge_weight = graph.edges[current_node, neighbor]['weight']
                    distance = current_dist + edge_weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(
                            queue, (distance, neighbor, path + [neighbor]))
                        highlight_edge(current_node, neighbor, "red")

                canvas.after(500, step)

        step()

    tk.Button(root, text="BFS", command=lambda: custom_bfs(
        G, "Titan Student Union", "Humanities Building")).place(x=0, y=0)
    
    tk.Button(root, text="DFS", command=lambda: custom_dfs(
        G, "Titan Student Union", "Humanities Building")).place(x=0, y=30)
    
    tk.Button(root, text="Dijkstra", command=lambda: custom_dijkstra(
        G, "Titan Student Union", "Humanities Building")).place(x=0, y=60)
    
    tk.Button(root, text="Reset", command=reset_graph).place(x=0, y=90)

    root.mainloop()


if __name__ == "__main__":
    main()
