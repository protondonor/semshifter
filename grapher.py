from semshifter import semshift
from helper import clean_shift

def find_all_shifts(word, rounds=2, shift_map={}):
  if rounds < 1 or word in shift_map:
    return {}
  nexts = clean_shift(semshift(word))
  shift_map[word] = nexts
  for next_word in nexts:
    if len(next_word.split()) == 1:
      next_map = find_all_shifts(next_word, rounds-1, shift_map)
      shift_map.update((k,v) for k,v in next_map.items() if k not in shift_map and len(v) > 0)
  return shift_map

def graphviz_descendants(word, rounds=2):
  shifts = find_all_shifts(word, rounds, {})
  shift_string = "\n  ".join('"{}" -> "{}";'.format(x,y) for x,ys in shifts.items() for y in ys if len(y.split()) == 1)
  return """
digraph g{{
  rankdir=LR;
  "{}" [shape=doublecircle];
  {}
}}
""".format(word, shift_string)
