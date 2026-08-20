# 📦 其他研究 | 2026年08月21日

> 本类共 **184** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-184](./part-04.md)

---

### 1. [Position: Profiling Game Worlds by Transition Complexity](https://arxiv.org/abs/2608.18079)

**<font color=#1a73e8>作者：</font>** Lele Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Game world modeling (GWM) and reinforcement learning (RL) are often confounded because research papers rarely quantify how difficult the underlying transition prediction problem is at the declared interface (pixels/tokens/latents with finite history). We propose the Transition Complexity Profile (TCP): a small, reproducible set of metrics that characterizes an environment's (or gameplay dataset's) induced transition kernel by (i) intrinsic one-step branching, (ii) interaction-induced uncertainty and opponent influence when observable, and (iii) temporal/spatial dependency span via standardized probe curves. TCP is reported with an explicit reference distribution, protocol stochasticity, and a versioned measurement budget (sampling/resampling and fixed probe compute), enabling comparable numbers across benchmarks. We outline how common game families and modern "neural game engine" domains populate this landscape and call for TCP to become standard benchmark metadata and a required statistic in GWM and RL papers.

---


### 2. [Position: Behavioral Systems Require Behavioral Tests](https://arxiv.org/abs/2608.18081)

**<font color=#1a73e8>作者：</font>** Manuel Cherep, Nikhil Singh, Pattie Maes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial agentic systems increasingly operate as behavioral systems by interacting with dynamic environments, pursuing goals, and adapting over time. Yet, current evaluation methods largely focus on performance outcomes, not the underlying behavioral processes that produce them. This paper argues that AI agents must be evaluated like other behavioral systems: through systematic observation, perturbation, and interpretation of their actions. We draw on lessons from the behavioral sciences to motivate this position, and propose a research agenda focused on developing rigorous behavioral tests. These include methods for recovering decision strategies from action sequences, constructing environments that isolate behavioral differences, and probing emergent dynamics in multi-agent systems. Taken together, these directions offer a roadmap for developing a science of AI behavior.

---


### 3. [LongNovel: A Multi-Scale Benchmark for Hallucination Detection in Long-Context Novel Summarization](https://arxiv.org/abs/2608.18082)

**<font color=#1a73e8>作者：</font>** Ruizhi Zhang, Jinwei Chen, Xiangju Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although context windows have expanded significantly in recent years, hallucinations in long-context summarization remain a challenge. Long novels are better suited than news or papers for researching these hallucinations, due to their intrinsic information and detailed descriptions of events and dialogues. However, current research lacks a multi-scale benchmark for hallucination detection in long-context novel summarization and does not fully explore how hallucinations change as the context grows longer. In this study, we propose LongNovel, a multi-scale long-context bilingual (Chinese and English) novel benchmark for hallucination detection. This benchmark is constructed from 29 Chinese novels (ranging from 16k to 100k tokens) and chapter-level data from the BookSum dataset. We design 8 hallucination types and employ a combination of Multi-Model Arbitration and Entity-Referenced Hallucination Generation to ensure both data authenticity and a balanced distribution of hallucination categories. Furthermore, we manually revise the content in the test set to guarantee data reliability. Extensive experimental results demonstrate that LongNovel is a challenging benchmark. We release LongNovel for future research. this https URL

---


### 4. [SuTRA : Structurally-Unified Tokenization with Root Awareness](https://arxiv.org/abs/2608.18087)

**<font color=#1a73e8>作者：</font>** Vaibhav Rathore, Siddhant Gole, Dadhichi Telwadkar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing subword tokenizers optimize statistical compression but ignore morphological structure, particularly the relationship between roots and affixes. This is harmful for morphologically rich Indic languages, where basic units are complex orthographic syllables (aksharas) rather than letters. Frequency-based methods over-fragment words, arbitrarily splitting roots and affixes - a phenomenon we term Morphological Shattering. We propose SuTRA (Structurally-Unified Tokenization with Root Awareness), a morphology-aware algorithm that preserves akshara indivisibility and penalizes merges crossing morphological boundaries. We also release a new morphological segmentation dataset for Hindi, Marathi, and Gujarati. SuTRA reduces shattering, achieving peak gains of +14.7% in morphological alignment (Boundary F1) and +34% in semantic recoverability (Hindi) over BPE. These structural gains yield an average improvement of +8.08 chrF2 in machine translation.

---


### 5. [A Metamorphic Artificial Age Score Decision-Support Prototype for Flight-Log-Based Drone Propeller Health Monitoring](https://arxiv.org/abs/2608.18088)

**<font color=#1a73e8>作者：</font>** Seyma Yaman Kayadibi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drone propeller faults can create safety and reliability risks when their effects are distributed across multiple flight-log channels rather than appearing as a single diagnostic signal. This paper proposes a Metamorphic Artificial Age Score (AAS) decision-support prototype for flight-log-based drone propeller health monitoring. Using selected historical real flight logs from the 2024 DronePropA public dataset, the framework computes six health-related indicators from raw MATLAB matrices: trajectory tracking error, attitude instability, thrust-command burden, motor-command imbalance, ESC-command instability, and battery-level stress. These indicators are normalized relative to a healthy baseline and evaluated through candidate scoring policies, metamorphic adequacy relations, and a redundancy-adjusted AAS formulation. In this context, AAS is used as a structural policy-adequacy and burden measure rather than as a chronological age measure. A controlled retrospective evaluation was performed using one healthy baseline and three defective propeller cases under the same speed profile and trajectory. The healthy case was assigned to routine monitoring. The Severity 1 case was dominated by ESC-command instability and assigned to maintenance review. The Severity 2 case reached maximum motor-command and ESC-command burden, while the Severity 3 case reached maximum trajectory tracking error; both triggered mandatory inspection. The results show that propeller fault effects may appear through different operational channels, supporting the need for a multi-indicator decision-support layer for post-flight maintenance prioritization and autonomous-system oversight.

---


### 6. [BERTilda: Explainable Topic Lifecycle Tracking with Split/Merge Detection via Similarity-and-Flow Temporal Graphs](https://arxiv.org/abs/2608.18101)

**<font color=#1a73e8>作者：</font>** Cláudia Oliveira, Álvaro Figueira  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Longitudinal text streams exhibit topic birth and death, but also discrete structural reorganizations in which themes split into subtopics or merge into broader narratives. Many dynamic topic models emphasize smooth drift, while snapshot topic models (fit independently per time window) leave temporal correspondence underspecified. We present BERTilda, an explainable framework that discovers topics independently in each window (using an embedding-based topic model) and then constructs a temporal topic graph linking topics across adjacent windows. Links are supported by two complementary signals: (i) semantic similarity between topic representations and (ii) a bidirectional coverage signal that estimates document outflow (where a topic goes) and inflow (where a topic comes from) via cross-window tweet-to-topic attribution. Graph-based rules label continuations, splits, merges, disappearances, and unclear transitions. We evaluate BERTilda on political corpora, including U.S. congressional tweets and historical speech datasets, report topic-quality and temporal-stability diagnostics, and validate lifecycle labels on a gold-standard subset annotated by three independent annotators. On the annotated subset, BERTilda reaches majority agreement rates up to 87% and attains the highest macro-average agreement across the compared methods, with particularly strong disappearance detection relative to similarity-only and forward-only baselines.

---


### 7. [Operationalizing Narrative Entropy (Sn): A Two-Scene Registered Pilot Report and Pre-Validation Protocol](https://arxiv.org/abs/2608.18109)

