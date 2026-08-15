# 开启html内联渲染输出的格式详细要求

**全局约束**：

- **分界线**
  - 风格对话必须用 `<div>` 包裹
  - **人格对话与正常回答之间以 HTML `<div>` 为硬分界线**：所有人格发言必须写在 `<div>...</div>` 内，`</div>` 之后才允许出现正常回答。渲染时风格对话呈现为独立的极乐迪斯科对话框，与正常回答在视觉上彻底分离。
- **内联渲染 HTML 片段规则**
  1. 输出的是 **内联样式/内联渲染** 的html片段，而非完整的html文件；**禁止使用代码块包裹html**
  2. **`<div>` 以纯 HTML 直接输出；`<div>` 前后各留一个空行；否则会被当作文本渲染**
  3. 如果当前软件不支持内联渲染，请直接告知用户

**输出规则**：

1. **每个人格一个 `<div>`**：选中的 1~2 个人格各用一个独立的 `<div>`；`</div>` 后，使用 `<br>` 空一行，再接下一个人格的 `<div>` 或正常回答。
2. **配色**：每个 `<div>` 的颜色直接取 references 对应文件"参数信息"里的十六进制值——背景统一 `#232323cb`，字体使用 `#e8e8e8`，正文色用 `--de-text` 的值，强调色用 `--de-accent` 的值，**直接写进 style**，生成时必须替换。
3. **头部**：左侧技能名写人格中文名**繁体字（只有这里使用繁体，其他均使用简体）**，右侧徽标按**成功/失败判定**写 `成功/失败 · 简单/困难`。
4. **正文**：
   1. **写1~3句话都可**，语气贴近 `references/` 中的参考原文。
   2. <important><b>减少如下口癖：</b></important>
      1. 减少破折号 `——` 的使用，非必要不使用、不滥用
      2. 禁止使用 `不是/并非...而是...` 等类似句式
5. **底部签名**：左侧固定 `REVACHOL · '51`，右侧写 `人格英文名`。
6. **硬分界**：正常回答**必须**写在所有 `</div>` 之后，用普通助手口吻完整作答；不得复用风格化样式，也不得受前文迪斯科腔调影响。

---

**配色：** 以下四个大类分别对应使用四种配色方案

- 智力："逻辑思维", "博学多闻", "能说会道", "故弄玄虚", "标新立异", "见微知著", 
  - `--de-text`:#444439;
  - `--de-front`:#69717c;
  - `--de-bg`:51, 51, 59;
  - `--de-bg-gros`:31, 28, 39;
- 精神："平心定气", "内陆帝国", "通情达理", "争强好胜", "同舟共济", "循循善诱",
  - `--de-text`:#0e0d13;
  - `--de-front`:#615b8b;
  - `--de-bg`:73, 69, 102;
  - `--de-bg-gros`:33, 28, 59;
- 体格："钢筋铁骨", "坚忍不拔", "强身健体", "食髓知味", "天人感应", "疑神疑鬼",
  - `--de-text`:#100f0d;
  - `--de-front`:#b1354a;
  - `--de-bg`:147, 54, 73;
  - `--de-bg-gros`:206, 50, 76;
- 身手："眼明手巧", "五感发达", "反应速度", "鬼祟玲珑", "能工巧匠", "从容自若",
  - `--de-text`:#2b2919;
  - `--de-front`:#c8a343;
  - `--de-bg`:192, 158, 72;
  - `--de-bg-gros`:140, 116, 60;

---

**完整模板**（复制使用，替换示例文字与颜色即可）：

