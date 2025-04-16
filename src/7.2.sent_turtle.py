"""
This module contains a PostOffice class that allows users to send and receive messages.
It supports features such as sending messages, reading unread messages, and searching for words in the inbox.
"""

class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title , message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        try:
            user_box = self.boxes[recipient]
        except KeyError as e:
            raise KeyError("Recipient does not exist.") from e
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'unread': True,
            'title': message_title,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name , n = 0):
        try:
            user_box = self.boxes[user_name]
        except KeyError as exc:
            raise KeyError("User not found") from exc
    
        n = len(user_box) if n == 0 else n
        message_number = min(len(user_box), n)
        read_number = 0
        read_messages = []
        while read_number < message_number:
            if user_box[read_number].get('unread'):
                read_messages.append(user_box[read_number])
                user_box[read_number]['unread'] = False
                read_number += 1
            else:
                read_number += 1
                message_number += 1
    
        return read_messages

    def search_inbox(self , username , word):
        """
           Searches for a word in the user's inbox messages and returns the matching messages.
           Raises KeyError if the username does not exist.
           """
        try:
            user_box = self.boxes[username]
        except KeyError as e:
            raise KeyError("username does not exist.") from e

        result = []
        for box in user_box:
            if word.lower() in box['body'].lower() or word.lower() in box['title'].lower():
                result.append(box)
        return result