**<font color=#1a73e8>作者：</font>** Levent Bulut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Narrative Entropy ($S_n$) is a proposed quantitative descriptor within the Bulut Doctrine, intended to capture the rate at which a narrative text imposes processing load on a reader. To date the construct has been defined theoretically but not operationalized against real texts. This report documents the first such operationalization (the v2.0 pilot): two narrative scenes -- the opening restaurant scene of Tarantino's Reservoir Dogs and the opening interior-monologue block of Carver's Cathedral -- were coded manually by a single rater and scored with the candidate formula $S_n = I_f \times C_b \times t$. The result was a divergence from the author's naive intuition: the single-voice monologue ($S_n = 30.0$) scored higher than the nine-character dialogue scene ($S_n = 18.8$). We treat this not as a result to be explained away but as the central finding, and we refuse post-hoc adjustment of the formula. Three competing interpretations are presented -- formula incompleteness, genuine high-load prose, and measurement error -- and the design that would discriminate among them is pre-registered. This v2.1 revision adds: (i) explicit acknowledgement that the divergence is consistent with the pre-existing architectural framework which privileges inferential reconstruction over surface declaration, and that what was called "contrary to expectation" in v2.0 reflected the author's anticipatory intuition rather than the methodology's own predictions; (ii) a pre-registered construct validity test for $I_f$, motivated by the observation that $I_f$ values were nearly equal across the two scenes (1.71 vs 1.58) despite the headline $S_n$ divergence. The document functions simultaneously as a pilot report ($n=2$) and as a pre-registration of the next-stage protocol. It does not claim that $S_n$ has been validated.

---


### 8. [Emergence of Agentic AI: A Review on Evolution, Background, Working Principles, Applications, Adoption Factors, and Future Research Directions](https://arxiv.org/abs/2608.18110)

**<font color=#1a73e8>作者：</font>** AKM Bahalul Haque, Al Amin Islam Ridoy, Mohammad Rayhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI is gaining new insights and advancements in the field of Artificial Intelligence, fostering significant potential to enable rapid transformation across various this http URL rapid advancement and the potential to revolutionize various domains advocate the need for a deeper understanding and firm grasp of the technology. Moreover, an investigation into state of the art research directions in agentic AI needs to be conducted to comprehensively assess the potential scope for improvement and this http URL, to address these objectives, a comprehensive review can provide researchers and practitioners with valuable insights into the current state and future research scopes of agentic this http URL, this work considers the recently published scholarly contributions in agentic AI across various domains and discusses the fundamentals and working principles of Agentic AI, traces the historical and theoretical evolution of agency in artificial systems, explores and discusses Agentic AIs architecture, working principles, and functionalities, explores real-world applications of Agentic AI across various domains, analyzes the research findings, identifies current challenges, and discuss potential future research directions, and proposes a comprehensive framework of stakeholders intention to use and adopt Agentic AI with the help of proposed system quality this http URL, this systematic review provides researchers and practitioners with a comprehensive understanding of Agentic AI, its current developments and applications, highlights key research gaps, and outlines future research directions.

---


### 9. [Position: AI Leaderboards Are Underserving the Global South: A Case Study from India](https://arxiv.org/abs/2608.18117)

**<font color=#1a73e8>作者：</font>** Sourav Banerjee, Saikat Saha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that AI leaderboards are structurally ill-suited to serving the Global South because they lack independent governance, conflict-of-interest policies, and mechanisms for metric evolution. The barrier is not missing data; high-quality regional benchmarks already exist: IndicSUPERB, MILU, and LAHAJA for India; IrokoBench for Africa; AlGhafa for Arabic. The barrier is institutional design. Global leaderboards do not include these benchmarks, and no governance mechanism compels them to do so. Commercial pressure corrects leaderboard failures when paying customers in the Global North are affected. The Global South lacks equivalent leverage. Without governance, failures affecting Hindi, Swahili, or Arabic speakers persist indefinitely as documented but unaddressed gaps. Using India as a case study (1.4 billion people, 22 scheduled languages, high-quality benchmarks, but no trusted aggregation), we report findings from a consultation with 58 AI practitioners showing consistent preference for formal governance and disclosure-based conflict management. The solution is not more data but better institutions: regional leaderboards with independent governance from the start.

---


### 10. [Optimized Fuzzy Logic Approach with the IEEE Key Gas Method for Diagnosing Power Transformer Faults Using Dissolved Gas Analysis](https://arxiv.org/abs/2608.18133)

**<font color=#1a73e8>作者：</font>** Kim-Anh Nguyen, Huy Hoang Le, Ba Tu Phung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable transformer fault diagnosis is essential for maintaining power system stability. The IEEE Key Gas Method (KGM), a widely utilized approach in Dissolved Gas Analysis (DGA), exhibits limitations in addressing ambiguous data and ensuring high diagnostic accuracy. This study presents An enhanced model combining Fuzzy Logic with the IEEE Key Gas Method (FL-KGM) that introduces refined membership functions, optimized fuzzy rule sets, and a novel separation of CO and CO2 to eliminate diagnostic inconsistencies. By leveraging multidimensional gas ratio analysis and an adaptive classification framework, FL-KGM delivers superior fault identification and classification. Experimental validation utilizing real-world datasets demonstrates that FL-KGM achieves up to 98.6% accuracy, significantly outperforming KGM and other FL-based approaches. These findings elucidate the potential of FL-KGM in advancing transformer monitoring, enabling intelligent fault detection, and enhancing predictive maintenance strategies in modern power systems.

---


### 11. [Improving Rural Medication Safety with AI: A Scoping Review](https://arxiv.org/abs/2608.18135)

**<font color=#1a73e8>作者：</font>** Jeong-ah Kim, Muhammad Ashad Kabir, Daniel Terry 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Introduction: Medication errors (MEs) represent a significant threat to global healthcare systems, contributing to patient harm. Introducing artificial intelligence (AI) in rural healthcare enhances patient safety. The aim is to explore the applications and effectiveness of AI technologies in enhancing patient safety and reducing medication errors in rural health settings.
Methods: A scoping review was conducted through a systematic literature search spanning 2012 to 2025 across multiple databases, including EBSCohost, Emcare (Ovid), MEDLINE, and the ProQuest Consumer Health Database. Twelve primary studies from nine different nations were examined. Data were analysed thematically to obtain insights on AI interventions across the medication process.
Results: AI technologies have been integrated into every stage of medication management, right from prescribing and dispensing to administration and post-administration monitoring. Four key themes came to light: (1) the various types of AI being utilised (like Clinical Decision Support Systems, Machine Learning, Natural Language Processing, and smart pumps); (2) the phases of the medication process that are affected; (3) how effective these technologies are in minimising errors and boosting workflow safety; and (4) rural-specific challenges including infrastructure, staff training, system integration, and alert fatigue. Several studies have demonstrated that machine learning-based surveillance improves incident detection and reduces prescribing and transcription errors by an impressive 34% to 80%. Barriers included lack of governance frameworks, financial limitations, and clinician resistance, which still present major obstacles.
Conclusion: In rural healthcare, AI technologies hold great potential for enhancing pharmaceutical safety. They can allow data-driven monitoring, automate processes, and offer clinical decision assistance.

---


### 12. [RDFdL: Integrating RDF with Differential Dynamic Logic](https://arxiv.org/abs/2608.18165)

**<font color=#1a73e8>作者：</font>** Yuyang Li, Lukas Kubelka, Julia Butte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs modeled in RDF are powerful for describing static knowledge, but they cannot capture or reason about the dynamic behavior of physical systems, e.g., systems described by differential equations, which is a critical gap for AI-driven cyber-physical systems. To solve this, we propose RDFdL, a framework that integrates RDF with Differential Dynamic Logic (dL) to represent and reason about both static knowledge and the continuous dynamics of physical systems. For the dynamic part, we syntactically represent differential equations and ranges in the state space in RDF and SHACL and provide semantics using a translation to dL. Linking RDF and dL through their shared foundation in first-order logic achieves a unique integration: verification results for safety and reachability properties in the dynamic logic domain become available as entailment to SPARQL queries over RDF data. We implement the pipeline using Apache Jena for ontology-driven RDF reasoning and KeYmaera X, the theorem prover for dL, and sketch its applicability in manufacturing.

---


### 13. [Towards Reversible Forgetting: Managing Obsolete Knowledge in Continual Enterprise AI Agents](https://arxiv.org/abs/2608.18177)

