# Case Study - Rocks 'n' Diamonds
Boulderdash was a seminal game for the 8-bit era. It spawned many clones, but not quite as polished as the original, which leaned into the limitations of the colour pallets and capabilities of the platform to create a lean aesthetic that very much counted as 'tasteful' for the era. Clones often added more detailed sprites, more colours and animation to the detriment of the core gameplay.

Here we're going to recreate the essence the gameplay. It's notable for having a fairly simple structure and mechanics that rely on block-level calculations and very little in the way of animation. It makes for a clear and fast-paced game which has some nuance through excellent level design that involves random generation for sparse level data and includes small puzzles around avoiding getting trapped or killed while collecting enough diamonds.

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

What happens on each tick of the world clock is determined almost solely by the position of the tiles once any player interactions are calculated. Are they sitting on dirt, air, or another diamond/boulder? So all we need to do then is update the state of the tiles, calculate any consequences and render the world through the camera.

Now we have the bones of a working game with very little in the way of complexity.
