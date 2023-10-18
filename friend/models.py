from django_fsm import FSMField, transition
from django.db import models
from django.contrib.auth.models import User

status = [
    ('send', 'SEND'),
    ('accept', 'ACCEPT'),
    ('reject', 'REJECT'),
]


class Friend(models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    # status = models.CharField(max_length=6, choices=status)
    state = FSMField(default='send', choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.from_user.email

    @transition(field=state, source='send', target='accept')
    def accept(self):
        pass

    @transition(field=state, source='send', target='reject')
    def reject(self):
        pass
