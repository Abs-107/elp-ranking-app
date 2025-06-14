import streamlit as st
import pandas as pd
from streamlit_sortables import sort_items

st.set_page_config(page_title="Team Project Ranking", layout="wide")
st.title("🗳️ Drag and Drop to Rank Projects")
st.write("Reorder the projects below by dragging them. Place your most preferred project at the top.")

# Final 16 project summaries for voting
projects = [
    ("ELP26-166", "To evaluate the feasibility and operational implementation of a predictive maintenance system for aircraft components. The project aims to leverage data and engineering insights to reduce costs and improve safety."),
    ("ELP26-132", "*****, a leader in premium study abroad and career counselling, is exploring strategic expansion and digital solutions. The focus is on enhancing global presence and streamlining user engagement."),
    ("ELP26-151", "***** is India’s first and largest marketplace for senior care services. The project aims to build a scalable, tech-enabled growth model in a fragmented sector."),
    ("ELP26-169", "Aircraft maintenance is a critical, complex, and expensive operation. The project seeks to analyze efficiency gaps and recommend AI-based workflow optimization."),
    ("ELP26-245", "***** is a pioneering deep-tech company revolutionizing battery materials. The project involves global market assessment and strategic partner identification."),
    ("ELP26-173", "This project involves the development of a strategic GTM plan for a new health-tech platform. It focuses on market sizing, competition analysis, and pricing strategy."),
    ("ELP26-211", "The project explores opportunities for an AI-driven recruitment platform to scale in Tier-2/3 markets. Emphasis is on market sizing, differentiation, and partnerships."),
    ("ELP26-212", "Focused on digitizing fleet operations in logistics, this project seeks to define product-market fit and market expansion paths. The outcome will guide platform positioning."),
    ("ELP26-237", "The project focuses on market strategy for cross-border payment infrastructure. It includes competitor benchmarking and corridor prioritization."),
    ("ELP26-236", "This is a strategic review of opportunities in the affordable housing financing segment. The project involves policy analysis, pricing frameworks, and growth strategies."),
    ("ELP26-187", "The project aims to create a blueprint for global expansion for a sustainability-focused Indian B2B company. It involves stakeholder analysis and market entry playbooks."),
    ("ELP26-191", "The objective is to develop an AI-powered market intelligence dashboard. It will automate business signal tracking and strategic alert generation."),
    ("ELP26-179", "This project focuses on designing a market entry strategy for a food-tech startup. Key tasks include competitor analysis, pricing, and distribution network design."),
    ("ELP26-143", "The client is a real estate data aggregator platform expanding into analytics. This project aims to define monetization strategy and B2B positioning."),
    ("ELP26-209", "This strategy project evaluates entry into the mental wellness segment. The team will define customer segments, product roadmap, and GTM channels."),
    ("ELP26-222", "The project explores diversification opportunities for a retail electronics giant. Focus areas include emerging categories and business model innovation.")
]

# Format for display: split into code and description columns with styling
styled_projects = [
    f"""
    <div style='display: flex; background-color: #d0f0e0; padding: 10px; margin: 5px; border-radius: 6px;'>
        <div style='flex: 1; font-weight: bold; color: #0b4d3a;'>{code}</div>
        <div style='flex: 4; color: #0a3c2d;'>{desc}</div>
    </div>
    """ for code, desc in projects
]

# Use HTML to render styled list
sorted_html = sort_items(styled_projects, direction="vertical")

# Convert back to original text for submission
reverse_map = {v: k for v, k in zip(styled_projects, projects)}
sorted_projects = [reverse_map[item] for item in sorted_html]

if st.button("Submit Rankings"):
    if len(sorted_projects) != 16:
        st.warning("Please rank all 16 projects before submitting.")
    else:
        df = pd.DataFrame(sorted_projects, columns=["Project Code", "Summary"])
        df["Rank"] = range(1, len(df) + 1)
        df.to_csv("submission.csv", index=False, mode='a', header=False)
        st.success("✅ Rankings submitted successfully! Thank you.")
