def parse_questions(text):
    new_text = text.replace(':"hard","question":', "")
    new_text2 = new_text.replace(',"correct_answer":', ":[")
    new_txt3 = new_text2.replace('"incorrect_answers":[', "")
    return new_txt3


data = {
    "QUESTIONS": [
        {
            "Talos, the mythical giant bronze man, was the protector of which island?": [
                "Crete",
                "Sardinia",
                "Sicily",
                "Cyprus",
            ]
        },
        {
            "What was the punishment for Sysiphus's craftiness?": [
                "Cursed to roll a boulder up a hill for eternity.",
                "Tied to a boulder for eternity, being pecked by birds.",
                "Standing in a lake filled with water he could not drink.",
                "To fell a tree that regenerated after every axe swing.",
            ]
        },
        {
            "According to fairy folklore, what metal are fairies afraid of?": [
                "Iron.",
                "Silver.",
                "Gold.",
                "Copper.",
            ]
        },
        {
            "Who was the only god from Greece who did not get a name change in Rome?": [
                "Apollo",
                "Demeter",
                "Zeus",
                "Athena",
            ]
        },
        {
            "The ancient roman god of war was commonly known as...": [
                "Mars",
                "Jupiter",
                "Juno",
                "Ares",
            ]
        },
        {
            "This Greek mythological figure is the god of battle strategy (among other things).": [
                "Athena",
                "Ares",
                "Artemis",
                "Apollo",
            ]
        },
        {
            "The Hippogriff, not to be confused with the Griffon, is a magical creature with the front half of an eagle, and the back half of what?": [
                "A Horse",
                "A Dragon",
                "A Tiger",
                "A Lion",
            ]
        },
        {
            "Who in Greek mythology, who led the Argonauts in search of the Golden Fleece?": [
                "Jason",
                "Castor",
                "Daedalus",
                "Odysseus",
            ]
        },
        {"Neptune's greek name was...": ["Poseidon", "Ares", "Zeus", "Apollo"]},
        {"Hera is god of...": ["Marriage", "Agriculture", "Sea", "War"]},
        {
            "Which of the following Mesopotamian mythological figures was NOT a deity?": [
                "Enkidu",
                "Enki",
                "Enlil",
                "Enkimdu",
            ]
        },
        {
            "This Greek goddess's name was chosen for the dwarf planet responsible for discord on Pluto's classification amongst astronomers.": [
                "Eris",
                "Charon",
                "Ceres",
                "Dysnomia",
            ]
        },
        {
            "Who was the King of Gods in Ancient Greek mythology?": [
                "Zeus",
                "Apollo",
                "Hermes",
                "Poseidon",
            ]
        },
        {
            "In Greek Mythology, who was the daughter of King Minos?": [
                "Ariadne",
                "Athena",
                "Ariel",
                "Alana",
            ]
        },
        {
            "In Norse mythology, what is the name of the serpent which eats the roots of the ash tree Yggdrasil?": [
                "Nidhogg",
                "Bragi",
                "Odin",
                "Ymir",
            ]
        },
        {
            "Which of these Roman gods doesn't have a counterpart in Greek mythology?": [
                "Janus",
                "Vulcan",
                "Juno",
                "Mars",
            ]
        },
        {
            "Which Greek &amp; Roman god was known as the god of music, truth and prophecy, healing, the sun and light, plague, poetry, and more?": [
                "Apollo",
                "Aphrodite",
                "Artemis",
                "Athena",
            ]
        },
        {
            "The greek god Poseidon was the god of what?": [
                "The Sea",
                "War",
                "Sun",
                "Fire",
            ]
        },
        {
            "Which figure from Greek mythology traveled to the underworld to return his wife Eurydice to the land of the living?": [
                "Orpheus",
                "Hercules",
                "Perseus",
                "Daedalus",
            ]
        },
        {
            "Which of the following is NOT a god in Norse Mythology.": [
                "Jens",
                "Loki",
                "Tyr",
                "Snotra",
            ]
        },
        {
            "Nidhogg is a mythical creature from what mythology?": [
                "Norse",
                "Egyptian",
                "Greek",
                "Hindu",
            ]
        },
        {
            "In Greek mythology, who is the god of wine?": [
                "Dionysus",
                "Hephaestus",
                "Demeter",
                "Apollo",
            ]
        },
        {
            "Who is the Egyptian god of reproduction and lettuce?": [
                "Min",
                "Menu",
                "Mut",
                "Meret",
            ]
        },
        {"A minotaur is half human half what?": ["Bull", "Cow", "Horse", "Eagle"]},
        {
            "In most traditions, who was the wife of Zeus?": [
                "Hera",
                "Aphrodite",
                "Athena",
                "Hestia",
            ]
        },
        {
            "What is the name of the Greek god of blacksmiths?": [
                "Hephaestus",
                "Dyntos",
                "Vulcan",
                "Artagatus",
            ]
        },
        {
            "According to the Egyptian Myth of Osiris, who murdered Osiris?": [
                "Set",
                "Horus",
                "Ra",
                "Anhur",
            ]
        },
        {
            "Which of these mythological creatures is said to be half-man and half-horse?": [
                "Centaur",
                "Minotaur",
                "Pegasus",
                "Gorgon",
            ]
        },
        {
            "Which of the following is not one of the Greek Fates?": [
                "Narcissus",
                "Clotho",
                "Atropos",
                "Lachesis",
            ]
        },
        {
            "What mythology did the god &quot;Apollo&quot; come from?": [
                "Greek and Roman",
                "Roman and Spanish",
                "Greek and Chinese",
                "Greek, Roman and Norse",
            ]
        },
    ]
}
