import random

def match_players(queue):
    team_size = 5
    random.shuffle(queue)
    return [queue[i:i + team_size] for i in range(0, len(queue), team_size)]

if __name__ == "__main__":
    players = [f"Player{i}" for i in range(10)]
    print(match_players(players))
print("this is broken code")
