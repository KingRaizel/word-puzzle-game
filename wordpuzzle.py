import random

def puzzledword(wrd):
    pw = random.sample(wrd, k= len(wrd))
    return "".join(pw)

def printpuzzle(word, score):
    puzzleword = puzzledword(word)
    print("Arrange the below word in right order - ")
    print(puzzleword)
    userinput= input()
    print()
    if userinput.upper() == word:
        print("Correct")
        print()
        score+=1
    else:
        print("Wrong")
        print()
        score-=1
    
    return score
    

def main():
    score= 0
    words = ["COUNTRY", "PYTHON", "MACHINE", "LEARNING", "ITERATION", "ARTIFICIAL", "INTELLIGENCE"]
    swords = random.sample(words,k = 3)

    for w in swords:
        score = printpuzzle(w,score)
    
    print("Your score is {}".format(score))


main()