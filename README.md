# Alpha(bot)bot

## Server

### Download
```sh
sh <(wget -qO- https://raw.githubusercontent.com/PietroJominiITIS/alphabotbot/master/scripts/clone.sh) server alphabotbot_server
```

### Run
```sh
cd alphabot_server
python3 server.py
```

## Client

### Download
```sh
sh <(wget -qO- https://raw.githubusercontent.com/PietroJominiITIS/alphabotbot/master/scripts/clone.sh) client alphabot_client
```

### Run
```sh
cd alphabot_client
python3 client.py
```

## TODOS
- [x] apply [standard protocol](https://github.com/conradis/TPSIT-classi-quinte/blob/main/alphabot/specifica.md)
- [ ] images stream
- [x] dummy alphabot controller
- [x] rework file structure to allow common modules
- [ ] documentation / comments
- [ ] makes medium.py common -> server + client
- [ ] log