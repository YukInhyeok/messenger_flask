from app import db

class Chat(db.Model):
    __tablename__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    chat_id = db.Column(db.Integer)
    content = db.Column(db.String)
    img_src = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, name, chat_id, content, img_src):
        self.name = name
        self.chat_id = chat_id
        self.content = content
        self.img_src = img_src

    def __repr__(self):
        return f"<Chat {self.id}>"
