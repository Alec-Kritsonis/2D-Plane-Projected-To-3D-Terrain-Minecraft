# 2D-Plane-Projected-To-3D-Terrain-Minecraft

### Description

Project a 2D plane downwards onto a 3D base terrain

### Example Image:

This is taking a 2D pixel art in-world schematic (check out my image to schematic program https://github.com/Alec-Kritsonis/litematica-pixelart) and projecting it to a lidar map of terrain below.

![alt text](https://github.com/Alec-Kritsonis/2D-Plane-Projected-To-3D-Terrain-Minecraft/blob/main/images/Example%202D%20to%203D%20Mapping.png?raw=true)

### Details:

This will take a plane at a specific Y level and replace any base blocks (I used stone here) in that column, above and below, to the block at the Y level. This works by modifying the region files directly. This was stupid, and I tried every other way to project a plane onto terrain I could think of yet here we are. It works.

### Code Stuffs:

This is on python 3.12.2

Doing `pip freeze` yielded these for my packages:

mcworldlib==2023.7.13

numpy==2.0.2

nbtlib==2.0.4

The "NBT Viewer" extension by Misode helped a ton to debug.