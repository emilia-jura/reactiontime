from guizero import App, Box, PushButton, Text, ListBox, ButtonGroup, Window, TextBox
import random
font = "Secular One"

# Global widgets
app2 = None
round_num = None
start = None
subtitle3 = None
subtitle4 = None
age = None
username = None
instruct1 = None
faketime = None
counter = 0
running = False
rect = None
time_dis = None
time = random.randint(1500, 4000)
saveb = None
# each player's data is in the order: (round1 time, round2 time, round3 time, username, age)
overall_scores = []
uage = None
user = None
# this list if organized as [average, name, age]
averages = []
age_list = None
window1 = None


# global blocks
block11 = None
block12 = None
block13 = None
block14 = None
block15 = None
block16 = None
block17 = None
block18 = None
block19 = None
block20 = None
block21 = None
block22 = None
block23 = None
block24 = None
block25 = None
block26 = None


# leaderboard age-specific display
def notif(value):
    global app, overall_scores, averages, age_list, window1
    age_list = []
    for i in averages:
        if str(i[2]) == value:
            age_list.append(i)
    # age list organized as [average, name , age] but only of one age group
    age_list.sort()
    display_list = []
    # display list is organized as [name, name]
    for i in age_list:
        name = i[1]
        display_list.append(name)
    window1 = Window(app, title="Age " + str(value))
    msg = Text(window1, text="Top players:")
    top = ListBox(window1, items=display_list, command=top6)
    top.bg = "white"
    top.text_color = "#4B1D3F"
    top.text_size = 15
    top.font = font
    msg.text_color = "#4B1D3F"
    msg.font = font
    msg.text_size = 25
    window1.bg = "#D4F4DD"


def top6(value):
    global age_list, window1, overall_scores
    avg_time = "N/a"
    fast_time = "N/a"
    slow_time = "N/a"

    for i in age_list:
        if i[1] == value:
            avg_time = i[0]
            break
    for i in overall_scores:
        if i[3] == value:
            for w in i:
                if i[0] < i[1] and i[0] < i[2]:
                    fast_time = i[0]
                    break
                elif i[1] < i[0] and i[1] < i[2]:
                    fast_time = i[1]
                    break
                elif i[2] < i[0] and i[2] < i[1]:
                    fast_time = i[2]
                    break
                elif i[0] == i[1] and i[0] < i[2] or i[0] < i[1] and i[0] == i[2]:
                    fast_time = i[0]
                    break
                elif i[1] == i[0] and i [1] < i[2] or i[1] < i[0] and i [1] == i[2]:
                    fast_time = i[1]
                    break
                elif i[2] == i[0] and i[2] < i[1] or i[2] < i[0] and i[2] == i[1]:
                    fast_time = i[2]
                    break
    for i in overall_scores:
        if i[3] == value:
            for w in i:
                if i[0] > i[1] and i[0] > i[2]:
                    slow_time = i[0]
                    break
                elif i[1] > i[0] and i[1] > i[2]:
                    slow_time = i[1]
                    break
                elif i[2] > i[0] and i[2] > i[1]:
                    slow_time = i[2]
                    break
                elif i[0] == i[1] and i[0] > i[2] or i[0] > i[1] and i[0] == i[2]:
                    slow_time = i[0]
                elif i[1] == i[0] and i [1] > i[2] or i[1] > i[0] and i [1] == i[2]:
                    slow_time = i[1]
                elif i[2] == i[0] and i[2] > i[1] or i[2] > i[0] and i[2] == i[1]:
                    slow_time = i[2]
    window1.info(value, "Average time: " + str(avg_time) + " s" + "   Fastest time: " + str(fast_time) + " s" + "    Slowest time: " + str(slow_time) + " s")
    window1.text_color = "#4B1D3F"
    window1.font = font
    window1.text_size = 25


