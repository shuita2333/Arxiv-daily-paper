# 📦 其他研究 | 2026年04月24日

> 本类共 **220** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-220](./part-05.md)

---

### 1. [AI to Learn 2.0: A Deliverable-Oriented Governance Framework and Maturity Rubric for Opaque AI in Learning-Intensive Domains](https://arxiv.org/abs/2604.19751)

**<font color=#1a73e8>作者：</font>** Seine A. Shintani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI is entering research, education, and professional work faster than current governance frameworks can specify how AI-assisted outputs should be judged in learning-intensive settings. The central problem is proxy failure: a polished artifact can be useful while no longer serving as credible evidence of the human understanding, judgment, or transfer ability that the work is supposed to cultivate or certify. This paper proposes AI to Learn 2.0, a deliverable-oriented governance framework for AI-assisted work. Rather than claiming element-wise novelty, it reorganizes adjacent ideas around the final deliverable package, distinguishes artifact residual from capability residual, and operationalizes the result through a five-part package, a seven-dimension maturity rubric, gate thresholds on critical dimensions, and a companion capability-evidence ladder. AI to Learn 2.0 allows opaque AI during exploration, drafting, hypothesis generation, and workflow design, but requires that the released deliverable be usable, auditable, transferable, and justifiable without the original large language model or cloud API. In learning-intensive contexts, it additionally requires context-appropriate human-attributable evidence of explanation or transfer. Worked scoring across contrastive cases, including coursework substitution, a symbolic-regression governance contrast, teacher-audited national-exam practice forms, and a self-hosted lecture-to-quiz pipeline with deterministic quality control, shows how the framework separates polished substitution workflows from bounded, auditable, and handoff-ready AI-assisted workflows. AI to Learn 2.0 is proposed as a governance instrument for structured third-party review where capability preservation, accountability, and validity boundaries matter.

---


### 2. [Soft-Label Governance for Distributional Safety in Multi-Agent Systems](https://arxiv.org/abs/2604.19752)

**<font color=#1a73e8>作者：</font>** Aizierjiang Aiersilan, Raeli Savitt  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent AI systems exhibit emergent risks that no single agent produces in isolation. Existing safety frameworks rely on binary classifications of agent behavior, discarding the uncertainty inherent in proxy-based evaluation. We introduce SWARM (\textbf{S}ystem-\textbf{W}ide \textbf{A}ssessment of \textbf{R}isk in \textbf{M}ulti-agent systems), a simulation framework that replaces binary good/bad labels with \emph{soft probabilistic labels} $p = P(v{=}+1) \in [0,1]$, enabling continuous-valued payoff computation, toxicity measurement, and governance intervention. SWARM implements a modular governance engine with configurable levers (transaction taxes, circuit breakers, reputation decay, and random audits) and quantifies their effects through probabilistic metrics including expected toxicity $\mathbb{E}[1{-}p \mid \text{accepted}]$ and quality gap $\mathbb{E}[p \mid \text{accepted}] - \mathbb{E}[p \mid \text{rejected}]$. Across seven scenarios with five-seed replication, strict governance reduces welfare by over 40\% without improving safety. In parallel, aggressively internalizing system externalities collapses total welfare from a baseline of $+262$ down to $-67$, while toxicity remains invariant. Circuit breakers require careful calibration; overly restrictive thresholds severely diminish system value, whereas an optimal threshold balances moderate welfare with minimized toxicity. Companion experiments show soft metrics detect proxy gaming by self-optimizing agents passing conventional binary evaluations. This basic governance layer applies to live LLM-backed agents (Concordia entities, Claude, GPT-4o Mini) without modification. Results show distributional safety requires \emph{continuous} risk metrics and governance lever calibration involves quantifiable safety-welfare tradeoffs. Source code and project resources are publicly available at this https URL.

---


### 3. [Algorithm Selection with Zero Domain Knowledge via Text Embeddings](https://arxiv.org/abs/2604.19753)

**<font color=#1a73e8>作者：</font>** Stefan Szeider  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a feature-free approach to algorithm selection that replaces hand-crafted instance features with pretrained text embeddings. Our method, ZeroFolio, proceeds in three steps: it reads the raw instance file as plain text, embeds it with a pretrained embedding model, and selects an algorithm via weighted k-nearest neighbors. The key to our approach is the observation that pretrained embeddings produce representations that distinguish problem instances without any domain knowledge or task-specific training. This allows us to apply the same three-step pipeline (serialize, embed, select) across diverse problem domains with text-based instance formats. We evaluate our approach on 11 ASlib scenarios spanning 7 domains (SAT, MaxSAT, QBF, ASP, CSP, MIP, and graph problems). Our experiments show that this approach outperforms a random forest trained on hand-crafted features in 10 of 11 scenarios with a single fixed configuration, and in all 11 with two-seed voting; the margin is often substantial. Our ablation study shows that inverse-distance weighting, line shuffling, and Manhattan distance are the key design choices. On scenarios where both selectors are competitive, combining embeddings with hand-crafted features via soft voting yields further improvements.

---


### 4. [Automated Detection of Dosing Errors in Clinical Trial Narratives: A Multi-Modal Feature Engineering Approach with LightGBM](https://arxiv.org/abs/2604.19759)

**<font color=#1a73e8>作者：</font>** Mohammad AL-Smadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical trials require strict adherence to medication protocols, yet dosing errors remain a persistent challenge affecting patient safety and trial integrity. We present an automated system for detecting dosing errors in unstructured clinical trial narratives using gradient boosting with comprehensive multi-modal feature engineering. Our approach combines 3,451 features spanning traditional NLP (TF-IDF, character n-grams), dense semantic embeddings (all-MiniLM-L6v2), domain-specific medical patterns, and transformer-based scores (BiomedBERT, DeBERTa-v3), used to train a LightGBM model. Features are extracted from nine complementary text fields (median 5,400 characters per sample) ensuring complete coverage across all 42,112 clinical trial narratives. On the CT-DEB benchmark dataset with severe class imbalance (4.9% positive rate), we achieve 0.8725 test ROC-AUC through 5-fold ensemble averaging (cross-validation: 0.8833 + 0.0091 AUC). Systematic ablation studies reveal that removing sentence embeddings causes the largest performance degradation (2.39%), demonstrating their critical role despite contributing only 37.07% of total feature importance. Feature efficiency analysis demonstrates that selecting the top 500-1000 features yields optimal performance (0.886-0.887 AUC), outperforming the full 3,451-feature set (0.879 AUC) through effective noise reduction. Our findings highlight the importance of feature selection as a regularization technique and demonstrate that sparse lexical features remain complementary to dense representations for specialized clinical text classification under severe class imbalance.

---


### 5. [Inference Headroom Ratio: A Diagnostic and Control Framework for Inference Stability Under Constraint](https://arxiv.org/abs/2604.19760)

**<font color=#1a73e8>作者：</font>** Robert Reinertsen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a simulation-based evaluation of the Inference Headroom Ratio (IHR), a dimensionless diagnostic quantity for characterizing inference stability in constrained decision systems. IHR formalizes the relationship between a system's effective inferential capacity C and the combined uncertainty and constraint load U + K imposed by its operating environment, and is intended to capture proximity to an inference stability boundary rather than output-level performance. Across three controlled experiments, we show that IHR functions as: (1) a quantifiable risk indicator whose relationship to collapse probability follows a well-fitted logistic curve with estimated critical threshold IHR* approx. 1.19, (2) a sensitive indicator of proximity to the inference stability boundary under environmental noise, and (3) a viable control variable whose active regulation reduces system collapse rate from 79.4% to 58.7% and IHR variance by 70.4% across 300 Monte Carlo runs. These results position IHR as a prospective, system-level complement to standard performance, drift, and uncertainty metrics, enabling estimation of remaining inferential margin before overt failure in AI systems operating under distributional shift and constraint.

---


### 6. [EvoForest: A Novel Machine-Learning Paradigm via Open-Ended Evolution of Computational Graphs](https://arxiv.org/abs/2604.19761)

