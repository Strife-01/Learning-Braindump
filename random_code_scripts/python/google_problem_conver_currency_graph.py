def main():
    print(convert_currency([["USD", "JPY", 110], ["USD", "AUD", 1.45], ["JPY", "GBP", 0.0070]], "GBP", "AUD"))


def convert_currency(conversion_rates, start_curr, end_curr):
    output = 1
    # dictionary of indexes:currencies
    indexes = {}
    index = 0
    nr_currencies = 0
    
    for conversion_rate in conversion_rates:
        for i in range(2):
            if conversion_rate[i] not in indexes.values():
                indexes[index] = conversion_rate[i]
                index += 1
    
    for k,v in indexes.items():
        print(k, v)

    nr_currencies = index
    graph_matrix = []
    for _ in range(nr_currencies):
        tmp = []
        for __ in range(nr_currencies):
            tmp.append(0)
        graph_matrix.append(tmp)

    for conv in conversion_rates:
        index_1 = -1
        index_2 = -1
        for k, v in indexes.items():
            if v == conv[0]:
                index_1 = k
            if v == conv[1]:
                index_2 = k
        if index_1 != -1 and index_2 != -1:
            graph_matrix[index_1][index_2] = 1
            graph_matrix[index_2][index_1] = 1
    
    start = -1
    end = -1
    for k, v in indexes.items():
        if v == start_curr:
            start = k
        elif v == end_curr:
            end = end_curr
        if start != -1 and end != -1:
            break

    visited = []
    road = []
    parse(start, end, visited, graph_matrix, road)

    print(road)

    for i in range(len(road) - 1):
        for rate in conversion_rates:
            if rate[0] == indexes[road[i]] and rate[1] == indexes[road[i + 1]]:
                output = output * rate[2]
            elif rate[1] == indexes[road[i]] and rate[0] == indexes[road[i + 1]]:
                output = output / rate[2]

    for arr in graph_matrix:
        print(arr)

    return output


def parse(start, end, visited, graph_matrix, road):
    if start == end:
        road.append(end)
        return
    else:
        visited.append(start)
        road.append(start)
        for i in range(len(graph_matrix)):
            if i not in visited and graph_matrix[start][i] == 1:
                parse(i, end, visited, graph_matrix, road)


if __name__ == "__main__":
    main()
