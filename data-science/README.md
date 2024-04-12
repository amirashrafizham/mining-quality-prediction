### Summary
This dataset is about a flotation plant which is a process used to concentrate the iron ore. This process is very common in a mining plant.

Reference: [Kaggle](https://www.kaggle.com/edumagalhaes/quality-prediction-in-a-mining-process)

## What is froth flotation?
Imagine you have a magical bubble bath with tiny boats and colorful pebbles floating around. 🛁🚤🌈 Now, let’s talk about froth flotation, which is like a special bubble bath for minerals! 🌊💎

- Magical Minerals: Imagine we have a treasure chest full of different shiny rocks (minerals). Some are gold, some are silver, and some are just plain rocks. But we want only the precious ones!
- Making Minerals Float: First, we sprinkle a special powder on these rocks. This powder makes the rocks feel a little scared of water (we call it “hydrophobic”). Just like how you might not want to get wet in the rain, these rocks don’t want to touch water either! 🙅‍♂️💧
- Bubble Friends: Next, we blow tiny bubbles into our magical bubble bath. These bubbles are like little boats that sail through the water. But guess what? The scared rocks (our precious minerals) love these bubbles! They hop onto the bubbles and hold on tight. 🚢🪶
- Floating to the Top: The bubbles rise to the surface, carrying our precious minerals with them. It’s like an elevator ride for the rocks! They reach the top and form a fluffy layer called “froth.” 🛁🪶
- Collecting the Treasure: We scoop up this frothy layer and gently separate it from the rest of the water. And voilà! We’ve separated the valuable minerals from the plain rocks. 🎉💎

But how does it apply to our world of minerals? Let’s take a closer look at the minerals we’re dealing with:

- Silica (SiO₂): Imagine silica as tiny beach sand grains. In the world of minerals, silica is like the sand you find on the shore. It’s everywhere! But sometimes, we want to get rid of it because it hangs out with our precious minerals (like iron) and makes them less valuable.
- Iron (Fe): Iron is our treasure! It’s like gold or silver hidden in the sand. But here’s the tricky part: iron often hangs out with silica. They’re like best buddies at the mineral beach party.

Froth Flotation Magic: Now, froth flotation steps in. It’s like a magical bubble bath for minerals. Here’s how it works:
- Bubbles and Minerals: We blow tiny bubbles into our mineral mix (the beach sand). These bubbles are like little boats sailing through water. Guess what? Our precious iron minerals love these bubbles! They hop onto the bubbles and hold on tight. 🚢🪶
- Floating to the Top: The bubbles rise to the surface, carrying our iron buddies with them. It’s like an elevator ride for the iron grains. They reach the top and form a fluffy layer called “froth.” 🛁🪶
- Goodbye, Silica!: But wait, what about the pesky silica? Well, it doesn’t like bubbles. So, it stays behind, sulking in the water. We scoop up the frothy layer (with our iron) and gently remove it. And guess what? We’ve separated the valuable iron from the not-so-valuable silica! 🎉💎

### Froth Flotation Process Diagram

![Froth Flotation](https://cdn1.byjus.com/wp-content/uploads/2021/04/Froth-Flotation-Process-3.png)
![Froth Flotation](https://ars.els-cdn.com/content/image/3-s2.0-B9780128218754000110-f03-10-9780128218754.jpg)

### Goal of this dataset
The target is to predict the % of Silica in the end of the process, which is the concentrate of iron ore and its impurity (which is the % of Silica).

### Why prediction is needed
Although the % of Silica is measured (last column), its a lab measurement, which means that it takes at least one hour for the process engineers to have this value. So if it is posible to predict the amount of impurity in the process

### Column Details
- % Iron Feed -> % of Iron that comes from the iron ore that is being fed into the flotation cells
- % Silica Feed -> % of silica (impurity) that comes from the iron ore that is being fed into the flotation cells
- Starch Flow -> Starch (reagent) Flow measured in m3/h
- Amina Flow -> Amina (reagent) Flow measured in m3/h
- Ore Pulp Flow -> t/h
- Ore Pulp pH -> pH scale from 0 to 14
- Ore Pulp Density -> Density scale from 1 to 3 kg/cm³
- Flotation Column 01 Air Flow -> Air flow that goes into the flotation cell measured in Nm³/h
- Flotation Column 02 Air Flow -> Air flow that goes into the flotation cell measured in Nm³/h
- Flotation Column 03 Air Flow -> Air flow that goes into the flotation cell measured in Nm³/h
- Flotation Column 04 Air Flow -> Air flow that goes into the flotation cell measured in Nm³/h
- Flotation Column 05 Air Flow -> Air flow that goes into the flotation cell measured in Nm³/h
- Flotation Column 06 Air Flow -> Air flow that goes into the flotation cell measured in Nm³/h
- Flotation Column 07 Air Flow -> Air flow that goes into the flotation cell measured in Nm³/h
- Flotation Column 01 Level -> Froth level in the flotation cell measured in mm (millimeters)
- Flotation Column 02 Level -> Froth level in the flotation cell measured in mm (millimeters)
- Flotation Column 03 Level -> Froth level in the flotation cell measured in mm (millimeters)
- Flotation Column 04 Level -> Froth level in the flotation cell measured in mm (millimeters)
- Flotation Column 05 Level -> Froth level in the flotation cell measured in mm (millimeters)
- Flotation Column 06 Level -> Froth level in the flotation cell measured in mm (millimeters)
- Flotation Column 07 Level -> Froth level in the flotation cell measured in mm (millimeters)
- % Iron Concentrate -> % of Iron which represents how much iron is presented in the end of the flotation process (0-100%, lab measurement)
- % Silica Concentrate -> % of silica which represents how much iron is presented in the end of the flotation process (0-100%, lab measurement)