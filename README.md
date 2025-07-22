# Pokémon Black and White AP Manual
## About
A Manual Randomizer for use with Pokémon Black and White, for use with the [Archipelago Manual](https://github.com/ManualForArchipelago) Project. This Manual randomizes all ground items, HMs, Badges, and items given by important characters. Options are included to add hidden items as well as items from all the other NPCs.

This AP World assumes you know how to add items to your game using [PKHeX](https://github.com/kwsch/PKHeX) (brief tutorial is included below)

Shoutouts to Linneus and their [Pokémon Platinum Manual](https://github.com/Linneus/PlatinumAPManual/releases/tag/2.3) without out which I would not have been inspired to make this Manual or have the knowledge to add extra options.

## Check Rewards
- HMs
- TMs
- Badges
- Key Items
- Item from the "Items Pocket"
- Medicine Items

## Logic Requirements
*These are the items you are expected to receive from the server in order to progress past certain points*
 - HM01 Cut to get past the tree in the Dreamyard and then proceed to Route 3 as well as checks behind other Cut trees
 - Insect Badge to access the area of Route 4 North of the Cheren fight
 - Bolt Badge to access Driftveil City
 - Light/Dark Stone to initiate the Bianca fight and proceed to Tubeline Bridge
 - HM03 Surf to get any checks that require you to Surf
 - HM04 Strength to get checks behind Strength rocks
 - HM05 Waterfall to checks up Waterfalls (Currently only one check)
 - TM70 Flash to get checks in dark caves
 - Completing the "Recieve Bicycle" Event check to access eastern Pinwheel forest
 - All eight Badges to access Victory Road, the Pokémon League, and N's Castle

## Check Locations
### Always Available
- Items given by "important" NPCs
- Item balls you find on the ground
- HMs
- Badges
- Various events you complete throughout the game. (They will always give you the event as an item) These are just to help know what you gain access to upon completing the tasks.
### Available with options
- Hidden Items
- Items given by all other NPCs
- Mistralton Cave items

## Current Available Options
### Two Goal Options
- Defeat Ghetsis at N's Castle - The default goal where you collect eight Badges receive the game's credits (Longer goal ideal for Asyncs)
- Defeat Cobalion at Mistralton Cave - A shorter goal that excludes all checks from Twist Mountain and beyond, where you collect four Badges and take down the Sword of Justice (Ideal for Syncs)
### Other Options
- Include NPC Items - Adds checks from all random NPCs that give items
- Randomize Hidden Items - Adds checks for the hidden items found throughout the game
- Require Dowsing MCHN - Makes it so you need to receive the Dowsing MCHN before you are logically required to pick up hidden items
- Include Mistralton Cave Items - Adds Mistralton Cave checks to the pool. This option was added to improve the Cobalion goal by preventing you from having to go through the cave twice if this is set to "false"

## PKHeX Tutorial
This will be a quick guide showing just enough about PKHeX to use this AP World properly.

### Step 1: Download PKHeX
1. Go to the link for the PKHex Github link at the top of this readme
2. Click on Releases then download the zip file from assets
3. Extract the zip file to whatever location you want
### Step 2: Create a Save File
1. Start a new game of vanilla or randomized Pokémon Black or White
2. Save and quit your game when you can
3. Locate your save file on your computer, you will need it for the next step
### Step 3: Load Save in PKHeX
1. Open PKHeX and then click File
2. Click Open then select the save file you created earlier
3. Now that you've loaded your File in PKHeX, go to the "SAV" tab and then we can start adding items
### Step 4: Add Items to Your Game
1. Click on "Items" and that will pop-up the inventory Editor. The pockets were mainly concerned with are the "Key Items" and "HMs & TMs" pockets
2. Whenever you get an HM, TM70 Flash, the Super Rod, Bicycle, or Dowsing MCHN you can save your game and load the file to add them to your game. However, I recommend addling them all at once and then just not using them until they are "sent" to you
3. To add an item click one of the empty slots and choose the item(s) you want
4. Once you add all your items **Be sure to click on the count for every item and set it to the amount of that item you want**, in most cases this will be one
5. Click Save on the inventory Editor window
### Step 5: Adding Badges
1. The only Badge that actually allows you to skip anything for adding it before the game normally gives it to you is the Legend Badge. That would allow you to skip the eighth gym and go straight to Victory Road
2. To add Badges, click the "Trainer Info" button and in the window that pops up check mark the Badge(s) you want then click save
### Step 6: Export Your Edited Save
1. Go to File and then Export SAV
2. Chose the save file that you loaded into PKHex (make sure the file type matches because the program defaults to .sav) and click Save
3. Open your game and, if you did everthing right, your bag will have whatever items you add
