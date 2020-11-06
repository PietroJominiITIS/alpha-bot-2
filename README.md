# Alpha(bot)bot

## Server
```sh
./server/run.sh
# or
cd server && python3 index.py
```

## Client
```sh
# Still a placeholder client
python3 client_dummy.py
```

## Protocol
There are two types of messages:
1. sent by the `client`, received by the `server`
2. sent by the `server`, received by the `client`

### `client` -> `server`
The message has the form of: `origin;destination`

`origin` and `destination` have to be replaced by the actual origin and destination.

### `server` -> `client`
```
Status:
--------------
| OK? | DESC |   ==>    OK?.DESC
--------------          0.0 -> OK
                        0.1 -> OK :: No path
                        1.0 -> FAILED :: Wrong incoming format
                        1.1 -> FAIELD :: Origin not registered
                        1.2 -> FAILED :: Destination not registered
                        1.3 -> FAILED :: Server fault
Data:
0.1, 1.* -> None
       ----------------
0.0 -> | DIR | AMOUNT | (repeated)  ==>    DIR
       ----------------                      N -> Nord
                                             E -> Est
                                             S -> Sud
                                             W -> West 
                                           AMOUNT :: integer
EXAMPLE:
0.0;N10W200S15
1.2;
```
The message has the form of: `status;data`
```
-----------------
| status | data |    ==>    status;data
-----------------
```
#### status
|code|type|meaning|
|:-|:-:|-:|
|0.0|OK|all clear
|0.1|OK|no path found
|1.0|FAILED|wrong incoming format
|1.1|FAILED|origin not found
|1.2|FAILED|destination not found
|1.3|FAILED|server fault

#### data
|code|data
|:-|-:|
|0.1, 1.*|none
|0.0|`dir|amount` (\| is to be omitted)

**dir**
- `N` -> nord
- `E` -> est
- `S` -> sud
- `W` -> west

**amount**: any integer