**<font color=#1a73e8>作者：</font>** Nilutpaul Sarker Yash, Tirtho Roy, Ushashi Bhattacharjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning has traditionally treated forgetting as a failure, emphasizing preservation of previously acquired knowledge as environments evolve. We argue that this objective is incomplete for enterprise AI agents operating in non-stationary environments, where customers, policies, tools, workflows, regulations, and market conditions change over time. Indiscriminate retention can allow obsolete knowledge to influence decisions, creating negative transfer and operational risk. We therefore propose reversible forgetting: a conceptual framework with three operational memory states: active, dormant, and retired, and a reactivation transition that can restore dormant knowledge when its relevance returns. We instantiate the framework as a Hysteretic Reversible Memory Controller that accumulates relevance evidence, uses asymmetric thresholds to prevent state oscillation, tests reactivation in shadow mode, and gates retirement through policy. The framework reduces the influence of obsolete information without conflating temporary suppression with permanent erasure. Finance illustrates the idea: knowledge useful under one market regime may become harmful under another yet regain relevance when similar conditions recur.

---


### 14. [H$^2$EDL: Hyper Evidential Deep Learning for Hierarchical Classification](https://arxiv.org/abs/2608.18185)

**<font color=#1a73e8>作者：</font>** Yuanye Liu, Xiahai Zhuang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-grained recognition often involves hierarchical label spaces, where a model may be confident about a coarse semantic concept while remaining uncertain among its descendant classes. Such structured ambiguity requires uncertainty representations that capture both fine-grained classes and intermediate concepts. However, existing tools each capture only half of it: flat evidential classifiers quantify total ignorance with a single vacuity on the leaf frame, and hierarchical classifiers propagate point probabilities with no notion of evidence. Hyper-opinions would unify the two, but their general form is exponential in the label count, and existing hyper-evidential networks either require composite labels to be supplied in the training data or read them off an unstructured weight pattern, with no principled notion of which composites deserve mass. We observe that the taxonomy itself is the missing hyperdomain. Its subtrees and leaf singletons form a linear-size focal family, and one local Dirichlet opinion per branching node induces every composite mass in closed form. The resulting model, H$^2$EDL, can be interpreted in two complementary ways using the same set of parameters. From a prediction perspective, it functions as a hierarchical classifier that preserves consistency across different levels of the label tree. From a probabilistic perspective, it defines a valid tree-structured hyper-opinion, where the mass assigned to each node represents the belief that reaches that node but does not provide sufficient confidence to further specialize into its descendants. On FGVC-Aircraft and DERM12345, H$^2$EDL reduces calibration error by approximately half compared with cross-entropy baselines, with the improvement becoming more pronounced at deeper hierarchy levels and under larger training budgets.

---


### 15. [What Can Artificial Intelligence Learn from Medicine? Generative Analogies and Reliable Machine Learning Systems](https://arxiv.org/abs/2608.18186)

**<font color=#1a73e8>作者：</font>** Emanuele Ratti, Lena Zuchowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the past few years, machine learning (ML) has been widely (and to an extent, successfully) implemented in medicine. However, uncertainties surrounding ML have made it difficult to establish the bases of its epistemic and methodological warrants. In the literature, a parallel has been drawn between medicine and ML, suggesting that we should model epistemic and methodological standards for ML on the standards of clinical translation. By developing tools from Hesse work, we characterise the nature of this parallel as a generative analogy between the process of clinical translation and the process of building ML systems. We identify more precisely the epistemic and methodological warrants of clinical translation that are typically only mentioned when appealing to the analogy, and we show in which sense such warrants apply analogically to the context of ML. In particular, we interpret warrants of clinical translation in reliabilist terms, and we show how this can inform a new form of ML reliabilism, which is distinct from (though compatible with) existing reliabilist accounts in philosophy of AI.

---


### 16. [AdaRare: Telemetry-Guided Joint Profile Control for Greybox Fuzzing](https://arxiv.org/abs/2608.18187)

**<font color=#1a73e8>作者：</font>** Jingchuan Ma, Tongan Liu, Yanhua Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Greybox fuzzers combine interacting queue, mutation, dictionary, energy, and comparison-solving control surfaces, while prior adaptive systems typically optimize other decision objects or control layers. We present AdaRare, an AFL++ extension that coordinates five internal actuation mechanisms as one bounded in-process profile updated every 5,000 ms. Completed-window, action-induced telemetry feeds an arm-local recency-weighted linear scorer and a profile-conditioned controller target. The scorer borrows the algebraic structure of disjoint LinUCB, but serves as a closed-loop profile-ranking mechanism rather than a calibrated contextual-bandit action-value estimator or statistical confidence bound.
Across three sequential repeated-trial phases, Main provides broad integrated-system evidence: AdaRare has higher median edge coverage than vanilla AFL++ on all eight targets, with five Holm-significant comparisons. In the strongest matched result, Full AdaRare has higher median edge coverage than CmpLog-matched AFL++ on all five follow-up targets, with four Holm-significant comparisons. Batch A finds higher medians for telemetry-guided selection than fixed-context, random, and round-robin schedules in all 15 target-control comparisons, with 13 Holm-significant comparisons. The experiments do not establish independent No-A6-versus-Shadow or scarcity-bundle effects; A6 evidence is target-dependent and weakens under batch-wide correction. In an unmatched firmware case study, AdaRare-generated inputs exposed five distinct memory-corruption findings, each reproduced in a separate environment and later assigned a CVE identifier. Controller-boundary compute P99 medians are below 6.5 ms for a five-second window; complete-boundary P99 medians including synchronous logging are below 14.7 ms. These measurements characterize boundary latency, not total system overhead.

---


### 17. [A systematic review of machine learning techniques to address diagnosis and treatment of autism: challenges and opportunities](https://arxiv.org/abs/2608.18188)

**<font color=#1a73e8>作者：</font>** Rafael Muñoz-Terol, Jesús Peral, Sandra Amador 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autism spectrum disorder (ASD) is a developmental disability characterized by challenges in social interaction and communication. As the causes of ASD remain unclear, identifying relevant features and hidden correlations is crucial for early diagnosis. This systematic review evaluates 55 studies from 2017 to 2023 on the application of machine learning (ML) techniques to ASD. The primary objective is to examine recent ML applications in ASD research, identifying trends, techniques, and datasets that enhance diagnosis and treatment. Supervised learning methods dominate, as they align well with ASD diagnostic needs; however, the role of deep learning is expanding with greater data availability. Emerging techniques based on hybrid methods, where unsupervised, deep learning, and fuzzy logic could be included, will be interesting to observe in the future. The review highlights key challenges and opportunities, particularly the need for models that can integrate complex data -such as genetic and clinical information- to improve diagnostic accuracy and treatment outcomes. Additionally, incorporating innovative data sources, like wearable devices and biometric sensors, could enable continuous and non-intrusive monitoring, providing a more holistic understanding of ASD. Findings emphasize that addressing current challenges requires interdisciplinary collaboration and expanded datasets tailored to ASD. Future ML models will benefit from broader multimodal data integration, enabling researchers to more comprehensively address the complexities of ASD.

---


### 18. [Safe Domain Adaptation for Physics: Overcoming Nuisances, Label Shifts, and Simulation Priors](https://arxiv.org/abs/2608.18190)

**<font color=#1a73e8>作者：</font>** Ivan Kharuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain adaptation is widely used to make neural networks trained on simulations applicable to experimental data. Its premise is that the two domains differ only in nuisances, and that the quantity of interest is distributed identically in both. In physics neither assumption holds: simulations can be wrong about the physics, and the distribution of the target quantity - an energy spectrum, a redshift distribution - is often the measurement itself. We study the consequences of such mismatches on a toy air-shower benchmark in which a detector-response nuisance, a physical simulation shift, and an energy-spectrum shift can be switched on separately or together. Standard adversarial adaptation handles the conditional shifts, but once the two spectra differ it aligns them, replacing an uncontrolled bias by one anchored on the simulation prior. We present adaptive domain adaptation, which reweights the simulated events so as to focus domain adaptation on the genuine physical mismatch alone. Since the predicted spectrum depends on model training configuration, we provide a label-free model selection rule for selecting the near-the-best operation point.

---


### 19. [ChiroEcho: extending automated bat vocalisation classification beyond the learned taxonomy](https://arxiv.org/abs/2608.18191)

