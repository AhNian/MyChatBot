<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 --> 

## intent:bye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:weather
- what's the weather in [Singapore](GPE)
- What is the weather in [Singapore](GPE)
- Please tell me what is the weather now in [Singapore](GPE)
- What is the weather now?

## intent:Singapore
- Singapore
- sing
- Singa

## intent:IBMinfo
- What IBM do?
- What's IBM?
- IBM?

## intent:inform
- weather please
- weather now
- weather thanks

## intent:greet
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- Greetings
- hello everybody
- hello is anybody there
- hello robot
- Hey hey
- Hey there
- Hello there
- Hello sunshine
- Hello mister
- Excuse me
- Great to see you
- Good to see you
- It's great to see you
- Salutations
- Hello, how to you do?
- Greeting and salutations
- Greetings
- Greetings to you
- Ayee
- Heyoo
- Hey you!
- Hey love
- Yo
- Whazzup
- Sup!
- Howdy
- Howdy-doody
- Ahoy matey
- Fellers
- What's kickin?
- Whacha doing?
- Whaddup yo!
- Cheers
- Whassup!
- What's cookin?
- Hey, What's up!
- Howdy partner!
- What's up?
- What's poppin?
- What's up man?
- What's going on?


## intent:thank
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely

## intent:name
- [Susan](name)
- My name is [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)
- My name is [Peter](name)
- My name is [Brown](name)
- My name is [Thomas](name)
- My name is [Tim](name)
- My name is [Emily](name)
- My name is [Esabella](name)
- My name is [Jessica](name)
- My name is [Alina](name)
- My name is [Linda](name)
- My name is [Margaret](name)
- My name is [Eva](name)
- My name is [Emma](name)
- My name is [Samantha](name)
- My name is [Megan](name)
- My name is [James](name)
- My name is [Victoria](name)
- My name is [Victor](name)
- My name is [Poppy](name)
- My name is [Oliva](name)
- My name is [Jack](name)
- My name is [Harry](name)
- My name is [George](name)
- My name is [Jacob](name)
- My name is [Kyle](name)
- My name is [Joe](name)
- My name is [Damian](name)
- My name is [Noah](name)
- My name is [Ethan](name)
- My name is [Cody](name)
- My name is [Dave](name)
- My name is [Dickson](name)
- My name is [Robert](name)
- My name is [Albert](name)
- My name is [Richard](name)
- My name is [Danial](name)
- My name is [Kellu](name)
- My name is [Zoe](name)
- My name is [Kate](name)
- My name is [Jasper](name)
- My name is [Wendy](name)
- My name is [Carley](name)
- My name is [Nicole](name)
- My name is [Grace](name)
- My name is [Jasmine](name)
- My name is [Cheryl](name)
- My name is [Faith](name)
- My name is [Vicky](name)
- My name is [Jackson](name)
- My name is [Norman](name)
- My name is [Paticak](name)
- My name is [Johnathan](name)
- My name is [Ron](name)

## intent:joke
- Why don't you tell me a CK joke
- Chuck Norris joke 
- Make me laugh
- Can you please tell me a ck joke

## intent:dadjoke
- Tell me a dad joke
- Dad joke 
- Tell me a funny dad joke

## intent:pandafact
- Tell me a panda fact 
- Panda fact
- Tell me a funny panda fact

## intent:Introduction
- Who are you?
- What's your name?
- Can you tell me your name?
- Can i have your name?
- Can you kindly tell me your name?
- Could you kindly tell me your name?
- Could you please tell me your name?
- Could you do a self introduction?
- Do you mind, if i ask for your name?
- Would you mind, if i ask for your name?
- Would you introduce yourself?
- It would be lovely if you can tell me your name?
- Please tell me what is your name?
- Do you mind telling me yor name?
- Do let me know how can I address you as?
- How should I call you as?
- How should I address you as?
- How can I address you as?
- How should i address you by?
- May I ask your name?
- May I know who is this?
- Hey! What's your name?
- Mind giving me your name?
- Mind sharing with me your name?
- Let me know what are you called
- What is your name?
- What should I call you?
- What is your name sir?

