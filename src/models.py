__author__ = 'ubuntu'

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
'''
The classes found in this file are the model classes.
The "Mails" class defines the structure of an e-mail object.
The "Inbox" class defines which information about an account are needed.
The "Contacts" class is used to store contact objects in the model.
'''


class Mails(Base):
    __tablename__ = 'mails'

    id = Column(Integer, primary_key=True)
    remoteID = Column(String(255))
    date = Column(String(255))  #TODO: We should use the internal sqlite date type
    subject = Column(String(255), index=True)
    _from = Column(String(255))
    to = Column(String(255))
    cc = Column(Text)
    bcc = Column(Text)
    inReplyTo = Column(String(255), index=True)
    message = Column(String(255), index=True)
    read = Column(Integer())
    inboxId = Column(Integer, ForeignKey('inboxes.id'))


class Inbox(Base):
    __tablename__ = 'inboxes'

    # regular mail communication stuff
    id = Column(Integer, primary_key=True)
    userMail = Column(String(255))
    account = Column(String(255))
    password = Column(String(255), index=True)

    firstName = Column(String(255))
    lastName = Column(String(255))

    imapServer = Column(String(255))
    smtpServer = Column(String(255))

    imapPort = Column(String(255))
    smtpPort = Column(String(255))

    imapSSL = Column(Integer())
    smtpSSL = Column(Integer())

    smtpAuth = Column(Integer())

    # settings
    nbr_mails = Column(Integer())
    nbr_addresses = Column(Integer())
    colourblind_mode = Column(Integer())
    font_size = Column(Integer())

    caches = relationship("Mails")


#simply add a class like this?
class Contacts(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    emailAddress = Column(String(255))
    picture = Column(String(255))