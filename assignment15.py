import gc
import time
import tracemalloc

# Class to create circular references
class Node:
    def __init__(self):
        self.ref = None

# Function to create circular references
def create_objects(n):
    objects = []

    for i in range(n):
        a = Node()
        b = Node()

        a.ref = b
        b.ref = a

        objects.append(a)

    return objects


# Start memory tracking
tracemalloc.start()

# Enable garbage collection
gc.enable()

print("Garbage Collection Enabled:", gc.isenabled())

# Create objects
print("\nCreating objects...")
objects = create_objects(10000)

print("Objects created successfully.")

# Delete references
del objects

print("\nObjects deleted.")

# Check memory before collection
current, peak = tracemalloc.get_traced_memory()
print("Memory before collection:", current, "bytes")

# Perform manual garbage collection
start = time.time()

collected = gc.collect()

end = time.time()

# Check memory after collection
current, peak = tracemalloc.get_traced_memory()

print("\nGarbage Collection Completed")
print("Objects collected:", collected)
print("Memory after collection:", current, "bytes")
print("Peak memory usage:", peak, "bytes")
print("Time taken:", end - start, "seconds")

# Display garbage collection status
print("\nGarbage Collection Statistics:")
print(gc.get_stats())

# Stop memory tracking
tracemalloc.stop()

print("\nProgram completed successfully.")