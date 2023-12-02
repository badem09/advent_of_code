# --- Day 11: Monkey in the Middle ---
import math
from collections import deque

dict_monkey = {}

class Monkey:

    def __init__(self, id, liste_items, op, monkeyTrue, monkeyFalse):
        self.id = id
        self.current_items = deque(liste_items)
        self.op = op # retourne un float
        self.nextMonkeyTrue = monkeyTrue
        self.nextMonkeyFalse = monkeyFalse
        self.inspected_items = 0

    def throw_item(self, item, divisible):

        #item = self.current_items.popleft()

        if divisible:
            item = math.floor(item)
            nextMonkey = dict_monkey[self.nextMonkeyTrue]
            nextMonkey.current_items.append(item)


        else:
            item = math.floor(item)
            nextMonkey = dict_monkey[self.nextMonkeyFalse]
            nextMonkey.current_items.append(item)

        self.inspected_items += 1
        self.current_items.popleft() #ou remove?

    def execute_op(self):
        for _ in range(len(self.current_items)):
            items = self.current_items[0]
            a_jeter = []
            liste = self.op.split(" ")
            op_type = liste[1]
            var2 = liste[2]
            var3 = liste[-1][:-1]

            if op_type == "+":
                if var2.isdigit() and var3.isdigit():
                    items = (items + int(var2))  // 3 #int(var3)
            if op_type == "*":
                if var2.isdigit() and var3.isdigit():
                    items = (items * int(var2) )// 3 #int(var3)
                elif not var2.isdigit():
                    items = items**2 // 3 #int(var3)
            self.current_items[0] = items

            if (items/int(var3) % 1 == 0):
                self.throw_item(items,True)
            else:
                self.throw_item(items,False)




    def __str__(self):
        """   l1 = "Monkey n° " + str(self.id) + "\n"
        l2 = "items : " + str(self.current_items)  + "\n"
        l4 = 'op : ' + self.op + '\n'
        l3 = 'nextTrue : ' + str(self.nextMonkeyTrue) + ' nextFalse : ' + str(self.nextMonkeyFalse)

        return l1 + l2 + l4 + l3
        """
        #return "Monkey n° " + str(self.id) + " : " +  str(self.inspected_items)
        return str(self.current_items) + " : " + str(self.inspected_items)

def mise_en_place():
    f = open("inputTest.txt")
    liste_f = list(f)
    for i in range(len(liste_f)):
        l = liste_f[i]
        liste = l.split(" ")

        if "Monkey" in l:
            curr_monkey_id = int(liste[1][0])

        if "Starting" in l :
            liste_items = [int(i.replace(',',"")) for i in liste[4:]]

        if "Operation" in l:
            op = None
            n = [i.replace('\n',"") for i in liste[3:]]
            test = liste_f[i+1].split(" ") [-1]
            op = " ".join(n [2:6]) + " / " + test

        if "true" in l:
            monkeyT = int(liste[-1])

        if "false" in l :
            monkeyF = int(liste[-1])

        if l == "\n":
            monkey = Monkey(curr_monkey_id,liste_items,op,monkeyT,monkeyF)
            dict_monkey.update({curr_monkey_id:monkey})
            monkeyT = None
            monkeyF = None
            liste_items = None
            monkey = None


    def main():
        pass

if __name__ == "__main__":
    list_nb_items = []
    mise_en_place()

    for round in range (0,20):
        for key,m in dict_monkey.items():
            m.execute_op()
        print("round " , round)
        for key,m in dict_monkey.items():
            print(m)
    for key, m in dict_monkey.items():
        list_nb_items.append(m.inspected_items)

    max1 = max(list_nb_items)
    list_nb_items.remove(max1)
    max2 = max(list_nb_items)
    print(max1 * max2)



