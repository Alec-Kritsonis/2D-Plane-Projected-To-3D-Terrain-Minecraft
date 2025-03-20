### This is me/chatgpt rewiritng part of the mcworldlib library code cause its out of date. Ew.

import math
import numpy as np

BS_MIN_BITS = 4
BS_INDEXES = 4096
SECTION_HEIGHT = 16
CHUNK_SIZE = (16, 16)

def decode_long_array(
    data: np.ndarray,
    size: int,
    palette=None,
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
    pack_bits = data.itemsize * 8  # 64 bits for each Long Array element
    dense = False
    signed = False

    bits_per_entry = bits_per_index(data, palette, pack_bits)

    # validate the inputs and throw an error if there is a problem
    if not isinstance(bits_per_entry, int):
        raise ValueError(f"The bits_per_entry input must be an int.")

    assert (
        1 <= bits_per_entry <= 64
    ), f"bits_per_entry must be between 1 and 64 inclusive. Got {bits_per_entry}"

    # force the array to be a signed long array
    data = data.astype(">q")

    if dense:
        expected_len = math.ceil(size * bits_per_entry / 64)
    else:
        expected_len = math.ceil(size / (64 // bits_per_entry))
    if len(data) != expected_len:
        raise Exception(
            f"{'Dense e' if dense else 'E'}ncoded long array with {bits_per_entry} bits per entry should contain {expected_len} longs but got {len(data)}."
        )

    # unpack the long array into a bit array
    bits = np.unpackbits(data[::-1].astype(">i8").view("uint8"))
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

def encode_long_array(
    data: np.ndarray,
    palette=None,
    dense: bool = True,
    min_bits_per_entry=1,
) -> np.ndarray:
    """
    Encode a long array (from BlockStates or Heightmaps)

    :param array: A numpy array of the data to be encoded.
    :param bits_per_entry: The number of bits to use to store each value. If left as None will use the smallest bits per entry.
    :param dense: If true the long arrays will be treated as a bit stream. If false they are distinct values with padding
    :param min_bits_per_entry: The mimimum value that bits_per_entry can be. If it is less than this it will be capped at this value.
    :return: Encoded array as numpy array
    """
    dense = False
    pack_bits = data.itemsize * 8

    bits_per_entry = bits_per_index(data, palette, pack_bits)

    assert (
        1 <= min_bits_per_entry <= 64
    ), f"min_bits_per_entry must be between 1 and 64 inclusive. Got {bits_per_entry}"
    # cast to a signed longlong array
    data = data.astype(">q")
    # work out how many bits are required to store the
    required_bits_per_entry = max(
        max(
            int(np.amin(data)).bit_length(),
            int(np.amax(data)).bit_length(),
        ),
        min_bits_per_entry,
    )
    if bits_per_entry is None:
        # if a bit depth has not been requested use the minimum required
        bits_per_entry = required_bits_per_entry
    elif isinstance(bits_per_entry, int):
        assert (
            1 <= bits_per_entry <= 64
        ), f"bits_per_entry must be between 1 and 64 inclusive. Got {bits_per_entry}"
        # if a bit depth has been set and it is smaller than what is required throw an error
        if required_bits_per_entry > bits_per_entry:
            raise Exception(
                f"The array requires at least {required_bits_per_entry} bits per value which is more than the specified {bits_per_entry} bits"
            )
    else:
        raise ValueError(
            "bits_per_entry must be an int between 1 and 64 inclusive or None."
        )
    # make the negative values positive to make bit storage easier
    uarray = data.astype(">Q")
    if bits_per_entry < 64:
        mask = data < 0
        uarray[mask] = np.add(
            data[mask], 2**bits_per_entry, dtype=np.uint64, casting="unsafe"
        )
    data = uarray

    # unpack the individual values into a bit array
    bits: np.ndarray = np.unpackbits(
        np.ascontiguousarray(data[::-1]).view("uint8")
    ).reshape(-1, 64)[:, -bits_per_entry:]
    if dense:
        if bits.size % 64:
            # if the bit array does not fill a whole long
            # add padding to the last long if required
            bits = np.pad(
                bits.ravel(),
                [(64 - (bits.size % 64), 0)],
                "constant",
            )
    else:
        # if the array is not dense add padding
        entry_per_long = 64 // bits_per_entry
        if bits.shape[0] % entry_per_long:
            # add padding to the last long if required
            bits = np.pad(
                bits,
                [(entry_per_long - (bits.shape[0] % entry_per_long), 0), (0, 0)],
                "constant",
            )
        # add padding for each long
        bits = np.pad(
            bits.reshape(-1, bits_per_entry * entry_per_long),
            [(0, 0), (64 - bits_per_entry * entry_per_long, 0)],
            "constant",
        )

    # pack the bits into a long array
    return np.packbits(bits).view(dtype=">q")[::-1]

def bits_per_index(data, palette, pack_bits):
  """the size required to represent the largest index (minimum of 4 bits)"""
  bit_length = max(BS_MIN_BITS, (len(palette) - 1).bit_length())

  return bit_length

# noinspection PyPep8Naming
def get_section_blocks(section):
    np.set_printoptions(threshold=np.inf)
    """Return a (Palette, BlockState Indexes Array) tuple for a chunk section.

    Palette: NBT List of Block States, straight from NBT data
    Indexes: 16 x 16 x 16 numpy.ndarray, in YZX order, of indexes matching Palette's
    """
    if 'block_states' not in section:
      return None, None

    block_states = section['block_states']
    if 'palette' not in block_states or 'data' not in block_states:
      return None, None

    palette = block_states['palette']

    indexes = decode_long_array(np.array(block_states['data']), 16 * 16 * 16, palette)
    indexes = indexes.reshape((SECTION_HEIGHT, *reversed(CHUNK_SIZE)))

    return palette, indexes
