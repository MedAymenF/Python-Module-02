class CsvReader():
    def __init__(self, filename=None, sep=',',
                 header=False, skip_top=0, skip_bottom=0):
        self.get_header = header
        self.missing = False
        self.corrupted = False
        self.data = []
        try:
            self.file = open(filename)
        except FileNotFoundError:
            self.missing = True
        else:
            n_columns = None
            if self.get_header:
                self.header = self.file.readline().rstrip().split(sep)
                n_columns = len(self.header)
            for i in range(skip_top):
                self.file.readline()
            while True:
                line = self.file.readline().rstrip()
                if not line:
                    break
                split_line = line.split(sep)
                if '' in split_line:
                    self.corrupted = True
                    break
                length = len(split_line)
                if (n_columns and n_columns != length):
                    self.corrupted = True
                    break
                n_columns = length
                self.data.append(split_line)
            if not self.corrupted and skip_bottom:
                self.data = self.data[:-skip_bottom]

    def __enter__(self):
        if self.missing or self.corrupted:
            return None
        return self

    def __exit__(self, type, value, traceback):
        if not self.missing:
            self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip_bottom.
Returns:
nested list (list(list, list, ...)) representing the data."""
        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
Returns:
list: representing the data (when self.get_header is True).
None: (when self.get_header is False)."""
        if self.get_header:
            return self.header
        else:
            return None
