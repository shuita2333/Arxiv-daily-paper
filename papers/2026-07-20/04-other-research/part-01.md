# 📦 其他研究 | 2026年07月20日

> 本类共 **221** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-221](./part-05.md)

---

### 1. [Intelligent Three Level Learning Architecture for Autonomous UAV Swarms in Search and Rescue](https://arxiv.org/abs/2607.14093)

**<font color=#1a73e8>作者：</font>** Oleksii Bychkov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel three level hierarchical learning architecture for autonomous UAV swarms performing search and rescue operations. Unlike conventional approaches that apply a single learning paradigm across all hierarchy levels, the proposed architecture integrates three qualitatively different learning mechanisms corresponding to the biological hierarchy of reflexes, skills, and reasoning such as Hebbian neuroplasticity for individual agent adaptation, multi agent reinforcement learning with graph neural networks and behavior trees for tactical coordination, and model agnostic meta learning with BDI reasoning and a digital twin for strategic decision making.
The architecture is formalized through twenty two architectural contracts organized across six components such as BDI, Behavior Trees, GNN, MARL, Neuroplasticity, Meta Learning that collectively provide six classes of formal guarantees such as safety, budget correctness, optimality, liveness, starvation freedom, and inter level consistency.
We introduce Swarm Meta Cognition as a compositional property arising from the structured interaction of all three levels, enabling the swarm to monitor its own cognitive state and switch between cognitive strategies. Five constructive progress functions for SAR task types bridge the gap between abstract optimization theory and concrete operational scenarios.
The main integration theorem establishes that when all contracts are satisfied, the hybrid neuro-symbolic system preserves all six guarantee classes. For the dynamic case with active learning, five new contracts extend the framework with three additional guarantees such as cognitive resilience, graceful degradation, and monotonic meta improvement. Theoretical analysis demonstrates that the architecture addresses five fundamental limitations of existing hierarchical RL approaches.

---


### 2. [IMEX Interaction-Based Model Explanation](https://arxiv.org/abs/2607.14096)

**<font color=#1a73e8>作者：</font>** Emiliano Massi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In predictive modeling, the ability to explain why a model produces a given target prediction has become increasingly important [5, 10]. Black-box models do not provide a transparent description of the internal mechanisms that generate the prediction, making even accurate predictions difficult to interpret and validate. In critical contexts, predictive accuracy alone is not a sufficient validation metric if the reasons underlying model decisions remain unexplained. The IMEX (Interaction-Based Model Explanation) approach represents a methodological direction within explainable predictive modeling. IMEX is designed to identify which variables contribute most to the target prediction and which interactions among variables are significant in determining the target. The method does not impose limitations on higher-order interaction analysis, allowing the investigation of feature subsets with cardinality greater than two. Beyond the identification of feature importance, IMEX enables the exploration of interaction patterns that may be consistent with latent mechanisms influencing the outcome. Through the application of the IMEX algorithm, it is possible to construct an interpretability map of the predictions. The IMEX framework is built on two complementary metrics: Static Correlation Power (PCS), which quantifies the contribution of individual features, and Interaction Correlation Power (PCI), which captures non-additive effects among features. In the present work, the PCS component is experimentally validated through a comparison with INVASE [18] on three synthetic datasets with known structures. The results indicate that IMEX can recover relevant feature-level structures in the presence of non-linear, conditional, and multicollinear relationships between input features and prediction targets.

---


### 3. [RegNetAgents: A Multi-Agent Framework for Cross-Network Regulatory Driver Identification in Cancer Genomics](https://arxiv.org/abs/2607.14097)

**<font color=#1a73e8>作者：</font>** Jose A. Bird  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce RegNetAgents, an AI-oriented multi-agent framework for structured, query-driven regulatory candidate identification across heterogeneous gene regulatory networks. The system enables unified analysis of bulk tumor and single-cell-derived ARACNe networks by integrating TCGA-derived cancer networks with large-scale single-cell regulatory networks from the GREmLN project. For a given focal gene, the framework performs dual-network classification, cancer gene filtering using OncoKB annotations, and mode-of-action (MoA) assignment for tumor-derived regulatory relationships. Candidates are ranked by evidence consistency across networks (Both, TCGA-only, GREmLN-only). The system is implemented as a multi-agent LangGraph DAG workflow, accessible through a unified Python API and Model Context Protocol (MCP) client, operating as a downstream analytical layer over precomputed regulatory networks rather than a network inference method. Across eleven breast cancer (BRCA) and twelve colorectal cancer (COAD) focal genes, RegNetAgents identifies candidate regulators significantly enriched for OncoKB-annotated cancer genes. TCGA-derived candidates show strong enrichment (Stouffer Z = 6.69 for BRCA and 6.95 for COAD), while GREmLN-derived candidates also demonstrate significant enrichment (Z = 5.51 for BRCA and 7.06 for COAD; all p < 0.0001). No enrichment is observed in housekeeping or non-driver control gene sets, supporting signal specificity. An extended module enables structured evaluation of oncogenic potential, druggability, clinical relevance, and network vulnerability, supporting end-to-end interpretation from candidate identification to biological hypothesis generation. RegNetAgents establishes an interpretable AI framework for cross-network regulatory candidate identification in cancer genomics.

---


### 4. [Quantum Compositional NLP for Arabic: Grammar, Morphology, and Word Sense in Circuit Topology](https://arxiv.org/abs/2607.14100)

**<font color=#1a73e8>作者：</font>** Wajahath Mohammed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the first application of pregroup grammar-based quantum compositional natural language processing (QNLP) to Arabic; a morphologically rich, free-word-order language whose structural complexity provides a uniquely demanding testbed for theories of meaning composition in quantum circuits. Our system converts Arabic sentences into quantum circuits whose topology mirrors grammatical structure: subjects, verbs, and objects become quantum gates, and the typed dependencies between them (the pregroup grammar) determine how those gates are wired together. We conduct three controlled experiments spanning word order, morphological tense, and verb sense disambiguation, comparing quantum circuit methods against classical baselines including AraVec (Arabic word embeddings) and AraBERT (a pre-trained Arabic transformer).

---


### 5. [LBA: Textual Hard-Label Adversarial Attack under Low Query Budgets](https://arxiv.org/abs/2607.14101)

**<font color=#1a73e8>作者：</font>** Shixin Guo, Ming Zhong, Xuhong Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating high-quality adversarial texts with low query budgets remains a challenging problem in the hard-label scenario. Most existing approaches rely on greedy algorithms, where one position in the text is selected for substitution, followed by the substitutions of other positions. This local search approach may fail to discover high-quality adversarial examples and often leads to excessive query costs. Ideally, an optimal adversarial sample would consider all possible position combinations in the text, but exhaustive search is computationally impractical. To address this challenge, we propose a sampling-based method called LBA, which constructs an approximate distribution of high-quality adversarial examples by integrating both prior and posterior knowledge, and utilizes this distribution for sampling. As sampling progresses, posterior knowledge updates the approximate distribution, which in turn guides more effective sampling. Extensive experiments on six language models, ranging from small-scale to large-scale architectures across four datasets, demonstrate that LBA significantly outperforms state-of-the-art baselines on all evaluation metrics. Additionally, LLM-based assessment indicates that LBA generates more semantically preserved and comprehensible adversarial texts.

---


### 6. [UniSAGE: Unifying Static and Dynamic Attributes with Hyper-Structure](https://arxiv.org/abs/2607.14102)

**<font color=#1a73e8>作者：</font>** Taoran Fang, Yan Deng, Chunping Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid growth of digital data, real-world applications increasingly involve hierarchical information that combines static attributes with dynamic records. Modeling such heterogeneous data in a unified and generalizable manner remains challenging. Existing approaches often rely on extensive manual design, are tightly coupled to specific data schemas, and typically process static and dynamic attributes in isolation, thereby overlooking their implicit interactions. We propose UniSAGE, a unified framework for modeling data with both static and dynamic attributes. UniSAGE constructs a global attribute graph that represents hierarchical and temporal relationships in a unified structure. To ensure representational consistency, it introduces two orthogonal parameter subspaces that jointly support static aggregation and dynamic reasoning within a shared semantic space. Building on these unified representations, UniSAGE further enables task-specific interaction between static and dynamic attributes via a lightweight hyper-structure mechanism. UniSAGE is fully automated, robust to evolving data schemas, and capable of capturing complex cross-attribute dependencies. Extensive experiments on multiple public benchmarks and a real-world financial behavior dataset demonstrate that UniSAGE consistently outperforms existing methods, achieving performance improvements of over 10% on several tasks.

---


