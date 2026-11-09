import gettext

appname = "hello"
localedir = "./locales"
_ = gettext.gettext

en_i18n = gettext.translation(appname, localedir, fallback=False, languages=["en"])

en_i18n.install()

print(_("Hello World"))



# it = gettext.translation("base", localedir="locales", languages=["it"])
# it.install()
# _ = it.gettext
