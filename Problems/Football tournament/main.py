import itertools
# the variable 'teams' is already defined
teams_iter = itertools.combinations(teams, 2)
for i in teams_iter:
    print(i)