### 7. [UzWordnet and Generative AI for Learning Uzbek by Game Playing](https://arxiv.org/abs/2607.14104)

**<font color=#1a73e8>作者：</font>** Alessandro Agostini, Saydobid Khusanov, Mirkamol Mirkamilov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents an educational system architecture that enables learners to practice the Uzbek language through game-playing. The architecture integrates UzWordnet and the largest currently available orthographic dictionary for Uzbek as core lexical resources, together with generative AI as a fundamental component for learning support. We design four educational games to facilitate Uzbek language learning and propose a game-based methodology for improving UzWordnet as a direct by-product of game dynamics. Our approach combines game design and lexical resources to address objectives that are at the same time educational (language learning) and lexical (improvement and enrichment of a lexical resource).

---


### 8. [MAPS: Modeling Co-Existing Subjective Perspectives and Shared Meaning in Multi-Agent Cognitive Dialogue](https://arxiv.org/abs/2607.14110)

**<font color=#1a73e8>作者：</font>** Molood Arman, Clément Bonnafous  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human dialogue involves more than exchanging information; it also expresses beliefs, emotions, and subjective cognitive styles. Yet current AI dialogue systems often enforce semantic uniformity, sacrificing diversity and interpretability. We present MAPS (Multi-Agent Perspective Spaces), a novel framework that models dialogue between cognitively distinct agents through domain-weighted profiles, dynamic GRU-based memory, and interpretable token-level attention. MAPS enables agents to maintain individualized reasoning while progressively converging on shared meaning. Evaluations on EmpatheticDialogues, TopicalChat, and MultiWOZ show that MAPS supports semantic alignment without collapsing subjectivity. Our results demonstrate a path toward cognitively grounded, interpretable dialogue systems that balance expressiveness and coherence.

---


### 9. [DialogueVPR: Towards Conversational Visual Place Recognition](https://arxiv.org/abs/2607.14115)

**<font color=#1a73e8>作者：</font>** Yukun Song, Changwei Wang, Xingtian Pei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inspired by how humans communicate spatial information, language-guided geo-localization has gained significant traction for its intuitive and practical value. Despite this progress, most methods still rely on a static, one-shot retrieval paradigm, which fails to handle the ambiguity and incompleteness inherent in real-world natural language descriptions. We propose a paradigm shift to reasoning retrieval and introduce Dialogue Place Recognition (DlgPR), which casts localization as an interactive, dialogue-driven reasoning process. To support this new task, we present DlgQuest-Cities, the first large-scale dialogue-based benchmark for place recognition, and a unified reasoning framework that couples a cross-modal multi-level retriever with an intelligent questioner, DQ-pilot. DQ-pilot is trained in a curriculum: supervised fine-tuning on a curated DQ-cities-20k subset followed by reinforcement refinement on a harder DQ-cities-10k split via GRPO. Two task-aligned metrics guide learning: a Discriminative Difficulty Index (DDI) for curriculum sampling and a Positional Retrieval Gain (PRG) reward that directly measures retrieval improvement induced by a question. Experiments show this reasoning-based approach significantly outperforms baselines. The code and model are available at this https URL.

---


### 10. [ReportMedSAM: Guiding Segmentation Through Radiology Reports](https://arxiv.org/abs/2607.14116)

**<font color=#1a73e8>作者：</font>** Anghong Du, Theodoros N. Arvanitis, Colin Watts 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Free-form radiology reports contain rich clinical descriptions, yet converting them for reliable segmentation remains challenging due to the inherent variability of natural language. Existing pipelines often rely on predefined organ phrases or brittle rule-based inference-time extraction, which limits their scalability to novel anatomical structures and makes them sensitive to linguistic variations. To address this, we propose ReportMedSAM, a report-driven framework that replaces discrete extraction with a learnable concept bank. By leveraging a frozen medical vision-language encoder (BiomedCLIP), we align organ-level concept embeddings with large-scale clinical corpora through contrastive learning, establishing mutually orthogonal semantic anchors. Our approach explicitly mitigates organ-level semantic collapse and ensures high robustness against diverse clinical synonyms (e.g., "renal" vs. "kidney" ). During inference, a clinical report is embedded and matched against this concept bank to dynamically activate task-specific Mixture-of-Experts (MoE) modules. This decoupled design allows new concepts and experts to be added without retraining existing components, providing a parameter-isolated extension mechanism while keeping previously learned experts unchanged. Evaluated on the AbdomenAtlas 3.0 dataset, ReportMedSAM effectively interprets free-form reports, achieves competitive segmentation accuracy, and demonstrates seamless, non-interfering extension to novel clinical tasks.

---


### 11. [Position: Explainability Research Must Prioritize Foundations over Ad-hoc Methods](https://arxiv.org/abs/2607.14123)

**<font color=#1a73e8>作者：</font>** Michal Moshkovitz, Suraj Srinivas, Lesia Semenova 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the proliferation of Explainable AI (XAI) techniques -- from feature attributions to sparse autoencoders -- explanations rarely influence real-world workflows. In practice, they are often generated and discarded without guiding meaningful action. This gap reflects foundational shortcomings: research has not yet established methodologies for integrating explanations into end-to-end, human-in-the-loop systems. This position paper argues that the machine learning community must pivot from ad-hoc XAI methods toward addressing foundational & structural challenges, including unclear problem formulations, underspecified evaluation objectives, and the absence of pipelines for explanation-driven feedback. We support this claim through an analysis of recent ICML, NeurIPS, and ICLR papers and a survey of XAI practitioners, revealing recurring issues that limit cumulative progress. We conclude by outlining a practical checklist designed to shift XAI toward a more human-centered, action-oriented paradigm. By emphasizing foundational clarity over the development of ad-hoc methods, we hope to provide a roadmap for integrating explanations into actionable, feedback-driven AI systems.

---


### 12. [Explainable Geospatial AI for Satellite Ground Station Siting Using LiDAR-Derived Terrain Intelligence](https://arxiv.org/abs/2607.14127)

**<font color=#1a73e8>作者：</font>** Shohini Sarkar, Smithi Mahendran, Rishi Chudasama 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representative clutter height (RCH) is a key parameter in radio propagation and interference analysis because it captures the dominant height of local obstructions that drive terminal clutter loss. Current practice often relies on fixed clutter heights assigned to land use classes in Recommendation ITU-R P.452-18, but this misses within class variation and can lead to conservative exclusion zones and poor site ranking for low Earth orbit ground station siting and spectrum coordination. We present an interpretable, globally deployable machine learning framework for predicting RCH from open geospatial data. The model is trained using LiDAR derived labels from the U.S. Geological Survey 3D Elevation Program and inference time features from global land-cover, terrain, demographic, thermal, and optical remote sensing products. We define RCH using a robust 75th percentile clutter height statistic, evaluate multiple regressors, and select LightGBM for its accuracy, efficiency, and compatibility with feature attribution analysis. The final model achieves a mean absolute error of 1.79m and an R^2=0.765, reducing absolute error by more than 60% relative to the ITU baseline. Beyond aggregate fit, we evaluate domain facing criteria relevant to RF planning, including meter scale error, tolerance band accuracy, over and under estimation tails, agreement with ITU clutter height regimes, and SHAP-based physical plausibility. SHAP identifies tree canopy cover, land-cover semantics, and spectral reflectance as the most influential predictors. Studies on segmentation derived features, non-forest ablations, and land-cover matched international validation show that open geospatial data can improve clutter modeling at scale without sacrificing interpretability or deployability.

---


### 13. [Cross-Dataset Generalization in Urdu Fake News Detection: An Empirical Study with XLM-RoBERTa and a Length Confound Analysis](https://arxiv.org/abs/2607.14131)

**<font color=#1a73e8>作者：</font>** Muhammad Abdullah Haroon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Urdu fake news detection remains under-resourced despite Urdu being spoken by over 231 million people worldwide. While prior work has demonstrated strong in-domain performance on individual Urdu datasets, cross-dataset generalisation has received little systematic attention. This paper presents the first cross-dataset generalisation study for Urdu fake news detection, using two publicly available balanced datasets: the Ax-to-Grind Urdu corpus (10,083 articles, 15 domains) and the Notri-Fact Urdu dataset (13,388 articles). We fine-tune xlm-roberta-base under four experimental conditions, in-domain on each dataset and two zero-shot cross-domain transfer directions, comparing against TF-IDF baselines using Logistic Regression and Support Vector Machines. Our experiments reveal a striking asymmetry: Notri-Fact to Ax-to-Grind transfer achieves a macro F1 of 0.771, while the reverse collapses to F1 of 0.005, with the model predicting fake for 99.7% of test articles. We demonstrate that this collapse stems from a systematic length confound in Ax-to-Grind, where fake articles average 117 words versus 35 for real articles, a 3.4x asymmetry inducing shortcut learning. A length ablation capping articles at 50 words yields only a 0.0067 F1 drop, confirming the confound inflates but does not solely drive in-domain performance. We provide a reusable diagnostic methodology that combines bidirectional transfer analysis and prediction-collapse inspection to identify confound-driven behavior in multilingual fake news detection settings.

