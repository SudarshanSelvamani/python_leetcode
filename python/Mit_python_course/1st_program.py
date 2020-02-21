print('Please think of a number between 0 and 100!')
list1 = ['h', 'l', 'c']
low = 0
high = 100
ans = 0
while True:
    ans = int((high + low)/2)
    print('is this your secret number', ans)
    label = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if label in list1:
        if label == 'h':
            high = ans
        elif label == 'l':
            low = ans  
        else:
            print('Game over. Your secret number was:',ans)
            break
    else:
        print('Sorry, I did not understand your input.')


    
    
    
          

 


 