# main game window
def new():
    # global widgets
    global app2, round_num, start, subtitle3, subtitle4, age, username, instruct1, faketime

    # global blocks
    global block11, block12, block13, block14, block15, block16, block17, block18, block19, block20, block21, block22, block23, block24

    app2 = Window(app, width=927, height=562, title="Let's Play!")
    app2.bg = "#17BEBB"
    app2.set_full_screen()

    # main top bit for time, instructions, and round number
    block11 = Box(app2, align="top", height=96, width="fill")

    # separate block for time
    block12 = Box(block11, width=220, height="fill", align="left")
    faketime = Text(block12, text="0.00s", font=font, size=42, color="#4B1D3F")

    # separate block for instructions
    block13 = Box(block11, align="left", height="fill", width=545)
    instruct1 = Text(block13, text="Enter your information:", font=font, size=28, color="#4B1D3F", align="left")

    # block for the round number
    block14 = Box(block11, align="right", width="fill", height="fill")
    round_num = Text(block14, text="Round 1/3", font=font, size=22, color="#4B1D3F", align="left")

    # block for user inputs
    block15 = Box(app2, align="left", height="fill", width=220)

    # enter username subtitle
    block19 = Box(block15, align="top", width=197, height=30)
    block19.bg = "#D4F4DD"
    subtitle3 = Text(block19, align="left", text="Enter username: ", font=font, size=18, color="#4B1D3F")

    # enter username textbox
    block20 = Box(block15, align="top", width=197, height=30)
    block20.bg = "white"
    block21 = Box(block20, align="top", height=8, width="fill")
    username = TextBox(block20, height=40, width=140)

    # padding between bottom of age selection and edge
    block21 = Box(block15, align="bottom", width="fill", height=150)

    # start game button
    start = PushButton(block21, text="Start Game", align="top", command=round1)
    start.bg = "#D4F4DD"
    start.text_color = "#4B1D3F"
    start.font = font
    start.text_size = 12

    # blocks between button and age select
    block24 = Box(block15, align="bottom", width="fill", height=70)

    # background and age select
    block22 = Box(block15, align="bottom", height=280, width=197)
    block22.bg = "white"
    age = ButtonGroup(block22, options=["12", "13", "14", "15", "16", "17", "18"], align="left")
    age.bg = "white"
    age.text_size = 14
    age.text_color = "#4B1D3F"
    age.font = font

    # age select subtitle background and text
    block23 = Box(block15, align="bottom", height=30, width=197)
    block23.bg = "#D4F4DD"
    subtitle4 = Text(block23, align="left", text="Select age: ", font=font, size=18, color="#4B1D3F")

    # block for game space
    block16 = Box(app2, align="right", width="fill", height="fill")
    block16.bg = "#D4F4DD"

    # blocks to make space between edge of window
    block17 = Box(block16, height=11, width="fill", align="bottom")
    block17.bg = "#17BEBB"
    block18 = Box(block16, height="fill", width=11, align="right")
    block18.bg = "#17BEBB"


# actual game part
def round1():
    # global widgets
    global start, rect, time, time_dis, counter, username, saveb

    # global blocks
    global block12, block13, block16, block25, block26

    if username.value == "":
        app2.warn("Invalid Input", "You must enter a username.")
    else:
        start.disable()
        username.disable()
        age.disable()
        instruct1.destroy()
        faketime.destroy()
        time_dis = Text(block12, counter, font=font, size=42, color="#4B1D3F")
        instruct2 = Text(block13, text="Click the box when it turns red", font=font, size=24, color="#4B1D3F", align="left")
        block25 = Box(block16, width="fill", height=320)
        rect = PushButton(block16, text="", height=4, width=10, command=stop_time)
        block26 = Box(block16, width="fill", height=15)
        saveb = PushButton(block16, text="Next Round", command=save)
        saveb.disable()
        rect.disable()
        rect.bg = "white"
        rect.after(time, play)


def play():
    # global widgets
    global rect

    rect.enable()
    rect.bg = "red"
    x()
    rect.repeat(4, x)


def x():
    global running, counter
    running = True
    counter += 0.01
    time_dis.value = round(counter, 4)


def stop_time():
    global running, rect, saveb
    running = False
    rect.disable()
    rect.cancel(x)
    saveb.enable()


def save():
    # each player's data is in the order: (round1 time, round2 time, round3 time, username)
    # global widgets
    global counter, username, overall_scores, rect, start, time_dis, saveb, age, uage, user

    user = username.value
    uage = age.value
    timer = round(counter, 4)

    overall_scores.append([timer, None, None, user, uage])
    counter = 0
    time_dis.value = counter
    rect.bg = "white"
    saveb.destroy()
    round2()


