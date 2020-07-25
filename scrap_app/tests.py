print("Lets start what you want")
frame_prize = [1000, 800, 500]  # aluminum,steel,iron
handbreak_prize = [100, 900, 800]  # type 1, type2...
typr_prize = [500, 800]  # tube,tubless
chain_assm_prize = [1800, 1600, 1400]  # type1,type2....


class tests:

    def input(self):
        print("Enter Today's date in DD/MM/YYYY format")
        date = input()
        print('date:', int(date[0:2]) + 1, date[3:5], date[6:10])
        print("Which type of frame you want: \n \
              Press 1 for Aluminum \n \
              Press 2 for Iron \n \
              Press 3 for Steel")
        type_frame = int(input())


        print("Which type of Handle_break you want: \n \
              Press 1 for type1 \n \
              Press 2 for type2 \n \
              Press 3 for type3")
        type_hand_break = int(input())


        print("Which type of Wheel you want: \n \
              Press 1 for with tube \n \
              Press 2 for tubless")
        type_tyre = int(input())


        print("Which type of chain_assembly you want: \n \
              Press 1 for type1 \n \
              Press 2 for type2 \n \
              Press 3 for type3")
        type_chain_assembly = int(input())

        type_list = [type_frame, type_hand_break, type_tyre, type_chain_assembly,int(date[6:10])]
        return type_list



def calculte():
    total = 0
    obj = tests()
    list = obj.input()
    total = frame_prize[list[0]-1] + handbreak_prize[list[1]-1] + typr_prize[list[2]-1] + chain_assm_prize[list[3]-1] - (list[4] - 2020)*10
    print(total)

calculte()