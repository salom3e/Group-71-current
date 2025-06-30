# 2) რას გამოიტანს ეს კოდი?
products = ["apples", "oranges", "bananas", "Melon"]
products[3] =  "lime"
print(products[2])

# ეს კოდი გამოიტანს "bananas"-ს. სიის მესამე ინდექსის მქონე მნიშვნელობას შეუცვალეს ძველი მნიშვნელობა, მაგრამ ბოლოს print-ში 
# ამ ინდექსის მქონე ელემენტი არ გამოუძახებია


# 3) გამოიტანეთ მოცემული ცვლადიდან სიტყვა GOA. (Output ნდა იყოს space-ების გარეშე)

sentence = "GOA is the best"

print(sentence[0:3])

# არ გააკეთოთ ასე:
# print(sentence[0])
# print(sentence[1])
# print(sentence[2])

# ან ასე:
# print(sentence[0]),print(sentence[1]),print(sentence[2])



# 4) ახსენით რატომ გამოიტანს მოცემული კოდი ერორს?

month = "august" 
month[0] = "A"

# კოდი გამოიტანს ერორს, რადგან სიებში string ელემენტი უცვლელია, ანუ მას მნიშვნელოვას ვერ შევუცვლით

