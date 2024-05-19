import sqlite3

connection = sqlite3.connect('itemsF.db')

#create a cursor
cursor = connection.cursor()

#create a Table
cursor.execute("CREATE TABLE IF NOT EXISTS items (name text, attributes text, passive text)")


#datatypes 1)NULL (DOESNT EXIST) 2) INTEGER (WHOLE NUM)\
# 3) REAL (DECIMAL) 4) TEXT (TEXT) 5) BLOB (STORE EXACTLY LIKE HOW IT IS LIKE IMG AND MP3)
items_list = [
    ("Blade Of Despair", "+160physical attack, +5 movement speed", "Unique Passive: Dealing damage to non-Minion enemies below 50% HP increases physical attack by 25% which last 2 seconds(take effect before the damage is dealt)"),
    ("Melefic Roar", "+60physical attack", "Unique Attribute: +20& Physical Penetration. Unique Passive: When attacking an enemy, gains 0.125% more physical penetrationcapped at 40%"),
    ("Great Dragon Spear", "+70 Physical Attack,+10% Cooldown Reduction+20% Crit Chance","Unique Passive - Supreme Warrior: After casting an Ultimate, increase Movement Speed by 30% which last 7.5 seconds This effect has a 15 seconds cooldown"),
    ("Sea Halbert", "+80 Physical Attack+20% Attack Speed", "Unique Passive - Lifebane: Dealing damage to a target will reduce the Shield and HP Regen effects on them to 50%, of normal for 3 seconds.Unique Passive - Punish: Increase damage by 8%, against enemy heroes with higher extra HP."),
    ("Rose Gold Meteor", "+60 Physical Attack+23 Magic Defense+10 percent Lifesteal", "Unique Passive - Lifeline: When HP is about to drop below 30%, gains a 840~1820 shield (scales with level) and Increase Movement Speed by 50% when triggered, the effect decays over 3 seconds. Cooldown: 60 seconds."),
    ("Bloodlust Axe", "+70 Physical Attack+10% Cooldown Reduction", "Unique Attribute: +20% Spell Vamp"),
    ("Hunter Strike", "+80 Physical Attack+10% Cooldown Reduction", "Unique Attribute: +15 Physical Penetration Unique Passive - Retribution: Deals damage to an enemy hero or Creep for 5 times in a row and improves Movement Speed by 50% that decays rapidly over 3 seconds. This effect has 8 seconds cooldown."),
    ("Blade of Heptaseas", "+70 Physical Attack+250 HP", "Unique Attribute: +15 Physical PEN Unique Passive - Ambush: If no damage is dealt or taken from enemy heroes within 5 seconds, the next Basic Attack deals 160 (40% Total Physical Attack) as extra Physical Damage and slows the target by [40% which last for 1.5 seconds]."),
    ("Windtalker", "+35% Attack Speed +20 Movement Speed+10% Crit Chance", "Unique Passive - Typhoon: Every 5 to 2 seconds (reduced by 0.2 seconds for each Basic Attack), the next Basic Attack will hit up to 3 enemy units for 150 to 362 Magic Damage. (This attack can critically strike and the damage increases to 200% to Minions.) Unique Passive - Activate: Each time Typhoon is cast, one's movement speed will be increased [by] 5% which lasts a short time."),
    ("Endless battle", "+60 Physical Attack +250 HP +10% Cooldown Reduction +8% Hybrid Lifesteal +5% Movement Speed +5 Mana Regen", "Unique Passive - Divine Justice: After casting a skill, the next Basic Attack within 3 seconds deals 60% Physical Attack as extra True Damage (1.5 seconds cooldown). Unique Passive - Chase Fate: Triggering Divine Justice grants 10% more Movement Speed."),
    ("Berserker's Fury", "+65 Physical Attack +25% Crit Chance", "Unique Attribute: +40% Crit Damage Unique Passive - Doom: Critical strikes grant 5% more Physical Attack for 2 seconds."),
    ("Hass's Claws", "+30 Physical Attack +15% Attack Speed +20% Crit Chance", "Unique Attribute: +25 percent Lifesteal Unique Passive - Frenzy: Critical strikes grant 20% more Attack Speed for 2 seconds."),
    ("War Axe", "+25 Physical Attack +550 HP +10% Cooldown Reduction", "Unique Passive - Fighting Spirit: Dealing damage grants 12 extra Physical Attack and 2% more Spell Vamp per second for 4 seconds, up to 6 stacks. Deal 10% more True Damage according to Base Damage at full stacks. (This effect is reduced to 50% when used by Marksmen, Mages, and Supports)"),
    ("Wind of Nature", "+30 Physical Attack +20% Attack Speed +10 percent Lifesteal", "Unique Active - Wind Chant: Immune to all Physical Damage. Last 2 seconds. (Duration becomes half when used by non-marksmen). Cooldown 70 seconds."),
    ("Golden Staff", "+55 Physical Attack +15% Attack Speed", "Unique Passive - Swift: Unable to increase critical chance. Every 1 percent of critical chance gained will increase attack speed by 1%. Unique Passive - Endless Strike: After every 2 non-critical Basic Attacks. Attack Speed of the next Basic Attack is increased by 80 percent and its effects is triggered an extra 2 time(s)."),
    ("Corrosion Scythe", "+30 Physical Attack +30% Attack Speed +5% Movement Speed", "Unique Passive - Corrosive: Each time a Basic Attack deals damage to enemies, gains additional 80 Physical Damage and reduces the target's Movement Speed by 8% (halved for ranged Basic Attacks) for 1.5 seconds. Stacking up to 5 times. Unique Passive - Impulse: When each Basic Attack deals damage to enemies, increase Attack Speed by 6%. Stacks up to 5 times. Lasts 3 seconds."),
    ("Demon Hunter Sword", "+35 Physical Attack +20% Attack Speed", "Unique Passive - Devour: Basic attacks will deal 8 percent of the target's current HP as additional physical damage (up to 60 against creeps and minions). Unique Passive - Devour: Each Basic Attack grants 3 percent Lifesteal for 3 seconds. Stack up to 5 times."),
    ("Flask of The Oasis", "+60 Magic Power +300 HP +10% Cooldown Reduction", "Unique Attribute: +12% Healing Effect Unique Passive - Blessing: When casting a healing or shielding skill, if the target's HP is below 35 percent or falls below 35% within 5 seconds, they will get a 100-1500 shield that lasts 3 seconds. When this effect triggers, it also reduces the cooldown of the caster's skills by 2 seconds. (This effect can only trigger once every 60 seconds on the same target, and will not trigger on self-onl healing and shielding skills.)"),
    ("Genius Wand", "+75 Magic Power +5% Movement Speed", "Unique Attribute: +10 Magic Penetration Unique Passive - Magic: Dealing damage to enemy heroes will reduce their Magic Defense by 2~9 for 2 seconds (the Defense reduction scales with level). Stacks up to 3 times." ),
    ("Lightning Truncheon", "+75 Magic Power +400 Mana +10% Cooldown Reduction", "Unique Passive - Resonate: Every 6 seconds, the next skill that deals damage will resonate, dealing Magic Damage equal to 120% Magic Power against up to 3 enemies and increasing Movement Speed by 30% that decays over 2 seconds."),
    ("Fleeting Time", "+70 Magic Power +300 HP +15% Cooldown Reduction", "Unique Passive - Timestream: Hero kills or assists reduce Ultimate's current cooldown by 30%."),
    ("Blood Wings", "+90 Magic Power", "Unique Passive - Guard: Gains a (800 +100% Magic Power) Shield that will regenerate 20 seconds after being damaged. The Shield also grants 30 Movement Speed while it lasts and 150 Movement Speed for 1 second after it breaks."),
    ("Clock of Destiny", "+60 Magic Power +500 HP +600 Mana", "Unique Passive - Time: Gains 20 extra Max HP and 4 extra Magic Power every 20 seconds, capped at 15 stacks. Unique Passive - Reincarnate: Gains 5% more Magic Power and 600 extra Max Mana at max Time stacks."),
    ("Starlium Scythe", "+70 Magic Power +10% Cooldown Reduction +8% Hybrid Lifesteal +6 Mana Regen", "Unique Passive - Crisis: After casting a skill, the next Basic Attack within 3 seconds deals 100% Magic Power as extra True Damage and grants 10% more Movement Speed. (1.5 seconds cooldown)."),
    ("Glowing Wand", "+75 Magic Power +400 HP +5% Movement Speed", "Unique Passive - Scorch: Burn targets for 3 seconds, dealing Magic Damage equal to 1.5% target's Max HP per second."),
    ("Ice Queem Wand", "+75 Magic Power +10% Spell Vamp +300 HP +7% Movement Speed", "Unique Passive - Ice Bound: When a skill deals damage to an enemy hero, it will also slow them by 10% which lasts for 2 seconds (stacks up to 3 times). This effect has a 1 second cooldown"),
    ("Concentrated Energy", "+70 Magic Power +400 HP", "Unique Attribute: +20% Hybrid Lifesteal Unique Passive - Recharge: Increases Magic Power by 5 after dealing Magic Damage (this effect stacks up to 6 times and can only gain 1 stack every 0.4 second). When reaching full stacks, increases Magic Damage by 12% which lasts for 3 seconds."),
    ("Holy Crystal", "+185 Magic Power", "Unique Passive - Mystery: Increases Magic Power by 21%~35% (Scales with level)."),
    ("Divine Glaive", "+65 Magic Power", "Unique Attribute: +40% Magic Penetration Unique Passive - Spellbreaker: Each point of the enemy's Magic Defense increases Magic Penetration by 0.1% when dealing damage to it, capped at 20%."),
    ("Necklace of Durance", "+60 Magic Power +300 HP +380 Mana +5% Cooldown Reduction", "Unique Passive - Gift: Regens 20% HP and Mana within 2 seconds of leveling up. Unique Passive - Lifebane: Upon dealing damage to the target, reduces Shield and HP Regen of the target by 50% which lasts for 3 seconds."),
    ("Feather of Heaven", "+55 Magic Power +20% Attack Speed +10 percent Lifesteal +5% Cooldown Reduction", "Unique Passive - Affliction: Basic Attacks deal extra Magic Damage equal to 50 plus 30% Magic Power. Unique Passive - Impulse: When each Basic Attack deals damage to enemies, increase Attack Speed by 6%. Stacks up to 5 times. Lasts 3 seconds."),
    ("Winter Truncheon", "+60 Magic Power +20 Physical Defense +400 HP", "Unique Active - Frozen: Freeze upon using. The hero can't do anything but will be immune to all DMG and debuff. Last 2 seconds, Cooldown 100 seconds."),
    ("Enchanted Tailsman", "+50 Magic Power + 250 HP +20% Cooldown Reduction", "Unique Passive - Mana Spring: Regenerates 15% Max Mana every 10 seconds in total. Unique Passive - Magic Mastery: Max CD Reduction increased by 5%."),
    ("Radiant Armor", "+950 HP +40 Magic Defense +12 HP Regen", "Unique Passive - Holy Blessing: Taking Magic Damage grants 6-20 Magic Defense (scales with level) for 5 seconds, capped at 6 stacks (1 stack only every 0.6 second)."),
    ("Twilight Armor", "+1200 HP +15 Physical Defense", "Unique Passive - Twilight: When taking more than 800 damage in a single hit, the excess amount will be reduced by 300 + 15% Max HP. Cooldown: 5 seconds."),
    ("Brute Force Breastplate", "+600 HP +23 Physical Defense +10% Cooldown Reduction", "Unique Passive - Brute Force: Each second after dealing damage, gain 6 extra Physical Attack and Magic Power and 2 percent extra Movement Speed for 4 seconds, up to 6 stacks. Gain 15 percent extra Control Duration Reduction at full stacks."),
    ("Immortality", "+800 HP +15 Physical Defense", "Unique Passive - Immortal: Resurrect 2.5 seconds upon death and gets 16% Max HP and 220-1200 shield that lasts for 3 seconds. (Scales with level) This effect has a cooldown of 210 seconds."),
    ("Dominance Ice", "+500 Mana +55 Physical Defense +5% Movement Speed", "Unique Passive - Artic Cold: Taking damage will reduce the Attack Speed of the atacker to 80 percent of normal for 1 second. Unique Passive - Lifebane: Taking damage will reduce the Shield and HP Regen effects of the attacker to 50 percent of normal for 1 second."),







]  
cursor.executemany("insert into items values (?, ?, ?)", items_list)


#print database rows to see
for row in cursor.execute("select * from items"):
    print(row)




#commit the command
connection.commit()

#close the cnnection
connection.close
