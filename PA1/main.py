#!/usr/bin/python3

import sys
from algorithm import find_shortest_cycle
from fileprocess import parse_file

if len(sys.argv) != 3 or sys.argv[1] != "--input":
    print("Usage: python main.py --input input_graph_file")
    exit(1)

file = sys.argv[2]
graph = parse_file(file)
shortest_cycle_length = find_shortest_cycle(graph)
print(f"The length of the shortest cycle is: {shortest_cycle_length}")
