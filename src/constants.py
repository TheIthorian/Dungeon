class ENEMY_LISTS:
    SIZE_LIST = ["small", "medium", "large"]
    CATEGORY_LIST = ["animal", "humanoid", "undead"]
    RARITY_LIST = ["common", "rare", "boss"]


class ENEMY_NAMES:
    SMALL_ANIMAL = ["rat", "mosquito", "toad", "salamander", "spider"]
    MEDIUM_ANIMAL = ["hound", "panther", "wolf", "raptor"]
    LARGE_ANIMAL = ["bear", "crocodile", "lion", "bear", "scarab", "lizard"]
    SMALL_HUMANOID = ["goblin", "gnome", "halfling", "dwarf", "fairy"]
    MEDIUM_HUMANOID = ["human", "elf", "orc", "drow"]
    LARGE_HUMANOID = ["troll", "ogre", "golem", "minotaur", "giant", "centaur"]
    SMALL_UNDEAD = ["tomb-snake", "corpse-fly", "ghoul", "spirit"]
    MEDIUM_UNDEAD = ["zombie", "wraith", "skeleton", "wight", "draugr"]
    LARGE_UNDEAD = ["bone-giant", "flesh-golem"]


ITEM_TYPES_LIST = ["attire", "weapon", "consumable"]


class ITEM_NAMES:
    WEAPON_NAMES_LIST = ["sword", "axe", "mace", "hammer", "spear"]
    ATTIRE_NAMES_LIST = ["armour", "cuirass", "garb", "hauberk", "raiment"]
    CONSUMABLE_NAMES_LIST = ["loaf", "broth", "meal", "soup", "porridge"]


SECTOR_LIST = ["caves", "tombs", "sewers", "dungeons"]


class SECTOR_WEIGHTS:
    CAVES = (15, 4, 1)
    TOMBS = (1, 1, 18)
    SEWERS = (9, 3, 8)
    DUNGEONS = (6, 7, 6)


class ADJECTIVES:
    ENEMY_IS_RARE_ADJECTIVES = {
        "animal": ["aggressive", "threatening", "ravenous", "slavering", "rabid"],
        "humanoid": ["insane", "hallucinating", "zealous", "manic"],
        "undead": ["hungering", "restless", "eerie", "lumbering", "shambling"],
    }
    ENEMY_IS_BOSS_ADJECTIVES = {
        "animal": ["monstrous", "gargantuan", "colossal"],
        "humanoid": ["villainous", "murderous", "flagellating", "barbaric"],
        "undead": ["necromantic", "sanguine", "hulking", "towering"],
    }
    ATTIRE_ADJECTIVES = {
        "low_psd_low_dfc": ["rusty", "torn", "broken", "ancient", "orcish"],
        "low_psd_high_dfc": ["heavy", "functional", "plated", "dwarven", "resilient"],
        "high_psd_low_dfc": ["appealing", "shiny", "delicate", "engraved", "embossed"],
        "high_psd_high_dfc": [
            "lordly",
            "masterful",
            "heroic",
            "glorious",
            "magisterial",
        ],
    }
    WEAPON_ADJECTIVES = {
        "low_atk_low_dmg": ["rusty", "battered", "broken", "crumbling", "orcish"],
        "low_atk_high_dmg": ["heavy", "weighty", "large", "dwarven", "powerful"],
        "high_atk_low_dmg": [
            "lightweight",
            "delicate",
            "nimble",
            "agile",
            "well-balanced",
        ],
        "high_atk_high_dmg": ["masterwork", "lordly", "elven", "heroic", "legendary"],
    }
    CONSUMABLE_ADJECTIVES = {
        "low_health": ["mouldy", "smelly", "suspicious", "repellent", "gross"],
        "high_health": ["hearty", "decadent", "healthy", "substantial", "sizeable"],
    }


