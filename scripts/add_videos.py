"""
Add video URLs to files missing them in their frontmatter.
"""
import os, re

emner_dir = 'src/content/emner'

# Map of slug to video URL (best educational match)
VIDEOS = {
    'sql-grunnleggende': 'https://www.youtube.com/watch?v=7S_tz1z_5bA',
    'active-directory': 'https://www.youtube.com/watch?v=85-bp7XxWDQ',
    'bruker-og-tilgangsstyring': 'https://www.youtube.com/watch?v=fSRgESnRwAU',
    'filsystem': 'https://www.youtube.com/watch?v=F5itS2u4I1A',
    'linux-grunnleggende': 'https://www.youtube.com/watch?v=pkZEKIXe3u4',
    'risikoanalyse': 'https://www.youtube.com/watch?v=DejxGE91xJY',
    'trusselbildet': 'https://www.youtube.com/watch?v=nG9v3RSSXTo',
    'automatisering': 'https://www.youtube.com/watch?v=j9MAMgyNpAU',
}

count = 0
for emne in sorted(os.listdir(emner_dir)):
    ep = os.path.join(emner_dir, emne)
    if not os.path.isdir(ep):
        continue
    for f in sorted(os.listdir(ep)):
        if not f.endswith('.md') and not f.endswith('.mdx'):
            continue
        if f == '_oversikt.md' or f == 'osi-modellen-interaktiv.mdx':
            continue
        
        # Extract base slug (strip -en suffix for matching)
        base = re.sub(r'\.mdx?$', '', f)
        match_key = base.replace('-en', '')  # strip lang suffix
        
        if match_key not in VIDEOS:
            continue
            
        fp = os.path.join(ep, f)
        with open(fp) as fh:
            content = fh.read()
        
        if re.search(r'^video:', content, re.MULTILINE):
            continue  # already has video
            
        # Add video: after the last non-empty frontmatter tag (before tags or after sources)
        video_url = VIDEOS[match_key]
        
        # Insert video: line before tags: or at end of frontmatter
        if 'tags:' in content.split('---')[1] if '---' in content else False:
            content = re.sub(r'^tags:', f'video: {video_url}\ntags:', content, count=1, flags=re.MULTILINE)
        elif 'flashcards:' in content.split('---')[1] if '---' in content else False:
            content = re.sub(r'^flashcards:', f'video: {video_url}\nflashcards:', content, count=1, flags=re.MULTILINE)
        elif 'notebooklm:' in content.split('---')[1] if '---' in content else False:
            content = re.sub(r'^notebooklm:', f'video: {video_url}\nnotebooklm:', content, count=1, flags=re.MULTILINE)
        else:
            # Insert before public: or at end of frontmatter
            content = re.sub(r'^public:', f'video: {video_url}\npublic:', content, count=1, flags=re.MULTILINE)
        
        with open(fp, 'w') as fh:
            fh.write(content)
        count += 1
        print(f'Added video to {emne}/{f} -> {video_url}')

print(f'\nDone! Added videos to {count} files.')
