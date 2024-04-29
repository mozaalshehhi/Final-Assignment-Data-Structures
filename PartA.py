import random

class Post:
    def __init__(self, postID, views, creatorname, postdate, posttime):
        self.postID = postID
        self.views = views
        self.creatorname = creatorname
        self.postdate = postdate
        self.posttime = posttime

#Max heap function
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

# Heapifying the list
heapify(posts, 0)


print("\nMax heap of posts:") #Excpected Outcome: Nora's post which has 10500 views
for post in posts:
    print(f"{post.postID}, {post.views}, {post.creatorname}, {post.postdate}, {post.posttime}")
