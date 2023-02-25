from flask import Flask
import threading
import time
import toml
import logging

class Config:
    def __init__(self):
        try:
            with open('./config.toml', 'r') as config_file:
                self._config = toml.load(config_file)
        except FileNotFoundError:
            print('cant find config')

    @property
    def network_port(self):
        return self._config['network']['port']

    @network_port.setter
    def network_port(self, port):
        if (not isinstance(port, int)):
            raise ValueError
        
        self._config["network"]["port"] = port

    @property
    def database_location(self):
        return self._config['database']["uri"]

    @database_location.setter
    def database_location(self, location):
        if (not isinstance(location, str)):
            raise ValueError
        
        self._config["database"]["uri"]= location

    def save(self):
        with open("./config.toml", 'w') as config_file:
            toml.dump(self._config, config_file)


app = Flask(__name__)

def main():
    app.run()


if __name__ == "__main__":
    main()
