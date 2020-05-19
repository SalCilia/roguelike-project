class Tile:

    def_init_(self, blocked, block_sight=None):
        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked
        
        self.block_sight = block_sight