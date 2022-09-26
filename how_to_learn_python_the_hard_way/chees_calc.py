def cheese_and_crackers():
    print(f"you have {crackers} crackers and {cheeses} cheeses")
    if crackers > cheeses:  # less cheese then crackers
        print(
            f"""you have an odd number of cheeses,\n in fact you will need to have\n {greater_crackers_math} cheeses on each cracker, in avrage""")
    if cheeses > crackers:  # more cheese then crackers
        print(
            f"""you have an odd number of crackers,\n in fact you will need to have\n {greater_cheeses_math} crackers with one cheese, in avrage""")
    if cheeses == crackers:
        print("this is perfect, balanced as it should be. great job! ")
    # else:
    # print("something is wrong, please call programmer! ")


cheeses = input("how many cheeses do you have?: ")
crackers = input("so how many crackers?: ")

greater_crackers_math = float(cheeses) / float(crackers)
greater_cheeses_math = float(crackers) / float(cheeses)

print(cheese_and_crackers())


def party_people():
    print(
        f"there are {amount_of_persons} coming over!\n each one could eat {persons_divided_by_portions} crackers each ")
    if persons_divided_by_portions < 1:
        print("this will be too cheesy")
    if crackers > cheeses:
        print("a little dry, not enough cheese, but i hope they will be happy! :) ")


amount_of_persons = input("how many is coming to your party?: ")

persons_divided_by_portions = float(crackers) / float(amount_of_persons)

print(party_people())
