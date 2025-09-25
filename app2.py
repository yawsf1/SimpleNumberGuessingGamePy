from random import randint

answer = randint(1, 100)
score = 0
attempt = 0
while True:
    try:
        n = int(input('\nEntrer a number between 1 and 100: '))
        if(n > 100 or n < 1):
            print('Incorrect number')
            continue
        else:
            if(n == answer):
                score = score + 1
                print("Congrats you did win\n")
                print(f'Your score now is {score}\n')
                print(f'And you attempts are: {attempt}\n')
                attempt = 0
                answer = randint(1, 100)

                continue
                
            elif(n > answer + 30):
                attempt = attempt + 1
                print("Too big")
                print(f'attempts : {attempt}')
            elif(n > answer):
                attempt = attempt + 1
                print("Bigger a bit")
                print(f'attempts : {attempt}')

            elif(n < answer - 30):
                attempt = attempt + 1
                print("Too small")
                print(f'attempts : {attempt}')

            elif(n < answer ):
                attempt = attempt + 1
                print("smaller a bit")
                print(f'attempts : {attempt}')
    except ValueError:
        print("You should enter a number")
        continue