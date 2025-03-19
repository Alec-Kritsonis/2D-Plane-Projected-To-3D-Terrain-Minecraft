import os
import mcworldlib as mc
from mcworldlib.anvil import RegionFile
from nbtlib import String
import nbtlib
import util

### This requires 5 unique blocks to be placed in the section as the palette needs to pull from block 5

def block_name(bid):
  return bid.split(':', 1)[-1].replace('_', ' ').title()

WORLD_PATH = "C:\\Users\\aleck\\AppData\\Roaming\\.fabric1.21\\saves\\world_geotiff"
# WORLD_PATH = "C:\\Users\\aleck\\AppData\\Roaming\\.fabric1.21\\saves\\MCA Test"
# MAP_Y = 31
MAP_Y = 135
BASE_BLOCK = 'minecraft:stone'
AIR_BLOCK = 'minecraft:air'

MAP_SECTION_CHUNK_Y = int(MAP_Y / util.SECTION_HEIGHT)
MAP_SECTION_CHUNK_Y_JSON = nbtlib.Byte(MAP_SECTION_CHUNK_Y)
MAP_SECTION_Y = MAP_Y % util.SECTION_HEIGHT

################################################################################
################################################################################
def get_map_section(chunk):
  map_section = None

  for section in chunk['sections']:
    if section['Y'] == MAP_SECTION_CHUNK_Y_JSON:
      map_section = section
      break

  if map_section == None:
    print(f"ERROR! Couldnt find map section for chunk {mc.pretty(chunk)}")

  return map_section

################################################################################
################################################################################
def get_map_blocks(chunk):
  section = get_map_section(chunk)

  palette, indexes = util.get_section_blocks(section)

  if palette is None or indexes is None:
    return

  # Debug chunk palette
  for i, p in enumerate(palette):
    bid = p['Name']
    props = f" {p['Properties']}" if p.get('Properties') else ""
    # print(f"{i:2d} = {block_name(bid)} [{bid}]{props}")

  map_plane = indexes[MAP_SECTION_Y]

  return [[palette[int(index)]['Name'] for index in row]
          for row in map_plane]

################################################################################
################################################################################
def overwrite_section(section, blocks_map):
  palette, indexes = util.get_section_blocks(section)

  if palette is None or indexes is None:
    return

  for y, sector_slice in enumerate(indexes, 0 * mc.util.SECTION_HEIGHT):
    # print(f"y={y}")
    for i, line in enumerate(sector_slice):
      for j, block_enum in enumerate(line):
        block_enum = int(block_enum)
        if str(palette[block_enum]['Name']) == BASE_BLOCK: # If terrain block is base block
          if blocks_map[i][j] != AIR_BLOCK:  # Dont overwrite if map block is air
            map_block = blocks_map[i][j]
            if not isInPalette(map_block, palette):  # Add new map block to section block list
              palette.append(nbtlib.Compound({'Name': nbtlib.String(map_block)}))
            index = next((i for i, compound in enumerate(palette) if str(compound['Name']) == map_block), -1)
            sector_slice[i][j] = index
    # print(sector_slice)

  indexes = indexes[:, ::-1, ::-1]
  encoded = util.encode_long_array(indexes, palette)
  # encoded = util._encode_blockstates(indexes, palette)

  section['block_states']['data'] = nbtlib.LongArray(encoded)
  section['block_states']['palette'] = palette

  # region.save()

################################################################################
################################################################################
def isInPalette(block_name, palette):
  return any(str(compound['Name']) == block_name for compound in palette)

################################################################################
# Main
################################################################################
if __name__ == "__main__":
  world = mc.load(WORLD_PATH)
  regions = world.regions[mc.OVERWORLD]

  for coords, region in regions.items():
  # region = regions[13, 9]
  # region = regions[1, 0]
  # chunk = region[30, 1]
  # chunk = region[2, 1]
    print(f"Working on region {coords}")
    for chunk in region.chunks:
      # print(f"\tWorking on chunk {chunk}")

      blocks_map = get_map_blocks(chunk)

      if blocks_map is not None: # Dont overwrite if there is no map
        # Traverse each section in a chunk and set BASE_BLOCKs to the block above it at y=MAP_Y
        for section in chunk['sections']:
          overwrite_section(section, blocks_map)

    region.save()
