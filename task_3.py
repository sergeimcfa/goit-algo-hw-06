import networkx as nx

def main():
    # Створюємо граф із вагами (вага = час у хвилинах)
    G = nx.Graph()
    
    # (u, v, weight)
    weighted_edges = [
        ("Хрещатик", "Майдан Незалежності", 2),
        ("Хрещатик", "Театральна", 2),
        ("Хрещатик", "Арсенальна", 3),
        ("Театральна", "Золоті Ворота", 1),
        ("Театральна", "Університет", 2),
        ("Золоті Ворота", "Палац Спорту", 3),
        ("Золоті Ворота", "Лук'янівська", 4),
        ("Майдан Незалежності", "Поштова Площа", 2),
        ("Майдан Незалежності", "Площа Українських Героїв", 2),
        ("Площа Українських Героїв", "Палац Спорту", 1),
        ("Площа Українських Героїв", "Олімпійська", 2),
        ("Палац Спорту", "Кловська", 3),
        ("Кловська", "Печерська", 2),
        ("Печерська", "Дружби Народів", 3)
    ]
    
    G.add_weighted_edges_from(weighted_edges)

    start_node = "Університет"

    print(f"--- Найкоротші шляхи від станції '{start_node}' (алгоритм Дейкстри) ---\n")

    # Знаходимо найкоротші шляхи до всіх інших вершин
    # shortest_paths повертає словник {цільова_вершина: [шлях]}
    shortest_paths = nx.single_source_dijkstra_path(G, source=start_node, weight='weight')
    
    # Знаходимо довжини цих шляхів
    # shortest_path_lengths повертає словник {цільова_вершина: довжина}
    shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source=start_node, weight='weight')

    # Виводимо результати гарно
    for target in shortest_paths:
        if target != start_node:
            path = shortest_paths[target]
            length = shortest_path_lengths[target]
            print(f"До '{target}':")
            print(f"  Маршрут: {path}")
            print(f"  Час: {length} хв\n")

if __name__ == "__main__":
    main()
