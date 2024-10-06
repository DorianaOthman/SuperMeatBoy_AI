# SuperMeatBoy_AI
Super Meat Boy Pygame game simulation to observe and test performance AI behavior against human participants

Super Meat Boy pygame Demo 
https://github.com/user-attachments/assets/7a9af848-dac8-4630-a732-844dd4dff095

Focus of AI Project:
- I focused on the problem of trying to create a suitable AI for the video game Super Meat Boy. The goal of this AI will be to get to its target as quickly as possible in as few deaths as possible.
- The “Light World” implemention performed by CoderboiYT (https://github.com/CoderboiYT/SuperMeatBoyAI/tree/main0 was compared against my “Dark Word” implementation. “Light World” contains the base levels in Super Meat Boy and “Dark World” contains the higher difficulty versions of these levels.
- The project was later expanded to test against human participants to compare performance.

Algorithms Implemented:
- Pathway Algorithm:
  - To determine the best pathway distance for each Meat Boy, BFS was used; this was specifically used as a fitness measure to rank the Meat Boys in each generation
- Neural Networks:
  - The Neural Networks in this implementation represent the “brain” of a Meat Boy; this determines the path that a Meat Boy takes and also determines if it should jump. The weight values of each Meat Boy are only changed based on the predetermined percentage chance set by the programmer. The Neural Networks initial input layer, hidden layer, and outer layer values are also initialized by the programmer.
- Genetic Algorithms:
  - Genetic Algorithms is the method used to improve each generation of Meat Boys. This is done by using an initial cut off percentage to determine the number of “good” and “bad” Meat Boys of each generation based on their ranking; the number of “good” and “bad” Meat Boys kept for the new generation is decided by initial predetermined percentages set by the programmer. The remaining Meatboys needed to fill the new generation are then determined by picking random “good” Meat Boy parents and creating new children based on a combination of their parent’s weights from their Neural Networks; the percentage taken from each parent is based on a predetermined percentage value. Another predetermined percentage also decides if these newly created children will have their weights modified. For each new generation, all of the “bad” Meatboys kept will have their weights modified.

Results:
- The Super Meat Boy AI was able to complete all tested levels effectively and performed better than most human participants. For full details of these results, you can read both of my reports in the research branch of this repository.
