#=====================================================================================
# bigram extractor

# eg. input: "i love machine learning"
#     output: i love
#         love machine
#         machine learning

words = input("Input sentence: ").split()

print("-----------------------Word pairs--------------------")

if len(words) == 1:
    print("NONE")
else:
    for i in range(1, len(words)):
        print(words[i-1], words[i])

print("-----------------------Word Pairs End--------------------")
print()

#=====================================================================================


# convert sentence into next word table 

# eg. input: "i love cats i love dogs i hate rain" 
#     output: {'i': ['love', 'love', 'hate'], 'love': ['cats', 'dogs'], 'cats': ['i'], 'dogs': ['i'], 'hate': ['rain'], 'rain': []}

# words = input().split()

d = {}

for i in range(len(words)):
    w = words[i]

    if w not in d:
        d[w] = []

    if i + 1 < len(words):
        d[w].append(words[i+1])


print("-----------------------Word Table--------------------")

print(d)

print("-----------------------Word Table End--------------------")


# for key in d:
#     val = d[key]

#     if val:
#         print(f"{key}: {" ".join(val)}")
#     else:
#         print(f"{key}: NONE")

#=====================================================================================

# Prediction system - takes pevious word, 

# eg. input: "i love cats i love dogs i hate rain" 
#     output: {'i': {'love': 2, 'hate': 1}, 'love': {'cats': 1, 'dogs': 1}, 'cats': {'i': 1}, 'dogs': {'i': 1},       'hate': {'rain': 1}, 'rain': {}}
# {'love': 2, 'hate': 1}
# love


count = {}

for key in d:
    count[key] = {}

    for word in d[key]:
        if word not in count[key]:
            count[key][word] = 0
        count[key][word] += 1

print("-----------------------Counter Table End--------------------")

print(count)

prev = input("Enter the word to predict after: ").strip()

print(count[prev])

print("-----------------------Counter Table End--------------------")
print("Predicted word: ")

if count[prev]:
    best_word = max(count[prev], key = count[prev].get)
    print(best_word)
else:
    print("NONE")