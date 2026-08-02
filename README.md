# DiscoElysiumPersonalities-Skill-Unified

以《极乐迪斯科》24 人格为原型的中文对话 skill。触发后，由 1~2 个人格以"脑内声音"的方式对你说话，再以普通助手口吻回答你的问题。

## 目录结构

```
├── SKILL.md                 # 人格对话 skill（路由、输出格式、HTML 模板）
├── references/              # 24 个人格的资料：详细介绍 + 配色参数 + 台词语料
├── assets/                  # 台词原文（1~400页）与展示用 HTML（四个色系）
└── scripts/
    └── classify_personalities.py   # 台词文件处理脚本：把台词按人格拆分/合并进 references/
```

## 使用

- **触发**：输入 `Disco:on` 或 `Disco on` 启动，之后默认保持开启；`Disco:off` 关闭。
- **新增台词**：将新一页台词放入 `assets/`，运行

```powershell
python scripts/classify_personalities.py assets/极乐迪斯科-台词-中文版-XXX~XXX页.md
```

结果自动合并进 `references/` 对应人格文件（按"含成功 / 不含成功"分节）。

## 配色

每个 references 文件 `## 参数信息` 提供 `--de-bg`（统一 `#0c0c0c`）、`--de-text`、`--de-accent`，按四大属性分组：

| 板块 | text | accent |
|---|---|---|
| Intellect 智力 | #7b857a | #3a4a62 |
| Psyche 精神 | #c7b7e7 | #221d39 |
| Physique 体格 | #b04045 | #7d2429 |
| Motorics 身手 | #c2a435 | #b69a46 |

生成对话时按人格替换进 HTML 模板即可换肤。

玩得愉快~⭐
