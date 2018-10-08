import json, os

class Settings:

    def __init__(self,env):

        with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as f:
            config = json.load(f)

            if(env == "dev"):
                self.host = config['default']['db']['host']
                self.port = config['default']['db']['port']
                self.database = config['default']['db']['database']
                self.user = config['default']['db']['user']
                self.password = config['default']['db']['password']

            if(env == "test"):
                self.host = config['test']['db']['host']
                self.port = config['test']['db']['port']
                self.database = config['test']['db']['database']
                self.user = config['test']['db']['user']
                self.password = config['test']['db']['password']

            if(env == "prod"):
                self.host = config['production']['db']['host']
                self.port = config['production']['db']['port']
                self.database = config['production']['db']['database']
                self.user = config['production']['db']['user']
                self.password = config['production']['db']['password']