**<font color=#1a73e8>作者：</font>** Burooj Ghani, Welmoed Eversteijn, Milan van Hirtum 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bats are key indicators of ecosystem health and are protected throughout Europe, making reliable population monitoring a conservation priority. Their cryptic nocturnal lifestyle makes passive acoustic monitoring essential, yet automated identification remains difficult as echolocation calls vary with behaviour and environment and overlap among species. We present a deep learning framework that jointly predicts species and genus and combines genus predictions with geographic species distributions at inference. When only one species of a predicted genus occurs in a region, the framework can resolve species absent from the learned taxonomy. This reframes geographic information as a means of extending, rather than constraining, a classifier's effective taxonomy. Using recordings spanning 35 European bat species, we evaluate closed-set classification, examine the instability of performance estimates for sparsely represented species, and conduct a controlled held-out proof-of-principle experiment. The rare-species analysis shows how limited evaluation data can obscure species-level performance, while the held-out experiment shows that genus predictions and location can recover labels unavailable to the species head. Geographic resolution extends operational coverage from 35 to 41 of the 48 native European bat species, increasing coverage from 73% to 85%. To our knowledge, this is the broadest operational coverage reported for automated European bat classification. More broadly, the bat framework provides proof of principle for resolving unseen fine-grained classes by combining coarse predictions with transparent external constraints.

---


### 20. [Bound-Aware Per-Organ Recall Risk Control for Multi-Organ CT Segmentation under Clinical Domain Shift](https://arxiv.org/abs/2608.18193)

**<font color=#1a73e8>作者：</font>** Souraj Adhikary, Negar Chabi, Andre Mastmeyer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution-free risk control adds organ-specific recall guarantees to frozen segmentation. We calibrate per-organ thresholds for an AMOS-trained nnU-Net, audit transfer to RAOS, and estimate local re-certification cost using case-level voxel false-negative rate (FNR). The AMOS control passes, but $7/12$ organs exceed $\alpha{=}0.10$ after transfer; smaller calibration sets can mask exceedances with conservative or vacuous thresholds. Risk-Controlling Prediction Sets (RCPS) give high-probability control of population-mean risk, whereas Conformal Risk Control (CRC) gives weaker expectation control. Both require exchangeability; fixed and global thresholds give no per-organ guarantee. The Waudby--Smith--Ramdas (WSR) betting bound re-certifies six Tier-1 organs with 25 local cases, versus 30--40 for Hoeffding--Bentkus (HB). CRC needs 10--15 but has a heavier individual-case tail. No Tier-2 organ meets our illustrative precision criterion with 25 cases.

---


### 21. [On the Triangle Inequality for the Jaccard Distance in Arbitrary Lattices](https://arxiv.org/abs/2608.18194)

**<font color=#1a73e8>作者：</font>** Costin Bădică, Amelia Bădică  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents new theoretical results on generalizing the Jaccard distance for lattices and real valuations. We demonstrate that when the valuation is strictly positive, monotone, and modular, the Jaccard distance satisfies the triangle inequality on arbitrary lattices, effectively generalizing earlier results that depended heavily on distributivity. Moving to relatively complemented distributive lattices (which safely drop the requirement for the global bounds found in Boolean algebras), we prove the triangle inequality holds as long as the valuation is positive, monotone, supermodular, and $\log$-submodular. Additionally, we adapt the symmetric-difference Jaccard formulation for submodular valuations to sectionally complemented distributive lattices. Shifting to necessary conditions, we prove that supermodularity is a strict requirement for the standard generalized Jaccard distance to operate as a valid metric. Finally, we map the practical value of relaxing these structural constraints to computational fields like quantum information theory, formal concept analysis, and machine learning, closing with a brief look at open mathematical problems.

---


### 22. [LumiTokens: 3D Relighting via Token-Space Lighting Transformation](https://arxiv.org/abs/2608.18215)

**<font color=#1a73e8>作者：</font>** Yiwen Chen, Matheus Gadelha, Huaizu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D relighting methods operate through either explicit material decomposition, diffusion-based view-space generation, or a combination of both, requiring full recomputation for each new lighting condition. We observe that recent latent scene representations, which encode multi-view images into a set of compact tokens with no fixed physical semantics, open up a novel design space for relighting. We present LumiTokens, a framework that formulates 3D relighting as a direct transformation on latent scene tokens, without explicit 3D representations, rendering equations, or physics-based decomposition. Our model introduces a Scene Token Editor that processes scene tokens jointly with light-ray tokens through self-attention, producing updated tokens that can be decoded into multi-view-consistent relit images. To support diverse lighting types through a unified interface, all lighting signals, including environment maps, point lights, and area lights, are parameterized as Plucker ray tokens, enabling native 3D user interaction with a representation that carries no explicit spatial structure. Crucially, this design supports progressive relighting: because the editor's output remains in the same latent space as its input, a user can incrementally build up illumination one light source at a time, with each edit composing in token space. Experiments demonstrate that LumiTokens achieves comparable or superior relighting quality to other methods and supports progressive, composable lighting edits. Project page: this https URL

---


### 23. [Think Shallow, Solve Deep: Controlling Recurrent Dynamics for Reliable Test-Time Depth](https://arxiv.org/abs/2608.18222)

**<font color=#1a73e8>作者：</font>** Ivan Viakhirev, Kirill Borodin, Amirah Almutairi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent-depth reasoners aim to solve harder problems by iterating their update longer at test time, but additional iterations can improve, preserve, or degrade an answer. We show that a measurable property of the trained operator, its finite-time dynamical regime (estimated as settling, marginal, or drifting), indicates which of these occurs. We give a sufficient condition for depth-safety: once an operator's per-step displacement is small relative to the decoder margin, the decoded answer cannot change under further iterations. Empirically, on algorithmic tasks trained from $800$ unaugmented examples per difficulty tier, settling operators do not degrade with added depth, and on some tasks convert it into higher accuracy on harder unseen instances (Sudoku, $0.19$ to $0.34$ past the training horizon). A single terminal fixed-point objective moves the regime and the depth behavior together: removing it induces drift and removes the gains, and adding it to a generic recurrence yields depth-safe extrapolation on carry propagation. We give four operational criteria for useful test-time depth, use them to catalogue failure modes, and, as a consistency check, apply the same measurements to Huginn-3.5B, which falls in the non-settling family.

---


### 24. [Classifying Directional Trajectories Near Criticality in the Three-State Majority-Vote Model with Deep Belief Networks and Bidirectional GRUs](https://arxiv.org/abs/2608.18235)

**<font color=#1a73e8>作者：</font>** Mauricio A. Valle, Gonzalo A. Ruz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we investigate whether the latent representations learned by a Deep Belief Network (DBN) and a Bidirectional Gated Recurrent Unit (Bi-GRU) can discriminate among four dynamically distinct trajectory types in the three-state majority vote model (MV3): approach from disorder, approach from order, departure to disorder, and departure to order. The DBN, pre-trained in an unsupervised manner on static equilibrium samples via a Gaussian-Bernoulli Restricted Boltzmann Machine input layer and architecture $784 \to 4096 \to 225 \to 81$, encodes each lattice snapshot into an 81-dimensional latent vector. A t-SNE analysis of the DBN latent space reveals only partial separation of the four trajectory types, reflecting the fact that a model trained on static configurations cannot fully resolve directional temporal structure. A two-layer Bi-GRU classifier, trained on sequences of DBN-encoded snapshots of length $T = 50$, achieves near-perfect separation of all four trajectory types in its hidden state space, as confirmed by t-SNE visualization on both training and test sets. Furthermore, a sliding-window application of the trained Bi-GRU to continuous MV3 dynamics demonstrates its ability to sense the system's current dynamical regime in real-time. These results establish a principled hierarchical architecture for detecting and classifying critical transitions in agent-based opinion dynamics models.

---


### 25. [GenEx: A Graph-Based Representational Paradigm for SARS-CoV-2 Variant Detection via Codon Co-occurrence Networks](https://arxiv.org/abs/2608.18238)

