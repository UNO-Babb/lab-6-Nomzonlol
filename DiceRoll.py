#DiceRoll.py
#Name:Nomaan Ahmed 
#Date:3/1/25
#Assignment:Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  #find the sum total of the two dice
  total = die1 + die2
  rolls[total] += 1
  #print statictics for dice rolls
  print("Sum\tCount\tPercentage")
  print("-" * 30)
  for i in range(2, 13):
        percentage = (rolls[i] / 10000) * 100
        print(f"{i}\t{rolls[i]}\t{percentage:.2f}%")

if __name__ == '__main__':
  main()
