# Knight tour puzzle
Command line game
___

## How to play

### 1. Input board size.

Size by `X` axle `space` size by `Y` axel 

Example (x = 6, y = 4):
> Enter your board dimensions: 6 4
### 2. Input first move.

Coordinate by `X` axle `space` coordinate by `Y` axel 

Example (x = 2, y = 3):
> Enter the knight's starting position: 2 3

### 3. Continue moves till you will step on each cell.

Coordinate by `X` axle `space` coordinate by `Y` axel 

Example (x = 2, y = 3):
> Enter the knight's starting position: 2 3

## Board

```commandline
 ---------------------
4| __ __ __  3 __ __ |
3| __  X __ __ __ __ |
2| __ __ __  5 __ __ |
1|  1 __  3 __ __ __ |
 ---------------------
    1  2  3  4  5  6

```
`X` - current position

`Any number` - How many moves possible to do from that number position

`*` - last moves

## Game solution
Game continue till you will step each cell or situation when you can't move.

If you visit all cell - **you win!**