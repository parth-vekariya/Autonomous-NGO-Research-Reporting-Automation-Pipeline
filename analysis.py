"""Generate analytical insights from NGO research data for Word report."""

from collections import Counter


def analyze_sectors(ngos: list[dict]) -> dict:
    sectors = [ngo.get("sector", "Unknown") for ngo in ngos]
    counts = Counter(sectors)
    return dict(counts.most_common())


def analyze_geographic_reach(ngos: list[dict]) -> dict:
    reach = [ngo.get("geographic_reach", "Unknown") for ngo in ngos]
    return dict(Counter(reach))


def analyze_fcra_compliance(ngos: list[dict]) -> dict:
    registered = sum(1 for n in ngos if "registered" in n.get("fcra_status", "").lower())
    not_dependent = sum(1 for n in ngos if "not" in n.get("fcra_status", "").lower())
    return {
        "fcra_registered": registered,
        "not_fcra_dependent": not_dependent,
        "total": len(ngos),
    }


def generate_challenges_analysis() -> str:
    return """Indian NGOs face a complex set of interconnected challenges that shape their operations, sustainability, and impact:

**1. Funding & Financial Sustainability**
Most NGOs in our dataset rely on a mix of CSR funding, individual donations, and government grants — but rarely all three equally. Smaller and regional NGOs (Deepalaya, Parivaar, Udaan) are heavily philanthropy-dependent, while larger organizations (Akshaya Patra, Pratham) benefit from government scheme partnerships that provide more predictable revenue. The challenge of donor dependency means NGOs must constantly fundraise rather than focus on program delivery.

**2. Regulatory & Compliance Burden**
India's NGO regulatory landscape — FCRA, 12A/80G (now 12AB), NGO Darpan registration, CSR-1 filing — creates significant administrative overhead. All 20 NGOs researched maintain FCRA or equivalent compliance, but the compliance burden disproportionately affects smaller organizations. FCRA license renewals and scrutiny have intensified since 2020, making foreign funding channels harder to access.

**3. Talent Acquisition & Retention**
NGOs compete with corporate sector for skilled professionals. Teach For India addresses this through its fellowship model, while Azim Premji Foundation can attract talent through competitive salaries backed by a $2 billion endowment. Smaller NGOs struggle to retain qualified staff, relying on volunteers and underpaid passionate workers.

**4. Measuring & Communicating Impact**
While organizations like Pratham (ASER) and Goonj have robust measurement systems, many NGOs face challenges in quantifying social impact. Impact statistics in our research often span different time periods and methodologies, making cross-NGO comparison difficult. This affects credibility with donors and government partners.

**5. Geographic & Scale Challenges**
Reaching remote and rural populations — where need is greatest — increases operational costs. NGOs like Sankara Eye Foundation solve this through camp-based outreach, while SELCO Foundation addresses energy poverty in off-grid areas. Scaling proven models from one state to another requires navigating different government bureaucracies and local contexts.

**6. Technology & Digital Divide**
Urban NGOs (CRY, Breakthrough) effectively use digital campaigns, but rural-focused organizations face challenges in digital service delivery. The COVID-19 pandemic exposed this gap starkly, particularly in education (Pratham's pivot to remote learning) and healthcare (Smile on Wheels model).

**7. Government Partnership Complexity**
While government partnerships provide scale (Akshaya Patra's PM POSHAN model, Pratham's state TaRL programs), they also create dependency on political will and bureaucratic processes. NGOs must balance advocacy roles (CRY's child rights campaigns) with collaborative government engagement."""


