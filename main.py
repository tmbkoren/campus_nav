import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from data import getCampusMap, getEdges, getHelpCoords, getIntersectionNodes
import networkx as nx
import heapq


def main():
    # Load and display the campus image as background
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack()

    campus_image = Image.open("img/campus_map_horizontal.png")
    bg_image = ImageTk.PhotoImage(campus_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

    # Create NetworkX graph for pathfinding
    G = nx.Graph()
    #helpCoords = getHelpCoords()
    campusMap = getCampusMap()
    intersection_nodes = getIntersectionNodes()

    # merging the two dictionaries
    mergedMap = dict()
    mergedMap.update(campusMap)
    mergedMap.update(intersection_nodes)
    edges = getEdges()

    # helpful grid of dots to help with node placement
    # for node, (x, y) in helpCoords.items():
    #     G.add_node(node, pos=(x, y))
    #     # Draw nodes on canvas
    #     canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")

    for node, (x, y, display) in mergedMap.items():
        G.add_node(node, pos=(x, y))
        if display:
            canvas.create_oval(x-10, y-10, x+10, y+10, fill="red")
        # displaying intersection nodes
        # else:
        #     canvas.create_oval(x-7, y-7, x+7, y+7, fill="pink")

    edge_ids = {}
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)
        x1, y1, _ = mergedMap[u]
        x2, y2, _ = mergedMap[v]
        edge_tag = f"{u}_{v}"
        edge_id = canvas.create_line(
            x1, y1, x2, y2, fill="blue", width=5, tags=(edge_tag))
        edge_ids[(u, v)] = edge_id

        # Bind click event to each edge to toggle its state
        canvas.tag_bind(edge_id, "<Button-1>", lambda event,
                        u=u, v=v: toggle_edge(u, v))

    # def highlight_node(node, color="yellow"):
    #     x, y = G.nodes[node]["pos"]
    #     canvas.create_oval(x-5, y-5, x+5, y+5, fill=color, tags=node)

    # def highlight_edge(u, v, color = "red"):
    #     """Highlight an edge between two nodes with a specific color."""
    #     # edge_id = edge_ids.get((u, v))
    #     # if edge_id is not None:
    #     #     canvas.itemconfig(edge_id, fill=color)
    #     edge_id = edge_ids.get((u, v)) or edge_ids.get(
    #         (v, u))  # Check both directions
    #     if edge_id is not None:
    #         canvas.itemconfig(edge_id, fill=color)

    def highlight_path(path, color="green"):
        """Highlight the edges in the current path with the specified color."""
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            edge_id = edge_ids.get((u, v)) or edge_ids.get(
                (v, u))
            if edge_id is not None:
                canvas.itemconfig(edge_id, fill=color)

    def reset_graph():
        for edge_id in edge_ids.values():
            canvas.itemconfig(edge_id, fill="blue", width=5)

    def toggle_edge(u, v):
        print(f"Toggle edge: {u} -> {v}")
        edge_tag = f"{u}_{v}"
        print(f"TAG: '{edge_tag}'")
        if G.has_edge(u, v):
            # Disable the edge: remove it from the graph and visually gray it out
            print("Removing edge", u, v)
            G.remove_edge(u, v)
            canvas.itemconfig(edge_tag, dash=(4, 2))
        else:
            # Enable the edge: add it back to the graph and color it
            G.add_edge(u, v, weight=1)  # Specify the original weight if needed
            canvas.itemconfig(edge_tag, dash=())  # Remove dashes

    def custom_bfs(graph, start, target):
        disalbeButtons()
        queue = [(start, [start])]
        visited = set()

        def step():
            reset_graph()
            if queue:
                current_node, path = queue.pop(0)
                if current_node in visited:
                    canvas.after(300, step)
                    return

                visited.add(current_node)
                highlight_path(path, "yellow")

                if current_node == target:
                    highlight_path(path, "green")
                    enableButtons()
                    # distance = sum(edge[2] for edge in path)
                    # messagebox.showinfo("Done", f"Done. Distance: {distance}")
                    messagebox.showinfo("Done", f"Done")
                    return path

                for neighbor in graph.neighbors(current_node):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

                canvas.after(300, step)

        step()

    def custom_dfs(graph, start, target):
        stack = [(start, [start])]
        disalbeButtons()
        visited = set()

        def step():
            reset_graph()
            if stack:
                current_node, path = stack.pop()
                if current_node in visited:
                    canvas.after(300, step)
                    return

                visited.add(current_node)
                highlight_path(path, "yellow")

                if current_node == target:
                    highlight_path(path, "green")
                    enableButtons()
                    # distance = sum(edge[2] for edge in path)
                    # messagebox.showinfo("Done", f"Done. Distance: {distance}")
                    messagebox.showinfo("Done", f"Done")
                    return

                for neighbor in graph.neighbors(current_node):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

                canvas.after(300, step)

        step()

    def custom_dijkstra(graph, start, target):
        disalbeButtons()
        queue = [(0, start, [start])]
        distances = {node: float('inf') for node in graph.nodes()}
        distances[start] = 0
        visited = set()

        def step():
            reset_graph()
            if queue:
                current_dist, current_node, path = heapq.heappop(queue)
                if current_node in visited:
                    canvas.after(300, step)
                    return

                visited.add(current_node)
                # highlight_node(current_node, "yellow")

                if current_node == target:
                    highlight_path(path, "green")
                    enableButtons()
                    # distance = sum(edge[2] for edge in path)
                    #messagebox.showinfo("Done", f"Done. Distance: {distance}")
                    messagebox.showinfo("Done", f"Done. Distance: {current_dist}")
                    return

                for neighbor in graph.neighbors(current_node):
                    edge_weight = graph.edges[current_node, neighbor]['weight']
                    distance = current_dist + edge_weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(
                            queue, (distance, neighbor, path + [neighbor]))
                        highlight_path(path + [neighbor], "yellow")

                canvas.after(300, step)

        step()

    def startBfs():
        start = startNode.get()
        end = endNode.get()
        if start == "" or end == "" or start==end:
            messagebox.showerror("Error", "Invalid choice")
            return
        custom_bfs(G, startNode.get(), endNode.get())

    def startDfs():
        start = startNode.get()
        end = endNode.get()
        if start == "" or end == "" or start == end:
            messagebox.showerror("Error", "Invalid choice")
            return
        custom_dfs(G, startNode.get(), endNode.get())

    def startDijkstra():
        start = startNode.get()
        end = endNode.get()
        if start == "" or end == "" or start == end:
            messagebox.showerror("Error", "Invalid choice")
            return
        custom_dijkstra(G, startNode.get(), endNode.get())

    
    bfsBtn = tk.Button(root, text="BFS", command=startBfs)
    bfsBtn.place(x=1281, y=0)

    dfsBtn = tk.Button(root, text="DFS", command=startDfs)
    dfsBtn.place(x=1281, y=30)

    dijBtn = tk.Button(root, text="Dijkstra", command=startDijkstra)
    dijBtn.place(x=1281, y=60)

    resetBtn = tk.Button(root, text="Reset", command=reset_graph)
    resetBtn.place(x=1281, y=90)

    def disalbeButtons():
        bfsBtn.config(state="disabled")
        dfsBtn.config(state="disabled")
        dijBtn.config(state="disabled")
        resetBtn.config(state="disabled")

    def enableButtons():
        bfsBtn.config(state="normal")
        dfsBtn.config(state="normal")
        dijBtn.config(state="normal")
        resetBtn.config(state="normal")

    comboValues = list(campusMap.keys())

    tk.Label(root, text="Start node: ").place(x=0, y=850)
    startNode = ttk.Combobox(root, values=comboValues)
    startNode.place(x=100, y=850)
    tk.Label(root, text="End node: ").place(x=400, y=850)
    endNode = ttk.Combobox(root, values=comboValues)
    endNode.place(x=500, y=850)

    root.mainloop()


if __name__ == "__main__":
    main()
