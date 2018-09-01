import requests
import sys
import yaml
import argparse
from jinja2 import Template

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--status', action='store_true', help='show response status')
parser.add_argument('-b', '--body', action='store_true', help='show response body')
parser.add_argument('-H', '--header', action='store_true', help='show response headers')
parser.add_argument('-e', '--environment', default=None)
parser.add_argument('file', metavar='FILE', type=argparse.FileType('r'))


class App:
    def run(self, args):
        self.args = parser.parse_args(args[1:])
        try:
            if self.args.environment:
                with open(self.args.environment) as env_file:
                    env = yaml.load(env_file)
            else:
                env = {}
            with self.args.file as request_file:
                template = Template(request_file.read())
            request_data = yaml.load(template.render(env))
            response = self.run_request(request_data)
            self.print_response(response)
        except Exception as e:
            print(e)
            raise

    def run_request(self, request_data):
        return requests.request(
            str(request_data['method']).lower(),
            request_data['url'],
            params=request_data['params'],
            headers=request_data['headers'],
            data=request_data['body']
        )

    def print_response(self, response):
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


if __name__ == '__main__':
    main()
