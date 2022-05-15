def welcome_screen():
    print("""---------------------------
Welcome to The Maori quiz
---------------------------""")
    while True:
        yes_no = input("Have you played before? (Y/N): ").upper()
        if yes_no == 'Y':
            maori_numbers()
            break
        elif yes_no == 'N':
            print("""\t* How to play *
The Maori quiz gives you three different type of questions
\t1. Maori numbers where you have a maths question and have to answer in Maori
\t2. Maori days where you are given days of the week and you have to change them into Maori
\t3. Maori months where you are given months in a year and you have to change them into Maori
After ten questions of each you are given a chance to go to the next type of questions
you get points after each question you get right and be careful once you fail one you 
can't play anymore. So have fun.
These are the Maori words you will need.
1 - tahi
2 - rua
3 - toru
4 - wha
5 - rima
6 - ono
7 - whitu
8 - waru
9 - iwa
10 - tekau
Monday - Rahina
Tuesday - Ratu
Wednesday - Raapa
Thursday - Rapare
Friday - Ramere
Saturday - Rahoroi
Sunday - Ratapu
January - Kohitatea
February - Hui-tanguru
March - Poutu-te-rangi
April - Paenga-whawha
May - Haratua
June - Pipiri
July - Hongongoi
August - Here-turi-koka
September - Mahuru
October - Whiringa-a-nuku
November - Whiringa-a-rangi
December - Hakihea""")
            maori_numbers()
            break
        else:
            print("That is not an answer")


def game_summary(points):
    if points >= 1:
        print(f"You got {points} points")
    else:
        print("Sorry but you didn't get any points")
    exit()


welcome_screen()