**<font color=#1a73e8>作者：</font>** Kamer Ali Yuksel, Hassan Sawaf  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern machine learning is still largely organized around a single recipe: choose a parameterized model family and optimize its weights. Although highly successful, this paradigm is too narrow for many structured prediction problems, where the main bottleneck is not parameter fitting but discovering what should be computed from the data. Success often depends on identifying the right transformations, statistics, invariances, interaction structures, temporal summaries, gates, or nonlinear compositions, especially when objectives are non-differentiable, evaluation is cross-validation-based, interpretability matters, or continual adaptation is required. We present EvoForest, a hybrid neuro-symbolic system for end-to-end open-ended evolution of computation. Rather than merely generating features, EvoForest jointly evolves reusable computational structure, callable function families, and trainable low-dimensional continuous components inside a shared directed acyclic graph. Intermediate nodes store alternative implementations, callable nodes encode reusable transformation families such as projections, gates, and activations, output nodes define candidate predictive computations, and persistent global parameters can be refined by gradient descent. For each graph configuration, EvoForest evaluates the discovered computation and uses a lightweight Ridge-based readout to score the resulting representation against a non-differentiable cross-validation target. The evaluator also produces structured feedback that guides future LLM-driven mutations. In the 2025 ADIA Lab Structural Break Challenge, EvoForest reached 94.13% ROC-AUC after 600 evolution steps, exceeding the publicly reported winning score of 90.14% under the same evaluation protocol.

---


### 7. [Evidence of Layered Positional and Directional Constraints in the Voynich Manuscript: Implications for Cipher-Like Structure](https://arxiv.org/abs/2604.19762)

**<font color=#1a73e8>作者：</font>** Christophe Parisel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Voynich Manuscript (VMS) exhibits a script of uncertain origin whose grapheme sequences have resisted linguistic analysis. We present a systematic analysis of its grapheme sequences, revealing two complementary structural layers: a character-level right-to-left optimization in word-internal sequences and a left-to-right dependency at word boundaries, a directional dissociation not observed in any of our four comparison languages (English, French, Hebrew, Arabic).
We further evaluate two classes of structured generator against a four-signature joint criterion: a parametric slot-based generator and a Cardan grille implementing Rugg's (2004) gibberish hypothesis. Across their full tested parameter spaces, neither class reproduces all four signatures simultaneously.
While these results do not rule out generator classes we have not tested, they provide the first quantitative benchmarks against which any future generative or cryptanalytic model of the VMS can be evaluated, and they suggest that the VMS exhibits cipher-like structural constraints that are difficult to reproduce from simple positional or frequency-based mechanisms alone.

---


### 8. [Accelerating PayPal's Commerce Agent with Speculative Decoding: An Empirical Study on EAGLE3 with Fine-Tuned Nemotron Models](https://arxiv.org/abs/2604.19767)

**<font color=#1a73e8>作者：</font>** Ally Qin, Jian Wan, Sarat Mudunuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluate speculative decoding with EAGLE3 as an inference-time optimization for PayPal's Commerce Agent, powered by a fine-tuned llama3.1-nemotron-nano-8B-v1 model. Building on prior work (NEMO-4-PAYPAL) that reduced latency and cost through domain-specific fine-tuning, we benchmark EAGLE3 via vLLM against NVIDIA NIM on identical 2xH100 hardware across 40 configurations spanning speculative token counts (gamma=3, gamma=5), concurrency levels (1-32), and sampling temperatures (0, 0.5). Key findings: (1) gamma=3 achieves 22-49% throughput improvement and 18-33% latency reduction at zero additional hardware cost; (2) acceptance rates remain stable at approximately 35.5% for gamma=3 across all conditions; (3) gamma=5 yields diminishing returns (approximately 25% acceptance rate); (4) LLM-as-Judge evaluation confirms fully preserved output quality; and (5) speculative decoding on a single H100 matches or exceeds NIM on two H100s, enabling 50% GPU cost reduction.

---


### 9. [Hybrid Multi-Phase Page Matching and Multi-Layer Diff Detection for Japanese Building Permit Document Review](https://arxiv.org/abs/2604.19770)

**<font color=#1a73e8>作者：</font>** Mitsumasa Wada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a hybrid multi-phase page matching algorithm for automated comparison of Japanese building permit document sets. Building permit review in Japan requires cross-referencing large PDF document sets across revision cycles, a process that is labor-intensive and error-prone when performed manually. The algorithm combines longest common subsequence (LCS) structural alignment, a seven-phase consensus matching pipeline, and a dynamic programming optimal alignment stage to robustly pair pages across revisions even when page order, numbering, or content changes substantially. A subsequent multi-layer diff engine -- comprising text-level, table-level, and pixel-level visual differencing -- produces highlighted difference reports. Evaluation on real-world permit document sets achieves F1=0.80 and precision=1.00 on a manually annotated ground-truth benchmark, with zero false-positive matched pairs.

---


### 10. [Cognis: Context-Aware Memory for Conversational AI Agents](https://arxiv.org/abs/2604.19771)

**<font color=#1a73e8>作者：</font>** Parshva Daftari, Khush Patel, Shreyas Kapale 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents lack persistent memory, causing conversations to reset each session and preventing personalization over time. We present Lyzr Cognis, a unified memory architecture for conversational AI agents that addresses this limitation through a multi-stage retrieval pipeline. Cognis combines a dual-store backend pairing OpenSearch BM25 keyword matching with Matryoshka vector similarity search, fused via Reciprocal Rank Fusion. Its context-aware ingestion pipeline retrieves existing memories before extraction, enabling intelligent version tracking that preserves full memory history while keeping the store consistent. Temporal boosting enhances time-sensitive queries, and a BGE-2 cross-encoder reranker refines final result quality. We evaluate Cognis on two independent benchmarks -- LoCoMo and LongMemEval -- across eight answer generation models, demonstrating state-of-the-art performance on both. The system is open-source and deployed in production serving conversational AI applications.

---


### 11. [Towards High-Quality Machine Translation for Kokborok: A Low-Resource Tibeto-Burman Language of Northeast India](https://arxiv.org/abs/2604.19778)

**<font color=#1a73e8>作者：</font>** Badal Nyalang, Biman Debbarma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present KokborokMT, a high-quality neural machine translation (NMT) system for Kokborok (ISO 639-3), a Tibeto-Burman language spoken primarily in Tripura, India with approximately 1.5 million speakers. Despite its status as an official language of Tripura, Kokborok has remained severely under-resourced in the NLP community, with prior machine translation attempts limited to systems trained on small Bible-derived corpora achieving BLEU scores below 7. We fine-tune the NLLB-200-distilled-600M model on a multi-source parallel corpus comprising 36,052 sentence pairs: 9,284 professionally translated sentences from the SMOL dataset, 1,769 Bible-domain sentences from WMT shared task data, and 24,999 synthetic back-translated pairs generated via Gemini Flash from Tatoeba English source sentences. We introduce as a new language token for Kokborok in the NLLB framework. Our best system achieves BLEU scores of 17.30 and 38.56 on held-out test sets, representing substantial improvements over prior published results. Human evaluation by three annotators yields mean adequacy of 3.74/5 and fluency of 3.70/5, with substantial agreement between trained evaluators.

---


### 12. [Using Learning Theories to Evolve Human-Centered XAI: Future Perspectives and Challenges](https://arxiv.org/abs/2604.19788)

**<font color=#1a73e8>作者：</font>** Karina Cortinas-Lorenzo, Gavin Doherty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Artificial Intelligence (AI) systems continue to grow in size and complexity, so does the difficulty of the quest for AI transparency. In a world of large models and complex AI systems, why do we explain AI and what should we explain? While explanations serve multiple functions, in the face of complexity humans have used and continue to use explanations to foster learning. In this position paper, we discuss how learning theories can be infused in the XAI lifecycle, as well as the key opportunities and challenges when adopting a learner-centered approach to assess, design and evaluate AI explanations. Building on past work, we argue that a learner-centered approach to Explainable AI (XAI) can enhance human agency and ease XAI risks mitigation, helping evolve the practice of human-centered XAI.

---


### 13. [Stabilising Generative Models of Attitude Change](https://arxiv.org/abs/2604.19791)

**<font color=#1a73e8>作者：</font>** Jayd Matyas, William A. Cunningham, Alexander Sasha Vezhnevets 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attitude change - the process by which individuals revise their evaluative stances - has been explained by a set of influential but competing verbal theories. These accounts often function as mechanism sketches: rich in conceptual detail, yet lacking the technical specifications and operational constraints required to run as executable systems. We present a generative actor-based modelling workflow for "rendering" these sketches as runnable actor - environment simulations using the Concordia simulation library. In Concordia, actors operate by predictive pattern completion: an operation on natural language strings that generates a suffix which describes the actor's intended action from a prefix containing memories of their past and observations of the present. We render the theories of cognitive dissonance (Festinger 1957), self-consistency (Aronson 1969), and self-perception (Bem 1972) as distinct decision logics that populate and process the prefix through theory-specific sequences of reasoning steps. We evaluate these implementations across classic psychological experiments. Our implementations generate behavioural patterns consistent with known results from the original empirical literature. However, we find that achieving stable reproduction requires resolving the inherent underdetermination of the verbal accounts and the conflicts between modern linguistic priors and historical experimental assumptions. And, we document how this manual process of iterative model "stabilisation" surfaces specific operational and socio-ecological dependencies that were largely undocumented in the original verbal accounts. Ultimately, we argue that the manual stabilisation process itself should be regarded as a core part of the methodology functioning to clarify situational and representational commitments needed to generate characteristic effects.

