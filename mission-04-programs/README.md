# Mission 4 - How programs run

## 1. Task / objective

Run a simple Python file and compare a compiler with an interpreter.

## 2. Work completed

I ran `python3 hello.py` and got `Hello from Python`.

| Point | Compiler | Interpreter |
| --- | --- | --- |
| When it works | Before the translated code runs. | While the program runs. |
| Usual result | An object file or executable. | The result of running the code, like text on screen. |
| Example | Clang compiling a C program. | CPython running Python bytecode. |
| Advantage | You can run the compiled file again. | You can try small edits directly from the source. |

A compiler translates the code before it runs. An interpreter carries out the instructions while the program runs. CPython does both by turning source into bytecode and then running it.

## 3. Commands / tools used

`python3 hello.py` ran the file. `print()` showed the message.

## 4. My understanding

The text in the file tells Python what to do. The text in Terminal is what the program printed.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[hello.py](hello.py)

## 8. Commit details

Local. Commit and push pending.
