# NLB KOSOVO: BRANCH NETWORK STRATEGIC DIAGNOSTIC & OPTIMIZATION BLUEPRINT

**Prepared for: Group CEO and CFO**
**Date: March 2026**
**Classification: Confidential - Board Level**

---

# PRELIMINARY STEPS: EVIDENCE MAPPING AND METHODOLOGY

---

## STEP 1 - FILE INVENTORY

| # | File | Location | Status |
|---|------|----------|--------|
| 1 | Branch Productivity.xlsx | Branch Productivity\ | Fully parsed - 19 sheets covering PI clients, business clients, digital penetration, loans, deposits, cards, POS |
| 2 | Kosovo_Banking_Intelligence_v4.html | BQK\ | HTML dashboard - banking system structure, market shares, payment trends |
| 3 | index.html (Banking System BI) | Banking System BI\ | BI dashboard with system-level data |
| 4 | economic_intelligence.html | ASKdata\ | Macro-economic dashboard by municipality |
| 5 | Vende-Pune-2025 (1).xlsx | Branch Productivity\ | ATK employment/workplaces data - complex report format, partially parseable |
| 6 | Pagesat-Periudhore-2025.xlsx | Branch Productivity\ | ATK periodic payments by municipality - large dataset |
| 7 | Deklarimi-2025 (1).xlsx | Branch Productivity\ | ATK tax declarations data - large dataset |
| 8 | Qarkullimi-2025 (1).xlsx | Branch Productivity\ | ATK turnover/revenue data by municipality - large dataset |
| 9 | Market share February 2025 - trend.xlsx | Banking System BI\ | Market share (EUR and %), P&L, Balance Sheet for all 10 Kosovo banks |
| 10 | ASK data files (01-10) | ASKdata\ / ASK\ | Demographics, labor, wages, business enterprise, GDP, trade, housing |
| 11 | CBK data files | BQK\ | Central bank time series: loans, deposits, interest rates, payments, external sector |
| 12 | Economic Intelligence ATK files | ASKdata\ | Formal economy indicators by municipality |

---

## STEP 2 - ROLE OF EACH FILE

### Branch Productivity.xlsx - PRIMARY EVIDENCE
**Type:** Internal bank data - branch-level client counts, product penetration, digital adoption
**Analytical Role:** Core of branch performance analysis. Provides client numbers (PI and Business), product counts (CA, SA, TDA, Mortgages, Consumer Loans, Credit Cards, Overdrafts), digital banking adoption (M-Banking, E-Banking), and POS terminal counts per branch. Contains both 2025 and 2026 data enabling YoY growth analysis.
**Can support:** Client penetration analysis, product cross-sell assessment, digital migration measurement, branch growth comparison, market penetration vs. population
**Cannot support:** Revenue per branch, costs per branch, profitability per branch, staffing levels, transaction volumes, balance sheet per branch (EUR amounts)

### Market Share February 2025 - trend.xlsx - COMPETITIVE POSITIONING
**Type:** Central bank regulatory data - all 10 Kosovo banks
**Analytical Role:** NLB's competitive position across assets, loans (corporate, SME, micro, retail, mortgage, consumer), deposits (corporate, retail), and profitability metrics
**Can support:** Market share analysis, competitive intensity assessment, NLB's strategic positioning
**Cannot support:** Branch-level competitive data, competitor branch locations

### ATK Files (Qarkullimi, Deklarimi, Vende-Pune, Pagesat) - TERRITORY POTENTIAL
**Type:** Tax administration data - formal economy indicators by municipality
**Analytical Role:** Proxy for local economic activity, business formalization, employment density, salary mass
**Limitation:** Complex report formatting made automated parsing incomplete. Used where extractable; otherwise supplemented with ASK demographic data.

### ASK Data Files - DEMOGRAPHIC & ECONOMIC CONTEXT
**Type:** Kosovo Agency of Statistics data
**Analytical Role:** Population structure, labor market, wages, business counts, GDP contribution by sector
**Can support:** Market sizing by municipality, income profiling, employment structure assessment

### CBK/BQK Data - BANKING SYSTEM TRENDS
**Type:** Central bank financial data and payment statistics
**Analytical Role:** System-level trends in lending, deposits, payments, interest rates, digital adoption
**Can support:** Macro trend identification, sector benchmarking

---

## STEP 3 - DATA GAPS AND LIMITATIONS

### CRITICAL MISSING DATA

| Gap | Impact | Workaround Used |
|-----|--------|-----------------|
| **Branch-level P&L** (revenue, costs, profit) | Cannot compute true branch profitability | Used product counts and loan volumes as revenue proxies; cross-sell intensity as productivity proxy |
| **Staffing per branch** (headcount, roles, FTE) | Cannot compute per-employee productivity | Used client-per-branch ratios and product density as efficiency proxies |
| **Branch-level EUR balances** (loan book, deposit book) | Cannot compute balance sheet contribution | Used loan/deposit counts as directional indicators |
| **Transaction volumes per branch** | Cannot measure operational load vs. digital migration | Used digital penetration rates as proxy for teller demand reduction potential |
| **Competitor branch map** | Cannot assess competitive pressure at branch level | Used overall market share position and business density as proxies |
| **Branch physical characteristics** (size, format, age) | Cannot assess format fit | Made inferences from product mix and client volumes |
| **Customer satisfaction / NPS per branch** | Cannot assess service quality dimension | Not addressed - flagged as data requirement |

### DATA QUALITY ISSUES

1. **ATK Files:** Complex merged-cell report formatting prevented clean automated parsing. Municipality-level turnover, employment, and declaration data is available but not fully integrated. **Impact:** Territory potential assessment relies more heavily on population/business counts than on economic activity intensity.

2. **Branch-Territory Mapping:** The "Total" sheet maps branches to municipalities, but some branches serve wider catchment areas (e.g., Mitrovicë Veriore shows 135% penetration of local population, indicating it serves surrounding Serb-majority municipalities). **Impact:** Penetration ratios for some branches are inflated relative to their nominal municipality.

3. **Time Period:** Branch data compares 2025 vs. 2026 (current). Market share data is as of February 2025. Minor misalignment but directionally consistent.

4. **Product Counts vs. Values:** All branch data is in NUMBER of products/clients, not EUR volumes. A branch with 100 mortgages could have EUR 5M or EUR 15M depending on average ticket size. **Impact:** All productivity comparisons are COUNT-based, not VALUE-based.

5. **TDA Data Anomaly:** TDA (Time Deposit) counts dropped 43% YoY system-wide, from 15,274 to 8,647. This likely reflects a strategic product shift (toward Savings Accounts, which grew 122%) rather than genuine client attrition. Must be interpreted in context.

---

## STEP 4 - ANALYTICAL METHODOLOGY

### Framework: Five-Dimensional Branch Assessment

Each branch is evaluated across five dimensions, each scored on available data:

**1. Market Penetration Index (MPI)**
- PI Client Penetration = Active PI Clients / Population >15
- Business Client Penetration = Active Business Clients / Registered Businesses
- Benchmarked against network average (18.5% PI, 16.9% Business)
- Classification: Under-penetrated (<15%), Average (15-25%), Well-penetrated (>25%)

**2. Product Intensity Score (PIS)**
- Total active products per client (CA + SA + TDA + Mortgages + Consumer + CC + OVD) / Active Clients
- Loan penetration = (Mortgage + Consumer) / Active Clients
- Credit card penetration = CC / Active Clients
- Benchmarked against network averages

**3. Digital Maturity Index (DMI)**
- M-Banking adoption rate (% of active clients)
- E-Banking adoption rate
- Business digital adoption rate
- Network average: PI M-Banking 46.5%, Business M-Banking 80.2%

**4. Growth Momentum Score (GMS)**
- YoY PI client growth rate
- YoY Business client growth rate
- Comparison to population growth and business registration trends

**5. Territory Potential Score (TPS)**
- Population size and density
- Number of registered businesses
- Business-to-population ratio (economic activity proxy)
- Served vs. unserved municipality assessment

### Branch Segmentation Logic
Branches are classified into archetypes based on the combination of these five scores:
- **Star Branches:** High penetration + High growth + High product intensity
- **Growth Engines:** Lower penetration + High territory potential + Above-average growth
- **Cash Cows:** High penetration + Mature market + Stable performance
- **Digital Leaders:** High digital adoption + Opportunity to reduce physical footprint
- **Underperformers:** Below-average on multiple dimensions relative to territory potential
- **Structural Outliers:** Unique market conditions requiring special strategy (e.g., Serb-majority areas)

### Fact vs. Inference Labeling
Throughout this report:
- **[DATA]** = directly supported by uploaded file data
- **[INFERENCE]** = logical deduction from available data
- **[HYPOTHESIS]** = strategic reasoning requiring validation with additional data

---

# PART 1 - EXECUTIVE SUMMARY

---

## The Headline

NLB Kosovo operates 27 active branches (+2 nascent) serving 240,157 PI clients and 13,169 business clients across a market of 1.6 million people and 77,712 registered businesses. **NLB reaches only 18.5% of the adult population and 16.9% of businesses** - leaving substantial room for growth, particularly in territories where it already has physical presence but hasn't converted market potential into client relationships.

## Five Biggest Findings

### 1. Massive Penetration Variance Signals Both Excellence and Neglect [DATA]
Branch PI penetration ranges from 4.6% (Leposaviq) to 135% (Mitrovicë Veriore). Among established branches, the gap between top performers (Hani i Elezit at 53%, Deçan at 34%, Shtërpcë at 33%) and laggards (Fushë Kosovë at 13.3%, Malishevë at 13.6%, Prizren at 14.0%) is enormous. **Prizren - Kosovo's second-largest city with 147,000 people - has the same penetration rate as a village of 9,000**. This is the single most important finding in this analysis.

### 2. Digital Migration Is Real but Unevenly Distributed [DATA]
Network-wide, 46.5% of PI clients use M-Banking and 80.2% of business clients are digitally active. But the range is stark: Prishtinë leads at 62.4% M-Banking vs. Shtërpcë at 27.2%. **Branches below 35% M-Banking adoption (Shtërpcë, Mitrovicë Veriore, Rahovec, Skenderaj) are likely carrying excessive teller workloads that could be partly migrated digitally** - freeing staff for sales and advisory functions.

### 3. Product Cross-Sell Is Shallow Outside Prishtinë [INFERENCE]
Prishtinë accounts for 19.8% of all clients but disproportionately dominates mortgages (36.1% of all mortgage loans), credit cards (24.9%), and savings accounts (31.2%). Most regional branches show weak cross-sell: clients have a current account and possibly one loan, with minimal card, savings, or investment product penetration. **The revenue per client in regional branches is almost certainly far below Prishtinë**.

