---
layout: post
title:  "32blit - Screen Modes"
article: "A guide to screen modes"
date:   2019-05-23 09:00:00 +0000
categories: introduction
published: false
---
# 32blit - Screen Modes

Since the Apple II debuted with a whopping 6 colours in its 280x192 "High-res" mode and 16 in its 40x48 Low-res mode, the tradeoff between colour fidelity, performance and resolution has remained a constant in computer graphics. Computers quickly saw leaps to 16, 256 and 65K colours but were still subject to memory constraints that made creating and storing artwork using anything more than a handful of colours impossible.

On early hardware - in video modes such as CGA and EGA - a colour palette - which is conceptually similar to an artist's physical palette of paints - would be "baked in" to the computer, selected at design-time due to hardware limitations, business decisions or other technicalities.

When VGA rolled around it allowed a 256-colour palette to be selected from around 65,000 colours by the artist. This was still a limitation, but the ability to select from a larger pool of colours meant games could vary their tone and visual style more widely. This colour-palette goverened which of these colours a game could use, and compressed what might otherwise be 16-bits of RGB colour information into a single, 8-bit index pointing at a colour in the palette. This limited set of 256 values, and the way they're represented in memory, is the namesake of "8-bit" era videogame graphics.

On more modern hardware a colour-palette is selected from the millions of colours that the display hardware is capable of displaying and is chosen by artists attempting to limit themselves and capture some of the magic of the 8-bit era. Incredible things can be done within these limitations. If you've ever watched an animated gif on the internet you'll have been looking at an under-construction banner, meme or video that's comprised of just that- a mere 256 colours.

## Limitations & Classic Computer Art

The need to produce artwork from a constrained palette containing a handful of colours inspired some creative workarounds and resulted in artwork with the distinctly "retro" character we can point to today.

To compound this, early colour palettes were chosen by engineers, with the technical limitations of hardware in mind, and not by artists. This often led to some pretty garish and, to the untrained eye, worthless colour choices. CGA and EGA were particularly egregious examples of this.

In a nod to human inginuity when confronted with limitations, artists managed to coax visual magic out of these few colours. Here's an EGA-colour scene from 1990s DOS point and click adventure "The Secret Of Monkey Island", illustrated by Mark Ferrari:

![Monkey Island](secret-of-monkey-island-dos-ega.png)

> "The most creative work I ever did, was done when I had just those 16 horrible colours to do it in."

* Mark Ferrari - https://youtu.be/aMcJ1Jvtef0?t=266

Here's that same scene as if it were displayed on a CGA graphics card. This one isn't quite so magic:

![Monkey Island](secret-of-monkey-island-dos-ega-in-cga.png)

# Choosing The Right Screen Modes For 32blit (working title)

Being built around an ARM microcontroller, 32blit must also strike a balance between resolution and colour format to reserve as much RAM as possible for your game logic, and as much CPU time as possible to keep the framerate stable and your games smooth.

32blit supports two resolutions a 160x120, RGB-colour standard mode, and a 320x240, 256-colour high-resolution mode.

These modes are chosen specifically to give you two clear choices for your games, each with different trade-offs. The high-resolution mode is faithful to classic gaming systems, challenging you to prepare your assets carefully and produce something that looks and feels like a true 8-bit retro classic. The low-resolution mode sacrifices resolution for such luxuries as full RGB colour and alpha blending, allowing you to produce vibrant visual effects that would have been difficult or impossible on early hardware.

## 160x120, RGB-colour Standard Mode

Harking back to the Apple II again, its 40 by 48 pixel mode gave developers about two and a half times as many colours to work with than the high resolution mode. With 32blit the drop in resolution gives us over 65,000 times as many colours as the 256-colour high-resolution mode.

Indeed in 160x120 mode the display supports full RGB colour, commonly known as 24-bit or "True Color". That's around 16 million colours. Alone this would occupy 57,600 bytes of memory at 24-bits per pixel. We've packed an 8-bit alpha mask into this buffer bringing it up to 76,800 bytes and nicely aligning our pixels into 32-bit integers (8-bits red, green and blue, plus 8-bits alpha). Curiously this is the same amount of memory as our 256-colour high resolution mode, which is a convinient decision to make when slicing the microcontroller memory up into logical portions for the different parts of the system.

The 160x120 surface that your game draws upon is then pixel-doubled into the display buffer. In practise this means that each game pixel occupies four pixels on the screen, since it has doubled both horizontally and vertically in size. It doesn't cost you any additional processing time or effort to perform this step, since the pixels need copied to the display buffer anyway.

This might sound like an awful waste of perfectly good LCD resolution but it's surprising what detail you can pack into 160x120; the reduction in pixel count means you can afford to put a lot more processing behind every pixel in your game.

Let's see how Secret Of Monkey Island might look at 160x120:

![Monkey Island](secret-of-monkey-island-160-120.png)

The original game actually rendered at 320x200, so we're seeing just over a quarter of the screen but there's still more than enough room to set the scene and position our character. A point and click adventure could work at this resolution, but it would have to get clever with the user interface since there's not much room for text.

