print('''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
      ''')



print("Welcome to Treasure Island.")
print("Your mission is to find the Treasure.")
choice1 = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\" ").lower()

if choice1 == "left":
    choice2 = input("Swim or Wait?").lower()
    if choice2 == "wait":
        door = input("you have three doors.Red,Blue or yellow door?").lower()
        if door == "yellow":
            print("*** You WIN ***")
        else:
            print("Game Over.")
    else:
        print("You got attacked.Game Over.")
else:
    print("You fell into a hole. Game Over.")