**<font color=#1a73e8>作者：</font>** Arefin Amin, Labiba Faiza Karim, M. Monir Uddin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Genomic analysis on viruses such as SARS-CoV-2 variants: Beta, Gamma, Delta, and Omicron is heavily dominated by classical bioinformatics methods, including Sequence Alignment, Phylogenetic Analysis, and Mutation Frequency Statistics. These approaches use pairwise codon or nucleotide distance matrices to analyze gene sequences, treating them as linear strings rather than capturing their complex contextual interdependencies. We proposed GenEx, a pipeline that converts raw gene sequences into codon co-occurrence graphs and extracts more than 25 graph features. Our two most prominent techniques for graph generation and feature extraction are MSCG (Multi-Scale Codon Co-occurrence Graph) and LAPCG (Linear-time Adjacency PMI Codon Graph). Using these algorithms, we treated codon sequences as structured symbolic vocabularies interpretable to codon co-occurrence graph analysis, a representational paradigm borrowed from computational linguistics. Another major contribution includes implementing a spectral graph feature extraction using Singular Value Decomposition (SVD), using the squared singular value ($\sigma^2$) instead of the traditionally used eigenvalue, which helped us to amplify the separation between dominant and subdominant spectral components, thereby enhancing inter-class separability in downstream classification. And to further demonstrate that our method works, we trained 23 benchmarked ML models against the latest SARS-CoV-2 variants, achieving remarkable results in detecting all SARS-CoV-2 variants.

---


### 26. [Zero-Shot Transfer of Force Map Estimation Across GelSight Mini Sensors](https://arxiv.org/abs/2608.18240)

**<font color=#1a73e8>作者：</font>** Julio Castaño Amoros, Pablo Gil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid industrialization of the touch sensor manufacturing process, most of these sensors are still handmade in research laboratories. This complicates standardizing their performance, requiring the repetition of data collection and training models for each unit produced. To address this problem, this paper presents a method that can generalize the estimation of 3D force maps across different GelSight Mini sensor units, regardless of the sensor version. Specifically, the method consists of two stages: a domain adaptation stage, in which the input tactile image is reconstructed as a general tactile image using a UniT-based model; and a stage for estimating 3D force maps employing a U-Net network. Our proposal achieves promising results in both steps, such as an SSIM of 0.9338 +- 0.0358 in the image reconstruction phase and an MAE_F of 1.1294 +- 1.5934(N) in the force estimation phase.

---


### 27. [Bidirectional representational alignment between biological and artificial neural networks](https://arxiv.org/abs/2608.18244)

**<font color=#1a73e8>作者：</font>** Samuel Kostousov, Abhinn Kaushik, Brokoslaw Laschowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that representational alignment between biological and artificial neural networks is asymmetric: model representations predict neural responses much better than neural responses predict model representations. This asymmetry raises the question of whether representational geometry contributes to bidirectional representational alignment. We hypothesized that steering representational geometry during training can systematically influence bidirectional alignment. To test this hypothesis, we developed a computational framework that integrates spectral regularization with bidirectional predictivity analyses. As an initial demonstration, we evaluated our framework using self-supervised contrastive vision models. Steering the spectral geometry of the learned representations substantially increased reverse predictivity with modest reductions in forward predictivity, yielding a 55% relative improvement in bidirectional predictivity. These improvements were accompanied by reduced effective dimensionality and a reorganization of the shared representational subspace, within which forward and reverse predictivity became approximately symmetric at intermediate spectral exponents. Overall, these findings demonstrate that representational geometry can be systematically steered to modulate bidirectional representational alignment between biological and artificial neural networks.

---


### 28. [Visual-Prompt Guided Wildlife Instance-Level Recognition](https://arxiv.org/abs/2608.18246)

**<font color=#1a73e8>作者：</font>** Mufhumudzi Muthivhi, Jiahao Huo, Terence van Zyl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained wildlife re-identification remains a challenging area in research. Current state-of-the-art approaches apply a detection and re-identification pipeline. We propose a one-stage end-to-end detection and re-identification model that performs identity searching within the latent space. We adopt DINOv2 for robust spatial geometry and MegaDescriptor for wildlife re-identification. We enhance latent queries with prompt re-identification features. A detection decoder queries the scene latent space to establish object boundaries around the target identity. Preliminary findings reflect a competitive mean average precision score of 30.584% compared to the state-of-the-art two stage approach of 44.89%. Qualitative results depict effective bounding and identification of animal identities.

---


### 29. [Model Card for OpenAI Privacy Filter](https://arxiv.org/abs/2608.18274)

**<font color=#1a73e8>作者：</font>** Charles de Bourcy, Sahra Ghalebikesabi, Avi Schwarzschild 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> OpenAI Privacy Filter is a compact, bidirectional token-classification model for detecting and redacting personally identifiable information (PII) and secrets in unstructured text. The model is derived from an autoregressively pretrained checkpoint and converted into a bidirectional, banded-attention classifier that labels an input sequence in a single forward pass. A constrained Viterbi decoder produces coherent spans across eight privacy categories and exposes configurable operating points for precision-recall tradeoffs. Privacy Filter has 1.5 billion total parameters, 50 million active parameters per token, and a 128,000-token context window. It is designed for efficient local deployment and domain-specific fine-tuning. Privacy Filter is intended as a configurable data-minimization component within layered privacy workflows, not as an anonymization or compliance guarantee.

---


### 30. [Acquisition Geometry-Assisted Whole-Group Localization of X-ray Fluorescence Maps in Optical Microscopy Images](https://arxiv.org/abs/2608.18305)

**<font color=#1a73e8>作者：</font>** Xiangyu Yin, Tatjana Paunesku, Letonia Copeland-Hardin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray fluorescence (XRF) microscopy maps elemental distributions, while optical microscopy can provide complementary morphological context. Localizing XRF fields of view (FOVs) in optical images is difficult because the two modalities differ in contrast mechanism and resolution. Most current workflows place each XRF tile independently, even when acquisition metadata already record the tiles' relative scan positions. This study formalizes XRF tile-group localization, in which one optical-frame placement is estimated for the whole group, constrained by acquisition geometry and quantified using group intersection-over-union (GroupIoU). In a controlled case study, independent localization failed with GroupIoU 0.000, whereas group localization achieved 0.931. Replacing the normalized cross-correlation (NCC) metric with mutual information (MI) gave nearly identical results, showing that the outcome is not specific to one local similarity metric. In another multiscale case study, using a coarse XRF survey scan to connect the fine-scale tile group to the optical image increased mean GroupIoU from 0.694 to 0.856. These case studies support using acquisition geometry as an explicit constraint when localizing related XRF tiles.

---


### 31. [High-Flux Count-Free Single-Photon 3D Cameras](https://arxiv.org/abs/2608.18306)

**<font color=#1a73e8>作者：</font>** Kaustubh Sadekar, Vivek K Goyal, David Maier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-photon cameras based on single-photon avalanche diode (SPAD) technology are gaining popularity for 3D sensing, thanks to their extreme sensitivity and time resolution. There are two key challenges with single-photon cameras that limit their widespread use: (i) they suffer from non-linear distortions called ''pile-up'' when operated in high-photon-flux conditions, and (ii) they generate a large volume of raw photon data, creating a severe data bottleneck at each sensor pixel. In this work, we show that while compressive capture techniques successfully mitigate data transfer challenges, they exacerbate the effects of dead-time distortion because they fail to retain sufficient information about the photon detection history to allow post-processing pile-up correction via existing methods. We propose a new computational-imaging method that combines free-running capture with an analysis-by-synthesis software pipeline to mitigate pile-up distortions. Our results with hardware emulations and full-scene and single-pixel simulations show that our method can reliably capture scene distance and reflectance over a wide range of illumination conditions. Our work will enable high-resolution SPAD cameras that are severely bandwidth-constrained to operate in real-world high-flux scenarios.

---


### 32. [FedCoRe: Target-Adaptive Completion for Missing Modalities in Healthcare Federated Learning](https://arxiv.org/abs/2608.18311)

