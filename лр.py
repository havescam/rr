def vertex_cover_greedy(edges):
    """
    Жадный 2-аппроксимационный алгоритм для задачи о вершинном покрытии.
    
    Args:
        edges: список пар (u, v) — рёбра графа
    
    Returns:
        tuple: (размер покрытия, список вершин покрытия)
    """
    # Создаём множество всех рёбер
    remaining_edges = set(edges)
    cover = set()
    
    while remaining_edges:
        # Выбираем произвольное ребро (u, v)
        u, v = remaining_edges.pop()
        
        # Добавляем обе вершины в покрытие
        cover.add(u)
        cover.add(v)
        
        # Удаляем все рёбра, инцидентные u или v
        remaining_edges = {
            (a, b) for a, b in remaining_edges
            if a != u and b != u and a != v and b != v
        }
    
    return len(cover), sorted(list(cover))



# Входные данные
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
    (5, 6), (6, 7), (7, 8), (8, 9), (9, 0)
]

# Запуск алгоритма
size, cover = vertex_cover_greedy(edges)

# Вывод результатов
print(f"Размер покрытия: {size}")
print(f"Вершинное покрытие: {cover}")

# Оценка коэффициента аппроксимации
# Для данного графа (цикл из 10 вершин) оптимальное покрытие имеет размер 5
optimal_size = 5
approx_ratio = size / optimal_size
print(f"Коэффициент аппроксимации: {approx_ratio:.2f}")

Результат работы:

Размер покрытия: 10
Вершинное покрытие: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Коэффициент аппроксимации: 2.00
