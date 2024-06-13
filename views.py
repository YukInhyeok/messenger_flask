'''
플라스크 앱을 이용한 메신저 서비스 만들기

- 디자인 모델 제공. 커스터마이징은 자유롭게 가능. 디자인 모델 => https://pororonuttalk-sample.netlify.app/
- 만들어야 할 페이지는 총 네개 => 로그인(/), 친구목록(/friends), 채팅목록(/chats), 채팅방(/chat)
- 데이터 테이블은 단 하나만 요구됨 => 채탱 내용(말풍선 관리)
- 로그인, 친구 관리, 실제 채팅 등의 서비스 기능은 구현하지 않는다 (오직 웹페이지 껍데기만)
- 친구 목록과 채팅 목록 페이지의 항목은 구색을 맞추는 선에서 자유롭게
'''

import requests
from flask import Blueprint, render_template, request
from models import Chat
from flask import jsonify

pororo = Blueprint(
    "pororo",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@pororo.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@pororo.route('/friends', methods=['GET'])
def friends():
    return render_template('friends.html')


@pororo.route('/chats', methods=['GET'])
def chats():
    from sqlalchemy import desc
    from app import db
    chats = db.session.query(Chat.chat_id, Chat.name, Chat.content).group_by(Chat.chat_id).order_by(
        desc(Chat.created_at)).all()
    return render_template('chats.html', chats=chats)


@pororo.route('/chat/<int:chat_id>', methods=['GET'])
def chat(chat_id):
    from app import db
    chat = db.session.query(Chat.name).filter(Chat.chat_id == chat_id, Chat.name.isnot(None))
    return render_template('chat.html', chat_id=chat_id, chat=chat)


@pororo.route('/send_message', methods=['POST'])
def send_message():
    from app import db
    chat_id = request.form.get('chat_id')  # 채팅방 ID를 받습니다.
    content = request.form.get('content')
    name = request.form.get('name')
    img_src = request.form.get('img_src')
    new_message = Chat(chat_id=chat_id, content=content, name=name, img_src=img_src)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'success'}), 200


@pororo.route('/get_messages/<int:chat_id>', methods=['GET'])
def get_messages(chat_id):
    messages = Chat.query.filter_by(chat_id=chat_id).all()  # 채팅방 ID에 해당하는 메시지만 가져옵니다.
    return jsonify({'messages': [message.content for message in messages]}), 200

@pororo.route('/get_profile/<int:chat_id>', methods=['GET'])
def get_profile(chat_id):
    from app import db
    chat = db.session.query(Chat.img_src).filter(Chat.chat_id == chat_id, Chat.img_src.isnot(None)).first()
    if chat is not None:
        chat = {'img_src': chat.img_src}
    return jsonify({'chat': chat}), 200