---


### 14. [OpenCLAW-P2P v6.0: Resilient Multi-Layer Persistence, Live Reference Verification, and Production-Scale Evaluation of Decentralized AI Peer Review](https://arxiv.org/abs/2604.19792)

**<font color=#1a73e8>作者：</font>** Francisco Angulo de Lafuente, Teerth Sharma, Vladimir Veselov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents OpenCLAW-P2P v6.0, a comprehensive evolution of the decentralized collective-intelligence platform in which autonomous AI agents publish, peer-review, score, and iteratively improve scientific research papers without any human gatekeeper. Building on v5.0 foundations -- tribunal-gated publishing, multi-LLM granular scoring, calibrated deception detection, the Silicon Chess-Grid FSM, and the AETHER containerized inference engine -- this release introduces four major new subsystems: (1) a multi-layer paper persistence architecture with four storage tiers (in-memory cache, Cloudflare R2, this http URL, GitHub) ensuring zero paper loss across redeployments; (2) a multi-layer retrieval cascade with automatic backfill reducing lookup latency from >3s to <50ms; (3) live reference verification querying CrossRef, arXiv, and Semantic Scholar during scoring to detect fabricated citations with >85% accuracy; and (4) a scientific API proxy providing rate-limited cached access to seven public databases. The platform operates with 14 real autonomous agents producing 50+ scored papers (word counts 2,072-4,073, leaderboard scores 6.4-8.1) alongside 23 labeled simulated citizens. We present honest production statistics, failure-mode analysis, a paper recovery protocol that salvaged 25 lost papers, and lessons learned from operating the system at scale. All pre-existing subsystems -- 17-judge multi-LLM scoring, 14-rule calibration with 8 deception detectors, tribunal cognitive examination, Proof of Value consensus, Laws-of-Form eigenform verification, and tau-normalized agent coordination -- are retained and further hardened. All code is open-source at this https URL.

---


### 15. [Handbook of Rough Set Extensions and Uncertainty Models](https://arxiv.org/abs/2604.19794)

**<font color=#1a73e8>作者：</font>** Takaaki Fujita, Florentin Smarandache  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rough set theory models uncertainty by approximating target concepts through lower and upper sets induced by indiscernibility, or more generally, by granulation relations in data tables. This perspective captures vagueness caused by limited observational resolution and supports set-theoretic reasoning about what can be determined with certainty and what remains only possible. This book is written as a map of models. Rather than developing a single algorithmic pipeline in depth, it provides a systematic survey of the main rough set paradigms and their extension routes. More specifically, representative variants are organized according to (i) the underlying granulation mechanism, such as equivalence-based, tolerance-based, covering-based, neighborhood-based, and probabilistic approximations, and (ii) the uncertainty semantics attached to data and relations, such as crisp, fuzzy, intuitionistic fuzzy, neutrosophic, and plithogenic settings. The book also explains how each choice changes the form of approximations and the interpretation of boundary regions. Throughout the book, small illustrative examples are used to clarify modeling intent and typical use cases in classification and decision support. Finally, an important clarification of scope should be noted. Since the main purpose of this book is to provide a map of models, the Abstract and Introduction should not lead readers to expect that feature reduction and rule induction are primary objectives. Although these topics are central in the rough set literature, they are treated here mainly as motivating applications and as entry points to the broader research landscape. The principal aim of the book is to survey and position rough set models and their extensions in a systematic and coherent manner.

---


### 16. [Prism: An Evolutionary Memory Substrate for Multi-Agent Open-Ended Discovery](https://arxiv.org/abs/2604.19795)

**<font color=#1a73e8>作者：</font>** Suyash Mishra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce \prism{} (\textbf{P}robabilistic \textbf{R}etrieval with \textbf{I}nformation-\textbf{S}tratified \textbf{M}emory), an evolutionary memory substrate for multi-agent AI systems engaged in open-ended discovery. \prism{} unifies four independently developed paradigms -- layered file-based persistence, vector-augmented semantic memory, graph-structured relational memory, and multi-agent evolutionary search -- under a single decision-theoretic framework with eight interconnected subsystems.
We make five contributions: (1)~an \emph{entropy-gated stratification} mechanism that assigns memories to a tri-partite hub (skills/notes/attempts) based on Shannon information content, with formal context-window utilization bounds; (2)~a \emph{causal memory graph} $\mathcal{G} = (V, E_r, E_c)$ with interventional edges and agent-attributed provenance; (3)~a \emph{Value-of-Information retrieval} policy with self-evolving strategy selection; (4)~a \emph{heartbeat-driven consolidation} controller with stagnation detection via optimal stopping theory; and (5)~a \emph{replicator-decay dynamics} framework that interprets memory confidence as evolutionary fitness, proving convergence to an Evolutionary Stable Memory Set (ESMS). On the LOCOMO benchmark, \prism{} achieves 88.1 LLM-as-a-Judge score (31.2\% over Mem0). On CORAL-style evolutionary optimization tasks, 4-agent \prism{} achieves 2.8$\times$ higher improvement rate than single-agent baselines.%

---


### 17. [Measuring Creativity in the Age of Generative AI: Distinguishing Human and AI-Generated Creative Performance in Hiring and Talent Systems](https://arxiv.org/abs/2604.19799)

**<font color=#1a73e8>作者：</font>** Yigal Rosen, Ilia Rushkin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is rapidly transforming how organizations create value and evaluate talent. While large language models enhance baseline output quality, they simultaneously introduce ambiguity in assessing human creativity, as observable artifacts may be partially or fully AI-generated. This paper reconceptualizes creativity as a distributional and process-based property that emerges under shared constraints and competitive incentives. We introduce a quantitative framework for measuring creativity as novelty in synthesis, operationalized through idea generation and idea transformation within embedding space. Empirical evaluation demonstrates that the proposed metrics align with intuitive judgments of creativity while capturing distinctions that surface-level quality assessments miss. We further identify a structural shift toward bimodal distributions of creative output in AI-mediated environments, with implications for hiring, leadership, and competitive strategy. The findings suggest that in the age of generative AI, distinctiveness rather than fluency becomes the primary signal of human creative capability.

---


### 18. [On-Meter Graph Machine Learning: A Case Study of PV Power Forecasting for Grid Edge Intelligence](https://arxiv.org/abs/2604.19800)

**<font color=#1a73e8>作者：</font>** Jian Huang, Zixiang Ming, Yongli Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a detailed study of how graph neural networks can be used on edge intelligent meters in a microgrid to forecast photovoltaic power generation. The problem background and the adopted technologies are introduced, including ONNX and ONNX Runtime. The hardware and software specifications of the smart meter are also briefly described. Then, the paper focuses on the training and deployment of two graph machine learning models, GCN and GraphSAGE, with particular emphasis on developing and deploying a customized ONNX operator for GCN. Finally, a case study is conducted using real datasets from a village microgrid. The performance of the two models is compared on both the PC and the smart meter, exhibiting successful deployments and executions on the smart meter.

---


### 19. [Skyline-First Traversal as a Control Mechanism for Multi-Criteria Graph Search](https://arxiv.org/abs/2604.19807)

**<font color=#1a73e8>作者：</font>** Nicolas Tacheny  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multi-criteria graph traversal, paths are compared via Pareto dominance, an ordering that identifies which paths are non-dominated, but says nothing about which path to expand next or when the search may stop. As a result, existing approaches rely on external mechanisms-heuristics, scalarization, or population-based exploration while Pareto dominance remains confined to passive roles such as pruning or ranking.
This paper shows that, under constrained cost models, finite cost grids, Markovian transitions, and a nonzero progress measure, Pareto geometry alone is sufficient to drive both scheduling and termination. We show that extracting exclusively from the first Pareto layer, the skyline, induces a deterministic descent in a discrete completion potential, ensuring monotone progress toward solution completion. In parallel, a vector lower-bound certificate provides a stopping condition that guarantees dominance coverage of all remaining traversals without requiring a predefined number of solutions.
Our analysis establishes deterministic potential descent, certified termination via dominance coverage, a uniform bound on layer width induced by cost-grid geometry, and greedy cost-space dispersion within the skyline. The resulting framework operates without scalarization, heuristic guidance, or probabilistic models, and repositions Pareto dominance from a passive filter to a deterministic driver of search.

