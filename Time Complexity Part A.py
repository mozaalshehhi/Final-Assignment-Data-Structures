    
#plt 
import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to calculate the time complexities for BST and Max Heap
def bst_time_complexity_worst_case(n):
    # Worst-case scenario for BST (unbalanced tree)
    return n ** 2

def bst_time_complexity_average_case(n):
    # Average-case scenario for BST (balanced tree)
    return n * np.log2(n)

def max_heap_time_complexity(n):
    # Max heap construction complexity is linear
    return n

# Generating data points
n_values = np.arange(1, 100)
bst_complexities_worst_case = [bst_time_complexity_worst_case(n) for n in n_values]
bst_complexities_average_case = [bst_time_complexity_average_case(n) for n in n_values]
max_heap_complexities = [max_heap_time_complexity(n) for n in n_values]

# Plotting the graphs
plt.figure(figsize=(10, 12))

plt.subplot(2, 1, 1)
plt.plot(n_values, bst_complexities_worst_case, label='BST (Worst Case)')
plt.plot(n_values, bst_complexities_average_case, label='BST (Average Case)')
plt.xlabel('Number of Posts')
plt.ylabel('Time Complexity')
plt.title('Binary Search Tree (BST) Time Complexity Analysis')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(n_values, max_heap_complexities, label='Max Heap')
plt.xlabel('Number of Posts')
plt.ylabel('Time Complexity')
plt.title('Max Heap Time Complexity Analysis')
plt.legend()
plt.grid(True)
