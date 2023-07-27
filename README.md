# bp-rss-sema

## Feed RSS

- CE - [rss-sema-ce.xml](https://boopixel.github.io/bp-rss-sema/src/feed/rss-sema-ce.xml)
- RS - [rss-sema-rs.xml](https://boopixel.github.io/bp-rss-sema/src/feed/rss-sema-rs.xml)

## Test

### Docker Build

```shell
docker build --tag rss-sema-ubuntu/dev --file Dockerfile .
docker build --tag rss-sema-arch/dev --file Dockerfile.archlinux .
```

### Docker Run

```shell
docker run -t -v ${PWD}:/opt/ rss-sema-ubuntu/dev
docker run -t -v ${PWD}:/opt/ rss-sema-arch/dev
```

## Commit Style

- ⚙️ FEATURE
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI
- ❤️️ TEST
- ⬆️ CI/CD
- ⚠️ SECURITY

## License

This project is licensed under the terms of the MIT license.
