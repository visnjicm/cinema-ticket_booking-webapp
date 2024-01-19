import secrets

from SQLClasses import SQLTable


class CreditCard:

    def __init__(self, card_company, number, cvc, card_owner):
        self.card_type = card_company
        self.card_number = number
        self.card_cvc = cvc
        self.card_holder = card_owner

    def validate(self, price):
        pass


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat: str, card: CreditCard):
        seat_db = SeatDB()
        cc_db = CreditCardDB()

        if seat_db.is_free(seat):
            print(f"The preferred seat {seat} is available! :)")
            if cc_db.find_row(card):
                print(f"Found the credit card! Now let's just check your funds.. :)")
                seat_price = seat_db.get_price(seat)
                if cc_db.get_balance(card) > seat_price:
                    print("You have enough money to buy the ticket! :)")

                    with open('ticket.txt', 'w') as file:
                        file.write(f"MOVIE TICKET\n\n\n")
                        file.write(f"Name: {self.name}\nSeat: {seat}\nCost:{seat_price}\n\n")
                        file.write(f"Ticket ID/Confirmation: {secrets.token_urlsafe(12)}")

                    seat_db.occupy(seat)
                    cc_db.change_balance(seat_price, card)

                else:
                    print("Ticket purchase declined. Insufficient funds. :(")
            else:
                print("Credit card not found. :(")
                print("Purchase unsuccessful. Closing app.")
        else:
            print(f"The seat {seat} is not available! :(")
            print("Purchase unsuccessful. Closing app.")

    # seat_db = SeatDB()
    # if seat_db.is_free(pref_seat):
    #     print(f"The preferred seat {pref_seat} is available! :)")
    #     # 1.then we need to check if the user's card information is correct or not
    #     # 2.if it's correct then check whether the user has enough money on their card to purchase the seat they want
    #     # given the price of the seat
    #     # 3.if they have enough money, generate a pdf copy of the ticket and give it to the user
    # else:
    #     print(f"The seat {pref_seat} is not available! :(")
    #     print("Purchase unsuccessful. Closing app.")
    #     exit()


class SeatDB(SQLTable):

    def __init__(self):
        # pass
        super().__init__('cinema.db', 'Seat')

    def _fetch_seat_row(self, seat_id):
        self.sql_expression = f'SELECT * FROM {self.table_name} WHERE seat_id = ?'
        self.sql_parameters = (seat_id,)
        self.cursor.execute(self.sql_expression, self.sql_parameters)
        self.row = self.cursor.fetchone()

    def get_price(self, seat_id):
        self._fetch_seat_row(seat_id)
        return self.row[2]

    def is_free(self, seat_id):
        self._fetch_seat_row(seat_id)
        return False if self.row[1] == 1 else True

    def occupy(self, seat_id):
        if self.is_free(seat_id):
            self.sql_expression = f'UPDATE {self.table_name} SET taken = 1 WHERE seat_id = ?'
            self.sql_parameters = (seat_id,)
            self.cursor.execute(self.sql_expression, self.sql_parameters)
            self.conn.commit()
            self.close_and_reopen_sql_connection()
            print(f"Seat {seat_id} occupied successfully.")
        else:
            print(f"Cannot occupy {seat_id}. Seat is already taken!")


class CreditCardDB(SQLTable):
    # database = "banking.db"
    card_number = 000000000
    card_cvc = 000
    card_holder = ""
    card_balance = 000
    cc_lst = []

    def __init__(self):
        super().__init__('banking.db', 'Card')
        self.sql_expression = f'SELECT * FROM {self.table_name}'
        self.sql_parameters = ()
        self.cursor.execute(self.sql_expression, self.sql_parameters)
        self.cc_lst = self.cursor.fetchall()

    # def _fetch_card_row(self, card_number):
    #     self.sql_expression = f'SELECT * FROM {self.table_name} WHERE  = ?'
    #     self.sql_parameters = (card_number,)
    #     self.cursor.execute(self.sql_expression, self.sql_parameters)
    #     self.row = self.cursor.fetchone()

    def get_balance(self, credit_card: CreditCard):
        return self.find_row(credit_card)[4]

    def find_row(self, credit_card: CreditCard):
        for entry in self.cc_lst:
            if int(credit_card.card_number) == int(entry[1]) \
                    and int(credit_card.card_cvc) == int(entry[2]) \
                    and str(credit_card.card_holder.lower()) == str(entry[3]).lower():
                return entry
        return []

    def change_balance(self, amount, credit_card: CreditCard):
        self.sql_expression = f'UPDATE {self.table_name} SET balance = balance-? WHERE number = ?'
        self.sql_parameters = (amount, credit_card.card_number)
        self.cursor.execute(self.sql_expression, self.sql_parameters, )
        self.conn.commit()
        self.close_and_reopen_sql_connection()