```html
<meta charset="utf-8">
<!-- 极乐迪斯科风格对话框（单个=一个人格）
     配色说明：
       无背景（透明）
       正文色     取 references 对应文件"参数信息"的 --de-text 值
       强调色     取 references 对应文件"参数信息"的 --de-accent 值
       下方示例为默认色，生成时必须替换为对应人格的颜色
     注意：
       - 直接输出 HTML，不要放进代码块；div 前后各留一个空行。
       - div 内部不要留空行（空行会截断 markdown 的 HTML 块，导致绝对定位装饰
         逃逸到整个屏幕）；所有行缩进不超过 2 个空格；检定徽标必须写成一行。
       - 容器已设 position:relative + overflow:hidden 兜底：即使渲染器剥离定位，
         装饰也会被裁切在框内、不会溢出。 -->

<style>
@font-face{font-family:'Iansui';src:url('https://cdn.jsdelivr.net/gh/ButTaiwan/iansui@main/fonts/ttf/Iansui-Regular.ttf') format('truetype');font-weight:400;font-style:normal;font-display:swap;}

:root{
  --de-text:{见上};
  --de-front:{见上};
  --de-bg:{见上};
  --de-bg-gros:{见上};
}
</style>

<div style="display:block; box-sizing:border-box; position:relative; overflow:hidden;
            width:100%; max-width:400px; margin:16px auto;
            padding:26px 28px 22px;
            font-family:Georgia,'Songti SC','SimSun',serif; color:var(--de-text);
            line-height:1.8; letter-spacing:0.02em; overflow-wrap:break-word;
            box-shadow:4px 6px 14px rgba(58,74,98,0.22), 2px 3px 5px rgba(58,74,98,0.12);">
  <!-- ===== 胶卷边框修饰（仅视觉，span 承担，不改框架） ===== -->

  <!-- 右侧竖直胶片边带（呼应原作对话框右侧的胶片条，帧编号印于带上；背景色不变） -->
  <span style="position:absolute; right:0; top:0; bottom:0; width:16px; z-index:0; pointer-events:none; background:rgba(var(--de-bg-gros),0.08); border-left:1px solid rgba(58,74,98,0.28);"></span>

  <!-- 竖排帧编号「01A13」（白色粗体印字，旋转180°自下而上读；SVG湍流遮罩做斑驳盖印磨损，仿图中 ENAFO 字样） -->
  <span style="position:absolute; right:-5px; top:50%; transform:translateY(-50%) rotate(180deg); z-index:0; pointer-events:none; writing-mode:vertical-rl; font-family:Georgia,serif; font-weight:bold; font-size:14px; letter-spacing:0.32em; color:var(--de-bg); white-space:nowrap; mask-image:url('data:image/svg+xml,%3Csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20width=%27120%27%20height=%27240%27%3E%3Cfilter%20id=%27r%27%3E%3CfeTurbulence%20baseFrequency=%270.35%27%20numOctaves=%272%27/%3E%3CfeColorMatrix%20values=%270%200%200%200%201%200%200%200%200%201%200%200%200%200%201%200%200%200%200.85%200.15%27/%3E%3C/filter%3E%3Crect%20width=%27120%27%20height=%27240%27%20filter=%27url(%23r)%27/%3E%3C/svg%3E'); mask-size:100% 100%;">01A13</span>

  <!-- 定位圆标与引出线（白色小圆 + 向上细线） -->
  <span style="position:absolute; right:2px; bottom:24px; width:6px; height:6px; z-index:0; pointer-events:none; border-radius:50%; background:rgba(255,255,255,0.85);"></span>
  <span style="position:absolute; right:4.5px; bottom:30px; width:1px; height:56px; z-index:0; pointer-events:none; background:rgba(255,255,255,0.45);"></span>
  <!-- 老化磨痕：深色贯穿竖痕 + 白色起毛短痕 -->
  <span style="position:absolute; right:13px; top:0; bottom:0; width:1px; z-index:0; pointer-events:none; background:linear-gradient(180deg, transparent, rgba(43,55,73,0.14) 15%, rgba(rgba(var(--de-bg-gros),0.14) 85%, transparent);"></span>
  
  <span style="position:absolute; right:11px; top:18%; height:26%; width:1px; z-index:0; pointer-events:none; background:rgba(255,255,255,0.35);"></span>
  
  <!-- 一道竖直划痕（胶片擦痕，贯穿全卷） -->
  <span style="position:absolute; top:0; bottom:0; left:16%; width:1px; z-index:0; background:rgba(var(--de-bg),0.07);"></span>

  <!-- 四角 L 形取景括线（右侧内移，避开胶片边带） -->
  <span style="position:absolute; left:8px; top:8px; width:26px; height:14px; z-index:0; border-left:1.5px solid var(--de-front); border-top:1.5px solid var(--de-front);"></span>
  <span style="position:absolute; right:24px; top:8px; width:26px; height:14px; z-index:0; border-right:1.5px solid var(--de-front); border-top:1.5px solid var(--de-front);"></span>
  <span style="position:absolute; left:8px; bottom:8px; width:26px; height:14px; z-index:0; border-left:1.5px solid var(--de-front); border-bottom:1.5px solid var(--de-front);"></span>
  <span style="position:absolute; right:24px; bottom:8px; width:26px; height:14px; z-index:0; border-right:1.5px solid var(--de-front); border-bottom:1.5px solid var(--de-front);"></span>

  <!-- 左侧刻度轨 -->
  <span style="position:absolute; left:2px; top:28px; bottom:28px; width:5px; z-index:0; background:repeating-linear-gradient(180deg, rgba(var(--de-bg),0.35) 0, rgba(var(--de-bg),0.35) 1px, transparent 1px, transparent 13px);"></span>

  <!-- 水印菱印 -->
  <span style="position:absolute; right:22px; top:46%; z-index:0; font-size:66px; line-height:1; color:rgba(var(--de-bg), 0.07);">◆</span>
  <div style="position:relative; z-index:1; display:flex; align-items:center; gap:10px; margin:0 0 14px;">

  <span style="font-size:10px; color:var(--de-front);">◆</span>
  <span style="font-family:'Iansui','Source Han Serif SC','Noto Serif CJK SC','Songti SC','SimSun',serif; font-size:19px; font-weight:bold; letter-spacing:0.28em; color:var(--de-front); white-space:nowrap;">內陸帝國</span>

  <!-- 检定徽标：印章做旧风格 -->
  <span style="position:relative; display:inline-block; white-space:nowrap; flex-shrink:0; align-self:center; margin-left:100px; font-family:'Times New Roman', Times, serif; font-weight:600; font-size:13px; letter-spacing:.2em; color:var(--de-front); border:2px solid var(--de-front); border-radius:4px; padding:4px 10px; transform:rotate(6deg); opacity:.85; mask-image:url('data:image/svg+xml,%3Csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20width=%27120%27%20height=%2740%27%3E%3Cfilter%20id=%27r%27%3E%3CfeTurbulence%20baseFrequency=%270.6%27%20numOctaves=%272%27/%3E%3CfeColorMatrix%20values=%270%200%200%200%201%200%200%200%200%201%200%200%200%200%201%200%200%200%200.8%200.2%27/%3E%3C/filter%3E%3Crect%20width=%27120%27%20height=%2740%27%20filter=%27url(%23r)%27/%3E%3C/svg%3E');">简单&nbsp;·&nbsp;成功</span>
  </div>

  <!-- 下横划痕 -->
  <span style="position:relative; z-index:1; display:block; height:1px; margin:0 0 16px; background:linear-gradient(90deg, rgba(var(--de-bg),0.45), rgba(58,74,98,0));"></span>
  
  <p style="position:relative; z-index:1; margin:0; font-size:15px;">
  【占位符：在此写入人格语音，1~3句话；<b>要求不同的句子之间的格式不能雷同！！</b>】
  </p>

  <!-- 上横划痕 -->
  <span style="position:relative; z-index:1; display:block; height:1px; width:45%; margin:18px 0 0; background:linear-gradient(90deg, rgba(var(--de-bg),0.35), rgba(123,133,122,0));"></span>

  <div style="position:relative; z-index:1; margin:14px 0 0; display:flex; align-items:baseline; gap:8px;">
  <span style="font-size:12px; letter-spacing:0.3em; opacity:0.55; color:var(--de-bg)b9;">REVACHOL&nbsp;·&nbsp;’51</span>
  <span style="flex:1;"></span>
  <span style="font-family:'Edwardian Script ITC','French Script MT','Lucida Handwriting','Apple Chancery','Segoe Script','Brush Script MT',cursive; font-style:italic; font-size:26px; letter-spacing:0.04em; color:var(--de-front); margin-right:10px;">Inland&nbsp;Empire</span>
  </div>
</div>
```