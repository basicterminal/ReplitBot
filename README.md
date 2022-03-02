# Replit Bot
Very USEFUL Replit API Wrapper that can `fetch repl` content, like creation date, views, filenames and more. All using `connect.sid` which is easily accessible.

## Docs
### Login
Very simple to do, simply follow the instructions. 
```
Cookies > Connect.Sid > Value
```
```py
bot = replbot(
      connect_sid = "CONNECT.SID HERE"
).login()
```
### Fetch Replit
```py
print(bot.fetch_repl(
    author_name      = "OWNER USERNAME"
    author_repl_name = "OWNER REPL NAME"
))
```
