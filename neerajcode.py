print('Welcome to general knowledge Quiz competition')
answer=input('Are you ready to answer the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1:  Which country is home to the kangaroo?')
    if answer.lower()==' Australia':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2:  Who wrote the Indian National Anthem?')
    if answer.lower()=='  Rabindranath Tagore':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Who is the inventor of Radio?')
    if answer.lower()=='Marconi':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
