#hangman game
import random

movie_list = [ "lagaan", "highway", "thor", "dangal", "newton"] 

movie = random.choice(movie_list) 

enc="*"*len(movie)            #encrypting the movie name

score = 10
while score>0 :           #checking score after each iteration
    print(enc) 
    print("score=", score)
    guess = input("guess a letter: ")  
    if guess == "" : 
    	print("Enter a character") 
    	continue
    index = [ ] 
    p=0
    c=0 
    
    for i in range(0,len(movie)) :           #to check whether entered character matches the name
    
        if guess in movie[i] :
              index.append(i)           #adding the index as a list whose character is equal to the entered character
        else : 
              p+=1 
              
    if p != len(movie) :           #if character in atleast one index matches
              fenc = list(enc) 
              for j in index :           #replacing "*" with the entered character 
                      if "*" in fenc[j] :          #to check whether the character is not already guessed
                          c+=1
                          fenc[j]=guess
                      else : 
                          break
                          
              if c == len(index) :           #if character is not guessed already
                       print("\n\ncorrect guess") 
                       score+=3 
              else : 
                       score-=2
                       print("\n\nincorrect guess")

              enc = ""
              for k in fenc : 
                       enc += k
    else :           #when none of the characters of name matches the entered character
              print("\n\nincorrect guess")
              score-=2 
              
    if '*' in enc :           #to check whether any letter is left in the movie name to be guessed
              pass 
    else :
              print(movie) 
              print(score)
              print("\nYou win")
              break
              
else :           #if score is not greater than zero
    print(movie)
    print("\nYou lose")