### 4. Business Banking Is Underdeveloped in Major Markets [DATA]
NLB serves only 16.9% of registered businesses. In major markets: Gjakovë 10.8%, Gjilan 10.6%, Prizren 12.7%, Ferizaj 11.4%. **These four cities alone represent 21,812 businesses, of which NLB serves only 2,521 - leaving approximately 19,291 unserved businesses in markets where NLB has established branches**.

### 5. Savings Account Explosion Is a Strategic Opportunity [DATA]
Savings accounts grew from 13,791 to 30,615 (up 122% YoY) while TDA dropped from 15,274 to 8,647 (down 43%). This isn't attrition - it's migration. Clients are moving from locked term deposits to more liquid savings. **This shift, if managed well, could strengthen NLB's funding base while improving client engagement**. If managed poorly, it signals rate sensitivity and potential outflow risk.

## Biggest Hidden Opportunities

1. **Prizren**: 147,000 people, 7,119 businesses, only 14% PI penetration. [DATA] This is NLB's largest single under-penetration gap. A focused 3-year campaign could realistically add 8,000-12,000 clients.

2. **Gjakovë**: 78,700 people, 4,005 businesses, only 14% PI penetration and 10.8% business penetration. [DATA] Similar profile to Prizren.

3. **Business banking nationally**: Only 16.9% penetration against 77,712 businesses. [DATA] Every 1 percentage point of business penetration gain = ~777 new business clients, each worth multiples of a PI client in revenue.

4. **Digital migration in 8 low-adoption branches** (below 40% M-Banking): Can potentially redeploy 15-25% of teller capacity toward sales if digital adoption is driven up. [HYPOTHESIS]

5. **Unserved municipalities**: Dragash (28,896 pop, 652 businesses) and Shtime (24,308 pop, 802 businesses) represent the most attractive expansion candidates among municipalities without NLB presence. [INFERENCE]

## Key Strategic Recommendations (Preview)

1. **Launch "Prizren Offensive"** - dedicated commercial push to close the penetration gap in Kosovo's second city
2. **Business Banking Acceleration** - target 20% business penetration within 24 months (from 16.9%)
3. **Digital Migration Program** - bring all branches above 50% M-Banking within 12 months
4. **Workforce Rebalancing** - shift teller capacity toward sales/advisory in digitally mature branches
5. **Light-Format Expansion** - open service points in Dragash and Shtime
6. **Product Cross-Sell Initiative** - structured program to increase products-per-client in regional branches
7. **Savings Product Strategy** - capitalize on SA growth momentum with tiered savings and goal-based products

## Likely Upside
**[HYPOTHESIS - requires validation with EUR balance data]**
- Closing the Prizren/Gjakovë penetration gap alone could add 15,000-20,000 PI clients
- Raising business penetration by 3pp = ~2,330 new business clients
- Conservative estimate: 10-15% revenue growth achievable from network optimization without new branch investment
- Digital migration-driven workforce reallocation could improve cost-to-income by 2-4pp

## Major Risks and Constraints
- **Missing profitability data** means recommendations are based on volume/penetration logic, not margin analysis. Some branches may be unprofitable for reasons not visible in count data.
- **Staffing data absence** means workforce recommendations are directional, not prescriptive.
- **Competitor response** is not modeled - aggressive NLB moves may trigger competitive reactions.
- **Macro risk**: Kosovo's economic growth, while solid, depends on remittances, diaspora investment, and EU integration progress.

---

# PART 2 - DIAGNOSTIC FRAMEWORK

---

## Branch Performance Assessment Matrix

The framework evaluates each branch on five dimensions. Each metric is calculated from available data and compared to the network average.

### Dimension 1: Market Penetration

| Metric | Formula | Network Average | Top Quartile | Bottom Quartile |
|--------|---------|-----------------|--------------|-----------------|
| PI Penetration | Active PI / Pop >15 | 19.2% | >25% | <15% |
| Business Penetration | Active Biz / Registered Biz | 16.9% | >22% | <12% |
| Client Growth | YoY PI growth % | 3.9% | >5% | <2% |
| Business Growth | YoY Biz growth % | 2.2% | >5% | <0% |

### Dimension 2: Product Intensity

| Metric | Formula | Network Average |
|--------|---------|-----------------|
| Mortgage Penetration | Mortgage Loans / Active PI | 3.9% |
| Consumer Loan Penetration | Consumer Loans / Active PI | 11.3% |
| Credit Card Penetration | (CC + OVD) / Active PI | 5.8% |
| Savings Penetration | SA / Active PI | 12.7% (2026, post-growth) |
| Deposit Mix | TDA / (CA + SA + TDA) | Declining |

### Dimension 3: Digital Maturity

| Metric | Formula | Network Average |
|--------|---------|-----------------|
| PI M-Banking | M-click / Active PI | 46.5% |
| PI E-Banking | E-click / Active PI | 6.8% |
| Business M-Banking | M-click Biz / Active Biz | 80.2% |
| Business E-Banking | E-click Biz / Active Biz | 56.3% |

### Dimension 4: Growth Momentum

| Metric | Measurement |
|--------|-------------|
| PI Client Growth | Absolute and % YoY |
| Business Client Growth | Absolute and % YoY |
| SA Product Growth | As indicator of engagement trend |
| Loan Growth | Consumer + Mortgage YoY |

### Dimension 5: Territory Potential

| Metric | Measurement |
|--------|-------------|
| Population >15 | Market size |
| Registered Businesses | Commercial opportunity |
| Business Density | Businesses per 1,000 pop (economic vitality proxy) |
| Untapped PI Headroom | (Pop>15 * Target Penetration) - Current Clients |
| Untapped Biz Headroom | (Reg Biz * Target Penetration) - Current Biz Clients |

---

# PART 3 - BRANCH SEGMENTATION

---

## Segmentation Results

Based on the five-dimensional analysis, NLB's 27 active branches fall into six distinct archetypes:

### SEGMENT 1: DOMINANT HUB (1 branch)
**Prishtinë**

| Metric | Value | vs. Network |
|--------|-------|-------------|
| PI Clients | 47,635 | 19.8% of all NLB clients |
| Business Clients | 4,216 | 32.0% of all NLB business clients |
| PI Penetration | 26.9% | Above average |
| Biz Penetration | 19.7% | Above average |
| M-Banking PI | 62.4% | Highest in network |
| Mortgages | 3,386 | 36.1% of network total |
| Consumer Loans | 7,665 | 28.1% of network total |
| YoY PI Growth | +2,215 | 24.5% of all net new clients |

**Diagnosis:** Prishtinë is the crown jewel - highest digital maturity, deepest product penetration, dominant market position. However, concentration risk is real: nearly 1 in 5 NLB clients sits in one branch. Prishtinë is also the hardest market to grow further due to fierce competition from all 10 banks.

**Strategic Role:** Protect, deepen, and innovate. This is the benchmark branch for product intensity and digital adoption.

---

### SEGMENT 2: MAJOR MARKET UNDERPERFORMERS (4 branches)
**Prizren, Ferizaj, Gjakovë, Gjilan**

These are Kosovo's largest cities after Prishtinë, with combined population of 418,180 and 21,812 businesses. Yet their performance is disproportionately weak:

| Branch | Pop >15 | PI Clients | PI Penetration | Biz Penetration | M-Bank% |
|--------|---------|------------|----------------|-----------------|---------|
| Prizren | 115,421 | 16,152 | 14.0% | 12.7% | 37.0% |
| Ferizaj | 84,228 | 13,576 | 16.1% | 11.4% | 46.3% |
| Gjakovë | 62,970 | 8,812 | 14.0% | 10.8% | 37.6% |
| Gjilan | 66,517 | 11,535 | 17.3% | 10.6% | 48.3% |
| **Average** | | | **15.4%** | **11.4%** | **42.3%** |
| **Network Avg** | | | **19.2%** | **16.9%** | **46.5%** |

**Diagnosis:** All four are below network average on both PI and Business penetration. Prizren and Gjakovë also lag on digital adoption. **These branches are not weak because their markets are weak - they are weak because they have not captured their market potential.** [INFERENCE: this could be due to insufficient staffing, wrong branch format, weak local management, or competitive pressure from better-positioned rivals]

**Strategic Role:** Aggressive growth targets. These represent NLB's biggest organic growth opportunity by far.

**Quantified Opportunity:**
If these four branches were brought to just the network average penetration of 19.2%:
- Prizren: 22,161 PI clients needed (gap of +6,009)
- Ferizaj: 16,172 needed (gap of +2,596)
- Gjakovë: 12,090 needed (gap of +3,278)
- Gjilan: 12,771 needed (gap of +1,236)
- **Total potential: +13,119 additional PI clients** [INFERENCE]

---

### SEGMENT 3: STRONG REGIONAL PERFORMERS (7 branches)
**Pejë, Mitrovicë, Gllogoc, Podujevë, Kaçanik, Deçan, Obiliq**

These branches show above-average penetration in their markets:

| Branch | Pop >15 | PI Penetration | Biz Penetration | M-Bank% | YoY Growth |
|--------|---------|----------------|-----------------|---------|------------|
| Deçan | 22,138 | 34.0% | 36.9% | 51.7% | +155 |
| Kaçanik | 21,269 | 28.0% | 35.0% | 49.6% | +217 |
| Pejë | 65,980 | 22.8% | 16.7% | 43.6% | +476 |
| Obiliq | 17,367 | 23.8% | 18.2% | 45.1% | +181 |
| Gllogoc | 36,276 | 24.3% | 21.8% | 49.5% | +315 |
| Mitrovicë | 50,171 | 23.7% | 16.9% | 35.7% | +62 |
| Podujevë | 54,812 | 19.5% | 14.7% | 43.7% | +578 |

**Diagnosis:** These branches have achieved solid market positions. Deçan and Kaçanik are notably strong with 34% and 28% PI penetration respectively. Pejë is an important regional hub. Mitrovicë shows high penetration but very low growth (+62 clients YoY) suggesting it may be reaching saturation or losing momentum. Podujevë shows strong growth momentum (+578 YoY).

**Strategic Role:** Defend market position, optimize product mix, push digital migration (especially Mitrovicë at 35.7% M-Banking).

---

### SEGMENT 4: MODERATE PERFORMERS WITH GROWTH POTENTIAL (8 branches)
**Fushë Kosovë, Vushtrri, Lipjan, Suharekë, Malishevë, Istog, Klinë, Viti**

