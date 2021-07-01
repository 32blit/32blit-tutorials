# Case Study - Rocks 'n' Diamonds
Boulderdash was a seminal game for the 8-bit era. It spawned many clones, but not quite as polished as the original, which leaned into the limitations of the colour pallets and capabilities of the platform to create a lean aesthetic that very much counted as 'tasteful' for the era. Clones often added more detailed sprites, more colours and animation to the detriment of the core gameplay. You can read more on the process at [Retro Gamer](https://www.retrogamer.net/retro_games80/the-making-of-boulder-dash/).

Here we're going to recreate the essence the gameplay. It's notable for having a fairly simple structure and mechanics that rely on block-level calculations and very little in the way of animation. It makes for a clear and fast-paced game which has some nuance through excellent level design that involves random generation with specific design elements overlaid for sparse level data. Small puzzles emerge around avoiding getting trapped or killed while collecting or generating enough diamonds.

The key concepts we'll cover here will be:

- Random generation
- Setting up the playfield
- Tile-level game mechanics
- Game and player states

# Random generation

We don't want to necessarily have to design each level by hand. We can just say "We want so many rocks, diamonds and dirt." and then tweak the bits we care about. Since we want the levels to be the same each time (for now), we need deterministic randomness. Then when we get a playable level, it won't potentially break on us, by being randomly unplayable.

## Seeds of construction



## Gilding the level



# Game and player states

We start by setting up the stages of world creation, running and end states, and what the player and world can be doing in each of these states. What do we need to cover? Is the player alive or dead? Do we need to store state on the tiles of the map, or can we just rely on their location in each tick to determine what each tile should be doing? Have we got enough diamonds to complete the level?

# Tile-level game mechanics

Now we have a map, we need to make the logic for how things like boulder/diamond physics work, and how the player moves through dirt and collects diamonds. This is controlled through the state of the map, and then applying the rules on each tick of the world clock.

## Player Mechanics

There are a couple of things to wire up here. Inputs to player movements. Interactions with boulders and diamonds, be it pushing, collecting, being stopped by or being crushed by them.

## Boulder and Diamond Physics

What happens on each tick of the world clock is determined solely by the tiles. Are they sitting on dirt, air, or another diamond/boulder? Are they falling or not? From this all we need to do is update the state of the tiles, calculate any consequences and render the world through the camera.

Now we have the bones of a working game with very little in the way of complexity.

# What Next?

While we've set up some basics here, we've left a lot for you to take a swing at and learn from. Either by recreating features from the original Boulder Dash and clones, or adding your own nuance to the engine based on which skills you want to develop.

## Enemies
As it stands, gravity is your only enemy. Maybe you could add some enemies. Either dumb ones that follow simple rules (Travel though air and always turn left. Explodes when hit by rock/diamond), or even exhibit some basic intelligence such as always heading towards the player. Play around to see which concepts work and don't. Look at examples of how other classic enemies work. Do you know how the [Ghosts in Pac-Man function](https://www.youtube.com/watch?v=ataGotQ7ir8&ab_channel=RetroGameMechanicsExplained)?

## Power-ups
How about adding abilities to your player? Is it fun if they can sometimes run faster, push two boulders maybe? Run through walls? How do get these bonuses? Do they make room for new and better puzzles?

## Art Attack
Maybe you want to enhance the aesthetic of the game? Can you redraw the sprites to make the game underwater themed? Space themed? Can you change the physics a little so the main character is swimming and has inertia and splat if they go too deep? This could add nuances and new level styles to the game. Or it could suck. Have a go!
