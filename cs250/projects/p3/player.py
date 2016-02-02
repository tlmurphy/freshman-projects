import sys
from music import Music

def main():

    m = Music(sys.argv[1])
    m.set_beat(0.25)
    m.header()

    m.play("C", 3, 1)
    #m.play("D", 3, 2)
    m.play("A", 3, 2)

main()
