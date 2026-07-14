from io import StringIO
import json
from time import perf_counter as counter
import logging

import templates as t


def render_quicklook_type(data: dict, type_: str) -> str:
    projects: list[dict[str, str]] = data["content"][type_]
    type_res = StringIO(t.QUICKLOOK_HEAD.format(
        title=next(tp["name"] for tp in data if tp["id"] == type_)
    ))

    for project in projects:
        pass  # TODO: COMPLETE THIS


def render_quicklook() -> str:
    content_buf = StringIO()
    with open("./source/ranks.json", "r", encoding="utf-8") as f:
        ranks_data = json.load(f)

    for k in ranks_data["content"]:
        content_buf.write(render_quicklook_type(ranks_data, k))


def render():
    with open("./README.tmp.md", "w", encoding="utf-8") as f:
        f.write(t.HOME)

    with open("./quicklook.md", "w", encoding="utf-8") as f:
        f.write(render_quicklook())


if __name__ == "__main__":
    log = logging.getLogger()
    logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s",
                        level=logging.DEBUG)

    t0 = counter()
    render()
    log.info(f"Completed Rendering in {counter() - t0:.3f} seconds")
