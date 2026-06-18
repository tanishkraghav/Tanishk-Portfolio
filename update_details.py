import re
import os

page_js_path = r"C:\Users\hp\.gemini\antigravity\scratch\tanishk_portfolio\src\app\page.js"
with open(page_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace NPS -> TR
content = content.replace("NPS\n        </a >", "TR\n        </a >")

# Replace PROJECTS
new_projects = """const PROJECTS = [
  {
    name: 'ResearchPilot',
    tag: 'Multi-Agent AI',
    year: '2024',
    description:
      'A 5-node LangGraph supervisor graph routing queries across specialist agents with confidence-weighted synthesis and PromptOps eval layer.',
    bullets: [
      'Routed queries across 4 specialist agents (web search, RAG, fact-check, synthesiser).',
      'Shipped an integrated PromptOps eval layer with A/B comparison across 3 LLMs.',
    ],
    stack: ['Python', 'LangGraph', 'Groq API', 'Tavily', 'ChromaDB', 'FastAPI', 'React', 'Docker'],
    accent: 'from-violet-500 via-fuchsia-500 to-pink-500',
    live: 'https://github.com/tanishkraghav',
    github: 'https://github.com/tanishkraghav',
  },
  {
    name: 'Text-to-SQL LLM App',
    tag: 'Generative AI',
    year: '2024',
    description:
      'A Streamlit app using Groq API and LangChain to translate natural language to SQL, achieving 92% accuracy.',
    bullets: [
      'Integrated SQLite, MySQL, and PostgreSQL backends.',
      'Enabled schema-aware query generation across 3+ database systems.',
    ],
    stack: ['Python', 'Streamlit', 'Groq API', 'LangChain', 'SQL'],
    accent: 'from-sky-500 via-cyan-400 to-emerald-400',
    live: 'https://github.com/tanishkraghav',
    github: 'https://github.com/tanishkraghav',
  },
  {
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
  },
]"""
content = re.sub(r'const PROJECTS = \[.*?\]\n', new_projects + '\n', content, flags=re.DOTALL)

# Replace EXPERIENCE
new_experience = """const EXPERIENCE = [
  {
    company: 'C-DAC',
    role: 'HPC Intern',
    period: 'Dec 2024 \u2014 Feb 2025',
    location: 'Onsite',
    bullets: [
      'Reconfigured SLURM job scheduling across a 200-node HPC cluster, cutting computational backlog by 20% and improving resource utilization.',
      'Engineered parallel processing pipelines for batch workloads, increasing data throughput by 15% and reducing job completion time.',
    ],
    tags: ['HPC', 'SLURM', 'Parallel Processing', 'Cluster Management'],
  },
  {
    company: 'Airtel',
    role: 'Cybersecurity Intern',
    period: 'Jul 2025 \u2014 Aug 2025',
    location: 'Onsite',
    bullets: [
      'Triaged and analyzed 1,000+ daily security alerts using monitoring tools, achieving zero missed critical escalations.',
      'Accelerated incident response efficiency by 15% by implementing improved alert prioritization workflows.',
    ],
    tags: ['Cybersecurity', 'Alert Triage', 'Incident Response'],
  },
  {
    company: 'Edunet Foundation',
    role: 'AI & Cloud Intern',
    period: 'Sep 2025 \u2014 Nov 2025',
    location: 'Remote',
    bullets: [
      'Deployed an NLP-powered conversational AI chatbot on IBM Cloud, improving predefined query accuracy by 30%.',
      'Trained and evaluated 3+ supervised ML models on IBM Cloud, reaching up to 85% classification accuracy.',
    ],
    tags: ['AI', 'IBM Cloud', 'NLP', 'Machine Learning'],
  },
]"""
content = re.sub(r'const EXPERIENCE = \[.*?\]\n', new_experience + '\n', content, flags=re.DOTALL)

# Replace SKILLS
new_skills = """const SKILLS = {
  'Languages & Data': ['Python (Pandas, NumPy, Scikit-learn)', 'R', 'SQL', 'Excel'],
  'AI / ML': ['Machine Learning', 'Deep Learning', 'NLP', 'Generative AI', 'Agentic AI', 'LangChain', 'LangGraph', 'RAG'],
  'Visualization': ['Power BI', 'Tableau', 'Matplotlib', 'Seaborn'],
  'Cloud & DevOps': ['Oracle Cloud', 'IBM Cloud', 'HPC', 'SLURM', 'Docker', 'Git'],
  'Frameworks': ['FastAPI', 'React'],
}"""
content = re.sub(r'const SKILLS = \{.*?\}\n', new_skills + '\n', content, flags=re.DOTALL)

# Replace MARQUEE
new_marquee = """const MARQUEE = [
  'Python', 'SQL', 'LangChain', 'LangGraph', 'Generative AI', 'Agentic AI',
  'Machine Learning', 'NLP', 'Docker', 'FastAPI', 'React', 'Power BI', 'Oracle Cloud',
  'IBM Cloud', 'HPC', 'SLURM', 'ChromaDB', 'RAG',
]"""
content = re.sub(r'const MARQUEE = \[.*?\]\n', new_marquee + '\n', content, flags=re.DOTALL)

# Replace B.Tech info
content = content.replace("B.Tech IIIT Una'26", "B.Tech IMS Engineering College '26")

# Replace Name
content = content.replace('Nitin Pratap <span className="font-serif italic text-foreground/80">Singh</span>', 'Tanishk <span className="font-serif italic text-foreground/80">Raghav</span>')

# Replace Subtitle
content = content.replace('Software Engineer building <span className="text-foreground">delightful interfaces</span> at the\n            intersection of design and engineering.Crafting fast, considered products with Next.js, TypeScript and a love for the details.',
'Data Scientist & LLM Developer building <span className="text-foreground">agentic AI systems</span> and intelligent NLP pipelines. Transforming unstructured data into scalable solutions with Python, LangChain, and advanced ML workflows.')

# Replace Stats
content = content.replace("{ k: '3', v: 'Internships Completed' }", "{ k: '3+', v: 'Internships Completed' }")
content = content.replace("{ k: '15+', v: 'Projects shipped' }", "{ k: '10+', v: 'Projects shipped' }")
content = content.replace("{ k: 'AWS', v: 'EC2 · RDS · S3' }", "{ k: 'Cloud', v: 'Oracle · IBM' }")
content = content.replace("{ k: '∞', v: 'Cups of chai' }", "{ k: '87%', v: 'Model Accuracy' }")

# Replace About Section text
content = content.replace("I'm a fresher Software Engineer who treats every interface like a product. From pixel-perfect motion to\n              shipping production - grade backends on AWS, I love bridging the gap between what feels good and what scales.\n              When I'm not shipping, I'm exploring new tech, contributing to side projects, or studying products I admire.",
"I'm an AI-focused Data Scientist and LLM Developer with a proven track record in Generative AI and NLP pipelines. From building autonomous multi-agent systems to accelerating ETL pipelines by 40%, I am passionate about engineering scalable, intelligent applications.")
content = content.replace("Open to SWE / Frontend roles", "Open to Data Science / AI roles")
content = content.replace("Next.js · TypeScript · AWS · Design Engineering", "Python · LangChain · LangGraph · AI Agents")

# Replace Links
content = content.replace("https://github.com/NitinSingh07", "https://github.com/tanishkraghav")
content = content.replace("https://www.linkedin.com/in/nitin-pratap-singh-319665257/", "https://www.linkedin.com/in/tanishk-raghav/")
content = content.replace("nitinthakur4406@gmail.com", "tanishkraghav2004@gmail.com")
content = content.replace("nitinthakur4406 @gmail.com", "tanishkraghav2004@gmail.com")

# Replace Footer
content = content.replace("Nitin Pratap Singh", "Tanishk Raghav")

with open(page_js_path, 'w', encoding='utf-8') as f:
    f.write(content)

layout_js_path = r"C:\Users\hp\.gemini\antigravity\scratch\tanishk_portfolio\src\app\layout.js"
with open(layout_js_path, 'r', encoding='utf-8') as f:
    l_content = f.read()

l_content = l_content.replace("Nitin Pratap Singh", "Tanishk Raghav")
l_content = l_content.replace("Software Engineer", "Data Scientist")

with open(layout_js_path, 'w', encoding='utf-8') as f:
    f.write(l_content)