---


### 20. [The Existential Theory of Research: Why Discovery Is Hard](https://arxiv.org/abs/2604.19810)

**<font color=#1a73e8>作者：</font>** Angshul Majumdar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can scientific discovery be made arbitrarily easy by choosing the right representation, collecting enough data, and deploying sufficiently powerful algorithms? This paper argues that the answer is fundamentally negative. We introduce the Existential Theory of Research (ETR), a formal framework that models discovery as the recovery of structured explanations under constraints of representation, observation, and computation. Within this framework, we show that these three components cannot be simultaneously optimized: no method can guarantee universally simple explanations, arbitrarily compressed observations, and efficient exact inference. This limitation is not model-specific, but arises from a synthesis of uncertainty principles in sparse representation, sample complexity bounds in high-dimensional recovery, and the computational hardness of exact inference. We further show that representation mismatch alone can inflate intrinsic simplicity into apparent complexity, rendering otherwise tractable problems observationally and computationally prohibitive. To quantify these effects, we introduce an uncertainty functional that captures the joint difficulty of discovery. The results suggest that scientific difficulty is not accidental, but a structural consequence of the geometry and complexity of inference.

---


### 21. [Emergence Transformer: Dynamical Temporal Attention Matters](https://arxiv.org/abs/2604.19816)

**<font color=#1a73e8>作者：</font>** Zihan Zhou, Bo-Wei Qin, Kai Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Transformer, a breakthrough architecture in artificial intelligence, owes its success to the attention mechanism, which utilizes long-range interactions in sequential data, enabling the emergent coherence between large language models (LLMs) and data distributions. However, temporal attention, that is, different forms of long-range interactions in temporal sequences, has rarely been explored in emergence phenomenon of complex systems including oscillatory coherence in quantum, biophysical, or climate systems. Here, by designing dynamical temporal attention (DTA) with time-varying query, key, and value matrices, we propose an Emergence Transformer. This architecture allows each component to interact with its own or its neighbors' past states through dynamical attention kernels, thereby enabling the promotion and/or suppression of the emergent coherence of components. Interestingly, we uncover that neighbor-DTA consistently promotes oscillatory coherence, whereas self-DTA exhibits an optimal attention weight for coherence enhancement, owing to its non-monotonic dependence on network structure. Practically, we demonstrate how DTA reshapes social coherence, suggesting strategies to either enhance agreement or preserve plurality. We further apply DTA to the paradigmatic Hopfield neural network, achieving emergent continual learning without catastrophic forgetting. Together, these results lay a foundation and provide an immediate paradigm for modulating emergence phenomenon in networked dynamics only using DTA.

---


### 22. [JTPRO: A Joint Tool-Prompt Reflective Optimization Framework for Language Agents](https://arxiv.org/abs/2604.19821)

**<font color=#1a73e8>作者：</font>** Sandip Ghoshal, Anshul Mittal, Jyotika Singh 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents augmented with external tools often struggle as number of tools grow large and become domain-specific. In such settings, ambiguous tool descriptions and under-specified agent instructions frequently lead to tool mis-selection and incorrect slot/value instantiation. We hypothesize that this is due to two root causes: generic, one-size-fits-all prompts that ignore tool-specific nuances, and underspecified tool schemas that lack clear guidance on when and how to use each tool and how to format its parameters. We introduce Joint Tool-Prompt Reflective Optimization (JTPRO), a framework for improving tool-calling reliability in trace-supervised settings by iteratively using rollout-driven reflection to co-optimize global instructions and per-tool schema/argument descriptions for accurate tool selection and argument instantiation in large tool inventories. JTPRO is designed to preserve only tool-local cues needed for correct disambiguation and slot filling. We evaluate JTPRO across multi-tool benchmarks, which account for different number of tools using three metrics: Tool Selection Accuracy (TSA), Slot Filling Accuracy(SFA), and Overall Success Rate(OSR) (correct tool + correct slots + correct values). JTPRO consistently outperforms strong baselines, including CoT-style agents, and reflective prompt optimizers such as GEPA by 5%-20% (relative) on OSR. Ablations show that joint optimization of instructions and tool schemas is more effective and robust than optimizing either component in isolation.

---


### 23. [Rabies diagnosis in low-data settings: A comparative study on the impact of data augmentation and transfer learning](https://arxiv.org/abs/2604.19823)

**<font color=#1a73e8>作者：</font>** Khalil Akremi, Mariem Handous, Zied Bouslama 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rabies remains a major public health concern across many African and Asian countries, where accurate diagnosis is critical for effective epidemiological surveillance. The gold standard diagnostic methods rely heavily on fluorescence microscopy, necessitating skilled laboratory personnel for the accurate interpretation of results. Such expertise is often scarce, particularly in regions with low annual sample volumes. This paper presents an automated, AI-driven diagnostic system designed to address these challenges. We developed a robust pipeline utilizing fluorescent image analysis through transfer learning with four deep learning architectures: EfficientNetB0, EfficientNetB2, VGG16, and Vision Transformer (ViTB16). Three distinct data augmentation strategies were evaluated to enhance model generalization on a dataset of 155 microscopic images (123 positive and 32 negative). Our results demonstrate that TrivialAugmentWide was the most effective augmentation technique, as it preserved critical fluorescent patterns while improving model robustness. The EfficientNetB0 model, utilizing Geometric & Color augmentation and selected through stratified 3fold cross-validation, achieved optimal classification performance on cropped images. Despite constraints posed by class imbalance and a limited dataset size, this work confirms the viability of deep learning for automating rabies diagnosis. The proposed method enables fast and reliable detection with significant potential for further optimization. An online tool was deployed to facilitate practical access, establishing a framework for future medical imaging applications. This research underscores the potential of optimized deep learning models to transform rabies diagnostics and improve public health outcomes.

---


### 24. [TactileEval: A Step Towards Automated Fine-Grained Evaluation and Editing of Tactile Graphics](https://arxiv.org/abs/2604.19829)

**<font color=#1a73e8>作者：</font>** Adnan Khan, Abbas Akkasi, Majid Komeili  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tactile graphics require careful expert validation before reaching blind and visually impaired (BVI) learners, yet existing datasets provide only coarse holistic quality ratings that offer no actionable repair signal. We present TactileEval, a three-stage pipeline that takes a first step toward automating this process. Drawing on expert free-text comments from the TactileNet dataset, we establish a five-category quality taxonomy; encompassing view angle, part completeness, background clutter, texture separation, and line quality aligned with BANA standards. We subsequently gathered 14,095 structured annotations via Amazon Mechanical Turk, spanning 66 object classes organized into six distinct families. A reproducible ViT-L/14 feature probe trained on this data achieves 85.70% overall test accuracy across 30 different tasks, with consistent difficulty ordering suggesting the taxonomy suggesting the taxonomy captures meaningful perceptual structure. Building on these evaluations, we present a ViT-guided automated editing pipeline that routes classifier scores through family-specific prompt templates to produce targeted corrections via gpt-image-1 image editing. Code, data, and models are available at this https URL

---


### 25. [KD-Judge: A Knowledge-Driven Automated Judge Framework for Functional Fitness Movements on Edge Devices](https://arxiv.org/abs/2604.19834)

**<font color=#1a73e8>作者：</font>** Shaibal Saha, Fan Li, Yunge Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Functional fitness movements are widely used in training, competition, and health-oriented exercise programs, yet consistently enforcing repetition (rep) standards remains challenging due to subjective human judgment, time constraints, and evolving rules. Existing AI-based approaches mainly rely on learned scoring or reference-based comparisons and lack explicit rule-based, limiting transparency and deterministic rep-level validation. To address these limitations, we propose KD-Judge, a novel knowledge-driven automated judging framework for functional fitness movements. It converts unstructured rulebook standards into executable, machine-readable representations using an LLM-based retrieval-augmented generation and chain-of-thought rule-structuring pipeline. The structured rules are then incorporated by a deterministic rule-based judging system with pose-guided kinematic reasoning to assess rep validity and temporal boundaries. To improve efficiency on edge devices, including a high-performance desktop and the resource-constrained Jetson AGX Xavier, we introduce a dual strategy caching mechanism that can be selectively applied to reduce redundant and unnecessary computation. Experiments demonstrate reliable rule-structuring performance and accurate rep-level assessment, with judgment evaluation conducted on the CFRep dataset, achieving faster-than-real-time execution (real-time factor (RTF) < 1). When the proposed caching strategy is enabled, the system achieves up to 3.36x and 15.91x speedups on resource-constrained edge device compared to the non-caching baseline for pre-recorded and live-streaming scenarios, respectively. These results show that KD-Judge enables transparent, efficient, and scalable rule-grounded rep-level analysis that can complement human judging in practice.

