from phue import Bridge
import readchar
import random

# globals
peters_room = ['Hue ambiance lamp 1', 'Hue ambiance lamp 2']
b = Bridge('192.168.1.5')


def lights_on ():
    '''
    Turns on both lights in peters room
    '''
    for light in peters_room:
        b.set_light(light, 'bri', 254, transitiontime=1)
        b.set_light(light, 'on', True, transitiontime=1)

def lights_off ():
    '''
    Turns off both lights in peters room
    '''
    for light in peters_room:
        b.set_light(light, 'on', False, transitiontime=1)


print("press 1 then 2 to signify walk in. press 2 then 1 to signify walk out.")

# main loop
# Using two motion sensors:
# when triggered
#   seq 1 then 2 (walk in)
#   seq 2 then 1 (walk out)
#   calculate num people in the room to see if lights should be on or off
# At the moment its two buttons

n_people = 0
while True:
    val = readchar.readkey()
    if val == '1':
        val = readchar.readkey()
        if val == '2':
            n_people += 1
            print (n_people,  "in the room.") 
    
    elif val == '2':
        val = readchar.readkey()
        if val == '1':
            n_people -= 1
            print (n_people,  "in the room.")
    elif val == 'x':
        exit()
    if n_people > 0:
        lights_on()
    elif n_people <= 0:
        lights_off()


