class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
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
        except KeyError:
            raise KeyError("Recipient does not exist.")
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'was read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_message(self, username , N = 0):
        """
           Retrieves up to N unread messages from the user's inbox and marks them as read.
           If N is 0, retrieves all unread messages.
           Raises KeyError if the username does not exist.
           """
        try:
            user_box = self.boxes[username]
        except KeyError:
            raise KeyError("username does not exist.")
        result = []
        if N == 0:
            n = len(user_box)
        i = 0
        while i < N and i < len(user_box):
            if not user_box[i].get('was read'):
                result.append(user_box[i])
                user_box[i].update({'was read': True})
                i += 1
            else:
                i += 1
                N += 1
        return result

    def search_inbox(self , username , word):
        """
           Searches for a word in the user's inbox messages and returns the matching messages.
           Raises KeyError if the username does not exist.
           """
        try:
            user_box = self.boxes[username]
        except KeyError:
            raise KeyError("username does not exist.")

        result = []
        for box in user_box:
            if word in box['body']:
                result.append(box)



