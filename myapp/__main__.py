from .app import db

db.create_all()

from datetime import datetime
from .api.models import Post

current_date = datetime.today().date()
new_post = Post(
    title="A new morning", description="A new morning details", created_at=current_date
)
db.session.add(new_post)
db.session.commit()
