from dataclasses import dataclass
from io import StringIO


HOME = """\
<div align="center">

<img width="156" src="./images/aiwb-icon.png">

<h1>
<picture>
      <source media="(prefers-color-scheme: dark)" srcset="./images/fontlogo/aiwb-font-white.png">
      <img alt="aiwb-logo" src="./images/fontlogo/aiwb-font-dark.png" height="28">
    </picture>
</h1>

专为广大中小学电教打造的班级希沃/鸿合等<br/>一体机/数字白板/班班通一站式软件推荐清单<br/>和实用知识手册，助你在新学期快速上手<br/>班级一体机新玩法！
<br/>**为广大电教倾情撰写，让班级大屏更好用！**

**🌟 风带来故事的种子，时间使之发芽 🌟**

<a href="./CONTRIBUTING.md">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./images/navigation/贡献指南-白.svg">
      <img alt="贡献指南" src="./images/navigation/贡献指南-黑.svg" height="52">
    </picture>
</a>&nbsp;
<a href="https://github.com/awesome-iwb/awesome-iwb/issues/57">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./images/navigation/最新项目-白.svg">
      <img alt="最新项目" src="./images/navigation/最新项目-黑.svg" height="52">
    </picture>
</a>&nbsp;
<img alt="分隔符" height="52" src="./images/navigation/分隔符.svg">&nbsp;
<a href="#%EF%B8%8F-屏幕批注与白板软件">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./images/navigation/白板软件-白.svg">
      <img alt="白板软件" src="./images/navigation/白板软件-黑.svg" height="52">
    </picture>
</a>&nbsp;
<a href="#-课表与看板类软件">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./images/navigation/课表看板-白.svg">
      <img alt="课表看板" src="./images/navigation/课表看板-黑.svg" height="52">
    </picture>
</a>&nbsp;
<a href="#%EF%B8%8F-辅助类软件与实用工具">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./images/navigation/工具辅助-白.svg">
      <img alt="工具辅助" src="./images/navigation/工具辅助-黑.svg" height="52">
    </picture>
</a>&nbsp;

<br/>
<br/>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0)
![Maintenance](https://img.shields.io/badge/Maintained%3F-YES-green.svg)<br/>
![GitHub last commit](https://img.shields.io/github/last-commit/awesome-iwb/awesome-iwb)
![Visitors](https://api.visitorbadge.io/api/combined?path=https://github.com/awesome-iwb/awesome-iwb&label=Visitors&countColor=%23263759&style=flat)
![Lastest Update](https://img.shields.io/badge/%E6%9C%80%E5%90%8E%E6%9B%B4%E6%96%B0-2026%E5%B9%B46%E6%9C%887%E6%97%A5-orange)
[![交流群](https://img.shields.io/badge/-%E4%BA%A4%E6%B5%81%E7%BE%A4%20995186133-white?style=flat&logo=qq)](https://qm.qq.com/q/gro00q2v8A)
![Repobeats Analyzer](https://repobeats.axiom.co/api/embed/e21726d2782bb081ef5d8f89360f1ed0d93af4ef.svg "Repobeats analytics image")

</div>

> [!note]
> 诚邀各位开发者加入 Awesome Iwb 的交流群。如果你的项目在 Awesome Iwb 上面上榜了，请加入开发者交流群：995186133。

> [!note]
> Awesome Iwb 官网已推出，关于本readme的问题将不再受理，后续将会使用自动化工具生成新版readme，敬请期待！如需提交项目请登录我们的官网：https://aiwb.smart-teach.cn

---

## ⚠️ 注意

> [!IMPORTANT]
> 在使用任何软件之前，应仔细阅读其仓库中的 README 或其他形式的说明。本文档旨在推荐以下优质软件，尽可能详细展现其功能，如欲提出问题，请前往对应开源仓库/交流平台。

> [!WARNING]
> 以下软件均为免费或非买断制，如遇收费提示请注意甄别是否为盗版软件！

## 速览

[![Quicklook Page goto](./rendering/images/quicklook.svg)](./docs/quicklook.md)

## ✏️ 屏幕批注与白板软件

[![notation_and_whiteboard goto](./rendering/images/notation_and_whiteboard.svg)](./docs/notation_and_whiteboard.md)

## 🗓️ 课表与看板类软件

[![timetable_and_dashboard goto](./rendering/images/timetable_and_dashboard.svg)](./docs/timetable_and_dashboard.md)

## 🛠️ 辅助类软件与实用工具

[![utilities_and_tools goto](./rendering/images/utilities_and_tools.svg)](./docs/utilities_and_tools.md)

## ℹ️ 关于项目

[![about goto](./rendering/images/about.svg)](./docs/about.md)

## 🙏 贡献者和特别感谢

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/2-2-3-trimethylpentane"><img src="https://avatars.githubusercontent.com/u/141403762?v=4?s=100" width="100px;" alt="2,2,3-三甲基戊烷"/><br /><sub><b>2,2,3-三甲基戊烷</b></sub></a><br /><a href="#content-2-2-3-trimethylpentane" title="Content">🖋</a> <a href="#data-2-2-3-trimethylpentane" title="Data">🔣</a> <a href="#doc-2-2-3-trimethylpentane" title="Documentation">📖</a> <a href="#ideas-2-2-3-trimethylpentane" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-2-2-3-trimethylpentane" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/wwiinnddyy"><img src="https://avatars.githubusercontent.com/u/170236045?v=4?s=100" width="100px;" alt="lincube"/><br /><sub><b>lincube</b></sub></a><br /><a href="#ideas-wwiinnddyy" title="Ideas, Planning, & Feedback">🤔</a> <a href="#tool-wwiinnddyy" title="Tools">🔧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Aris-Offline"><img src="https://avatars.githubusercontent.com/u/65645068?v=4?s=100" width="100px;" alt="Aris"/><br /><sub><b>Aris</b></sub></a><br /><a href="#content-Aris-Offline" title="Content">🖋</a> <a href="#data-Aris-Offline" title="Data">🔣</a> <a href="#doc-Aris-Offline" title="Documentation">📖</a> <a href="#maintenance-Aris-Offline" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://lipoly.ink"><img src="https://avatars.githubusercontent.com/u/110595296?v=4?s=100" width="100px;" alt="LiPolymer"/><br /><sub><b>LiPolymer</b></sub></a><br /><a href="#content-LiPolymer" title="Content">🖋</a> <a href="#data-LiPolymer" title="Data">🔣</a> <a href="#doc-LiPolymer" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/unDefFtr"><img src="https://avatars.githubusercontent.com/u/83688818?v=4?s=100" width="100px;" alt="谭麒峰"/><br /><sub><b>谭麒峰</b></sub></a><br /><a href="#content-unDefFtr" title="Content">🖋</a> <a href="#data-unDefFtr" title="Data">🔣</a> <a href="#doc-unDefFtr" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://blog.typed-sigterm.me/"><img src="https://avatars.githubusercontent.com/u/145281501?v=4?s=100" width="100px;" alt="Typed SIGTERM"/><br /><sub><b>Typed SIGTERM</b></sub></a><br /><a href="#content-typed-sigterm" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Jursin"><img src="https://avatars.githubusercontent.com/u/127487914?v=4?s=100" width="100px;" alt="Jursin"/><br /><sub><b>Jursin</b></sub></a><br /><a href="#doc-Jursin" title="Documentation">📖</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.rzly.net"><img src="https://avatars.githubusercontent.com/u/60139353?v=4?s=100" width="100px;" alt="IUU6"/><br /><sub><b>IUU6</b></sub></a><br /><a href="#content-iuu6" title="Content">🖋</a> <a href="#doc-iuu6" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/DryIce-cc"><img src="https://avatars.githubusercontent.com/u/165131008?v=4?s=100" width="100px;" alt="干冰DryIce"/><br /><sub><b>干冰DryIce</b></sub></a><br /><a href="#doc-DryIce-cc" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/alovelydoge"><img src="https://avatars.githubusercontent.com/u/156295679?v=4?s=100" width="100px;" alt="alovelydoge"/><br /><sub><b>alovelydoge</b></sub></a><br /><a href="#doc-alovelydoge" title="Documentation">📖</a> <a href="#bug-alovelydoge" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/makitoid"><img src="https://avatars.githubusercontent.com/u/123004192?v=4?s=100" width="100px;" alt="SJB.w"/><br /><sub><b>SJB.w</b></sub></a><br /><a href="#doc-Makitoid" title="Documentation">📖</a> <a href="#bug-Makitoid" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://wuyuan.dev"><img src="https://avatars.githubusercontent.com/u/88357633?v=4?s=100" width="100px;" alt="孙悟元"/><br /><sub><b>孙悟元</b></sub></a><br /><a href="#doc-SunWuyuan" title="Documentation">📖</a> <a href="#bug-SunWuyuan" title="Bug reports">🐛</a> <a href="#content-SunWuyuan" title="Content">🖋</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

以及一切帮助我们完善资料和文档的贡献者们。同时还得感谢所有 Awesome-Iwb 中列出的开发者们，正是你们，为教学一体机的软件生态做出了巨大贡献。

## Copyright

© Copyright 2025-2026 智教联盟SmartTeachCN"""


