# Flask modules
from flask_assets import Environment, Bundle

# App modules
from app import app

assets = Environment(app)
assets.register({
	'layout_css': Bundle(
		'assets/css/layouts/layout.css',
		'assets/css/essentials/fonts.css',
		'assets/css/essentials/colors.css',
		filters='libsass',
		output='cache/css/layouts/layout.css'
	),
	'index_css': Bundle(
		'assets/css/index.css',
		'assets/css/components/input.css',
		filters='libsass',
		output='cache/css/index.css'
	),
	'create_css': Bundle(
		'assets/css/create.css',
		filters='libsass',
		output='cache/css/create.css'
	),
	'view_css': Bundle(
		'assets/css/view.css',
		filters='libsass',
		output='cache/css/view.css'
	),
	'header_css': Bundle(
		'assets/css/components/header.css',
		filters='libsass',
		output='cache/css/components/header.css'
	),
	'header_js': Bundle(
		'assets/js/header.js',
		filters='jsmin',
		output='cache/js/header.js'
	),
	'submit_js': Bundle(
		'assets/js/submit.js',
		filters='jsmin',
		output='cache/js/submit.js'
	),
	'view_js': Bundle(
		'assets/js/view.js',
		filters='jsmin',
		output='cache/js/view.js'
	),
	'jquery_lib': Bundle(
		'assets/js/lib/jquery.js',
		filters='jsmin',
		output='cache/js/lib/jquery.js'
	)
})