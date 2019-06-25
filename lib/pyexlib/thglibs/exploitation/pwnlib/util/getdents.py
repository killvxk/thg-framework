from ..context import context
from .packing import unpack


class linux_dirent:
    def __init__(self, buf):
        n = context.bytes

        # long
        self.d_ino = unpack(buf[:n])
        buf = buf[n:]

        # long
        self.d_off = unpack(buf[:n])
        buf = buf[n:]

        # short
        self.d_reclen = unpack(buf[:2], 16)
        buf = buf[2:]

        # name
        self.d_name = buf[:buf.index(b'\x00')]

    def __len__(self):
        return self.d_reclen # 2 * context.bytes + 2 + len(self.d_name) + 1

    def __str__(self):
        return "inode=%i %r" % (self.d_ino, self.d_name)


def dirents(buf):
    """unpack_dents(buf) -> list

    Extracts data from a buffer emitted by getdents()

    Arguments:
        buf(bytes): Byte array

    Returns:
        A list of filenames.

    Example:

        >>> data = unhex('5ade6d010100000010002e0000000004010000000200000010002e2e006e3d04092b6d010300000010007461736b00045bde6d010400000010006664003b3504')
        >>> print(dirents(data))
        [b'.', b'..', b'fd', b'task']
    """
    d = []

    while buf:
        try:
            ent = linux_dirent(buf)
        except ValueError:
            break

        d.append(ent.d_name)
        buf = buf[len(ent):]

    return sorted(d)
