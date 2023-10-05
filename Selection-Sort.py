import time

start_time = time.time()
def selection_sort(v):
    for i in range(len(v)):
        min_idx = i
        
        for j in range(i + 1, len(v)):
            if v[j] < v[min_idx]:
                min_idx = j

        v[i], v[min_idx] = v[min_idx], v[i]

    return v
    

valores = []

valores_ordenados = selection_sort(valores)
print(valores_ordenados)

end_time = time.time()

print("O tempo que leva para a execução é :", end_time - start_time)