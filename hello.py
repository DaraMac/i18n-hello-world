import gettext

gettext.install(domain="hello", localedir="locales")

print(_("Hello World"))