---


### 14. [Human AI Construction of Bayesian Networks for Operational Decision Support -- A Virtual Survey Approach](https://arxiv.org/abs/2607.14141)

**<font color=#1a73e8>作者：</font>** Kumar Rahul, Shovan Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian Belief Networks (BBNs) are powerful tools for decision-making under uncertainty. However, building their structures and estimating parameters are difficult. Currently, researchers must choose between relying on expert judgement or using large datasets to learn the structure and parameters of the network. We propose a new methodology using Large Language Models to bridge the gap between expert opinion and data-driven learning. This approach uses a panel of AI agents to estimate probabilities based on specific personas and context. We then apply a trimmed-mean rule to remove noise from these responses. We develop a six step BBN framework and illustrate it to model customer intention to consult a doctor in an alternative healthcare system. The model reveals that while self efficacy appears to be a major factor, its actual causal impact is small. In contrast, subjective norms have a much stronger effect in modelling customers' intention. The most effective strategy is to improve both confidence and community norms simultaneously.

---


### 15. [Capability from Access Structure, Not Scale: Lower Bounds and Pre-Registered Tests for Hybrid Sequence Models](https://arxiv.org/abs/2607.14144)

**<font color=#1a73e8>作者：</font>** Wenhui Chen, Jianlin Chen, Ziyao Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Platonic Representation Hypothesis (PRH) holds that as models scale, representations of heterogeneous networks converge toward a shared model of reality. We propose its sequel and boundary, the Capability Convergence Hypothesis (CCH): under a fixed per-token inference budget, representational convergence does not entail capability convergence. Capability instead converges toward a class, the access-complete hybrid: any architecture holding both a compressive O(1)-state channel and a scalable verbatim-index channel. We anchor it on a witness task, the Newton's-apple problem in an infinite stream, and name three resource walls: a Shannon wall barring any o(Nb)-state architecture, a horizon wall barring any fixed window, and a circuit wall barring fixed-depth attention-only composition (conditional on TC0 != NC1). Under an explicit separability assumption a hybrid crosses all three by paying each wall's price, so capability is strictly super-additive under composition. We separate what we prove from what we conjecture: the access-completeness principle rests on information-theoretic lower bounds and pre-registered experiments, while the field-level convergence trend is an economics-motivated conjecture. We report the first pre-registered small-scale tests under criteria frozen before the data: the predicted scissors gap is measured (exact-retrieval error 0.994 vs. 0.000 once a 64-scalar state gains one global-attention layer), the state-tracking bifurcation lands at the registered boundary, and a conjunction witness shows an irreducibly two-channel solution; one prediction failed with its direction reversed and is reported as such. Representational convergence is given freely by scale; capability convergence must be purchased by access structure.

---


### 16. [Breaking Refusal in the First Half: A Mechanistic Study of the Prefill Jailbreak](https://arxiv.org/abs/2607.14147)

**<font color=#1a73e8>作者：</font>** Alex Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligned language models refuse harmful requests, but a one-line prefill ("Sure, here is") strips the refusal. We ask where and how it fails. The harm representation stays intact: on the prompts the attack flips to compliance, a linear probe reads harm as high as on the refused ones (0.91-0.98), while behavioral refusal drops to chance. This holds across four models and three families (1.5-3.8B, and at 14B). Refusal is therefore a shallow, response-site computation. We localize it to an early window: a dose-matched position control shows the first half of the response suffices to break refusal, while the second half is nearly inert. Three causal probes converge on that window. Restoring the harm direction there partially re-engages refusal. Injecting the model's own refuse-state reverses the jailbreak (74%, held-out). And knocking out the early response's attention to the prefill, but not an equal attention mass elsewhere, selectively collapses the harmful continuation. A base-model control identifies the mechanism: the same knockout collapses the continuation prefill-specifically even in a non-safety-tuned base model (64% to 25% harmful content vs a matched control's 64%, replicated at 7B). So the prefill's grip is generic autoregressive conditioning, not safety-specific suppression, and "refusal restoration" is a model-dependent fallback. The dominant mechanism is passive. A small safety-specific attractor remains on top (logit-trace concentration 0.24 vs 0.03), whose active-vs-passive character we size but do not fully separate. No single direction or component is a clean handle either: the decision is decodable but distributed, and refusal tracks harm rather than scary surface. The consequence is structural: a monitor reading the untouched prompt-side representation is immune by construction, but only to response-site attacks. The mechanism is diffuse; the failure surface is local.

---


### 17. ["Trust Junk" Leads to Unjustified Support for Highly Discriminatory Predictive Models](https://arxiv.org/abs/2607.14152)

**<font color=#1a73e8>作者：</font>** Michael Correll, Lucy Havens, Mahsan Nourani  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The persuasive power of data visualizations can go awry: for instance, in an explainable AI (XAI) context, visualizations can produce over-trust of predictive models. In this paper, we use a crowdsourced study to show that providing accurate (but superfluous or irrelevant) data in a model explanation can, in fact, result in unjustified trust and other positive beliefs about a model, even when the model is patently discriminatory and unfair. Our results suggest that XAI designers and developers need to consider the implicit or explicit rhetorics of their work, and beware of the potential of visualizations to imbue models with unearned trust.

---


### 18. [Certified Domain Consistency for Multi-Domain Retrieval: Label-Free Per-Domain Contamination Control with Conformal Risk Guarantees](https://arxiv.org/abs/2607.14157)

**<font color=#1a73e8>作者：</font>** Jayakumar Manoharan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval over corpora that mix several domains often returns relevant but wrong-domain evidence that ranking metrics miss and that conformal risk control bounds only marginally, under-covering the worst domains. This work introduces C3R, a drop-in control layer that, from an inferred domain posterior and no query-time label, certifies a per-domain contamination budget where feasible and otherwise abstains rather than silently violating; on the hardest domains it guarantees a reduction, not a tight bound. The core is a two-split scheme built on risk-controlling prediction sets, whose finite-sample transfer bound crosses from the inferred to the true domain with fully estimable slack, supports heterogeneous budgets, and inverts for deployment. Population validity rests on this bound and a controlled simulation; across a thousand resampled calibrations the certificate never violates (a stability result) while marginal control violates the most-contaminated domain in every draw, and soft demotion retains more recall than the strongest calibrated cascade at equal certified contamination. The method replicates across open testbeds including an independent one from public federal regulations, and an LLM-judged downstream probe indicates wrong-authority grounding rises with contamination and falls under control. The layer is frozen-stack and reranker-agnostic.

---


### 19. [Orchestrating Power Grid Studies with Multi-Agent AI and MCP Servers](https://arxiv.org/abs/2607.14158)

**<font color=#1a73e8>作者：</font>** Jérôme Picault, Clément Goubet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper explores how Agentic AI and Model Context Protocol (MCP) can support power-grid studies in a Transmission System Operator (TSO) context. We focus on integrating Large Language Models with numerical simulation tools, structured workflows, and human supervision. We identify key industrial requirements for agent assisted grid studies and introduce pypowsybl-mcp, an MCP-based interface exposing selected capabilities of our simulation tool, pypowsybl to AI agents. This first step provides a testbed to study how agents can setup simulations, execute analyses, retrieve results, and interact with power-system simulators through standardized tool calls. We also discuss principles for human-in-the-loop, multi-agent workflows and outline an evaluation strategy combining technical metrics and practitioner feedback. The paper positions MCP-based tool integration as a step toward more interactive, auditable, and scalable grid-study environments.

---


### 20. [MemoHarness: Agent Harnesses That Learn from Experience](https://arxiv.org/abs/2607.14159)

