# Config file for firefox ui tests run via TaskCluster.


config = {
    "vcs_share_base": "/builds/hg-shared",

    "find_links": [
        "http://pypi.pub.build.mozilla.org/pub",
    ],
    "pip_index": False,

    "download_minidump_stackwalk": True,
    "tooltool_cache": "/builds/worker/tooltool-cache",
}
