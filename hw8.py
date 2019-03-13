# -*- coding: utf-8 -*-
with open("HW8.txt") as file:
  quantity_person = int(input("How much person"))
  new_eat = input("Describe mew recept ")
  while True:
    file.write(new_eat)
    meal = file.readline().strip()
    list_meal = meal.split()
    quantity = file.readline().rstrip('\n')
    h = quantity.split()
    k = 0
    for i in h:
      i = int(i)
      for k in range(i):
        big_list = []
        list_1 = file.readline().strip()
        l_list_1 = list_1.split()
        l_list_2 = l_list_1[0::2]
        quantity = int(l_list_2[1])*quantity_person
        print(l_list_2, n)
        big_list.append({'ingridient_name': l_list_2[0], 'quantity': quantity, 'measure': l_list_2[2]})
        print(big_list)
