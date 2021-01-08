### How do I run the code?

```sh
python index.py -p /path/to/the/directory/with/the/scripts -e file_to_exclude.py
python index.py --path=/path/to/the/directory/with/the/scripts --exclude=file_to_exclude.py
```

### Example

```sh
python index.py -p scripts -e config.py
python index.py --path=scripts --exclude=config.py

python index.py -p C:\Users\Desktop\scripts -e config.py
python index.py --path=C:\Users\Desktop\scripts --exclude=config.py
```
