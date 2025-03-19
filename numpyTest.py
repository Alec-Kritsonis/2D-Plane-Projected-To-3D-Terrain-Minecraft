import math
import numpy as np

# 25 blocks in palette
data = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,111573012255342592,253362875110886499,187079982645873763,291717033926886432,111578750331981955,325420474483084387,227576100944972903,111573048831804448,111888538068522148,44332839744048227,632247226842844267,652005013946672352,147881059492187761,43981068065508451,817036201889500193,111609372376074464,109248886468261608,332422088294075524,153407268354894881,112735241144474720,73220163402571875,111773061252,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# 4 blocks in palette
# data = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8589938688,8591052800,8591052800,13693419523,3517578412080,219851785008,3311473471491,3505501974531,50331699,13740737280,3505549160496])

# 2 block in palette
# data = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

# 3 blocks in palette
# data = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2])

# 4 blocks in palette
# data = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3])

pack_bits = data.itemsize * 8

# Define constants
BS_MIN_BITS = 4
BS_INDEXES = 4096  # Small number of block states for test
bits = 5  # Number of bits per block state index (for example, 5 bits)
SECTION_HEIGHT = 16
CHUNK_SIZE = (16, 16)

################################################################################
################################################################################
def mine():
  unpacked = np.unpackbits(
    data[::-1].astype(f">i{pack_bits//8}").view(f"uint{pack_bits//8}")
  )
  print(f"\nUnpadded Bits: {unpacked.size}")
  np.set_printoptions(threshold=np.inf)
  print(unpacked)

  pad_length = (bits - (len(unpacked) % bits)) % bits  # Calculate how many bits to pad
  padded = np.pad(unpacked, (0, pad_length), mode="constant")
  print(f"\nPadded Bits: {padded.size}")
  print(padded)

  # Reshape the padded bits into rows of 'bits' length
  reshaped = padded.reshape(-1, bits)
  print(f"\nReshaped Bits (5 bits per index): {reshaped.shape}")
  # print(reshaped)

  # Pack the reshaped bits back into bytes
  packed = np.packbits(reshaped)
  print(f"\nPacked Bits: {packed.size}")
  print(packed)

  # Pad the packed bits so that the total size is divisible by 8 (required for 64-bit ints)
  if len(packed) % 8 != 0:
    packed = np.pad(packed, (0, 8 - len(packed) % 8), mode="constant")
    print(f"\nPadded Packed Bits: {packed.size}")
    print(packed)

  # Convert packed bits to 64-bit integers (int64)
  indexes = packed.view(dtype=">q")[::-1]  # Reverse to match the Minecraft format
  print(f"\nFinal Block State Indexes: {indexes.size}")
  print(indexes)

  # Ensure the indexes have exactly 4096 block states (for a 16x16x16 chunk)
  # If the number of indexes is less than 4096, pad it with zeros
  if len(indexes) < BS_INDEXES:
    indexes = np.pad(indexes, (0, BS_INDEXES - len(indexes)), mode="constant")
    print(f"\nPadded Block State Indexes to 4096: {indexes.size}")

  indexes = indexes.reshape((SECTION_HEIGHT, *reversed(CHUNK_SIZE)))
  # print(indexes)

################################################################################
################################################################################
def _decode_blockstates():
  unpacked = np.unpackbits(
    data[::-1].astype(f">i{pack_bits//8}").view(f"uint{pack_bits//8}")
  )
  print(f"\nUnpadded Bits: {unpacked.size}")
  np.set_printoptions(threshold=np.inf)
  print(unpacked)

  padded = np.pad(
    unpacked.reshape(-1, bits),
    [(0, 0), (pack_bits - bits, 0)],
    "constant"
  )
  print(f"\nPadded Bits: {padded.size}")
  print(padded)

  packed = np.packbits(padded)
  print(f"\nPacked Bits: {packed.size}")
  print(packed)

  indexes = packed.view(dtype=">q")[::-1]
  print(f"\nFinal Block State Indexes: {indexes.size}")
  print(indexes)

  indexes = indexes.reshape((SECTION_HEIGHT, *reversed(CHUNK_SIZE)))
  # print(indexes)

################################################################################
################################################################################
def decode_long_array(
    long_array: np.ndarray,
    size: int,
    bits_per_entry: int,
    dense=True,
    signed: bool = False,
) -> np.ndarray:
    """
    Decode a long array (from BlockStates or Heightmaps)

    :param long_array: Encoded long array
    :param size: The expected size of the returned array
    :param bits_per_entry: The number of bits per entry in the encoded array.
    :param dense: If true the long arrays will be treated as a bit stream. If false they are distinct values with padding
    :param signed: Should the returned array be signed.
    :return: Decoded array as numpy array
    """
    # validate the inputs and throw an error if there is a problem
    if not isinstance(bits_per_entry, int):
        raise ValueError(f"The bits_per_entry input must be an int.")

    assert (
        1 <= bits_per_entry <= 64
    ), f"bits_per_entry must be between 1 and 64 inclusive. Got {bits_per_entry}"

    # force the array to be a signed long array
    long_array = long_array.astype(">q")

    if dense:
        expected_len = math.ceil(size * bits_per_entry / 64)
    else:
        expected_len = math.ceil(size / (64 // bits_per_entry))
    if len(long_array) != expected_len:
        raise Exception(
            f"{'Dense e' if dense else 'E'}ncoded long array with {bits_per_entry} bits per entry should contain {expected_len} longs but got {len(long_array)}."
        )

    # unpack the long array into a bit array
    bits = np.unpackbits(long_array[::-1].astype(">i8").view("uint8"))
    if dense:
        if bits.size % bits_per_entry:
            # if the array is densely packed and there is extra padding, remove it
            bits = bits[bits.size % bits_per_entry :]
    else:
        # if not densely packed remove the padding per long
        entry_per_long = 64 // bits_per_entry
        bits = bits.reshape(-1, 64)[:, -entry_per_long * bits_per_entry :]

    byte_length = 2 ** math.ceil(math.log(math.ceil(bits_per_entry / 8), 2))
    dtype = {1: "B", 2: ">H", 4: ">I", 8: ">Q"}[byte_length]

    # pad the bits to fill one of the above data types
    arr = np.packbits(
        np.pad(
            bits.reshape(-1, bits_per_entry)[-size:, :],
            [(0, 0), (byte_length * 8 - bits_per_entry, 0)],
            "constant",
        )
    ).view(dtype=dtype)[::-1]
    if signed:
        # convert to a signed array if requested
        sarray = arr.astype({1: "b", 2: ">h", 4: ">i", 8: ">q"}[byte_length])
        if bits_per_entry < 64:
            mask = arr >= 2 ** (bits_per_entry - 1)
            sarray[mask] = np.subtract(
                arr[mask], 2**bits_per_entry, dtype=np.int64
            )
        arr = sarray
    return arr

################################################################################
# Main
################################################################################
if __name__ == "__main__":
  np.set_printoptions(threshold=np.inf)

  # mine()
  # _decode_blockstates()
  print(decode_long_array(data, 16 * 16 * 16, bits, dense=False))