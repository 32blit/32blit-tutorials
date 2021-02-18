# 32blit Tutorials

## What are we doing?!

This course assumes a working knowledge of Lua and/or C++ programming, or a willingness to gain that knowledge elsewhere as you follow along. Much of the 32Blit API is simple enough that you can flesh out a basic idea without a deep understanding of either, but as your ideas and the resulting challenges evolve you will need to be competent in your language of choice.

We’ll be guiding you through the process of applying your programming knowledge to the challenge of making games. You’ll tackle some of the core concepts behind games reminiscent of the 8-bit and 16-bit eras and learn to identify and solve the technical components needed to bring your game idea to life. We will use some common tropes to hang these concepts around, but it will help if you have a game idea you’re keen to implement. 

## What are we *not* doing?

### We’re not teaching you to code

We won’t be teaching you how to code from scratch. There are plenty of good resources for that.
TODO: Link to resources.

### We’re not teaching you everything

Games programming is a rich and deep subject rife with arcane knowledge and weird edge-cases across a myriad platforms. The true scope of the subject boggles the mind, so we’re keeping things simple and not attempting to write a book. 32blit narrows things down to a single focus and gives us the opportunity to fast track you from coder to fledgling game-coder.

## Ready Player One

First, let’s get you set up with the basics you’ll need for the rest of this journey.

### IDE/Dev Environment

This will be personal to you as a developer, but we recommend using Visual Studio, Visual Studio Code, or just a plain Makefile and the command line. Either way, head to the Github README page for the 32blit SDK and follow the instructions for your platform:

https://github.com/32blit/32blit-sdk

#### What does this give you?

You’ll now be able to compile code so that it can be run on your OS - whether it’s Linux, Windows or macOS - and also turned into a binary - or “.blit” file - for the 32blit hardware.

### Bootstrapping your first project

To go with the grain of the 32blit ecosystem we recommend you use GitHub and start your project from our boilerplate - https://github.com/32blit/32blit-boilerplate/ - this starts you off with the right files, configuration and structure for your new 32blit game. It will also allow you to ship your game by publishing a release, and GitHub will do the hard work of building it for every supported platform.

## Concepts, planning and motivation

You’ll find it hard to succeed at making even the simplest of games if your motivation and end-goal are not clear. Have an idea for a game at the ready - even if it’s a simple one, or a different take upon something that already exists - and be prepared to see it through to completion.

As Tom DeMarco says in Peopleware “somewhere, today, an accounts payable system development is failing.” Even though accounting software has been a solved problem for decades, doesn’t mean that someone coming at the problem anew won’t founder or lose motivation.

We’ll guide you through the creation of three different genres of game, each of which you’ll have seen in a different form before, and each with their own unique technical challenges and considerations. A platformer, a Shmup and a puzzler. They cover a broad range of techniques and styles, which you can freely pull-apart and reuse  to make your own vision come to life as we go along. They will also exercise all the possibilities of the 32blit hardware and API.

If you’re struggling with motivation, we asked the pirate crew at Pimoroni if there was a nugget of an idea they wanted to create right now. Here are some of the answers we got. We hope they’re useful in sparking imagination:

Paul: *“I want a simple, chaotic, 8-player single-screen game where no-one is friends by the end of it. Gauntlet with a room full of tetchy leopards.”*

Phil: *“I want an arcade style fleet vs fleet, top-down pirate-ship combat game that’s all about lining up and landing your shots at speed.”*

These ideas will not come when you bid them to. They’ll appear at odd points. After waking from a weird dream or while doing something mundane that you look at in a new way for a moment. It’s important to capture these ideas as they come to you. If it isn’t written down, it might as well not exist. So have a little game ideas journal, or a note on your phone where you keep these nuggets. When you next sit down to code, you can break out the book, and pick an idea at random, and force yourself to make it happen, whether it’s the art, the motion, the logic, whatever bit of the idea is a challenge. Get your mind used to getting its hit of dopamine from solving these little problems, based on your ideas. You’ll grow as a creative coder.

## The Tutorials

### C++

1. [Particle Effects](c++/01-particle-effects/README.md)
2. [Path Finding](c++/02-path-finding/README.md)
3. [Multi-Channel Sound](c++/03-multi-channel-sound/README.md)
4. [2D Physics](c++/04-2d-physics/README.md)
5. [Enemy AI](c++/05-enemy-ai/README.md)
6. [Matrices & Transformation](c++/06-matrices-and-transformations/README.md)
7. [Drawing In 3D](c++/07-drawing-in-3d/README.md)
8. [Lighting Effects](c++/08-lighting-effects/README.md)
9. [Faking Mode 7](c++/09-faking-mode-7/README.md)
10. [Raycasting](c++/10-raycasting/README.md)
11. [Demo Effects](c++/11-demo-effects/README.md)
12. [Integrating Lua Scripts](c++/12-integrating-lua-scripts/README.md)

### Lua

1. [Drawing Shapes](lua/01-drawing-shapes/README.md)
2. [Working With Sprites](lua/02-working-with-sprites/README.md)
3. [Processing Input](lua/03-processing-input/README.md)
4. [Making Noise](lua/04-making-noise/README.md)
5. [Timers & Events](lua/05-timers-and-events/README.md)
6. [The Game Loop](lua/06-the-game-loop/README.md)
7. [Creating Menus](lua/07-creating-menus/README.md)
8. [Collision Detection](lua/08-collision-detection/README.md)
9. [Working With Maps](lua/09-working-with-maps/README.md)
10. [Structuring Your Code](lua/10-structuring-your-code/README.md)
11. [Vectors](lua/11-vectors/README.md)
12. [Saving Game State](lua/12-saving-game-state/README.md)