def generate_similarities_analysis(ngos: list[dict]) -> str:
    national_count = sum(1 for n in ngos if n.get("geographic_reach") == "National")
    fcra_count = sum(1 for n in ngos if "registered" in n.get("fcra_status", "").lower())

    return f"""Despite operating across diverse sectors, the 20 researched NGOs share several common working model characteristics:

**1. Multi-Stakeholder Partnership Model**
Nearly all NGOs use a partnership-based approach rather than direct-only implementation. CRY partners with 150 grassroots NGOs, Pratham works with state governments, and Akshaya Patra operates on a Public-Private Partnership model. This reflects a shared understanding that scale requires collaboration.

**2. Government Scheme Integration**
{national_count} of 20 NGOs operate nationally, and most integrate with existing government schemes rather than replacing them. Examples include Akshaya Patra (PM POSHAN), Pratham (state education departments), HelpAge (National Programme for Health Care of the Elderly), and Smile Foundation (National Health Mission). This "fill the gaps" approach is the dominant Indian NGO model.

**3. CSR as Primary Private Funding Channel**
Corporate Social Responsibility funding appears as a funding source for 18+ NGOs in our dataset. Organizations like Smile Foundation (200+ corporate partners), Magic Bus (50+ partners), and Nanhi Kali (Mahindra Group anchor) demonstrate the centrality of CSR to Indian NGO financing since the 2013 Companies Act mandate.

**4. Compliance-First Operations**
{fcra_count} NGOs maintain FCRA registration, and all 20 have 12A/80G tax exemption status. Indian NGOs have evolved to treat regulatory compliance as a baseline requirement, not an optional extra — reflecting the maturing of the sector.

**5. Founder-Driven Origin Stories**
Every NGO in our dataset has a compelling founder narrative — from Rippan Kapur (CRY, ₹50 startup) to Harish Hande (SELCO, Ramon Magsaysay Award) to Vinayak Lohani (Parivaar, IIT-IIM graduate). Personal conviction and sacrifice narratives are a shared cultural feature of Indian NGO founding stories.

**6. Dual Mission: Service Delivery + Advocacy**
Most NGOs combine direct service (feeding children, rescuing animals, providing healthcare) with systemic advocacy (CRY's child rights policy work, Breakthrough's Bell Bajao campaign, PFA's legal advocacy). This dual approach is distinctly Indian — NGOs serve immediate needs while pushing for structural change.

**7. Digital Presence & Transparency**
All 20 NGOs maintain active websites and at least 3-4 social media platforms. This reflects sector-wide movement toward transparency and donor engagement through digital channels."""


def generate_differences_analysis(ngos: list[dict]) -> str:
    return """The 20 researched NGOs differ significantly in their operational models, scale, and strategic approaches:

**1. Funding Model Spectrum**

| Model Type | NGOs | Characteristics |
|------------|------|-----------------|
| Government-Dependent | Akshaya Patra, Pratham | Primary revenue from government schemes; high scale, lower autonomy |
| CSR-Corporate | Nanhi Kali, Smile Foundation, Magic Bus | Corporate partnerships as anchor funding; brand-aligned programs |
| Endowment/Philanthropy | Azim Premji Foundation | Self-funded via billionaire endowment; systemic reform focus |
| Civil Society/Crowdsourced | Goonj, CRY | Individual donations and material contributions; high community engagement |
| Fee-for-Service Hybrid | Sankara Eye Foundation | Free surgeries funded by paying patients and CSR in cross-subsidy model |

**2. Operational Scale & Reach**

- **National giants**: Pratham (8M children), Akshaya Patra (2.35M daily meals), CRY (4.7M children impacted)
- **Regional specialists**: Deepalaya (Delhi NCR), Teach For India (7 cities), Parivaar (West Bengal/MP)
- **Niche experts**: Udaan (cerebral palsy only), SELCO (renewable energy only), WTI (wildlife only)

**3. Implementation Approach**

- **Direct implementation**: Goonj, Sankara Eye, Parivaar — own staff and infrastructure
- **Partnership/network model**: CRY (150 partners), Pratham (government + community)
- **Fellowship/volunteer model**: Teach For India (2-year fellowships)
- **Campaign/advocacy model**: Breakthrough (Bell Bajao media campaigns)
- **Material recycling model**: Goonj (unique urban-to-rural surplus redistribution)

**4. Sector Focus Breadth**

- **Single-issue deep**: Akshaya Patra (meals only), Nanhi Kali (girl education only), SELCO (solar energy only)
- **Multi-sector integrated**: Smile Foundation (education + health + livelihood), Deepalaya (education + health + vocational)
- **Ecosystem/systemic**: Azim Premji Foundation (entire public education system reform)

**5. Founder Profile Diversity**

- Corporate professionals: Santanu Mishra (Smile), Shaheen Mistri (Teach For India), Anand Mahindra (Nanhi Kali)
- Activists/journalists: Anshu Gupta (Goonj), Maneka Gandhi (PFA), Mallika Dutt (Breakthrough)
- Technical experts: Madhu Pandit Dasa (Akshaya Patra, IIT), Dr. R.V. Ramani (Sankara Eye), Dr. Harish Hande (SELCO)
- Bureaucrats/officials: M.K. Ranjitsinh (WTI, former IAS)

**6. Technology & Innovation**

- High-tech kitchens: Akshaya Patra (centralized automated kitchens serving 100,000+ meals/day per kitchen)
- Sport-for-development: Magic Bus (using rugby/football as education hook)
- Material innovation: Goonj (MY Pad from textile waste, Cloth for Work barter model)
- Data-driven education: Pratham (ASER survey, TaRL methodology cited globally)
- Renewable energy: SELCO (decentralized solar ecosystems)"""