| Branch | Pop >15 | PI Penetration | Biz Penetration | M-Bank% | YoY Growth |
|--------|---------|----------------|-----------------|---------|------------|
| Fushë Kosovë | 47,439 | 13.3% | 19.6% | 56.0% | +240 |
| Vushtrri | 47,591 | 13.7% | 11.3% | 37.6% | +235 |
| Lipjan | 41,804 | 14.2% | 18.8% | 41.5% | +234 |
| Suharekë | 36,111 | 16.4% | 16.6% | 38.5% | +285 |
| Istog | 26,385 | 19.4% | 22.2% | 48.2% | +261 |
| Malishevë | 32,516 | 13.6% | 22.0% | 50.2% | +266 |
| Klinë | 23,708 | 18.2% | 26.3% | 46.5% | +87 |
| Viti | 27,813 | 18.5% | 16.9% | 45.4% | +193 |

**Diagnosis:** Mixed bag. Fushë Kosovë is notable: very low PI penetration (13.3%) despite high digital maturity (56.0% M-Banking) and decent business penetration. This suggests the branch may have an operationally savvy client base but hasn't expanded its retail franchise. Malishevë shows an interesting split: low PI penetration (13.6%) but high business penetration (22.0%) - suggesting it's more of a commercial town. Klinë has the highest business penetration in this group (26.3%) but slow growth.

**Strategic Role:** Targeted PI acquisition campaigns; business deepening in Vushtrri and Viti where business penetration is low.

---

### SEGMENT 5: STRUCTURAL OUTLIERS - SERB-MAJORITY MARKETS (4 branches)
**Mitrovicë Veriore, Graçanicë, Shtërpcë, Leposaviq/Zubin Potok**

| Branch | Pop >15 | PI Clients | PI Penetration | Biz Penetration | M-Bank% |
|--------|---------|------------|----------------|-----------------|---------|
| Mit. Veriore | 6,833 | 9,261 | 135.5% | 98.7% | 30.8% |
| Graçanicë | 14,806 | 3,691 | 24.9% | 10.7% | 28.7% |
| Shtërpcë | 9,026 | 2,976 | 33.0% | 37.2% | 27.2% |
| Leposaviq | 8,435 | 389 | 4.6% | 29.4% | 48.1% |
| Zubin Potok | 2,940 | 184 | 6.3% | 28.0% | - |

**Diagnosis:** These require separate strategic treatment.

- **Mitrovicë Veriore** is an outlier in every sense: 135% PI penetration (serves clients from surrounding municipalities including Zveçan, Zubin Potok, and potentially northern Kosovo broadly), 98.7% business penetration, but only 30.8% M-Banking. [DATA] This branch appears to be NLB's dominant gateway to the Serb community in northern Kosovo. Its market position is extraordinary and strategically valuable. Low digital adoption likely reflects demographic/preference factors.

- **Graçanicë** shows high penetration but very low digital adoption (28.7%) and low business penetration (10.7%). [DATA]

- **Shtërpcë** has the lowest M-Banking adoption in the network (27.2%) and is small. [DATA]

- **Leposaviq and Zubin Potok** are nascent - Leposaviq has only 389 PI clients and Zubin Potok 184. These are recent market entries. [DATA]

**Strategic Role:** Protect and serve with adapted model. Do NOT apply standard commercial targets. These markets have unique political, demographic, and linguistic dynamics. Focus on service quality and steady organic growth. Mitrovicë Veriore needs investment in digital adoption and possibly branch modernization given its critical role.

---

### SEGMENT 6: SMALL-MARKET DEFENDERS (3 branches)
**Kamenicë, Rahovec, Skenderaj**

| Branch | Pop >15 | PI Penetration | Biz Penetration | M-Bank% | YoY Growth |
|--------|---------|----------------|-----------------|---------|------------|
| Rahovec | 32,724 | 16.8% | 11.8% | 33.8% | +156 |
| Skenderaj | 31,671 | 19.2% | 23.4% | 34.9% | +301 |
| Kamenicë | 19,137 | 16.9% | 14.3% | 45.8% | +181 |

**Diagnosis:** Mid-size branches in less dynamic markets. Rahovec and Skenderaj show notably low digital adoption (<35% M-Banking), meaning their branches likely handle a high proportion of routine transactions manually. Skenderaj shows decent growth and good business penetration but needs digital push.

**Strategic Role:** Drive digital migration aggressively. Evaluate whether teller-heavy staffing can be reduced as digital adoption rises. Consider light-format conversion for the lowest-volume branches if economics warrant.

---

### SEGMENT 7: SMALL SPECIALIZED BRANCHES (2 branches)
**Hani i Elezit, Graçanicë (already categorized above)**

**Hani i Elezit** deserves special mention:

| Metric | Value | Commentary |
|--------|-------|------------|
| Population | 8,533 | Very small municipality |
| PI Penetration | 53.1% | Second highest in network |
| Biz Penetration | 67.7% | Second highest in network |
| M-Banking | 56.2% | Above network average |
| YoY Growth | +269 | Very strong for size |
| Consumer Loans | 522 | High relative to client base |

**Diagnosis:** Hani i Elezit is a border town (Turkey/North Macedonia border crossing) with disproportionately high NLB penetration and strong economics. [DATA] The high consumer loan count relative to clients (15.2% of active PI have consumer loans vs. network average of 11.3%) suggests an active lending market. [INFERENCE: border towns often have trade-related cash flows and remittance activity that drive banking demand beyond what population alone would suggest.]

---

## BRANCH SEGMENTATION SUMMARY TABLE

| Segment | Branches | Total PI Clients | % of Network | Priority Action |
|---------|----------|-----------------|--------------|-----------------|
| Dominant Hub | 1 (Prishtinë) | 47,635 | 19.8% | Protect, deepen, innovate |
| Major Market Underperformers | 4 | 50,075 | 20.8% | **Aggressive growth** |
| Strong Regional Performers | 7 | 58,514 | 24.4% | Defend, optimize |
| Moderate w/ Growth Potential | 8 | 42,383 | 17.6% | Targeted campaigns |
| Structural Outliers | 5 | 16,501 | 6.9% | Adapted model |
| Small-Market Defenders | 3 | 14,740 | 6.1% | Digital migration |
| Small Specialized | 1 (Hani i Elezit) | 3,424 | 1.4% | Maintain excellence |
| **Unserved Municipalities** | **9** | **0** | **0%** | **Evaluate expansion** |

---

# PART 4 - BRANCH-BY-BRANCH ANALYSIS

---

## 1. PRISHTINË (Branch 0001) - DOMINANT HUB

**Current Profile:**
- Population served: 227,466 (Pop >15: 177,302)
- Registered businesses: 21,396
- Active PI clients: 47,635 (2026), up from 45,420 (+4.9% YoY)
- Active Business clients: 4,216, up from 4,168 (+1.2% YoY)
- Products: 5,268 CA | 9,546 SA | 2,444 TDA | 3,386 Mortgages | 7,665 Consumer | 7,458 CC+OVD
- Digital: 62.4% M-Banking | 11.3% E-Banking (PI) | 79.4% M-Banking (Biz)
- POS terminals: 1,705

**Strengths:**
- Highest absolute client volume and product depth in network
- Highest PI M-Banking adoption (62.4%)
- Dominates mortgage lending (36.1% of network) and consumer lending (28.1%)
- Strong POS network (44.6% of all network POS terminals)
- Diversified client mix (PI + Micro + CIB)

**Weaknesses:**
- PI penetration at 26.9% means 73% of adult population is not NLB client [DATA]
- Business penetration only 19.7% - 17,180 unserved businesses [DATA]
- YoY business growth sluggish (+48 net new = +1.2%) [DATA]
- E-Banking still only 11.3% - room for desktop/online growth [DATA]

**Market Context:**
Prishtinë is Kosovo's capital and economic center, with the highest concentration of government, corporate, and service sector activity. All 10 banks compete aggressively here. [INFERENCE: marginal client acquisition is expensive and competitive, but the absolute market size justifies continued investment.]

**Digital Opportunity:** HIGH - already leading, but can push E-Banking and reduce routine transactions further. Target: 70% M-Banking, 20% E-Banking within 12 months.

**Product Mix:** Well-balanced but should increase SA cross-sell (already strong at 9,546) and push investment/wealth products to affluent segment. [HYPOTHESIS: Prishtinë likely has the highest concentration of affluent clients needing wealth management services.]

**Growth Opportunity:**
- Business acquisition: +2,000 new business clients over 24 months (target: 22% penetration)
- PI deepening: focus on product cross-sell rather than client acquisition
- Card activation: 7,458 CC+OVD is strong but activation/usage rates unknown

**Recommended Actions:**
1. Shift branch model toward advisory/relationship management, away from transactions
2. Launch affluent/private banking proposition
3. Dedicated SME acquisition team
4. Push E-Banking to 20% through payroll partnership campaigns
5. Evaluate sub-branch or service point in underserved Prishtinë neighborhoods

---

## 2. PRIZREN (Branch 1005) - CRITICAL UNDERPERFORMER

**Current Profile:**
- Population: 147,246 (Pop >15: 115,421) - Kosovo's 2nd largest city
- Registered businesses: 7,119
- Active PI: 16,152 (up from 15,388, +5.0% YoY)
- Active Business: 905 (down from 945, -4.2% YoY) [DATA - LOSING BUSINESS CLIENTS]
- Products: 1,027 CA | 1,743 SA | 811 TDA | 427 Mortgages | 1,382 Consumer | 1,062 CC+OVD
- Digital: 37.0% M-Banking | 3.9% E-Banking (PI) | 68.5% M-Banking (Biz)
- POS: 156

**Strengths:**
- Large market with growth momentum (+764 PI YoY, +5.0%)
- Strong SA growth trajectory

**Weaknesses:**
- **14.0% PI penetration in Kosovo's second city is unacceptable** [DATA]
- **LOSING business clients (-40 YoY, -4.2%)** [DATA - RED FLAG]
- M-Banking at 37.0% is 9.5pp below network average [DATA]
- E-Banking at 3.9% is among the lowest [DATA]
- Only 156 POS terminals for 7,119 businesses = massive gap [DATA]
- Mortgage loans only 427 for a city of 147K - only 2.6% of PI clients [DATA]
- Business digital adoption at 68.5% is 11.7pp below network average [DATA]

