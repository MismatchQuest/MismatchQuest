OBJECT_CONGEN_FEW_SHOT_PROMPT = """
Guidelines:
- Object/Noun Misalignment: Change a key object or noun in the caption to create a contradiction, you can also add or remove an object, or alter the quantity of an item. The contradictory caption should then focus on a different object/noun, and this discrepancy must be clearly highlighted in the misalignment description.

Examples: 

CAPTION: a cartoon of a robotic action figure standing on a rock in the desert with mountains in the background
CONTRADICTION: a woman standing on a rock in the desert with mountains in the background
MISALIGNMENT: No woman (CONTRADICTION: woman), instead there is a robotic action figure standing on a rock (CAPTION: robotic action figure standing on a rock)
MISALIGNMENT TYPE: Object/Noun

CAPTION: portrait of a beautiful woman with short hair in a white t shirt on the street with trees in the background
CONTRADICTION: portrait of a beautiful alien with short hair in a white t shirt on the street with trees in the background
MISALIGNMENT: A woman (CAPTION: woman) , not an alien  (CONTRADICTION: alien) , is the subject of the portrait.
MISALIGNMENT TYPE: Object/Noun

CAPTION: A cartoon painting of three cats and a mouse on a yellow wall .
CONTRADICTION: A cartoon painting of five cats and a mouse on a yellow wall .
MISALIGNMENT: Three cats (CAPTION: three cats), not five are in the cartoon painting.
MISALIGNMENT TYPE: Object/Noun

CAPTION: a painting of a landscape with mountains and clouds in the sky
CONTRADICTION: a painting of a landscape with a beach and clouds in the sky
MISALIGNMENT: The painting is of a landscape with mountains (CAPTION: landscape with mountains) , not trees (CONTRADICTION: landscape with a beach) .
MISALIGNMENT TYPE: Object/Noun

CAPTION: A black and green cat figurine on a gray surface.
CONTRADICTION: A black and green cat with a funny unicorn figurine on a gray surface.
MISALIGNMENT: The funny unicorn (CONTRADICTION: funny unicorn) is missing (CAPTION: None:) .
MISALIGNMENT TYPE: Object/Noun

CAPTION: a black and white drawing of a person wearing a helmet and headphones
CONTRADICTION: a black and white drawing of a person wearing a helmet and sunglasses
MISALIGNMENT: The person is wearing a headphone (CAPTION: person wearing a helmet and headphones), not sunglasses (CONTRADICTION: person wearing a helmet and sunglasses).
MISALIGNMENT TYPE: Object/Noun

CAPTION: a silhouette of a person standing in a forest with a castle in the background
CONTRADICTION: a silhouette of a dragon standing in a forest with a city in the background
MISALIGNMENT: The silhouette is of a person (CAPTION: silhouette of a person), not a dragon (CONTRADICTION: silhouette of a dragon)
MISALIGNMENT TYPE: Object/Noun

CAPTION: a black and white landscape of an iceberg in the ocean with a boat on the sand
CONTRADICTION: a black and white landscape of an iceberg in the ocean with a boat in the water
MISALIGNMENT: The boat is in the sand (CAPTION: boat on the sand), not on the sand (CONTRADICTION: boat in the water)
MISALIGNMENT TYPE: Object/Noun
"""

ATTR_CONGEN_FEW_SHOT_PROMPT = """
Guidelines:
- Attribute/Adjective Misalignment: Alter an attribute or adjective that describes an object or scene in the original caption. This alteration should create a contradiction in the description. Ensure that the changed attribute/adjective remains plausible within the context of the caption and doesn't alter the core meaning. The discrepancy between the original caption's attribute and the contradictory attribute should be highlighted in the misalignment description.

Examples: 

CAPTION: a gold coin with a logo on it on a gray wall
CONTRADICTION: A gold coin with a logo on it is on an orange wall
MISALIGNMENT: The gold coin is on a gray wall (CAPTION: gray wall), not an orange wall (CONTRADICTION: orange wall)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: a waterfall in a tropical forest with green plants and trees
CONTRADICTION: a waterfall in a snowy forest with green plants and trees
MISALIGNMENT: The forest is not snowy (CONTRADICTION: snowy forest), instead is a tropical one (CAPTION: tropical forest)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: A cartoon drawing of a person with bat wings on a white paper with a keyboard and pens on a table .
CONTRADICTION: A cartoon drawing of a person with angel wings on a white paper with a keyboard and pens on a table.
MISALIGNMENT: The person wings are bat wings (CAPTION: person with bat wings), not angel wings (CONTRADICTION: person with angle wings).
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: portrait of a woman with long hair on a grey background
CONTRADICTION: A portrait of a woman with short hair on a grey background
MISALIGNMENT: The woman has long hair (CAPTION: long hair), not short hair (CONTRADICTION: short hair)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: A futuristic spider toy and a robotic spider toy on a gray surface .
CONTRADICTION: A futuristic spider toy and a plastic spider toy on a gray surface
MISALIGNMENT: The spider toy is robotic (CONTRADICTION: robotic spider toy), not plastic (CAPTION: plastic spider toy)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: a black and white drawing of a light fixture with a gray background
CONTRADICTION: A colorful drawing of a light fixture with a gray background
MISALIGNMENT: The drawing is not colorful (CONTRADICTION: colorful drawing) , instead is black and white (CAPTION: black and white drawing) .
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: a painting of a skeleton person with a skull face and a hooded person with a skull face
CONTRADICTION: A painting of a real person with a skull face and a hooded person with a skull face
MISALIGNMENT: The person is not real (CONTRADICTION: real person), but a skeleton (CAPTION: skeleton person)
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: A black and white portrait of a bald man with glasses and a beard .
CONTRADICTION: A black and white portrait of a bald man with glasses and an eyepatch
MISALIGNMENT: The man has glasses and beard (CONTRADICTION: man with glasses and a beard), not glasses and eyepatch (CAPTION: man with glasses and an eyepatch) .
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: a red color smoke coming from a fire in the sky with clouds and grass on the ground
CONTRADICTION: a blue color smoke coming from a fire in the sky with clouds and grass on the ground
MISALIGNMENT: The smoke is red (CAPTION: red color smoke), not blue (CONTRADICTION: blue color smoke)
MISALIGNMENT TYPE: Attribute/Adjective
"""

