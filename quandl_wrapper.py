import urllib.request

class wrapper:
    def __init__(self, APIkey):
        self.APIkey = APIkey

    def query(self, data_type, data_name, data_code, output_format, options={}):
        query = "https://www.quandl.com/api/v3/" + data_type + "/" + data_name + "/" + data_code + "." + output_format + "?"
        for command, value in options.items():
            query += command + "=" + str(value) + "&"
        query += "api_key=" + self.APIkey
        return urllib.request.urlopen(query).read()