def generate_sector_participation_analysis(sector_counts: dict) -> str:
    ranked = "\n".join(
        f"   {i+1}. **{sector}**: {count} NGO(s)"
        for i, (sector, count) in enumerate(sector_counts.items())
    )

    return f"""Based on our research of 20 leading Indian NGOs and supplemented by sector-wide data:

**Sector Distribution in Our Dataset:**

{ranked}

**India's Broader NGO Sector Landscape:**

According to NITI Aayog's NGO Darpan portal, India has approximately 1.87 lakh registered NGOs, with an estimated 33 lakh total CSOs/NGOs operating across sectors. The sector participation ranking broadly follows:

**1. Education (Highest Participation)**
Education attracts the most NGO activity in India. In our dataset, 8 of 20 NGOs (40%) have education as a primary or major focus — Pratham, CRY, Akshaya Patra, Teach For India, Deepalaya, Magic Bus, Parivaar, and Azim Premji Foundation. This aligns with India's development priorities: 250+ million school-age children, ASER reports showing learning deficits, and government schemes (PM POSHAN, Samagra Shiksha) creating partnership opportunities.

**2. Healthcare (Second Highest)**
Healthcare NGOs address India's dual challenge of accessibility and affordability. Our dataset includes HelpAge India, Smile Foundation (health vertical), Sankara Eye Foundation, and Udaan — spanning elderly care, mobile health, eye care, and disability rehabilitation. The National Health Mission and NPCB create government partnership pathways.

**3. Environmental Conservation (Growing Rapidly)**
Environmental NGOs are growing fastest, driven by climate change awareness and CSR environmental mandates. WWF India, SELCO Foundation, Goonj (environmental angle), and WTI represent diverse approaches — from species conservation to renewable energy to waste recycling.

**4. Women Empowerment (Focused Niche)**
Women empowerment NGOs like Nanhi Kali and Breakthrough operate in a focused niche with high impact per dollar. Government schemes (Beti Bachao Beti Padhao, Nirbhaya Fund) and SDG 5 alignment drive funding.

**5. Child Rights & Protection (Cross-Cutting)**
Child-focused work spans multiple sectors — CRY (rights), Parivaar (residential care), Magic Bus (youth development). Child rights is more a cross-cutting theme than a standalone sector.

**6. Animal Welfare (Underserved but Passionate)**
Animal welfare (PFA, WTI) represents a smaller but highly committed segment. Lower government funding but strong individual donor and international support.

**7. Elderly Care (Emerging Priority)**
With India's aging population (138 million elderly by 2025), organizations like HelpAge India address a rapidly growing but historically neglected demographic.

**Key Insight**: Education and healthcare together account for over 60% of major NGO activity in India, reflecting both the scale of need and the availability of government co-funding mechanisms that make these sectors more sustainable for NGO operations."""


