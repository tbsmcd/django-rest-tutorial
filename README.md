# django-rest-tutorial

## 起動

```bash
% docker-compose up
```

## プロジェクト作成

```bash
% docker-compose run web django-admin startproject tutorial .                                                                                               1 ↵ ✖ ✹
WARNING: Found orphan containers (django-rest-tutorial_check_1) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
Creating django-rest-tutorial_web_run ... done
2022/03/14 06:37:37 Waiting for: tcp://db:3306
2022/03/14 06:37:37 Connected to tcp://db:3306
2022/03/14 06:37:38 Command finished successfully.
```

```bash
% docker-compose run web python manage.py startapp snippets                                                                                                   1 ↵ ✖
WARNING: Found orphan containers (django-rest-tutorial_check_1) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
Creating django-rest-tutorial_web_run ... done
2022/03/14 06:49:06 Waiting for: tcp://db:3306
2022/03/14 06:49:06 Connected to tcp://db:3306
2022/03/14 06:49:06 Command finished successfully.
```

## アクセス

- Web http://localhost:8002 
- PhpMyAdmin http://localhost:8080 

## Tips

DB が起動する前に Web が起動するとエラーが発生する。それを防止するために https://github.com/tbsmcd/django-rest-tutorial/blob/1d4d5b2d91b0c56250a92d4cfd4f4c139acbb7d1/docker-compose.yml#L32 を追加している。 