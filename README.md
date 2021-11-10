# FastAPI SocialLogin(GOOGLE)

fastapiの場合appのmount機能を提供しているので今作っているアプリケーションと今後作るアプリケーションにも使うためにGoogle OAuth2を使ってAuthentication機能を提供するappを作ってみました。



まず、SocialLogin機能を提供する3rd party libraryがあるか探してみた結果、

[FastAPI Users](https://github.com/fastapi-users)

を見つけた。しかし、このlibraryはbackendへのredirectが必要でcustomする必要があったため候補から消した。

他にないか探してみたけど検索力がなさすぎて出てこなかった。

結果、自分で作ることにした。



まず、イメージ的にはgoogle loginからredirectで`id_token`と`access_token`をもらってuserのprofile情報を持ってきてそれをもとにすでに登録されているユーザーであればloginを、そうでなければregister後loginをして最終的にはjwtを使って`access_token`と`refresh_token`を持ってCookieに保存させるlogin機能を作った。



### Image

![flow](https://tva1.sinaimg.cn/large/008i3skNgy1gw9u308ln9j30e70alt8x.jpg)

### Usage

```shell
# requirements
fastapi-jwt-auth
fastapi
tortoise
pydantic
google-auth
aiohttp
```



__in main app__

```python
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from oauth.main import app as oauth_app # this app

app = FastAPI()
app.mount("/auth", oauth_app)

register_tortoise(
    app,
    db_url='sqlite://test.sqlite3',
    modules={"models": ["oauth.models.user"]},
    generate_schemas=True,
    add_exception_handlers=True
)
```

