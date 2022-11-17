def SaveInput(no_of_teams):  # to take input add  the data to storage
    data = {}
    for i in range(no_of_teams):
        print("Enter team name: ")
        teamname = input()  # input the name of Team
        print("Enter points earned by the team: ")
        points = int(input())  # points Team scored
        print("Enter result of matches with , separated values(L as loss , W as win): ")
        matchresult = [str(i) for i in input().split(',')]  # matches result
        team = {'teamname': teamname, 'points': points,
                'matchresult': matchresult}  # dictionary stores team name,points and match result
        data[teamname] = team
    print(data)
    return data  # dictionary stores the data regarding team


def FindConsecutiveLossTeamsAndItsAverage(teamdata):  # to find team who has two consecutive loss, and it's average
    consecutivelossteams = {}
    for teamname, values in teamdata.items():
        # print(team,stats)
        list_ = values['matchresult']
        for i in list_:
            if (i == 'L'):  # checking first loss
                firstlossindex = list_.index(i)
                nextindex = firstlossindex + 1
                if (nextindex < len(list_) and list_[nextindex] == 'L'):  # checking for consecutive loss , if next
                    # index is less than list length
                    consecutivelossteams[teamname] = [values['points'],
                                                      len(list_)]  # adding the points and length of the match result
                    # to dictionary to get the average
    if (len(consecutivelossteams) == 0):
        print('No team have consecutive loss')
    else:
        print("Teams having consecutive loss :", consecutivelossteams)
        for team, data in consecutivelossteams.items():
            average = data[0] / data[1]
            print(team, "--Average points--", average)


print("Enter number of teams:")
number_of_teams = int(input())  # input for number of teams
data = SaveInput(number_of_teams)
FindConsecutiveLossTeamsAndItsAverage(data)