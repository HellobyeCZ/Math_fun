# Math_fun
Repository just for fun, with some interesting math problems/theorems.

# Current codes in Math_fun class

## Birthday paradox
### Description
[wiki](https://en.wikipedia.org/wiki/Birthday_problem)

### Code
Ever wondered what is the probability of 2 people sharing birthday in a group?
- First: ```math_fun.BD_paradox_sim(n, k, N)``` will get you approx. probability of k people having birthday in same day in group of n (simulated N times).
- Second: ```math_fun.BD_paradox_calc(n)``` will calculate exact probabilty of k people having birthday in same day in group of n.

### Examples:
```
math_fun.BD_paradox_sim(35,2,100)
math_fun.BD_paradox_calc(35)
```

## Fibonnaci series
### Description
[wiki](https://en.wikipedia.org/wiki/Fibonacci_number)

### Code
Non optimized version usually crash at 100-th number. 
- First: ```math_fun.Fibonnaci(n)``` will get you first n numbers of Fibonnaci series.
- Second: ```math_fun.Fibonnaci_opt(n)``` will get you first n numbers of Fibonnaci series. BUT OPTIMIZED. 

### Examples:
```
math_fun.Fibonnaci(10)
math_fun.Fibonnaci_opt(50)
```
## Collatz Conjecture
### Description
[wiki](https://en.wikipedia.org/wiki/Collatz_conjecture)

### Code
- ```math_fun.Collatz_Conjecture(i)``` Will return list of all numbers in sequnce after i. Based on Collatz conjecture rules.

### Examples:
```
l_list = []
for i in tqdm(range(40)):
    l = math_fun.Collatz_Conjecture(i)
    plt.plot(l)
    l_list.append(l)
    #print(i)

plt.show()
```
