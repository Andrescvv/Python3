def run():
    LIMIT = 1000
    counter = 0
    potency_2 = 2**counter

    while potency_2 < LIMIT:
        print(f"2 to the {counter} equals to {potency_2}")
        counter += 1
        potency_2 = 2**counter

# def run_2():
#     LIMIT = 1000
#     counter = 0
#     potency_2 = 2**counter
    
#     # # Este codigo no funciona
#     # for potency_2 in range(LIMIT):
#     #     print(f"2 to the {counter} equals to {potency_2}")
#     #     counter += 1
#     #     potency_2 = 2**counter

def run_3():
    for counter in range(1000):
        if counter % 2 != 0:
            continue
        print(counter)

    for i in range(10):
        if i == 7:
            break
        print(i)

    counter = 0

    while counter <= 100:
        if counter % 2 != 0:
            print(f"{counter} Impar")
        elif counter % 2 == 0: 
            print(f"{counter} Par")
        counter += 1

if __name__ == "__main__":
    run()
    # run_2()
    run_3()
    


