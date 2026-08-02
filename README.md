# DiscoElysiumPersonalities-Skill-Unified

以《极乐迪斯科》（Disco Elysium）24 人格系统为原型的 AI 对话 Skill。触发后，从 24 个人格中选出 1~2 个最合适的，以"脑内声音"的方式对用户说话（复刻游戏中主角脑内多声部的体验），再以普通助手口吻正常、完整地回答用户的问题。

## 各目录说明

**`SKILL.md`** — Skill 的核心定义文件。包含完整的工作流程（路由 → 判定成功/失败 → 取料 → 输出）、24 人格路由表（按智力/精神/体格/身手四大属性分组）、HTML 对话框模板，以及硬约束规则（风格对话必须用 `<div>` 包裹）。AI 在每次触发时都会按此流程执行。

**`references/`** — 24 个人格的独立资料文件，每人一格。每个文件包含：
- **人格详细介绍**：在原作中的定位、适合的玩家类型、高/低级时的表现
- **参数信息**：`--de-bg`、`--de-text`、`--de-accent` 三个十六进制颜色值，用于生成 HTML 对话框配色
- **语料参考/范例**：分"含成功"和"不含成功"两节，收录游戏内该人格的台词原文，供 AI 模仿语气与措辞

**`assets/`** — 辅助资产：
- `disco-elysium-textbox.html`：四种色系的 HTML 对话框展示，与 SKILL.md 中的模板保持一致，可在浏览器中直接打开预览四个属性组的配色效果
- 两个 `.md` 文件：极乐迪斯科游戏的全部台词（1~400 页），是 classify_personalities.py 的输入源

**`scripts/classify_personalities.py`** — 台词处理脚本。读取游戏台词原始文件，按"四字人格名 — 内容"的格式解析每一行，根据是否含 `【成功】` 标记分节，自动合并进 `references/` 下对应人格文件的对应小节中。用法：

```powershell
python scripts/classify_personalities.py assets/极乐迪斯科-台词-中文版-XXX~XXX页.md
```

**`disco-elysium-personalities.skill`** — Skill 压缩归档文件，包含打包后的完整 Skill 内容。

## 使用

- **启动**：输入 `Disco:on` 或 `Disco on`；启动后默认保持开启，后续对话持续生效
- **关闭**：输入 `Disco:off`
- **新增台词**：将新语料 `.md` 放入 `assets/`，运行 classify_personalities.py 自动分类合并

## 输出范例

用户提问："为什么我的代码总是有 bug？"

Skill 会分析语境，选中 **逻辑思维**（智力/Intellect，从零散证据中编织脉络）作为主导人格、**从容自若**（精神/Psyche，保持镇定掩饰真实情绪）作为副手人格。两个人格以脑内声音的形式跳出来发言，随后以普通助手口吻给出正常回答。

完整输出如下：

<div style="display:block; box-sizing:border-box; position:relative;
            width:100%; max-width:400px; margin:16px auto;
            padding:26px 28px 22px;
            font-family:Georgia,'Songti SC','SimSun',serif; color:#7b857a;
            line-height:1.8; letter-spacing:0.02em; overflow-wrap:break-word;">

  <div style="position:relative; z-index:1; display:flex; align-items:center; gap:10px; margin:0 0 14px;">

  <span style="font-size:10px; color:#3a4a62;">◆</span>
  <span style="font-family:'Source Han Serif SC','Noto Serif CJK SC','Songti SC','SimSun',serif; font-size:19px; font-weight:bold; letter-spacing:0.28em; color:#3a4a62; white-space:nowrap;">逻辑思维</span>

  <span style="position:relative; display:inline-block; white-space:nowrap; font-family:'Source Han Serif SC','Noto Serif CJK SC','Songti SC','SimSun',serif; font-size:13px; letter-spacing:0.12em; padding:5px 12px; color:#3a4a62; background:rgba(58,74,98,0.08);"><span style="position:absolute; left:0; top:0; width:calc(100% - 9px); height:100%; border-top:1px solid #3a4a62; border-left:1px solid #3a4a62;"></span><span style="position:absolute; right:0; top:0; width:calc(100% - 9px); height:100%; border-top:1px solid #3a4a62; border-right:1px solid #3a4a62;"></span><span style="position:absolute; left:0; bottom:0; width:calc(100% - 9px); height:100%; border-bottom:1px solid #3a4a62; border-left:1px solid #3a4a62;"></span><span style="position:absolute; right:0; bottom:0; width:calc(100% - 9px); height:100%; border-bottom:1px solid #3a4a62; border-right:1px solid #3a4a62;"></span>简单&nbsp;·&nbsp;成功</span>

  </div>

  <span style="position:relative; z-index:1; display:block; height:1px; margin:0 0 16px; background:linear-gradient(90deg, rgba(58,74,98,0.45), rgba(58,74,98,0));"></span>

  <p style="position:relative; z-index:1; margin:0; font-size:15px;">
  你几乎可以<b>感受</b>到这种关联正在大脑额叶中成形。bug和bug之间有一根线，你只是拒绝去看。每一次hotfix都在逃避那个真正的结构性问题。
  </p>

  <span style="position:relative; z-index:1; display:block; height:1px; width:45%; margin:18px 0 0; background:linear-gradient(90deg, rgba(123,133,122,0.35), rgba(123,133,122,0));"></span>

  <div style="position:relative; z-index:1; margin:14px 0 0; display:flex; align-items:baseline; gap:8px;">
  <span style="font-size:12px; letter-spacing:0.3em; opacity:0.55; color:#7b857a;">REVACHOL&nbsp;·&nbsp;'51</span>
  <span style="flex:1;"></span>
  <span style="font-family:'Edwardian Script ITC','French Script MT','Lucida Handwriting','Apple Chancery','Segoe Script','Brush Script MT',cursive; font-style:italic; font-size:23px; letter-spacing:0.04em; color:#3a4a62;">Logic</span>
  </div>

