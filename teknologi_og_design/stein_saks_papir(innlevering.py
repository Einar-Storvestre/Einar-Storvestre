options = {"stein":"papir","saks":"stein","papir":"saks"}
while True:
    raw_input = input("stein, saks eller papir?: ")
    if raw_input.islower():
        if raw_input=="stein":
            print("jeg valgte "+(options["stein"]))
        if raw_input=="papir":
            print("jeg valgte "+options["papir"])
        if raw_input=="saks":
            print("jeg valgte "+options["saks"])
    else:
        print(f"du vinner. XOXO jeg valgte ikke {(options[raw_input.lower()])}, du er best")
    unlimited_tries = input("vil du spille på nytt? ja/nei: ")
    if unlimited_tries=="nei":
        print("ok...")
        break
    if unlimited_tries == "ja" or "ja ":
        print("nice")
print("hade")