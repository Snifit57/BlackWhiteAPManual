# Pokémon Black and White AP Manual
## About
A Manual Randomizer for use with Pokémon Black and White, for use with the [Archipelago Manual](https://github.com/ManualForArchipelago) Project. This Manual randomizes all ground items, HMs, Badges, and items given by important characters. Options are included to add hidden items as well as items from all the other NPCs. The latest stable release of the Manual AP World being in your Custom Worlds folder is required for this to work as expected.

This AP World assumes you know how to add items to your game using [PKHeX](https://github.com/kwsch/PKHeX) (brief tutorial is included below)

Shoutouts to Linneus and their [Pokémon Platinum Manual](https://github.com/Linneus/PlatinumAPManual/releases/tag/2.3) without out which I would not have been inspired to make this Manual or have the knowledge to add extra options.

## Why Play the Manual World Instead of the Traditional World?
*This is not meant to discredit the traditional world, the creator(s) put in a lot of time/effort, this is merely acknowledging that it is not complete yet*
- The traditional world is a lot more complicated and therfore still has a lot of issues to work out, the Manual is currently quite stable
- The Manual allows you to randomize the Pokemon in the game using the [Univeral Pokemon Ranomizer](https://github.com/Ajarmar/universal-pokemon-randomizer-zx/releases)
- Thw Manual allows you to turn off Abyssal Ruins items in post-game goals
- The Manual allows you to choose whether you should be expected to traverse dark areas without TM70 Flash or not
- The Manual allows you to toggle hidden items and optional NPC Items

## Check Rewards
- HMs
- TMs
- Badges
- Key Items
- Items from the "Items Pocket"
- Medicine Items
- Berries

## Logic Requirements
*These are the items you are expected to receive from the server in order to progress past certain points*
 - HM01 Cut to get past the tree in the Dreamyard and then proceed to Route 3 as well as checks behind other Cut trees
 - Insect Badge to access the area of Route 4 North of the Cheren fight
 - Bolt Badge to access Driftveil City
 - Light/Dark Stone to initiate the Bianca fight and proceed to Tubeline Bridge
 - HM03 Surf to get any checks that require you to Surf (Moor of Icirrus as well as two Route 8 checks require Surf due to the puddles freezing in Winter)
 - HM04 Strength to get checks behind Strength rocks
 - HM05 Waterfall to checks up Waterfalls (only one check for the two main-game goals)
 - TM70 Flash to get checks in dark caves
 - Completing the "Recieve Bicycle" Event check to access eastern Pinwheel forest
 - Resort Pass to access Desert Resort and Relic Castle if the `add_resort_pass` option is enabled
 - All eight Badges to access Victory Road, the Pokémon League, and N's Castle
 - `[EVENT] Defeat Elite Four` to get any check available after defeating Ghetsis and receiving the game's credits
 - HM03 Surf to access Giant Chasm
 - HM03 Surf and HM06 Dive to enter Abyssal Ruins if you turn on the `include_abyssal_ruins_items` option
 - Machine Part to 'repair' the 'blackout' affecting Marvelous Bridge, Route 15, Route 14, and Abundant Shrine therfore granting access to those areas and their checks
 - HM03 Surf and HM05 Waterfall to access Abundant Shrine

## Check Locations
### Always Available
- Items given by "important" NPCs
- Item balls you find on the ground
- HMs
- Badges
- Various events you complete throughout the game. (They will always give you the event as an item) These are just to help know what you gain access to upon completing the tasks.
### Available with options
- Hidden items
- Items given by all other NPCs
- Mistralton Cave items
- Abyssal Ruins items
- Post-game items

## Available Options
### Four Goal Options
- Defeat Ghetsis at N's Castle - The default goal where you collect eight Badges and receive the game's credits (ideal for long Syncs or short Asyncs)
- Defeat Cobalion at Mistralton Cave - A shorter goal that excludes all checks from Twist Mountain and beyond, where you collect four Badges and take down the Sword of Justice (ideal for Syncs)
- Defeat Cynthia at Undella Town - A goal similar to the Steven goal from Emerald where you complete the standard goal then go back in to fight a tough final boss (ideal for a moderate length Async)
- Become Champion - The longest goal that includes the entire post-game and requires you to collect the seven Sage's Wills and arrest the six Sages that were scattered by the fall of Ghetsis then rebattle the Elite Four (ideal for long Asyncs)
### Other Options
- Include NPC Items - Adds checks from all random NPCs that give items
- Randomize Hidden Items - Adds checks for the hidden items found throughout the game
- Require Dowsing MCHN - Makes it so you need to receive the Dowsing MCHN before you are logically required to pick up hidden items
- Require Flash - Rquires you to receive TM70 Flash before you are logically required to pick up items in or through dark areas
- Include Mistralton Cave Items - Adds Mistralton Cave checks to the pool. This option was added to improve the Cobalion goal by preventing you from having to go through the cave twice if this is set to "false"
- Add Resort Pass - Adds a new item you need to receive before having logical access to Desert Resort and Relic Castle
- Include Abyssal Ruins Items - Adds Abyssal Ruins checks to the pool if you are doing one of the two post-game goals

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
