from skpy import Skype
sk = Skype("username", "password") # connect to Skype

sk.user # you
sk.contacts # your contacts
sk.chats # your conversations
contact = sk.contacts[""]  # receiver id 
contact.chat.sendMsg("User auto create bash script")# message
contact.chat.sendFile(open("/home/sysadmin/lab/bash/userauto.sh", "rb"), "user_create")# file upload
