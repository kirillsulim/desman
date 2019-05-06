import requests
import sys
import yaml
import argparse
from jinja2 import Template

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--status', help='show response status', action='store_true')
parser.add_argument('-b', '--body', help='show response body', action='store_true')
parser.add_argument('-H', '--header', help='show response headers', action='store_true')
parser.add_argument('-e', '--environment', help='use environment files', default=[], action='append')
parser.add_argument('file', help='request file')


def dict_merge_add(d1, d2):
    for k, v in d1.items():
        if k in d2:
            d2[k] = dict_merge_add(v, d2[k])
    d1.update(d2)
    return d1


class App:
    def __init__(self):
        self.args = None

    def run(self, args):
        self.args = parser.parse_args(args[1:])
        try:
            env = {}
            for env_file_name in self.args.environment:
                with open(env_file_name, encoding="utf-8") as env_file:
                    dict_merge_add(env, yaml.load(env_file, Loader=yaml.BaseLoader))

            with open(self.args.file, encoding="utf-8") as request_file:
                template = Template(request_file.read())

            request_data = yaml.load(template.render(env), Loader=yaml.BaseLoader)
            response = self.run_request(request_data)
            self.print_response(response)
        except Exception as e:
            print(e)
            raise

    def run_request(self, request_data):
        return requests.request(
            str(request_data.get('method')).lower(),
            request_data.get('url'),
            params=request_data.get('params'),
            headers=request_data.get('headers'),
            data=request_data.get('body').encode("utf-8"),
        )

    def print_response(self, response):
        if self.args.status:
            print("> Status: {} {}".format(response.status_code, response.reason))
        if self.args.header:
            print("> Headers:")
            for header in response.headers:
                print(">   {}: {}".format(header, response.headers[header]))
        if self.args.body and response.text:
            print()
            print(response.text)
        if not (self.args.body or self.args.status or self.args.header):
            print(response.text)


def main():
    App().run(sys.argv)


if __name__ == '__main__':
    main()
