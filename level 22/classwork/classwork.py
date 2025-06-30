# 2) ცვლადში შეინახეთ თქვენი გვარი. შემდეგ მომხმარებელს შემოატანინეთ თავისი გვარი. თუ თქვენი გვარები დაემთხვევა გამოიტანეთ "Our surnames are similar", სხვა შემთხვევაში "Our surnames are not similar"

my_surname = "Maisuradze"
user_surname = input("Enter your surname: ")

if my_surname == user_surname:
    print("Our surnames are similar")
else:
    print("Our surnames are not similar")


# 3) ცვლადში შეინახეთ თქვენი სიმაღლე. მომხმარებელსაც შეეკითხეთ მისი სიმაღლე.

# • თუ შენ უფრო მაღალი ხარ გამოიტანე: "I'm taller than you."

# • თუ მომხმარებელი უფრო მაღალია გამოიტანე: "You're taller than me"

# • თუ ტოლი სიმაღლეების ხართ, მაშინ დაბეჭდეთ "We have equal heights".

my_height = 1.60
user_height = float(input("Enter your height: "))

if my_height > user_height:
    print("I'm taller than you")
elif user_height > my_height:
    print("You're taller than me")
elif user_height == my_height:
    print("We have equal heights")
else:
    print("Wrong number")
