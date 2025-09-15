The goal is to rotate an array of numbers to the right

moving the k elements to the beginning of the list and shifting the remaining to the right

steps I took:

calculate the k=k%n where n is the length of the array, handling cases cases where k is larger than the array length

reverse the entire array

reverse the first k elements to return them to their original order

reverse the rest of the array
