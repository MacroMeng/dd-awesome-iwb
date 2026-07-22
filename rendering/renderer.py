import os
import reprlib
import traceback
from collections import defaultdict
from io import StringIO
import json
from time import perf_counter as counter
import logging

import templates as t


log = logging.getLogger()


def render_quicklook_type(data: dict, type_: str) -> str:
    projects: list[dict[str, str]] = data['content'][type_]
    type_res = t.QUICKLOOK_HEAD.format(
        title=next(tp['name'] for tp in data['types'] if tp['id'] == type_)
    )
    proj_res = StringIO()

    for project in projects:
        if 'stopped_updating' in project.get('tags', ()):
            _tag = '![停更](https://img.shields.io/badge/%E5%81%9C%E6%9B%B4-%23b91c1c?style=flat&label=)'
        elif 'closed_source' in project.get('tags', ()):
            _tag = next(tag['display'] for tag in data['tags'] if tag['id'] == 'closed_source')
        else:
            _tag = (f'![GitHub Commit Activity]'
                    f'(https://img.shields.io/github/commit-activity/y/'
                    f'{project["developer_gh"]}/{project["repo_gh"]}?label=)')

        proj_res.write(
            t.QUICKLOOK_LN.format(
                rank=project.get('rank', ''),
                name_decorator='~~'
                if 'stopped_updating' in project.get('tags', ())
                else '',
                name=project['name'],
                normalized_name='-'.join(project['name'].lower().split()),
                tags=_tag,
                developer_gh=project.get('developer_gh', ''),
                developer=project.get('developer', ''),
            )
        )

    return type_res + proj_res.getvalue()


def render_quicklook() -> str:
    content_buf = StringIO()
    with open('./source/ranks.json', 'r', encoding='utf-8') as f:
        ranks_data = json.load(f)
        log.debug(f'Loaded ranks_data: {reprlib.repr(ranks_data)}')

    for k in ranks_data['content']:
        log.debug(f'Rendering quicklook type: {k} from data {str(ranks_data)[:50]}...')
        content_buf.write(render_quicklook_type(ranks_data, k))

    return t.QUICKLOOK.format(content=content_buf.getvalue())


def render_field(data: dict, name: str) -> str:
    content_buf = StringIO()
    field_projs = [defaultdict(lambda: '', proj) for proj in data['content'][name]]

    for proj in field_projs:
        proj_tags = '\n'.join(tag['display'] for tag in data['tags'] if tag['id'] in proj.get('tags', ()))
        qq_display = ''.join(f'[![加入 QQ 群](https://img.shields.io/badge/-%E4%BA%A4%E6%B5%81%E7%BE%A4%20{qq["qq_num"]}-white?style=flat&logo=qq)]({qq["qq_link"]})'
                      for qq in proj['qq_group'])

        content_buf.write(t.Project.full(
            logo=proj['logo'],
            name=proj['name'],
            banner=proj['banner'],
            gen_tags=proj_tags,
            github=proj['github'],
            qq_chat=qq_display,
            description=proj['description'],
            kws=proj['keywords'],
            cmts={cmt['commenter']: cmt['content'] for cmt in proj.get('comments', [])},
            links=proj['links'],
        ))
        
    return content_buf.getvalue()


def render():
    log.debug('Rendering HOME -> README.tmp.md')
    with open('./README.tmp.md', 'w', encoding='utf-8') as f:
        f.write(t.HOME)
    log.debug('Completed Rendering HOME.')

    log.debug('Rendering quicklook.md -> ./docs/quicklook.md')
    with open('./docs/quicklook.md', 'w', encoding='utf-8') as f:
        f.write(render_quicklook())
    log.debug('Completed Rendering quicklook.md.')

    mainbody_md = list(set(os.listdir('./docs/')) - {'aiwbtoday.md', 'quicklook.md'})
    log.debug(f'Rendering main body: {mainbody_md}')
    with open('./source/full.json', 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    for fn in mainbody_md:
        with open(f'./docs/{fn}', 'w', encoding='utf-8') as f:
            f.write(render_field(full_data, os.path.splitext(os.path.basename(fn))[0]))
        log.debug(f'Completed Rendering {fn}.')
    log.debug('Completed Rendering main body.')


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(filename)s:%(lineno)d@%(asctime)s] %(levelname)s: %(message)s', level=logging.DEBUG
    )

    log.info(f'>>> Rendering Start at {counter()}')
    t0 = counter()
    try:
        render()
    except Exception as e:
        log.critical(f'!!! Rendering Failed: ({e.__class__.__qualname__}){e}')
        raise RuntimeError(f'Render Failed: {e}') from e
    log.info(f'>>> Completed Rendering in {counter() - t0:.3f} seconds')
