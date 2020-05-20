import os
from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.rank = 1000
        self.name = 'dict'
        self.mark = '[D]'

    def gather_candidates(self, context):
        candidates = []
        
        if self.vim.eval('g:minidict_dir'):
            minidict_dir = self.vim.eval('g:minidict_dir')
        else:
            return candidates
        
        dicts = [f for f in os.listdir(minidict_dir) if os.path.isfile(os.path.join(minidict_dir, f))]
        
        for dict in dicts:
            dict = open(minidict_dir + '/' + dict, 'r').read().split('\n')
            candidates = candidates + dict[0:-1]

        candidates = list(set(candidates))
        return [{'word': c} for c in candidates]