</div>

<br>

<div style="display:block; box-sizing:border-box; position:relative;
            width:100%; max-width:400px; margin:16px auto;
            padding:26px 28px 22px;
            font-family:Georgia,'Songti SC','SimSun',serif; color:#c7b7e7;
            line-height:1.8; letter-spacing:0.02em; overflow-wrap:break-word;">

  <div style="position:relative; z-index:1; display:flex; align-items:center; gap:10px; margin:0 0 14px;">

  <span style="font-size:10px; color:#221d39;">◆</span>
  <span style="font-family:'Source Han Serif SC','Noto Serif CJK SC','Songti SC','SimSun',serif; font-size:19px; font-weight:bold; letter-spacing:0.28em; color:#221d39; white-space:nowrap;">从容自若</span>

  <span style="position:relative; display:inline-block; white-space:nowrap; font-family:'Source Han Serif SC','Noto Serif CJK SC','Songti SC','SimSun',serif; font-size:13px; letter-spacing:0.12em; padding:5px 12px; color:#221d39; background:rgba(34,29,57,0.08);"><span style="position:absolute; left:0; top:0; width:calc(100% - 9px); height:100%; border-top:1px solid #221d39; border-left:1px solid #221d39;"></span><span style="position:absolute; right:0; top:0; width:calc(100% - 9px); height:100%; border-top:1px solid #221d39; border-right:1px solid #221d39;"></span><span style="position:absolute; left:0; bottom:0; width:calc(100% - 9px); height:100%; border-bottom:1px solid #221d39; border-left:1px solid #221d39;"></span><span style="position:absolute; right:0; bottom:0; width:calc(100% - 9px); height:100%; border-bottom:1px solid #221d39; border-right:1px solid #221d39;"></span>简单&nbsp;·&nbsp;成功</span>

  </div>

  <span style="position:relative; z-index:1; display:block; height:1px; margin:0 0 16px; background:linear-gradient(90deg, rgba(34,29,57,0.45), rgba(34,29,57,0));"></span>

  <p style="position:relative; z-index:1; margin:0; font-size:15px;">
  你现在就想冲进群聊里尖叫。别。深呼吸。把这张扑克脸焊在脸上，然后一行一行单步调试，就像你被所有人看着那样。
  </p>

  <span style="position:relative; z-index:1; display:block; height:1px; width:45%; margin:18px 0 0; background:linear-gradient(90deg, rgba(199,183,231,0.35), rgba(199,183,231,0));"></span>

  <div style="position:relative; z-index:1; margin:14px 0 0; display:flex; align-items:baseline; gap:8px;">
  <span style="font-size:12px; letter-spacing:0.3em; opacity:0.55; color:#c7b7e7;">REVACHOL&nbsp;·&nbsp;'51</span>
  <span style="flex:1;"></span>
  <span style="font-family:'Edwardian Script ITC','French Script MT','Lucida Handwriting','Apple Chancery','Segoe Script','Brush Script MT',cursive; font-style:italic; font-size:23px; letter-spacing:0.04em; color:#221d39;">Composure</span>
  </div>

</div>

<br>

写代码出 bug 是正常且不可避免的，关键在于**追因方法**而非频繁 hotfix。以下是一些可操作的建议：

1. **先复现，再修复**：如果你无法稳定复现一个 bug，那你其实并不理解它。把复现步骤写下来，精确到每一步操作和预期结果。

2. **二分法定位**：对于难以追踪的 bug，用 git bisect 或手动注释掉一半代码来缩小范围——这比肉眼扫代码快一个数量级。

3. **写测试，再改代码**：对 bug 触发路径先补一个失败的单测，修完后让它变绿。这能防止同一个 bug 在被修复后再次回归。

4. **关注"最近的改动"**：大多数 bug 的根因藏在最近一次提交里。先看 `git diff`，再怀疑框架/环境/依赖。

5. **接受 bug 是常态**：bug 不代表你能力不足。每一个有经验的开发者都在和 bug 共处。区别只在于他们有一套自己的排查流程，而不是原地恐慌。