**<font color=#1a73e8>作者：</font>** Yue Huang, Wenjie Wang, Han Bao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent harness is the external control layer that turns a base LLM into an executable agent by managing context, tools, orchestration, memory, decoding, and output handling. While harness design strongly affects agent behavior, most automatic improvement methods optimize narrower artifacts such as prompts, pipelines, or workflows, and deployed agents usually reuse a single global harness for all cases. We introduce MemoHarness, an adaptive harness optimization framework that learns from its own executions. MemoHarness decomposes the harness into six editable control dimensions, stores per-case diagnoses and distilled global patterns in a dual-layer experience bank, and adapts the learned harness to each test case using retrieved experience without test-time labels, feedback, or additional search. In our evaluation across shell-agent, code-generation, and analytical-reasoning benchmarks, MemoHarness improves over the fixed harnesses we compare against and shows selective transfer to unseen suites and base models. Its additional context can also remain cost-competitive when much of the retrieved experience is cacheable. These results provide evidence that execution experience is a practical substrate for building agent harnesses that are more adaptive than a single static configuration, while leaving broader claims about statistical robustness and component attribution to future work.

---


### 21. [QFireNet: A Quantum-Enhanced U-Net for Wildfire Segmentation from Sentinel-2 Imagery](https://arxiv.org/abs/2607.14160)

**<font color=#1a73e8>作者：</font>** Jaiman Munshi, Tanvi Tewary, Sawyer Bloom 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wildfire detection from satellite imagery is a semantic image segmentation problem that has proven to be difficult due to challenges such as class imbalance, feature complexity, and atmospheric interference. In this paper, we build on the foundational U-Net image segmentation model to develop a quantum-hybrid solution in hopes of more effectively modeling the high-dimensional spectral feature space of the Sen2Fire dataset. We inject a variational quantum circuit in the bottleneck portion of U-Net, specifically the QuFeX and QB-Net ansatzes. We test a classical Feature Pyramid Network (FPN) for further comparative analysis of the model, and we also explore classical improvements to the U-Net model and its training process, including a compression of parameters, alternative loss functions, and uniform mixing of input data. Our primary finding is that under matched conditions, both QB-Net (with an $F_1$ score of 31.18) and QuFeX ($F_1 = 30.79$) outperformed the classical U-Net baseline results ($F_1 = 28.71$). Additionally, the classical FPN achieved a comparable score of 31.13. A crucial finding was that data mixing removed a significant domain shift between the geographically-separated train and test sets, which boosted the classical FPN $F_1$ score to 39.76. We validate the architecture's robustness and generalizability to the wildfire detection problem via cross-dataset transfer on the California Burned Areas (CaBuAr) dataset. Overall, we find that quantum machine learning has potential to provide an advantage in the problem of wildfire image segmentation, and further experiments will continue to validate and expand upon this finding.

---


### 22. [How Much of a 10-K Matters? Aggregation-Dependent Value of Full-Text versus Risk-Factor Sentiment](https://arxiv.org/abs/2607.14174)

**<font color=#1a73e8>作者：</font>** Sanggyu Sean Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial sentiment extraction has largely relied on news text and supervised extraction against return labels alone, leaving 10-K filings -- and volatility, the target risk disclosure is arguably best suited to informing -- comparatively unexplored. We extend a supervised lexicon-learning approach to 10-K filings and their Item 1A risk-factor sections, training sentiment scores against both return and volatility labels at three levels of aggregation: sector, portfolio, and individual firm. Across 1,383 filings from 94 Nasdaq-100 technology constituents (2006--2023), we evaluate the resulting twelve sentiment metrics on classification accuracy, correlation with realised market outcomes, and qualitative lexical content. Full-filing text produces more accurate sentiment at the sector and portfolio level for both targets, but this reverses at the individual-firm level, where the narrower Item 1A section performs better -- an effect we attribute to the interaction between document volume and the amount of independent training signal available at each level of aggregation. A Loughran-McDonald dictionary baseline is consistently, strongly negatively correlated with price at every level tested, underscoring the value of a supervised approach for regulatory disclosure text. These findings, and the design choices they motivate, establish the sentiment-generation methodology underlying a subsequent, larger-scale, multi-source system.

---


### 23. [Low-Latency Relay Selection in NR-V2X Vehicular Communications via Graph Isomorphism Networks with Edge Features](https://arxiv.org/abs/2607.14176)

**<font color=#1a73e8>作者：</font>** Giambattista Amati, Federica Mangiatordi, Emiliano Pallotti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable, low-latency uplink connectivity is a key requirement for C-V2X networks in dense urban environments, where fast channel variations and blockages often degrade direct vehicle-to-infrastructure links. Multi-hop relaying can restore coverage, but relay-link activation under radio, capacity, and routing constraints results in an NP-hard optimisation problem, typically solved via Mixed-Integer Linear Programming (MILP), whose runtime scales poorly with graph size. This paper introduces an edge-aware Learning-to-Optimise framework for real-time relay selection. Each V2X snapshot is modelled as a directed graph: node features encode vehicle state and traffic demand, while edge features capture radio-link capacity. An offline MILP oracle generates optimal relay configurations that supervise a Graph Isomorphism Network with Edge Features (GINE), enabling edge-level relay activation through a single forward pass, with tightly bounded inference latency. To bridge learning and exact optimisation, we also propose a hybrid GINE-Pruned MILP (GP-MILP) strategy in which GINE predictions prune the MILP search space. Experiments on a large-scale dataset generated via an OSM-SUMO-GEMV$^2$ pipeline show that GINE closely matches MILP decisions at the link level (accuracy 0.9589), F1-score (0.9544) on validation) and yields consistent end-to-end connectivity gains over a 1-hop MILP baseline (up to 9.2% with four RSUs and 12% with two RSUs). Inference latency remains tightly bounded, with all evaluated instances completing within 5~ms. Moreover, GP-MILP preserves MILP-equivalent solutions (same objective value) while achieving solver runtimes below 30~ms for more than 98%) of the graph instances, making MILP-grade optimisation compatible with stringent NR-V2X latency budgets.

---


### 24. [ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System](https://arxiv.org/abs/2607.14178)

**<font color=#1a73e8>作者：</font>** Yutong He, Daibo Li, Guohong Li 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models have fueled autonomous AI agents capable of tackling complex scientific tasks, yet existing automated research systems remain predominantly focused on empirically driven domains with quantitative benchmarks, leaving theory-driven discovery, particularly in mathematically grounded disciplines requiring rigorous proofs and synthesis of domain knowledge, largely underexplored. Key challenges include the difficulty of verifying theoretical reasoning at scale, insufficient reasoning ability for autonomous frontier exploration, and a scarcity of procedural heuristics in the literature. We introduce ReasFlow, an end-to-end autonomous agent system for reasoning-centric scientific discovery that operationalizes a collaborative paradigm where the human expert acts as Principal Investigator while the agent executes rigorous derivations as a capable graduate student. ReasFlow incorporates (i) a robust internal verification loop that audits logical coherence and corrects fundamental errors prior to human inspection, and (ii) an automated knowledge retrieval and self-improvement mechanism that proactively surfaces both declarative facts and overlooked procedural heuristics, substantially reducing expert intervention. The system unifies literature synthesis, algorithm design, theorem proving, experimentation, and manuscript preparation in a single system. Deployed to autonomously generate five complete research papers with rigorous theoretical and empirical content from minimal prompts, ReasFlow consistently achieves the highest evaluation scores among state-of-the-art open-access baselines under a curated LLM-based review rubric. ReasFlow is publicly accessible via the ReasLab platform, providing a collaborative workspace for AI-assisted theoretical research. Github repo: this https URL.

---


### 25. [MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video Generation](https://arxiv.org/abs/2607.14189)

**<font color=#1a73e8>作者：</font>** Xiaohan Zhang, Yuqing Wen, Junlin Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-reference-to-audio-video (MR2AV) generation aims to generate coherent audio-video content conditioned on multiple references and textual instructions. Existing benchmarks mainly focus on text-driven generation, single-reference subject preservation, or isolated audio-video alignment, leaving the emerging MR2AV setting largely unexplored. Compared with these settings, MR2AV requires models to jointly reason over multiple references while generating synchronized visual and audio content. Models must not only preserve each reference faithfully but also correctly bind and compose multiple referenced entities into coherent audio-visual events. To address this gap, we introduce MultiRef-Compass, a unified benchmark for MR2AV generation. It comprises $350$ carefully curated samples constructed through a scalable and controllable asset-composition pipeline, covering multi-view subject preservation, multi-entity binding, and human-object-scene composition. To provide interpretable assessment, MultiRef-Compass defines an evaluation protocol with four dimensions: Basic Quality, Reference Consistency, Audio-Visual Consistency, and Instruction Following, using 14 sub-metrics. MultiRef-Compass integrates automatic metrics with a rejudging-enhanced MLLM-as-a-Judge framework, enabling scalable and auditable evaluation of both perceptual fidelity and reference-conditioned composition. Extensive experiments on eight representative MR2AV systems reveal substantial room for improvement across multiple evaluation dimensions, underscoring the need for a comprehensive benchmark and positioning MultiRef-Compass as a foundation for future MR2AV research.

