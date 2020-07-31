import random

def montyTrial():
    car_door = random.randint(1, 3)
    # print("Car door:",car_door)
    participant_first_choice = random.randint(1, 3)
    # print("Participant First Choice:",participant_first_choice)

    host_proper_choice = False
    while not host_proper_choice:
        host_choice = random.randint(1, 3)
        if host_choice not in (car_door,participant_first_choice):
            host_proper_choice = True
    # print("Host choice:",host_choice)

    non_switch_win = False
    if car_door == participant_first_choice:
        non_switch_win = True

    switch_win = False
    participant_second_choice = [x for x in (1,2,3) if x not in(host_choice,participant_first_choice)] 
    if car_door == participant_second_choice[0]:
        switch_win = True

    return non_switch_win, switch_win

i = 1
count_non_switch_win = 0
count_switch_win = 0
while (i <= 100):
    # print('===== Trial:',i)
    (non_switch_win,switch_win) = montyTrial()
    if non_switch_win:
        count_non_switch_win += 1
    if switch_win:
        count_switch_win += 1
    i += 1

print('Total Trials:',i-1)
print("Switch wins:",count_switch_win)
print("Non-Switch wins:",count_non_switch_win)
