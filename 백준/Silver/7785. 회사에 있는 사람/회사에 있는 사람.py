import sys

log = {}

for _ in range(int(sys.stdin.readline())):
  p, c = sys.stdin.readline().rstrip().split()

  if c == 'enter':
    log[p] = 'enter'
  else:
    if log[p]:
      del log[p]

for people in sorted(log, reverse=True):
  print(people)