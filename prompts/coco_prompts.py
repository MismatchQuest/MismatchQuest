OBJECT_CONGEN_FEW_SHOT_PROMPT = """
Guidelines:
- Object/Noun Misalignment: Change a key object or noun in the caption to create a contradiction, you can also add or remove an object, or alter the quantity of an item. The contradictory caption should then focus on a different object/noun, and this discrepancy must be clearly highlighted in the misalignment description.

Examples: 

CAPTION: A cartoon painting of three cats and a mouse on a yellow wall .
CONTRADICTION: A cartoon painting of five cats and a mouse on a yellow wall .
MISALIGNMENT: Three cats (CAPTION: three cats), not five are in the cartoon painting.
MISALIGNMENT TYPE: Object/Noun

CAPTION: A stained glass window with a cartoon image of a man with glasses and a beard .
CONTRADICTION: A stained glass window with a cartoon image of a man with a beard .
MISALIGNMENT: The man in stained glass wear glasses (CAPTION: man with glasses and a beard), instead of only beard (CONTRADICTION: man with a beard).
MISALIGNMENT TYPE: Object/Noun

CAPTION: A black and green cat figurine on a gray surface.
CONTRADICTION: A black and green cat with a funny unicorn figurine on a gray surface.
MISALIGNMENT: The funny unicorn (CONTRADICTION: funny unicorn) is missing (CAPTION: None:) .
MISALIGNMENT TYPE: Object/Noun

CAPTION: A sign welcomes visitors to Lake Kawaguchiko in English and in another language.
CONTRADICTION: A mascot welcomes visitors to Lake Kawaguchiko in Japanese and in another language.
MISALIGNMENT: There is a sign welcoming visitors to Lake Kawaguchiko (CAPTION: sign), not a mascot (CONTRADICTION: mascot)
MISALIGNMENT TYPE: Object/Noun

CAPTION: Two dogs on a leash playing on the shore and in the water of a lake.
CONTRADICTION: Two dogs on a leash playing on the shore and in the water of a volcano.
MISALIGNMENT: The dogs are playing on the shore and in the water of a lake (CAPTION: Two dogs on a leash playing on the shore and in the water of a lake), not a volcano (CONTRADICTION: Two dogs on a leash playing on the shore and in the water of a volcano).
MISALIGNMENT TYPE: Object/Noun

CAPTION: a man kneeling on a surfboard as he starts to ride a wave
CONTRADICTION: a man hand-standing on a surfboard as he starts to ride a wave 
MISALIGNMENT: The surfer is kneeling on a surfboard (CAPTION: a man kneeling on a surfboard), not performing a hand-standing on it. (CONTRADICTION: a man hand-standing on a surfboard)
MISALIGNMENT TYPE: Object/Noun

CAPTION: Three pigeons on the side walk munching on a thrown out breadstick.
CONTRADICTION: Eight pigeons on the side walk munching on a thrown out pizza crust.
MISALIGNMENT: There are three pigeons eating a breadstick (CAPTION: Three pigeons munching on a breadstick), not eight. (CONTRADICTION: Eight pigeons munching on a breadstick)
MISALIGNMENT TYPE: Object/Noun

CAPTION: A box of pizza with peppers, onions and sausage on it.
CONTRADICTION: A box of pizza with pineapple on it.
MISALIGNMENT: The pizza has peppers, onions and mushrooms on it (CAPTION: peppers, onions and mushrooms), not pineapple (CONTRADICTION: pineapple)
MISALIGNMENT TYPE: Object/Noun

CAPTION: A baseball player holding a bat while standing next to a home plate.
CONTRADICTION: A baseball player holding a bat while standing next to Batman.
MISALIGNMENT: The baseball player is not holding a bat next to Batman (CONTRADICTION: player next to Batman) , instead is next to a home plate (CAPTION: player next to home plate) .
MISALIGNMENT TYPE: Object/Noun

CAPTION: A woman playing tennis is swinging at a tennis ball.
CONTRADICTION: A woman playing tennis is juggling tennis balls.
MISALIGNMENT: The woman is swinging at a tennis ball (CAPTION: woman playing tennis is swinging at a tennis ball), not juggling tennis balls (CONTRADICTION: woman playing tennis is juggling tennis balls).
MISALIGNMENT TYPE: Action/Verb

CAPTION: A bird is sitting on a branch eating a banana peel.
CONTRADICTION: A bird is sitting on a branch eating an apple.
MISALIGNMENT: The bird is eating an apple (CAPTION: bird eating an apple), not a banana peel (CONTRADICTION: bird eating a banana peel).
MISALIGNMENT TYPE: Object/Noun
"""

