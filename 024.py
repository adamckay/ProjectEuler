import subprocess

source = """
import Data.List 

fac 0 = 1
fac n = n * fac (n - 1)

perms [] _ = []
perms xs n = x : perms (delete x xs) (mod n m)
   where m = fac $ length xs - 1
         y = div n m
         x = xs !! y

main = print $ perms "0123456789" 999999
"""


commands = [
    'yes | curl -sSL https://get.haskellstack.org/ | sh',
    'stack ghc ./Main.hs',
    './Main'
]

file = open('Main.hs', 'w')
file.write(source)
file.close()

[subprocess.Popen(c, shell=True).communicate() for c in commands]