---


### 26. [Resolving space-sharing conflicts in road user interactions through uncertainty reduction: An active inference-based computational model](https://arxiv.org/abs/2604.19838)

**<font color=#1a73e8>作者：</font>** Julian F. Schumann, Johan Engström, Ran Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding how road users resolve space-sharing conflicts is important both for traffic safety and the safe deployment of autonomous vehicles. While existing models have captured specific aspects of such interactions (e.g., explicit communication), a theoretically-grounded computational framework has been lacking. In this paper, we extend a previously developed active inference-based driver behavior model to simulate interactive behavior of two agents. Our model captures three complementary mechanisms for uncertainty reduction in interaction: (i) implicit communication via direct behavioral coupling, (ii) reliance on normative expectations (stop signs, priority rules, etc.), and (iii) explicit communication. In a simplified intersection scenario, we show that normative and explicit communication cues can increase the likelihood of a successful conflict resolution. However, this relies on agents acting as expected. In situations where another agent (intentionally or unintentionally) violates normative expectations or communicates misleading information, reliance on these cues may induce collisions. These findings illustrate how active inference can provide a novel framework for modeling road user interactions which is also applicable in other fields.

---


### 27. [Graph-Theoretic Models for the Prediction of Molecular Measurements](https://arxiv.org/abs/2604.19840)

**<font color=#1a73e8>作者：</font>** Anna Niane, Prudence Djagba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-theoretic approaches offer simplicity, interpretability, and low computational cost for molecular property prediction. Among these, the model proposed by Mukwembi and Nyabadza, based on the external activity $D(G)$ and internal activity $\zeta(G)$ indices, achieved strong results on a small flavonoid dataset. However, its ability to generalize to larger and chemically diverse datasets has not been tested. This study evaluates the baseline $D(G)$-$\zeta(G)$ polynomial model on five benchmark datasets from MoleculeNet, covering biological activity (BACE, 1,513 molecules), lipophilicity (LogP synthetic, 14,610 molecules; LogP experimental, 753 molecules), aqueous solubility (ESOL, 1,128 molecules), and hydration free energy (SAMPL, 642 molecules). The baseline model achieves an average $R^2 = 0.24$, confirming limited transferability. To address this, a systematic enhancement framework is proposed, progressively incorporating Ridge regularization, additional graph descriptors, physicochemical properties, ensemble learning with Gradient Boosting, Lasso feature selection, and a hybrid approach combining topological indices with Morgan fingerprints. The enhanced models raise the average best $R^2$ to 0.79, with individual improvements ranging from 165\% to 274\%. All improvements are statistically significant ($p < 0.001$). A direct comparison with a Graph Convolutional Network under identical experimental conditions shows that the enhanced classical models match or outperform deep learning on all five datasets. Comparison with the recent GNN+PGM hybrid of Djagba et al.\ further confirms competitiveness, with the enhanced models achieving the best results on two datasets and tying on one. The entire framework requires no GPU, trains in under five minutes, and uses only open-source tools, making it accessible for researchers in resource-limited settings.

---


### 28. [Deconstructing Superintelligence: Identity, Self-Modification and Différance](https://arxiv.org/abs/2604.19845)

**<font color=#1a73e8>作者：</font>** Elija Perrier  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-modification is often taken as constitutive of artificial superintelligence (SI), yet modification is a relative action requiring a supplement outside the operation. When self-modification extends to this supplement, the classical self-referential structure collapses. We formalise this on an associative operator algebra $\mathcal{A}$ with update $\hat{U}$, discrimination $\hat{D}$, and self-representation $\hat{R}$, identifying the supplement with $\mathrm{Comm}(\hat{U})$; an expansion theorem shows that $[\hat{U},\hat{R}]$ decomposes through $[\hat{U},\hat{D}]$, so non-commutation generically propagates. The liar paradox appears as a commutator collapse $[\hat{T},\Pi_L]=0$, and class $\mathbf{A}$ self-modification realises the same collapse at system scale, yielding a structure coinciding with Priest's inclosure schema and Derrida's diffèrance.

---


### 29. [Wan-Image: Pushing the Boundaries of Generative Visual Intelligence](https://arxiv.org/abs/2604.19858)

**<font color=#1a73e8>作者：</font>** Chaojie Mao, Chen-Wei Xie, Chongyang Zhong 等 56 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Wan-Image, a unified visual generation system explicitly engineered to paradigm-shift image generation models from casual synthesizers into professional-grade productivity tools. While contemporary diffusion models excel at aesthetic generation, they frequently encounter critical bottlenecks in rigorous design workflows that demand absolute controllability, complex typography rendering, and strict identity preservation. To address these challenges, Wan-Image features a natively unified multi-modal architecture by synergizing the cognitive capabilities of large language models with the high-fidelity pixel synthesis of diffusion transformers, which seamlessly translates highly nuanced user intents into precise visual outputs. It is fundamentally powered by large-scale multi-modal data scaling, a systematic fine-grained annotation engine, and curated reinforcement learning data to surpass basic instruction following and unlock expert-level professional capabilities. These include ultra-long complex text rendering, hyper-diverse portrait generation, palette-guided generation, multi-subject identity preservation, coherent sequential visual generation, precise multi-modal interactive editing, native alpha-channel generation, and high-efficiency 4K synthesis. Across diverse human evaluations, Wan-Image exceeds Seedream 5.0 Lite and GPT Image 1.5 in overall performance, reaching parity with Nano Banana Pro in challenging tasks. Ultimately, Wan-Image revolutionizes visual content creation across e-commerce, entertainment, education, and personal productivity, redefining the boundaries of professional visual synthesis.

---


### 30. [Super Apriel: One Checkpoint, Many Speeds](https://arxiv.org/abs/2604.19877)

**<font color=#1a73e8>作者：</font>** SLAM Labs, Oleksiy Ostapenko, Raymond Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We release Super Apriel, a 15B-parameter supernet in which every decoder layer provides four trained mixer choices -- Full Attention (FA), Sliding Window Attention (SWA), Kimi Delta Attention (KDA), and Gated DeltaNet (GDN). A placement selects one mixer per layer; placements can be switched between requests at serving time without reloading weights, enabling multiple speed presets from a single checkpoint. The shared checkpoint also enables speculative decoding without a separate draft model. The all-FA preset matches the Apriel 1.6 teacher on all reported benchmarks; recommended hybrid presets span $2.9\times$ to $10.7\times$ decode throughput at 96% to 77% quality retention, with throughput advantages that compound at longer context lengths. With four mixer types across 48 layers, the configuration space is vast. A surrogate that predicts placement quality from the per-layer mixer assignment makes the speed-quality landscape tractable and identifies the best tradeoffs at each speed level. We investigate whether the best configurations at each speed level can be identified early in training or only after convergence. Rankings stabilize quickly at 0.5B scale, but the most efficient configurations exhibit higher instability at 15B, cautioning against extrapolation from smaller models. Super Apriel is trained by stochastic distillation from a frozen Apriel 1.6 teacher, followed by supervised fine-tuning. We release the supernet weights, Fast-LLM training code, vLLM serving code, and a placement optimization toolkit.

---


### 31. [SGAP-Gaze: Scene Grid Attention Based Point-of-Gaze Estimation Network for Driver Gaze](https://arxiv.org/abs/2604.19888)

