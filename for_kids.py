def run(*kids):
    for kid in kids:
        print(f"{kid} ran like a fool.")

def swing(*kids):
    for kid in kids:
        print(f"{kid} fell off the swing!")

def slide(*kids):
    for kid in kids:
        print(f"{kid} got a friction burn on the slide!")
    
def hide_and_seek(*kids):
    for kid in kids:
        print(f"Hey... did anyone ever find {kid}? Oh no, call the cops, we need a search party!")

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")