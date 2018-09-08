# desman
Desman is console HTTP API requests tool. Desman uses .yml files to save request information. You can use enviroment files wich are also .yml files, to substitute variables to request.

## Installation
### Pip
```sh
pip install desman
```

### Docker on Unix-like
Desman can be installed as .sh script running docker image:
```
sudo curl -L --fail https://raw.githubusercontent.com/kirillsulim/desman/master/scripts/run/run.sh -o /usr/local/bin/desman
sudo chmod +x /usr/local/bin/desman
```

Default tag in script is latest. If you want to fix specific version, change corresponding variable in script.

### Docken on Windows
Desman can be installed as .ps1 script running docker image. 
[Download script](https://raw.githubusercontent.com/kirillsulim/desman/master/scripts/run/run.ps1) and set required permissions.
Default tag in script is latest. If you want to fix specific version, change corresponding variable in script.

## How to use
### Simple request
Create .yml file with request description:
```yml
method: get
url: http://host.com/
```

then pass file path to desman
```sh
desman path/to/file.yml
```

and desman prints the body of response to console.

### Request with parameters
Query parameters can be passed in url
```yml
method: get
url: http://host.com/?param=value
```
or be passed separately
```yml
method: get
url: http://host.com/
params:
  param: value
```

### Headers
Headers can be passed in headers field
```yml
method: get
url: http://host.com/
headers:
  Authorization: Bearer some-auth-token
params:
  param: value
```

### Body
Body content can be passed in body field in request file
```yml
method: post
url: http://host.com/post
headers:
  Authorization: Bearer some-auth-token
body: |
  {
      "stringField": "JSON value",
      "nestedObject": {
          "nestedField": [1, 2, 3]
      }
  }
```

## Output parameters
The output of HTTP response is controlled by these optional paramters:
- `-s` print status of response
- `-H` print heafers of response
- `-b` print body of response

If none of these parameters are passed desman prints only body of response.

## Using environments
All request files are [Jinja2](http://jinja.pocoo.org/) templates.

```yml
# request.yml
method: post
url: http://{{server.host}}:{{server.port}}/post
headers:
  Authorization: Bearer {{my-token}}
body: |
  {
      "stringField": "JSON value",
      "nestedObject": {
          "nestedField": [1, 2, 3]
      }
  }
```

Variables are substituted from enviroment .yml files

```yml
# env.yml
server:
  host: host.com
  port: 8080
my-token: "some-auth-token"
```

which are passed in optional parameter `-e`

```sh
desman -e env.yml request.yml
```

You can use many enviroment files. If they have similar fields desman will use the last occurence of value.

With many enviroment files

```yml
# env.yml
server:
  host: host.com
  port: 8080
my-token: "some-auth-token"
```

```yml
# new-token.yml
my-token: "new-token"
```

if both passed as

```sh
desman -e env.yml -e new-token.yml request.yml
```

request will be performed with `Authorization: Bearer new-token` header.
