# The Hero Arrives In 35 Minutes

The battle system used in the game is available as an example for anyone who wants to roll their own turn-based battle system in Ren'Py.

A description and download for the game is available at: https://jsfehler.itch.io/the-hero-arrives-in-35-minutes

The primary concern was building some sort of workable scripting system for enemies.
In the game, the player's character is also controlled using this script, creating a fully automatic battle (ie: AI vs AI). However, building your own menu system to directly control the player's actions is not impossible.

In a nutshell:

- The Actor class contains information about stats, equipment, and other information about each participant in a battle.
- An Actor must be created for each character appearing in a battle
- Every Actor has one or more BattleRules.
- Every BattleRule: 
  - Watches an Actor or group of Actors
  - Has a Condition that must be met to be activated
  - Has a BattleAction that is used on the condition being met
  - Has a target for that BattleAction  
- Actors must be added to a BattleActors group. BattleActors are used in the battle screens and loop.
