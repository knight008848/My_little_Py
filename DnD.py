import random, copy

NUM_FIGHTS = 1
VERBOSE = True

# Lower thac0 and lower ac values are better. Higher damage & hp values are better.
aliceTemplate = {'name': 'Alice', 'hp': 14, 'ac': 5, 'thac0': 18, 'dmgnum': 1, 'dmgsize':6, 'dmgmod': 0}
bobTemplate   = {'name': 'Bob',   'hp': 12, 'ac': 7, 'thac0': 16, 'dmgnum': 2, 'dmgsize':4, 'dmgmod': 0}

def display(s):
    if VERBOSE:
        print(s)

def attack(attacker, defender):
    if random.randint(1, 20) >= attacker['thac0'] - defender['ac']:
        damage = 0
        for i in range(attacker['dmgnum']):
            damage += random.randint(1, attacker['dmgsize'])
        damage += attacker['dmgmod']
        display('%s (%s hp) hits %s (%s hp) for %s points of damage. %s is reduced to %s hp.' % (attacker['name'], attacker['hp'], defender['name'], defender['hp'], damage, defender['name'], defender['hp'] - damage))
        defender['hp'] -= damage
    else:
        display('%s misses %s.' % (attacker['name'], defender['name']))

aliceWins = 0
bobWins = 0
for i in range(NUM_FIGHTS):
    display('======================')
    display('Start of combat #%s' % (i+1))
    alice = copy.deepcopy(aliceTemplate)
    bob = copy.deepcopy(bobTemplate)
    while True:
        attack(alice, bob)
        if bob['hp'] <= 0:
            break

        attack(bob, alice)
        if alice['hp'] <= 0:
            break
    if alice['hp'] <= 0:
        display('Alice has died.')
        bobWins += 1
    if bob['hp'] <= 0:
        display('Bob has died.')
        aliceWins += 1

print()
print('Alice won %s (%s%%) fights. Bob won %s (%s%%) fights.' % (aliceWins, round(aliceWins / NUM_FIGHTS * 100, 2), bobWins, round(bobWins / NUM_FIGHTS * 100, 2)))