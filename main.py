print("Jeff's Last Ride")
print("Chapter One: Prologue")
print("2015, Martinsville")
print("Logano ahead in the lead dominating this race. Gordon following close behind. Gordon sends in the corner! Will he catch Logano? Oh he gets loose! Gordon falls way behind. Logano cruises to a two second lead. He approaches the lap cars. He goes on the outside of Matt Kenseth...")
print("Spotter: Hey Jeff, I feel like there's gonna be some trouble up ahead.")
print("You: Whaddya mean?")
print("Spotter: I feel like Kenseth is gonna do something to Logano cuz, y'know, last week")
print("You: Yeah he looks like he's about to do something big")
print("Logano to the outside! Will he get by Kenseth...?")
move_1 = input("Throttle through the wreck or brake?(throttle/brake) ")
if move_1 == "throttle":
  print("Spotter: Jeff slow down!")  
  print("You manage to catch up to Logano, but not before you smack right into the back of Matt Kenseth's car...")
if move_1 == "brake":
  print("Kenseth wrecks Logano! Logano is hard into the wall. The caution is out and the crowd is deafening. Gordon sweeps by and the crowd gets even louder!")
  print("You: Matt just got himself a ton of new fans")
  print("You are now in 1st place")
  print("Spotter: Alright, we're in the lead now but we still need to hold off the rest of the pack for 10 laps. Make sure you nail this final restart")
  move_2 = input("Inside lane or Outside lane? (inside/outside) ")
  if move_2 == "outside":
    print("You get a nice run of the top lane but as soon as you swoop down in the corner you hear a thud near the back of your car as you spin out...")
    
if move_2 == "inside":
      print("Larson gets a big run on your outside but you manage to hold your position in the corner. He slows down to avoid the wall and you accelerate perfectly out of the corner. You cruise to a nice lead when your spotter tells you that a caution came out")
      print("You: What happened this time?")
      print("Spotter: Someone spun out on turn 4. I think it was hornish")
      print("You: Well that sucks. We have to do this whole thing all over again")
      print("Spotter: Yeah, it's tough but we can hold them off. We have to, it's our only hope of advancing to the final four.")
      print("Yeah. This our last shot a drive for five.")
      print("And we are going to overtime! These next two laps will decide the winner of this race. Remember, after the leader takes the white flag, the next flag will end the race.")
      move_3 = input("Spotter: Alright Jeff, it's your choice, wanna go outside or inside? ")
if move_3 == "inside":
  print("You take the inside lane, confident that it will work again. However, as soon as you hit the brakes you feel the car moving faster towards the wall. Your spotter tells you that you were rammed into by Ryan Newman and you crash into the wall, effectively ending your race and your championship hopes.")
if move_3 == "outside":
  print("You decide to switchup your strategy and you head to the outside. You get a big run as you head to the corner. You watch Ryan Newman send it into the corner and lose control. Adrenaline rushes through you as you slam the brakes and drift the corner, narrowly missing the wall.")
  print("You: Whoo that was a close one!")
  print("Spotter: Keep going! We gotta finish before the tire blows")
  print("You: Do I have a tire rub or something?")
  print("Spotter: JUST KEEP GOING!")
  print("You make the rest of the corners without any issues. You take the white flag and pour all your concentration into this final lap. You take the first two corners, slightly slower than you last lap, but as soon as you exit you feel a slight bump from the rear of your car")
  print("You: What was that Eddie?")
  print("Spotter: Uhh-Nothing just keep going and uhh take it easy on the corners")
  print("You immediately realize that you have a tire coming down.")
  print("Just two more turns you think to yourself")
  move_4 = input("Do you ignore your spotter and push hard, or do you do what he tells you to and take it easy? (push/slow) ")
  if move_4 == "push":
    print("You: Hell naw. I'm gonna fully send it")
    print("You ignore your spotters warning and send it in the corner. You brake hard and turn.")
    print("Spotter: No you idiot! The tire's gonna blow" )
    print("Suddenly you hear a pop behind you and you stard sliding across the track. Desperate to save it, you brake hard and turn the steering wheel. But it's no use and you crash into the wall. The cars that were previously behind you zoom right past you and you end up last.")
