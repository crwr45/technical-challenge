Command-line usage:

```shell
python -m listmanager --help
```

Add an entry for product 21 to a gift list:
```shell
python -m listmanager --list_file ~/list.json add --product_file ~/products.json 21
```

Remove the entry for product 21 from a gift list:
```shell
python -m listmanager --list_file ~/list.json remove --product_file ~/products.json 21
```

Purchase product 18 from a gift list:
```shell
python -m listmanager --list_file ~/list.json purchase --product_file ~/products.json 21
```


Show all items on a list:
```shell
python -m listmanager --list_file ~/list.json listitems
```


See purchasing status of a list:
```shell
python -m listmanager --list_file ~/list.json status
```
