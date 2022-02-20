# Flask modules
from flask_assets import Environment, Bundle

# App modules
from app import app

assets = Environment(app)
assets.register({
	'layout_css': Bundle(
		'assets/css/layouts/layout.css',
		'assets/css/components/header.css',
		'assets/css/components/input.css',
		'assets/css/essentials/fonts.css',
		filters='libsass',
		output='css/layouts/layout.css'
	),
	'index_css': Bundle(
		'assets/css/index.css',
		filters='libsass',
		output='css/index.css'
	),
	'header_js': Bundle(
		'assets/js/header.js',
		filters='jsmin',
		output='js/header.js'
	),
	'submit_js': Bundle(
		'assets/js/submit.js',
		filters='jsmin',
		output='js/submit.js'
	),
	'jquery_lib': Bundle(
		'assets/js/lib/jquery.js',
		filters='jsmin',
		output='js/lib/jquery.js'
	)
})