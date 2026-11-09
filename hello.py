import gettext

appname = "hello"
localedir = "locales"

gettext.install(appname, localedir)

print(_("Hello World"))
