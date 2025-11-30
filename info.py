from pyscript import display, document

clubs = {
    "clubA": {
        'club_name': 'Math Club',
        'description': 'Where we add numbers',
        'time': '3-5PM',
        'loc': 'Club Room 1',
        'mod': 'Ishan',
        'num': '5'
    },

    "clubB": {
        'club_name': 'Science Club',
        'description': 'Where we figure out science',
        'time': '3-5PM',
        'loc': 'Club Room 2',
        'mod': 'Justice',
        'num': '6'
    },

    "clubC": {
        'club_name': 'English Club',
        'description': 'Where we play with words',
        'time': '3-5PM',
        'loc': 'Club Room 3',
        'mod': 'Quiambao',
        'num': '7'
    }
}

def generate(e):
    output = document.getElementById("output")
    output.innerHTML = ""

    selected = document.getElementById("clubSelect").value
    club = clubs[selected]

    display(f"Club Name: {club['club_name']}", target="output")
    display(f"Description: {club['description']}", target="output")
    display(f"Time: {club['time']}", target="output")
    display(f"Location: {club['loc']}", target="output")
    display(f"Moderator: {club['mod']}", target="output")
    display(f"Members: {club['num']}", target="output")