## intent:IntroductionWN
- Please tell me your name
- Please let me know how can I call you?
- Please introduce yourself to us?
- Please tell me who are you?

## intent:help
- Could you mind helping me with this?
- Could you mind lending me a helping hand?
- Do you mind helping me out?
- Do you mind doing me a favour?
- Do you mind helping me?
- Mind helping me with this?
- Mind supporting me on this?
- Will you mind helping me with this?
- Will you mind doing me a favour?
- Will you mind lending me a help?
- Would you mind doing me a favour?
- Would you mind helping me out with this
- Can I ask a favour from you?
- Can I ask you a question?
- Can I ask you for a favour?
- Can I ask you something?
- Could I ask a favour of you?
- Could I ask you a favour?
- Could I ask you for a favour?
- Could I ask you for help?
- Could I ask you something?
- Could I ask you to do me a favour?
- Could I ask you to help me?
- I wonder if i can ask for a favour?
- I wonder if i can ask for help?
- I wonder if i could ask for for help?
- May I ask for a favour?
- May I ask a question?
- May I ask for some help?
- May I ask you a favour?
- May I ask you a question?
- May I ask you for some help?
- Are you able to help me?
- Are you able to lend me a hand?
- Do you think you will be able to do me a favour?
- Do you think you will be able to help me?
- Do you think you will be able to lend me a hand?
- Could I trouble you in this matter?
- Could I trouble you to help me?
- Could I trouble you with this?
- Cound I trouble you?
- I might need your help here
- I might need some help here
- I might need your help
- I was hoping that you can help me with this?
- I was hoping that you can help me?
- I was hoping that you can lend me a hand with this?
- I was hoping you will be here to help me on this?
- I was hoping you will be here to assist me?
- I was wondering if you can give me some advice?
- I was wondering if you could do me a favour?
- I was wondering if you could give me some advice?
- I was wondering if you could help me?
- I was wondering if you would help me?
- I was wondering if you would do me a favour?
- I will like to know if you could do me a favour?
- I will like to know if you could lend me a hand here?
- It will be kind of you if you can advice me on this issue
- Please can you lend me a hand?
- Please can you advice me on this problem?
- Please can you do me a favour?
- Sorry to bother you, can you help me
- Sorry to bother you, can you help me with this?
- Sorry to bother you, could you help me with this?
- Sorry to bother you, would you doing me a favour
- Sorry to bother you, would you lend me a hand?
- Will it be alright if you can help me out?
- Will it be alright if you can lend me a hand?
- Will it be too much trouble for you to help me with this matter?
- Will it be too much trouble for you to help me with this problem?
- Will it be too much trouble for you to help me with this?
- Will you be willing to help?
- Will you be willing to lend me a hand?
- Will you like to help me out?
- Will you like to lend me hand?
- Will you please help me with this?
- Will you please help me?
- Would it be all right if you can give me some advice?
- Would it be all right if you could give me some advice?
- Would it be alright if you can do me a favour?
- Would it be alright if you can give me some advice?
- Would it be alright if you can help me out?
- Would it be alright if you can lend me a hand?
- Would it be alright if you could do me a favour?
- Would it be alright if you could give me some advice?
- Would it be alright if you could help me out?
- Would it be alright if you could lend me a hand?
- Would it be alright if you lend me a hand?
- Would it be possible for you do me a favour?
- Would it be possible for you lend me a hand?
- Would it be possible for you to assist me?
- Would it be possible for you to do me a favour?
- Would it be possible for you to give me a hand?
- Would it be possible for you to help me out?
- Would it be possible for you to help me?
- Would it be possible for you to lend me a hand?
- Would it be possible if you help me?
- Would it be possible if you were to do me a favour 
- Would it be possible if you were to help me out 
- Would it be possible if you were to lend me a hand
- Would it be possible that you lend me a hand?
- Would you be so kind and do me a favour?
- Would you be so kind and help me out?
- Would you be so kind as to do me a favour?
- Would you be so kind as to help me?
- Would you be so kind to help me with this?
- Would you be so kind to help me?
- Would you be willing be to help me?
- Would you be willing to do me a favour?
- Would you be willing to give me an advice?
- Would you be willing to help me in this?
- Would you be willing to help me?
- Would you be willing to lend me a hand?
- Would you have any idea on this?
- Would you help me out?
- Would you help me with this?
- Would you help me?
- Would you kindly assist me?
- Would you like to do me a favour?
- Would you like to give me an advice?
- Would you like to help me out here?
- Would you like to help me?
- Would you like to help out?
- Would you like to lend me a hand here?
- Would you like to lend me hand?
- Would you look at this matter for me?
- Would you please do me a favour?
- Would you please explain to me?
- Would you please help me?
- Would you please send some help here 
- Would you please solve this problem?
- Would you possible do me a favour?
- Would you possibly help me?
- Would you possibly know the solution to this matter?
- Would you possibly know the solution to this problem?

