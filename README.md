Just practicing on python-semantic-versioning

[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)


## How to use



* Add commit.
```
git commit -am 'fix(toml): Minor'
```


Add breaking change:
```sh
perf(pencil): remove graphiteWidth option

BREAKING CHANGE: The graphiteWidth option has been removed.
The default graphite width of 10mm is always used for performance reasons. 
```

* Run semantic-release tool
```
GH_TOKEN=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 semantic-release version
```

This will create a new tag and will publish a new release (and the tag) on the remote repo.

_Note:_ Should set the GH_TOKEN as env variable.

Test release from GH action.
Second change.
Third change.
Fourth Change.
5
6