if move_4 == "slow":
      print("You coast into the corner and pump the brakes. You manage to get around without any damage. You floor it to the end. You check your mirror and you see Jamie Mcmurray closing in on you. You keep your foot on the throttle and you just barely hold him off for the win.")
      print("Spotter: YOU DID IT JEFF! YOU ARE THE MAN!")
      print("The crowd goes wild as you cool down, registering what just happened")
      print("You just got a win at your final race at Martinsville. With the emotional significance this track carries, you know it's going to be one to remember.")
      chap1 = input("Do you want to continue the story? (yes/no) ")
if chap1 == "no":
  print("Oh well, that's too bad") 
confidence = 80
focus = 80 
skill = 90
engineering = 30
reputation = 100
frendliness = 70
intimidation = 30
hero = 90
villian = 10 
sportsmanship = 90
showmanship = 10
sponsorship = 99
if chap1 == "yes":
  print("Chapter Two: Preparing for Homestead")
  print("2015, Hendrick Motorsports Headquarters")
  print("Alan Gustafson (Crew Chief): Congrats on the win man! Let's go take the championship at Homestead!")
  print("How do you want to reply to this? (Type A or B to choose your answer)")
  talk1 = input("([A] Yeah! Let's bring it home!) or ( [B] Sure, but we need to focus on getting our car right. We have to make sure that everything goes right) ")
  if talk1 == "A" :
    print("Your confidence has gone up 5 levels")
    confidence += 5
if talk1 == "B" :
  print("Your focus has gone up 5 levels")
  focus += 5
statcheck1 = input("Would you like to check your stats? (yes/no) ")
if statcheck1 == "yes" :
  print("Confidence =", confidence)
  print("Focus =", focus)
  print("Skill =", skill)
  print("Engineering =", engineering)
  print("Reputation =", reputation)
  print("Frendliness/Intimidation =", frendliness, "/", intimidation)
  print("Hero/Villian =", hero, "/", villian)
  print("Sportsmanship/Showmanship =", sportsmanship, "/", showmanship)
  print("Sponsorship =", sponsorship)
if talk1 == "A":
  print("Alan Gustafson (Crew Chief): Hell yeah! That's what I'm talkin' about. Lets go get that win.")
if talk1 == "B" :
  print("Yeah you're right. I should probably double check everything, just to make sure we got our setups right for practice.")
print("One Week Until Homestead")
print("What would you like to do during your free time? (type the letter assigned to your choice)")
prac1 = input("( [A] I want to practice on the simulator to sharpen my skills at the track/( [B] I want to check out the car in the garage and see if I can learn anything from the engineers/( [C] I want to check footage of old races at Homestead) ")
if prac1 == "A" :
  print("You spend some time on the Iracing simulator and practice with a variety of temperatures and tire conditions. Due to this practice you gain 5 skill")
  skill += 5
if prac1 == "B" :
  print("You head to the garage to check out the car. You walk in and see the team engineers working on the car while Alan Gustafson directs traffic. One of the engineers notice you and he invites you to come over and take a look at the engine. He discusses many things involving the durability of the engine while making sure that you understand everything. You listen intently and soak up the information. When he finishes talking, you stand up and pour yourself a cup of coffee, amazed how much you have learned in such little time.")
  print("Your engineering has increased by 10")
  engineering += 10
if prac1 == "C" :
  print("You head to the tape room and check old DVDs along with recent in-depth recordings of races. Your eyes move through the different tapes and their labels until one finally catches your eye, 2014 Homestead. The sight of it brings a frown to your face but you reluctantly push the tape in and watch. You try to think to yourself that there was nothing you could have done differently and that it was for the sake of the sport, but bitterness crawls all over your body.")
  print("In 2014 you had a chance to make a statement. You had a chance to show everyone that despite getting eliminated you were the REAL champion. Yet your team owner ordered you to pit. Why? Because it would look bad if a non final four member won the championship race. But now, you have a chance at redemption. You made the final four and you have a chance to win it all in your final season. One. Final. Time. But have you really got over last year? Or are you willing to put the past behind you and look forward to the future ")
  film = input("[A] I should have won the championship last year. If it weren't for stupid Brad and his idiocy, you would have had a shot at tying Jimmie for 6 / [B] ")