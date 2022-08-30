# SlowType - Python type-print module
## All functions and classes
```python
SlowTypes.SlowType()
```
### - Default SlowType module function.
### Next:
```python
SlowTypes.SlowType_DelayRandom()
```
### - SlowType with random duration
### - Alternative:
```python
SlowTypes.SlowType_UsingDelayGenerator(..., lambda x, y: random.uniform(0.1, 0.2))
```
### Next:
```python
SlowTypes.SlowType_UsingDelayGenerator()
```
### - Using function to get delay
### - DelayGenerators (or user custom)
### Next:
```python
SlowtypeExamples.ProgressBarExample()
```
### Next:
### - Progress bar example
```python
SlowtypeExamples.PasswordHackerExample()
```
### Next:
### - Password hacker example
```python
DelayGenerators.Faster()
```
### - Makes type faster after next char
### Next:
```python
DelayGenerators.Slower()
```
### - Makes type slower after next char
### Next:
```python
DelayGenerators.PrintSleep(x, y)
```
### - Prints X chars and waiting Y seconds
### Next:
```python
PrintOnLine()
```
### - Print a text on line, where cursor is
### Next:
```python
ClearLine()
```
### Next:
### - Clear line, where cursor
```python
LineUp()
```
### - Moving cursor up
## Examples
### Example of slow type with input:
```python
text = SlowTypes.SlowType('What is your name?: ', 0.1, True)
```
### Example of using SlowTypes.SlowType_UsingDelayGenerator
```python
SlowTypes.SlowType_UsingDelayGenerator('Just a big string... ' * 5, DelayGenerators.Faster, 10)
```
#### Translated by google translate!