What about another style of game? Let's take Sonic 2 - originally displayed at 320x244 or 320x240 on the Genesis/Megadrive - and re-imagine it to 160x120:

![Sonic 2](sonic-2-160-120.png)

In this case the text denoting score, time, rings and remaining lives is taking up proportionally more of the screen so that it's readable, but not so much that it's not clear what's going on in the game. This is pretty much how Sonic translated to the GameGear which had a screen resolution of 160x144 pixels- tantilizingly close to 32blit. A re-imagining of Sonic 1 from the GameGear is pretty trivial:

![Sonic 1 GG](sonic-1-gg-160-120.png)

None of these examples, however, take advantage of true colour and alpha-blended layers. To see how that might look in what's effectively a modern-retro game (and not "real" 8-bit) here's a sample of our platformer:

![Platformer](platformer-160-120.png)

These type of games with little on-screen text and no need for complex user-interfaces or intricately detailed graphics are best suited for 32blit's 160x120 mode. This could include Kart Racers, SHMUPs, Platformers and Fighters. Artists seeking to capture a retro-aesthetic will need to be careful not to get carried away with colours, instead using the powerful realtime lighting and visual effects that this mode makes available to bring atmosphere to their 8-bittish art.

## 320x240, 256-colour High Resolution Mode

In 320x240 mode each pixel is an 8-bit number indexed into a 256-colour palette. As luck would have it, this also occupies 76,800 bytes.

In classic computer terms our 320x240 mode is very similar to the Mode 13h from VGA graphics hardware circa 1987. Mode 13h supported 256 colours at 320x200 pixels and played home to classics such as the aforementioned The Secret Of Monkey Island, Command & Conquer, Commander Keen and Tyrian.

The pixels of Mode 13h were stretched vertically when displayed on a 4:3 CRT screen, but 32blit's 320x240 resolution - with 40 additional horizontal lines - fits perfectly on its 4:3 LCD giving predictably square pixels and some additional screen real-estate which those classic titles lacked.

A 256-colour palette brings in some interesting restrictions and benefits. We lose alpha blending because we can't guarantee that the blended result of two colours will actually *be* in your palette. But what we gain from not having to worry about alpha blending is raw, blistering speed. This is important, since we're dealing with four times as many pixels. This doesn't mean you can't be smart about your visual style and effects- using colours in your palette to create transparent windows- but does mean there's a little extra challenge to accomplishing this.

Along with speed we gain classic palette-twiddling magic which we can use to add animation and visual effects very cheaply. For example- by just rotating a reserved set of colours, you can make a static torch appear to be burning.

Let's see how Secret Of Monkey Island might look at 320x240:

![Monkey Island](secret-of-monkey-island-320-240.png)

Whoa! It's clear to see that- despite the loss of alpha blending and a restrictive colour palette- the 320x240 mode offers some clear advantages for games dealing with lots of text, highly detailed scenes or complex user interfaces. Point and click adventures are a classic example of this, but you might also use this mode for - for example - RPGs, Text Adventures, Strategy Games and Top-down Racers.

Faking transparent surfaces or liquids isn't impossible, though. You might reserve 3 sets of 8 colours for your characters to handle how they look normally, behind glass and under water effectively calculating your alpha blending up-front and applying a little artistic fine-tuning. Once you've set this up, you can shift your palette to underwater by just adding the right offset to each pixel's palette index.

![Mech Pre Alpha](mech-pre-alpha-blending.png)

32blit's 256 colour mode isn't without some modern accomodations. You can pick those 256 colours from the full 16 million available in true-colour and you can swap them out between scenes or even frames to completely change the look and feel of your game. For example you might reserve 64 colours for common items- UI, characters and objects, but swap out another 64 depending on which background you're drawing. Adjusting the saturation and brightness of your background colours could even give you day/night effects from the same image.

For example here's a snowy scene rendered by crunching a photo to just 64 colours:

![Snowy Scene](snowy-scene-64-color-320-240.png)

And by swapping out those for another 64 colours we can suddenly draw blue skies and rolling hills:

![Snowy Scene](rolling-hills-64-color-320-240.png)

And, surprisingly, we can also render that snowy castle scene pretty convincingly using the rolling hills colour palette:

![Snowy Scene](snowy-scene-64-color-with-rolling-hills-palette-320-240.png)

And we can even transform our green rolling hills into a sun-scorched tundra by using our snowy scene colour palette:

![Rolling Hills](rolling-hills-64-color-320-240-with-snowy-scene-palette.png)

Palettes are cool!

A 64-colour (6-bits per pixel) backdrop image would take up around 57k of storage, including its colour table. Crunched to 16-colours (4-bits per pixel) the same image retains much of its character but fits into around 38k. With some careful palette choices and rough tweaks to the image we can even crunch this down to 8-colours (3-bits per pixel) - getting some pretty convincing results for a photo that's just been quantized - and squeeze it under 29k.

![Snowy Scene](snowy-scene-8-color-320-240.png)

How you break down your 256-colour palette, and how and when you swap or cycle colours is entirely up to you.