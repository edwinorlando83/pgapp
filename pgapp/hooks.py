# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pgapp"
app_title = "pgapp"
app_publisher = "orlando"
app_description = "des"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ee"
app_license = "MIT"
app_logo_url = "/files/logo.png"

after_install = "pgapp.setup.after_install"

website_context = {
"favicon": "/assets/pgapp/icon.png",
"splash_image": "/assets/pgapp/logo-gpm-2.png"
}

app_include_css = "/assets/pgapp/css/pgapp.css"
app_logo_url = "/assets/pgapp/logo-gpm-2.png"
brand_html = ' <img src="/assets/pgapp/logo-gpm-2.png"> '
web_include_css = ["/assets/pgapp/css/pgapp.css" ]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pgapp/css/pgapp.css"
# app_include_js = "/assets/pgapp/js/pgapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/pgapp/css/pgapp.css"
# web_include_js = "/assets/pgapp/js/pgapp.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pgapp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pgapp.install.before_install"
# after_install = "pgapp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pgapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pgapp.tasks.all"
# 	],
# 	"daily": [
# 		"pgapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"pgapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pgapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pgapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pgapp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pgapp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pgapp.task.get_dashboard_data"
# }