ATTR_CONGEN_FEW_SHOT_PROMPT = """
Guidelines:
- Attribute/Adjective Misalignment: Alter an attribute or adjective that describes an object or scene in the original caption. This alteration should create a contradiction in the description. Ensure that the changed attribute/adjective remains plausible within the context of the caption and doesn't alter the core meaning. The discrepancy between the original caption's attribute and the contradictory attribute should be highlighted in the misalignment description.

Examples: 

CAPTION: "a waterfall in a tropical forest with green plants and trees"
CONTRADICTION: a waterfall in a snowy forest with green plants and trees
MISALIGNMENT: The forest is not snowy (CONTRADICTION: snowy forest), instead is a tropical one (CAPTION: tropical forest)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: "a cartoon of a red haired mermaid holding a fish in the sea"
CONTRADICTION: a cartoon of a mermaid with black hair in the water
MISALIGNMENT: The hair of the cartoon mermaid is red (CAPTION: red haired mermaid), not black (CONTRADICTION: mermaid with black hair)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: "A cartoon drawing of a person with bat wings on a white paper with a keyboard and pens on a table ."
CONTRADICTION: A cartoon drawing of a person with angel wings on a white paper with a keyboard and pens on a table.
MISALIGNMENT: The person wings are bat wings (CAPTION: person with bat wings), not angel wings (CONTRADICTION: person with angle wings).
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: portrait of a naked woman with long hair on a grey background
CONTRADICTION: A portrait of a naked woman with short hair on a grey background
MISALIGNMENT: The woman has long hair (CAPTION: long hair), not short hair (CONTRADICTION: short hair)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: The colorful flowers are in the vase next to the window.
CONTRADICTION: The white and black flowers are in the vase next to the window.
MISALIGNMENT: The flowers are colorful (CAPTION: colorful flowers) , not white and black (CONTRADICTION: white and black flowers)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: Vase sitting next to the window with droopy flowers in it.
CONTRADICTION: Vase sitting next to the window with fresh flowers in it.
MISALIGNMENT: The vase has droppy flowers (CAPTION: droppy flowers), not fresh flowers (CAPTION: fresh flowers)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: A bicycle chained to a red pole and a green pole on the sidewalk in front of a building.
CONTRADICTION: A bicycle chained to a red pole and a blue pole on the sidewalk in front of a building.
MISALIGNMENT: One of the poles is red (CAPTION: green pole), not blue (CONTRADICTION: blue pole)
MISALIGNMENT TYPE: Attribute/Adjective
"""

