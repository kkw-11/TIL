words = ["hot", "dot", "dog", "lot", "log", "cog"]

for i in range(len(words)) :
    wd = "hit"
    print([j for j in range(len(words[i])) if words[i][j] != wd[j]])