**Diagnosis:**
This is NLB's most glaring underperformance. Prizren has the second-largest population, significant business activity, a tourism sector (historic city center), and strong diaspora connections. Yet NLB has lower penetration here than in towns 1/10th its size. **The fact that NLB is LOSING business clients in Prizren while growing elsewhere suggests an acute execution or competitive problem.** [INFERENCE: possible causes include inadequate branch staffing, poor location, aggressive competitor presence (likely RBKO, BKT, PCB who may have multiple branches in Prizren), or weak local management.]

**Recommended Actions [URGENT]:**
1. Commission immediate diagnostic: Why are business clients leaving? Exit interview or analysis required.
2. Appoint senior branch manager with commercial mandate and growth targets
3. Deploy dedicated SME relationship manager (if not already present)
4. Launch POS acquisition campaign - current 156 POS vs. 7,119 businesses is a 2.2% penetration
5. Set 24-month target: 22,000 PI clients (+36% from current), 1,200 business clients (+33%)
6. Evaluate need for second branch location or service point in Prizren
7. Aggressive digital onboarding - target 50% M-Banking within 12 months
8. Launch mortgage campaign - Prizren has construction/housing activity but only 427 mortgage loans

**Expected Impact:** If Prizren reaches network-average 19.2% PI penetration = +6,009 PI clients; network-average 16.9% biz penetration = +298 biz clients.

---

## 3. FERIZAJ (Branch 1003)

**Current Profile:**
- Population: 109,255 (Pop >15: 84,228) - Kosovo's 3rd largest
- Businesses: 6,371
- Active PI: 13,576 (+545 YoY, +4.2%)
- Active Business: 726 (-3 YoY, -0.4%)
- Digital: 46.3% M-Banking | 6.0% E-Banking
- Products: 538 Mortgages | 1,578 Consumer | 1,585 CC+OVD

**Strengths:**
- Decent digital adoption (46.3%, near network average)
- Strong consumer lending (1,578) and credit card uptake (1,585 CC+OVD combined)
- Highest CC penetration outside Prishtinë (11.7% of clients)

**Weaknesses:**
- PI penetration only 16.1% for the 3rd largest city [DATA]
- Business penetration 11.4% - 5,645 businesses unserved [DATA]
- Business clients flat/slightly declining [DATA]
- POS terminals: 107 for 6,371 businesses (1.7%) [DATA]

**Recommended Actions:**
1. Business banking push: target +300 new business clients in 12 months
2. POS merchant acquisition campaign
3. Consumer lending and card cross-sell strengths should be leveraged - branch has proven ability in these products
4. Target 20% PI penetration = need +3,270 new PI clients over 24 months

---

## 4. PEJË (Branch 1006)

**Current Profile:**
- Population: 82,745 (Pop >15: 65,980)
- Businesses: 4,172
- Active PI: 15,027 (+476 YoY, +3.3%)
- Active Business: 698 (-3 YoY)
- Digital: 43.6% M-Banking | 4.7% E-Banking
- POS: 421

**Strengths:**
- 22.8% PI penetration - above network average [DATA]
- 421 POS terminals - second highest after Prishtinë [DATA]
- Strong consumer lending volume (1,780)
- Decent client base relative to market

**Weaknesses:**
- Business penetration only 16.7% and declining (-3 YoY) [DATA]
- Digital adoption slightly below average
- Mortgage penetration relatively low (434 loans = 2.9% of clients)

**Recommended Actions:**
1. Leverage strong POS base for merchant service deepening
2. Protect PI market share - focus on retention and cross-sell
3. Reverse business client decline with targeted acquisition
4. Push mortgage lending in Pejë's active construction market

---

## 5. GJAKOVË (Branch 1004)

**Current Profile:**
- Population: 78,699 (Pop >15: 62,970)
- Businesses: 4,005
- Active PI: 8,812 (+10 YoY, +0.1%) [DATA - GROWTH STALLED]
- Active Business: 431 (-70 YoY, -14.0%) [DATA - SEVERE BUSINESS CLIENT LOSS]
- Digital: 37.6% M-Banking | 4.3% E-Banking
- POS: 60

**Strengths:**
- Some historical mortgage presence (447 loans)

**Weaknesses:**
- **14.0% PI penetration - tied for lowest among major cities** [DATA]
- **Lost 70 business clients YoY (-14.0%) - worst business decline in network** [DATA - CRITICAL]
- PI growth essentially zero (+10 clients) [DATA]
- Digital adoption well below average (37.6%) [DATA]
- Only 60 POS terminals for 4,005 businesses (1.5%) [DATA]
- Business penetration 10.8% - worst among major cities [DATA]

**Diagnosis:**
**Gjakovë is in crisis.** Near-zero PI growth combined with 14% business client hemorrhage suggests something fundamentally wrong - potentially branch location, staff quality, competitive displacement, or operational issues. This requires immediate management attention. [INFERENCE]

**Recommended Actions [URGENT]:**
1. Emergency business client retention analysis - why are 70 businesses leaving?
2. Branch-level audit: staff capability, location adequacy, opening hours, service quality
3. Competitive mapping: what are RBKO, BKT, PCB doing in Gjakovë that NLB is not?
4. Consider branch relocation or second service point if current location is suboptimal
5. Deploy dedicated commercial banker with acquisition targets
6. 12-month target: stabilize at minimum, then grow PI by 500 and business by 100

---

## 6. GJILAN (Branch 1002)

**Current Profile:**
- Population: 82,980 (Pop >15: 66,517)
- Businesses: 4,317
- Active PI: 11,535 (+344 YoY, +3.1%)
- Active Business: 459 (+20 YoY, +4.6%)
- Digital: 48.3% M-Banking | 4.9% E-Banking
- Mortgages: 670 (highest outside Prishtinë) | Consumer: 1,439

**Strengths:**
- Strongest mortgage penetration outside Prishtinë (670 loans = 5.8% of clients) [DATA]
- Growing both PI and business clients
- Above-average digital adoption (48.3%)

**Weaknesses:**
- PI penetration at 17.3% below average for a city this size [DATA]
- Business penetration only 10.6% - 3,858 unserved businesses [DATA]
- POS: 115 for 4,317 businesses (2.7%) [DATA]

**Recommended Actions:**
1. Build on mortgage strength - Gjilan may have active property market
2. Business banking is the key gap: target +250 new business clients in 12 months
3. Continue digital momentum - target 55% M-Banking
4. PI acquisition target: +1,000 over 24 months to reach 19% penetration

---

## 7-27. REMAINING BRANCHES (Summarized)

### Medium-Size Branches

**Podujevë** (Pop 70,975): PI penetration 19.5%, strong growth (+578 YoY = +5.7%). Digital at 43.7%. Business penetration only 14.7%. **Action:** Business acquisition focus.

**Mitrovicë** (Pop 64,742): PI penetration 23.7% (strong), but growth stalled (+62 YoY = +0.5%). M-Banking low at 35.7%. **Action:** Digital migration urgently needed; evaluate branch model for advisory shift.

**Fushë Kosovë** (Pop 63,949): PI penetration only 13.3% but M-Banking high at 56.0% and business penetration at 19.6%. **Action:** This is a digitally-mature branch in Prishtinë's orbit. Focus on PI acquisition - large untapped population.

**Vushtrri** (Pop 61,528): PI penetration 13.7%, business only 11.3%. Digital low at 37.6%. **Action:** Underperforming on all dimensions. Needs comprehensive commercial push.

**Lipjan** (Pop 55,044): PI penetration 14.2%, business 18.8%. Digital average at 41.5%. **Action:** PI acquisition focus. Within Prishtinë commuter belt - target salary account migration.

### Smaller Branches

**Gllogoc** (Pop 48,079): Strong performer - 24.3% PI penetration, 21.8% business, 49.5% M-Banking. **Action:** Maintain performance, push toward 55% digital.

**Suharekë** (Pop 45,749): PI penetration 16.4%, digital low at 38.5%. **Action:** Digital migration push, moderate growth targets.

**Malishevë** (Pop 43,888): Low PI (13.6%) but good business penetration (22.0%) and high M-Banking (50.2%). **Action:** PI acquisition; branch serves as business-focused service point.

**Rahovec** (Pop 41,799): PI penetration 16.8%, business only 11.8%, M-Banking low at 33.8%. **Action:** Digital migration is priority. Consider staffing adjustment if transaction volumes are high.

**Skenderaj** (Pop 40,664): PI penetration 19.2% (at average), good business (23.4%), but very low M-Banking (34.9%). **Action:** Digital push. High business penetration suggests strong commercial branch - protect this.

**Viti** (Pop 35,566): PI penetration 18.5%, digital average at 45.4%. **Action:** Steady growth, deepen product cross-sell.

**Istog** (Pop 33,008): PI penetration 19.4%, good business (22.2%), M-Banking strong at 48.2%. **Action:** Well-balanced branch. Focus on product depth.

**Klinë** (Pop 30,503): 18.2% PI, highest business penetration in segment (26.3%) but slow growth (+87 YoY). **Action:** May be approaching saturation. Focus on products-per-client.

**Kaçanik** (Pop 27,716): Strong at 28.0% PI penetration, 35.0% business, good digital (49.6%). **Action:** Growth leader for its size. Protect and maintain.

**Deçan** (Pop 27,775): Outstanding 34.0% PI penetration, 36.9% business. **Action:** Star small branch. Maintain model, export best practices to other small branches.

**Kamenicë** (Pop 22,868): PI penetration 16.9%, business 14.3%, M-Banking 45.8%. **Action:** Moderate growth potential. Consider whether branch format should be lightened.

**Obiliq** (Pop 22,815): Good PI at 23.8%, low business at 18.2%. In Prishtinë orbit. **Action:** Salary account acquisition from industrial zone workers.

**Graçanicë** (Pop 18,486): 24.9% PI but very low digital (28.7%) and low business (10.7%). Serb-majority community. **Action:** Adapted model, gentle digital onboarding, business banking awareness campaign.

**Hani i Elezit** (Pop 8,533): Exceptional 53.1% PI, 67.7% business, good digital (56.2%). Border town economics drive strong banking demand. **Action:** Protect this franchise. Consider trade finance products for border traders.

**Shtërpcë** (Pop 10,771): 33.0% PI but lowest M-Banking in network (27.2%). **Action:** Digital onboarding program tailored to demographic (Serb-majority, potentially older).

---

# PART 5 - IDEAL BRANCH MODEL

---

## Model 1: LARGE CITY BRANCH (Prishtinë, Prizren, Ferizaj, Pejë, Gjilan, Gjakovë)

**Strategic Role:** Full-service banking hub serving PI, Micro, SME, and CIB clients. Advisory-led model with digital-first transaction handling.

