# Define four Python functions named run, swing, slide, and hide_and_seek.
# Each function should take a child's name as an argument. Each function 
# should print that the child performed the activity.

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run(name):
        print(f'{name} ran like a fool!')
run("pam")  

def swing(name):
    print(f'{name} swung really high!')
swing("marybeth")  

def slide(name):
    print(f'{name} slid down the slide!')

slide("mike")    

def hide(name):
    print(f'{name} hid behind the car')

hide("henry")    


for run in running_kids:
    print(run, "ran like a fool")

for swing in swinging_kids:
    print(swing, "swung really high!")

for slide in sliding_kids:
     print(slide, "slid down the slide!")

for hide in hiding_kids:
    print(hide, "hid behind the car")        