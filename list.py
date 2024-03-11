word_list = ["apple", "banana", "orange", "grape", "pear", "kiwi","santy","g"]

odd_words=[word for word in word_list
    if len(word)%2!=0]
print(odd_words)