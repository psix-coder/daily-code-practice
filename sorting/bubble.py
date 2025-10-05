# def bubble_sort(arr):
#     """
#     Bubble Sort algoritmi
#     Massivni o'sish tartibida saralaydi
#     """
#     n = len(arr)
    
#     # Bu yerga kodingizni yozing!
#     pass


# # Test
# if __name__ == "__main__":
#     # Test 1
#     arr1 = [5, 2, 8, 1, 9]
#     bubble_sort(arr1)
#     print(arr1)  # [1, 2, 5, 8, 9]



def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr1 = [5, 2, 8, 1, 9]
bubble_sort(arr1)
print(arr1) 