**Target Client Mix:**
- PI: 60% of clients, 40% of revenue
- Micro Business: 25% of clients, 30% of revenue
- SME: 10% of clients, 20% of revenue
- CIB: 5% of clients, 10% of revenue

**Recommended Product Focus:**
- Mortgages (primary market for housing finance)
- SME lending (working capital, investment loans)
- POS/card acquiring (merchant services)
- Salary account packages
- Insurance cross-sell
- Investment/savings products
- Trade finance (where relevant)

**Staffing Model (indicative - requires validation with actual headcount data):**
- Branch Manager (1)
- Deputy/Operations Manager (1)
- Relationship Managers - PI/Affluent (2-3)
- Relationship Managers - Business/SME (2-3)
- Credit Analyst / Micro Analyst (1-2)
- Tellers / Service staff (3-4, declining as digital grows)
- Digital support / Sales (1-2)
- Total: 12-17 FTE

**Digital / Service Model:**
- Target: 60%+ M-Banking, 15%+ E-Banking
- Self-service zones with ATM, deposit machines, card issuance
- Appointment-based advisory for complex products
- Walk-in service for basic transactions (declining over time)
- Cash handling outsourced or centralized where possible

**Productivity Expectations:**
- PI clients per branch: 12,000-20,000+
- Business clients per branch: 600-1,500+
- Products per client: >2.5
- Loan penetration: >15% of active clients
- Card penetration: >10% of active clients

**KPIs:**
- Client acquisition (monthly net new PI and Business)
- Cross-sell ratio
- Digital migration rate
- Business client retention rate
- Loan origination volume
- POS terminal activation

---

## Model 2: MEDIUM CITY BRANCH (Mitrovicë, Podujevë, Fushë Kosovë, Vushtrri, Lipjan, Gllogoc, Suharekë)

**Strategic Role:** Regional service center with balanced transaction and commercial focus. Increasingly digital-first for routine services.

**Target Client Mix:**
- PI: 70% of clients, 50% of revenue
- Micro Business: 25% of clients, 35% of revenue
- SME: 5% of clients, 15% of revenue

**Recommended Product Focus:**
- Consumer lending (primary driver)
- Salary accounts
- Micro/SME lending
- Savings accounts
- Credit cards and overdrafts
- Basic insurance products
- Remittance services (where diaspora connection is strong)

**Staffing Model:**
- Branch Manager (1) - player/coach, handles key relationships
- Relationship Manager (1-2, combined PI/Business)
- Credit/Sales Officer (1)
- Tellers / Service (2-3)
- Total: 5-8 FTE

**Digital / Service Model:**
- Target: 50%+ M-Banking
- ATM and basic self-service
- Branch handles advisory + onboarding + complex transactions
- Routine transactions actively migrated to digital

**Productivity Expectations:**
- PI clients: 5,000-12,000
- Business clients: 200-500
- Products per client: >2.0
- Consumer loan penetration: >10%

---

## Model 3: SMALL CITY / TOWN BRANCH (Malishevë, Rahovec, Skenderaj, Viti, Istog, Klinë, Kamenicë, Kaçanik, Deçan, Obiliq, Hani i Elezit, Graçanicë, Shtërpcë)

**Strategic Role:** Community-anchored service point with strong local relationships. Lean operations, high digital push.

**Target Client Mix:**
- PI: 75% of clients, 55% of revenue
- Micro Business: 20% of clients, 35% of revenue
- SME (rare): 5% of clients, 10% of revenue

**Recommended Product Focus:**
- Consumer lending (core product)
- Savings accounts
- Salary account packages
- Micro business loans
- Remittances (especially border/diaspora towns)
- Agricultural lending (where relevant - Rahovec wine region, Malishevë agriculture)
- Basic cards and overdrafts

**Staffing Model:**
- Branch Manager (1) - handles both operations and key commercial relationships
- Multi-skilled Officer (1-2) - combined teller/sales/service
- Total: 3-4 FTE

**Digital / Service Model:**
- Target: 45%+ M-Banking
- ATM (essential)
- Branch open reduced hours if volumes warrant (e.g., 09:00-15:00)
- All routine transactions pushed to digital/ATM
- Branch time focused on onboarding, lending, advisory

**Productivity Expectations:**
- PI clients: 2,500-7,500
- Business clients: 100-350
- Products per client: >1.8

**Variant - Light-Format Branch:**
For the smallest markets (Shtërpcë, Leposaviq, Zubin Potok, potential new points):
- 2 FTE: Branch Lead + Universal Banker
- Limited hours (e.g., 3-4 days/week or mornings only)
- ATM essential
- Digital onboarding primary channel
- Lending processed centrally with local relationship management

---

# PART 6 - EXPANSION AND NETWORK OPTIMIZATION

---

## 6.1 WHERE TO EXPAND

### Priority 1: DRAGASH (Population 28,896 | 652 Businesses)
**Case:** Dragash is the largest municipality without NLB presence. Population of 28,896 with 652 registered businesses. Located in the Sharr Mountains region, primarily rural/agricultural with some tourism potential.
**Recommendation:** Light-format branch or service point (2-3 FTE). Start with ATM + weekly presence, then upgrade based on demand.
**Expected Outcome:** 2,000-3,500 PI clients within 24 months if NLB captures 15-20% of adult population.
**Format:** Light branch
**Confidence:** [INFERENCE - requires local market validation: competitor presence, physical location availability, cost structure]

### Priority 2: SHTIME (Population 24,308 | 802 Businesses)
**Case:** Second-largest unserved municipality. Located on the Prishtinë-Prizren highway, between Ferizaj and Suharekë. Good road connectivity.
**Recommendation:** Service point or light branch (2-3 FTE). 802 businesses suggest meaningful commercial activity.
**Expected Outcome:** 2,000-3,000 PI clients, 100-150 business clients within 24 months.
**Format:** Light branch with focus on consumer lending and salary accounts
**Confidence:** [INFERENCE]

### Priority 3: SECOND PRESENCE IN PRIZREN
**Case:** Prizren has 147,246 people and only 14% NLB PI penetration. A single branch appears insufficient for this market. [HYPOTHESIS: NLB may have only one branch while competitors have multiple locations, creating a coverage disadvantage.]
**Recommendation:** Open a second branch or service point in a high-traffic commercial zone or residential area not served by the current branch.
**Format:** Medium-format branch focused on PI acquisition and business banking
**Confidence:** [HYPOTHESIS - requires competitive mapping and current branch location analysis]

### Priority 4: SECOND PRESENCE IN PRISHTINË
**Case:** Prishtinë has 227,466 people. Even at 26.9% PI penetration, 73% of adults are not NLB clients. Sub-areas of Prishtinë (e.g., Matiçan, Çagllavicë, new residential developments) may be underserved.
**Recommendation:** Evaluate satellite branch or service point in growing residential/commercial areas of greater Prishtinë.
**Format:** Medium or light branch
**Confidence:** [HYPOTHESIS - requires geographic analysis of client distribution within Prishtinë]

### Lower Priority: Remaining Unserved Municipalities
| Municipality | Pop | Businesses | Recommendation |
|-------------|-----|-----------|----------------|
| Mamushë | 5,607 | 219 | Not viable for standalone branch. Serve via nearby Prizren/Rahovec |
| Novobërdë | 4,493 | 122 | Too small. Serve via Gjilan or Kamenicë |
| Junik | 3,943 | 77 | Too small. Serve via Deçan |
| Kllokot | 3,041 | 75 | Too small. Serve via Gjilan/Viti |
| Partesh | 3,240 | 84 | Serb-majority. Serve via Gjilan or Graçanicë |
| Zveçan | 2,867 | 134 | Served via Mitrovicë Veriore (already 135% penetration) |
| Ranillug | 2,481 | 35 | Too small. No action |

---

## 6.2 WHERE TO REDESIGN

### Digital-First Conversion Candidates
Branches with high digital adoption AND small client base could be converted to lighter formats:

| Branch | PI Clients | M-Banking% | Candidate? |
|--------|-----------|-------------|------------|
| Hani i Elezit | 3,424 | 56.2% | No - exceptional performer, keep current model |
| Obiliq | 4,126 | 45.1% | Maybe - Prishtinë orbit, could be lightened |
| Kamenicë | 3,239 | 45.8% | Yes - small market, digital-ready |
| Shtërpcë | 2,976 | 27.2% | No - low digital, needs adapted model |

### Format Upgrade Candidates
Branches in larger markets that may need investment:

| Branch | PI Clients | Gap to Average | Action |
|--------|-----------|---------------|--------|
| Prizren | 16,152 | -5.2pp penetration | Possible second branch + upgrade |
| Gjakovë | 8,812 | -5.2pp penetration | Branch audit, possible relocation |
| Fushë Kosovë | 6,301 | -5.9pp penetration | Evaluate if location serves population |
| Vushtrri | 6,504 | -5.5pp penetration | May need repositioning |

---

## 6.3 WHERE TO SHIFT CAPACITY

### Digital Migration = Workforce Reallocation Opportunity

**[HYPOTHESIS: the following assumes 1 teller handles ~40-50 routine transactions/day]**

Branches below 35% M-Banking have the highest proportion of routine transactions still done in-branch:

| Branch | M-Banking% | Estimated Teller Load | Action |
|--------|------------|----------------------|--------|
| Shtërpcë | 27.2% | High | Deploy digital ambassador, set 40% target in 12 months |
| Graçanicë | 28.7% | High | Same - culturally adapted approach |
| Mit. Veriore | 30.8% | High | Same - linguistically adapted (Serbian) |
| Rahovec | 33.8% | Medium-High | Digital push campaign |
| Skenderaj | 34.9% | Medium-High | Digital push campaign |
| Mitrovicë | 35.7% | Medium | Digital push + potential teller reduction |

If these 6 branches increase M-Banking by 15pp each, [HYPOTHESIS] approximately 20-30% of their routine transaction volume could shift to digital, potentially freeing 0.5-1.0 FTE per branch (3-6 FTE total) that could be redeployed to sales/advisory roles or optimized out.

---

## 6.4 PRIORITIZED ACTION TABLE

| Priority | Action | Branches Affected | Impact | Feasibility | Speed |
|----------|--------|-------------------|--------|-------------|-------|
| 1 | Prizren commercial offensive | 1 | Very High | High | 0-6 months |
| 2 | Gjakovë emergency diagnostic | 1 | High | High | Immediate |
| 3 | Business banking acceleration | All | Very High | Medium | 3-12 months |
| 4 | Digital migration program | 6 low-adoption branches | Medium | High | 3-12 months |
| 5 | Open light branch in Dragash | New | Medium | Medium | 6-12 months |
| 6 | Open light branch in Shtime | New | Medium | Medium | 6-12 months |
| 7 | Product cross-sell campaign | All regional | High | High | 0-6 months |
| 8 | Prizren second branch/point | 1 | High | Medium | 6-18 months |
| 9 | Workforce rebalancing | All | Medium | Low-Medium | 12-24 months |
| 10 | Light-format conversion pilot | 1-2 small branches | Low-Medium | Medium | 12-18 months |

