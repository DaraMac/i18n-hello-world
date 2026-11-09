import gettext

# user_locale = input("Locale: ").strip()

appname = "hello"
localedir = "./locales"

translations = gettext.translation(appname, localedir, fallback=False)
# translations = gettext.translation(appname, localedir, fallback=False, languages=[user_locale])

translations.install()

print(_("Hello World"))



# it = gettext.translation("base", localedir="locales", languages=["it"])
# it.install()
# _ = it.gettext
