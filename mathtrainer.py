import random
def check(oper,number1,number2):
    return eval('number1'+oper+'number2')
    
    


if __name__ == "__main__":
    name = input("enter your name please :")

    lvl=int(input (f""" hi {name} what is your level : 
                     (1) Beginner
                     (2) intermediate
                     (3) expert
                     -> """))
    oper = input("choose your operation  - / * + :")
    if lvl==1:
        _start=1
        _end=10

    if lvl==2:
        _start=1000
        _end=4000

    if lvl==3:
        _start=10000
        _end=50000
    _try=3 # how much of tries do u have
    score=0
    while True:
        number1=random.randrange(_start,_end)
        number2=random.randrange(_start,_end)
        answer=int(input(f"""
        {number1}
    {oper}
        {number2}
        _________
      ->"""))
        result=check(oper=oper,number1=number1,number2=number2)
        if answer==result:
            score+=1
        while _try !=0 and answer!=result:
            _try-=1
            answer=int(input("""wrong answer try again !!
    ->"""))
        if _try==0:
            print (f"""GAME OVER !!
your score is {score}""")
            break
