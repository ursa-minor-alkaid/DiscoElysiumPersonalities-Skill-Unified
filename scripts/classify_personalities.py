# -*- coding: utf-8 -*-
"""按极乐迪斯科 24 人格分类台词，合并到 references/ 下每人格一个 markdown 文件。

用法:
    python classify_personalities.py <输入.md> [输出目录]
    不带参数时默认处理项目根目录下的 SKILL.md
    第二个参数可选，指定输出目录（默认项目 references/ 目录）

规则:
    - 只提取以 24 人格名（四字）开头的行；行内第一个 "—" 之前为标记区，
      忽略 "—" 前后的空格；
    - 标记区去掉末尾的 "【...】"（如 【成功】）后，必须以某个人格名开头；
    - 被去掉的 "【...】" 标记会重新贴在内容前，因此内容保留 【成功】 等原标记；
    - 每人格一个 .md 文件（以英文名命名，见 ENGLISH_NAMES），文件内按
      "含成功"（标记中含【成功】）与 "不含成功" 两节分类；
    - 新内容合并进已有文件的对应小节（旧内容在前、新内容在后），而非覆盖；
    - 无法匹配 24 人格的行会被丢弃。
"""

import os
import re
import sys
from collections import OrderedDict

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'references')

PERSONALITIES = [
    # 智力
    "逻辑思维", "博学多闻", "能说会道", "故弄玄虚", "标新立异", "见微知著",
    # 精神
    "平心定气", "内陆帝国", "通情达理", "争强好胜", "同舟共济", "循循善诱",
    # 体格
    "钢筋铁骨", "坚忍不拔", "强身健体", "食髓知味", "天人感应", "疑神疑鬼",
    # 身手
    "眼明手巧", "五感发达", "反应速度", "鬼祟玲珑", "能工巧匠", "从容自若",
]

MARKER_RE = re.compile(r'((?:【[^】]*】)+)$')

# 输出文件名（英文名；Windows 不允许文件名含 "/"，故 Hand/Eye 写成 Hand-Eye）
ENGLISH_NAMES = {
    "逻辑思维": "Logic",
    "博学多闻": "Encyclopedia",
    "能说会道": "Rhetoric",
    "故弄玄虚": "Drama",
    "标新立异": "Conceptualization",
    "见微知著": "Visual Calculus",
    "平心定气": "Volition",
    "内陆帝国": "Inland Empire",
    "通情达理": "Empathy",
    "争强好胜": "Authority",
    "同舟共济": "Esprit de Corps",
    "循循善诱": "Suggestion",
    "钢筋铁骨": "Endurance",
    "坚忍不拔": "Pain Threshold",
    "强身健体": "Physical Instrument",
    "食髓知味": "Electrochemistry",
    "天人感应": "Shivers",
    "疑神疑鬼": "Half Light",
    "眼明手巧": "Hand-Eye Coordination",
    "五感发达": "Perception",
    "反应速度": "Reaction Speed",
    "鬼祟玲珑": "Savoir Faire",
    "能工巧匠": "Interfacing",
    "从容自若": "Composure",
}


def parse(line):
    """解析一行，返回 (人格名, 是否含成功, 内容)；不匹配 24 人格时返回 None。"""
    idx = line.find('—')
    if idx == -1:
        return None
    prefix = line[:idx].strip()
    content = line[idx + 1:].strip()

    m = MARKER_RE.search(prefix)
    if m:
        name = prefix[:m.start()].strip()
        marker = m.group(1)
    else:
        name = prefix
        marker = ''

    if not name:
        return None
    for p in PERSONALITIES:
        if name.startswith(p):
            return p, '【成功】' in marker, marker + content
    return None


def read_existing(filepath):
    """读取已有文件，返回 (含成功行列表, 不含成功行列表)；文件不存在时返回两个空列表。"""
    success, normal = [], []
    if not os.path.isfile(filepath):
        return success, normal
    current = None
    with open(filepath, encoding='utf-8') as f:
        for raw in f:
            line = raw.rstrip('\r\n')
            if line == '## 含成功':
                current = success
            elif line == '## 不含成功':
                current = normal
            elif line.strip() and current is not None:
                current.append(line.strip())
    return success, normal


def write_sections(filepath, success_lines, normal_lines):
    parts = []
    if success_lines:
        parts.append('## 含成功\n\n' + '\n\n'.join(success_lines))
    if normal_lines:
        parts.append('## 不含成功\n\n' + '\n\n'.join(normal_lines))
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(parts) + '\n')


def main():
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = os.path.join(PROJECT_ROOT, 'SKILL.md')
    output_dir = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUTPUT_DIR

    if not os.path.isfile(input_path):
        print(f'错误：找不到文件 {input_path}')
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    new_lines = OrderedDict((p, {'成功': [], '普通': []}) for p in PERSONALITIES)
    dropped = 0

    with open(input_path, encoding='utf-8') as f:
        for raw in f:
            line = raw.rstrip('\r\n')
            if not line.strip():
                continue
            parsed = parse(line)
            if parsed is None:
                dropped += 1
                continue
            name, is_success, content = parsed
            new_lines[name]['成功' if is_success else '普通'].append(content)

    appended = 0
    for name in PERSONALITIES:
        ns = new_lines[name]['成功']
        nn = new_lines[name]['普通']
        if not ns and not nn:
            continue
        en_name = ENGLISH_NAMES[name]
        filepath = os.path.join(output_dir, en_name + '.md')
        old_success, old_normal = read_existing(filepath)
        success_lines = old_success + ns
        normal_lines = old_normal + nn
        write_sections(filepath, success_lines, normal_lines)
        print(f'[{en_name}] +{len(ns)} 含成功 / +{len(nn)} 不含成功'
              f'（累计 {len(success_lines)} / {len(normal_lines)}）')
        appended += 1

    print(f'\n完成：合并 {appended} 个文件（24 个人格），丢弃 {dropped} 行。')
    print(f'输出目录 {output_dir}')


if __name__ == '__main__':
    main()
