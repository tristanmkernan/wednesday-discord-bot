# Wednesday Frog Bot

<p align="center">
  <a href="https://discordapp.com/api/oauth2/authorize?client_id=596048932971348027&permissions=116800&scope=bot"><img src="https://img.shields.io/badge/discord-add%20bot-lightgrey.svg" /></a>
</p>

[](https://discordapp.com/api/oauth2/authorize?client_id=596048932971348027&permissions=116800&scope=bot)

## Development

```shell
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ nano -w .env  # set BOT_PASSWORD
$ echo BOT_PASSWORD=42
$ python main.py
```

## Publish

As above, with a `.env` file configured, use Docker to run the app.

```shell
$ docker-compose build
$ docker-compose up --detach
```

## License

GPLv3+
