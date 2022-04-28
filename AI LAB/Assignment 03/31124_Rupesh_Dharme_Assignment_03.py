# Rupesh Dharme
# TE 01
# 31124
# Assignment 03

# Implement Greedy search algorithm for Selection Sort problem.

# cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

priority = { # priority of cards
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

def selectionSort(cards):
    
    for i in range(len(cards) - 1): # for each index from "0" to "n-2" we find minimum element from unsorted array

        next = i # stores the index of minimum element
        for j in range(i, len(cards)):
            if priority[cards[j]] < priority[cards[next]]: # finding the next minimum element
                next = j
        
        temp = cards[next]
        cards[next] = cards[i] # swapping the minimum element with element at index "i"
        cards[i] = temp

def main():
    cards = list(map(str.upper, input("Enter cards in any order\n").split(" ")))

    selectionSort(cards)
    
    for card in cards:
        print(card, end = " ")
    
if __name__ == "__main__":
    main()