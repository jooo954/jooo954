from time import sleep as s
from random import choice as c

from docutils.nodes import paragraph

story = {
    "description 1":[
        "You find yourself standing in an open field, filled with grass and yellow wildflowers.",
        "You are lost now and you want to get back to your house !",
        "Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.",
        "You found a wood and you enter it and then you found a house and a cave.",
        "The Best Score In These Game Is 500 GOOD LUCK",
    ],
    "back from the cave":[
        "You return back to the open field"
    ],
    "get into the house" : {
        "g-t-h description":["You heard a horror giggles from the house",
                       "and a woman says some spells and cooking something"],
        "knock the door":{
            "ktd description" : [
                [
                    "You knocked the door and wait for 15 minutes !!",
                    "You knocked the door and wait for 1 hour !! ('Why you still standing there for 1 hour ??')"
                ],
                    "An old woman opened the door to you and she looks angry",
                    "She shouted on you and tell you what do you want ??",
                    "You say iam lost here i want you to tell me how to get back to my house",
                    "She smiled a horror smile and tell you get in i will serve you a food and a drink",
                    "You get in and then she lock the door and the fight is start between you and her"
            ],
            "cast spell":{
                "have new magic stick":[
                    "You fight hard and cast a strong spells",
                    "She cast a very strong spell that want to turns you to a frog",
                    "You Defend very well because of you new magic stic",
                    "You finish her with the strongest spell the humans ever knows !!",
                    "You Win !!"],
                "don't have new magic stick":[
                    "You do your best but your old magic stick doesn't help you",
                    "She turns you to frog from her first spell ! !",
                    "She start cooking you and you are now the meal.('The End')",
                    "You Loos !!"
                ],
            },


        },
        "run away":[
            "You run so fast but she see you and start running after you",
            "You still running and your heart beats starts glow up",
            "She get tired from you, you are so fast",
            "You save your life from this bad woman and you at least still alive ('The End') "
        ]
    },
    "get into the cave":{
        "first time":[
            "You found the cave is very small from inside",
            "You see a shining thing in a lack inside the cave",
            "You get it and you realise that it's a new strong magic stick",
            "You get it and go out of the cave."
        ],
        "not first time":[
            "Nothing new the cave is empty after taking the new magic stick"
        ]
    },
}
choices = {
    "main choices":{
        1:"Go to the house",
        2:"Peer into the cave"}
    ,
    "home choices":{
        "main":{
            1:"Knock The Door",
            2:"Run Away"
        },
        "branch":{
            1:"cast a spell to the wick",
            2:"run away"
        }
    }
}
def get_item(dictionary,target_key):

    if target_key in dictionary:
        return dictionary[target_key]
    else:
        for value in dictionary.values():
            if isinstance(value, dict):
                result = get_item(value, target_key)
                if result is not None :
                    return result
new_weapon = False
main_choices = choices["main choices"]
home_choices = get_item(choices, "main")
fight_choices = get_item(choices, "branch")
h_n_m_s = get_item(story, "have new magic stick")
d_n_m_s = get_item(story, "don't have new magic stick")

description = list(story["description 1"])
first_choice = [get_item(story,"g-t-h description"), # return []
                get_item(story,"get into the cave")]# return {}
second_choice = [get_item(story,"knock the door"),# return {cast spell, run away}
                 get_item(story,"run away")]# return []
third_choice = [get_item(story,"cast spell"),# return {have new magic stick,
                # don't have new magic stick }
                get_item(story,"run away")]# return []



def print_pause(story):
    time_choices =[0.1, 0.2, 0.3, 0.4, 0.5]
    s(c(time_choices))
    print(story)
    s(c(time_choices))


def h_t_e(choice, score, new_weapon): # home to end of the game
    p_home_choices()
    choice = choice_taker()
    knock_or_runaway_choice = k_o_r(choice, score)
    if choice == 2:
        if knock_or_runaway_choice == 'y':
            score = 0
            main(score)
        elif knock_or_runaway_choice == "n":
            print("Thanks For Playing my game")
    f_o_r(choice, new_weapon, score)


