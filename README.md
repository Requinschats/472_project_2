## Repository URL

https://github.com/Requinschats/472_project_2

## Run the program

Run main.py in root

## Game parameters

** Everything is set in main.py

#### Set board parameters:

Instead of manual inputs in the console:

1. click into m.input_mock_game_settings()
2. change parameters from the mock function

1 explanation: run parameters can be selected from mocks.py. Mocks required to generate required game traces are found
at the bottom of the file, ex. input_mock_game_trace_8().

#### Set game parameters:

1. change play values on line 17
2. change heuristic values on line 18
3. set rounds count on line 15

## Output paths

- Scoreboard: scoreboard/scoreboard.
- Game traces: game_traces/game_traces

## Heuristics

Implementation in Heuristic/heuristic.py

#### Heuristic 1

In def evaluate_state_h1:

1. Check for winning state: return +- range extremities
2. Check for winning move: return +- close to range extremities
3. Center score: For each move on the board, calculate min and max distance from center (quadratic distance). Make it
   inverse as closer is better.
4. Subtract Max center score from min center score to get a differential. Positive is good. Negative is bad for max.
5. Connection score: For each move on the board, calculate for each player if the move is connected to the same symbol.
   Connection has close to exponential weight as each connection is counted twice.
6. Subtract Max connection score from min connection score to get a differential. Positive is good. Negative is bad for
   max.
7. Return a weighted combination of both metrics as the heuristic evaluation

#### Heuristic 2

In def evaluate_state_h2:

1. Check for winning state: return +- range extremities
2. Check for winning move: return +- close to range extremities
3. Cardinality differential score: for each move on the board calculate a variant of the connection score, checkout:
   select_surrounding_position_cardinality_contribution
4. Subtract Max cardinality score from min cardinality score to get a differential. Positive is good. Negative is bad
   for max.

#### Heuristic analysis

- H2 is faster to evaluate than H1 as it makes less iterates on the game board.
- To get good performing heuristics, I had to consider winning lines and winning moves on each heuristic evaluation.
  Sadly current implementation is slow to evaluate and slows down the heuristics. I had to use a maximum computing time
  of over 10 seconds to get good results (human hard to beat results).
- evaluate_state_random was used as a point of reference when developing
- Starting heuristic always wins on 4+ size boards
