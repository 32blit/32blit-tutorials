Title: C++ 1. Particle Effects
Date: 2021-07-02 14:00
Modified: 2021-07-02 14:00
Category: C++
Tags: c++, tutorial
Slug: c++-01-particle-effects
Authors: Jon Williamson
Summary: C++ Particle Effects on the 32Blit


- [Introduction](#introduction)
- [How do they work?](#how-do-they-work)
- [Before we start](#before-we-start)
- [An example in C++](#an-example-in-C)
- [Taking it further](#taking-it-further)

## Introduction

Particle effects are a great way to make your games feel richer or add interesting environmental mechanics. 

It's important to apply them with care, though, as overuse can make things confusing and distracting for the player. Treat them as the final layer of polish rather than the main focus and you can't go far wrong.

## How do they work?

The core concept behind implementing particle effects is to generate a collection of simple entities which have some sort of behaviour attached to them. For each frame rendered you update the entities based on their behaviour rules and draw them to screen.

> Each particle is a tiny little automaton that exists in your game world. They live and die by their own rules!

Take, for example, the weather.

We want to create a rain effect in our game to enhance the moodiness of an outdoor level. Often, to apply an effect like this, you would fake it by just drawing something that looks a bit like rain and animating it over the scene.

In our game, however, we want the rain to strike surfaces and bounce off, we want it to hit the protagonist and splash and pool. To achieve that we must create an approximate model of real water falling from a real sky.

## Before we start
When it comes to implementing our particle effect there are a few considerations we need to be aware of...

- **Quantity**: 
How many particles will we model at once? This decision is driven by the aesthetic you want to create, is it a torrential rain or just a light drizzle? It also has important ramifications for performance since each particle must be separately updated and drawn each frame.

- **Life-cycle**:
How long will our particles live? Since we can only have a fixed number of particles we need to decide how long they will exist for so that "expired" particles can be re-used.

> **32blit** has a powerful 400MHz processor so we can model some pretty complex behaviours and still smash out those frames.

- **Behaviour**:
We need to reduce our behaviour down to a simple set of rules which can be applied to each particle every frame. These rules ideally shouldn't involve a lot of complex maths since we will be potentially be processing them tens of thousands of times a second (for example if we have 250 particles on screen at 50 frames per second).

- **Appearance**:
Particles are a great opportunity to play with alpha blending and layering. As they cluster and separate based on the rules implemented you can create some really interesting interactions and create surprisingly realistic and organic feeling effects.

Once we have an idea of the answers to these questions things can start to take shape.

## An example in C++

In **32blit** we provide you with a pre-built particle generator, it's a module which manages the creation and lifecycle of your particles (the fiddly boring bit).

All you need to do is provide two small bits of code:

> Here we're using C++ but you can do exactly the same thing in Lua!

- **Setup function**: Sets up the initial position and velocity.
- **Update function**: Update the velocity (optional).

The particle generator takes care of the rest, constantly updating the particle positions and ages each time the game engine ticks and creating/destroying particles as required.

Let's take a look at how our rain could be implemented... 

```c++
void setup_rain(particle &p) {
    // new drops appear at the top of the screen
    p.pos.y = 0;            
    p.pos.x = (std::rand() % 120) + 100;    

    // travel at 100 pixels per second down the screen
    p.vel = vec2(0, 100);                   
}

void update_rain(particle &p) {
    // if the particle hits the bottom of the screen...
    if (p.pos.y >= 239) {
        p.pos.y = 239;
    }
}

uint16_t count = 250;
uint16_t lifetime = 4000; // 4 seconds
particle_generator rain(count, lifetime, setup_rain, update_rain);
```

When we come to render our frame we can just loop over the list of particles in the generator and draw them to the framebuffer however we want.

```c++
void render(uint32_t time_ms) {
    // raindrops keep falling on my head...
    fb.pen(rgba(128, 128, 255));
    for(auto &p : rain.particles) {
        fb.pixel(p.pos);
    }
}
```

And here's the result...

<video width="640" loop autoplay muted playsinline>
    <source src="simple-rain-1.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>*Just a few lines of code and it's pretty good!*

Et voila! We have a torrent of blue pixels falling down the screen and landing at the bottom. The lifetime of the particles means they also "pool" for a while before being removed and reused.

It's not bad but we can do so much more...

## Taking it further
This was a very simple example, all of our particles were the same, we didn't do any complicated collision detection, and we drew them as single blue pixels. Let's take this example much further by exploring:

- Collision detection against your game world
- Include gravity so that the particles accelerate over time
- Add a "bounce" to the rain drops when they hit the ground
- Draw elongated drops when moving faster
- Alpha blend the raindrops with the background scenery

Each of these improvements will make our rain effect more compelling and interesting.

<video width="640" loop autoplay muted playsinline>
    <source src="particle-effects.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>*In the tutorials we'll cover other effects*

See how the rain interacts with the logo in the corner, splashing on the top and dripping from the side. The same techniques are used to generate spark and smoke effects.