def start_place():
    for sentence in description:
        print_pause(sentence)
    for key, value in main_choices.items():
        print_pause(f"{key}.{value}")
    choice = choice_taker()
    return choice

def p_home_choices():
    paragraph = home_choices
    for key , value in paragraph.items():
        print_pause(f"{key}.{value}")

def k_o_r(choice, score): # knock the door or run away
    if choice == 1:
        paragraph = get_item(story, "ktd description")
        print_pause(c(paragraph[0]))
        for p in paragraph[1:]:
            print_pause(p)
    if choice == 2:
        paragraph = second_choice[1]
        for p in paragraph:
            print(p)
        print(f"your score is {score} P\n")
        restart = input("Enter 'y' to restart or 'n' to exite")
        return restart.lower()


def f_o_r(choice, new_weapon, score): # fight or run away
    if choice == 1:
        seniros = fight_choices
        for key , value in seniros.items():
            print_pause(f"{key}.{value}")
        choice = choice_taker()
        if choice == 1:
            if new_weapon:
                paragraph = h_n_m_s
                score += 400
                for i in paragraph:
                    print_pause(i)
                print(f"\nYour score is the best your score is {score}")
            else:
                paragraph = d_n_m_s
                score = 0
                for i in paragraph:
                    print_pause(i)
                print(f"\nYour score is the worst your score is {score}P\nbecause of your fear")
            play_again()

    if choice == 2:
        paragraph = second_choice[1]
        for p in paragraph:
            print(p)
        print(f"your score is {score} P\n")
        restart = input("Enter 'y' to restart or 'n' to exite")
        return restart.lower()




def g_t_c (score, cave_entries): # go to the cave
    cave_entries += 1
    if cave_entries == 1:
        score += 100
        paragraph = get_item(first_choice[1], "first time")
        for p in paragraph:
            print_pause(p)
    else:
        paragraph = get_item(first_choice[1], "not first time")
        for p in paragraph:
            print_pause(p)
    back_form_the_cave(cave_entries, score)
    return [True, cave_entries]

def play_again():
    play_again = input("'y' => play again , 'n' => exite\n=>")
    current_choices = ['y', 'n']
    if play_again.lower() in current_choices:
        if play_again.lower() == "y":
            print("Enjoy the game\n")
            main(0)
        if play_again.lower() == "n":
            print("Thanks for playing\n")
def back_form_the_cave(cave_entries, score):
    paragraph = get_item(story, "back from the cave")
    for i in paragraph:
        print_pause(i)
    for key, value in main_choices.items():
        print(f"{key}.{value}")
    choice = choice_taker()
    desiction_making(first_choice, choice, cave_entries, score, True)
    return choice

def choice_taker():
    choice = input("Please enter 1 or 2\n=>")
    while choice.isdigit() == False:
        print("please enter numbers only")
        choice = input("Please enter 1 or 2\n=>")
    return int(choice)


def run_away(score):
    paragraph = get_list(story, "run away")
    for i in paragraph:
        print(i)


def desiction_making(context, choice, cave_entries, score, new_weapon):
    result = context[choice - 1]
    if isinstance(result, list):
        for i in result:
            print(i)
        h_t_e(choice, score, new_weapon)



    elif isinstance(result, dict):
        if context == first_choice:
            cave_results = g_t_c(score, cave_entries)
            new_weapon = cave_results[0]
            cave_entries = cave_results [1]
            print("\n")
            return [new_weapon, cave_entries]



def main(score):
    new_weapon = False
    cave_enteries = 0
    choice = start_place()
    result = desiction_making(first_choice, choice, cave_enteries, score, new_weapon)
    if choice == 2:
        new_weapon = result[0]
        cave_enteries = result [1]





score = 0



main(score)