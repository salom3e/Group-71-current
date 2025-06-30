# 1) სიტყვა "Motorcycle"-იდან Slicing-ის მეშვეობით გამოიტანეთ ცალკე "Motor" და ცალკე "cycle"

word = "Motorcycle"
print(word[:5])
print(word[5:])

# 2) fruits = ["Mango", "Melon", "Cherry", "Pear", "Watermelon"]

# მოცემული სიიდან გამოიტანეთ ელემენტები - Cherry, Pear, Watermelon.

fruits = ["Mango", "Melon", "Cherry", "Pear", "Watermelon"]
slicing = fruits[2:5]
print(slicing)


# 3) colors = ["red", "green", "blue", "black", "White", "Brown"]

# მოცემული სიიდან გამოიტანეთ მხოლოდ red, green, blue

colors = ["red", "green", "blue", "black", "White", "Brown"]
slicing = colors[:3]
print(slicing)