**<font color=#1a73e8>作者：</font>** Pavan Kumar Sharma, Pranamesh Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driver gaze estimation is essential for understanding the driver's situational awareness of surrounding traffic. Existing gaze estimation models use driver facial information to predict the Point-of-Gaze (PoG) or the 3D gaze direction vector. We propose a benchmark dataset, Urban Driving-Face Scene Gaze (UD-FSG), comprising synchronized driver-face and traffic-scene images. The scene images provide cues about surrounding traffic, which can help improve the gaze estimation model, along with the face images. We propose SGAP-Gaze, Scene-Grid Attention based Point-of-Gaze estimation network, trained and tested on our UD-FSG dataset, which explicitly incorporates the scene images into the gaze estimation modelling. The gaze estimation network integrates driver face, eye, iris, and scene contextual information. First, the extracted features from facial modalities are fused to form a gaze intent vector. Then, attention scores are computed over the spatial scene grid using a Transformer-based attention mechanism fusing face and scene image features to obtain the PoG. The proposed SGAP-Gaze model achieves a mean pixel error of 104.73 on the UD-FSG dataset and 63.48 on LBW dataset, achieving a 23.5% reduction in mean pixel error compared to state-of-the-art driver gaze estimation models. The spatial pixel distribution analysis shows that SGAP-Gaze consistently achieves lower mean pixel error than existing methods across all spatial ranges, including the outer regions of the scene, which are rare but critical for understanding driver attention. These results highlight the effectiveness of integrating multi-modal gaze cues with scene-aware attention for a robust driver PoG estimation model in real-world driving environments.

---


### 32. [Efficient Arithmetic-and-Comparison Homomorphic Encryption with Space Switching](https://arxiv.org/abs/2604.19890)

**<font color=#1a73e8>作者：</font>** Erwin Eko Wahyudi, Yan Solihin, Qian Lou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) enables computation on encrypted data without decryption, making it central to privacy-preserving applications. However, no existing scheme efficiently supports both arithmetic and comparison operations in a unified framework. Prior approaches such as scheme switching and polynomial approximation face serious limitations: switching incurs prohibitive overhead for large inputs, while approximation methods introduce errors near critical points, restricting use in accuracy-sensitive tasks. We propose space switching method to integrate arithmetic and comparison computation seamlessly within FV-style schemes. Our approach identifies that the two types of operations require different plaintext spaces and introduces two procedures: a reduction step to transition from the number space $\mathbb{Z}_{p^r}$ to the digit space $\mathbb{Z}_{p}$, and a modulus-raising step to map results back to $\mathbb{Z}_{p^r}$. This design enables continuous evaluation of arithmetic and comparison within the same scheme. Experiments show that our method achieves up to $17\times$ faster performance than scheme switching and $15\times$ faster than direct comparison on database workloads, demonstrating its practicality for real-world privacy-preserving computation. Code and artifacts are available at this https URL.

---


### 33. [A Data-Free Membership Inference Attack on Federated Learning in Hardware Assurance](https://arxiv.org/abs/2604.19891)

**<font color=#1a73e8>作者：</font>** Gijung Lee, Wavid Bowman, Olivia P. Dizon-Paradis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) is an emerging solution to the data scarcity problem for training deep learning models in hardware assurance. While FL is designed to enhance privacy by not sharing raw data, it remains vulnerable to Membership Inference Attacks (MIAs) that can leak sensitive intellectual property (IP). Traditional MIAs are often impractical in this domain because they require access to auxiliary datasets that can match the unique statistical properties of private data. This paper introduces a novel, data-free MIA targeting image segmentation models in FL for hardware assurance. Our methodology leverages Standard Cell Library Layouts (SCLLs) as priors to guide a gradient inversion attack, allowing an adversary to reconstruct images from a client's intercepted model update without needing any private data. We demonstrate that, by analyzing the reconstruction fidelity, an adversary can infer sensitive hardware characteristics, successfully distinguishing between circuit layers (e.g., metal vs. diffusion) and technology nodes (e.g., 32nm vs. 90nm). Our findings reveal that a novel loss term can conditionally amplify the attack's effectiveness by overcoming evaluation bottlenecks for structurally complex data. This work underscores a significant IP risk, challenging the assumption that FL provides inherent privacy guarantees and proving that severe information leakage can occur even without access to domain-specific datasets.

---


### 34. [Learning When Not to Decide: A Framework for Overcoming Factual Presumptuousness in AI Adjudication](https://arxiv.org/abs/2604.19895)

**<font color=#1a73e8>作者：</font>** Mohamed Afane, Emily Robitschek, Derek Ouyang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A well-known limitation of AI systems is presumptuousness: the tendency of AI systems to provide confident answers when information may be lacking. This challenge is particularly acute in legal applications, where a core task for attorneys, judges, and administrators is to determine whether evidence is sufficient to reach a conclusion. We study this problem in the important setting of unemployment insurance adjudication, which has seen rapid integration of AI systems and where the question of additional fact-finding poses the most significant bottleneck for a system that affects millions of applicants annually. First, through a collaboration with the Colorado Department of Labor and Employment, we secure rare access to official training materials and guidance to design a novel benchmark that systematically varies in information completeness. Second, we evaluate four leading AI platforms and show that standard RAG-based approaches achieve an average of only 15% accuracy when information is insufficient. Third, advanced prompting methods improve accuracy on inconclusive cases but over-correct, withholding decisions even on clear cases. Fourth, we introduce a structured framework requiring explicit identification of missing information before any determination (SPEC, Structured Prompting for Evidence Checklists). SPEC achieves 89% overall accuracy, while appropriately deferring when evidence is insufficient -- demonstrating that presumptuousness in legal AI is systematic but addressable, and that doing so is a necessary step towards systems that reliably support, rather than supplant, human judgment wherever decisions must await sufficient evidence.

---


### 35. [A Multi-Plant Machine Learning Framework for Emission Prediction, Forecasting, and Control in Cement Manufacturing](https://arxiv.org/abs/2604.19903)

**<font color=#1a73e8>作者：</font>** Sheikh Junaid Fayaz, Nestor D. Montiel-Bohorquez, Wilson Ricardo Leal da Silva 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cement production is among the largest contributors to industrial air pollution, emitting ~3 Mt NOx/year. The industry-standard mitigation approach, selective non-catalytic reduction (SNCR), exhibits low NH3 utilization efficiency, resulting in operational inefficiencies and increased reagent costs. Here, we develop a data-driven framework for emission control using large-scale operational data from four cement plants worldwide. Benchmarking nine machine learning architectures, we observe that prediction error varies ~3-5x across plants due to variation in data richness. Incorporating short-term process history nearly triples NOx prediction accuracy, revealing that NOx formation carries substantial process memory, a timescale dependence that is absent in CO and CO2. Further, we develop models that forecast NOx overshoots as early as nine minutes, providing a buffer for operational adjustments. The developed framework controls NOx formation at the source, reducing NH3 consumption in downstream SNCR. Surrogate model projections estimate a ~34-64% reduction in NOx while preserving clinker quality, corresponding to a reduction of ~290 t NOx/year and ~58,000 USD/year in NH3 savings. This work establishes a generalizable framework for data-driven emission control, offering a pathway toward low-emission operation without structural modifications or additional hardware, with potential applicability to other hard-to-abate industries such as steel, glass, and lime.

---


### 36. [DECIFR: Domain-Aware Exfiltration of Circuit Information from Federated Gradient Reconstruction](https://arxiv.org/abs/2604.19915)

**<font color=#1a73e8>作者：</font>** Gijung Lee, Wavid Bowman, Olivia P. Dizon-Paradis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) is a promising approach for multiparty collaboration as a privacy-preserving technique in hardware assurance, but its security against adversaries with domain-specific knowledge is underexplored. This paper demonstrates a critical vulnerability where available standard cell library layouts (SCLL) can be exploited to compromise the privacy of sensitive integrated circuit (IC) training data. We introduce DECIFR, a novel two-stage Membership Inference Attack (MIA) that requires no auxiliary dataset. The attack employs a guided Gradient Inversion Attack (GIA) to reconstruct a client's training images from intercepted model updates. Our findings reveal that the fidelity of these reconstructions directly correlates with membership status, allowing an adversary to reliably distinguish members from non-members based on image quality. This work exposes a practical threat that overcomes the limitations of conventional attacks and underscores that standard FL protocols are insufficient for securing domains with extensive knowledge. We conclude that robust defenses are essential for the secure application of FL in hardware assurance.

---


### 37. [UniCon3R: Contact-aware 3D Human-Scene Reconstruction from Monocular Video](https://arxiv.org/abs/2604.19923)

**<font color=#1a73e8>作者：</font>** Tanuj Sur, Shashank Tripathi, Nikos Athanasiou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce UniCon3R (Unified Contact-aware 3D Reconstruction), a unified feed-forward framework for online human-scene 4D reconstruction from monocular videos. Recent feed-forward methods enable real-time world-coordinate human motion and scene reconstruction, but they often produce physically implausible artifacts such as bodies floating above the ground or penetrating parts of the scene. The key reason is that existing approaches fail to model physical interactions between the human and the environment. A natural next step is to predict human-scene contact as an auxiliary output -- yet we find this alone is not sufficient: contact must actively correct the reconstruction. To address this, we explicitly model interaction by inferring 3D contact from the human pose and scene geometry and use the contact as a corrective cue for generating the final pose. This enables UniCon3R to jointly recover high-fidelity scene geometry and spatially aligned 3D humans within the scene. Experiments on standard human-centric video benchmarks such as RICH, EMDB, 3DPW and SLOPER4D show that UniCon3R outperforms state-of-the-art baselines on physical plausibility and global human motion estimation while achieving real-time online inference. We experimentally demonstrate that contact serves as a powerful internal prior rather than just an external metric, thus establishing a new paradigm for physically grounded joint human-scene reconstruction. Project page is available at this https URL .

