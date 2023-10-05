import time

start_time = time.time()


def merge_sort(v):
    if len(v) <= 1:
        return v

    mid = len(v) // 2
    left_half = v[:mid]
    right_half = v[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


valores = []



valores_ordenados = merge_sort(valores)
print(valores_ordenados)

end_time = time.time()

print("O tempo que leva para a execução é :", end_time - start_time)