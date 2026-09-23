import random 

words = [
	"aback", "abase", "abate", "abbey", "abbot", "abide", "abled", "abode",
	"abort", "about", "above", "abuse", "abyss", "acorn", "acrid", "actor",
	"acute", "adapt", "adept", "admit", "adopt", "adore", "adorn", "adult",
	"after", "again", "agent", " agile", "aging", "aglow", "agony", "agree",
	"ahead", "aisle", "alarm", "album", "alert", "alike", "alive", "allow",
	"alone", "along", "aloud", "alter", "amaze", "amber", "amend", "amiss",
	"among", "ample", "amuse", "angel", "anger", "angle", "angry", "ankle",
	"annex", "antic", "anvil", "apart", "apple", "apply", "apron", "arise",
	"armor", "arose", "array", "arrow", "arson", "aside", "asset", "atlas",
	"attic", "audio", "audit", "avoid", "await", "awake", "award", "aware",
	"badge", "badly", "baker", "balmy", "banjo", "basic", "basin", "basis",
	"batch", "bathe", "beach", "beard", "beast", "began", "begin", "begun",
	"being", "belly", "below", "bench", "berry", "bible", "bingo", "birth",
	"black", "blade", "blame", "bland", "blank", "blast", "blaze", "bleak",
	"blend", "bless", "blind", "blink", "block", "blood", "bloom", "blown",
	"board", "boast", "bonus", "boost", "booth", "bound", "brain", "brake",
	"brand", "brave", "bread", "break", "brick", "bride", "brief", "bring",
	"broad", "broke", "brown", "brush", "build", "bulky", "bunch", "buyer",
	"cabin", "cable", "camel", "candy", "carry", "carve", "catch", "cause",
	"cedar", "chain", "chair", "chalk", "champ", "chant", "chaos", "charm",
	"chase", "cheap", "check", "cheer", "chess", "chest", "chief", "child",
	"chime", "choir", "chord", "claim", "clash", "class", "clean", "clear",
	"clerk", "click", "climb", "clock", "close", "cloud", "coach", "coast",
	"color", "comic", "coral", "couch", "could", "count", "court", "cover",
	"crack", "craft", "crane", "crash", "crate", "crawl", "crazy", "cream",
	"creek", "crime", "crisp", "cross", "crowd", "crown", "crude", "curve",
	"cycle", "daily", "dairy", "dance", "death", "debug", "delay", "depth",
	"diary", "dirty", "doubt", "dough", "draft", "drain", "drama", "drawn",
	"dream", "dress", "drill", "drink", "drive", "drown", "eager", "early",
	"earth", "eight", "elect", "elite", "empty", "enemy", "enjoy", "enter",
	"entry", "equal", "error", "event", "every", "exact", "extra", "faith",
	"false", "fancy", "favor", "feast", "fence", "fetch", "field", "fiery",
	"fifth", " fifty", "fight", "final", "first", "flame", "flask", "flesh",
	"float", "flock", "floor", "flour", "fluid", "focus", "force", "forge",
	"forth", "forty", "forum", "found", "frame", "fresh", "front", "fruit",
	"giant", "given", "glare", "glass", "globe", "glory", "glove", "going",
	"grace", "grade", "grain", "grand", "grant", "grape", "graph", " grasp",
	"grass", "great", "green", "greet", "grief", "grill", "grind", "gross",
	"group", "grove", "grown", "guard", "guess", "guest", "guide", "habit",
	"happy", "harsh", "heart", "heavy", "hello", "hence", "honey", "honor",
	"horse", "hotel", "house", "human", "humor", "ideal", "image", "imply",
	"index", "inner", "input", "irony", "issue", "ivory", "jelly", "jewel",
	"joint", "jolly", "judge", "juice", "juicy", "known", "label", "labor",
	"large", "laser", "later", "laugh", "layer", "learn", "least", "leave",
	"legal", "lemon", "level", "light", "limit", "linen", "local", "lodge",
	"logic", "loose", "lucky", "lunar", "lunch", "magic", "major", "maker",
	"maple", "march", "match", "maybe", "mayor", "medal", "media", "mercy",
	"metal", "meter", "might", "minor", "model", "money", "month", "moral",
	"motor", "mount", "mouse", "mouth", "movie", "music", "naive", "nerve",
	"never", "night", "noble", "noise", "north", "novel", "nurse", "ocean",
	"offer", "often", "olive", "onion", "opera", "orbit", "order", "organ",
	"other", "outer", "owner", "paint", "panel", "paper", "party", "pause",
	"peace", "pearl", "phase", "phone", "photo", "piano", "piece", "pilot",
	"pizza", "place", "plain", "plane", "plant", "plate", "plead", "point",
	"power", "press", "price", "pride", "prime", "print", "prior", "prize",
	"proof", "proud", "queen", "quick", "quiet", "radio", "raise", "rally",
	"ranch", "range", "rapid", "ratio", "reach", "react", "ready", "realm",
	"refer", "relax", "renew", "reply", "right", "rival", "river", "robot",
	"rough", "round", "route", "royal", "rugby", "ruler", "rural", "salad",
	"scale", "scare", "scene", "scope", "score", "scout", "scrap", "sense",
	"serve", "seven", "shade", "shake", "shame", "shape", "share", "sharp",
	"sheep", "sheet", "shelf", "shell", "shift", "shine", "shirt", "shock",
	"shore", "short", "shout", "sight", "since", "skill", "skirt", "sleep",
	"slice", "slide", "slope", "small", "smart", "smile", "smoke", "snake",
	"solar", "solid", "solve", "sound", "south", "space", "spare", "speak",
	"speed", "spell", "spend", "spice", "spite", "split", "spoke", "sport",
	"spray", "stack", "staff", "stage", "stair", "stake", "stand", "stare",
	"start", "state", "steak", "steal", "steam", "steel", "stick", "still",
	"stock", "stone", "stood", "store", "storm", "story", "strip", "stuck",
	"study", "style", "sugar", "suite", "super", "sweet", "table", "taste",
	"teach", "teeth", "thank", "their", "theme", "there", "thick", "thing",
	"think", "third", "those", "three", "throw", "tight", "title", "today",
	"topic", "total", "touch", "tough", "tower", "trace", "track", "trade",
	"train", "treat", "trend", "trial", "tribe", "trick", "tried", "truck",
	"trust", "truth", "uncle", "under", "union", "unite", "until", "upper",
	"upset", "urban", "usage", "usual", "valid", "value", "video", "vital",
	"voice", "waste", "watch", "water", "weary", "weigh", "whale", "wheat",
	"wheel", "where", "which", "while", "white", "whole", "whose", "woman",
	"world", "worry", "worse", "worth", "would", "write", "wrong", "young",
	"youth", "zebra"
]

word = random.choice(words)


def play(guess,word):
    if guess == word: 
            print("Congratulations! You guessed the word.")
            return (True)
    else: 
        trys = ""
    for letter in len(guess):
        if guess[letter] in word:
            trys += "🟧"
        elif guess[letter] == word[letter]:
            trys += "🟩"
        else: trys += "✖️"
    print (trys)

count = 5

while count !=1:
    guess = input("enter a 5 letter word")
    if len(guess) != 5:
        print("guess again")
    else: 
        if play(guess,word) == True:
            count = 0
        else: count -=1

