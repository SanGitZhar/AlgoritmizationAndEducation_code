def CalcSumNumber (num, count_stop,count_control):
     num *=num
     count_control += 1
     print('iterration № ', count_control-1,' num = ', num)
     #check the stop moment
     if count_control>count_stop:
          return print('number multiplied ',count_stop,' times by it self = ', num)
     else:
          #recursion "function calls itself"
          CalcSumNumber(num,count_stop,count_control)     

def Main():
     #variable for control stop moment in recursion func
     count_control=1
     #input the number and multiply counter
     print("input the number")
     calc_num = float(input())
     print ("input how many times multiply by itself")
     power = int(input())
     #recursion func
     CalcSumNumber(calc_num, power,count_control)
     

Main()     