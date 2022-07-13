from turtle import title

from django.db.models import CharField, Model, TextField


class Skill(Model):
    title = CharField(max_length=50, unique=True)
    description = TextField()

    def __repr__(self) -> str:
        return f"<Skill: title - {self.title}>"
