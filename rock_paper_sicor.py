import random as r
class rock_paper_scissors:
    def __init__(self,user_points,oponent_points):
        self.user_points=user_points
        self.oponent_points=oponent_points
    def game(self,items):
         self.items=items
         while True:
            self.choice=r.choice(self.items)
            print(f"1-rock\n2-paper\n3-scissors\n4-display score\n5-end game")
            try:
                self.user_input=int(input("enter your choice :"))
                if self.user_input==1:  #rock
                   if self.choice=="paper":
                       print(f"user : rock\noponent : {self.choice}")
                       print(f"you lost !")
                       self.oponent_points+=1
                   elif self.choice=="scissors":
                       print(f"user : rock\noponent : {self.choice}")
                       print(f"you won !")
                       self.user_points+=1
                   else:
                       print(f"user : rock\noponent : {self.choice}")
                       print(f"tie")
                elif self.user_input==2:  #paper
                      if self.choice=="rock":
                          print(f"user : paper\noponent : {self.choice}")
                          print(f"you won")
                          self.user_points += 1
                      elif self.choice=="scissors":
                          print(f"user : paper\noponent : {self.choice}")
                          print(f"you lost !")
                          self.oponent_points += 1
                      else:
                          print(f"user : paper\noponent : {self.choice}")
                          print(f"tie")
                elif self.user_input==3: #scissors
                    if self.choice=="rock":
                        print(f"user : scissors\noponent : {self.choice}")
                        print(f"you lost")
                        self.oponent_points += 1
                    elif self.choice=="paper":
                        print(f"user : scissors\noponent : {self.choice}")
                        print(f"you won")
                        self.user_points += 1
                    else:
                        print(f"user : scissors\noponent : {self.choice}")
                        print(f"tie")
                elif self.user_input==4:
                    print(f"your points : {self.user_points}\noponent point : {self.oponent_points}")
                else:
                    print(f"your points : {self.user_points}\noponent point : {self.oponent_points}")
                    break
            except Exception as e:
               print(f"error : {e}")
def main():
    user_points=0
    oponent_points=0
    list_=["rock","paper","scissors"]
    obj=rock_paper_scissors(user_points,oponent_points)
    obj.game(list_)
if __name__=="__main__":
    main()