def round2():
    # global widgets
    global start, rect, time, time_dis, counter, username, saveb

    # global blocks
    global block12, block13, block16, block25, block26

    round_num.value = "Round: 2/3"
    saveb = PushButton(block16, text="Next Round", command=save2)
    saveb.disable()
    rect.disable()
    rect.after(time, play)


def save2():
    # each player's data is in the order: (round1 time, round2 time, round3 time, username)
    # global widgets
    global counter, username, overall_scores, time_dis, saveb, uage, app2

    timer = round(counter, 4)

    for i in overall_scores:
        if i[3] == user and i[4] == uage:
            i[1] = timer

    counter = 0
    time_dis.value = counter
    saveb.destroy()
    round3()


def round3():
    # global widgets
    global start, rect, time, time_dis, counter, username, saveb, round_num

    # global blocks
    global block12, block13, block16, block25, block26

    round_num.value = "Round: 3/3"
    saveb = PushButton(block16, text="Finish and close", command=save3)
    saveb.disable()
    rect.disable()
    rect.bg = "white"
    rect.after(time, play)


def save3():
    # each player's data is in the order: (round1 time, round2 time, round3 time, username, age)
    # global widgets
    global counter, username, overall_scores, app2, uage, averages, app

    timer = round(counter, 4)
    a = None
    y = None
    name = None
    age_ = None

    for i in overall_scores:
        if i[3] == user and i[4] == uage:
            i[2] = timer
            a = i[0]
            y = i[1]
            name = i[3]
            age_ = i[4]
            break

    avg = a + y + timer
    avg = round(avg/3, 2)
    averages.append([avg, name, age_])

    counter = 0
    app2.destroy()
    app.update()


# main app setup
app = App(width=927, height=562, title="Reaction Time by Emilia")
app.bg = "#17BEBB"

# block for the title
block1 = Box(app, width="fill", height=105, align="top")

# block for the settings
block2 = Box(app, width=230, height="fill", align="left")
block2.bg = "#17BEBB"

# block for the play button
block3 = Box(app, width="fill", height="fill", align="right")
block3.bg = "#D4F4DD"

# adding the title onto the first block
title = Text(block1, text="Reaction Time Game!", font=font, size=52, color="#4B1D3F")

# making the leaderboard subtitle background
block4 = Box(block2, width=197, height=30)
block4.bg = "#D4F4DD"

# making the leaderboard subtitle text and list display
subtitle1 = Text(block4, text="Leaderboard:", font=font, size=18, color="#4B1D3F", align="left")
leaderboard = ListBox(block2, align="top", width=197, height=200, items=["12", "13", "14", "15", "16", "17", "18"], command=notif)
leaderboard.bg = "white"
leaderboard.text_size = 14
leaderboard.text_color = "#4B1D3F"
leaderboard.font = font

# spacing out the difficulty from the bottom
block6 = Box(block2, align="bottom", width="fill", height=30)

# making a bigger white background for the difficulty
block7 = Box(block2, align="bottom", width=197, height=145)
block7.bg = "white"

# making the difficulty text and button group display
difficulty = ButtonGroup(block7, align="top", options=["Easy", "Medium", "Hard"], selected="Easy")
difficulty.bg = "white"
difficulty.text_size = 17
difficulty.text_color = "#4B1D3F"
difficulty.font = font

# making the difficulty subtitle background and text
block5 = Box(block2, width=197, height=30, align="bottom")
block5.bg = "#D4F4DD"
subtitle2 = Text(block5, text="Difficulty", font=font, size=18, color="#4B1D3F", align="left")

# spacing out the play button section from the window borders
block8 = Box(block3, align="bottom", width="fill", height=13)
block8.bg = "#17BEBB"
block9 = Box(block3, align="right", height="fill", width=13)
block9.bg = "#17BEBB"

# making a block half way(ish) down so that the play button is in the middle of block 3
block10 = Box(block3, align="top", width="fill", height=190)

# main play button that goes to actual game
play_btn = PushButton(block3, text="Play", align="top", command=new)
play_btn.font = font
play_btn.text_size = 18
play_btn.text_color = "#4B1D3F"


app.display()

