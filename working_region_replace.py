import os
import mcworldlib as mc
from mcworldlib.anvil import RegionFile
from nbtlib import String

WORLD_PATH = "C:\\Users\\aleck\\AppData\\Roaming\\.fabric1.21\\saves\\MCA Test"

world = mc.load(WORLD_PATH)
regions = world.regions[mc.OVERWORLD]

region = regions[0, -1]

chunk = region[1, 1]

found = False
sections = 0
for chunk in region.values():
  try:
    for section in chunk['sections']:
      palette = section['block_states']['palette']
      for block in palette:
        if block['Name'] == 'minecraft:grass_block':
          block['Name'] = String('minecraft:diamond_block')
          # if 'Properties' in block:
              # del block['Properties']
          sections += 1
          found = True
          break
  except:
    print(f"Skipping chunk")
if sections:
  print(f'Sections with grass blocks found in')
  region.save()
if found:
  print(f'All grass blocks converted to diamonds. Happy "mining"!')