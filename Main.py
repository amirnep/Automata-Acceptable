#Nazariye: Dr. Bouyer
#Project by Amir Nematpour - 981830281

import Class as c

if __name__ == '__main__':
    obj = c.accept_reject()

    if obj.check():
        print("Accepted.")
    else:
        print("Rejected.")

quit = input("Press Enter to exit.")
