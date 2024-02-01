def with_lib():
    import roman

    number = input("Enter a Rome Numeral: ")

    try:
        convert_eq = roman.fromRoman(number)
        if convert_eq >= 5000:
            print("Please enter a lower number.")
        else:
            print(convert_eq)
    except roman.InvalidRomanNumeralError:
        print("Invalid value")

def without_lib_broken():
    romes = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,

        "X": 10,
        "XX": 20,
        "XXX": 30,
        "XL": 40,
        "L": 50,
        "LX": 60,
        "LXX": 70,
        "LXXX": 80,
        "XC": 90,

        "C": 100,
        "CC": 200,
        "CCC": 300,
        "CD": 400,
        "D": 500,
        "DC": 600,
        "DCC": 700,
        "DCCC": 800,
        "CM": 900,

        "M": 1000,
        "MM": 2000,
        "MMM": 3000,
        "M_V": 4000,
        "_V": 5000
    }

    romerals_1 = input("Enter the Rome Numeral: ")
    #romerals_1 = "MMMDCCCLXXXVIII"
    print(f"romerals_1 == {romerals_1}")
    romes_keys = list(romes.keys())

    """
    romerals_len_1 = len(romerals_1)
    last = romerals_len_1 - romerals_len_1 - 1
    revx = romerals_1[-last:]
    print(revx)
    """
    solve = 0
    #while solve == 0:

    romerals_len_1 = len(romerals_1)
    minus_1 = 12
    len_from_1 = romerals_len_1 - minus_1
    print(f"romerals_len_1=={romerals_len_1}")
    print(f"minus_1=={minus_1}")
    print(f"len_from_1=={len_from_1}")
    romerals_after_minus_1 = romerals_1[:len_from_1]
    print(f"romerals_after_minus_1=={romerals_after_minus_1}")

    if romerals_1 in romes_keys:
        print(romes[romerals_1])
    elif romerals_after_minus_1 in romes_keys:
        print(f"{romerals_after_minus_1} == {romes[romerals_after_minus_1]}")
        romerals_2 = romerals_1[len_from_1:]
        romerals_len_2 = len(romerals_2)
        minus_2 = 8
        len_from_2 = romerals_len_2 - minus_2
        romerals_after_minus_2 = romerals_2[:len_from_2]
        if romerals_2 in romes_keys:
            print(f"{romerals_2} == {romes[romerals_2]}")
        elif romerals_after_minus_2 in romes_keys:
            print(f"{romerals_after_minus_2}=={romes[romerals_after_minus_2]}")
            romerals_3 = romerals_2[len_from_2:]
            romerals_len_3 = len(romerals_3)
            minus_3 = 4
            len_from_3 = romerals_len_3 - minus_3
            romerals_after_minus_3 = romerals_3[:len_from_3]
            if romerals_3 in romes_keys:
                print(f"{romerals_3}=={romes[romerals_3]}")
            elif romerals_after_minus_3 in romes_keys:
                print(f"{romerals_after_minus_3}=={romes[romerals_after_minus_3]}")
                romerals_4 = romerals_3[len_from_3:]
                if romerals_4 in romes_keys:
                    print(f"{romerals_4}=={romes[romerals_4]}")
                    solve = 1
                else:
                    print("\n Enter a lower number.")
                    without_lib_broken()
        else:
            print("\n Enter a lower number.")
    else:
        print("\n Enter a lower number.")

def without_lib_quasi_experimental():
    romes = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,

        "X": 10,
        "XX": 20,
        "XXX": 30,
        "XL": 40,
        "L": 50,
        "LX": 60,
        "LXX": 70,
        "LXXX": 80,
        "XC": 90,

        "C": 100,
        "CC": 200,
        "CCC": 300,
        "CD": 400,
        "D": 500,
        "DC": 600,
        "DCC": 700,
        "DCCC": 800,
        "CM": 900,

        "M": 1000,
        "MM": 2000,
        "MMM": 3000,
        "M_V": 4000,
        "_V": 5000
    }

    rome_numeral = input("Please enter Rome Numeral: ")
    if rome_numeral.islower():
        rome_numeral = rome_numeral.upper()
    #rome_numeral = "CCCLXXXVIII"
    romes_keys = list(romes.keys())
    numeral_len = len(rome_numeral)
    if numeral_len == 0:
        print("Please enter a value.")
        exit(without_lib_quasi_experimental())
    #print(f"numeral_len=={numeral_len}")
    check_list = [*rome_numeral]
    if "_" in check_list:
        check_list.remove("_")
    for check in check_list:
        if check not in romes_keys:
            print("Invalid value.")
            exit(without_lib_quasi_experimental())

    solve = 0
    minus_1 = 0
    minus_2 = 0
    minus_3 = 0
    while solve == 0:
        after_minus = rome_numeral[0:numeral_len - minus_1]
        #print(f"after_minus=={after_minus}")
        if after_minus in romes_keys:
            first_key = romes[after_minus]
            #print(f"{after_minus}=={first_key}")
            first_len = len(after_minus)
            #print(f"first_len=={first_len}")
            after_minus_2 = rome_numeral[first_len:numeral_len - minus_2]
            #print(f"after_minus_2=={after_minus_2}")

            if numeral_len - first_len != 0:
                if after_minus_2 in romes_keys:
                    second_key = romes[after_minus_2]
                    #print(f"{after_minus_2}=={second_key}")
                    #print(f"{rome_numeral} == {first_key + second_key}")
                    second_len = len(after_minus_2) + first_len
                    after_minus_3 = rome_numeral[second_len:numeral_len - minus_3]
                    #print(f"after_minus_3=={after_minus_3}")

                    if numeral_len - second_len != 0:
                        if after_minus_3 in romes_keys:
                            third_key = romes[after_minus_3]
                            #print(f"{after_minus_3}=={third_key}")
                            third_len = len(after_minus_3) + second_len
                            after_minus_4 = rome_numeral[third_len:numeral_len]

                            if numeral_len - third_len != 0:
                                if after_minus_4 in romes_keys:
                                    fourth_key = romes[after_minus_4]
                                    print(f"{rome_numeral} == {first_key + second_key + third_key + fourth_key}")
                                    solve += 1
                            else:
                                print(f"{rome_numeral} == {first_key + second_key + third_key}")
                                solve += 1
                        else:
                            minus_3 += 1
                    else:
                        print(f"{rome_numeral} == {first_key + second_key}")
                        solve += 1
                else:
                    minus_2 += 1
            else:
                print(f"{rome_numeral} == {first_key}")
                solve += 1
        else:
            minus_1 += 1

without_lib_quasi_experimental()