---

# PART 7 - IMPLEMENTATION ROADMAP

---

## Phase 1: Quick Wins (0-3 Months)

### Week 1-4: Diagnostic Actions
1. **Gjakovë Emergency Audit:** Send senior team to understand business client hemorrhage (-70 YoY). Interview departing clients, assess branch operations, benchmark against competitors.
2. **Prizren Business Client Exit Analysis:** Investigate -40 business client decline. Determine whether this is competitor-driven, service-driven, or market-driven.
3. **Data Infrastructure:** Build branch-level P&L capability if not already in place. This report is constrained by the absence of revenue/cost data per branch.

### Month 1-3: Commercial Campaigns
4. **Salary Account Blitz in Large Cities:** Target unbanked employees in Prizren, Ferizaj, Gjakovë, Gjilan through employer partnerships. Focus on industrial zones, government offices, education sector.
5. **POS Acquisition Campaign:** Focus on Prizren (156 POS for 7,119 businesses), Ferizaj (107 for 6,371), Gjakovë (60 for 4,005). Quick revenue and visibility win.
6. **Consumer Lending Push:** Standardize and speed up consumer loan origination in all branches. Set branch-level targets for loan origination.
7. **Savings Account Momentum:** Capitalize on 122% SA growth by launching promotional savings campaigns (goal-based savings, bonus rate tiers).

### Month 1-3: Digital Quick Wins
8. **Digital Onboarding in 6 Low-Adoption Branches:** Deploy "digital ambassador" (existing staff trained as digital coaches) in Shtërpcë, Graçanicë, Mitrovicë Veriore, Rahovec, Skenderaj, Mitrovicë.
9. **Set M-Banking Activation Targets:** Every branch below 45% gets a monthly activation target with branch manager accountability.

---

## Phase 2: Medium-Term Initiatives (3-12 Months)

### Month 3-6: Growth Infrastructure
10. **Prizren Growth Plan:** Dedicated branch upgrade with potential second service point. Hire/deploy additional commercial staff. Set 3-year target: 22,000 PI clients, 1,200 business clients.
11. **Business Banking Unit Formation:** Create centralized business banking support team that works across branches to acquire and onboard business clients. Target: +2,330 new business clients network-wide (20% penetration).
12. **Product Bundling:** Design 3-4 product packages (Starter, Professional, Business, Premium) with clear pricing and benefits. Train all branch staff on consultative selling.

### Month 6-12: Network Optimization
13. **Dragash Light Branch:** Open service point (ATM + 2 FTE + 3 days/week). Evaluate demand for full-time presence.
14. **Shtime Light Branch:** Similar model.
15. **Gjakovë Intervention:** Implement findings from Month 1 diagnostic. If branch location is problematic, initiate relocation process.
16. **Staffing Model Pilots:** In 3-4 digitally mature branches (Prishtinë, Fushë Kosovë, Istog, Kaçanik), pilot advisory-led model with reduced teller positions and increased sales/relationship manager roles.

### Month 6-12: Product Optimization
17. **Mortgage Campaign in Growth Markets:** Prizren, Gjilan, Ferizaj, Pejë show mortgage under-penetration. Partner with construction companies, real estate developers.
18. **Micro-Lending Enhancement:** Standardize micro-business loan product for quick approval. Deploy in high-business-density branches (Deçan, Kaçanik, Klinë, Skenderaj).
19. **Remittance Strategy:** For border and diaspora-heavy towns (Hani i Elezit, Kaçanik, Dragash, Malishevë), ensure competitive remittance pricing and convert remittance receivers into full banking clients.

---

## Phase 3: Structural Transformation (12+ Months)

### Month 12-24: Model Evolution
20. **Full Branch Model Transition:** Convert all large-city branches to advisory-led model. Transaction handling primarily via digital + self-service.
21. **Workforce Redesign:** Complete the shift from teller-dominated to sales/advisory-dominated staffing across the network. Target: 60% of branch FTE in commercial/advisory roles, 40% in operations/service.
22. **Branch Format Rationalization:** Convert 2-3 smallest branches to light format if economics warrant. Reinvest savings in growth markets.
23. **Prishtinë Sub-Branching:** Open 1-2 satellite locations in growing Prishtinë neighborhoods.
24. **Prizren Second Branch:** Based on first-year results of Prizren offensive, open second full or medium-format branch.

### Month 18-36: Strategic Capability
25. **Wealth/Affluent Banking:** Launch dedicated proposition in Prishtinë. Segment existing affluent clients. Offer advisory, savings, and investment products.
26. **Data-Driven Branch Management:** Implement real-time branch performance dashboards. Monthly performance reviews using KPI framework (see Part 8).
27. **Continuous Network Review:** Annual assessment of all branches against the five-dimensional framework, with action plans for underperformers.

---

# PART 8 - KPI FRAMEWORK

---

## Branch Performance Scorecard

### Tier 1: Strategic KPIs (CEO/CFO Level - Monthly Review)

| KPI | Metric | Target | Current Baseline |
|-----|--------|--------|-----------------|
| **Network Client Growth** | Net new PI clients (monthly) | +1,000/month | ~750/month (implied from +9,041 YoY) |
| **Network Business Growth** | Net new business clients (monthly) | +100/month | ~23/month (implied from +281 YoY) |
| **PI Market Penetration** | Active PI / Pop >15 | 22% by 2028 | 19.2% |
| **Business Market Penetration** | Active Biz / Registered Biz | 20% by 2027 | 16.9% |
| **Digital Migration Rate** | % of PI clients with M-Banking | 55% by 2027 | 46.5% |
| **Cross-Sell Ratio** | Products per active client | 2.5 by 2028 | ~2.0 (estimated) |
| **Underperformer Closure Rate** | # branches below 15% PI penetration | 0 by 2028 | 7 branches |

### Tier 2: Branch-Level KPIs (Branch Manager Level - Weekly/Monthly)

| Category | KPI | Measurement |
|----------|-----|-------------|
| **Profitability** | Revenue per client (when available) | EUR / active client |
| | Cost-to-income ratio (when available) | Operating costs / Operating income |
| | Loan origination volume | # and EUR of new loans per month |
| **Productivity** | Clients per FTE | Active clients / Branch FTE |
| | New clients per FTE | Net new clients / Branch FTE |
| | Products sold per FTE | New products originated / Branch FTE |
| **Market Penetration** | PI penetration rate | Active PI / Pop >15 |
| | Business penetration rate | Active Biz / Registered Biz |
| | POS penetration | POS terminals / Registered Biz |
| **Workforce Efficiency** | Transaction per teller (when available) | Branch transactions / Teller FTE |
| | Sales conversion rate | Products sold / Client meetings |
| **Digital Migration** | M-Banking activation rate | M-click users / Active PI |
| | E-Banking activation rate | E-click users / Active PI |
| | Digital transaction share | Digital txns / Total txns (when available) |
| **Product Mix** | Consumer loan penetration | Consumer loans / Active PI |
| | Mortgage penetration | Mortgage loans / Active PI |
| | Card penetration | (CC + OVD) / Active PI |
| | Savings penetration | SA / Active PI |
| | Business lending penetration | (ST + LT loans) / Active Biz |
| **Client Acquisition** | Net new PI clients | Monthly count |
| | Net new Business clients | Monthly count |
| | Business client retention rate | (Start - Churned) / Start |

### Tier 3: Network-Wide Monitoring (Management Committee - Quarterly)

| KPI | Purpose |
|-----|---------|
| Branch ranking by PI penetration | Identify persistent underperformers |
| Branch ranking by digital adoption | Track migration progress |
| Client growth heatmap by municipality | Identify momentum shifts |
| Business client retention by branch | Early warning for problems like Gjakovë |
| Product mix variance by branch archetype | Ensure appropriate product focus |
| Staffing efficiency benchmarks | Track workforce optimization |

---

# PART 9 - MANAGEMENT QUESTIONS

---

## The 15 Most Important Questions the CEO/CFO Should Ask

### On Performance

1. **"Why is Prizren - our second-largest market by population - performing at the same penetration level as towns 1/10th its size?"** This demands a specific answer: Is it branch location? Staffing? Competition? Historical neglect? The answer will determine whether Prizren needs investment, restructuring, or management change.

2. **"Why are we losing business clients in Gjakovë (-14%) and Prizren (-4%)? Where are they going, and what triggered it?"** Business client attrition in two major cities simultaneously suggests a systemic issue, not random churn.

3. **"What is driving the 3x performance difference in PI penetration between our best and worst branches in comparable markets?"** Deçan achieves 34% penetration in a town of 28K; Vushtrri achieves 13.7% in a town of 62K. Is this branch management quality, competitive landscape, or something else?

### On Revenue and Profitability

4. **"Do we have branch-level P&L? If not, when will we?"** This analysis was constrained by the absence of revenue and cost data per branch. Without branch-level P&L, management cannot identify whether high-penetration branches are actually profitable or whether small branches are subsidized by Prishtinë.

5. **"What is our revenue per client in Prishtinë versus our regional branches?"** [HYPOTHESIS: the gap is likely 2-3x due to product mix and balance differences.] This has direct implications for where to invest growth resources.

6. **"What is our true cost-to-income ratio at branch level, and how does it compare to the sector average?"** System-level data suggests NLB's C/I may be above sector average (~88% vs 86%). If true, branch-level cost optimization is urgent.

### On Digital and Workforce

7. **"What percentage of branch transactions today could be done digitally? What is the actual teller utilization rate?"** Without transaction volume data, the digital migration opportunity is estimated directionally. Hard data would sharpen the business case for workforce rebalancing.

8. **"How many FTE do we have per branch, and what is the ratio of sales/advisory versus operations/service?"** This report cannot assess workforce fit because staffing data is missing. This is a critical gap.

9. **"If we raised M-Banking adoption from 46.5% to 60% network-wide, what would the cost saving be in reduced teller need?"** This is the core business case for digital migration investment.

### On Growth Strategy

10. **"Are we prepared to commit serious resources to Prizren and Gjakovë, or will we accept structural underperformance in these markets?"** Half-measures won't work. These markets need dedicated commercial teams, potentially new locations, and 2-3 year investment horizons.