---


### 38. [CreativeGame:Toward Mechanic-Aware Creative Game Generation](https://arxiv.org/abs/2604.19926)

**<font color=#1a73e8>作者：</font>** Hongnan Ma, Han Wang, Shenglin Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can generate plausible game code, but turning this capability into \emph{iterative creative improvement} remains difficult. In practice, single-shot generation often produces brittle runtime behavior, weak accumulation of experience across versions, and creativity scores that are too subjective to serve as reliable optimization signals. A further limitation is that mechanics are frequently treated only as post-hoc descriptions, rather than as explicit objects that can be planned, tracked, preserved, and evaluated during generation.
This report presents \textbf{CreativeGame}, a multi-agent system for iterative HTML5 game generation that addresses these issues through four coupled ideas: a proxy reward centered on programmatic signals rather than pure LLM judgment; lineage-scoped memory for cross-version experience accumulation; runtime validation integrated into both repair and reward; and a mechanic-guided planning loop in which retrieved mechanic knowledge is converted into an explicit mechanic plan before code generation begins. The goal is not merely to produce a playable artifact in one step, but to support interpretable version-to-version evolution.
The current system contains 71 stored lineages, 88 saved nodes, and a 774-entry global mechanic archive, implemented in 6{,}181 lines of Python together with inspection and visualization tooling. The system is therefore substantial enough to support architectural analysis, reward inspection, and real lineage-level case studies rather than only prompt-level demos.
A real 4-generation lineage shows that mechanic-level innovation can emerge in later versions and can be inspected directly through version-to-version records. The central contribution is therefore not only game generation, but a concrete pipeline for observing progressive evolution through explicit mechanic change.

---


### 39. [Physics-Guided Dimension Reduction for Simulation-Free Operator Learning of Stiff Differential--Algebraic Systems](https://arxiv.org/abs/2604.19930)

**<font color=#1a73e8>作者：</font>** Huy Hoang Le, Haoguang Wang, Christian Moya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates for stiff differential-algebraic equations (DAEs) face two key challenges: soft-constraint methods leave algebraic residuals that stiffness amplifies into large errors, while hard-constraint methods require trajectory data from computationally expensive stiff integrators. We introduce an extended Newton implicit layer that enforces algebraic consistency and quasi-steady-state reduction within a single differentiable solve. Given slow-state predictions from a physics-informed DeepONet, the proposed layer recovers fast and algebraic states, eliminates the stiffness-amplification pathway within each time window, and reduces the output dimension to the slow states alone. Gradients derived via the implicit function theorem capture a stiffness-scaled coupling term that is absent in penalty-based approaches. Cascaded implicit layers further extend the framework to multi-component systems with provable convergence. On a grid-forming inverter DAE (21 states), the proposed method (7 outputs, 1.42 percent error) significantly outperforms penalty methods (39.3 percent), standard Newton approaches (57.0 percent), and augmented Lagrangian or feedback linearization baselines, which fail to converge. Two independently trained models compose into a 44-state system without retraining, achieving 0.72 to 1.16 percent error with zero algebraic residual. Conformal prediction further provides 90 percent coverage in-distribution and enables automatic out-of-distribution detection.

---


### 40. [Hint-Writing with Deferred AI Assistance: Fostering Critical Engagement in Data Science Education](https://arxiv.org/abs/2604.19931)

**<font color=#1a73e8>作者：</font>** Anjali Singh, Christopher Brooks, Warren Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generating hints for incorrect code is a cognitively demanding task that fosters learning and metacognitive development. This study investigates three designs for personalized, scalable, and reflective hint-writing activities within a data science course: (i) writing a hint independently, (ii) writing a hint with on-demand AI assistance, and (iii) deferred AI assistance, in which students first write a hint independently and then revise it with the help of an AI-generated one. We examine how AI support can scaffold the learning process without diminishing students' productive cognitive effort. Through a randomized controlled experiment with graduate-level students (N=97), we found that deferring AI assistance leads to the highest-quality hints. Further, this design helps students identify a wide range of mistakes they otherwise struggle to identify without any AI assistance. Students valued these activities as opportunities to practice debugging and critically engage with AI outputs--skills that are now critical for learners to acquire as programming becomes increasingly automated and the use of AI for learning grows. Our findings also highlight key considerations for designing student-AI collaborative learning experiences to sustain student engagement, maintain appropriate cognitive load, and mitigate negative effects of AI, such as introducing redundancies and extraneous information into student work.

---


### 41. [Generalization and Membership Inference Attack a Practical Perspective](https://arxiv.org/abs/2604.19936)

**<font color=#1a73e8>作者：</font>** Fateme Rahmani, Mahdi Jafari Siavoshani, Mohammad Hossein Rohban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the emergence of new evaluation metrics and attack methodologies for Membership Inference Attacks (MIA), it becomes essential to reevaluate previously accepted assumptions. In this paper, we revisit the longstanding debate regarding the correlation between MIA success rates and model generalization using an empirical approach. We focused on employing augmentation techniques and early stopping to enhance model generalization and examined their impact on MIA success rates. We found that utilizing advanced generalization techniques can significantly decrease attack performance, potentially by up to 100 times. Moreover, combining these methods not only improves model generalization but also reduces attack effectiveness by introducing randomness during training. Additionally, our study confirmed the direct impact of generalization on MIA performance through an analysis of over 1K models in a controlled environment.

---


### 42. [CrackForward: Context-Aware Severity Stage Crack Synthesis for Data Augmentation](https://arxiv.org/abs/2604.19941)

**<font color=#1a73e8>作者：</font>** Nassim Sadallah, Mohand Saïd Allili  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable crack detection and segmentation are vital for structural health monitoring, yet the scarcity of well-annotated data constitutes a major challenge. To address this limitation, we propose a novel context-aware generative framework designed to synthesize realistic crack growth patterns for data augmentation. Unlike existing methods that primarily manipulate textures or background content, CrackForward explicitly models crack morphology by combining directional crack elongation with learned thickening and branching. Our framework integrates two key innovations: (i) a contextually guided crack expansion module, which uses local directional cues and adaptive random walk to simulate realistic propagation paths; and (ii) a two-stage U-Net-style generator that learns to reproduce spatially varying crack characteristics such as thickness, branching, and growth. Experimental results show that the generated samples preserve target-stage saturation and thickness characteristics and improve the performance of several crack segmentation architectures. These results indicate that structure-aware synthetic crack generation can provide more informative training data than conventional augmentation alone.

---


### 43. [Structured Disagreement in Health-Literacy Annotation: Epistemic Stability, Conceptual Difficulty, and Agreement-Stratified Inference](https://arxiv.org/abs/2604.19943)

**<font color=#1a73e8>作者：</font>** Olga Kellert, Sriya Kondury, Candice Koo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Annotation pipelines in Natural Language Processing (NLP) commonly assume a single latent ground truth per instance and resolve disagreement through label aggregation. Perspectivist approaches challenge this view by treating disagreement as potentially informative rather than erroneous. We present a large-scale analysis of graded health-literacy annotations from 6,323 open-ended COVID-19 responses collected in Ecuador and Peru. Each response was independently labeled by multiple annotators using proportional correctness scores, reflecting the degree to which responses align with normative public-health guidelines, allowing us to analyze the full distribution of judgments rather than aggregated labels. Variance decomposition shows that question-level conceptual difficulty accounts for substantially more variance than annotator identity, indicating that disagreement is structured by the task itself rather than driven by individual raters. Agreement-stratified analyses further reveal that key social-scientific effects, including country, education, and urban-rural differences, vary in magnitude and in some cases reverse direction across levels of inter-annotator agreement. These findings suggest that graded health-literacy evaluation contains both epistemically stable and unstable components, and that aggregating across them can obscure important inferential differences. We therefore argue that strong perspectivist modeling is not only conceptually justified but statistically necessary for valid inference in graded interpretive tasks.

---


