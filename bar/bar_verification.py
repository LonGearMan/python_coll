# --- в помощь ---
# texts[lang][""]
# .isalpha()
# .isdigit():
# .append
# .remove
# --- в помощь ---
from storage import texts, names, ages, passwrds


def run(lang):
    name = None
    age = None
    good = None
    attemps = 0
    max = 3

    while True:
        text = input(texts[lang]["ask_age"].format(left=max - attemps))

        bukva = False
        cifra = False
        for s in text:
            if s.isalpha():
                bukva = True
            if s.isdigit():
                cifra = True

        if bukva and cifra:
            attemps += 1
            print(texts[lang]["mixed"])
            if attemps >= max:
                print(texts[lang]["too_many"])
                break
            continue
        if bukva:
            attemps += 1
            print(texts[lang]["letters"].format(left=max - attemps))
            if attemps >= max:
                print(texts[lang]["too_many"])
                break
            continue
        try:
            age = int(text)

            if age > 99:
                print(texts[lang]["too_old"])
                attemps += 1
                if attemps >= max:
                    print(texts[lang]["too_many"])
                    break
            elif age >= 18:
                print(texts[lang]["welcome"])
                name = input(texts[lang]["ask_name"])

                bukva2 = False
                cifra2 = False
                for negr2 in name:
                    if negr2.isalpha():
                        bukva2 = True
                    if negr2.isdigit():
                        cifra2 = True
                if cifra2:
                    attemps += 1
                    print(texts[lang]["digits"])
                    if attemps >= max:
                        print(texts[lang]["too_many"])
                        break
                    continue
                if bukva2:
                    print(texts[lang]["success"].format(name=name, age=age))
                    pwd = input(texts[lang]["ask_password"])
                    names.append(name)
                    ages.append(age)
                    passwrds.append(pwd)
                    break
            elif age < 0:
                print(texts[lang]["neg"])
                attemps += 1
                if attemps >= max:
                    print(texts[lang]["too_many"])
                    break
            else:
                attemps += 1
                if attemps >= max:
                    print(texts[lang]["too_many"])
                    break
                good = input(texts[lang]["truth"])
                if good == "0":
                    print(texts[lang]["bye"])
                    break

        except ValueError:
            attemps += 1
            print(texts[lang]["not_a_number"])
            if attemps >= max:
                print(texts[lang]["too_many"])
                break
