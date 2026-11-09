import gettext

appname = "hello"
localedir = "locales"

translations = gettext.translation(appname, localedir, fallback=False)
translations.install()

print(_("Hello World"))
