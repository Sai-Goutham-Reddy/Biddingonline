class clear:
 def __call__(self):
  import os
  if os.name==('ce','nt','dos'): os.system('cls')
  elif os.name=='posix': os.system('clear')
  else: print('\n'*120)
 def __neg__(self): self()
 def __repr__(self):
  self();return ''

clear=clear()