**<font color=#1a73e8>作者：</font>** Holger R. Roth, Ziyue Xu, Peter Cnudde  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated multimodal models often assume every site has every modality, although hospitals differ in access to EHRs, chest radiographs, and ECGs. We study this setting on a MIMIC-derived respiratory deterioration task with simulated FL clients and introduce FedCoRe (Federated Cross-Modal Representation Completion). FedCoRe learns representation- or logit-space corrections rather than generating synthetic ECGs or CXR images. When a client observes a modality that may be missing at deployment, it evaluates the same example with and without that modality to obtain paired supervision. Only clients with such pairs update the completion module, and validation may retain the unchanged prediction. We freeze the trained multimodal predictor during evaluation so that measured differences come only from completion. Hiding ECG reduced AUROC by about 0.085; paired-example FedAvg restored 0.0415 AUROC, or 49.0% of the lost performance. We therefore report two distinct effects: paired-example FedAvg partially recovers the missing-ECG gap, while validation-selected completion is a task-specific classifier-logit correction rather than literal ECG recovery. For CXR, effect-aware completion recovers 52.8% of the loss in a controlled test where CXR is hidden. Paired-example FedAvg transfers part of this effect, but validation keeps the no-completion baseline for deployment cases whose inputs lack CXR. Thus, FedCoRe should be read as a validation-gated completion/correction framework: it can recover missing-modality signal in supported settings, but it should be deployed only when paired examples and validation evidence support that modality.

---


### 33. [Artifact-centered Claim-aware Observability for Autonomous Scientific Agents](https://arxiv.org/abs/2608.18312)

**<font color=#1a73e8>作者：</font>** Xiangyu Yin, Ming Du, Michael H. Prince 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous scientific agents now increasingly propose ideas, write code, run experiments, analyze results, and even draft papers. Observe and audit those agents are necessary but logging every model call is not enough, scientists also need to inspect the artifacts and claims that the systems produced and their relations. This is driven by the fact that failures in scientific agent systems are often distributed across several objects. A manuscript claim may cite the wrong evidence, a search process may select a degenerate candidate, a laboratory novelty claim may depend on an unstated rule, or a multi-agent plan may change without a visible trigger. Existing tracing, experiment tracking, and archival provenance tools are valuable, but their native objects do not make these scientific audit relations first-class. We argue that autonomous scientific systems should emit portable, claim-aware artifact lineage as a minimum audit layer. We propose a compact observability profile organized around individuals, operators, fitness records, lineage, archives, runs, streams, and steering commands. In this profile, scientific claims are ordinary individuals with explicit evidence bindings and verification records. The profile is intended as a semantic layer that complements current telemetry and provenance standards. Execution details can remain in OpenTelemetry. Final packages can export to PROV-O or RO-Crate standards.

---


### 34. [A Configurable Privacy-Preserving MRI Processing Workflow Using Deep Learning-Based Brain Extraction and Adaptive Anatomical Preservation](https://arxiv.org/abs/2608.18316)

**<font color=#1a73e8>作者：</font>** Rayeef Ali Khan, Komal Raj Mahantesh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structural Magnetic Resonance Imaging (MRI) is widely used in neuroimaging research and clinical practice, but structural MRI volumes may retain facial and cranial anatomical information that raises privacy concerns. Existing deep learning-based brain extraction methods generally produce a single fixed output, limiting flexibility when different applications require different balances between privacy and anatomical preservation. This paper presents a configurable privacy-preserving MRI processing workflow that extends deep learning-based brain extraction through adaptive anatomical preservation, interactive preservation selection, and integrated quality control. The workflow employs SynthStrip for automated brain extraction, followed by morphological mask expansion to generate configurable shell-based preservation levels. An Interactive Preservation Framework enables users to compare preservation configurations and select an appropriate output, while an integrated Quality Control Framework provides multi-plane visualisation and brain-mask overlay verification. The workflow was implemented in Python using open-source neuroimaging libraries within the Renku reproducible research environment and evaluated using structural T1-weighted MRI data from the publicly available IXI dataset. Experimental results demonstrate anatomically plausible brain extraction and configurable preservation outputs, supported by systematic visual verification. The principal contribution is a modular and reproducible MRI preprocessing framework that enhances deep learning-based brain extraction with configurable anatomical preservation, interactive user-guided processing, and integrated quality control. The workflow provides a practical foundation for privacy-oriented neuroimaging research and collaborative medical image analysis.

---


### 35. [Reproducible Multimodal Affordance Prediction](https://arxiv.org/abs/2608.18317)

**<font color=#1a73e8>作者：</font>** Tommaso Apicella, Alessio Xompero, Andrea Cavallaro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affordance prediction is the identification of potential actions an agent can perform on a target object from multimodal inputs. Affordance prediction methods are difficult to evaluate and compare due to heterogeneous problem formulations, inconsistent dataset annotations, incomplete reporting of experimental protocols, and limited information about deployment conditions. These limitations challenge fair benchmarking and performance comparison. To promote transparency, we propose the Affordance Sheet, a documentation detailing task formulation with its input modalities, model architectures and training information, datasets, and experimental protocols. Affordance Sheets enable reproducible benchmarking and reliable evaluation of affordance models for real-world scenarios, including generalisation to novel conditions and human safety.

---


### 36. [SingularClip: Preventing Spectral Collapse to Maintain Plasticity in Continual and Reinforcement Learning](https://arxiv.org/abs/2608.18319)

**<font color=#1a73e8>作者：</font>** Tyler Kastner, Nimrod De La Vega, Amir-massoud Farahmand  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks trained on nonstationary tasks frequently lose the ability to fit new targets, a phenomenon referred to as loss of plasticity. We identify a novel source of plasticity loss due to the growing anisotropy of weight matrices' singular values during training, and analyze this phenomenon both empirically and theoretically. To mitigate this issue, we introduce SingularClip, a procedure that periodically clips the singular values of all weight matrices. We show that SingularClip performs strongly against baselines across a range of tasks in both continual supervised learning and deep reinforcement learning.

---


### 37. [When Does Dynamic Ensembling Pay Off? Diagnosing Regionwise Gains in Regression under Distribution Shift](https://arxiv.org/abs/2608.18330)

**<font color=#1a73e8>作者：</font>** Tianxin Zhou, Ruixi Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whether input-dependent ("dynamic") combination of a regression model pool beats the best static blend depends on the shift and is rarely known before deployment. Can a small labeled target-domain probe tell us when reallocating trust across regions of the input space will pay off? We answer this with $\widehat{D}_{\mathrm{CF5}}$, which estimates from the probe the cross-fitted gain of the regionwise convex combination over the best static convex blend: the realizable value of deciding, region by region, whom to trust. Across a frozen suite of 12 dataset-shift pairs (spatial, temporal, domain, feature-cluster), $\widehat{D}_{\mathrm{CF5}}$ predicts realized regionwise test gains with dataset-level Spearman $+0.98$ (95% CI $[+0.83, +1.00]$; $p=5\times10^{-5}$), including two cases overturning preregistered expectations. The relationship holds in a 16-pair sensitivity analysis (Spearman $+0.83$), whereas alternative probe diagnostics reach at most $+0.66$. This contrast isolates regional trust reallocation: correlation is $+0.98$ for regionwise-convex gain, but $+0.01$ for smooth covariate-dependent stacking after affine correction. A controlled generator shows dynamic gains arise from the interaction of shift heterogeneity and local competence, increase with shift severity, and become realizable between 128 and 256 probe labels in the tested grid. The Probe-Validated Ensemble Selector chooses among a static affine stacker and dynamic realizers, deploying a candidate only when a held-out lower confidence bound clears the static-convex floor. In a preregistered prospective batch, it matched or improved the floor in all 12 runs; two deployments reduced test risk by 11% and 16%, while the gate rejected a candidate whose un-gated deployment incurred $>30\times$ the static loss. We release OpenRegShift, a reproducible evaluation harness for regression ensembles under distribution shift.

---


### 38. [XNET: Intelligent Dynamic Sampling for High-Speed Network Security Monitoring](https://arxiv.org/abs/2608.18349)

