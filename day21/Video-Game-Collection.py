class VideoGame:
    def __init__(self, title, genre, hours_played) -> None:
        self.title = title
        self.genre = genre
        self.hours_played = hours_played
        self.completed = False #تمامنشده
    def completed_game(self):
        if self.completed == False:
            self.completed = True
            return "Completed!"
        else:
            return "Already completed!"
    def show_info(self):
        status = "Completed" if self.completed else "Not completed"
        return f"{self.title} | {self.genre} | {self.hours_played} | {status}"
games = [
    VideoGame("The Witcher 3", "RPG", 120),
    VideoGame("Cyberpunk 2077", "RPG", 80),
    VideoGame("Minecraft", "Sandbox", 500),
    VideoGame("Valorant", "FPS", 300),
    VideoGame("GTA V", "Action", 250),
    VideoGame("Red Dead Redemption 2", "Action", 150),
    VideoGame("Hades", "Roguelike", 60),
    VideoGame("Celeste", "Platformer", 40),
    VideoGame("Portal 2", "Puzzle", 20),
    VideoGame("Terraria", "Sandbox", 200)
]

games[0].completed_game()
games[3].completed_game()
games[7].completed_game()
games[4].completed_game()
games[1].completed_game()
games[9].completed_game()

def count_completed_games(games):
    count = 0
    for game in games:
        if game.completed == True:
            count += 1
    return count
result = count_completed_games(games)
print(result)

def find_most_played_game(games):
    most_played_title = None
    highest_time = -1
    for game in games:
        if game.hours_played > highest_time:
            highest_time = game.hours_played
            most_played_title = game.title
    return most_played_title, highest_time
result = find_most_played_game(games)
print(result)

def find_total_hours_played(games):
    total = 0
    for game in games:
        total += game.hours_played
    return total
result = find_total_hours_played(games)
print("total time=", result)

for game in games:
    print(game.show_info())






