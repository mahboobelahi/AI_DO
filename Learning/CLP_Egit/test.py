import random

def order_based_crossover(parent1, parent2):
    # Create two child chromosomes filled with placeholders
    child1 = [-1] * len(parent1)
    child2 = [-1] * len(parent2)
    
    # Select two random positions i and j
    i = random.randint(0, len(parent1) - 1)
    j = random.randint(i, len(parent1) - 1)
    
    # Copy genetic material from parents to children within the range [i, j]
    child1[i:j+1] = parent1[i:j+1]
    child2[i:j+1] = parent2[i:j+1]
    
    # Create sets to keep track of copied values
    copied_values_child1 = set(child1[i:j+1])
    copied_values_child2 = set(child2[i:j+1])
    
    # Fill the remaining positions circularly with values from the other parent
    idx1, idx2 = (j + 1) % len(parent1), (j + 1) % len(parent2)
    for _ in range(len(parent1) - (j + 1)):
        while parent2[idx2] in copied_values_child1:
            idx2 = (idx2 + 1) % len(parent2)
        while parent1[idx1] in copied_values_child2:
            idx1 = (idx1 + 1) % len(parent1)
        child1[idx1] = parent2[idx2]
        child2[idx2] = parent1[idx1]
        copied_values_child1.add(parent2[idx2])
        copied_values_child2.add(parent1[idx1])
        idx1 = (idx1 + 1) % len(parent1)
        idx2 = (idx2 + 1) % len(parent2)
    
    return child1, child2

# Example usage
parent1 = [3,6,2,0,2,4,5]
parent2 = [4,0,2,1,5,3,6]

child1, child2 = order_based_crossover(parent1, parent2)
print("Child 1:", child1)
print("Child 2:", child2)
