from flask_assets import Bundle

bundles = {
	'base_js': Bundle(
		'js/lib/jquery.min-3.6.0.js',
		'js/lib/bootstrap.min-5.1.0.js',
		filters='jsmin',
		output='tmp/base-cdi.js'
	),
	'base_css': Bundle(
		'css/lib/bootstrap.min-5.1.0.css',
		filters='cssmin',
		output='tmp/base-cdi.css'
	)
}