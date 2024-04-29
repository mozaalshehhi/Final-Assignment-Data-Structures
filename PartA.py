import random

class Post:
    def __init__(self, postID, views, creatorname, postdate, posttime):
        self.postID = postID
        self.views = views
        self.creatorname = creatorname
        self.postdate = postdate
        self.posttime = posttime

class Node: #Creating class node
    def __init__(self, post):
        self.post = post
        self.left = None
        self.right = None
        
#Hash Table: 1
class Hash: #Creating hash table
    def __init__(self):
        self.hashTable = {} #Creates dictionary to insert the posts inside the hashtable

    def sortingPostsByDate(self, posts): #Creating hashtable to organize posts by date to access posts by their unique time
        for post in posts:
            if post.postdate in self.hashTable: #Checks whether if the post date is in the hashtable to append it if not creates new entry
                self.hashTable[post.postdate].append(post)
            else:
                self.hashTable[post.postdate] = [post]

        sortedKeys = sorted(self.hashTable.keys()) #Here it sorts the dates of the hash table

        sortedPosts = []
        for key in sortedKeys: #Here it extends the sorted posts list with posts from each date in sorted order.
            sortedPosts.extend(self.hashTable[key])

        return sortedPosts

#Binary Search Tree : 2
def insert(root, post): #Function to insert a post node into the BST based on the post's date

    if root is None:
        return Node(post)
    else:
        if root.post.postdate < post.postdate:
            root.right = insert(root.right, post)
        else:
            root.left = insert(root.left, post)
    return root

def findingPosts(root, startDate, endDate, result=[]): #Function to find posts within a specific time range in the binary search tree.
    if root is None:
        return result
    if startDate <= root.post.postdate <= endDate:
        result.append(root.post)
    if root.post.postdate > startDate:
        findingPosts(root.left, startDate, endDate, result)
    if root.post.postdate < endDate:
        findingPosts(root.right, startDate, endDate, result)
    return result

#Max heap function: 3
def heapify(heap, i):
    #Functions to calculate the index of left and right children.
    def left(i):
        return 2 * i + 1
    def right(i):
        return 2 * i + 2

    left_idx = left(i)
    right_idx = right(i)
    largest = i
    

    if left_idx < len(heap) and heap[left_idx].views > heap[largest].views: #Here it Compares with the left child and updates the largest if it's not the largest.
        largest = left_idx

    if right_idx < len(heap) and heap[right_idx].views > heap[largest].views: #Here it Compares with the right child and updates the largest if it's not the largest.
        largest = right_idx

    if largest != i: #It checks whether if the largest not is not the current node, if not it swaps and compares it again.
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, largest)

#Test Case:

# Creating posts 
post1 = Post(1, 102, "Zii877", "2024-04-26", "08:30")
post2 = Post(2, 2455, "Mxi-65", "2024-04-27", "10:45")
post3 = Post(3, 2003, "Mozza.09", "2024-04-28", "12:15")
post4 = Post(4, 10500, "Nor42", "2024-04-29", "14:20")
post5 = Post(5, 780, "i._tr3", "2024-04-30", "16:40")


posts = [post1, post2, post3, post4, post5] #Creating a List for the post


random.shuffle(posts) #Here we Shuffle the list to create a random order


print("Original list of posts:") #Expected: it will print randomly since I used random.shuffle(posts) as it randomly shuffled the post.
for post in posts:
    print(f" The post ID:{post.postID}, The post views: {post.views}, The name of the creator of the post is: {post.creatorname}, The post Date: {post.postdate}, The post time: {post.posttime}")

#Test Case for BST:
# Creating a binary search tree and inserting posts
root = None
root = insert(root, post1)
root = insert(root, post2)
root = insert(root, post3)
root = insert(root, post4)
root = insert(root, post5)

# Test finding posts within a specific time range
startDate = "2024-04-27"
endDate = "2024-04-29"
postsInRange = findingPosts(root, startDate, endDate)
print(f"\nPosts within the time range within", startDate, "till", endDate)
for post in postsInRange:
    print(post.postID, post.views, post.creatorname, post.postdate, post.posttime) #Expected Outcome: it will print the posts that ranges within 27 till 29 without including the post that was posted at date 30


#Test case for hashtable:
postList = [post1, post2, post3, post4, post5]
hashTable = Hash()
sortedPosts = hashTable.sortingPostsByDate(postList)
print("\nSorted posts by date:")
for post in sortedPosts:
    print(f"Post ID:",post.postID,"Post View:", post.views,"Username of the post's creator:", post.creatorname,"Post's Date:", post.postdate,"Post's Time:", post.posttime) 


#Max heap test case:
heapify(posts, 0)
print("\nMax heap of posts:") #Excpected Outcome: Nora's post which has 10500 views
for post in posts:
    print(f"{post.postID}, {post.views}, {post.creatorname}, {post.postdate}, {post.posttime}")
    
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