---


### 26. [A Temporal Machine Learning-Based Time-to-Event Model for Predicting ALS Progression and Healthcare Utilization](https://arxiv.org/abs/2607.14190)

**<font color=#1a73e8>作者：</font>** Zongliang Yue, Qi Li, Terry Heiman-Patterson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Amyotrophic lateral sclerosis (ALS) is a progressive and heterogeneous neurodegenerative disease in which predicting clinically meaningful milestones, such as assistive device use, remains challenging. We developed a time-to-event, digital-twin-inspired framework that integrates longitudinal ALS Functional Rating Scale-Revised (ALSFRS-R) trajectories with survival modeling to support individualized prediction of functional decline and assistive device utilization. We constructed a harmonized longitudinal dataset by integrating diagnosis records, ALSFRS-R assessments, activities of daily living, and demographic information, followed by preprocessing to ensure data quality, temporal alignment, and cohort consistency. Correlation-based clustering identified coherent functional domains spanning bulbar, upper limb, axial, lower limb, and respiratory systems. Generalized additive mixed models characterized nonlinear, domain-specific functional decline across all domains. In addition, a temporal machine learning model was developed to predict longitudinal functional decline and capture stage-dependent disease progression. Cox proportional hazards modeling further identified lower limb function, particularly walking and stair climbing, as the strongest predictors of earlier wheelchair access. Building on these results, we implemented a digital twin-inspired temporal machine learning-based time-to-event (TTE) model that generates individualized survival curves and dynamically predicts wheelchair-free survival. This framework provides a scalable, interpretable, and clinically actionable approach for linking ALS progression with personalized decision support, with applications in proactive care planning, clinical trial stratification, and precision medicine.

---


### 27. [Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning](https://arxiv.org/abs/2607.14192)

**<font color=#1a73e8>作者：</font>** Dingsu Wang, Filip Ryzner, Kelly He 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As recommender systems mature in the past few years, their optimization objectives have evolved from a primary focusing on short-term behavioral signals to a broader emphasis on long-term user engagement and retention. However, directly optimizing retention is difficult because return signals are sparse, delayed, and only partially attributable to earlier recommendations. Prior work has addressed this challenge with sequential modeling and reinforcement learning, but these approaches typically require task specific reward engineering, substantial computational overhead, and surface specific implementations that are difficult to generalize. In this paper, we present a unified, model-agnostic downstream reward framework for optimizing long-term user value in large-scale recommendation systems. First, we formulate the downstream reward learning problem and develop an offline screening framework to identify session level behaviors that are both observable early and predictive of future retention. We then propose several model-agnostic downstream rewards signals derived from observed user action patterns across multiple sources. We further discuss the engineering effort to productionize the proposed rewards derivations and challenges we faced when adding them to our ranking models. Online A/B experiments demonstrate consistent improvements in engagement and retention-related metrics, and the framework has been deployed across multiple Pinterest surfaces, including Homefeed, Related Pins, Search, and Notifications.

---


### 28. [Inference-Time Concept Suppression and Video-Centric Evaluation for Text-to-Video Models](https://arxiv.org/abs/2607.14194)

**<font color=#1a73e8>作者：</font>** Wenxuan Chen, Wenjie Feng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) generators can synthesize realistic and temporally coherent videos, but controllably removing a target concept from a generator remains difficult.
Unlike text-to-image concept erasure, T2V unlearning must suppress a target concept that may persist across frames while preserving non-target subjects, actions, scenes, and temporal structure.
We propose \textbf{SIRUS}, a training-free inference-time framework for concept-level T2V unlearning.
Given textual aliases of a target concept, SIRUS localizes target-related prompt evidence and suppresses target expression during sampling, without updating the text encoder or denoising network.
We further introduce a video-oriented evaluation framework for T2V unlearning that separately measures target forgetting, non-target preservation, video quality, jailbreak robustness, and efficiency, using video-level failure criteria, frame-level residue statistics, paired preservation analysis, VBench-based quality diagnostics, and deployment overhead measurement.
Across five safety, object, and style concepts on CogVideoX, SIRUS reaches 70.4\% average forgetting success and 25.7\% average frame hit, compared with 44.4\% / 47.2\% for VideoEraser, while reducing the average VBench quality drop from -0.043 to -0.016, yielding the strongest forgetting-quality trade-off among fully evaluated baselines.
Transfer experiments on Wan2.2 further suggest that SIRUS generalizes across modern T2V backbones.

---


### 29. [Augmentations for Robust and Efficient Imitation Learning in Streamed Video Games](https://arxiv.org/abs/2607.14200)

**<font color=#1a73e8>作者：</font>** Somjit Nath, Abdelhak Lemkhenter, Pallavi Choudhury 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imitation learning is an appealing way to scale game-playing agents to complex 3D environments by training policies to map visual observations to actions from human demonstrations. However, these demonstrations are expensive to collect and modern game-playing is often done through streaming in which network delay and compression introduce spatiotemporally correlated visual artifacts that can cause a covariance shift at test time. To address these challenges, we propose streaming augmentations that mimic four types of artifacts commonly encountered during streaming with low-bandwidth network connection: pixelated blocks and scrubs, global blur, and ghosting. We instantiate our approach on top of predictive inverse dynamics models (PIDM), which combine future-state conditioning with an inverse dynamics policy in a learned latent space, and evaluate the impact of our augmentations across three tasks in modern 3D video games. Under stable streaming conditions, agents trained with spatiotemporal augmentations achieve up to 41% higher evaluation performance compared to agents trained without augmentations under an identical data budget. When network lag is introduced, agents trained with augmentations degrade by only 7.45% vs 49.82% of the original performance for agents trained only with the original data. These results clearly indicate that spatiotemporal augmentations tailored for the streaming setting are a simple yet powerful tool to train robust and efficient game-playing agents.

---


### 30. [KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned Video Generation](https://arxiv.org/abs/2607.14202)

**<font color=#1a73e8>作者：</font>** Yuqi Tang, Tengfei Liu, Yizheng Lai 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation increasingly relies on keyframe-based workflows, where creators specify a sequence of reference images to guide generation. Although recent models support multi-keyframe conditioning, it remains unclear whether they can faithfully reproduce the prescribed keyframes while maintaining overall video quality. We present KeyFrame-Compass, the first comprehensive benchmark for evaluating keyframe-conditioned video generation. The benchmark contains 386 carefully curated samples spanning three application domains, two video structures, two prompt granularities, two conditioning formats, and four keyframe densities, enabling controlled analysis under diverse generation settings. We further introduce an automated evaluation framework that jointly measures keyframe execution and overall video quality. Specifically, we decompose keyframe execution into six complementary metrics covering presence, fidelity, temporal ordering, localization, persistence, and uniqueness, while assessing overall video quality through evidence-grounded MLLM judgments augmented with specialized perception models. Experiments on nine representative video generation systems reveal several fundamental limitations. Current models exhibit a clear trade-off between faithful keyframe execution and natural video synthesis. Their performance further degrades as keyframe constraints become denser and most open-source models also fail to interpret storyboard-grid inputs as temporally ordered keyframe sequences.

---


### 31. [Privacy Leakage in Federated Learning in Radiology Reports: A Comparative Evaluation of Tokenizer-Driven Privacy Risks](https://arxiv.org/abs/2607.14205)

**<font color=#1a73e8>作者：</font>** Santhosh Parampottupadam, Andres Martinez, Dimitrios Bounias 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables multi-institutional training on clinical text without sharing raw data, but gradient inversion can reconstruct sensitive information from shared model updates. The extent of this leakage for radiology reports, and the role of tokenizer design, remains unclear. We quantify gradient-based text reconstruction in FL and compare privacy risk across three tokenizers with the model architecture held fixed. Six FL clients trained a GPT-2-style transformer (sequence length 32) on public radiology corpora (368,751 diagnostic reports, 98,206 discharge summaries, 1,500 MIMIC-CXR free-text reports) using the GPT-2, RadBERT, and LLaMA-2 tokenizers at batch sizes of 64, 128, and 256. Assuming an active malicious server that modifies the shared architecture before distribution, we applied analytic gradient inversion and measured reconstruction fidelity over five runs. Exact sentence reconstruction ranged from 31% to 44% across tokenizers (30.6-43.5% across the 27 tokenizer x dataset x batch-size cells). At batch size 64 on the Discharge dataset, accuracy was 42.1% (GPT-2), 42.3% (RadBERT), and 39.4% (LLaMA-2), decreasing to 37.3%, 37.2%, and 34.3% at batch size 256. S-BLEU declined as batch size grew (GPT-2: 0.44 to 0.33; RadBERT: 0.48 to 0.35). RadBERT yielded the highest reconstruction fidelity and recovered the most clinical terms (18.1% of a 1,440-term reference vocabulary, vs 12.5% for GPT-2 and 9.4% for LLaMA-2), yet no tokenizer prevented leakage. Substantial portions of report text are therefore recoverable from FL gradients even at larger batch sizes and with domain-specific tokenizers. Tokenizer design influences leakage severity and is a privacy-relevant decision, not only a utility one; safeguards such as secure aggregation and differential privacy are likely necessary to meet HIPAA and GDPR requirements for FL in radiology NLP.

