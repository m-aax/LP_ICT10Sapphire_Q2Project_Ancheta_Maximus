from pyscript import document  #type: ignore

# Club information stored in a dictionary
club_data = {
    "Literature Club": (
        "Literature Club\n"
        "Description: Read and absorb knowledge from works of scholars and maesters in Westeros.\n"
        "Meeting Time: Every Tuesday 3:45–5:30 PM\n"
        "Location: Classroom 41 (Literature Room)\n"
        "Advisor: Mr. Tarly\n"
        "Number of Members: 18\n"
        "Category: Academic"
    ),
    "History Club": (
        "History Club\n"
        "Description: Absorb the histories of Westeros and their royal families. Learn about the history of Westeros and the Targaryen dynasty.\n"
        "Meeting Time: Every Thursday 4:00–5:00 PM\n"
        "Location: Classroom 18 (History Room)\n"
        "Advisor: Mr. Three Eyed Raven\n"
        "Number of Members: 22\n"
        "Category: Academic"
    ),
    "Maesters Guild": (
        "Maester's Guild\n"
        "Description: Learn about the art of magic, medicine, and more knowledge. Great maesters start here, and exceptional students here are sent to the Citadel.\n"
        "Meeting Time: Every Friday 3:30–5:00 PM\n"
        "Location: Library 2\n"
        "Advisor: Maester Qyburn\n"
        "Number of Members: 24\n"
        "Category: Academic"
    ),
    "CA Club": (
        "Combat Arts Club\n"
        "Description: Master the art of combat with swords, lance, and the bow and arrow. This is the start of your journey to knighthood or even Kingsguard.\n"
        "Meeting Time: Every Monday 4:00–5:30 PM\n"
        "Location: Classroom 12\n"
        "Advisor: Mr. Jaime Lannister\n"
        "Number of Members: 30\n"
        "Category: Physical"
    ),
     "Warfare Guild": (
        "Warfare Guild\n"
        "Description: Learn the fundamentals of battle and warfare, as well as tactics and strategies.  \n"
        "Meeting Time: Every Monday 4:00–5:30 PM\n"
        "Location: Classroom 12\n"
        "Advisor: Mr. Tywin Lannister\n"
        "Number of Members: 30\n"
        "Category: Physical"
    ),
}
def show_club_info(event):
    club = document.querySelector("#club-select").value
    info_box = document.querySelector("#club-info")
    info = club_data.get(club, "Club information not found.")
    info_box.innerText = info

