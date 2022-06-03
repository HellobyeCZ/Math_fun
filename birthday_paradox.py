from itertools import combinations
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from tqdm import tqdm
import math

class math_fun:

    "Class for showing off interesting math phenomenons."

    def BD_paradox_sim(students, n_SameBD, n):

        "Simulation of wide known Birthday paradox."

        data = pd.DataFrame(index= np.arange(students), columns= np.arange(n))
        boolean_ = pd.Series(index= np.arange(n), dtype="int")

        for i in tqdm(range(n)):
            data[i] = np.random.randint(1,365,students)

            if n_SameBD == 2:
                boo = int(data[i].duplicated().any())
                boolean_[i] = boo
            else:
                max_ = data[i].value_counts().max()
                boo = int(max_ >= n_SameBD)
                boolean_[i] = boo


        results = pd.DataFrame()

        results["cumsum"] = np.cumsum(boolean_)
        results["n"] = range(1, n+1)
        results["Prob"] = results["cumsum"]/results["n"]

        per_cent = sum(boolean_)/n

        plt.plot(results["Prob"])
        plt.title(f"Probability over iterations")

        print(f"\nBased on simulation (n = {n}), probability of at least {n_SameBD} students having birthday on the same day in class of size {students} is: {per_cent}.\n")

    def BD_paradox_calc(students):

        "Works only for 2 birthdays in same day."

        num_of_combination = len(list(combinations(range(students),2)))

        prob = 1 - math.pow(364/365,num_of_combination)

        print(f"\nCALCULATED probability of 2 people sharing birthday in one day in class of {students} is {round(prob,3)}.\n")


    def Fibonnaci(n):

        "Return n-th number from Fibonacci sequence (NOT OPTIMIZED)."

        if n <= 1:
            return n

        else: 
            return math_fun.Fibonnaci(n-1) + math_fun.Fibonnaci(n-2)

    
    def Fibonnaci_opt(n):
        
        "Return n-th number from Fibonacci sequence (OPTIMIZED)."
        
        if n <= 1:
            return n

        else:
            Fib = pd.Series(range(n+1))
            Fib[0] = 0
            Fib[1] = 1
            for i in range(2,n+1):
                Fib[i] = Fib[i-1]+Fib[i-2]
            
            return Fib[n]



math_fun.BD_paradox_sim(35,2,100)
math_fun.BD_paradox_calc(35)
math_fun.Fibonnaci(20)
math_fun.Fibonnaci_opt(50)