---


### 32. [SeeSE3: Emergence of 3D Space in Vision Features](https://arxiv.org/abs/2607.14228)

**<font color=#1a73e8>作者：</font>** Caroline Chen, Sayna Ebrahimi, Fedor Kitashov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we ask whether vision foundation models construct representations that reflect the intrinsic properties of 3D Euclidean space. Unlike previous works that probe 3D awareness of vision features by regressing image-centric quantities such as depth or normals, we investigate the relation between the structure of the space of visual features and the group of Euclidean transformations $SE(3)$. We propose a set of probes to evaluate this relation from both topological and geometric perspectives: a mutual neighborhood metric that measures the alignment between feature neighborhoods and spatial topology, and a Poincaré Adapter to test the linear accessibility of the geometry of camera motion from latent displacements in static scenes. We show that self-supervised vision models, which, in principle, have not been trained with direct 3D supervision or active agency, possess latent subspaces that are remarkably strongly correlated with three-dimensional Euclidean space, when probed correctly. Building on this insight we propose a new class of "Latent-Space Navigation" techniques that perform visual odometry and localization purely in the latent space, bypassing the need for explicit 3D reconstruction.

---


### 33. [LIGO-PINN: Learned Initialization via Gated Optimization to Alleviate Convergence Failures in Physics Informed Neural Networks](https://arxiv.org/abs/2607.14233)

**<font color=#1a73e8>作者：</font>** Nilay Anurag, Shital Adhikari, Taniya Kapoor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have had a broad research impact in modeling domains governed by partial differential equations (PDE). However, PINNs have been shown to perform poorly, sometimes even converging to trivial solutions, in challenging PDE domains, or when generalizing to unseen but related PDE domains. Previously proposed solutions detail hyperparameter tuning to reduce loss imbalance between data-driven and physics guided losses, curriculum learning based training strategies, or dynamic re-sampling of hard collocation points. These methods face certain pitfalls: hyperparameter tuning is expensive, designing a training curriculum is ambiguous in multi-parameter PDE settings, and dynamic resampling still fails in complex PDE settings. Complementary to this line of thinking, we believe the initial PINN network weights also play a crucial role in the emergence of catastrophic failures during training, yet the effect of PINN weight initialization has been surprisingly under-investigated. To this end, we propose a framework for Learned Initialization via Gated Layerwise Optimization (LIGO-PINN) to overcome PINN convergence failures. Through rigorous evaluation on 1D and 2D PDE domains, including a challenging 2D fluid dynamics setting, we demonstrate that our methodology outperforms state-of-the-art methods designed to alleviate PINN failures, achieving a 91.5% average performance improvement across six baselines and 81% over the strongest baseline. We also verify that LIGO-PINN generalizes to 3D unstructured domains. Finally, we analyze training dynamics across all three PDE domains to explain both LIGO-PINN's improvement and the convergence failure of traditional PINNs. Code: this https URL
Keywords: Machine Learning, Physics-Informed Neural Networks, Deep Learning, PDE Modeling

---


### 34. [Align AI to Dynamic Human-AI Workflows](https://arxiv.org/abs/2607.14240)

**<font color=#1a73e8>作者：</font>** Valerie Chen, Cleotilde Gonzalez, Anita Williams Woolley 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current alignment approaches typically focus on emulating human behavior using static representations of human preferences, failing to capture the dynamic, context-dependent nature of real-world human-AI interactions. In this paper, we argue for a shift from static and emulative to interactive and complementary alignment, where preferences emerge through interaction and alignment is defined not by satisfying preferences alone. We first formalize this gap by contrasting existing alignment with a trajectory-level view in which human and model behavior co-evolve over time. Because these interaction dynamics have not been adequately captured within existing ML formulations, we ground this perspective in insights from an interdisciplinary workshop. We draw on lessons from social-science accounts of human-human collaboration and then argue that human-AI systems amplify these dynamics, introducing new asymmetries that make reasoning about uncertainty harder and introduce new coordination challenges. Based on these lessons and new challenges, we conclude by outlining a research agenda for developing AI systems that align with humans in interaction, requiring an interdisciplinary synthesis of machine learning and the social and decision sciences.

---


### 35. [Implicit Reasoning Steering via Concept Chaining](https://arxiv.org/abs/2607.14242)

**<font color=#1a73e8>作者：</font>** Xiao Ye, Sanika Chavan, Yuxi Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often appear to reason reliably, yet on many questions repeated sampling yields both correct and incorrect answers, revealing an underlying fragility in how final decisions are formed. We study whether this fragility can be exploited through implicit reasoning steering: using natural-language text to bias a model toward a designated answer without explicit instructions, triggers, or direct answer cues. Our approach, Concept Chaining, generates a short connection paragraph that links question entities to a target option through one or two intermediate concepts. We then continue pretraining a victim model on these connection paragraphs and evaluate whether its answer preference shifts on the original multiple-choice questions. Our results show that indirect, natural-looking text can systematically steer model predictions while remaining substantially less inferable than direct paraphrases, which shows that reasoning brittleness is not merely an evaluation artifact: it creates a practical channel through which latent biases can be amplified by ordinary-looking text to covertly redirect model decisions.

---


### 36. [The Steering Budget: Examples beat Knobs](https://arxiv.org/abs/2607.14246)

**<font color=#1a73e8>作者：</font>** Raj Kumar Rajendran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models are steered with knobs -- prompts, guidance scales, property tags. Turn one as hard as you like and, past a point, it stops moving the property you care about. We find that ceiling is not a shortcoming of the model but a budget, set by the training data before the model is trained: a property's movable range splits in two -- the part a knob can reach, and a second, significant part that only examples -- concrete instances of what you want more of -- can reach. That second part is usually much larger, but not always, and the same budget says so in advance.
Reaching that second part takes a different move: instead of turning a knob, you show the model examples, composed from what it already learned rather than added to its training. A cheap audit of the training data measures the budget; we give a recipe for building the example set that reaches all of it.
This buys two things a knob can't. Reach: it moves a property across the whole budget, not just the part a knob reaches. Expressiveness: it steers toward targets you can only specify by example -- including ones you can't put into words. We turn these into a handful of falsifiable claims and verify them in two unrelated domains, image and crystal-structure generation -- marking where a knob is enough, and where only examples will do.

---


### 37. [3D Lane Detection with Odometry for High-Speed Vehicle Racing](https://arxiv.org/abs/2607.14248)

**<font color=#1a73e8>作者：</font>** Omoruyi Atekha, John Subosits, Marcus Greiff  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lane boundary detection is a critical component in autonomous driving systems and has been rigorously studied in regular driving scenarios. However, it is less explored in vehicle racing, where the car moves at higher speeds across more extreme road geometries. To study this problem, we introduce a new dataset for 3D lane detection in racing, featuring >$250$k images from multiple camera feeds and inertial measurements taken with a Lexus LC 500 driving on a closed circuit. With this dataset, we compare various approaches to 3D lane detection and propose modifications that permit frames to be processed at rates of almost 300Hz while retaining high predictive performance in the racing application. This facilitates a multi-camera ensemble approach that is validated on hardware. We show that sensing modalities such as inertial measurements can be leveraged for pre-integration to regress road geometries over both cameras and time, yielding improvements in key metrics. Compared to methods such as BevLaneDet, adding odometry and ensemble predictions improves the F1 score by 3 points and reduces near-vehicle mean absolute errors (MAEs) by $>30 \%$. We show F1 scores $>$0.9 and lateral MAEs of $<$0.18m in vehicle deployments.

---


### 38. [MIDiff: Tackling Sparsity and Imbalance in Mobile Usage Generation via Multivariate-Imaging Diffusion](https://arxiv.org/abs/2607.14249)