VERB_CONGEN_FEW_SHOT_PROMPT = """
Guidelines:
- Action/Verb Misalignment: Modify a central action or verb in the original caption. This change should introduce a contradiction in terms of the activity or behavior described. The changed verb should make sense within the context and should neither be too drastic nor too obscure. Ensure the difference between the original caption's action and the contradictory action is clearly and succinctly articulated in the misalignment description.

Examples: 

CAPTION: "a close up of a lion with a long mane sitting on the grass with trees in the background"
CONTRADICTION: a close up of a lion with a long mane jumping on the grass in the forest with trees in the background
MISALIGNMENT: The lion is sitting (CAPTION: a lion sitting), not jumping on the grass (CONTRADICTION: lion jumping)
MISALIGNMENT TYPE: Action/Verb

CAPTION: "A painting of a man standing in front of a fire in a field with trees and sky in the background ."
CONTRADICTION: A painting of a man running in front of a fire in a field with trees and a cloudy sky .
MISALIGNMENT: The main the painting is standing (CAPTION: man standing in front of a fire), not running (CONTRADICTION: man running in front of a fire)
MISALIGNMENT TYPE: Action/Verb

CAPTION: "A tattooed woman in a purple brassiere and purple underpants is standing in front of a table with a bottle on it."
CONTRADICTION: A tattooed woman in a purple brassiere and purple underpants is dancing in front of a table with a bottle on it.
MISALIGNMENT: The woman is not dancing (CONTRADICTION: tattooed woman dancing), instead is sitting (CAPTION: A tattooed woman is standing)
MISALIGNMENT TYPE: Action/Verb

CAPTION: "portrait of a smiling man and woman hugging each other on the street with trees and buildings in the backgroun"
CONTRADICTION: portrait of a smiling man and woman fighting on the street with trees and buildings in the background
MISALIGNMENT: The man and woman are not fighting each other (CONTRADICTION: man and woman fighting), instead are hugging (CAPTION: a smiling man and woman hugging each other)
MISALIGNMENT TYPE: Action/Verb

CAPTION: A black background with a picture of a guy in a red hat jumping with a skate board.
CONTRADICTION: A black background with a picture of a guy in a red hat drinking water with a skate board.
MISALIGNMENT: The guy is not drinking water (CONTRADICTION: guy drinking water), instead is sitting (CAPTION: guy sitting)
MISALIGNMENT TYPE: Action/Verb

CAPTION: a kid trying to use a skating board on the road
CONTRADICTION: a kid breaking a skating board on the road
MISALIGNMENT: The kid is trying to use a skating board (CAPTION: kid trying to use a skating board), not breaking it (CONTRADICTION: kid breaking a skating board)
MISALIGNMENT TYPE: Action/Verb

CAPTION: Seated person wearing blue jeans holding a white corded electronic device.
CONTRADICTION: Seated person wearing blue jeans chewing a white cordless electronic device.
MISALIGNMENT: The person is holding a corded electronic device (CAPTION: person holding a white corded electronic device), not chewing a corded electronic device (CONTRADICTION: person chewing a corded electronic device)
MISALIGNMENT TYPE: Action/Verb

CAPTION: A cup, saucer and spoon sitting next to a newspaper.
CONTRADICTION: A cup, saucer, and spoon flying next to a newspaper.
MISALIGNMENT: The cup, saucer, and spoon are sitting (CAPTION: cup, saucer, and spoon sitting next to a newspaper), not flying (CONTRADICTION: cup, saucer, and spoon flying next to a newspaper).
MISALIGNMENT TYPE: Action/Verb

CAPTION: A man that is standing in the grass with a kite.
Contradiction: A man that is lying in the grass with a kite.
Misalignment: The man is standing (CAPTION: man standing in the grass with a kite), not lying (CONTRADICTION: man lying in the grass with a kite).
Misalignment Type: Action/Verb

"""

RELATION_CONGEN_FEW_SHOT_PROMPT = """
Guidelines:
- Relation Misalignment: Change the relationship or position between objects. This entails tweaking prepositions, positioning, or context which defines the relationship between the mentioned items. In the misalignment description, specifically indicate the changed relation and the affected subjects.- Mention at the SOURCE fields the changed preposition and related subject

Examples: 

CAPTION: "A laptop next to a stack of books on a wooden desk"
CONTRADICTION: A laptop under a stack of books on a wooden desk.
MISALIGNMENT: The laptop is next to the the books (CAPTION: laptop next to a stack of books), not under them (CONTRADICTION: laptop under a stack of books).
MISALIGNMENT TYPE: Relation

CAPTION: Two cats are sitting below a branch of a tree in front of a building with windows and trees in the background .
CONTRADICTION: Two cats are sitting above a branch of a tree in front of a building with windows and trees in the background .
MISALIGNMENT: The cats are in front of the building sitting below a branch (CAPTION: Two cats sitting below a branch), not above it (CONTRADICTION: Two cats sitting above a branch)
MISALIGNMENT TYPE: Relation

CAPTION: portrait of a redhead girl with blue eyes in a violet color t shirt sitting on a yellow color sofa near a gray wall
CONTRADICTION: portrait of a redhead girl with blue eyes in a violet color t shirt sitting on a yellow color sofa apart from a gray wall
MISALIGNMENT: The sofa is near the wall (CAPTION: a yellow sofa near a gray wall), not apart from it (CONTRADICTION: a yellow sofa apart from a gray wall)
MISALIGNMENT TYPE: Relation

CAPTION: Old fashioned chests are stacked atop each other on a city block.
CONTRADICTION: Old fashioned chests are stacked next to each other on a city block.
MISALIGNMENT: The chests are stacked atop each other (CAPTION: chests stacked atop each other), not next to each other (CONTRADICTION: chests stacked next to each other).
MISALIGNMENT TYPE: Relation

CAPTION: Boy holding large stuffed toy bear outside of building.
CONTRADICTION: Boy holding large stuffed toy bear inside of building.
MISALIGNMENT: The boy is outside of a building (CAPTION: Boy holding large stuffed toy bear outside of building), not inside of it  (CONTRADICTION: boy holding large stuffed toy bear inside of building) .
MISALIGNMENT TYPE: Relation
"""

