"""
Web Research Agent Module
=========================
Extensible module for automated NGO data retrieval from internet sources.

Integrate with Cursor Agent, web search APIs, or scraping tools to populate
the JSON database automatically before running the export pipeline.
"""

import json
from pathlib import Path
from typing import Optional

# Research sources to query per NGO field
RESEARCH_SOURCES = {
    "official_website": "Primary source for mission, vision, programs, contact",
    "wikipedia": "Founding year, founders, history, impact overview",
    "ngodarpan.gov.in": "FCRA status, 12A/80G, Darpan ID, government grants",
    "linkedin": "Organization size, employee count, headquarters",
    "annual_reports": "Impact statistics, funding sources, partnerships",
    "news_media": "Awards, media coverage, recent activity",
    "guidestarindia.org": "Credibility ratings, financial transparency",
}

# Search query templates for each data field
SEARCH_TEMPLATES = {
    "founding": "{ngo_name} India founded year founder history",
    "programs": "{ngo_name} India key programs projects initiatives",
    "impact": "{ngo_name} India impact statistics beneficiaries",
    "compliance": "{ngo_name} FCRA 12A 80G NGO Darpan registration India",
    "partnerships": "{ngo_name} CSR partners government collaboration India",
    "awards": "{ngo_name} awards recognition media coverage India",
    "contact": "{ngo_name} registered office address phone email India",
}


def generate_research_queries(ngo_name: str) -> dict[str, str]:
    """Generate search queries for all data fields of an NGO."""
    return {
        field: template.format(ngo_name=ngo_name)
        for field, template in SEARCH_TEMPLATES.items()
    }


def get_seed_ngo_list() -> list[dict]:
    """Default list of 20 NGOs to research, organized by sector."""
    return [
        {"name": "Child Rights and You", "short": "CRY", "sector": "Child Rights"},
        {"name": "Goonj", "short": "Goonj", "sector": "Rural Development"},
        {"name": "Pratham Education Foundation", "short": "Pratham", "sector": "Education"},
        {"name": "The Akshaya Patra Foundation", "short": "Akshaya Patra", "sector": "Education/Nutrition"},
        {"name": "HelpAge India", "short": "HelpAge", "sector": "Elderly Care"},
        {"name": "Smile Foundation", "short": "Smile", "sector": "Healthcare/Education"},
        {"name": "Wildlife Trust of India", "short": "WTI", "sector": "Animal Welfare"},
        {"name": "People for Animals", "short": "PFA", "sector": "Animal Welfare"},
        {"name": "Nanhi Kali", "short": "Nanhi Kali", "sector": "Women Empowerment"},
        {"name": "Breakthrough Trust", "short": "Breakthrough", "sector": "Women Empowerment"},
        {"name": "Teach For India", "short": "TFI", "sector": "Education"},
        {"name": "Sankara Eye Foundation India", "short": "Sankara Eye", "sector": "Healthcare"},
        {"name": "SELCO Foundation", "short": "SELCO", "sector": "Environment/Energy"},
        {"name": "WWF-India", "short": "WWF India", "sector": "Environmental Conservation"},
        {"name": "Udaan Welfare Foundation", "short": "Udaan", "sector": "Healthcare"},
        {"name": "Deepalaya", "short": "Deepalaya", "sector": "Education"},
        {"name": "Magic Bus India Foundation", "short": "Magic Bus", "sector": "Youth Development"},
        {"name": "Parivaar Education Society", "short": "Parivaar", "sector": "Child Welfare"},
        {"name": "Azim Premji Foundation", "short": "APF", "sector": "Education"},
        {"name": "CARE India", "short": "CARE India", "sector": "Healthcare/Disaster Relief"},
    ]


def create_empty_ngo_template(seed: dict) -> dict:
    """Create an empty NGO record from a seed entry for research population."""
    return {
        "sector": seed.get("sector", ""),
        "full_official_name": seed.get("name", ""),
        "short_name": seed.get("short", ""),
        "founding_year": "",
        "founding_context": "",
        "founder_names": "",
        "founder_background": "",
        "mission": "",
        "vision": "",
        "focus_scope": "",
        "programs": [],
        "states_districts": "",
        "geographic_reach": "",
        "website": "",
        "facebook": "",
        "instagram": "",
        "twitter_x": "",
        "linkedin": "",
        "youtube": "",
        "impact_stats": [],
        "registered_office": "",
        "phone": "",
        "email": "",
        "government_grants": "",
        "csr_funding": "",
        "international_donors": "",
        "fcra_status": "",
        "tax_exemption": "",
        "darpan_id": "",
        "government_tieups": "",
        "corporate_csr_partners": "",
        "international_affiliations": "",
        "awards": "",
        "media_coverage": "",
        "credibility_ratings": "",
        "_research_queries": generate_research_queries(seed.get("name", "")),
    }


def initialize_research_database(output_path: Optional[Path] = None) -> Path:
    """Create a blank research database with search queries for AI agent population."""
    seeds = get_seed_ngo_list()
    database = [create_empty_ngo_template(seed) for seed in seeds]

    if output_path is None:
        output_path = Path(__file__).parent.parent / "data" / "ngos_research_pending.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    return output_path


if __name__ == "__main__":
    path = initialize_research_database()
    print(f"Research template created: {path}")
    print(f"NGOs to research: {len(get_seed_ngo_list())}")
    print("\nNext steps:")
    print("  1. Use AI agent with web search to populate each NGO's fields")
    print("  2. Save completed data to data/ngos_database.json")
    print("  3. Run: python src/main.py")
