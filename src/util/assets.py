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
	'index_css': Bundle(
		'assets/css/components/index.css',
		filters='cssmin',
		output='tmp/src/landing.css'
	)
}