class WEAPON_INSPECT:
    LOW_ATTACK_LOW_DMG = [
        "\nThe weapon is rusted beyond repair. It may be completely useless.",
        "\nThe weapon is in ruins.",
        "\nYou hold the crumbling weapon aloft, doubtful that it could even hurt a fly.",
        "\nWhat little remains of this weapon is almost certainly worthless to you.",
        "\nThe weapon might make for a decent doorstop.",
    ]
    LOW_ATTACK_MED_DMG = [
        "\nThe weapon is shoddy, but you still wouldn't want to get in the way of it.",
        "\nIt's definitely functional, if a little unwieldy.",
        "\nThe weapon appears newly forged... by a goblin.",
        "\nTurning the weapon over, you notice it is spotted with rust.",
        "\nYou've seen finer weapons. Far finer, in fact.",
    ]
    LOW_ATTACK_HIGH_DMG = [
        "\nWith both hands around the hilt you can barely lift the massive weapon.",
        "\nIt's one of the largest weapons you've ever seen and as unwieldy as it is deadly.",
        "\nThe enormous weapon could do great harm... if you could hit anything with it.",
        "\nWas this weapon made for a man or a giant?",
        "\nWhat metal is this? You can barely lift the thing.",
    ]
    MED_ATTACK_LOW_DMG = [
        "\nOnce, this was a well-crafted weapon. Now, it's rusty.",
        "\nIt's weighty but well-balanced, though time has weakened it.",
        "\nAge has crumbled what was once a masterwork weapon.",
        "\nDisappointingly, the weapon appears too worn to do serious harm.",
        "\nThe weapon is easy to handle but its surface is marred by fractures.",
    ]
    MED_ATTACK_MED_DMG = [
        "\nWeighty, but not too heavy. It'll hurt.",
        "\nThe weapon is in remarkably good condition.",
        "\nPutting the weapon through the motions, you find that you have... no comment",
        "\nWhat a remarkably unremarkable weapon.",
        "\nThe weapon is not too old... but not new either.",
    ]
    MED_ATTACK_HIGH_DMG = [
        "\nThe weapon is large and clearly formidable.",
        "\nYou have to hold the weapon in both hands, but it doesn't feel clumsy.",
        "\nYou are confident that this weapon could deal some serious harm.",
        "\nThe weapon's craftsmanship is certainly remarkable.",
        "\nThe weapon is in perfect condition and you can immediately tell how deadly it is.",
    ]
    HIGH_ATTACK_LOW_DMG = [
        "\nThe weapon is light-weight and delicate, if a little rusty.",
        "\nTime has sapped what little magic was once imbued in this weapon.",
        "\nThe tiny weapon is masterfully crafted. It was likely made for a halfling.",
        "\nThe weapon glides through the air but has a dullness to it.",
        "\nOnce, this weapon might have been legendary. Now, it is ancient.",
    ]
    HIGH_ATTACK_MED_DMG = [
        "\nThe weapon is as light as a feather but could clearly do some serious damage.",
        "\nThe weapon flickers with magical energy, but the enchantment is fading.",
        "\nThe weapon is etched and intricate, and you're sure you could use it to great effect.",
        "\nTurning the weapon over, you're very aware you're holding someone's life's work.",
        "\nYou've rarely seen a finer weapon than this.",
    ]
    HIGH_ATTACK_HIGH_DMG = [
        "\nThe deadly weapon hums in violent anticipation. Clutching it in both hands, it feels"
        " almost as though it is an extension of yourself.",
        "\nHolding the weapon up high, it shimmers in an ominous, deadly sort of way.",
        "\nAs soon as you touch the weapon, you feel a dark sort of power course through you.",
        "\nLifting the weapon above your head, you speak a word in an unknown language, and the"
        " weapon erupts in thunderous blue fire.",
        "\nYou feel a sharp pain in your mind and are overcome with a dark thirst. You realise"
        " the weapon is... speaking to you... commanding you.",
    ]