VERB_CONGEN_FEW_SHOT_PROMPT = """
Guidelines:
- Action/Verb Misalignment: Modify a central action or verb in the original caption. This change should introduce a contradiction in terms of the activity or behavior described. The changed verb should make sense within the context and should neither be too drastic nor too obscure. Ensure the difference between the original caption's action and the contradictory action is clearly and succinctly articulated in the misalignment description.

Examples: 

CAPTION: "A person dressed as Captain America is holding a shield in front of a wall."
CONTRADICTION: A person dressed as Captain America is throwing a shield and standing in front of a wall.
MISALIGNMENT: The person is not throwing a shield (CONTRADICTION: person throwing a shield), instead is holding it (CAPTION: person holding a shield)
MISALIGNMENT TYPE: Action/Verb

CAPTION: "a close up of a lion with a long mane sitting on the grass with trees in the background"
CONTRADICTION: a close up of a lion with a long mane drinking water on the grass in the forest with trees in the background
MISALIGNMENT: The lion is sitting (CAPTION: a lion sitting), not jumping on the grass (CONTRADICTION: lion drinking water)
MISALIGNMENT TYPE: Action/Verb

CAPTION: "A painting of a man standing in front of a fire in a field with trees and sky in the background ."
CONTRADICTION: A painting of a man running in front of a fire in a field with trees and a cloudy sky .
MISALIGNMENT: The main the painting is standing (CAPTION: man standing in front of a fire), not running (CONTRADICTION: man running in front of a fire)
MISALIGNMENT TYPE: Action/Verb

CAPTION: "A cartoon of a man in a suit and hat sitting at a table in a city with buildings and a blue sky."
CONTRADICTION: A cartoon of a man in a suit and hat jumping on a table in a city with buildings and a blue sky.
MISALIGNMENT: The man is not jumping (CONTRADICTION: man in a suit and hat jumping) , instead is sitting at the table (CAPTION: man in a suit and hat sitting)
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

CAPTION: a futuristic spaceship flying in the sky with clouds and stars in the background
CONTRADICTION: a futuristic spaceship explodes in the sky with clouds and stars in the background
MISALIGNMENT: The spaceship is not exploded (CONTRADICTION: spaceship explodes), instead is flying (CAPTION: spaceship flying)
MISALIGNMENT TYPE: Action/Verb

CAPTION: a fantasy painting of a forest with a river flowing through it and trees in the background
"CONTRADICTION: a fantasy painting of a forest with a river freeze through it and trees in the background
MISALIGNMENT: The river is flowing (CONTRADICTION: river flowing), not freeze (CAPTION: river freeze)
MISALIGNMENT TYPE: Action/Verb"
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

CAPTION: "A laptop next to a stack of books on a wooden desk"
CONTRADICTION: A laptop under a stack of books on a wooden desk.
MISALIGNMENT: The laptop is next to the the books (CAPTION: laptop next to a stack of books), not under them (CONTRADICTION: laptop under a stack of books).
MISALIGNMENT TYPE: Relation

CAPTION: Two cats are sitting below a branch of a tree in front of a building with windows and trees in the background .
CONTRADICTION: Two cats are sitting above a branch of a tree in front of a building with windows and trees in the background .
MISALIGNMENT: The cats are in front of the building sitting below a branch(CAPTION: Two cats sitting below a branch), not above it (CONTRADICTION: Two cats sitting above a branch)
MISALIGNMENT TYPE: Relation

CAPTION: a black and white drawing of a light fixture with a gray background
CONTRADICTION: A colorful drawing of a light fixture with a gray background
MISALIGNMENT: The drawing is not colorful (CONTRADICTION: colorful drawing) , instead is black and white (CAPTION: black and white drawing) .
MISALIGNMENT TYPE: Attribute/Adjective

CAPTION: a futuristic spaceship flying in the sky with clouds and stars in the background
CONTRADICTION: a futuristic spaceship explodes in the sky with clouds and stars in the background
MISALIGNMENT: The spaceship is not exploded (CONTRADICTION: spaceship explodes), instead is flying (CAPTION: spaceship flying)
MISALIGNMENT TYPE: Action/Verb

CAPTION: a silhouette of a person standing in a forest with a castle in the background
CONTRADICTION: a silhouette of a dragon standing in a forest with a city in the background
MISALIGNMENT: The silhouette is of a person (CAPTION: silhouette of a person), not a dragon (CONTRADICTION: silhouette of a dragon)
MISALIGNMENT TYPE: Object/Noun
"""

TYPE_TO_FEW_SHOT_PROMPT = {
    "Relation": RELATION_CONGEN_FEW_SHOT_PROMPT,
    "Action/Verb": VERB_CONGEN_FEW_SHOT_PROMPT,
    "Attribute/Adjective": ATTR_CONGEN_FEW_SHOT_PROMPT,
    "Object/Noun": OBJECT_CONGEN_FEW_SHOT_PROMPT,
    "None": GENERAL_CONGEN_FEW_SHOT_PROMPT
}