GENERAL_CONGEN_FEW_SHOT_PROMPT = """
Choose randomly from one of this misalignment types options :
- Object/Noun Misalignment: Change a key object or noun.
- Attribute/Adjective Misalignment: Modify an attribute of an object.
- Action/Verb Misalignment: Alter a specific action or verb performed by the object.
- Relation Misalignment: Change the relationship or position between objects.
Highlight Change: Explicitly mention what was changed between the CAPTION and the CONTRADICTION in the MISALIGNMENT section.

Examples: 

CAPTION: "a cartoon of a robotic action figure standing on a rock in the desert with mountains in the background"
CONTRADICTION: a woman standing on a rock in the desert with mountains in the background
MISALIGNMENT: No woman (CONTRADICTION: a woman standing on a rock), instead there is a robotic action (CAPTION: a cartoon of a robotic action figure standing on a rock) 
MISALIGNMENT TYPE: Object/Noun

CAPTION: "a black and white image of a dark tunnel with a light shining through it"
CONTRADICTION: A black and white image of a dark mountain
MISALIGNMENT: This is a tunnel (CAPTION: a dark tunnel), not a black and white mountain (CONTRADICTION: dark mountain)
MISALIGNMENT TYPE: Object/Noun

CAPTION: "a gold coin with a logo on it on a gray wall"
CONTRADICTION: A gold coin with a logo on it is on an orange wall
MISALIGNMENT: The gold coin is on a gray wall (CAPTION: gray wall), not an orange wall (CONTRADICTION: orange wall)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: "a waterfall in a tropical forest with green plants and trees"
CONTRADICTION: a waterfall in a snowy forest with green plants and trees
MISALIGNMENT: The forest is not snowy (CONTRADICTION: snowy forest), instead is a tropical one (CAPTION: tropical forest)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: "A person dressed as Captain America is holding a shield in front of a wall."
CONTRADICTION: A person dressed as Captain America is throwing a shield and standing in front of a wall.
MISALIGNMENT: The person is not throwing a shield (CONTRADICTION: person throwing a shield), instead is holding it (CAPTION: person holding a shield)
MISALIGNMENT TYPE: Action/Verb

CAPTION: "a close up of a lion with a long mane sitting on the grass with trees in the background"
CONTRADICTION: a close up of a lion with a long mane jumping on the grass in the forest with trees in the background
MISALIGNMENT: The lion is sitting (CAPTION: a lion sitting), not jumping on the grass (CONTRADICTION: lion jumping)
MISALIGNMENT TYPE: Action/Verb

CAPTION: A black background with a picture of a guy in a red hat jumping with a skate board.
CONTRADICTION: A black background with a picture of a guy in a red hat drinking water with a skate board.
MISALIGNMENT: The guy is not drinking water (CONTRADICTION: guy drinking water), instead is sitting (CAPTION: guy sitting)
MISALIGNMENT TYPE: Action/Verb

CAPTION: a man kneeling on a surfboard as he starts to ride a wave
CONTRADICTION: a man hand-standing on a surfboard as he starts to ride a wave 
MISALIGNMENT: The surfer is kneeling on a surfboard (CAPTION: a man kneeling on a surfboard), not performing a hand-standing on it. (CONTRADICTION: a man hand-standing on a surfboard)
MISALIGNMENT TYPE: Object/Noun

CAPTION: "A laptop next to a stack of books on a wooden desk"
CONTRADICTION: A laptop under a stack of books on a wooden desk.
MISALIGNMENT: The laptop is next to the the books (CAPTION: laptop next to a stack of books), not under them (CONTRADICTION: laptop under a stack of books).
MISALIGNMENT TYPE: Relation

CAPTION: Two cats are sitting below a branch of a tree in front of a building with windows and trees in the background .
CONTRADICTION: Two cats are sitting above a branch of a tree in front of a building with windows and trees in the background .
MISALIGNMENT: The cats are in front of the building sitting below a branch(CAPTION: Two cats sitting below a branch), not above it (CONTRADICTION: Two cats sitting above a branch)
MISALIGNMENT TYPE: Relation
"""


TYPE_TO_FEW_SHOT_PROMPT = {
    "Relation": RELATION_CONGEN_FEW_SHOT_PROMPT,
    "Action/Verb": VERB_CONGEN_FEW_SHOT_PROMPT,
    "Attribute/Adjective": ATTR_CONGEN_FEW_SHOT_PROMPT,
    "Object/Noun": OBJECT_CONGEN_FEW_SHOT_PROMPT,
    "None": GENERAL_CONGEN_FEW_SHOT_PROMPT
}