**<font color=#1a73e8>作者：</font>** Thomas Papastergiou, Karthika Subramani, Joseph Reilly 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Growing network speeds, with 100GbE line rates becoming common in modern enterprise networks, pose challenges to operators and security applications, as they struggle to scale their operational efficiency accordingly, without relying on costly hardware, excessive sampling, or complex distributed deployments. Unintentional loss due to stochastic packet sampling often produces low-quality traffic, further risking missed detection of critical security incidents, particularly those hidden in typically low-rate traffic, such as APT/malware command-and-control communications. In this paper, we introduce XNET, a system that monitors traffic at line rate using commodity hardware and applies dynamic sampling to amplify the visibility of high security value traffic. XNET leverages Linux's XDP technology to process packets efficiently, classify them based on their security value, and sample them as per configured policies. The outcome is a reduced packet stream in which the security-relevant portion of the traffic is amplified at the expense of less interesting traffic segments. XNET is a highly flexible, scalable and dynamic system that can be adapted based on a network's needs. We deployed XNET in a large real-world network using only commodity hardware, where our results show that XNET can achieve up to 84% traffic reduction with no packet loss while increasing the visibility of otherwise negligible traffic fivefold. With controlled stress tests, we further demonstrate XNET's scalability up to 100Gbps. Additionally, we show that XNET sampling led to a detection rate of 99.6% in an IDS application.

---


### 39. [0xPass: A Secure Protocol for Universal Cross-Chain Accounts](https://arxiv.org/abs/2608.18359)

**<font color=#1a73e8>作者：</font>** Bernardo David, Keon Kim, Krish Chelikavada  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Universal accounts allow users to manage assets and execute operations across heterogeneous blockchain ecosystems through a single interface, but they introduce security and trust challenges involving authentication, authorization, transaction signing, key custody, recovery, and decentralization. This paper presents 0xPass, a modular protocol architecture for universal cross-chain accounts. 0xPass separates request orchestration, transaction solving, and transaction signing into interoperable layers. User-approved requests are bound to authenticated identities and authorized across layers, while threshold signatures prevent any single transaction node from holding a complete signing key. The design also supports constrained authorization delegation, transaction policies, account recovery, distributed key management, and auditable communication among independently operated sub-networks. We describe a staged deployment path from a centrally operated service to a permissioned network and ultimately to a permissionless network with third-party modules, collateral-backed onboarding, and rotating key-management committees. The resulting architecture provides a practical framework for extending cross-chain account functionality while progressively reducing centralized trust and preserving user control over transaction authorization.

---


### 40. [Depth Anything V4: Dynamic 4D Scene Reconstruction via Riemannian Flow Matching on 4D Gaussian Splatting](https://arxiv.org/abs/2608.18388)

**<font color=#1a73e8>作者：</font>** Jiaming Fan, Jian Lu, Jinling Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Depth Anything V4 (DAV4), a framework for dynamic 4D scene reconstruction from monocular video. Our key contribution is the application of Riemannian Flow Matching (RFM) to 4D Gaussian Splatting parameters, defining probability paths directly on non-Euclidean manifolds (scale, rotation, opacity), ensuring all intermediate states are valid. Through controlled experiments, we isolate RFM's contribution from test-time optimization (TTO) and pre-training. A deterministic MLP baseline with the same data, architecture, and TTO achieves F-score 0.762; RFM achieves 0.806 - the +0.044 gain is RFM's isolated contribution. We provide corrected computational cost analysis: pre-training is 360 GPU-hours, amortizing for large-scale deployment (over 10,000 scenes). Uncertainty is quantified via Negative Gaussian Log-Likelihood and Expected Calibration Error. DAV4 outperforms prior Depth Anything models and per-scene 4D-GS on dynamic reconstruction and novel-view synthesis, while using no human-annotated depth labels as training losses.

---


### 41. [When Clean Signals Are Not Enough: Detecting Structural Ambiguity for Safe Wearable Stress Classification](https://arxiv.org/abs/2608.18397)

**<font color=#1a73e8>作者：</font>** Saba A. Farahani, Hung Cao, Amir M. Rahmani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wearable stress classifiers can achieve strong average performance while failing completely for a particular individual. On WESAD, a Random Forest reaches 93.0% mean accuracy yet yields F1 = 0 for Subject 14, whose cross-signal coupling weakens near stress onset. We call this structural ambiguity: individually plausible physiological channels form an inter-signal pattern that is poorly supported by the person's non-stress reference. We introduce the Individual Conformal Coupling Monitor (ICCM), a lightweight and transparent pre-inference monitor that quantifies subject-specific coupling divergence and routes each window to classify, defer, or abstain without retraining the downstream classifier. Across WESAD (N = 15) and Stress-Predict (N = 35), full-cohort Pearson associations between ambiguity and accuracy are negative (r = -0.607, p = 0.016; r = -0.412, p = 0.014). Robustness analyses temper this finding: rank correlations are not significant, and the WESAD association disappears when Subject 14 is removed. ICCM changes false-positive counts from 29 to 27 and 94 to 92, although neither paired change is significant. It withholds 3 of Subject 14's 21 stress windows but does not repair the missed-stress failure. These results position ICCM as an interpretable signal of unsupported physiology and individual failure, rather than a stand-alone safety guarantee.

---


### 42. [What Does Attention Transfer Transfer? Attention Structure and Robustness in Vision Transformers](https://arxiv.org/abs/2608.18399)

**<font color=#1a73e8>作者：</font>** Jesse Ponnock  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision transformers (ViTs) trained to copy a pretrained teacher's attention maps recover most of fine-tuning's in-distribution accuracy yet fall measurably short of it under distribution shift, as recent work has shown. What the copy delivers has never been measured directly in the attention structure and tied to robustness. We build that instrumentation for ViT-S students of a self-supervised teacher on ImageNet-100, and report three findings that triangulate one conclusion. First, the transfer is essentially perfect and permanently so: the distilled student's attention ends up roughly two orders of magnitude closer to the teacher's than fine-tuning does, and does not drift with additional training. Second, the gap is real at 14$\times$ fewer parameters and 10$\times$ less data than previously studied, but it has a time axis. It tracks training maturity, and completing the schedules that the stopping rule interrupted closes it below our pre-registered threshold in two of three seeds, with comparisons at equal accuracy giving the same result. The endpoint gap at this scale is substantially a training-maturity artifact: robustness matures later than accuracy, and stopping rules tuned to accuracy undersample it. Third, forcing cross-row redundancy down by half the structural separation between the distilled and fine-tuned conditions produces no detectable robustness response under two registered ways of matching accuracy. Verified transfer, a gap that closes while the structure never moves, and a null under direct intervention are together consistent with the deficit residing in features, not in the visible attention structure. This is elimination plus intervention, and its scope is the regime we measured. In this regime, attention overlays show where a model looks, not what it knows.

---


### 43. [AoNT Trap: Borromean-Entangled Mutable Chameleon Trapdoor Hash All-or-Nothing Stream Cipher](https://arxiv.org/abs/2608.18403)

**<font color=#1a73e8>作者：</font>** Victor Kebande  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This work introduces the Borromean-Entangled Chameleon Trapdoor Hash All-or-Nothing (AoNT) Stream Cipher (BEC-Trap), a novel construction that merges Borromean interdependence, trapdoor-enabled mutability, and streaming encryption into a unified framework. The (BEC-Trap) cipher links key (K), initialization vector (V ), and internal state (St) in a Borromean structure, ensuring that breaking, guessing, or removing any one component collapses the entire keystream, providing a computational (AoNT) interdependence under standard cryptographic assumptions. A chameleon trapdoor hash is integrated to permit controlled collisions, enabling seamless rekeying, (V ) refresh, and state rotation without resynchronizing endpoints. This design provides confidentiality, forward secrecy, and adaptive key management with low computational overhead, making it suitable for high-throughput secure messaging, IoT communications, and privacy-preserving blockchain channels. Security analysis of the (BEC-Trap) shows that the construction is resistant to key-recovery attacks, state compromise, and desynchronization attempts, delivering a robust cryptographic primitive for next-generation secure communications.

---


### 44. [Vector Symbolic Policy Gradient](https://arxiv.org/abs/2608.18404)

