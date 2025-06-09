## Implementação de Insertion Sort simples, visando entender o funcionamento do código

def insertionSort(array):
    contador = 0

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
            contador += 1

        array[j+1] = key
        print(f"Interação número {i}: {array}")
        print(f"O contador está em: {contador}")

insertionSort([20, 9, 5, 4, 1, -20, -30, -40, -50])