import sys
import re
import json
import glob
from pathlib import Path
from datetime import datetime, timezone, timedelta
from urllib import parse

data_dir = Path('data')


def build_group_line(posts_dir):
    markdown_files = list(posts_dir.glob('*.md'))
    markdown_files = [f for f in markdown_files if f.name != 'index.md']
    page_title = posts_dir.name
    follower_count = ''
    summary_path = posts_dir / 'latest_fetch_summary.json'
    if summary_path.exists():
        try:
            summary = json.loads(summary_path.read_text(encoding='utf-8'))
            follower_count = summary.get('page', {}).get('follower_count') or ''
        except Exception:
            pass
    index_path = parse.quote((posts_dir / 'index.md').as_posix(), safe='/')
    count_str = f' (已收錄: {len(markdown_files)})'
    follower_str = f' - {follower_count}' if follower_count else ''
    return f'### [{page_title}]({index_path}){count_str}{follower_str}'


def has_posts(d):
    return any(f.name != 'index.md' for f in d.glob('*.md'))


DATE_PREFIX_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})_')


def posts_by_date(posts_dir):
    """Map YYYY-MM-DD -> sorted list of markdown filenames posted that day."""
    by_date = {}
    for f in posts_dir.glob('*.md'):
        if f.name == 'index.md':
            continue
        match = DATE_PREFIX_RE.match(f.name)
        if not match:
            continue
        by_date.setdefault(match.group(1), []).append(f.name)
    for filenames in by_date.values():
        filenames.sort()
    return by_date


TITLE_RE = re.compile(r'^title:\s*"((?:[^"\\]|\\.)*)"', re.MULTILINE)

reports_dir = Path('data/reports')


def extract_title(post_path):
    try:
        text = post_path.read_text(encoding='utf-8')
    except OSError:
        return post_path.stem
    match = TITLE_RE.search(text)
    if not match:
        return post_path.stem
    return match.group(1).replace('\\"', '"').replace('\\\\', '\\')


def write_daily_report(date_str, group_dirs, all_by_date):
    lines = [f'# {date_str} 貼文彙整', '']
    any_post = False
    for d in group_dirs:
        filenames = all_by_date[d.name].get(date_str)
        if not filenames:
            continue
        any_post = True
        lines.append(f'## {d.name}')
        lines.append('')
        for fname in filenames:
            title = extract_title(d / fname)
            link_path = parse.quote((Path('..') / d.name / fname).as_posix(), safe='/')
            lines.append(f'- [{title}]({link_path})')
        lines.append('')
    if not any_post:
        lines.append('（當日無新貼文）')
        lines.append('')
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / f'{date_str}.md').write_text('\n'.join(lines), encoding='utf-8', newline='\n')


def build_weekly_table(group_dirs, today_utc):
    dates = [(today_utc - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
    all_by_date = {d.name: posts_by_date(d) for d in group_dirs}
    for date_str in dates:
        write_daily_report(date_str, group_dirs, all_by_date)

    header_cells = [f'[{d[5:].replace("-", "/")}](data/reports/{d}.md)' for d in dates]
    lines = [
        '## 報告彙整（近 7 天）',
        '',
        '| 名稱 | ' + ' | '.join(header_cells) + ' |',
        '|  :---: | ' + ' | '.join([':---:'] * len(dates)) + ' |',
    ]
    for d in group_dirs:
        by_date = all_by_date[d.name]
        cells = []
        for date_str in dates:
            filenames = by_date.get(date_str)
            if not filenames:
                cells.append('-')
                continue
            link_path = parse.quote((d / filenames[0]).as_posix(), safe='/')
            cells.append(f'[{len(filenames)}]({link_path})')
        page_title = d.name
        lines.append(f'| {page_title} | ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines)


group_dirs = sorted(
    (p for p in data_dir.iterdir() if p.is_dir() and (p / 'index.md').exists() and has_posts(p)),
    key=lambda p: p.name,
)
cst_time = datetime.now(timezone(timedelta(hours=8)))
now_str = cst_time.strftime('%Y-%m-%d %H:%M') + ' CST'
today_utc = datetime.now(timezone.utc)

lines = ['## 自動更新清單', '', f'Updated: {now_str}', '']
for d in group_dirs:
    lines.append(build_group_line(d))
    lines.append('')
generated = '\n'.join(lines)
weekly_generated = build_weekly_table(group_dirs, today_utc)

readme_path = Path('README.md')
text = readme_path.read_text(encoding='utf-8', newline='\n')

start_marker = '<!-- AUTO-GENERATED:POSTS START -->'
end_marker = '<!-- AUTO-GENERATED:POSTS END -->'
replacement = f'{start_marker}\n{generated}\n{end_marker}'
pattern = re.compile(rf'{re.escape(start_marker)}.*?{re.escape(end_marker)}', re.DOTALL)
text = pattern.sub(replacement, text)

weekly_start_marker = '<!-- AUTO-GENERATED:WEEKLY START -->'
weekly_end_marker = '<!-- AUTO-GENERATED:WEEKLY END -->'
weekly_replacement = f'{weekly_start_marker}\n{weekly_generated}\n{weekly_end_marker}'
weekly_pattern = re.compile(rf'{re.escape(weekly_start_marker)}.*?{re.escape(weekly_end_marker)}', re.DOTALL)
text = weekly_pattern.sub(weekly_replacement, text)

readme_path.write_text(text, encoding='utf-8', newline='\n')
print(f'README updated: {now_str}')
