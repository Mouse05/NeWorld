import random
import sys

def play_rock_paper_scissors(user_input):
    alien_input = random.randint(0, 2)
    rock_paper_scissors = ["rock", "paper", "scissors"]
    if rock_paper_scissors[alien_input] == "rock":
        if user_input == "scissors":
            print("You lose!")
            input_c = input("Please select rock, paper, or scissors")
            play_rock_paper_scissors(input_c)
        if user_input == "rock":
            print("You tie!")
            input_c = input("Please select rock, paper, or scissors")
            play_rock_paper_scissors(input_c)
        if user_input == "paper":
            print("You win!")
    if rock_paper_scissors[alien_input] == "scissors":
        if user_input == "paper":
            print("You lose!")
            input_c = input("Please select rock, paper, or scissors")
            play_rock_paper_scissors(input_c)
        if user_input == "scissors":
            print("You tie!")
            input_c = input("Please select rock, paper, or scissors")
            play_rock_paper_scissors(input_c)
        if user_input == "rock":
            print("You win!")
    if rock_paper_scissors[alien_input] == "paper":
        if user_input == "rock":
            print("You lose!")
            input_c = input("Please select rock, paper, or scissors")
            play_rock_paper_scissors(input_c)
        if user_input == "paper":
            print("You tie!")
            input_c = input("Please select rock, paper, or scissors")
            play_rock_paper_scissors(input_c)
        if user_input == "paper":
            print("You win!")

class character:
    def __init__(self, name, age, sex, knowledge):
        self.name = name
        self.age = age
        self.sex = sex
        self.knowledge = knowledge

print("\n\n *Yawn* You wake up in the morning, confused about where you are. Ah. You remember. You're on the PB&J 1600, humanity's first ship to the one of exoplanets with life detected on it! Now, you start to slowly orient yourselves to your surroundings...")

name = input("What is your character's name? ")
sex = input("What are your character's pronouns? ")
age = input("What is your character's age? ")
value = False
while value == False:
    try:
        age = int(age)
        value = True
    except:
        print("Please enter a valid age: ")
        age = input("What is your character's age? ")

    

knowledge = 0
notes_list = []

char = character(name, age, sex, knowledge)

print("Is this what your character's information is supposed to display? ")
print("Name: " + char.name + " Age: " + str(char.age) + " Pronouns: " + char.sex)
confirmation = input("Please enter 'no' if the information is incorrect. Otherwise, enter anything. ")
if confirmation == "no" or confirmation == "No":
    while confirmation == "no" or confirmation == "No":
        name = input("What is your character's name? ")
        age = input("What is your character's age? ")
        sex = input("What are your character's pronouns? ")
        print("Is this what your character's information is supposed to display? ")
        print(char.name, char.age, char.sex)
        confirmation = input("Please enter yes or no")
else:
    print("Perfect, let's continue!")

planet = input("Please pick a planet from the following (Ishmorz, Smayup, Hularu): ")
if planet != "Ishmorz" and planet != "Smayup" and planet != "Hularu":
    planet = input("Please enter a planet: ")
if planet == "Ishmorz":
    print("\n\n Zhooombbbb. Your spaceship lands on the first exoplanet. Your computer displays some information: \n\n Flight Log, Day 6432: \n\n Arrival on planet #1, Ishmorz. Native population: Ishmese. Planetary structure: very few land-based structures, largely oxygen based atmosphere but all major cities and civilizations underwater. \n\n End of flight log. Have a nice trip, Human " + char.name)
    
    print("\n\n Shhhhhhh. Your hatch opens, and you almost fall into the water below. You realize that the only thing that prevented you from sinking to your doom is a tiny flotation device attached to the PB&J (ironically, shaped like a pickle). You put on your diving suit, and drop into the water. \n\n You see a magnificent city, floating in the middle of the ocean, with neighborhoods made of a bubbly, gelatinous substance, shaped in bubbles. You are greeted by two Ishmese representatives, and are taken into a glowing yellow orb, to meet their king.")

    print("As you talk with the King, you can't help to notice how clear the water is. On Earth, the water is usually extremely murky, but here, even hundreds of feet into the ocean, it's as clear as on the surface. What do you think is causing this?")

    print("1. Lack of pollution 2. Magic 3. Dust-cleaning ships")

    input_a = input("Please enter a value: ")

    if input_a == "1":
        print("You are correct! After taks with the Ishmese king, you realize that they keep their water clean by preventing pollution.")
        knowledge += 1
        notes_list.append("Solve pollution to prevent oceanic pollution")
    else:
        print("The correct answer is 1.")

    print("\n You also notice that the oceanic creatures that the Ishmese keep are healthier. This is because of a lack of pollutants in the water. When pollutants are present, it can magnify up the foodchain, in a process called...")

    print("1. Biomagnification, 2. Ecoterrorism, 3. Magic")
    input_b = input("Please enter a value: ")
    if input_b == "1":
        print("You are correct!")
        knowledge += 1
        notes_list.append("Preventing pollution helps save species")
    else:
        print("The correct answer is 1")
        
    print("\n You have learned about the issues that the Ishmese were able to solve for with their amazing tecnology. However, they wish for you to provide a peice of knowledge from Earth, with a game. The head Ishmese laughs heartily. The sonar-gilled population loved games! So, you challenge them to a game of rock-paper-scissors, a simple game that can be taught anywhere!")

    input_c = input("Please pick rock, paper, or scissors.")

    play_rock_paper_scissors(input_c)

    print("Now that we've had some fun, let's go home!")
