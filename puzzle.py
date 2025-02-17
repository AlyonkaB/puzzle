def graph_dict(sequence_number: list[int]):
    graph = {}
    for number in sequence_number:
        str_number = str(number)
        start, end = str_number[:2], str_number[-2:]

        if start not in graph:
            graph[start] = []
        graph[start].append((number, end))
    return graph


def dfs(graph, current, visited, path, max_path):
    visited.add(current)
    path.append(current)

    if len(path) > len(max_path[0]):
        max_path[0] = path.copy()

    last_two = str(current)[-2:]
    for neighbor, _ in graph.get(last_two, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path, max_path)

    path.pop()
    visited.remove(current)


def find_longest_sequence():
    with open("source.txt") as f:
        numbers = [int(number) for number in f.read().split()]

        graph = graph_dict(numbers)
        max_path = [[]]

        for number in numbers:
            dfs(graph, number, set(), [], max_path)

        if not max_path[0]:
            return ""

        result = str(max_path[0][0])
        for i in range(1, len(max_path[0])):
            num_str = str(max_path[0][i])
            result += num_str[2:]
        print (len(max_path[0]))
        return result


if __name__ == "__main__":
    print(find_longest_sequence())