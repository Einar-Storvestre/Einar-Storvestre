

def f(x):
    return x**2 -3 * x +5

x= 0
dx = 0.1

while x < 3:
    print(f"x={x:.1f}, og f'({x:.1f}) er tilnærmet lik {(f(x+dx)-f(x))/dx:.2f}")
    x += dx