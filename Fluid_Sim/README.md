# Fluid Simulation
Karla Sofía González Rodríguez | 0214774

## Description
The next code simulates the physics of fluid flows, it gives the user the capability to create multiple sources for velocity and density, animate the velocity forces, give color to the fluid and simulate the presence of rectangles and squares in the simulation.
All of this modifications can be done by an input file that will be described in the next section.


## Input file
In order to run the simulation a data.json file will be needed, it is easy just follow the next steps:

1. The first part shows the density, in which you will need to put 2 vectors and the value of them. You can see this part as trying to draw a figure, where (x0,y1) is the first point and (x1,y1) is the end of the figure. The amount will indicate how much will be the intensity of the figure displayed.

> (Feel free to add as much densities as you want)

```json
"density" : [
      {
        "x0" : 2,
        "x1" : 12,
        "y0" : 2,
        "y1" : 12,
        "amount1" : 550
      }
```
2. The second part of the input file is the velocity, where a vector of (x0,y0) will be needed and in order to give direction, rx0 and ry0 will be needed, this will indicate how the arrows will be moving. Besides you will also need to indicate the force of the velocity, you can choose between circular, linear, rotationY, rotationX.

> (Feel free to add as much velocities as you want and play with the forces)

```json
"velocity" : [
      {
        "x0" : 5,
        "y0" : 10,
        "rx0" : 5,
        "ry0" : 5,
        "force" : "circular"
      }
```

3. The third part are the colors, in this you can indicate between a list of example colors and simply modify the fluidColor part. You can check the following [link](https://matplotlib.org/stable/gallery/color/colormap_reference.html) for reference. Besides you can also modify the colors of the arrows of the velocity, for it you will need to use hexadecimal color values you can check the following [link](https://htmlcolorcodes.com/es/) for reference.

> (Feel free to play with the colors)

```json
"color" : [
      {
        "fluidColor" : "Pastel1_r",
        "arrows" : "#000000"
      }
    ]
```

4. Finally you can be able to add figures, in this case just rectangles and squares. To add them you need to put the position of it with (x,y) and you can give the width and height with w and h.

> (Feel free to add as much figures as you want)

```json
"objects" : [
      {
        "figure" : "Rectangle",
        "x" : 20,
        "y" : 25,
        "w" : 20,
        "h" : 10
      }
    ]
```

## Conclusion
As a conclusion I can say that I really liked the project since it is very visual and interactive, as you can play with the movement and the colors in order to create what you imagined. 
However I faced problems, for me the most dificult part was to think in the input file since I was thinking to use a txt file but they I started investigating and found how a json file works, which in this case was really useful. 
Also I had some trouble with the figures as I wanted to have multiple types of figures but at the end I just en up with squares and rectancles.

Further than that, I loved the result and the interaction that a user can have with the fluid simulation.
