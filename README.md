Assuming you have venvs set up for multiple Python versions at e.g.
`.venv-{VERSION}`, you can run something like:

```sh
for i in $(ls -a | grep venv); do echo "$i"; echo ""; source $i/bin/activate; python main.py; echo ""; done
```

Running with:

```
3.8.19
3.9.19
3.10.14
3.11.8
3.11.9
3.12.3
```

yields:

```
.venv-3.8.19

Hello from foo.bar

.venv-3.9.19

Hello from foo.bar

.venv-3.10.14

Hello from foo.bar

.venv-3.11.8

Hello from foo.bar

.venv-3.11.9

Traceback (most recent call last):
  File ".../main.py", line 33, in <module>
    print(foo.bar)
          ^^^^^^^
  File "<frozen importlib.util>", line 276, in __getattribute__
AttributeError: module 'foo' has no attribute 'bar'

.venv-3.12.3

Traceback (most recent call last):
  File ".../main.py", line 33, in <module>
    print(foo.bar)
          ^^^^^^^
  File "<frozen importlib.util>", line 222, in __getattribute__
AttributeError: module 'foo' has no attribute 'bar'
```