11. **"Why is our business banking penetration only 16.9%? What is our win rate on business pitches, and what are businesses choosing instead?"** 83% of Kosovo businesses do not bank with NLB. Understanding why is a strategic imperative.

12. **"Should we open in Dragash and Shtime? What's the breakeven analysis?"** This report recommends light-format expansion, but the economic case requires cost data not available in the uploaded files.

### On Market and Competition

13. **"How many branches do our top 3 competitors have in Prizren, Ferizaj, and Gjakovë? Are we under-branched in these cities?"** [HYPOTHESIS: NLB may have single branches where competitors have 2-3, creating a structural disadvantage.]

14. **"What is our market share trend over the last 12 months in deposits and loans? Are we gaining or losing ground to specific competitors?"** The market share data shows NLB at ~16-20% across categories, but the trend direction matters more than the level.

15. **"Is our Savings Account growth (122% YoY) a deliberate strategy or an accidental outcome? Do we have a coherent deposit strategy?"** The massive SA growth combined with TDA decline suggests client behavior is shifting. NLB needs to decide whether to accelerate this (lower funding cost, more flexible) or stabilize TDA (longer-duration funding). This is a treasury/ALM question with strategic implications.

---

# EXHIBITS AND TABLES

---

## Exhibit A: Branch Ranking by PI Penetration (2026)

| Rank | Branch | Pop >15 | PI Clients | Penetration | Segment |
|------|--------|---------|------------|-------------|---------|
| 1 | Mit. Veriore | 6,833 | 9,261 | 135.5%* | Structural Outlier |
| 2 | Hani i Elezit | 6,447 | 3,424 | 53.1% | Small Specialized |
| 3 | Deçan | 22,138 | 7,529 | 34.0% | Strong Regional |
| 4 | Shtërpcë | 9,026 | 2,976 | 33.0% | Structural Outlier |
| 5 | Kaçanik | 21,269 | 5,947 | 28.0% | Strong Regional |
| 6 | Prishtinë | 177,302 | 47,635 | 26.9% | Dominant Hub |
| 7 | Graçanicë | 14,806 | 3,691 | 24.9% | Structural Outlier |
| 8 | Gllogoc | 36,276 | 8,808 | 24.3% | Strong Regional |
| 9 | Obiliq | 17,367 | 4,126 | 23.8% | Strong Regional |
| 10 | Mitrovicë | 50,171 | 11,901 | 23.7% | Strong Regional |
| 11 | Pejë | 65,980 | 15,027 | 22.8% | Strong Regional |
| 12 | Podujevë | 54,812 | 10,670 | 19.5% | Strong Regional |
| 13 | Istog | 26,385 | 5,105 | 19.4% | Moderate |
| 14 | Skenderaj | 31,671 | 6,091 | 19.2% | Small-Market |
| 15 | Viti | 27,813 | 5,153 | 18.5% | Moderate |
| 16 | Klinë | 23,708 | 4,322 | 18.2% | Moderate |
| 17 | Gjilan | 66,517 | 11,535 | 17.3% | **Underperformer** |
| 18 | Kamenicë | 19,137 | 3,239 | 16.9% | Small-Market |
| 19 | Rahovec | 32,724 | 5,514 | 16.8% | Small-Market |
| 20 | Suharekë | 36,111 | 5,922 | 16.4% | Moderate |
| 21 | Ferizaj | 84,228 | 13,576 | 16.1% | **Underperformer** |
| 22 | Lipjan | 41,804 | 5,950 | 14.2% | Moderate |
| 23 | Prizren | 115,421 | 16,152 | 14.0% | **Underperformer** |
| 24 | Gjakovë | 62,970 | 8,812 | 14.0% | **Underperformer** |
| 25 | Vushtrri | 47,591 | 6,504 | 13.7% | Moderate |
| 26 | Malishevë | 32,516 | 4,413 | 13.6% | Moderate |
| 27 | Fushë Kosovë | 47,439 | 6,301 | 13.3% | Moderate |
| 28 | Zubin Potok | 2,940 | 184 | 6.3% | Structural Outlier |
| 29 | Leposaviq | 8,435 | 389 | 4.6% | Structural Outlier |

*Serves clients beyond municipal boundary

---

## Exhibit B: Digital Maturity Ranking (PI M-Banking %)

| Rank | Branch | M-Banking % | E-Banking % | Gap to 50% Target |
|------|--------|------------|-------------|-------------------|
| 1 | Prishtinë | 62.4% | 11.3% | Exceeded |
| 2 | Hani i Elezit | 56.2% | 7.1% | Exceeded |
| 3 | Fushë Kosovë | 56.0% | 7.4% | Exceeded |
| 4 | Deçan | 51.7% | 6.3% | Exceeded |
| 5 | Malishevë | 50.2% | 5.1% | Exceeded |
| 6 | Kaçanik | 49.6% | 6.5% | -0.4pp |
| 7 | Gllogoc | 49.5% | 9.9% | -0.5pp |
| 8 | Leposaviq | 48.1% | 2.6% | -1.9pp |
| 9 | Gjilan | 48.3% | 4.9% | -1.7pp |
| 10 | Istog | 48.2% | 3.6% | -1.8pp |
| ... | ... | ... | ... | ... |
| 25 | Mitrovicë | 35.7% | 5.7% | -14.3pp |
| 26 | Skenderaj | 34.9% | 3.6% | -15.1pp |
| 27 | Rahovec | 33.8% | 4.8% | -16.2pp |
| 28 | Mit. Veriore | 30.8% | 8.4% | -19.2pp |
| 29 | Graçanicë | 28.7% | - | -21.3pp |
| 30 | Shtërpcë | 27.2% | 3.0% | -22.8pp |

---

## Exhibit C: Business Banking Opportunity Heatmap

| Branch | Registered Biz | NLB Biz Clients | Penetration | Unserved | POS | POS/Biz% |
|--------|---------------|-----------------|-------------|----------|-----|----------|
| Prishtinë | 21,396 | 4,216 | 19.7% | 17,180 | 1,705 | 8.0% |
| Prizren | 7,119 | 905 | 12.7% | 6,214 | 156 | 2.2% |
| Ferizaj | 6,371 | 726 | 11.4% | 5,645 | 107 | 1.7% |
| Gjilan | 4,317 | 459 | 10.6% | 3,858 | 115 | 2.7% |
| Pejë | 4,172 | 698 | 16.7% | 3,474 | 421 | 10.1% |
| Gjakovë | 4,005 | 431 | 10.8% | 3,574 | 60 | 1.5% |
| Podujevë | 2,381 | 349 | 14.7% | 2,032 | 45 | 1.9% |
| Mitrovicë | 2,529 | 427 | 16.9% | 2,102 | 107 | 4.2% |
| Fushë Kosovë | 2,711 | 531 | 19.6% | 2,180 | 201 | 7.4% |
| Suharekë | 2,085 | 346 | 16.6% | 1,739 | 33 | 1.6% |
| **TOTAL TOP 10** | **57,086** | **9,088** | **15.9%** | **47,998** | **2,950** | **5.2%** |

**Key Insight:** In NLB's top 10 markets by business count, there are nearly 48,000 unserved businesses. Even capturing 5% of these = 2,400 new business clients, a 26% increase in business client base.

---

## Exhibit D: Product Mix by Branch Archetype

| Product | Prishtinë | Large City Avg | Medium City Avg | Small City Avg | Network |
|---------|-----------|---------------|-----------------|----------------|---------|
| CA/Client | 11.1% | 6.3% | 5.0% | 5.6% | 6.5% |
| SA/Client | 20.0% | 10.8% | 11.1% | 12.2% | 12.7% |
| TDA/Client | 5.1% | 4.3% | 3.9% | 3.2% | 3.6% |
| Mortgage/Client | 7.1% | 3.3% | 2.9% | 2.9% | 3.9% |
| Consumer/Client | 16.1% | 10.9% | 10.6% | 10.5% | 11.3% |
| CC+OVD/Client | 15.7% | 9.3% | 7.1% | 6.4% | 7.8% |

**Key Insight:** Prishtinë's product intensity is 2-3x higher than regional branches across every product category. This is the clearest indicator that regional branches have major cross-sell upside. Raising regional branches' product mix to even 70% of Prishtinë's levels would significantly increase NLB's per-client revenue.

---

## Exhibit E: Growth Momentum Table (2025-2026 YoY)

| Branch | PI Growth | PI Growth % | Biz Growth | Biz Growth % | Net Assessment |
|--------|----------|-------------|-----------|--------------|----------------|
| Prishtinë | +2,215 | +4.9% | +48 | +1.2% | Growing but Biz lagging |
| Prizren | +764 | +5.0% | -40 | -4.2% | PI growing, **Biz declining** |
| Podujevë | +578 | +5.7% | +2 | +0.6% | Strong PI, Biz flat |
| Ferizaj | +545 | +4.2% | -3 | -0.4% | OK PI, Biz flat |
| Pejë | +476 | +3.3% | -3 | -0.4% | OK PI, Biz flat |
| Gjilan | +344 | +3.1% | +20 | +4.6% | Balanced growth |
| Gllogoc | +315 | +3.7% | -11 | -3.1% | PI growing, Biz declining |
| Skenderaj | +301 | +5.2% | +5 | +2.0% | Solid growth |
| Suharekë | +285 | +5.1% | +13 | +3.9% | Good momentum |
| Hani i Elezit | +269 | +8.5% | +17 | +9.8% | **Fastest grower** |
| Malishevë | +266 | +6.4% | +8 | +3.2% | Good |
| Istog | +261 | +5.4% | +10 | +3.9% | Good |
| Fushë Kosovë | +240 | +4.0% | +70 | +15.2% | **Biz growth leader** |
| Vushtrri | +235 | +3.7% | 0 | 0% | PI OK, Biz stalled |
| Lipjan | +234 | +4.1% | -4 | -1.1% | OK PI, Biz declining |
| Kaçanik | +217 | +3.8% | +43 | +15.0% | Strong all-round |
| Leposaviq | +196 | +101.6% | +36 | +83.7% | Rapid ramp-up |
| Viti | +193 | +3.9% | -1 | -0.4% | Average |
| Kamenicë | +181 | +5.9% | +23 | +20.4% | Small but growing well |
| Obiliq | +181 | +4.6% | +1 | +0.8% | Steady |
| Rahovec | +156 | +2.9% | -1 | -0.5% | Below average |
| Deçan | +155 | +2.1% | -2 | -0.7% | Slowing |
| Zubin Potok | +145 | +371.8% | +20 | +333% | New market ramp |
| Graçanicë | +81 | +2.2% | +3 | +3.1% | Slow |
| Klinë | +87 | +2.1% | 0 | 0% | Stalling |
| Shtërpcë | +95 | +3.3% | +7 | +7.6% | Moderate |
| Mitrovicë | +62 | +0.5% | +27 | +6.8% | **PI growth stalled** |
| Mit. Veriore | -46 | -0.5% | +63 | +25.7% | PI declining, Biz booming |
| Gjakovë | +10 | +0.1% | -70 | -14.0% | **CRISIS** |

