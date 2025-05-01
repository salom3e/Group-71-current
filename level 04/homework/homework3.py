# 4) გაასწორეთ მოცემული კოდები:
#    Fix the following codes:

# 1. name = "Giorgi"
#    print(namme)

# 2. number = 5
#    text = " apples"
#    result = number + text
#    print(result)

# 3. name = liKa
#    name2 = naame + "4"


# 1)
name = "Giorgi"
print(name) #ცვლადის სახელი პრინტში არასწორად ეწერა.

# 2)
number = "5" #ამ ცვლადის მნიშვნელობა იყო ინტეჯერი, შესაბამისად სტრინგს ვერ მიემატებოდა. მისი ტიპი სტრინგად შევცვალე.
text = " apples"
result = number + text
print(result)

#ან 
number = 5
text = " apples"
result = str(number) + text #აქაც იგივე, უბრალოდ ბრჭყალებით არა, str ფუნქციით შევცვალე number ცვლადის მონაცემის ტიპი.
print(result)

# 3)
name = "Lika" #სტინგის ტიპის მონაცემი არ იყო ბრჭყალებში მოქცეული.
name2 = name + "4" #name ცვლადის სახელი არასწორად იყო ჩამოტანილი.