**<font color=#1a73e8>作者：</font>** Yilai Liu, Shiyuan Zhang, Hongyang Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile usage traces are critical for tasks such as user behavior prediction and app recommendation, yet their use is constrained by privacy restrictions and costly large-scale data collection. Although generative models perform well on general time series, their application to mobile usage data remains challenging because (i) limited user activity causes severe sparsity, (ii) heterogeneous variable types complicate joint modeling, and (iii) functional differences across apps create pronounced usage imbalance. To address these challenges, we propose Multivariate-Imaging Diffusion (MIDiff), a diffusion-based framework operating in an imaging space defined by Cross-Gramian Angular Sum Field (C-GASF). C-GASF transforms sparse multivariate sequences into correlation images, while MIDiff employs Triple Attention in a U-Net to preserve temporal consistency and variable dependencies. Experiments show that MIDiff achieves state-of-the-art performance across fidelity metrics. In particular, it obtains a Discriminative Accuracy (DA) of 0.1526, compared with 0.3476 for the strongest baseline, ZITS-VAE, demonstrating its effectiveness in generating realistic and diverse mobile usage traces. Our code is available at this https URL.

---


### 39. [Local Additive Feature Attribution: A Mathematical Taxonomy and Reporting Checklist](https://arxiv.org/abs/2607.14271)

**<font color=#1a73e8>作者：</font>** Rebecca Afriyie Sarpong, Daniel Commey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature-attribution methods are central to explainable artificial intelligence. Their assumptions are expressed in several mathematical languages: cooperative-game values, path integrals, gradient operators, perturbation distributions, and backpropagation rules. This survey proposes a common framework for local additive feature attribution. It organizes Shapley, path-based, gradient/backpropagation, perturbation, and CAM-style methods around five specification choices: value function, reference, path, perturbation distribution, and conservation rule. It then compares these methods through an axiom-by-method matrix and links common failure modes, including baseline sensitivity, off-manifold perturbations, sanity-check failures, adversarial manipulation, and method disagreement, to the assumptions that produce them. Finally, the survey proposes a ten-item reporting checklist for studies that use local additive attributions. The central message is that attribution results are meaningful only relative to the mathematical assumptions under which they are defined, and that those assumptions should be reported.

---


### 40. [Lyapunov Guidance: A Unified Framework for Stabilizing Generative Flows](https://arxiv.org/abs/2607.14272)

**<font color=#1a73e8>作者：</font>** Jingdong Zhang, Xinze Li, Yize Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching has emerged as an effective framework for learning complex data distributions, but adapting pretrained flow models to new tasks often requires computationally expensive retraining. Post-training guidance provides a more efficient alternative, but existing methods are largely heuristic and offer no explicit stability guarantees. We address this limitation by proposing LyaGuide, a unified Lyapunov-guided framework that formulates flow guidance as a Lyapunov control problem. Our main theoretical result establishes an equivalence between guided flow matching and Lyapunov control, thereby unifying common guidance strategies, such as classifier guidance, reward guidance, and energy-based guidance, within a single control-theoretic framework. To enforce the Lyapunov condition, we introduce a pseudo-projection operator with a closed-form expression that endows learned or heuristic guidance terms with explicit stability guarantees. LyaGuide supports two practical settings: a model-driven setting, where the target guidance distribution is specified through a known Lyapunov function, and a data-driven setting, where the guidance is adapted from task-specific downstream data. LyaGuide is compatible with existing guidance methods, introduces minimal additional computational overhead, and is straightforward to integrate in practice. Extensive experiments on synthetic benchmarks, image inverse problems, reinforcement learning planning, and energy-based modeling demonstrate consistent improvements in sample quality, guidance fidelity, and robustness, while maintaining computational efficiency.

---


### 41. [XCT-SAM: Sequential Parameter-Efficient Domain Adaptation of SAM for Industrial XCT Defect Segmentation](https://arxiv.org/abs/2607.14287)

**<font color=#1a73e8>作者：</font>** Md Mahedi Hasan, Md Mushfiqur Rahaman, Alan Pachkovskiy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Defect segmentation in additive manufacturing (AM) X-ray computed tomography (XCT) images remains challenging due to severe class imbalance and large distribution shifts across scan conditions. Although recent foundation models such as the Segment Anything Model (SAM) provide strong general-purpose segmentation priors, their natural-image pre-training transfers poorly to the AM XCT domain, where defects appear as subtle non-semantic microstructural anomalies. Moreover, adapting SAM to the AM domain is further limited by the large domain gap and scarcity of labeled real XCT data. We present XCT-SAM, a sequential parameter-efficient adaptation framework for AM XCT defect segmentation. Instead of adapting SAM directly from natural images to XCT data, we first fine-tune Conv-LoRA adapters on an alloy-microstructure dataset and subsequently transfer the adapted model to XCT images, progressively bridging the domain gap. Using Conv-LoRA adapters with rank r=2, the framework injects convolutional spatial inductive bias into SAM's backbone while training approximately 4.15M parameters and keeping over 99% of the model frozen. We evaluate XCT-SAM on out-of-distribution CycleGAN-XCT benchmarks and real-world NIST XCT scans. Across both settings, XCT-SAM consistently outperforms zero-shot SAM and other domain-adapted SAM baselines, achieving the best overall IoU and Dice scores. These results demonstrate the effectiveness of intermediate domain adaptation with parameter-efficient adapters for industrial XCT defect segmentation. The source code is publicly available at this https URL

---


### 42. [Measuring How Students Rely on Generative AI in Academic Writing: Development and Multi-Source Validation of the Generative AI Reliance Types Scale (GenAI-RTS)](https://arxiv.org/abs/2607.14301)

**<font color=#1a73e8>作者：</font>** Shahin Hossain, Tukhbita Afroz Nawmi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As generative AI (GenAI) becomes increasingly embedded in undergraduate academic writing, how students rely on these tools, rather than simply whether they use them, has become a central question for learning, academic integrity, and educational equity. Existing measures of reliance were developed inductively, focused on discrete problem-solving tasks, and validated mainly with homogeneous samples. This study developed and validated the GenAI Reliance Types Scale (GenAI-RTS), a 20-item instrument measuring four theoretically derived types of GenAI reliance: Strategic, Instrumental, Dependent, and Dialogic. Validation followed the multisource framework of the Standards for Educational and Psychological Testing, drawing on a survey of 382 undergraduates at a U.S. Minority-Serving Institution and interviews with 14 purposively sampled students. Confirmatory factor analyses of six competing models supported a five-factor structure in which Strategic Reliance comprises two facets, Deliberate Use and Critical Evaluation, alongside Instrumental, Dependent, and Dialogic factors (CFI = .92, RMSEA = .08; DWLS CFI = .98, RMSEA = .07). Subscale reliability was acceptable to good (omega = .75-.88), and scalar measurement invariance held across gender, first-generation status, and STEM/non-STEM majors, to our knowledge the first such evidence for a GenAI reliance instrument. Rasch analysis indicated that a five-point response format would improve category functioning. Strategic reliance was positively associated with AI literacy, and the reliance types differentiated students across multiple writing process and outcome variables. The GenAI-RTS offers researchers and educators a theoretically grounded, psychometrically validated instrument for identifying undergraduate reliance profiles and supporting research, assessment, and AI literacy intervention.

---


### 43. [DCVC-MB: Neural B-Frame Video Compression using State Space Models](https://arxiv.org/abs/2607.14305)

**<font color=#1a73e8>作者：</font>** Arjun Arora, Calvin-Khang Ta, Carlos Restrepo-Galeano 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper we propose DCVC-Mamba (DCVC-MB), a neural video codec framework for B-frame coding. Our approach incorporates an IBP frame strategy for low-delay B-frame coding, a spatio-temporal fusion model based on state-space models for bidirectional temporal prediction, and an entropy-aware skipping mechanism that selectively omits coding certain latents to reduce entropy coding times. In addition to our model contributions we also implement two inference-time strategies that enhance compression performance. Experimental evaluation shows that DCVC-MB compares favorably to existing NVCs and traditional codecs. The method demonstrates BD-rate reductions of up to $8.98\%$ on average compared to prior neural video codecs, and improvements of up to $30.45\%$ and $1.81\%$ over the VTM-19.0-LDP and VTM-19.0-RA(Inter-GoP=16) benchmarks, respectively, contributing to advances in neural video compression.

---


### 44. [Towards a Unified Multidimensional Explainability Metric: Evaluating Trustworthiness in AI Models](https://arxiv.org/abs/2607.14315)

