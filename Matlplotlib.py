import matplotlib.pyplot as plt
import numpy as np

print("Hello there! \nEnter the team names")
team1 = input()
team2 = input()

format=-1
def form():
    global format  
    print("Please Select Fomat\n")
    print("1. T10 Cricket")
    print("2. ODI Cricket")
    print("3. T20 Cricket")
    format = int(input())
    if (format==1 or format== 2 or format==3):
        print("Enter the Score in each matches\n")
        return
    else:
        print("Invalid format selected")
        form()

form()



def ploter(p ,q):
            over =[]
            score_team1 =[]
            score_team2=[]
            for i in range(p,q):
                score_team1.append(int(input(f"Enter the score of   {team1}   in Over  {i}:" )))
                score_team2.append(int(input(f"Enter the score of  {team2}  in Over  {i}: ")))
                over.append("Overs " + str(i))
                print("\n")
    
            total_score_team1=sum(score_team1)
            total_score_team2=sum(score_team2)


            plt.figure(figsize=(10, 6))
            x = np.arange(len(over))

            plt.bar(x - 0.2, score_team1, width=0.4, label=team1, color='#4CD0E4')
            plt.bar(x + 0.2, score_team2, width=0.4, label=team2, color='#E44C4C')

            plt.xlabel('Overs')
            plt.ylabel('Scores')
            plt.title(f"Scores Per Over: {team1} vs {team2}")
            plt.xticks(x, over, rotation=45)  
            plt.legend()  
            plt.tight_layout()  
            plt.show()


def linplot(p,q):

            over =[]
            score_team1 =[]
            score_team2=[]
            for i in range(p,q):
                score_team1.append(int(input(f"Enter the score of   {team1}   in Over  {i}:" )))
                score_team2.append(int(input(f"Enter the score of  {team2}  in Over  {i}: ")))
                over.append("Overs " + str(i))
                print("\n")
    
            total_score_team1=sum(score_team1)
            total_score_team2=sum(score_team2)

            plt.figure(figsize=(10, 6))
            plt.plot(over, score_team1, label=f'{team1} Scores', color='#4CD0E4', marker='o')
            plt.plot(over, score_team2, label=f'{team2} Scores', color='#E44C4C', marker='x')

            plt.xlabel('Overs')
            plt.ylabel('Scores')
            plt.title(f"Scores Over Time: {team1} vs {team2}")
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.show()







def chose():
    print("Which Type of Visulisation Required")
    print("1 Bar Grap")
    print("2 Line Graph")
    data=int(input())

    if (data==1):
        if (format==1):
            ploter(1,11)
        elif (format==2):
            ploter(1,51)
        elif(format==3):  
            ploter(1,21)    

    elif(data==2):
        if (format==1):
            linplot(1,11)
        elif (format==2):
           linplot(1,51)
        elif(format==3):  
            linplot(1,21)  
    else:
        print("Invalid Input")
        chose()
chose()        