elif planet == "Smayup":
    print("\n\n Zhooombbbb. Your spaceship lands on the second exoplanet. Your computer displays some information: \n\n Flight Log, Day 6432: \n\n Arrival on planet Smayup. Native population: Smayites. Planetary structure: very few land-based structures, largely oxygen based atmosphere but all major cities and civilizations underground. \n\n End of flight log. Have a nice trip, Human " + char.name)
    
    print("\n\n Shhhhhhh. Your hatch opens, and you finally stand on solid Earth. You look around at the surprisingly lush land. But there seems to be nothing around! You see a tunnel and decide to explore. \n\n You see a magnificent empire, built of our Earth, with neighborhoods made of a rocky, muddly substance. You are greeted by two Smayite representatives, and are taken into a massive rock castle, to meet their king.")

    print("As you talk with the King, you can't help to notice how fresh the air smells, even underwater. On Earth, the air smells smoky even on the surface, but here, even hundreds of feet underground, it's as clear as on the surface. What do you think is causing this?")

    print("1. Lack of factories 2. Magic 3. Carbon capturing bugs")

    input_a = str(input("Please enter a value: "))

    if input_a == "1":
        print("You are correct! After talks with the Smayite leader, you realize that they keep their air clean by preventing factory pollution.")
        knowledge += 1
        notes_list.append("Solve factory pollution to keep cleaner air.")
    else:
        print("The correct answer is 1")
            
    print("\n You also notice that the planet is much cooler than on Earth. On Earth, _______ makes the excess carbon dioxice in the atmosphere heat the Earth up significantly")

    print("1. Eri effect, 2. Greenhouse effect, 3. Carbon Cycle")
    input_b = input("Please enter a value: ")
    if input_b == "2":
        print("You are correct!")
        knowledge += 1
        notes_list.append("Preventing pollution helps save species")
    else:
        print("The correct answer is 2")
        
    print("\n\n You have learned about the issues that the Smayites were able to solve for with their amazing technology. However, as an extremely shy and recluse species, they wish for you to pass a lie-detector test first!")

    input_c = input("Smayite king: what is your name? ")
    if input_c != char.name:        
        print("You are an imposter! Please leave.")
        print("You leave the planet dissapointed that they took away your knowledge.")
        sys.exit()
    input_d = input("Smayite king: what is your age? ")
    if input_c != char.age:
        print("You are an imposter! Please leave.")
        print("You leave the planet dissapointed that they took away your knowledge.")
        sys.exit()
    input_e = input("Smayite king: what is your gender? ")
    if input_c != char.sex:
        print("You are an imposter! Please leave.")
        print("You leave the planet dissapointed that they took away your knowledge.")
        sys.exit()

    print("Congratulations, you convined the king you are not an imposter. Let's go home!")
elif planet == "Hularu":
    print("\n\n Zhooombbbb. Your spaceship lands on the second exoplanet. Your computer displays some information: \n\n Flight Log, Day 6432: \n\n Arrival on planet Hularu. Native population: Hularians. Planetary structure: very surface-based, with cities in the mountains. \n\n End of flight log. Have a nice trip, Human " + char.name)
    
    print("\n\n Shhhhhhh. Your hatch opens, and you finally stand on solid Earth. You look around at the high altitudes and the seemingly unforgiving atmosphere. You see a city in the distance put on your oxygen mask, and move towards it. \n\n You see a magnificent city, built of plants, with neighborhoods made of a plants. You are greeted by two Hularian representatives, and are taken into a cave in the mountain, to meet their king.")

    print("As you talk with the King, you can't help to notice how abundant plants are. On Earth, On Earth, plants and such a lush environment is rare to come by. What do you think is causing this?")

    print("1. Deforestation 2. Magic 3. Plant seeds from above")

    input_a = str(input("Please enter a value: "))

    if input_a == "1":
        print("You are correct! After talks with the Hularian leader, you realize that they keep their plants by preserving them.")
        knowledge += 1
        notes_list.append("Preserve plants by preventing deforestation.")
    else:
        print("The correct answer is 1.")
        
    print("\n You also notice that the air is much fresher than that of Earth. On Earth, the lack of trees results in the loss of a...")

    print("1. Carbon releaser, 2. Carbon cycle, 3. Carbon sink")
    input_b = input("Please enter a value: ")
    if input_b == "3":
        print("You are correct!")
        knowledge += 1
        notes_list.append("Planting trees decreses amount of carbon dioxide.")
    else:
        print("The correct answer is 3")
        
    print("\n You have learned about the issues that the Hularians were able to solve for with their amazing technology. However, as an agreiculture based species, they want you to plant some trees!")

    input_c = str(input("What plant do you want to plant? 1. Wheat, 2. Corn, 3. Potatoes "))
    if input_c == "1":
       input_d = input("Please enter 50 L of water to the field *enter 'water field'*.")
       if input_d == "water field":
           input_e = input("Please sow the seeds! *enter 'sow'* ")
           if input_e == "sow":
               print("Now, we wait! ... ... ...")
               print("You have planted wheat!")
    if input_c == "1":
        input_d = input("Please enter 25 L of water to the field *enter 'water field'*. ")
        if input_d == "water field":
            input_e = input("Please sow the seeds! *enter 'sow'* ")
            if input_e == "sow":
                print("Now, we wait! ... ... ...")
                print("You have planted corn!")
    if input_c == "1":
        input_d = input("Please enter 15 L of water to the field *enter 'water field'*. ")
        if input_d == "water field":
            input_e = input("Please sow the seeds! *enter 'sow'* ")
            if input_e == "sow":
                print("Now, we wait! ... ... ...")
                print("You have planted potatoes!")
    
    print("Congratulations, you convinced the king that you are a great gardener! Now, to return home!")

print("You return from your trip, with the following knowledge: ")
for note in notes_list:
    print(note)

print("Commander " + char.name + "we thank you for you contribution to society! We shall take your contributions for the environment seriously!")