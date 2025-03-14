from collections import defaultdict
def parse_file(path):
    """
    Parses input file in to a directed graph [an adjacency list].
    all nodes and distances should be int.

    format:
    v1 : dest1 wt11 dest2 wt12 
    eg:
    0: 1 1 2 4
    """
    graph = defaultdict(list)
    try:
        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if not parts[0] or parts[0][0] == "#": # ignore empty line and line start with # 
                    continue
                if len(parts) != 2:
                    raise ValueError(f"Invalid line format: {line.strip()}")
                source = parts[0].strip()
                if not source.isdigit():
                    raise ValueError(f"Invalid vertex name: {source}")
                
                source = int(source)
                edges = parts[1].strip().split()

                if len(edges) % 2 != 0:
                    raise ValueError(f"Invalid edge format in line: {line.strip()}")
                for i in range(0, len(edges), 2):
                    dest, weight = edges[i], edges[i + 1]
                    if not dest.isdigit() or not weight.isdigit() or int(weight) <= 0:
                        raise ValueError(f"Invalid edge data: {edges[i]} {edges[i + 1]}")
                    graph[source].append((int(dest), int(weight)))
        if not graph:
            raise ValueError("Empty Graph")
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        exit(1)
    except ValueError as e:
        print(f"Error in input file: {e}")
        exit(1)
    except Exception as e:
        print(f"Error Unexpected: {e}")
        exit(1)
    return graph