# Working with Lists
from pyscript import document
# Variables
country = ("Philippines", "Japan", "South Korea", "North Korea", "Thailand", "Taiwan", "Hong Kong","Indonesia") # the selection
nickname = ("Pearl of the Orient","Land of the Rising Sun", "Land of the Morning Calm", "The Hermit Kingdom","Land of Smiles","The Beautiful Island", "Asia's World City","The Emerald of the Equator") # nicknames of the following items

def show_nick(e):
    selected_country = document.getElementById("country").value

    selected_nickname = nickname[int(selected_country)]

    document.getElementById("result").innerText = selected_nickname