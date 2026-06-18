import re

page_js_path = r"C:\Users\hp\.gemini\antigravity\scratch\tanishk_portfolio\src\app\page.js"
with open(page_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Taxi Trip Analysis project
old_project = """  {
    name: 'Taxi Trip Analysis',
    tag: 'Data Analysis',
    year: '2024',
    description: 'Ingested and processed a 2GB+ NYC taxi dataset using optimized Pandas pipelines.',
    bullets: [
      'Reduced compute time by 35% through optimized pipelines.',
      'Built a Power BI dashboard to visualize revenue trends, identifying 20% higher fare yields.',
    ],
    stack: ['Python', 'Pandas', 'Power BI', 'Matplotlib'],
    accent: 'from-rose-500 via-orange-400 to-amber-300',
    live: 'https://github.com/tanishkraghav',
    github: 'https://github.com/tanishkraghav',
  },"""

new_project = """  {
    name: 'AI Persona',
    tag: 'Voice & Chat Agent',
    year: '2024',
    description: 'A live AI persona integrating Vapi, Claude Sonnet, and ElevenLabs for voice calls, plus a Next.js chat interface with RAG over personal knowledge.',
    bullets: [
      'Orchestrated a Voice Agent (Vapi + Deepgram + Claude + ElevenLabs) achieving ~1.4s avg first-response latency.',
      'Built a Next.js RAG chat interface using Anthropic SDK, Vercel Edge, and custom chunk retrieval.',
    ],
    stack: ['Next.js', 'Anthropic', 'Vapi', 'ElevenLabs', 'Deepgram', 'RAG'],
    accent: 'from-rose-500 via-orange-400 to-amber-300',
    live: 'https://tanishk-persona.vercel.app/',
    github: 'https://github.com/tanishkraghav/ai-persona',
  },"""

if old_project in content:
    content = content.replace(old_project, new_project)
    with open(page_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Old project text not found exactly as expected")
    # Try regex fallback
    new_content = re.sub(r'\{\s*name:\s*\'Taxi Trip Analysis\'.*?\},', new_project, content, flags=re.DOTALL)
    if new_content != content:
        with open(page_js_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Replaced successfully using regex")
    else:
        print("Regex fallback also failed")
