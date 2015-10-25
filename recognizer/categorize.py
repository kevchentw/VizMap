f_word = open("./word.txt","r")

sentence = input("Enter: ")

for line in f_word:
    test = line.split(" ")
    for item in test:
        if sentence.find(item) != -1:
            print(test[0])