class ATTIRE_INSPECT:
    LOW_DEFENCE_LOW_PERSUADE = [
        "\nThe attire is both broken and ugly.",
        "\nIt's rusty and it reeks.",
        "\nYour hands come away covered in a strange substance.",
        "\nYou wouldn't be caught dead wearing that.",
        "\nThere are no redeeming qualities here.",
    ]
    LOW_DEFENCE_MED_PERSUADE = [
        "\nThe attire seems fragile, but it's not ugly.",
        "\nIt's oddly charming.",
        "\nA little old, perhaps, and probably not going to turn a blade.",
        "\nThe stitching is fine, but you're not sure this would hold up in combat.",
        "\nThis is, without a doubt, an outfit.",
    ]
    LOW_DEFENCE_HIGH_PERSUADE = [
        "\nThis is far too fine a raiment for a place like this!",
        "\nElegant and finely-crafted, but not suitable for adventuring.",
        "\nA lot of time and patience went in to making this, but it's not for combat.",
        "\nThe outfit is imposing... but it's more bark than bite.",
        "\nIt's an intricate piece but any metalwork is as thin as paper.",
    ]
    MED_DEFENCE_LOW_PERSUADE = [
        "\nIts ugly but it will hold its own in combat.",
        "\nSo long as you have a hand free to pinch your nose, the attire is suited to combat.",
        "\nThough spotted with rust, you have confidence this would protect you.",
        "\nIt looks protective but what are those stains?",
        "\nThe metalwork is functional if not decorative.",
    ]
    MED_DEFENCE_MED_PERSUADE = [
        "\nThis is a soldier's uniform. It's smart, lightweight, and will keep you safe.",
        "\nTurning the equipment over in your hands you're definitely satisfied with it.",
        "\nIt's a fine piece of equipment.",
        "\nWhat a remarkably unremarkable raiment.",
        "\nDespite its time down in these depths, the attire is well-maintained.",
    ]
    MED_DEFENCE_HIGH_PERSUADE = [
        "\nThe metalwork is both thick and delicately embossed.",
        "\nYou get the feeling this armour was designed for someone with a lot of spare coin.",
        "\nThe mail shirt is adorned with intricate symbols and patterns.",
        "\nThe equipment comes with a breastplate with a dragon embossed upon it.",
        "\nA fine, plumed helm is included in the set. Likely made for a military officer.",
    ]
    HIGH_DEFENCE_LOW_PERSUADE = [
        "\nThe unappealing suit of armour embodies the concept of 'function over form'.",
        "\nYou get the impression this thick armour was made for something larger than human.",
        "\nThe centrepiece of this titanic suit of armour is a monstrous, terrifying mask.",
        "\nThe stench of death lingers around the armour.",
        "\nThe raiment is thick and protective, but amateurishly assembled.",
    ]
    HIGH_DEFENCE_MED_PERSUADE = [
        "\nTrying the equipment on, you're surprised at how well it fits you.",
        "\nThe imposing metalwork could turn aside most any blade.",
        "\nSomeone has taken very good care of this armour... and recently.",
        "\nUnlike iron or steel, the metal of this raiment is black as night.",
        "\nThe breastplate must be an inch thick and yet, somehow, it's very lightweight.",
    ]
    HIGH_DEFENCE_HIGH_PERSUADE = [
        "\nThe armour glimmers with latent energy. There is something foreboding about it.",
        "\nYou feel like you recognise it from the myths and legends you heard as a child.",
        "\nThe armour is immaculate. When you press your finger against it, you sense a"
        "mystical force pushing back at you.",
        "\nAs you step towards the armour you stumble, kicking a pebble towards it. With a"
        " mighty crack, the armour shoots out a bolt of energy, launching the pebble away.",
        "\nThe armour is formed of a continuous, seamless plane of metal. Yet, when you"
        " try it on, it moves with your limbs like a second skin.",
    ]


class CONSUMABLE_INSPECT:
    LOW_HEALTH = ["\nYou'd have to be desperate to consume this."]
    MED_HEALTH = ["\nIt looks good enough."]
    HIGH_HEALTH = ["\nIt looks wholesome and hearty."]


class THREAT_RESPONSE:
    NO_THREAT = (
        "\nThe being appears to be wounded, and wouldn't be able to take much more."
    )
    LITTLE_THREAT = "\nThe being isn't particularly threatening."
    SOME_THREAT = "\nThe being moves with determined intent towards you."
    THREATENING = "\nThe being appears powerful and aggressive."
    SERIOUS_THREAT = (
        "\nSweat beads on your brow. You doubt you'll be leaving here alive."
    )


