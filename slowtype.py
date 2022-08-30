"""

SlowType - Small library for text type effect

Created by Its-MatriX

Found a bug?
Discord: 404 - Not Found#9176

"""

from time import sleep
from random import uniform, choice
from sys import stdout


class DelayGenerators:

    def Faster(CharacterIndex, TypeTextLength, Divide: float = 1):
        """
        
        Returns: (TypeTextLength-CharacterIndex)/Divide

        In args: float

        """
        return (TypeTextLength - CharacterIndex) / Divide

    def Slower(CharacterIndex, TypeTextLength, Divide: float = 1):
        """
        
        Returns: -(CharacterIndex-TypeTextLength)/Divide

        In args: float

        """
        return (CharacterIndex) / Divide

    def PrintSleep(CharacterIndex, TypeTextLength, Args):
        """

        In args: (DivMod, Sleep)
        Print DivMod characters and sleeps Sleep seconds

        """
        DivMod = Args[0]
        Sleep = Args[1]

        CharacterIndex += 1

        if CharacterIndex % DivMod != 0:
            return 0
        else:
            return Sleep


class SlowTypes:

    def SlowType(TypeText: str,
                 NextCharDelay: float = 0.1,
                 UseInput: bool = False,
                 NewLineAfterEnd: bool = True):
        """
        
        Standard SlowType, delay has attribute NextCharDelay
        
        """

        for TypeChar in TypeText:
            print(TypeChar, end='', flush=True)
            sleep(NextCharDelay)

        if UseInput:
            return input()

        if NewLineAfterEnd:
            print()

    def SlowType_DelayRandom(TypeText: str,
                             NextCharDelayMin: float = 0.1,
                             NextCharDelayMax: float = 0.2,
                             UseInput: bool = False,
                             NewLineAfterEnd: bool = True):
        """
        
        Random delay (from NextCharDelayMin to NextCharDelayMax)
        
        Alternative:
        SlowTypes.SlowType_UsingDelayGenerator(..., lambda x, y: random.uniform(0.1, 0.2))

        """

        for TypeChar in TypeText:
            print(TypeChar, end='', flush=True)
            sleep(uniform(NextCharDelayMin, NextCharDelayMax))

        if UseInput:
            return input()

        if NewLineAfterEnd:
            print()

    def SlowType_UsingDelayGenerator(TypeText: str,
                                     DelayGenerator,
                                     DelayGeneratorArgs: any = None,
                                     UseInput: bool = False,
                                     NewLineAfterEnd: bool = True):
        """
        
        DelayGenerator: Function
        Attributes:
            CharacterIndex: attribute #0, index of character (first character has index 0)
            len TypeText: attribute #1, length of type text

        Example of DelayGenerator:

        / ------------------------------ /

        def GenerateDelay(CharacterIndex, TypeTextLength, OtherArgs):
            return CharacterIndex / 10 # delay: index/10 secs

        SlowTypes.SlowType_UsingDelayGenerator(..., GenerateDelay, (1, 2, 3), False)

        / ------------------------------ /

        And acceps args for delay generator function (any object as arg, ex: {"Speed": 1, ...})
            
        Delay returned by DelayGenerator function
        
        """

        CharacterIndex = 0
        for TypeChar in TypeText:
            print(TypeChar, end='', flush=True)

            if DelayGeneratorArgs:
                sleep(
                    DelayGenerator(CharacterIndex, len(TypeText),
                                   DelayGeneratorArgs))
            else:
                sleep(DelayGenerator(CharacterIndex, len(TypeText)))

            CharacterIndex += 1

        if UseInput:
            return input()

        if NewLineAfterEnd:
            print()


def _random_chars():
    return ''.join([choice('QWERTYUIOPASDFGHJKLZXCVBNM') for x in range(15)])


def PrintOnLine(TypeText: str,
                Clear: bool = True,
                NewLineAfterEnd: bool = False):
    """
    
    Types a text on line, where cursor is now
    
    """
    print(TypeText, end='' if not Clear else '\r', flush=True)

    if NewLineAfterEnd:
        print()


def ClearLine(GoToLineUp: bool = False):
    """
    
    Clear a line, where cursor is now
    
    """

    if GoToLineUp:
        stdout.write('\x1b[1A')
        stdout.write('\x1b[2K')
    else:
        stdout.write('\x1b[2K')


def LineUp():
    """
    
    Moving cursor on 1 line up
    
    """

    stdout.write('\x1b[1A')


class SlowtypeExamples:

    def ProgressbarExample():
        """
        
        Progress bar example
        Progress: #_________ [10%]
        
        """

        Progress = 0

        while Progress < 20:
            sleep(.1)
            Progress += 1
            PrintOnLine(f'Progress: ' + '#' * Progress + '_' *
                        (20 - Progress) + ' [' + str(Progress * 5) + '%]')

        ClearLine()
        PrintOnLine('Progress: DONE')

        print('\n')

    def PasswordHackerExample():
        """
        
        Password hacker example
        ABCDEABCDE | INVALID
        
        """

        print('Password hacker\n')

        while True:
            PrintOnLine(_random_chars() + ' | INVALID')
            sleep(.1)