**<font color=#1a73e8>作者：</font>** Georgios Makridis, Georgios Fatouros, Athanasios Kiourtis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a comprehensive framework for assessing the explainability of various XAI methods, such as LIME and SHAP, across multiple datasets and machine learning models, with the ultimate goal of creating a unified multidimensional explainability score. Our methodology focuses on three key aspects of explainability: fidelity, simplicity, and stability. We leverage benchmarking experiments to systematically evaluate these aspects and use the insights gained to construct an offline knowledge base. This knowledge base captures the explainability scores for each registered model and serves as a valuable resource for context-dependent evaluation of explainability. By analyzing the complementary characteristics and metadata of AI models, datasets, and XAI methods, the knowledge base will enable the estimation of explainability scores for previously unseen datasets and models. Properties like fidelity, simplicity, and stability may vary significantly based on the dataset, underlying model, and domain expertise of the end user. We demonstrate our framework by applying it to three open-source datasets, discussing the implications of the obtained results in relation to the characteristics of the datasets. Our work contributes to the growing field of XAI by providing a robust and versatile tool for evaluating and comparing the explainability of various XAI methods, ultimately supporting the development of more transparent and trustworthy AI systems.

---


### 45. [Counterfactual Optimal Action Trees (COAT): Interpretable Prescriptive Policies from Observational Data](https://arxiv.org/abs/2607.14318)

**<font color=#1a73e8>作者：</font>** Youssef Drissi, Markus Ettl, Shivaram Subramanian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce COAT (Counterfactual Optimal Action Tree), a framework for learning interpretable prescriptive policies from observational data. COAT combines counterfactual outcome estimation with large-scale mixed-integer optimization, using column generation to translate causal predictions into feasible, transparent decisions under business and regulatory constraints. We apply COAT to airline ancillary pricing, a setting characterized by complex business rules and limited experimental flexibility. In a 17-week field pilot with a major global airline, COAT increased upsell revenue per booking by 6.9%, with the airline projecting \$50-\$150 million in incremental annual premium seat revenue across eligible domestic markets. The success of the pilot led to scaled adoption and informed broader AI-driven decision initiatives within the organization.

---


### 46. [PReM: Learning What to Preserve and When to Refresh for Context Compression](https://arxiv.org/abs/2607.14327)

**<font color=#1a73e8>作者：</font>** Bohan Yu, Lei Shen, Chenxi Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficient long-context inference is not only about reducing memory cost, but also about keeping useful contextual evidence accessible as generation proceeds. However, existing compression-oriented approaches, such as key-value (KV) cache compression and context compression, often either make an early decision about which contextual information to keep or rely on an external compressor. Such designs make it difficult to adapt the compressed context to the evidence needed by later reasoning steps. This paper introduces PReM (Preserve and Refresh Memory), a context-compression framework that maintains the long context as the model's internal layer-wise KV memory and learns what to preserve and when to refresh it. Specifically, PReM uses a dedicated memory layer to make memory-selection decisions, and a special memory token <m> to trigger refreshes during generation. To train this behavior, PReM introduces Phase-Separated Refresh Training, aligning memory selection with memory-conditioned generation while preserving continuity across refreshes. Experiments with 32K-token contexts show that PReM outperforms strong baselines under both 16x and 32x compression, while maintaining a favorable balance between answer quality and inference efficiency.

---


### 47. [Beyond scalar losses: calibrating segmentation models via gradient vector field surgery](https://arxiv.org/abs/2607.14338)

**<font color=#1a73e8>作者：</font>** Laurin Lux, Alexander H. Berger, Moritz Knolle 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Region-based loss functions, such as the Dice loss, have established themselves as the de facto standard for highly class- and region-imbalanced segmentation tasks. However, models trained using region-based loss functions are notoriously miscalibrated and typically yield over-confident predictions. In medical imaging applications, such as defining tumor resection margins, this miscalibration is hindering clinical adoption. In this work, we outline a novel gradient perspective on this overconfidence and show how it affects region-based loss functions. We propose a "surgery" on the gradient vector field as a simple, yet effective intervention to mitigate calibration issues. This surgery adds a factor to the loss's partial derivative, scaling the gradient's magnitude linearly with the prediction error. In empirical evaluations across 2D and 3D medical segmentation tasks, we demonstrate the effectiveness of this intervention while maintaining high prediction accuracy when used in conjunction with any region-based loss function.

---


### 48. [Learning Who to Treat When Treatment is Missing](https://arxiv.org/abs/2607.14346)

**<font color=#1a73e8>作者：</font>** Johnna Sundberg, Rayid Ghani, Eli Ben-Michael 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy learning methods are increasingly used to inform treatment allocation under budget constraints. Most proposed methods assume complete treatment data, yet applications frequently suffer from missingness that can bias estimates and lead to suboptimal policies. We address this gap by extending efficient estimators for average treatment effect (ATE) estimation to policy value and conditional average treatment effect (CATE) estimation under missing at random (MAR) and missing completely conditionally at random (MCCAR) treatment data. Through asymptotic efficiency analysis, we prove that the MAR estimator, which leverages partially-observed units, is both valid and more efficient than the MCCAR estimator when MCCAR assumptions hold. This result provides formal justification for preferring MAR-based estimation in policy learning under both missing data settings. Our comprehensive experiments using synthetic and semi-synthetic datasets confirm that correctly specifying the missingness mechanism is crucial: misspecified estimators remain biased regardless of sample size, while our estimators achieve near-oracle performance when assumptions are satisfied. Our work provides practitioners with theoretically grounded, empirically validated tools for robust policy learning in the presence of missing treatment data.

---


### 49. [HABIB_TAZ at SemEval-2026 Task 11: Disentangling Formal Logic from Content via Synthetic Training and Multi-Objective Optimization](https://arxiv.org/abs/2607.14349)

**<font color=#1a73e8>作者：</font>** Abdullah Shaikh, Zain Naqi, Taha Zahid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) excel in many general NLP tasks, their formal reasoning capabilities are often compromised by content effects, demonstrating a measurable bias towards real-world plausibility. In this paper, we present our system for SemEval-2026 Task 11, which evaluates the ability of models to disentangle formal logic from content across 12 languages with and without distractor premises. We address this challenge using mDeBERTa-v3 networks fine-tuned on a synthetic, rule-based dataset of syllogistic schemes to avoid the semantic noise of LLM-augmented data. To explicitly decouple plausibility from logical structure, our training pipeline employs a multi-objective loss function combining Adaptive Group Distributionally Robust Optimization (DRO), a scheduled differentiable bias penalty, and KL-Divergence consistency regularization. Our system achieved #1 ranks and perfect Ranking Scores (100.0) with 0.00% bias and 100.0% accuracy on Subtask 1 (English), Subtask 2 (Noisy English), and Subtask 3 (Multilingual). On the highly complex Subtask 4 (Noisy Multilingual), the system achieved the 6th rank with 89.06% Accuracy and F1-score, alongside a limited 2.89% Bias and a 37.78 Ranking Score. Our dataset generation engine and codebase are publicly available to facilitate future work on robust logical reasoning.

---


### 50. [Dynamic Manipulation Hypergraphs for HAR: Beyond Pairwise Relations: Dynamic Manipulation Hypergraphs for Vision-Based Human Activity Recognition](https://arxiv.org/abs/2607.14350)

**<font color=#1a73e8>作者：</font>** Fatemeh Ziaeetabar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained manipulation recognition requires modeling evolving relations among hands, objects, tools, and supporting surfaces. Conventional graph-based methods use pairwise edges that can fragment a coordinated event into disconnected binary relations. We propose a dynamic manipulation hypergraph framework that represents multi-entity configurations as higher-order relational units. At each temporal step, relevant entities are encoded using appearance, spatial, motion, and semantic-role features. Hyperedge candidates are instantiated and ranked using proximity, contact, and motion-coupling predicates. A hypergraph reasoning network performs node-to-hyperedge and hyperedge-to-node message passing, followed by temporal attention over the evolving interaction structure. The framework provides class-agnostic hyperedge-importance scores that identify entity configurations and temporal intervals emphasized by the model without treating them as causal explanations. Quantitative evaluation is conducted on EPIC-KITCHENS-100/VISOR and Assembly101 under an annotation-assisted entity-localization protocol. Video-only and entity-based methods provide contextual comparisons, while a matched pairwise graph and a static hypergraph serve as the principal controlled baselines because they use identical entity inputs and comparable relational settings. The proposed method improves HO-F1 over the matched pairwise graph by 6.9 percentage points on EPIC-KITCHENS-100/VISOR and 9.5 points on Assembly101, and exceeds the static hypergraph by 4.4 and 5.8 points, respectively. Qualitative analysis on ARCTIC further shows correspondence between highly ranked hyperedges and contact-rich manipulation intervals. These results demonstrate the value of time-varying higher-order relational modeling for fine-grained manipulation activity recognition.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-221](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
