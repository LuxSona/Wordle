# Description

Wordle is a puzzle game hosted by the New York Times. The goal of the game is to guess a hidden, 5 letter word in under 6 guesses.

Each guess reveals more information about the hidden word. Specifically, when you guess a word, the letters from your guess are marked according to their presence in the hidden word.
## Rules of Wordle
If the player guesses a letter that's present in the word, AND the letter corresponds to the same place on the hidden word, then that letter is marked (G)REEN no matter what.
If the player guesses a letter that's present in the word, but the letter does not correspond to the same place on the hidden word, then that letter is marked (Y)ELLOW.
If the player guesses a letter that's not present in the word, then that letter is marked G(R)AY.

For example, if `secret = heron` and `guess = hello`, then the colors that would be marked are `GGRRY`. 

If a word contains two of the same letter, we check for each individual letter. For example, if `secret=chess` and `guess=scars`, then the letters would be marked as `YYRRG`, because the final 's' is in the correct place, but the initial 's' is not.

Finally, if a guess contains two of the same letter, and that matches only with one on our secret word, the second of the two letters gets marked as gray. For example, `secret=caves` and `guess=chess`, the result would be `YRYRY`.

# Implementation
This project aims to implement Wordle using a client-server style architecture. The logical implementation will be handled by a server on the backend and any/all front-end logic will be handled by the client. These two entities communicate using a specific schema (see )