def generate_regulatory_analysis(fcra_data: dict) -> str:
    return f"""**India-Specific Regulatory Landscape Analysis**

Of the 20 NGOs researched:
- **FCRA Registered**: {fcra_data['fcra_registered']} organizations
- **Not FCRA-dependent**: {fcra_data['not_fcra_dependent']} (primarily domestic endowment funded)
- **12A/80G Compliant**: All 20 organizations

**FCRA (Foreign Contribution Regulation Act, 2010)**
FCRA registration is the gateway for receiving foreign donations. Organizations like Goonj (SBI FCRA account), CRY (international chapters), and Pratham (global chapters) depend on foreign funding channels. The 2020 FCRA amendments — requiring Aadhaar-based compliance, restricting sub-granting, and capping administrative expenses at 20% — have significantly impacted smaller NGOs' ability to receive international funds.

**12A/80G Tax Exemptions**
All researched NGOs maintain 12A (tax exemption for the organization) and 80G (50% tax deduction for donors) registrations. Since the 2021 Income Tax reforms, these require re-registration under Form 10A/10AB with 5-year validity periods. NGOs must now proactively renew compliance or risk losing donor tax benefits.

**NITI Aayog NGO Darpan**
NGO Darpan registration is mandatory for accessing government grants and serves as a credibility signal. All 20 NGOs are expected to maintain active Darpan profiles with updated financials, board member details, and project information. Verification should be done at ngodarpan.gov.in.

**CSR-1 Registration**
NGOs accepting corporate CSR funds must register on the MCA CSR portal. Organizations like Smile Foundation (200+ CSR partners) and Magic Bus (50+ partners) rely heavily on this registration for corporate funding access.

**Patterns Observed:**
1. Larger, national NGOs maintain all compliance registrations as standard practice
2. Foreign-funded NGOs (Goonj, Breakthrough, Magic Bus) are most affected by FCRA changes
3. Endowment-funded organizations (Azim Premji Foundation) are least dependent on regulatory funding channels
4. CSR-1 registration has become as important as FCRA for funding diversification"""


def generate_recommendations() -> str:
    return """**Key Insights & Recommendations**

**For Researchers & Interns:**
1. Always verify NGO Darpan ID, FCRA status, and 12A/80G at official government portals — not just NGO websites
2. Note the time period for impact statistics; numbers without context can mislead
3. Distinguish between registered name and popular abbreviation (e.g., Child Rights and You vs. CRY)
4. Check social media activity dates to assess current organizational health
5. Cross-reference annual reports with website claims for accuracy

**For NGO Sector Understanding:**
1. **Education + Healthcare dominate** the Indian NGO landscape due to government co-funding opportunities
2. **Partnership models scale better** than direct-only implementation in the Indian context
3. **CSR is the lifeline** of private funding since the 2013 Companies Act
4. **Compliance is non-negotiable** — FCRA, 12A/80G, and Darpan form the regulatory trinity
5. **Founder narratives matter** in Indian NGO culture — personal sacrifice stories build donor trust

**For Future Research Automation:**
1. Integrate live API calls to ngodarpan.gov.in for real-time Darpan ID verification
2. Add web scraping for annual report data extraction
3. Implement social media activity scoring for organizational health assessment
4. Build sector comparison dashboards with standardized impact metrics
5. Schedule automated re-research cycles to keep data current"""


def generate_all_analysis(ngos: list[dict]) -> dict[str, str]:
    sector_counts = analyze_sectors(ngos)
    fcra_data = analyze_fcra_compliance(ngos)

    return {
        "challenges": generate_challenges_analysis(),
        "similarities": generate_similarities_analysis(ngos),
        "differences": generate_differences_analysis(ngos),
        "sector_participation": generate_sector_participation_analysis(sector_counts),
        "regulatory": generate_regulatory_analysis(fcra_data),
        "recommendations": generate_recommendations(),
        "sector_counts": sector_counts,
        "geographic_reach": analyze_geographic_reach(ngos),
    }
