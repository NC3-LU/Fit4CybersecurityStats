## Presentation

[![License](https://img.shields.io/github/license/CASES-LU/Fit4CybersecurityStats.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0.html)

Agglomerates stats of several
[Fit4Cybersecurity](https://github.com/CASES-LU/Fit4Cybersecurity) instances.


## Installation


```bash
$ make install
```

## Configuration

You can create your own configuration file and write it in the folder ```instance```.
If that is the case you must export its name in an environment variable:

```bash
export APP_CONFIG="config.py"
```


## Generate HTML (static)

```bash
$ make html output=index.html
```

HTML template is located in ```fit4cybersecuritystats/templates/html```.


## Generate Markdown (static)

```bash
$ make markdown
```

Markdown template is located in ```fit4cybersecuritystats/templates/markdown```.


## Launch the web server (dynamic)

```bash
$ make runserver
```

HTML template is located in ```fit4cybersecuritystats/templates/web```.


## Deploy to Heroku

With this button:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/CASES-LU/Fit4CybersecurityStats)

And voilà !


## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)

Copyright (C) 2022 SECURITYMADEIN.LU