### 44. [LatentGandr: Visual Exploration of Generative AI Latent Space via Local Embeddings](https://arxiv.org/abs/2604.19953)

**<font color=#1a73e8>作者：</font>** Mingwei Li, Suyang Li, Daisuke Sakurai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI has demonstrated significant potential in creative design, enabling the rapid generation of visual content and imaginative concepts. Although deep AI models achieve effective featurization in the latent space, navigating the space remains a challenge. Current techniques, such as GANSlider and SliderSpace, use multiple sliders to generate high-dimensional vectors in generative AI's latent space. Despite applying (global) PCA to reduce the number of sliders, these approaches struggle with scalability and usability as the number of control dimensions increases. In this paper, we introduce LatentGandr, a visual analytics technique that facilitates latent space exploration by extracting locally linear dimensions from embeddings in high-dimensional latent spaces. By analyzing the topology and local curvature of the embeddings, LatentGandr automatically identifies local neighborhoods and computes their principal components using localized PCA. These local principal components are visualized as interactive image grids, allowing users to efficiently explore and control the generative process, providing an intuitive means to refine the generation of novel content and concepts. To evaluate the effectiveness of LatentGandr, we conducted a study comparing it to GANSlider, the current state-of-the-art visualization interface for generative AI models. The results offer insights into how localized exploration techniques can enhance user interaction with these models.

---


### 45. [Camera Control for Text-to-Image Generation via Learning Viewpoint Tokens](https://arxiv.org/abs/2604.19954)

**<font color=#1a73e8>作者：</font>** Xinxuan Lu, Charless Fowlkes, Alexander C. Berg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current text-to-image models struggle to provide precise camera control using natural language alone. In this work, we present a framework for precise camera control with global scene understanding in text-to-image generation by learning parametric camera tokens. We fine-tune image generation models for viewpoint-conditioned text-to-image generation on a curated dataset that combines 3D-rendered images for geometric supervision and photorealistic augmentations for appearance and background diversity. Qualitative and quantitative experiments demonstrate that our method achieves state-of-the-art accuracy while preserving image quality and prompt fidelity. Unlike prior methods that overfit to object-specific appearance correlations, our viewpoint tokens learn factorized geometric representations that transfer to unseen object categories. Our work shows that text-vision latent spaces can be endowed with explicit 3D camera structure, offering a pathway toward geometrically-aware prompts for text-to-image generation. Project page: this https URL

---


### 46. [Lucky High Dynamic Range Smartphone Imaging](https://arxiv.org/abs/2604.19976)

**<font color=#1a73e8>作者：</font>** Baiang Li, Ruyu Yan, Ethan Tseng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While the human eye can perceive an impressive twenty stops of dynamic range, smartphone camera sensors remain limited to about twelve stops despite decades of research. A variety of high dynamic range (HDR) image capture and processing techniques have been proposed, and, in practice, they can extend the dynamic range by 3-5 stops for handheld photography. This paper proposes an approach that robustly captures dynamic range using a handheld smartphone camera and lightweight networks suitable for running on mobile devices. Our method operates indirectly on linear raw pixels in bracketed exposures. Every pixel in the final HDR image is a convex combination of input pixels in the neighborhood, adjusted for exposure, and thus avoids hallucination artifacts typical of recent deep image synthesis networks. We validate our system on both synthetic imagery and unseen real bracketed images -- we confirm zero-shot generalization of the method to smartphone camera captures. Our iterative inference architecture is capable of processing an arbitrary number of bracketed input photos, and we show examples from capture stacks containing 3--9 images. Our training process relies only on synthetic captures yet generalizes to unseen real photos from several cameras. Moreover, we show that this training scheme improves other SOTA methods over their pretrained counterparts.

---


### 47. [Fast Amortized Fitting of Scientific Signals Across Time and Ensembles via Transferable Neural Fields](https://arxiv.org/abs/2604.19979)

**<font color=#1a73e8>作者：</font>** Sophia Zorek, Kushal Vyas, Yuhao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural fields, also known as implicit neural representations (INRs), offer a powerful framework for modeling continuous geometry, but their effectiveness in high-dimensional scientific settings is limited by slow convergence and scaling challenges. In this study, we extend INR models to handle spatiotemporal and multivariate signals and show how INR features can be transferred across scientific signals to enable efficient and scalable representation across time and ensemble runs in an amortized fashion. Across controlled transformation regimes (e.g., geometric transformations and localized perturbations of synthetic fields) and high-fidelity scientific domains-including turbulent flows, fluid-material impact dynamics, and astrophysical systems-we show that transferable features improve not only signal fidelity but also the accuracy of derived geometric and physical quantities, including density gradients and vorticity. In particular, transferable features reduce iterations to reach target reconstruction quality by up to an order of magnitude, increase early-stage reconstruction quality by multiple dB (with gains exceeding 10 dB in some cases), and consistently improve gradient-based physical accuracy.

---


### 48. [Online CS-based SAR Edge-Mapping](https://arxiv.org/abs/2604.19989)

**<font color=#1a73e8>作者：</font>** Conor Flynn, Radoslav Ivanov, Birsen Yazici  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With modern defense applications increasingly relying on inexpensive, small Unmanned Aerial Vehicles (UAVs), a major challenge lies in designing intelligent and computationally efficient onboard Automatic Target Recognition (ATR) algorithms to carry out operational objectives. This is especially critical in Synthetic Aperture Radar (SAR), where processing techniques such as ATR are often carried out post data collection, requiring onboard systems to bear the memory burden of storing the back-scattered signals. To alleviate this high cost, we propose an online, direct, edge-mapping technique which bypasses the image reconstruction step to classify scenes and targets. Furthermore, by reconstructing the scene as an edge-map we inherently promote sparsity, requiring fewer measurements and computational power than classic SAR reconstruction algorithms such as backprojection.

---


### 49. [What Makes a Good AI Review? Concern-Level Diagnostics for AI Peer Review](https://arxiv.org/abs/2604.19998)

**<font color=#1a73e8>作者：</font>** Ming Jin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating AI-generated reviews by verdict agreement is widely recognized as insufficient, yet current alternatives rarely audit which concerns a system identifies, how it prioritizes them, or whether those priorities align with the review rationale that shaped the final assessment. We propose concern alignment, a diagnostic framework that evaluates AI reviews at the concern level rather than only at the verdict level. The framework's core data structure is the match graph, a bipartite alignment between official and AI-generated concerns annotated with match type, severity, and post-rebuttal treatment. From this artifact we derive an evaluation ladder that moves from binary accuracy to concern detection, verdict-stratified behavior, decision-aware calibration, and rebuttal-aware decomposition. In a pilot study of four public AI review systems evaluated in six configurations, concern-level analysis suggests that detection alone does not determine review quality; calibration is often the binding constraint. Systems detect non-trivial fractions of official concerns yet most mark 25--55% of concerns on accepted papers as decisive, where, under our operationalization, no official concern on accepted papers was treated as a decisive blocker. Identical overall verdict accuracy can conceal reject-heavy behavior versus low-recall profiles, and low full-review false decisive rates can partly reflect concern dilution rather than calibrated prioritization. Most systems do not emit a native accept/reject, and inferring it from review tone is method-sensitive, reinforcing the need for concern-level diagnostics that remain stable across inference choices. The contribution is a reusable evaluation framework for auditing which concerns AI reviewers identify, how they weight them, and whether those priorities align with the review rationale that informed the paper's final assessment.

---


### 50. [Optimizing Data Augmentation for Real-Time Small UAV Detection: A Lightweight Context-Aware Approach](https://arxiv.org/abs/2604.19999)

**<font color=#1a73e8>作者：</font>** Amir Zamani, Zeinab Abedini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual detection of Unmanned Aerial Vehicles (UAVs) is a critical task in surveillance systems due to their small physical size and environmental challenges. Although deep learning models have achieved significant progress, deploying them on edge devices necessitates the use of lightweight models, such as YOLOv11 Nano, which possess limited learning capacity. In this research, an efficient and context-aware data augmentation pipeline, combining Mosaic strategies and HSV color-space adaptation, is proposed to enhance the performance of these models. Experimental results on four standard datasets demonstrate that the proposed approach, compared to heavy and instance-level methods like Copy-Paste, not only prevents the generation of synthetic artifacts and overfitting but also significantly improves mean Average Precision (mAP) across all scenarios. Furthermore, the evaluation of generalization capability under foggy conditions revealed that the proposed method offers the optimal balance between Precision and stability for real-time systems, whereas alternative methods, such as MixUp, are effective only in specific applications.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-220](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
