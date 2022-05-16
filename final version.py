import random


def welcome_screen():
    print("""---------------------------
Welcome to The Maori quiz
---------------------------""")
    yes_no_checker()


def yes_no_checker():
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


def maori_numbers():
    starter = input("Do you want to go through the 10 questions? (Y/N): ").upper()
    if starter == 'Y':
        print("")
    elif starter == 'N':
        print("Goodbye")
        exit()
    else:
        print("That is not an answer")
        maori_numbers()
    points = 0
    nine = input("""Question 1 
12 - 3 = """).lower()
    if nine == 'iwa':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    eight = input("""Question 2
2 + 6 = """).lower()
    if eight == 'waru':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    three = input("""Question 3
4 - 1 = """).lower()
    if three == 'toru':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    two = input("""Question 4
10 - 8 = """).lower()
    if two == 'rua':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    ten = input("""Question 5
5 + 5 = """).lower()
    if ten == 'tekau':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    one = input("""Question 6
3 - 2 = """).lower()
    if one == 'tahi':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    five = input("""Question 7
7 - 2 = """).lower()
    if five == 'rima':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    six = input("""Question 8
2 + 4 = """).lower()
    if six == 'ono':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    seven = input("""Question 9
4 + 3 = """).lower()
    if seven == 'whitu':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    four = input("""Question 10
4 + 0 = """).lower()
    if four == 'wha':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    last_num = input("Do you want to go on to Maori days? (Y/N): ").upper()
    if last_num == 'Y':
        maori_days(points)
    elif last_num == 'N':
        extra_nums(points)
    else:
        print("That is not an answer")


def maori_days(points):
    start = input("Do you want to go through the 10 questions? (Y/N): ").upper()
    if start == 'Y':
        print("")
    elif start == 'N':
        print("Goodbye")
        exit()
    else:
        print("That is not an answer")
        maori_days(points)
    tuesday = input("""Question 1 
Tuesday = """).lower()
    if tuesday == 'ratu':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    monday = input("""Question 2
Monday = """).lower()
    if monday == 'rahina':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    wed = input("""Question 3
Wednesday = """).lower()
    if wed == 'raapa':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    tue = input("""Question 4
Tuesday = """).lower()
    if tue == 'ratu':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    wednesday = input("""Question 5
Wednesday = """).lower()
    if wednesday == 'raapa':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    mon = input("""Question 6
Monday = """).lower()
    if mon == 'rahina':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    fri = input("""Question 7
Friday = """).lower()
    if fri == 'ramere':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    sat = input("""Question 8
Saturday = """).lower()
    if sat == 'rahoroi':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    sun = input("""Question 9
Sunday = """).lower()
    if sun == 'ratapu':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    thurs = input("""Question 10
Thursday = """).lower()
    if thurs == 'rapare':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    last_day = input("Do you want to go on to Maori months? (Y/N): ").upper()
    if last_day == 'Y':
        maori_months(points)
    elif last_day == 'N':
        extra_days(points)
    else:
        print("That is not an answer")


def maori_months(points):
    starter = input("Do you want to go through the 10 questions? (Y/N): ").upper()
    if starter == 'Y':
        print("")
    elif starter == 'N':
        print("Goodbye")
        exit()
    else:
        print("That is not an answer")
        maori_months(points)
    september = input("""Question 1 
September = """).lower()
    if september == 'mahuru':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    august = input("""Question 2
August = """).lower()
    if august == 'here-turi-koka':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    march = input("""Question 3
March = """).lower()
    if march == 'poutu-te-rangi':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    february = input("""Question 4
February = """).lower()
    if february == 'hui-tanguru':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    october = input("""Question 5
October = """).lower()
    if october == 'whiringa-a-nuku':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    january = input("""Question 6
January = """).lower()
    if january == 'kohitatea':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    may = input("""Question 7
May = """).lower()
    if may == 'haratua':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    june = input("""Question 8
June = """).lower()
    if june == 'pipiri':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    july = input("""Question 9
July = """).lower()
    if july == 'hongongoi':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    april = input("""Question 10
April = """).lower()
    if april == 'paenga-whawha':
        print("That is correct!")
        points += 1
    else:
        print("That is incorrect sorry")
        point_counter(points)
    last_months = input("Do you want to finish? (Y/N): ").upper()
    if last_months == 'Y':
        point_counter(points)
    elif last_months == 'N':
        extra_months(points)
    else:
        print("That is not an answer")


def point_counter(points):
    if points < 10:
        print("Try to get to Maori days next time. Thanks for playing")
    elif points == 10 or points < 20:
        print("You completed Maori numbers well done")
    elif points == 20 or points < 30:
        print("You completed Maori days amazing job")
    elif points == 30:
        print("You got 100% complete brilliant job")
    else:
        print("Better luck next time")
    game_summary(points)


def extra_nums(points):
    randomly = random.randint(1,5)
    if randomly == 1:
        nine = input("""4 + 5 = """).lower()
        if nine == 'iwa':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomly == 2:
        eight = input("""58 - 50 = """).lower()
        if eight == 'waru':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomly == 3:
        three = input("""754 - 751 = """).lower()
        if three == 'toru':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomly == 4:
        two = input("""35 - 33 = """).lower()
        if two == 'rua':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomly == 5:
        ten = input("""845 - 835 = """).lower()
        if ten == 'tekau':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)


def extra_days(points):
    randomize = random.randint(1,5)
    if randomize == 1:
        tuesday = input("""Second day of the week = """).lower()
        if tuesday == 'ratu':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomize == 2:
        monday = input("""First day of the week = """).lower()
        if monday == 'rahina':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomize == 3:
        wed = input("""Third day of the week = """).lower()
        if wed == 'raapa':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomize == 4:
        tue = input("""Second day of the week = """).lower()
        if tue == 'ratu':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomize == 5:
        wednesday = input("""Third day of the week = """).lower()
        if wednesday == 'raapa':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)


def extra_months(points):
    randomizer = random.randint(1,5)
    if randomizer == 1:
        december = input("""December = """).lower()
        if december == 'hakihea':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomizer == 2:
        november = input("""November = """).lower()
        if november == 'whiringa-a-rangi':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomizer == 3:
        march = input("""The third month = """).lower()
        if march == 'poutu-te-rangi':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomizer == 4:
        february = input("""The second month = """).lower()
        if february == 'hui-tanguru':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)
    elif randomizer == 5:
        october = input("""The tenth month = """).lower()
        if october == 'whiringa-a-nuku':
            print("That is correct!")
            points += 1
        else:
            print("That is incorrect sorry")
            point_counter(points)


def game_summary(points):
    if points >= 2:
        print(f"You got {points} points")
    elif points == 1:
        print(f"You got {points} point")
    else:
        print("Sorry but you didn't get any points")
    exit()


welcome_screen()