**<font color=#1a73e8>作者：</font>** Ryozo Masukawa, Sanggeon Yun, SungHeon Jeong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We answer this question with Vector-Symbolic Policy Gradient (VSPG), a discrete-action actor that represents each action by a unit-norm hypervector and scores it by similarity to the encoded state. Under the standard softmax policy-gradient surrogate, we prove that its update is exactly advantage-weighted hypervector bundling followed by normalization, and therefore supports standard advantage estimators. We further show that each trained action hypervector is a fixed-size compressed kernel memory, storing an advantage-weighted kernel expansion over visited states and transferring evidence according to the encoder-induced similarity. This provides a concrete mechanism that can support sample-efficient learning without increasing inference-time memory. Finally, for bipolar action memories, we prove that greedy action selection is stable under random bit flips, with failure probability decaying exponentially in the hypervector dimension. VSPG thus connects VSA action memories, log-linear policy gradients, and kernel policy search while providing a quantitative robustness guarantee.

---


### 45. [JSL-DC: A Word-Level Japanese Sign Language Dataset with Linguist-Derived Descriptions for Distinguishing Confusable Signs](https://arxiv.org/abs/2608.18412)

**<font color=#1a73e8>作者：</font>** Ken Takaki, Asuka Ando, Misa Suzuki 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective sign language (SL) acquisition is crucial for deaf children, yet 95% are born to hearing parents who often lack proficiency in SL. SL recognition can power learning tools to help parents communicate with their children. However, Japanese Sign Language (JSL) lacks large-scale, multi-signer datasets, hindering the development of models that can generalize to new users. To address this gap, we introduce JSL-DC, the largest JSL dataset by video count, comprising 36.7K videos from 19 signers. The entire process was Deaf-centric: the lexicon comprising 270 JSL words was selected by Deaf and Coda linguists to facilitate parent-child communication, all participants were Deaf individuals who use JSL daily, and the data underwent a two-stage review process involving Deaf linguists. Moreover, we provide linguist-derived descriptions for distinguishing confusable signs. We demonstrate that the proposed model inspired by the descriptions outperforms state-of-the-art recognition methods by 9.8% on the confusable subset. The dataset, along with its linguistic description that inspires new models, will be released under a CC-BY 4.0 license to accelerate research in SL recognition.

---


### 46. [CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2608.18413)

**<font color=#1a73e8>作者：</font>** Shihan Chen, Junjing Zhang, Qingsong Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting enables efficient novel view synthesis, but accurate mesh reconstruction remains difficult in weakly observed and occluded regions, where Gaussian primitives may grow into unstable or geometrically inconsistent structures. We propose CoMVS-GS, a general surface reconstruction framework that combines Multi-View Stereo with Gaussian splatting. CoMVS-GS initializes Gaussian primitives from dense multi-view stereo points with pre-flattened scales and normal-aligned orientations, providing stronger geometric priors than sparse structure-from-motion initialization and reducing ambiguity during early optimization. It further introduces PatchMatch-3DGS Mutual Supervision, where Gaussian-rendered depths and normals initialize PatchMatch refinement, and refined PatchMatch depths supervise Gaussian optimization to improve weakly constrained geometry. For surface extraction, CoMVS-GS replaces truncated signed distance field voxel fusion with a Delaunay graph-cut meshing pipeline, reducing sensitivity to voxel resolution while preserving visibility-consistent surface evidence. Experiments on DTU, GauU-Scene V2, and MatrixCity show that CoMVS-GS remains competitive on object-level reconstruction and improves geometric accuracy and mesh compactness in outdoor scenes while maintaining high rendering quality.

---


### 47. [The Road Taken: The Role of Optimizers at the Edge of Stability](https://arxiv.org/abs/2608.18415)

**<font color=#1a73e8>作者：</font>** Jaerin Lee, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The edge of stability refers to a phenomenon in deep learning with gradient-based optimizers where the Hessian eigenvalues of the loss remain stable above a threshold that the classical descent lemma predicts to be unstable. Previous works formulate the edge of stability with respect to the maximum Hessian eigenvalue and the learning rate. However, we observe that many first-order methods, including gradient descent, significantly violate the stability bound predicted by these theories by a factor as large as $\times 21.1$. Moreover, this deviation turns out to be systematic and highly dependent on the underlying optimizer, which is not captured by previous formulations. This calls for a new formulation of the stability threshold, which we derive from the directional Hessian and the gradient-alignment score with respect to the actual update taken by the optimizer, rather than the maximum curvature mode. Our new formulation of the realized edge of stability not only removes optimizer-dependent offsets and provides more consistent predictions of the stability threshold, but also introduces new diagnostic tools that reveal the unique role of the optimizer in actively balancing between the temporal and spatial budgets in first-order optimization.

---


### 48. [Tangut Word Segmentation under Extreme Resource Scarcity: Integrating Traditional Lexicons and Unlabeled Text](https://arxiv.org/abs/2608.18437)

**<font color=#1a73e8>作者：</font>** Lifan Deng, Yongwei Zhang, Sen Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tangut is an extinct language whose script does not explicitly mark word boundaries. We present the first systematic study of Tangut word segmentation using 2,750 expert-annotated segments(31,893 tokens), traditional lexicons, and unlabeled text. Our framework combines a reliability-calibrated lexicon-lattice representation, explicit distributional statistics, and a lightweight character encoder pretrained with MLM. Segment-level five-fold cross-validation shows that lexical and statistical features raise CRF F1 to approximately 0.91. The full TangutEncoder reaches the highest mean F1 (0.911) and improves recall beyond the labeled training vocabulary. These results demonstrate generalization beyond the limited supervised vocabulary across thematically diverse held-out passages, while document-level transfer remains to be evaluated.

---


### 49. [Adaptive Multi-Agent Feature Selection for Personalized Fall Risk Prevention](https://arxiv.org/abs/2608.18450)

**<font color=#1a73e8>作者：</font>** Chang Liu, Ladda Thiamwong, Yanjie Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Falls among older adults represent a major public health challenge driven by complex, time-varying interactions across multiple risk domains. Effective fall risk factor identification requires learning from heterogeneous longitudinal data while accounting for sparse and delayed fall-related outcome events. However, existing approaches are largely static and fail to adaptively model evolving, individualized risk factors across modalities and time. We propose PAFIR, a Personalized and Adaptive Feature selection framework for fall risk Identification and pRevention, which formulates adaptive feature selection as a reinforcement learning problem over longitudinal multimodal health data. PAFIR jointly models structural dependencies among correlated assessment variables and temporal dynamics in wearable-derived physical activity data, and learns adaptive selection policies across repeated study visits using reward signals derived from sparse fall incidence outcomes. We apply PAFIR to data from the Physio fEedback Exercise pRogram (PEER) cluster-randomized trial. Experimental results demonstrate that PAFIR more effectively captures longitudinal and structural patterns of feature relevance than state-of-the-art baselines, and enables dynamic, subject-specific feature selection. By adapting selected features over time, PAFIR supports more timely and personalized fall prevention strategies.

---


### 50. [Atrial Fibrillation Detection with Arbitrary Leads via a Codebook-Based Reconstruction-Classification Framework](https://arxiv.org/abs/2608.18451)

**<font color=#1a73e8>作者：</font>** Hongtao Li, Jia Wei, Guoyao Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> \textbf{Background and Objective}: Reliable atrial fibrillation (AF) detection from electrocardiogram (ECG) signals remains challenging in real-world clinical settings due to variable lead configurations, cross-dataset domain shifts, and pervasive physiological and technical artifacts. So we develop a robust and generalizable deep learning model for accurate AF detection.\\ \textbf{Methods}: We propose the Dual-Codebook Graph Collaborative Network (DCGCNet), a novel end-to-end vector-quantized variational autoencoder that jointly performs AF classification and ECG reconstruction. DCGCNet introduces two key components: (1) a Local-Global Contrastive Module for learning noise-invariant representations, and (2) an Adaptive Codebook Vector Quantizer that dynamically refines codebook prototypes to better align with input data distributions, thereby preventing codebook collapse and enhancing generalization.\\ \textbf{Results}: DCGCNet achieves state-of-the-art performance in standard intra-dataset 12-lead evaluation and demonstrates exceptional cross-dataset generalization across seven diverse settings, consistently attaining AUC > 0.98 in all cases. Furthermore, it maintains high diagnostic accuracy under realistic noisy conditions, including baseline wander, powerline interference, and EMG artifacts.\\ \textbf{Conclusions}: DCGCNet establishes a new benchmark for robust, generalizable, and noise-resilient AF detection, showing strong potential for deployment in real-world clinical environments.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-184](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
