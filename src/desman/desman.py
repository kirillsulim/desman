import requests
import sys
import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--status', action='store_true', help='show response status')
parser.add_argument('-b', '--body', action='store_true', help='show response body')
parser.add_argument('-H', '--header', action='store_true', help='show response headers')
parser.add_argument('file', metavar='FILE', type=argparse.FileType('r'))


class App:
    def run(self, args):
        self.args = parser.parse_args(args[1:])
        with(self.args.file) as f:
            try:
                reqdata = yaml.load(f)
                self.run_req(reqdata)
            except Exception as e:
                print(e)
                raise

    def run_req(self, reqdata):
        response = requests.request(str(reqdata['method']).lower(), reqdata['url'], params=reqdata['params'], headers=reqdata['headers'], data=reqdata['body'])
        if self.args.status:
            print("> Status: {} {}".format(response.status_code, response.reason))
        if self.args.header:
            print("> Headers:")
            for header in response.headers:
                print(">   {}: {}".format(header, response.headers[header]))
        if self.args.body:
            print()
            print(response.text)
        if not (self.args.body or self.args.status or self.args.header):
            print(response.text)


def main():
    App().run(sys.argv)
