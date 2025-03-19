import os
import mcworldlib as mc
from mcworldlib.anvil import RegionFile
from nbtlib import String
import nbtlib
import util

### This requires 5 unique blocks to be placed in the section as the palette needs to pull from block 5

def block_name(bid):
  return bid.split(':', 1)[-1].replace('_', ' ').title()

WORLD_PATH = "C:\\Users\\aleck\\AppData\\Roaming\\.fabric1.21\\saves\\MCA Test"

world = mc.load(WORLD_PATH)
regions = world.regions[mc.OVERWORLD]

region = regions[1, 0]

chunk = region[1, 1]

found = False
sections = 0
Y = 0

for section in chunk['sections']:
  palette, indexes = util.get_section_blocks(section)
  # print(indexes)
  print(f"SECTION Y={Y}")
  for i, p in enumerate(palette):
    bid = p['Name']
    props = f" {p['Properties']}" if p.get('Properties') else ""
    print(f"{i:2d} = {block_name(bid)} [{bid}]{props}")
  print()
  for y, sector_slice in enumerate(indexes, Y * mc.util.SECTION_HEIGHT):
    print(f"y={y}")
    if y == 10:
      indexes[10][5][10] = 5
    print(sector_slice)
    print()
  print()
  encoded = util._encode_blockstates(indexes, palette)
  # print(encoded)
  section['block_states']['data'] = nbtlib.LongArray(encoded)
  break

print("SAVING")
region.save()
if found:
  print(f'All grass blocks converted to diamonds. Happy "mining"!')

