from flask_assets import Bundle

bundles = {
	'base_js': Bundle(
		'assets/js/lib/jquery.min-3.6.0.js',
		'assets/js/lib/bootstrap.min-5.1.0.js',
		filters='jsmin',
		output='tmp/index.js'
	),
	'base_css': Bundle(
		'assets/css/lib/bootstrap.min-5.1.0.css',
		'assets/css/abstracts/fonts.css',
		'assets/css/base.css',
		filters='cssmin',
		output='tmp/index.css'
	),
	'index_js': Bundle(
		'assets/js/components/submit.js',
		filters='cssmin',
		output='tmp/src/index.js'
	),
	'index_css': Bundle(
		'assets/css/components/index.css',
		filters='cssmin',
		output='tmp/src/landing.css'
	),
	'tos_css': Bundle(
		'assets/css/components/terms-of-service.css',
		filters='cssmin',
		output='tmp/src/terms-of-service.css'
	)
}