## intent:do
- What can you do?
- What's your functionability?
- Would you mind sharing with me what you can do?
- Would you mind sharing what you can do?
- Would you mind sharing with me what you do?
- Alright, can you share with me what you can do?
- It will be great if you can share with me what you can do
- It will be wonderful if you can share with me what you can do
- It will really help if you can share with me what you can do
- It would be good if you can share with me what you can do
- It would be good if you share with me what you can do
- I wonder if you can share with me what you can do
- I wonder if you can share with me what you do
- I wonder if you would like to share with me what you can do
- I wonder if you would like to share with me what you do
- I would be glad that if you can share with me what you can do
- I would be glad that if you can share with me what you do
- I would be grateful if you can share with me what you can do?
- If it's okay, would you like to share with me what you can do?
- Is it alright for you to share with me what you can do?
- It will be better for me if you can share me what you can do?
- It will be better for me to know what you can do?
- May I know what are some things you can do?
- May I know what things you can do?
- May I know what you can do?
- Please let me know what are some things you can do
- Please let me know what things you can do
- Please let me know what you can do
- What are some things you can do
- What can you really do?
- What could you do?
- What some things you can do
- What would you likely can do?
- Would you mind if i ask you what you can do?
- I would like to enquire you on what you can do
- I would like to enquire you on what you do
- I would like to know what you can do
- I would like to take this chance to ask you what you can do?
- I would like to take this chance to ask you what you do?
- I would like to take this chance to know what you can do?
- I would like to take this chance to know what you do?
- I would like to understand what you can do
- I would love to hear what you can do
- I would love to know what you can do
- I would love to listen to the things you can do
- I would love to listen to the things you do
- I would love to listen to what you can do
- I would want to know what you really can do
- It will be amazing for me to know what you can do?
- Are you able to tell me what you can do for me?
- Can you please tell me what you can do for me?
- Can you now tell me further what you can do for me?
- Could you please tell me more about what you can do for me?
- Could you please tell me what you can do for me?
- Do you mind telling me what you can do for me?
- Please tell me what you can do for me?
- Tell me more about what you can do for me
- Anything you can do for me?
- Anything you can do?
- Are you able to share with me what you can do for me?
- Can I check with you what you can do for me?
- Can you explain what you can do for me?
- Can you list out what you can do for me?
- Can you share with me what are some things you can do for me?
- Can you share with me what you can do for me?
- I hope that you can share with me what you can do for me?
- I like to know what you can do for me
- I want to know what you can do for me
- Are you able to tell me what you can do?
- Can you please tell me what you can do please?
- Can you please tell me what you can do?
- Could you please tell me more about what you can do?
- Could you please tell me what you can do
- Please tell me what you can do?
- Can I check with you what you can do?
- Can you share with me what you can do?
- I like to know what you can do
- I want to know what you can do
- I would like to know what you really can do

## intent:aboutyourself 
- Tell me more about yourself? 
- More about yourself?
- More information about yourself?
- Tell me more information about yourself?
- Give me more information about yourself?
- Give me more information about yourself please?
- Give me more information regarding yourself?
- Give me more information regarding yourself please?
- Heard from others about you, can you tell me more about yourself?
- Heard from others about you, could you tell me more about yourself?
- Could you share more information about yourself?
- Can you share more information about yourself?
- I would like to know more information about yourself?
- Please share with me more information about yourself?
- Share with me more information about yourself?
- Could you please share more about yourself?
- Can you share with me more about yourself?
- Can you tell me more about you?
- Can i know more about you?
- Do you mind telling me more about you?