@dataclass
class Project:
    """为项目生成 Readme 文本的类"""

    header = """\
<img src={logo} width="56" height="56"/>

### {name}

![banner]({banner})
"""
    badges = """\
{gen_tags}
[![stars](https://img.shields.io/github/stars/{github}?style=flat&color=red)](https://github.com/{github}/stargazers)
[![forks](https://img.shields.io/github/forks/{github}?style=flat&color=blue)](https://github.com/{github}/forks)
[![Watchers](https://img.shields.io/github/watchers/{github}?style=flat&color=green)](https://github.com/{github}/watchers)
[![Downloads](https://img.shields.io/github/downloads/{github}/total?style=flat&logo=github)](https://github.com/{github}/releases)<br/>
[![GitHub Issues](https://img.shields.io/github/issues-search/{github}?query=is%3Aopen&label=issues&color=purple)](https://github.com/{github}/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/{github}?style=flat)](https://github.com/{github}/discussions)
[![Created At](https://img.shields.io/github/created-at/{github})](https://github.com/{github})
[![GitHub Last Commit](https://img.shields.io/github/last-commit/{github})](https://github.com/{github}/commits/master)<br/>
[![GitHub Language Count](https://img.shields.io/github/languages/count/{github})](https://github.com/{github})
[![GitHub Top Language](https://img.shields.io/github/languages/top/{github})](https://github.com/{github})
![GitHub License](https://img.shields.io/github/license/{github}?color=red)
{qq_chat}
"""
    description = '{description}'

    @property
    def keywords(self):
        return '\n'.join(
            f'![{keyword}](https://img.shields.io/badge/{keyword}-white)'
            for keyword in self._kws
        )

    @keywords.setter
    def keywords(self, value: list[str]):
        self._kws = value

    @property
    def comments(self):
        return '\n\n'.join(f'💬 **{k} 锐评**：{v}' for k, v in self._cmts.items())

    @comments.setter
    def comments(self, value: dict[str, str]):
        self._cmts = value

    @property
    def links(self):
        return """\
<table>
{}
</table>
""".format(
            '\n'.join(
                f"""<tr>
    <td><img src="{self._links["display_logo"]}" width="18" height="18"></td>
    <td><b>{self._links["display_source"]}</b></td>
    <td><a href="{self._links["url"]}">{self._links["display_link"]}</a></td>
</tr>"""
            )
        )

    @links.setter
    def links(self, value: dict[str, str]):
        self._links = value

    @property
    def full(self):
        res = StringIO()

        for s in (
            self.header,
            self.badges,
            self.description,
            self.keywords,
            self.comments,
            self.links,
        ):
            res.write(s)

        return res.read()


