def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

print("You are off on your space mission! You've just taken off and left the Earth's atmosphere. Your team is ready for an adventure of a lifetime! The goal of this mission is to try to find life in the universe. As the captain - you now have an important choice. Where do you go?")
userInput = input("Enter A or B. A) Head towards Mars B) Head into empty space: ")

if userInput == 'A':
# Student 1 finishes this code
     pass

elif userInput == 'B':
     print('\n\nyou head off into empty space with no plan. Your crew ask if they should chart a course to a small nearby exoplanet')
     userInput = input("A) Head towards the unnamed exoplanet B) go farther into empty space: ")
     if userInput == 'A':
          print('\n\nyou land on the small planet and scan for life. There is a ')
          userInput = input("A) Head towards the unnamed exoplanet B) go farther into empty space: ")
     elif userInput == 'B':
          print('\n\nyou head off into empty space with no plan, again. You drift through nothingness for 3 months without any signs of life. finally, a huge blue exoplanet looms in the distance. if looks promising')
          userInput = input(f"A) Head towards the large blue exoplanet B) {strike('go farther into empty space')}  die: ")
          if userInput == 'A':
               pass
          elif userInput == 'B':
               print("\n\nyou order your crew further into the darkness. They don't take kindly to it. As your body floats calmy out of the airlock, you see the magnificent blue orb grow closer....\ngame over")


else: 
     print("You entered something wrong - refresh and try again!")

