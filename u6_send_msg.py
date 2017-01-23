from twilio import rest

account_sid = "AC7e3eaa8be29b45a3e328fa94a9e0b177"
auth_token = "4dbe3804093f711b7262199c5442ac86"
client = rest.TwilioRestClient(account_sid,auth_token)

message = client.sms.messages.create(body="Special Moments .. :) ",
                                        to="+919480042341",
                                     from_="+15138029390")

print message.sid
