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


group_dirs = sorted(p for p in data_dir.iterdir() if p.is_dir() and (p / 'index.md').exists())
cst_time = datetime.now(timezone(timedelta(hours=8)))
now_str = cst_time.strftime('%Y-%m-%d %H:%M') + ' CST'

lines = ['## 自動更新清單', '', f'Updated: {now_str}', '']
for d in group_dirs:
    lines.append(build_group_line(d))
    lines.append('')
generated = '\n'.join(lines)

readme_path = Path('README.md')
text = readme_path.read_text(encoding='utf-8')
start_marker = '<!-- AUTO-GENERATED:POSTS START -->'
end_marker = '<!-- AUTO-GENERATED:POSTS END -->'
replacement = f'{start_marker}\n{generated}\n{end_marker}'
pattern = re.compile(rf'{re.escape(start_marker)}.*?{re.escape(end_marker)}', re.DOTALL)
text = pattern.sub(replacement, text)
readme_path.write_text(text, encoding='utf-8')
print(f'README updated: {now_str}')
