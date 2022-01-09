def main():
    n = int(input())
    teams = {}

    for _ in range(n):
        first_team, first_team_score, second_team, second_team_score = input().split(';')

        if first_team not in teams.keys():
            # [0]=всего игр; [1]=побед;[2]=ничьих;[3]=поражений;[4]=всего очков
            teams[first_team] = [0, 0, 0, 0, 0]
        if second_team not in teams.keys():
            teams[second_team] = [0, 0, 0, 0, 0]

        teams[first_team][0] += 1
        teams[second_team][0] += 1

        if int(first_team_score) > int(second_team_score):
            teams[first_team][1] += 1
            teams[first_team][4] += 3
            teams[second_team][3] += 1
        elif int(first_team_score) < int(second_team_score):
            teams[second_team][1] += 1
            teams[second_team][4] += 3
            teams[first_team][3] += 1
        elif int(second_team_score) == int(second_team_score):
            teams[first_team][2] += 1
            teams[first_team][4] += 1
            teams[second_team][2] += 1
            teams[second_team][4] += 1

    for key, value in teams.items():
        print(key, end=':')

        for v in value:
            print(v, end=' ')

        print()


if __name__ == '__main__':
    main()
