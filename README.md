# django-rest-tutorial

## 起動

```bash
% docker-compose up
```

## アクセス

- Web http://localhost:8002 
- PhpMyAdmin http://localhost:8080 

## Tips

DB が起動する前に Web が起動するとエラーが発生する。それを防止するために https://github.com/tbsmcd/django-rest-tutorial/blob/1d4d5b2d91b0c56250a92d4cfd4f4c139acbb7d1/docker-compose.yml#L32 を追加している。 