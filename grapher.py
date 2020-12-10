import sys
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
      shift_map.update((k,v) for k,v in next_map.items() if k not in shift_map)
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

if __name__ == "__main__":
  args = sys.argv[1:]
  if args:
      word = args[0]
      rounds = int(args[1]) if len(args) > 1 else 2
      print(graphviz_descendants(word, rounds))
  else:
      word = ''
      while(word != "quit()"):
          word = input("type in a word to do 2 rounds with, or else 'quit()' to quit: ")
          if word != "quit()":
              print(graphviz_descendants(word))