## intent:where
- Where are you from?
- Who invented you?
- Who created you?

## intent:yhere
- Why are you here?
- What are you doing here?
- Could I know what are you doing here?
- Can I know what are you doing here?
- Could I know why are you here?
- Can I know why are you here?

## intent:yexist 
- Why do you exist
- Do you exist?
- Why you exist?

## intent:notfunny 
- Not funny
- Your joke are not funny 
- Is not funny 
- I don't think that is funny 
- I don't think it is funny
- Your joke are bad 
- Joke are bad 
- Is bad 
- Bad joke

## intent:exercise
- Do you exercise?
- How often do you exercise?
- How frequent do you exercise?
- Do you exercise frequently?
- Do you exercise regularly?

## intent:parents 
- Do you have parents?
- Who are your parenets?
- Mind telling me who are your parents?
- Could I know who are your parents?
- Can I know who are your parents?
- Do tell me who are your parents?
- May I know who are your parents?

## intent:dice
- Roll a dice 
- Tell me a number one to six 
- Roll dice 

## intent:flipcoin
- Flip a coin 
- Flip coin 
- Head or tail

## intent:jobscope
- What is your job scope 
- Job scope 
- What could be your job scope? 

## intent:chatbot
- What is a chatbot?
- Chatbot?
- Can I know what is a chatbot?
- Could you tell me what is a chatbot?
- Can you tell me what is a chatbot?

## intent:AI
- What is AI?
- AI?
- Can you tell me what is AI
- Could you tell me what is AI
- I would like to know what is AI 

## intent:program
- How are you programmed?
- How do you work?
- Can I know how do you work?
- Could you tell me how do you work?
- Do you mind telling me how do you work?


## intent:feeling
- How are you feeling?
- Are you feeling alright?
- You okay?
- How are you feeling today?

## intent:born
- Where were you born?
- Where is your hometown?
- Where did your born take place?

## intent:hobby
- Do you have any hobby?
- Do you have hobbies?
- How do you spent your free time?

## intent:clever
- How clever are you?
- Are you clever?
- Clever?

## intent:fun
- Are you have fun?
- Having fun?
- Are you having fun?

## intent:bored
- You look bored
- Are you bored?
- Boring?

## intent:lonely
- I'm lonely
- Lonely
- I'm so lonely right now

## intent:sad
- I'm sad
- I am so sad right now
- I'm having a bad time now

## intent:cheerup
- I need a cheer up right now
- Can you cheer me up?
- Cheer me up please

## intent:thinking
- What are you thinking right now?
- Are you thinking about something?
- Are you thinking?

## intent:tired
- Are you tired?
- Do you ever get tired?
- tired?

## intent:age
- What's your age?
- Your age?
- Do you mind me asking about your age?

## intent:single
- Are you single?
- Single?
- Do you mind me asking are you single?

## intent:movie
- What is your favourite movie?
- Which movie is your favourite?
- Do you like movie?

## intent:food
- Do you like food?
- Which is your favourite food?
- Which country of food is your favourite?

## intent:drink
- Do you drink?
- Which drink is your favourite?
- You drink?

## intent:catFact
- Cat fact
- Give me a cat fact
- Random cat fact
- Tell me a cat fact
- Tell me something about cat
- Random fact about cat
- Tell me something random about cat

## intent:dogFact
- Dog fact
- Give me a dog fact
- Random dog fact
- Tell me a dog fact
- Tell me dog fact
- Tell me a random dog fact
- Tell me some facts

## intent:puns
- Tell me a pun
- Give me a pun
- Random puns
- Puns
- Tell me a random pun
- Tell me pun
- Tell me random pun
- Random pun please
- Tell me another pun

## intent:another
- That's funny, tell me another one
- Hahaha, tell me another
- Haha, tell me another
- Ha ha, tell me another
- That's a good one, tell me another
- Nice! another one.

## intent:whyhere
- why are you here?
- why here?
- why are you here for?

## intent:drama
- what drama you like?
- drama?
- do you like to show drama?