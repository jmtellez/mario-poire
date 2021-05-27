import re #imports module.
def rem_vowel(s): #Removes Vowels.
    answer = re.sub(r'[AEIOU]', r'', s, flags=re.IGNORECASE) #uses re.sub to replace all the vowels with emptyspace to remove them.
    print(answer)
    return answer
  
while True:
    s = input("Enter a string: ")
    if s.islower() == True and len(s) >= 1 and len(s) <= 1000: #Checks to see that the string length is between 1 and 1000 as well as lowercase.
        rem_vowel(s)
        break
    else: #Prompts user to enter a string again if constraints aren't met.
        print("Error, try again.")
