extern "C" {
const CLAP_EXPORT struct clap_plugin_entry clap_entry = {
	CLAP_VERSION,
	clap_init_guard,
	clap_deinit_guard,
	clap_get_factory
}
}
