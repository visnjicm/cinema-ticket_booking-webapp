from cinema import CreditCard, User

if __name__ == "__main__":
    full_name = input("Your full name?:")
    pref_seat = input("Preferred seat number?:")
    card_type = input("Your card type?:")

    card_number = input("Your card number?:")
    card_cvc = input("Your card cvc?:")
    card_holder = input("Card holder name?:")

    user = User(full_name)
    user.buy(pref_seat, CreditCard(card_type, card_number, card_cvc, card_holder))

    # 1.tell whether purchase was succesful or not

    # 3.if purchase successful, reflect the fact that the user now occupies a seat number <seat number that
    # was found available>, reflect the change on the cinema db (taken = 1 means seat is taken, and vice versa)
    # 4.decrease balance on person's card info in banking db to reflect ticket purchase
    # 5.generate sample.pdf file -> PDF file that containes digital ticket mockup

    # 6. now, if someone runs the program again, and tries to take a seat that is already occupied, the program will not
    # make any changes to the db files, and just print to the user the fact that the seat is taken

    # 7. If the person enters the wrong card details, then the program should not make any changes to the db's, and
    # return the fact that there was a problem with the card (incorrect information was put)
