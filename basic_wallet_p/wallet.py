import os
import sys

import requests

# Global Vars
node = "http://localhost:5000"
quit_commands = ["quit", "Quit", "q", "QUIT"]

# Welcome
print("")
print("Welcome to your wallet")
print("")
print("Please enter your id:")
print("")

user_id = input()+"\n"

print("")
print(f"Welcome to your wallet {user_id[:-1]}!")
print("")
print("Type 'help' for help!")
print("")


# Take user input
command = input()


# Functionality
while command not in quit_commands:
    # Help
    if command == "help":
        print("")
        print("Commands:")
        print("")
        print("'balance': show your current balance")
        print("'help': show list of commands")
        print("'id': Change your id")
        print("'transactions': show your transactions")
        print("'quit': exit your wallet")
        print("")

        # New command
        command = input()


    # Change id
    elif command == "id":
        print("")
        print(f"Current ID: {user_id[:-1]}")
        print("")
        print("Please enter a new id:")
        print("")
        user_id = input()+"\n"
        print("")
        print(f"New ID: {user_id[:-1]}")
        print("")

        # New command
        command = input()


    # Get current balance
    elif command == "balance":
        # Get transaction data
        req = requests.get(url=node + "/chain")

        try:
            data = req.json()
        except ValueError:
            print("Error:  Non-json response")
            print("Response returned:")
            print(req)
            print("")
            command = input()

        chain = data['chain']

        # Instantiate & Calculate Balance
        balance = 0

        for block in chain:
            # Get the transactions
            transactions = block['transactions']
            
            for transaction in transactions:
                if transaction['sender'] == user_id:
                    balance -= transaction['amount']
                elif transaction['recipient'] == user_id:
                    balance += transaction['amount']

        # Display Balance
        print("")
        print(balance)
        print("")

        # New command
        command = input()


    # Get list of transactions
    elif command == "transactions":
        # Get transaction data
        req = requests.get(url=node + "/chain")

        try:
            data = req.json()
        except ValueError:
            print("Error:  Non-json response")
            print("Response returned:")
            print(req)
            print("")
            command = input()

        chain = data['chain']

        print("")
        for block in chain:
            # Get the transactions
            transactions = block['transactions']
            
            for transaction in transactions:
                if transaction['sender'] == user_id:
                    print(f"Sent: {transaction['amount']}")
                elif transaction['recipient'] == user_id:
                    print(f"Recieved: {transaction['amount']}")
        print("")

        command = input()

    # Another help for typos
    else:
        print("")
        print("Sorry dum dum, that's not a command")
        print("")
        print("Commands:")
        print("")
        print("'balance': show your current balance")
        print("'help': show list of commands")
        print("'id': Change your id")
        print("'transactions': show your transactions")
        print("'quit': exit your wallet")
        print("")

        # New command
        command = input()
# Quit