import os
from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'dict'
        self.mark = '[D]'
        self.dict_dir = self.vim.eval('g:dict_dir')

    def gather_candidates(self, context):
        dicts = [f for f in os.listdir(self.dict_dir) if os.path.isfile(os.path.join(self.dict_dir, f))]

        candidates = []
        for dict in dicts:
            dict = open(self.dict_dir + '/' + dict, 'r').read().split('\n')
            candidates = candidates + dict[0:-1]

        candidates = list(set(candidates))
        return [{'word': c} for c in candidates]
