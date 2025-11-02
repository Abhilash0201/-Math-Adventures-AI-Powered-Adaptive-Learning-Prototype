import random
def gen_problem(difficulty):
    if difficulty=='Easy':
        a,b=random.randint(1,10),random.randint(1,10);op='+'
    elif difficulty=='Medium':
        a,b=random.randint(5,20),random.randint(2,12);op=random.choice(['+','-'])
    else:
        a,b=random.randint(10,50),random.randint(2,20);op=random.choice(['+','-','*'])
    if op=='/': a=a*b
    q=f"{a} {op} {b}"; ans=eval(q); return q,ans,{}
