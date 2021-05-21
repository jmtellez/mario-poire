class Solution(object):
   def calculateTime(self, kboard, word):
        letter = {kboard[i]: i for i in range(26)} #sets range.
        current = 0
        result = 0
        for char in word:   #loops for every character in the word.
            result += abs(letter[char] - current) #updates the calculated time result.
            current = letter[char] #changes current position in the word.
        return result

ob1 = Solution() #stores solution.
keyboard = "abcdefghijklmnopqrstuvwxyz" #Preset keyboard.
while True:
        Word = input("Enter a string: ") #string input.
        if Word.islower() == True and len(Word) >= 1 and len(Word) <= 1000: #Checks to see that the string length is between 1 and 1000 as well as lowercase.
            print(ob1.calculateTime(keyboard, Word)) #prints calculated time.
            break
        else:
            print ("Error, try again.")