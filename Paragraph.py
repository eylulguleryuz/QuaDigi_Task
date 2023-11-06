import re

#input
text = """The European languages are members of the same family. Their separate existence is a myth. 
For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, 
their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: 
one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, 
pronunciation and more common words. If several languages coalesce, the grammar of the resulting language 
is more simple and regular than that of the individual languages. The new common language will be more simple 
and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be 
Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of 
mine told me what Occidental is."""
print("----------------------------")
print()
print("Text given:")
print(text)
print()

# 1) TO DO: Find the number of times each word in the paragraph is used. Print the top 3 most used words.
#######
# regular expressions can be used: words = re.findall(r'\w+', text.lower())
text = text.lower()
words = text.split()

# dictionary
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = sorted(word_count.items(), key=lambda x: -x[1])


top_words = sorted_word_count[:3]
print("----------------------------")
print()
print("Top 3 words:")
print("***")
for word, count in top_words:
    print(f"{word}: {count} times")
print()

#2) TO DO: Find the shortest sentence from the paragraph. Print the sentence and the number of words in that sentence.
#######
sentences = text.split('.')

# Considers the case if there are more than one shortest sentences
shortest_sentences = []
shortest_word_count = float('inf')

for sentence in sentences:
    words = sentence.strip().split()
    word_count = len(words)
    
    if word_count > 0 and word_count == shortest_word_count:
        shortest_sentences.append((sentence.strip(), word_count))
    
    elif word_count > 0 and word_count < shortest_word_count:
        shortest_sentences = [(sentence.strip(), word_count)]
        shortest_word_count = word_count

print("----------------------------")
print()

print("Shortest Sentence(s):")
print("***")
for sentence, word_count in shortest_sentences:
    print(sentence)
    print(f"Number of Words in the Sentence: {word_count}" )
    print()


# 3) TO DO: Print a version of the paragraph in which the first and every other letter from every word is capitalized.
#######
words = text.split()
def customize_word(word):
    result = ""
    for i, char in enumerate(word):
        if i % 2 == 0:  # every other letter
            result += char.upper()
        else:
            result += char
    return result

# Apply to each word
customize_words = [customize_word(word) for word in words]

modified_text = ' '.join(customize_words)
print("----------------------------")
print()
print(modified_text)
print()

# 4) TO DO: Print a version of the paragraph in which all words are in reversed order.
#######
sentences = text.split('.')

sentences = [sentence.strip() for sentence in sentences]

# Reverse the order of words in a sentence while preserving punctuation
def reverse_sentence_with_punctuation(sentence):
    words_and_punctuation = re.findall(r'\b\w+\b|[.,!?;]', sentence)
   
    words_and_punctuation = words_and_punctuation[::-1]
    reversed_sentence = ''
    for wordOrPunctiation in words_and_punctuation:
        # Avoid extra spaces before punctuation marks
        if wordOrPunctiation not in [".", ",", "!", "?", ";"]:
            reversed_sentence += ' ' + wordOrPunctiation
        else:
            reversed_sentence += wordOrPunctiation

    return reversed_sentence

reversed_sentences = [reverse_sentence_with_punctuation(sentence) for sentence in sentences]

# Add the dots to the end of sentences
modified_text = '.'.join(reversed_sentences)

print("----------------------------")
print()

print(modified_text)
print()


