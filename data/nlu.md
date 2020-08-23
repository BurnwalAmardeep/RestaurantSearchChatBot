## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hi
- hola

## intent:give_emailid
- my email id is [himadri.hk@live.com](email_id)
- my emailid is [himadri.hk@live.com](email_id)
- my id is [himadri.hk@live.com](email_id)
- my mail id is [himadri.hk@live.com](email_id)
- [test.mail@gmail.com](email_id)
- here it is [amardeep.burnwal@gmail.com](email_id)
- [burnwal.amardeep@gmail.com](email_id)
- [himadri.hk@gmail.com](email_id)
- yes. my email id is [himadri.hk@live.com](email_id)
- [himadri.hk@gmail.com](email_id)

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Yes
- yups

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for four people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- find me a restaurant near me
- show me some restaurants
- list restaurants in [jamshedpur](location)
- find restaurants
- find restaurants in [Bhopal](location)
- show me some restaurants in [bhopal](location)
- please find me some restaurants in [asansol](location)
- find me some restaurants in [asansol](location)
- find some restaurants in [swarg](location)
- find some [north indian](cuisine) restaurants in [ranchi](location)
- [Chinese](cuisine:chinese)

## intent:get_location
- [Bangalore](location)
- [Kolkata](location)
- [Mumbai](location)
- show in [nagpur](location)
- show in [808202](pincode)
- [560067](pincode)
- in [723103](pincode)
- I need in [123112](pincode)
- look in [213122](pincode)
- look in [ahmedabad](location)
- search in [121231](pincode)
- search in [delhi](location)
- [delhi](location)
- in [kolkata](location)
- [kolkata](location)
- [bangalore](location)

## intent:budget
- [<300](price)
- [Lesser than Rs 300](price)
- [300-700](price)
- [Rs 300 to Rs 700](price)
- [>700](price)
- [More than 700](price)
- [Rs 300 to Rs 700](price:300-700)
- [300-700](price)

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- nops
- nah

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## synonym:300-700
- Rs 300 to Rs 700
- between 300 to 700
- mid
- not more than 700
- 700

## synonym:<300
- Less than 300
- lower than 300
- 300 for 2
- low
- 300 for two
- Rs 300
- 300
- not more than 300

## synonym:>700
- More than 700
- High
- Greater than 700
- 800

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:email_id
- ^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
