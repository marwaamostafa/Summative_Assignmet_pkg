from typing import Any, Optional
import matplotlib
import matplotlib.pyplot as plt
import yaml


class Analysis():
    def __init__(self, analysis_config:str):
        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)

        self.config = config
        

    def load_data(self):
        print(self.config['figure_title'])
        

    def compute_analysis(self):
        pass

    def plot_data(self, save_path:Optional[str] = None) -> plt.Figure:
        pass
          # If save_path is not provided, use the default_save_path from the config
        if save_path is None:
            save_path = self.config['default_save_path']

        # Make the save_path absolute based on the project directory
        save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), save_path)

        logging.info('Saving plot to: %s', save_path)