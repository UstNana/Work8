k = 0
cookbook = {}
big_list = []
with open("HW8.txt") as f:
    while True:
        meal = f.readline().strip()
        list_meal = meal.split()
        quantity = f.readline().rstrip('\n')
        for k in range(int(quantity)):
          list_1 = f.readline().strip()
          l_list_1 = list_1.split()
          big_list.append({'ingridient_name': l_list_1[0], 'quantity': l_list_1[2], 'measure': l_list_1[4]})
          for eat in list_meal:
              if eat not in cookbook.keys():
                cookbook[eat] = big_list
                print (cookbook)
        f.readline()