class COMBAT_TEXT:
    END_COMBAT = "\nWith the encounter over, you head off deeper in to the darkness."
    RUN_SUCCESS = "\nYou flee."
    RUN_FAIL = "\nYou try to run away, but your foe prevents you."


class POSITIVE_EVENTS:
    GAIN_ITEM = "\nNestled within a dark corner, you notice something!"
    GAIN_HEALTH = (
        "\nYou find a pool of crystal clear water! Taking a sip, you feel revitalised!"
    )
    GAIN_DMG = "\nYou find an odd tincture nestled in a crack in a wall. You drink it, and feel stronger!"
    GAIN_MAX_HEALTH = "\nA strange voice echoes in the darkness. You feel protected."
    GAIN_PSD = "\nThe water flows surprisingly clean here. You make sure you to clean yourself up whilst you can."
    NO_EFFECT = (
        "\nThere is a sense of hope in the air, but you'd be a fool to trust it."
    )


class NEGATIVE_EVENTS:
    LOSE_HEALTH = "\nYou stumble over a mound of broken rocks and fall over."
    LOSE_MAX_HEALTH = "\nA strange voice echoes in the darkness. You feel shaken."
    LOSE_DMG = "\nThe darkness weighs heavily on you. You feel weaker."
    NO_EFFECT = "\nThere is an ominous feeling in the air, but you push through."


class ROOM_SPECIAL_EVENTS:
    AMBUSH = "\nAs soon as you step in to the room, the door slams shut, and something steps out of the darkness!"
    HERO = "\nA solemn figure sits by a fire in the middle of the room. They regale you with stories of past heroism."
    GOBLIN = "\nA short, fat goblin sleeps in the corner of the room. They're curled up in a tight ball."
    SKELETON = "\nSkeletal remains sit in an open coffin in the centre of the room. Something has been placed within."


class EXPLORE_SPECIAL_EVENTS:
    DARKNESS = "\nAs you stumble around the area, your torch goes out."
    BUMP = "\nSomething small bumps into you, giggling, and your pack suddenly feels lighter."
    CLOISTER = "\nAn empty cloister sits against a far wall, candles still burning. Otherwise, there is only silence."
    STEW = "\nA rotund orc stirs a cauldron of bubbling soup. Strange meat floats around the liquid."


class REST_SPECIAL_EVENTS:
    VISITOR = "\nAs you settle down to rest, a hunched figure with a crooked nose joins you. She offers you an apple."
    BAD_SLEEP = "\nYou toss and turn throughout the night, and feel hardly any better the morning after."
    GOOD_SLEEP = (
        "\nYou sleep more deeply than usual, and feel revitalised the morning after."
    )
    BARD = "\nA wandering bard, covered in grime, bursts through the door. He's clutching a lute like a weapon."
    PIXIE = "\nAn annoying, buzzing light flitters around your campsite."
    DOG = "\nA stray dog wanders into your campsite, and looks pleadingly up at you."


class SECTOR_INTRODUCTION_TEXT:
    CAVES = (
        "\nThe air is humid and stale, and you can hear the sound of rushing water in the distance. A limp, thin"
        "\nmoss covers most of the surface around you, and in this silence you could hear a pin drop. And yet... you"
        "\ndon't quite feel alone."
    )
    TOMBS = (
        "\nThe first thing you notice is the rotten stench. The smell of decay assaults your senses and it takes"
        "\nall your might not to retch. The air is unnaturally cold, and you feel as though you are being watched. Through"
        "\nthe walls you can hear the sounds of shuffling, lumbering... and scraping... like broken fingernails scratching"
        "\nagainst cold stone."
    )
    DUNGEONS = (
        "\nThis place feels... awake... alive, even... and malicious. Something terrible has happened here. Maybe"
        "\nlong ago... or maybe not. By the sounds of rattling chains, the baying of hounds, and sinister laughter,"
        "\nyou suspect it's more likely the latter."
    )
    SEWERS = (
        "\nThe odour to this place is as you would expect from a sewer... but something's wrong. There's something"
        "\nbeneath that smell. Older, darker, more rotten... and beyond the skittering of vermin through the halls"
        "\nyou could swear you hear other sounds as well. Blades being sharpened. Battle being done. The"
        "\nhorrifying shambling of the living dead."
    )
