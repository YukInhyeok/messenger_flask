'''
플라스크 앱을 이용한 메신저 서비스 만들기

- 디자인 모델 제공. 커스터마이징은 자유롭게 가능. 디자인 모델 => https://coconuttalk-sample.netlify.app/
- 만들어야 할 페이지는 총 네개 => 로그인(/), 친구목록(/friends), 채팅목록(/chats), 채팅방(/chat)
- 데이터 테이블은 단 하나만 요구됨 => 채탱 내용(말풍선 관리)
- 로그인, 친구 관리, 실제 채팅 등의 서비스 기능은 구현하지 않는다 (오직 웹페이지 껍데기만)
- 친구 목록과 채팅 목록 페이지의 항목은 구색을 맞추는 선에서 자유롭게
'''

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    from models import Chat

    from views import pororo
    app.register_blueprint(pororo, url_prefix='/pororo')

    return app
