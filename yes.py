lyrics = '''Creeper
Aw man
So we back in the mine
Got our pickaxe swinging from side to side
Side-side to side
This task, a grueling one
Hope to find some diamonds tonight, night, night
Diamonds tonight
Heads up
You hear a sound, turn around and look up
Total shock fills your body
Oh, no, it's you again
I can never forget those eyes, eyes, eyes
Eyes-eye-eyes
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
'Cause, baby, tonight
You grab your pick, shovel, and bolt again (Bolt again-gain)
And run, run until it's done, done
Until the sun comes up in the morn'
'Cause, baby, tonight
The creeper's tryna steal all our stuff again (Stuff again-gain)
Just when you think you're safe
Overhear some hissing from right behind
Right-right behind
That's a nice life you have
Shame it's gotta end at this time, time, time
Time-ti-time-time
Blows up
Then your health bar drops and you could use a one-up
Get inside, don't be tardy
So now you're stuck in there
Half a heart is left, but don't die, die, die
Die-die-die
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
'Cause, baby, tonight
You grab your pick, shovel, and bolt again (Bolt again-gain)
And run, run until it's done, done
Until the sun comes up in the morn'
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
(Creepers, you're mine, haha)
Dig up diamonds, and craft those diamonds
And make some armor, get it, baby
Go and forge that like you so MLG pro
The sword's made of diamonds, so come at me, bro, huh!
Training in your room under the torchlight
Hone that form to get you ready for the big fight
Every single day and the whole night
Creeper's out prowlin', hoo, alright
Look at me, look at you
Take my revenge, that's what I'm gonna do
I'm a warrior, baby, what else is new?
And my blade's gonna tear through you, bring it
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
(Gather your stuff, yeah, let's take back the world)
Yeah, baby, tonight (Haha)
Grab your sword, armor and go (It's on)
Take your revenge (Woo), oh-oh, oh-oh
So fight, fight, like it's the last, last night
Of your life, life, show them your bite (Woo)
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
'Cause, baby, tonight
You grab your pick, shovel and bolt again (Bolt again-gain, woo)
And run, run until it's done, done
Until the sun comes up in the morn'
'Cause, baby, tonight (Come on, swing your sword up high)
The creeper's tryna steal all our stuff again (Come on, jab your sword down low)
(Woo)'''

for idx, val in enumerate(lyrics.split('\n')):
    fname = ''
    if idx in range(0, 10):
        fname = '0' + str(idx)
    else:
        fname = str(idx)
    __import__('os').system('copy NUL ' + fname)
    __import__('os').system('git add ' + fname)
    __import__('os').system('git commit -m "' + val + '"')

__import__('os').system('git push')
