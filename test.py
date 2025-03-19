import os
import mcworldlib as mc
from mcworldlib.anvil import RegionFile
from nbtlib import String

WORLD_PATH = "C:\\Users\\aleck\\AppData\\Roaming\\.fabric1.21\\saves\\MCA Test"

world = mc.load(WORLD_PATH)
regions = world.regions[mc.OVERWORLD]

region = regions[1, 0]

chunk = region[1, 1]

found = False
sections = 0

try:
  # A dictionary to store the highest block in each (x, z) column
  highest_blocks = {}

  for section in chunk['sections']:
    if section['Y'] == '-4b':
      map_plane_section = section
    else:
      continue

    palette = section['block_states']['palette']
    highest_block = palette[-1]

    block_name = highest_block['Name']

    # Update the highest block for this (x, z) column
    if (x, z) not in highest_blocks or y > highest_blocks[(x, z)][0]:
      highest_blocks[(x, z)] = (y, block_name)
      print(block_name)

  # Second pass: Replace all blocks in the column with the highest one
  # for section in chunk['sections']:
  #     y_base = section['Y'] * 16  # Base Y level of the section
  #     if 'block_states' not in section:
  #         continue

  #     block_states = section['block_states']

  #     for index, block in enumerate(block_states['data']):
  #         x = (index // 16) % 16
  #         y = (index % 16) + y_base
  #         z = (index // 256) % 16

  #         if (x, z) in highest_blocks:
  #             highest_name = highest_blocks[(x, z)][1]

  #             # Find the corresponding index in the palette
  #             for i, palette_entry in enumerate(block_states['palette']):
  #                 if palette_entry['Name'] == highest_name:
  #                     block_states['data'][index] = i
  #                     break

except KeyError as e:
    print(f"Skipping chunk due to missing key: {e}")


region.save()
if found:
  print(f'All grass blocks converted to diamonds. Happy "mining"!')