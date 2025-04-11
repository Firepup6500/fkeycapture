# pylint: skip-file
from os import environ, system
from build import build

system("clear")
system("rm -rf testOnly && cp -r package/src/fkeycapture testOnly")
print("Should be nothing from here")
import testOnly as fkey

print("Until here")

bob = input("(If owner) Build (Y|*)? ").upper()
system("clear")

if environ["REPL_OWNER"] == "Firepup650" and bob == "Y":
    build()
    exit()
tests = {
    "1": {"Name": "Get", "Func": fkey.get, "Ext": [1, True, False, True]},
    "2": {"Name": "Getnum", "Func": fkey.getnum, "Ext": [1, False, False]},
}
print("Test get or getnum? ")
inp = fkey.getchars(chars=["1", "2"])  # type: ignore[arg-type]
print(f"Testing {tests[inp]['Name']}")
while 1:
    print(tests[inp]["Func"](*tests[inp]["Ext"]))
