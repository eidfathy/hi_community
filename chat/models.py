
from django.db import models
from accounts.models import User, UserProfile, PlacesProfile
from django.db.models import Max

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages_sent')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages_received')
    body = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    @staticmethod
    def send_message(from_user, to_user, body):
        sender_message = Message(
            user=from_user,
            sender=from_user,
            recipient=to_user,
            body=body,
            is_read=True
        )
        sender_message.save()

        recipient_message = Message(
            user=to_user,
            sender=from_user,
            body=body,
            recipient=from_user,
        )
        recipient_message.save()
        return sender_message

    @staticmethod
    def get_messages(user):
        messages = Message.objects.filter(user=user).values('recipient').annotate(last=models.Max('date')).order_by('-last')
        users = []
        for message in messages:
            users.append({
                'user': User.objects.get(pk=message['recipient']),
                'last': message['last'],
                'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
            })
        return users




