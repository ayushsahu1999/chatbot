import re
import random
# FOR TAKING TASKS
lib_name = [["name", "who"], ["hello", "hi"]]
lib_intro = [["form", "forms"], ["register", "regester"], ["issue", "issues", "isue"],[""]]
lib_form = [["driving lisence", "driving liscence","driving licence"], ["adhaar card", "adhar card"]]
lib_reg = [["voter id regester","voter id register", "voter id"],["request for change mobile number in adhaar card"],["mobile number","mobile no."]]
print("Hi, sir")
print("I am S_Bot \n"
      "I can fill you forms , Register with Queries ")
print("Select 1)Forms\n2)Register\n3)Issues")
intro_in = input("What can i do!\n")
wordList=re.sub("[^\w]"," ", intro_in).split()
trigger = int(0)
lion = int(0)
tiger = int(0)
abs = int(0)
for i in lib_intro:
    for j in i:
        for k in wordList:
            if k.lower() == j:
                trigger = lib_intro.index(i)
                break
for p in lib_name:
    for q in p:
        for r in wordList:
            if r.lower() == q:
                abs=1
                tiger = lib_name.index(p)
                break

process_choices_name = [["My name is dot_bot\n", "Hey! dot_bot is my name, Nice to meet you", "dot_bot is my name"],["oh hi!", "hi there!", "namaste", "bonjour"]]
process_choices_fo = [
    ["Welcome to the form filling wizard , \n I will Assist You ",
     "Welcome , I am happy to assist you with the form filling\n",
     "Welcome , Let's fill a form\n"],
    ["Sry for the troubles caused , Let's proceed to your registration ",
     "State the category for your Query"],
    ["Which issue do you want, I will assist you\n","Okay tell me!\n",
     "Lets help"]]
process_choices_fr = [
    ["I will help you\n", "Fill the form to help you\n"],
    ["Adhaar card form\n", "Fill the form to get adhaar card\n"]]
process_choices_reg = [
    ["Which area do you belong?\n", "why are you alive\n"],
    ["tell me your adhaar card\n", "adhaar card!"],
    ["tell me your mobile number","mobile number!"]
]
while abs==1 :
    abs=2
    for p in lib_name:
        for q in p:
            for r in wordList :
                if r.lower == q:
                    tiger = lib_name.index(p)
                    break
    print(random.choice(process_choices_name[tiger]))
    intro_in=input("")
    wordList = re.sub("[^\w]", " ", intro_in).split()
    for p in lib_name:
        for q in p:
            for r in wordList:
                if r.lower()==q :
                    abs=1
                    break

for i in lib_intro:
    for j in i:
        for k in wordList:
            if k.lower() == j:
                trigger = lib_intro.index(i)
                break

print(random.choice(process_choices_fo[trigger]))
sad = ["Enter the name", "Enter your city ", "Enter your state", "Enter pincode of your area",
           "Enter your locality", "Enter your mobile number"]
ans = []
if trigger == 0 :
    intro_in = input("Which form do you want\n")
    for k in lib_form:
        for l in k:
            if intro_in.lower() == l:
                lion = lib_form.index(k)
                break
    print(random.choice(process_choices_fr[lion]))
    for sd in sad:
        ans.append(input(sd))
    for x in range(6):
        print("You have applied for " + intro_in + "\n" + sad[x] + " -> " + ans[x])
    check = input("Do you want to continue?[yes/no]")
    if check == "yes":
        print("Thankyou for using our service!")
    elif check == "no":
        print("We can cancelled your request")
    else:
        print("please enter right choice")


elif trigger == 1 :
    intro_in = input("Which registration do you want\n")
    for k in lib_reg:
        for l in k:
            if intro_in.lower() == l:
                lion = lib_reg.index(k)
                break
    print(random.choice(process_choices_reg[lion]))
    for sd in sad:
        ans.append(input(sd))
    for x in range(6):
        print("You have applied for " + intro_in + "\n" + sad[x] + " -> " + ans[x])
    check = input("Do you want to continue?[yes/no]")
    if check == "yes":
        print("Thankyou for using our service!")
    elif check == "no":
        print("We can cancelled your request")
    else:
        print("please enter right choice")

else :
    print("l")




