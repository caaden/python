import pandas


class PCLReader(object):
    def __init__(self):
        self.initial_rows = 11

    def read_pcl(self, path_to_pcl):
        return pandas.read_csv(path_to_pcl, skiprows=self.initial_rows, header=None, names=("x", "y", "z"), delim_whitespace=True)