---

## Exhibit F: Expansion Priority Matrix

| Municipality | Pop | Biz | NLB Present? | Nearest NLB Branch | Recommended Format | Priority |
|-------------|-----|-----|-------------|--------------------|--------------------|----------|
| Dragash | 28,896 | 652 | No | Prizren (~30km) | Light branch | HIGH |
| Shtime | 24,308 | 802 | No | Lipjan/Ferizaj (~15km) | Light branch | HIGH |
| Prizren (2nd) | 147,246 | 7,119 | Yes (1 branch) | N/A | Medium branch | HIGH |
| Prishtinë (sub) | 227,466 | 21,396 | Yes (1 branch) | N/A | Medium branch | MEDIUM |
| Mamushë | 5,607 | 219 | No | Rahovec (~8km) | ATM only | LOW |
| Novobërdë | 4,493 | 122 | No | Gjilan (~30km) | ATM only | LOW |
| Junik | 3,943 | 77 | No | Deçan (~15km) | No action | VERY LOW |
| Kllokot | 3,041 | 75 | No | Gjilan (~25km) | No action | VERY LOW |
| Partesh | 3,240 | 84 | No | Gjilan (~15km) | No action | VERY LOW |
| Ranillug | 2,481 | 35 | No | Gjilan (~30km) | No action | VERY LOW |

---

# APPENDIX: METHODOLOGY NOTES AND CAVEATS

---

## What This Report Can and Cannot Claim

### Data-Supported Findings [HIGH CONFIDENCE]
- Branch-level client counts (PI and Business) and YoY changes
- Product penetration rates by branch (loans, cards, deposits by count)
- Digital adoption rates by branch (M-Banking, E-Banking)
- Market penetration rates (clients vs. population)
- Business penetration rates (clients vs. registered businesses)
- Branch segmentation based on multiple performance dimensions
- Identification of Prizren and Gjakovë as clear underperformers relative to market size
- Savings account growth and TDA decline as system-wide trends

### Inferences [MEDIUM CONFIDENCE]
- Revenue per client is materially higher in Prishtinë than regional branches (based on product mix evidence)
- Low M-Banking branches carry disproportionate teller workloads
- Business client losses in Gjakovë/Prizren suggest execution or competitive problems
- Hani i Elezit's exceptional performance is partly driven by border-town economics
- Mitrovicë Veriore serves a catchment area well beyond its municipal boundary
- Digital migration can free FTE for redeployment to sales/advisory roles

### Hypotheses [REQUIRE VALIDATION]
- NLB may be under-branched in Prizren relative to competitors
- Raising M-Banking from 46.5% to 60% would yield 2-4pp cost-to-income improvement
- A focused Prizren offensive could add 8,000-12,000 PI clients over 3 years
- Light-format branches in Dragash and Shtime would reach breakeven within 18-24 months
- Regional branch product cross-sell could be doubled with structured sales programs
- NLB's cost-to-income ratio is above sector average (suggested by market data but requires verification)
- Affluent banking proposition in Prishtinë would capture material revenue
- Workforce rebalancing from 70/30 operations/sales to 40/60 is achievable within 24 months

## Data Required for Next Phase of Analysis

1. **Branch-level P&L** (revenue, direct costs, allocated costs, profit contribution)
2. **Staffing per branch** (headcount by role, FTE, salary costs)
3. **Transaction volumes per branch** (teller, ATM, digital - by transaction type)
4. **Loan portfolio EUR volumes per branch** (outstanding balances, not just counts)
5. **Deposit EUR volumes per branch** (CA, SA, TDA balances)
6. **Competitor branch mapping** (location, format, competitor branches per municipality)
7. **Customer satisfaction data** (NPS, complaints, service quality metrics)
8. **ATK municipality data** (properly parsed: turnover, employment, salary mass, declarations by municipality)
9. **Branch physical data** (size, lease cost, age, format description)
10. **Client acquisition cost and channel attribution**

---

---

# SUPPLEMENTARY SECTION: KOSOVO BANKING SYSTEM CONTEXT

---

## System-Level Digital & Payment Intelligence [DATA - from CBK payment statistics]

### Account Landscape (2025)
- **Total bank accounts in Kosovo: ~2.67-2.78 million** (growing monthly)
- Account segmentation: Individual vs. Business
- Current accounts: ~2.1-2.2M
- E-banking accounts: ~1.07-1.17M = **~51-52% e-banking penetration system-wide**
- Savings accounts: ~408K-430K (system-wide)
- Term/Fixed deposits: ~47K-48K (system-wide)
- E-money accounts: ~107K-116K (emerging)

### NLB's Digital Position in System Context
NLB's 240,157 PI clients represent approximately **8.6-9.0% of total bank accounts** in Kosovo. NLB's M-Banking penetration of 46.5% is **below the system-wide e-banking penetration of 51-52%** [DATA]. This confirms a meaningful digital gap: NLB's clients are less digitally active than the Kosovo banking average.

**Implication:** NLB is not only behind its own potential on digital adoption - it is behind the system average. Competitors (likely RBKO, TEB, PCB) are driving higher digital adoption. This has direct cost implications: NLB branches handle more manual transactions per client than the industry norm.

### Payment System Trends [DATA]
- **Monthly payment volumes: EUR 3.1B - 4.6B** across the system
- **Card transactions: 154M-181M monthly**, dominated by debit cards (130M-155M)
- **Credit card transactions: 22M-29M monthly**
- **E-commerce payments: EUR 5.8M-9.6M monthly** - rapidly growing
- **Digital wallet usage: EUR 2.9M-10.8M monthly** - explosive growth trajectory (3.7x range suggests rapid adoption)

### Strategic Implications for NLB Branch Network

1. **Digital wallet growth (3.7x range in monthly values) signals a shift away from branch-based payments.** NLB must ensure its digital platform supports wallet-to-wallet, QR payments, and e-commerce integration or risk losing transaction revenue to fintechs.

2. **E-commerce at EUR 5.8M-9.6M/month is still small but accelerating.** This creates opportunity for NLB to position card products (especially credit cards) as the e-commerce enabler. Card cross-sell in branches should emphasize online shopping utility.

3. **System-wide 51-52% e-banking penetration** means the remaining ~48% of accounts are still branch-dependent. NLB's branches in areas with older demographics or lower digital literacy (Shtërpcë, Graçanicë, rural municipalities) will remain necessary physical touchpoints even as digital grows.

4. **Debit card dominance (85% of card transactions)** suggests credit card market is underdeveloped. NLB's 24,107 credit cards + 13,761 overdrafts represent a growth opportunity if card activation and usage campaigns are executed.

### Interest Rate Environment [DATA - from CBK time series]
- Loan interest rates tracked by customer segment (Households vs. Non-Financial Corporations)
- Deposit rates tracked by account type and maturity
- Sectoral lending data available (Agriculture, Industry, Construction, Trade, Services)
- **[NOTE: Detailed rate analysis not included as branch-level rate differentiation is not available. System-level rate environment affects all branches equally.]**

### Competitive Positioning Refinement

Based on the Market Share data analyzed:

| Metric | NLB Position | Key Competitors |
|--------|-------------|-----------------|
| Total Assets | #2 | RBKO #1, BKT #3 |
| Gross Loans | #2 | RBKO #1, BKT #3 |
| Deposits | #2-3 | RBKO #1, PCB competitive |
| Loan Growth (QoQ) | Strong grower | NLB grew loans +48.9M QoQ - among fastest |
| Deposit Growth | Challenged | NLB deposits -9.2M QoQ while loans grew |
| Housing Loans | Strong #2 | NLB +9.1M QoQ housing loan growth |
| Consumer Loans | Strong | NLB +6.6M QoQ |
| Corporate Lending | #2 | NLB +33.2M QoQ - strongest corporate growth |

**Critical Finding: NLB's Loan-Deposit Imbalance** [DATA]
NLB grew gross loans by ~EUR 48.9M in one quarter while deposits DECLINED by ~EUR 9.2M. This means NLB is expanding its lending faster than its funding base. **This has two implications for branch strategy:**

1. **Deposit gathering must become a branch priority.** The SA growth (+122% YoY) is positive but the TDA decline (-43%) more than offsets it in funding terms. Branches need explicit deposit-gathering targets.

2. **The Loan-to-Deposit ratio is expanding.** [INFERENCE] If sustained, this will pressure NLB's funding costs and may require wholesale funding, reducing net interest margin. Branch strategy should balance loan origination with deposit mobilization.

**Recommended Addition to Branch KPIs:**
- Monthly net deposit inflow per branch (CA + SA + TDA)
- Deposit-to-loan ratio trend per branch
- Average deposit balance per client (when EUR data available)

---

# REVISED STRATEGIC PRIORITY LIST (incorporating system-level context)

| Priority | Action | Rationale |
|----------|--------|-----------|
| **1** | **Close digital gap to system average** | NLB at 46.5% vs system 51-52%. Cost and competitive disadvantage. |
| **2** | **Prizren/Gjakovë commercial offensive** | Largest penetration gaps in largest markets |
| **3** | **Deposit mobilization campaign** | Loan growth outpacing deposits = funding risk |
| **4** | **Business banking acceleration** | 16.9% penetration vs 77,712 businesses |
| **5** | **Card activation and e-commerce positioning** | Digital wallets growing 3.7x, e-commerce accelerating |
| **6** | **Product cross-sell in regional branches** | Prishtinë shows 2-3x higher product intensity |
| **7** | **Network expansion (Dragash, Shtime)** | Unserved markets with viable economics |
| **8** | **Workforce rebalancing** | Shift from teller to advisory as digital grows |

---

**END OF REPORT**

*This document constitutes a strategic diagnostic based on available data. All recommendations labeled [HYPOTHESIS] should be validated with additional data before implementation decisions. The analysis identifies directional opportunities and risks but does not substitute for detailed financial modeling on specific initiatives.*

*Prepared using NLB internal data (Branch Productivity), Kosovo Banking Sector data (CBK/Market Share), Kosovo Payment Statistics (CBK), and Kosovo Statistical Agency demographic data.*
