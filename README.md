# SlowType - Python type-print module
## All functions and classes
### SlowTypes.SlowType()
#### - Default SlowType module function.
### SlowTypes.SlowType_DelayRandom()
#### - SlowType with random duration
#### - Alternative:
#### - SlowTypes.SlowType_UsingDelayGenerator(..., lambda x, y: random.uniform(0.1, 0.2))
### SlowTypes.SlowType_UsingDelayGenerator()
#### - Using function to get delay
#### - DelayGenerators (or user custom)
### SlowtypeExamples.ProgressBarExample()
#### - Progress bar example
### SlowtypeExamples.PasswordHackerExample()
#### - Password hacker example
### DelayGenerators.Faster()
#### - Makes type faster after next char
### DelayGenerators.Slower()
#### - Makes type slower after next char
### DelayGenerators.PrintSleep(x, y)
#### - Prints X chars and waiting Y seconds
### PrintOnLine()
#### - Print a text on line, where cursor is
### ClearLine()
#### - Clear line, where cursor
### LineUp()
#### - Moving cursor up
## Examples
### Example of slow type with input:
#### text = SlowTypes.SlowType('What is your name?: ', 0.1, True)
### Example of using SlowTypes.SlowType_UsingDelayGenerator
#### SlowTypes.SlowType_UsingDelayGenerator('Just a big string... ' * 5, DelayGenerators.Faster, 10)
##### Translated by google translate!