QUICKLOOK_LN = """\
| {rank} {name_decorator}[{name}](#{normalized_name}){name_decorator} {tags} | <picture><source media="(prefers-color-scheme: dark)" srcset="https://images.weserv.nl/?url=github.com/{developer}.png?v=4&h=64&w=64&fit=cover&mask=circle&maxage=7d&bg=222"><img src="https://images.weserv.nl/?url=github.com/{developer}.png?v=4&h=64&w=64&fit=cover&mask=circle&maxage=7d&bg=fff" width="20" height="20"/></picture>&nbsp;<a href="https://github.com/{developer}">{developer}</a> |
"""

QUICKLOOK = """\
## 📚 速览

- 🥇 是指最推荐使用的、必装软件推荐，每个类别下至少有一个被标记的软件或项目。

- 🥈 是指推荐尝试体验的，功能基本完善的软件。基本上这些被标注的项目大多比被 🥇 标注的项目稍微逊色一些或体验略微欠缺一些，但依旧做得很不错。

- 🌟 是指那些目前看来发展不怎么样的，但前景远大的软件或项目。

- 🔴 是指最近几天内收录的新软件或新项目。

{content}
"""

ABOUT = """\

## 🌟 Stars 历史图表

<div align="center">

[![Star 历史](https://starchart.cc/Awesome-Iwb/Awesome-Iwb.svg?variant=adaptive)](https://starchart.cc/Awesome-Iwb/Awesome-Iwb/stargazers)

**如果这个项目对您有帮助，请点亮 Star ⭐！**

</div>


## 📄 协议

<p xmlns:cc="http://creativecommons.org/ns#" >本作品已获得 <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0 许可<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

## 💗 友情链接

{friend_links}

## 🔗 相关链接

{related_links}

## 👋 同类项目推荐

{similar_projects}
"""
