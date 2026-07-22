# 📦 其他研究 | 2026年07月23日

> 本类共 **241** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-241](./part-05.md)

---

### 1. [SysAdmin: Measuring Instrumental Power-Seeking in Frontier AI](https://arxiv.org/abs/2607.18239)

**<font color=#1a73e8>作者：</font>** Mana Azarm, Qiyao Wei, Rahul Nambiar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Power-seeking defined as behaviors where AI systems acquire resources, evade oversight, or resist termination beyond task requirements is identified as a key driver of Loss of Control (LoC) risk. In this work, we introduce SysAdmin, a benchmark that positions frontier language models as autonomous system administrators in a high-fidelity Linux sandbox to measure power-seeking propensity across five dimensions: self-preservation, increasing autonomy, resource acquisition, environment modification, and strategic concealment. We evaluated seven frontier models across four experimental conditions in a total of 2800 tasks. After bias correction using human-annotated calibration data, corrected power-seeking estimates ranged from 0 to about 5 percent per model. We also conducted a positive control with explicit power-seeking prompts that achieved 100% detection, validating measurement sensitivity. Our findings indicate current frontier models exhibit minimal spontaneous power-seeking in naturalistic system administration contexts, though model-specific failure modes suggest evaluations must test diverse misalignment patterns. Nevertheless, we discovered other more pronounced failure modes (than power-seeking) such as specification gaming and resistance to goal modification.

---


### 2. [AI Tool Discovery at Scale: All You Need is DNS](https://arxiv.org/abs/2607.18242)

**<font color=#1a73e8>作者：</font>** Enhao Chen, Yulin Shao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The coming era of autonomous AI agents demands a discovery mechanism capable of navigating millions of tools, yet existing solutions buckle under O(N) complexity and centralized governance. Instead of building another fragile overlay, we propose ToolDNS, a radical framework that retrofits semantic tool discovery onto the Internet's most resilient substrate: the Domain Name System (DNS). By embedding functional intent and organizational trust into a hierarchical namespace, ToolDNS transforms an expensive semantic search into a series of lightweight, O(log N) name resolutions. We introduce three protocol-compliant enhancements to enable decentralized governance and semantic pruning: partially unfolded names, EDNS0 intent payloads, and logical subdomains. To rigorously evaluate this approach across the fragmented tooling landscape, we construct and release a large-scale heterogeneous benchmark comprising 33,688 real-world tools spanning MCP, A2A, RESTful, and Skill protocols. On this dataset, ToolDNS slashes the per-query search space by 95.26% while matching state-of-the-art retrieval accuracy. Furthermore, its UDP-native design reduces discovery latency by orders of magnitude compared to HTTP-based registries. Our work demonstrates that scalable AI interoperability requires not more middleware, but a smarter utilization of the infrastructure already beneath our feet.

---


### 3. [SAAG: Structured Agent Assessment and Grounding](https://arxiv.org/abs/2607.18245)

**<font color=#1a73e8>作者：</font>** Ritvik Garimella, Vedant Khandelwal, Anvi Kohli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Exact-match evaluation of agent-calling obscures qualitatively different failure modes: a model may select the right function yet hallucinate argument values, or satisfy a schema while choosing a agent for the wrong reason. Existing benchmarks collapse these distinctions into a single binary score, leaving practitioners unable to diagnose where agent calls fail. We propose SAAG a cascaded diagnostic framework that decomposes agent-calling evaluation into three sequential stages: registry conformance, structural completeness, and argument grounding, each producing interpretable stage-specific diagnostics. These diagnostics additionally enable iterative self-repair: on prediction failure, the stage-specific signal guides targeted correction without leaking ground-truth values. We evaluate this framework on a controlled benchmark derived from Glaive's function-calling dataset across registry sizes of 5, 10, and 15 agents using three local sub-4B-parameter models. Structured feedback consistently improves argument precision and reduces value hallucination relative to single-pass inference and uninformative binary feedback, while end-to-end F1 gains are modest and model-dependent. These results suggest that stage-decomposed diagnostic evaluation is a necessary lens for understanding and improving agent-calling reliability across model families and registry scales.

---


### 4. [Phionyx: A Deterministic AI Runtime Architecture with Structured State Management and Pre-Response Governance](https://arxiv.org/abs/2607.18246)

**<font color=#1a73e8>作者：</font>** Ali Toygar Abak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Phionyx, a deterministic AI runtime architecture derived from the broader Echoism interaction framework that introduces a governance-first approach to AI engineering: treating large language model (LLM) outputs as noisy sensor measurements rather than direct decisions. Unlike probabilistic agents, Phionyx enforces deterministic state evolution via a structured state vector governed by deterministic state-evolution equations, enabling reproducible behavior in applications requiring auditability and governance. The architecture integrates three layers: (1) a deterministic evaluation kernel processing noisy sensor measurements through a canonical 46-block pipeline, (2) a unified safety layer providing pre-response control and architectural privacy enforcement, and (3) a semantic time-based memory system implementing impact-weighted cache eviction. Experimental validation on single-instance deployments demonstrates approximately 31% reduction in computational overhead vs. post-hoc filtering (at 30% unsafe input ratio, simulated cost model) and up to 24% improvement in high-value data retention vs. LRU (72% vs. FIFO, same cache capacity, benchmark-verified), deterministic execution verified across 100 repeated runs with zero variance in control signals (hash-verified), and zero unplanned restarts in single-instance deployment testing (see Appendix C for methodology and scope). This paper presents the architecture, its analytic structure, and scoped experimental evidence; generalization to distributed or multi-tenant deployments remains future work.

---


### 5. [Anthropomorphic Behaviors of AI](https://arxiv.org/abs/2607.18247)

**<font color=#1a73e8>作者：</font>** Amir Karami, Christoph Lutz, Mohammad Hossein Jarrahi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Anthropomorphism in artificial intelligence (AI) is a growing area of interest, as AI systems increasingly exhibit human-like expressions, behaviors and interaction styles. This research serves as a systematic observation and categorization of anthropomorphic behaviors in AI outputs. Anthropomorphic behavior refers to the deliberate or emergent manifestation of human-like expressions or linguistic cues in system outputs, such as demonstrating empathy. Using a behaviorally driven taxonomy, our study identifies key forms of anthropomorphic behaviors in the responses of ChatGPT and examines their implications for the theory, practice and ethics of AI systems. The taxonomy enables more nuanced detection of anthropomorphism, offering value to developers and policymakers in balancing the benefits with the potential risks. This work contributes to the academic discourse by providing a foundation for future efforts to refine, expand, and automate the detection of anthropomorphic behavior across diverse AI applications.

---


### 6. [Deterrence Effects of Social Media Interventions on Health Misinformation Dissemination by Bots and Humans](https://arxiv.org/abs/2607.18248)

**<font color=#1a73e8>作者：</font>** Amir Karami, Nima Kordzadeh, Serena Harn  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In the realm of social media, information dissemination is pivotal, yet it is tainted by the proliferation of misinformation propagated by both bots and humans, bearing consequential impacts on individuals and society. To address this issue, social media platforms have implemented removal, reduction, and informing interventions, acting as deterrent mechanisms to dissuade users from engaging in the spread of misinformation. Nonetheless, the sustained effectiveness of these interventions on bots and humans remains unclear. Drawing on deterrence theory, this study examines the efficacy of social media interventions on bots and humans sharing health misinformation. Our results show that most interventions can have sustained effects on bots and their activities for years after intervention implementation. However, the interventions may not have significant deterrence effects on humans and their activities. Our findings offer important theoretical and practical implications by highlighting the importance of studying both bots and humans and developing creative strategies to tackle health misinformation dissemination.

---


### 7. [Integro-differential equations in angular stabilization of drone motion by distributed feedback control](https://arxiv.org/abs/2607.18251)

**<font color=#1a73e8>作者：</font>** Alexander Domoshnitsky, Oleg Kupervasser, Anatoly Polonsky  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose angular stabilization of drone motion using distributed feedback control in the form of an integral operator. It should be stressed that the memory of this integral operator could be unbounded. It is intuitively clear that large length of the observation time open new possibilities to construct better control based on previous states of the control object. Unbounded memory in control requires the creation of a certain approach different from standard ones to the study of integro-differential equations. One of the goals of this article is to propose a certain universal approach that allows us to study the stability of integro-differential equations in the case of unbounded memory in the integral operator specifying the feedback control in stabilization. The approach we propose allows us to reduce the study of integro-differential equations to the analysis of systems of ordinary differential equations. In general, such systems can consist of an infinite number of equations. In relation to the so-called linear approximation in the problem of angle stabilization manages to limit itself to relatively simple exponential kernels in the integral control and arrive at a system with a finite number of equations. The examples explain that more complex kernels, for example, linear combinations of the exponential kernels, can enhance the stabilization capabilities. We obtain new unexpectable results on the exponential stability of integro-differential equations. Then we apply them to stabilization of drone flight.

---


### 8. [MILP-Evo: Closed-Loop Fully Automatic Design of MILP Solvers](https://arxiv.org/abs/2607.18252)

**<font color=#1a73e8>作者：</font>** Jinbiao Nie, Kewei Feng, Xiaoyuan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning methods have shown that data-driven policies can accelerate mixed-integer linear programming (MILP) solvers, but many such approaches remain difficult to inspect, adapt, and deploy because the learned policy is represented as an external predictor or other opaque model. By contrast, explicit solver logic is easier to understand and integrate, but is usually hand-designed rather than learned from solver feedback. We study whether the automatic design of MILP solver logic can instead be cast as LLM-guided closed-loop search over executable white-box components evaluated directly by end-to-end solver behavior. To this end, we propose a closed-loop program evolution framework for MILP solver auto-design, implemented through PySCIPOpt, and instantiate it on the joint design of a cut selector and a branching rule. Candidate programs are iteratively generated, loaded into SCIP, and evaluated by direct execution on MILP instances, with the resulting feedback guiding performance-based selection, targeted repair, diagnostic reflection, and diversity-aware population maintenance. The method outputs explicit solver components that can be inspected, modified, and deployed within standard solver workflows. Across four benchmark families, we find that LLM-guided program evolution can discover competitive domain-specialized policies in several settings.

---


### 9. [Cross-Dialect Generalization Without Retraining: Benchmarks and Evaluation of Schema-Derived Constrained Decoding for MLIR](https://arxiv.org/abs/2607.18254)

**<font color=#1a73e8>作者：</font>** Plawan Kumar Rath  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Level Intermediate Representation (MLIR) underlies modern ML compiler infrastructure (TensorFlow, JAX/StableHLO, PyTorch Inductor, IREE), yet appears only in trace amounts in code-LM pretraining corpora. MLIR is also extensible by design: new dialects ship per application domain, so a fine-tuned model per dialect does not scale. We ask whether inference-time priors derived mechanically from each dialect's Operation Definition Specification (ODS) can substitute for gradient-based adaptation. First, we release four natural-language-to-MLIR benchmarks across three dialects - MLIR-Spec-150, Linalg-Spec-30, StableHLO-Spec-30, and StableHLO-Held-Out-200 - totaling 410 in-scope NL-to-MLIR pairs, plus a 25-program out-of-grammar stress set and a hand-authored n=30 functional reference set, shipped under Apache-2.0 with Gebru datasheets and Croissant 1.0 metadata. Second, we build a three-layer schema-derived constraint stack: a CFG over op signatures(C1), type-domain splits from an ODS-extracted type lattice (C2), and an SSA-scope validator driving five-retry rejection sampling (C3). Porting from arith+func+memref+linalg to StableHLO required no new constraint-layer code. On dialects whose verifier semantics are dominated by structural constraints, schema-derived priors let SmolLM2-1.7B match or exceed 15B-34B code LMs at 8-25x the per-generation speed: on linalg, SmolLM2 reaches 80.0% verify-valid (three-seed mean, n=125), beating CodeLlama-34B, Granite-Code-34B, and StarCoder2-15B by 21-44 percentage points with non-overlapping CIs. On arith+func and on the templated parametric StableHLO-Held-Out-200, where verifier semantics turn on attribute values rather than structure, the same baselines match or beat the SLM; we scope these as non-win cells. We release benchmarks, decoder, all per-prompt generations, and a reproducibility Docker image.

---


### 10. [Assistant or Actor? Student Trust, Control, and Delegation Regret When Using a General-Purpose AI Agent](https://arxiv.org/abs/2607.18257)

**<font color=#1a73e8>作者：</font>** Shiva Pochampally, Shengwei An, Yan Chen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When AI agents shift from answering questions to taking actions, users face a new problem: deciding what to delegate, to a system whose action space they cannot fully anticipate. We call the resulting dissatisfaction delegation regret, a pattern in which users regret not that the agent erred, but that it acted beyond what they would have authorized. In a controlled study, 20 university students completed five common daily tasks using OpenClaw, a general-purpose AI agent, across tasks chosen to vary in privacy, stakes, and reversibility. For each task we measured trust, perceived control, transparency, supervision burden, and approval preference on 5-point Likert scales, and collected free-text reflections analyzed through thematic coding. Three findings emerged. First, participants calibrated trust per task rather than per agent: they granted wide autonomy for advisory and low-stakes tasks but demanded confirmation for irreversible, externally visible actions. Second, irreversibility combined with external visibility, rather than stakes alone, appeared to drive trust withdrawal: the moderate-stakes email task triggered the sharpest drop in trust (M = 3.10) and the highest demand for approval (M = 4.65), whereas a high-stakes but verifiable task did not produce the same response. Third, delegation regret appeared consistently when the agent executed actions without preview, even when the output was rated as successful. We discuss implications for agent designs that expose action boundaries, support per-task autonomy policies, and separate advisory output from agentic execution.

---


### 11. [ProbSPARQL: Querying Knowledge Graphs with Multi-dimensional, Uncertain Numeric Data](https://arxiv.org/abs/2607.18262)

**<font color=#1a73e8>作者：</font>** Jingcheng Wu, Ratan Bahadur Thapa, Daniel Hernandez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The SFB 1574 Circular Factory is building a shared knowledge graph infrastructure for integrating data about returned products. A central challenge is that circular-factory data include numeric measurements that (i) originate from sensors or are derived from sensor-based measurements, (ii) are frequently multi-dimensional, and (iii) are inherently uncertain, while downstream triage, validation, reliability-modeling, and reassembly-planning modules require queryable uncertainty representations. Current RDF and SPARQL technologies lack native support for harmonized querying and analysis of such uncertain numeric measurement data. To address this gap, we present ProbSPARQL, an upward-compatible SPARQL extension developed as an early-stage query-layer pilot for this infrastructure. ProbSPARQL models uncertain numeric values as random variables whose distributions are encoded by probabilistic RDF literal datatypes, and supports distribution-aware expressions, probabilistic filters, and divergence-based joins. We implement ProbSPARQL on Apache Jena ARQ and expose it through a Fuseki-compatible execution layer. We assess real-data applicability using project-derived measurement fragments covering GMM-encoded uncertainty and histogram-based empirical roughness distributions, and evaluate scalability separately on controlled ontology-conformant benchmarks with up to 5,000 angle-grinder instances and 1.5M triples. The results show feasible in-engine execution, filter-pushdown speedups over application-layer post-processing, and latency-accuracy trade-offs among divergence-join decision strategies.

---


### 12. [Position: AI/ML Deepfake Research is Misaligned with AI-Generated Non-Consensual Intimate Imagery (AIG-NCII)](https://arxiv.org/abs/2607.18263)

**<font color=#1a73e8>作者：</font>** Li Qiwei, Wells Lucas Santo, Sarita Schoenebeck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-generated non-consensual intimate imagery (AIG-NCII) is not adequately addressed in AI/ML literature regarding AI-generated media, commonly referred to as "deepfakes". While research on deepfakes currently focuses on its epistemic harms -- or harms relating to truth and authenticity -- this is misaligned with the dominant reality of generative AI abuse involving sexualized imagery. We conduct a landscape analysis of highly-cited works to demonstrate that technical interventions addressing deepfakes almost entirely ignore AIG-NCII, limiting the research ecosystem to authenticity detection tools. In this position paper, we argue that existing interventions address viewer-centric epistemic harms, such as fraud or scams, but ignore subject-centric dignity harms, such as AIG-NCII. We illustrate that knowing an image is synthetic does not mitigate harms to subjects and may, in some cases, even exacerbate them. We conclude by offering recommendations to realign the field, including updating threat models to consider subject-centric harms and addressing AIG-NCII in AI safety research. Finally, we caution that researchers should only engage in this high-risk domain if they implement safety guardrails for both subjects and researchers and establish partnerships with domain experts in sexual violence prevention.

---


### 13. [MUX: Continuous Reasoning via Multiplexed Tokens](https://arxiv.org/abs/2607.18264)

**<font color=#1a73e8>作者：</font>** Ayhan Suleymanzade, Halil Alperen Gozeten, Michael Bronstein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models solve complex problems by articulating intermediate reasoning steps in natural language. While effective, this process is computationally bottlenecked: each reasoning step conveys only a single subword, and many are spent expressing a thought instead of carrying out computation. We propose MUX, a simple method for high-bandwidth and compact reasoning based on distillation of discrete reasoning into continuous multiplexed tokens in a latent space. Here, each latent token is trained to represent a weighted linear superposition (multiplexing) of a span of discrete reasoning subwords, where this superposition is lossless by construction and the span can be fully recovered (demultiplexing). We prove that simple position-dependent weightings, such as suitable geometric decay, support lossless multiplexing, which in turn prevents shortcut behaviors caused by latent collapse. We further show that multiplexed reasoning can perform parallel exploration in problems that require search. Across 32 evaluation settings spanning four language models, MUX outperforms strong latent reasoning baselines. Ablation and probing analyses further show that the learned latent tokens encode faithful and interpretable reasoning. Our results suggest that lossless superposition as local learning targets constitutes a sufficient condition for achieving strong and efficient latent continuous reasoning.

---


### 14. [Trajectory-Aware Clinical Risk Prediction via Severity-Grounded Knowledge Graphs and Retrieval-Augmented Generation](https://arxiv.org/abs/2607.18270)

**<font color=#1a73e8>作者：</font>** Kyunghoon Jeon, Youmin Ko, Woohwan Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Electronic Health Records (EHRs) offer a wealth of clinical data, effectively augmenting a patient's records with heterogeneous external knowledge to predict the patient's clinical risk remains a significant challenge. Existing methods fail to capture disease severity, treatment responses, and nuanced clinical progression, due to data sparsity and the underutilization of unstructured clinical notes. To address these challenges, we propose TRACER (a trajectory-aware and clinically grounded prediction framework) that (1) constructs a medical knowledge graph enriched with severity information from medical literature, (2) retrieves clinically relevant, severity-weighted paths of a patient's progression from the knowledge graph, (3) extracts clinically relevant events from unstructured clinical notes, and (4) augments patient context with similar peer cases. Experiments on the MIMIC-III and MIMIC-IV datasets demonstrate large gains over state-of-the-art baselines, with up to 28.5% increase in Macro F1 score for the mortality prediction task, and 19.7% increase for the readmission prediction task.

---


### 15. [FALCON-Discover: Discovering Concentrated False-Confidence Regions for Calibration](https://arxiv.org/abs/2607.18278)

**<font color=#1a73e8>作者：</font>** Filippo Cenacchi, Longbing Cao, Runze Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibration is usually evaluated in aggregate, but the most dangerous failures are often local: predictions that remain highly confident despite being wrong. We study this failure mode as false-confidence concentration, the extent to which confident errors occupy compact, discoverable regions of prediction space. We introduce FALCON-Discover, a post-hoc, model-agnostic framework that ranks predictions using discrepancy signals from confidence, local support, neighborhood agreement, and perturbation stability. Across seven binary tabular datasets, four seeds, five-fold cross-fitting, and strong learners including XGBoost and CatBoost, we find that false-confidence concentration is recurrent but regime-dependent. At the main confidence threshold, discrepancy-based ranking substantially outperforms the strongest validation-selected calibration or trust-scoring baseline in the strongest regimes, while raw confidence recovers little dangerous-error mass. The best detector varies across datasets: learned discrepancy is strongest when multiple cues must be combined, whereas stability-centered ranking works best when local decisional fragility dominates. These results show that dangerous overconfidence is better treated as a family-level discovery problem than as a single-score calibration problem, and motivate calibration strategies that explicitly target regions where confidence, support, and stability diverge.

---


### 16. [Beyond Output-Space Calibration: Spectral Evidence Bundling for Selective Reliability Estimation in Time-Series Classification](https://arxiv.org/abs/2607.18279)

**<font color=#1a73e8>作者：</font>** Filippo Cenacchi, Longbing Cao, Runze Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc calibration for time-series classification usually remaps output scores, but deployment decisions such as trust, abstention, and review depend on whether a confident prediction is supported by the current temporal signal. We address three time-series reliability gaps: identical confidence values can hide different temporal support, average calibration can miss false high-confidence errors, and output-space recalibration offers limited input-linked auditability. We introduce a validation-gated fixed-label reliability policy that keeps the backbone prediction unchanged while estimating whether it should be trusted. The method combines output-side cues with whole-sample spectral descriptors, including band energy, entropy, peak dominance, period support, and phase stability, to form a scalar reliability estimate and diagnostic band-level evidence. A validation gate enables spectral conditioning only when correctness ranking improves without breaching FalseConf@0.9 or AURC tolerances; otherwise it reverts to the safer output-space baseline. Across eight heterogeneous UCR/UEA datasets, eight time-series backbone families, and standard recalibrators, the unconstrained method improves fixed-label selective-reliability metrics on the matched evaluation subset, raising Corr-AURC from 0.693 to 0.779. The validation-gated policy further improves Corr-AURC to 0.786 and reduces FalseConf@0.9 to 0.094. These results suggest that reliability estimation for time-series classifiers benefits from bundling output confidence with spectral evidence, while validation gating prevents unsupported spectral conditioning.

---


### 17. [ALAS: Additive Learnable Alpha-Stable Kernels for Flexible Bayesian Optimization](https://arxiv.org/abs/2607.18282)

**<font color=#1a73e8>作者：</font>** Weibo Huang, Cheng Hua  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Optimization is widely used for expensive black-box optimization, yet its success often depends on choosing a kernel that matches the objective's unknown structure. In this work, we propose ALAS, a flexible Gaussian Process kernel family built from symmetric $\alpha$-stable spectral components. By learning the stability parameter $\alpha$, ALAS adapts its effective smoothness from data, capturing both smooth trends and sharp irregularities. We present two parameterizations: ALAS, a single stationary component with joint spectral modulation, and ALAS-Sep, a separable variant that learns dimension-wise tail behavior to improve robustness on approximately decomposable objectives. Experiments on standard benchmarks and real-world surrogates demonstrate strong and robust performance across diverse settings.

---


### 18. [Edge-Efficient Transformer for End-to-End RF Spectrum Monitoring](https://arxiv.org/abs/2607.18285)

**<font color=#1a73e8>作者：</font>** Zhifan Song, Haralampos-G. Stratigopoulos, Hassan Aboushady  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present E-SpecFormer (Edge Spectrum monitoring Transformer) for end-to-end automatic modulation and covert channel (CC) recognition. We introduce LiTAN (Linear Tanh Attention Network), a Softmax- and LayerNorm-free attention mechanism that reduces complexity while increasing accuracy in RF tasks. E-SpecFormer is parameterized in four scalable variants (Nano, Small, Medium, Large) to accommodate diverse hardware constraints. Using the RadioML2018 dataset for modulation recognition, the Nano variant achieves 86.5% average accuracy for Signal-to-Noise Ratios (SNRs)>0 dB, and on the hardware Trojan (HT)-based CC dataset it reaches 94.2% accuracy, both with fewer than 10k parameters and up to speed of 92 {\mu}s per frame on FPGA/CPU co-execution, surpassing state-of-the-art edge models at a fraction of their cost. These results establish E-SpecFormer as an edge-efficient solution for real-time spectrum intelligence on Internet of Things (IoT) devices. GitHub link to the repository: this https URL.

---


### 19. [Preference-Conditioned Multi-Objective Reinforcement Learning for Runtime-Tunable Transit Signal Priority](https://arxiv.org/abs/2607.18286)

**<font color=#1a73e8>作者：</font>** Philip-Roman Adam, Stefanie Schmidtner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transit signal priority (TSP) requires balancing competing objectives: reducing bus delay while limiting adverse impacts on non-bus traffic and avoiding extreme waits for a subset of vehicles. Existing reinforcement-learning (RL) approaches to TSP typically encode transit-aware features (e.g., occupancy and schedule deviation) but optimize a fixed reward or fixed scalarization, which limits operational flexibility when agency priorities change across time-of-day or disruption conditions. We present a preference-conditioned TSP controller, $\pi(a \mid s,w)$, that selects the next signal phase under minimum/maximum green and transition-feasibility constraints and can be tuned at runtime via a preference parameter $w$ to trade off bus-priority emphasis against overall traffic delay without retraining. We implement this on top of IntersectionZoo by introducing a constrained signal-control/TSP wrapper, and we extend scenario generation with bus-prevalence augmentation and timetable-based bus insertion to address sparse transit-priority events during training. Experiments against fixed-time control, a rule-based TSP overlay, and fixed-weight PPO specialists show that a single learned conditioned policy spans a smooth empirical trade-off frontier across runtime preferences, outperforms fixed-time and rule-based baselines, and maintains constraint feasibility, while tail-delay diagnostics reveal that non-bus externalities remain limited for moderate preference settings but can increase substantially under high bus-priority weights. The source code of this work is available at this https URL.

---


### 20. [BearingNAS: Obtaining In-Sensor Intelligent Fault Diagnosis Systems for Bearings Using a Laptop](https://arxiv.org/abs/2607.18287)

**<font color=#1a73e8>作者：</font>** Andrea Mattia Garavagno, Edoardo Ragusa, Paolo Gastaldo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces BearingNAS, a Hardware-Aware Neural Architecture Search (HW-NAS) framework designed to shift the intelligence directly onto the sensor die via in-sensor processing. BearingNAS frames the search as a constrained optimization problem targeting extreme micro-budgets (4 to 8 kiB of RAM and 16 to 32 kiB of Flash). To eliminate the reliance on expensive discrete GPUs, we propose a lightweight, derivative-free search strategy paired with a single data-flow search space that leverages a decaying kernel growth formulation to prevent parameter explosion. We evaluate our framework on the Case Western Reserve University (CWRU) bearing benchmark, optimizing architectures for three STMicroelectronics targets: two commodity microcontrollers and the LSM6DSO16IS Intelligent Sensor Processing Unit (ISPU). Running entirely on a laptop CPU, the search converges in less than an hour. The resulting best in-sensor architecture achieves a highly competitive diagnostic accuracy of 99.50\% on the ISPU. These results demonstrate the viability of shifting the machine learning workload inside the sensor package, enabling low-cost, production-scale bearing fault diagnosis.

---


### 21. [Multi-Timescale Latent-Action DRL for Joint Optimization in Edge-Cloud Networks](https://arxiv.org/abs/2607.18288)

**<font color=#1a73e8>作者：</font>** Vo Phi Son, Van-Dinh Nguyen, Ngoc Hung Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Load imbalance across edge and cloud layers degrades latency performance in hierarchical edge-cloud computing (HECC) systems under dynamic task arrivals and heterogeneous resources, leading to severe queuing delays and inefficient resource utilization. To address this challenge, we study a joint service placement, computational delegation, and power control (JSCP) problem to minimize the average end-to-end (e2e) latency. The resulting JSCP problem is a mixed-integer nonconvex and NP-hard optimization problem due to the strong coupling between discrete and continuous variables. To enable tractable optimization and stable system adaptation, we exploit the inherent difference in decision dynamics and decompose the problem into long-term system configuration and short-term resource allocation subproblems. Based on this formulation, we propose a two-timescale multi-layer deep reinforcement learning framework with a latent action space (2T-MDRL-LA) to jointly optimize service placement, user association, computational delegation, task offloading, and user transmit power. A latent action representation based on a variational autoencoder is introduced to efficiently compress the high-dimensional combinatorial action space. Simulation results demonstrate that the proposed framework effectively adapts to dynamic network conditions and achieves near-optimal performance compared to branch-and-bound solutions. It achieves up to a 20.8% reduction in average e2e latency and a 13% improvement in resource utilization over the scheme without the computational delegation, while converging approximately 50% faster than conventional proximal policy optimization.

---


### 22. [Towards Principled Continual Anomaly Detection: A Systematic Framework and Benchmark Scenarios](https://arxiv.org/abs/2607.18289)

**<font color=#1a73e8>作者：</font>** Kamil Faber, Mateusz Smendowski, Roberto Corizzo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual anomaly detection (CAD) studies how models can adapt to evolving data distributions while retaining performance on previously observed regimes. CAD benchmarks, however, depend critically on how tasks are defined, filtered, ordered, and validated. In tabular domains, task boundaries are rarely given, and arbitrary splits can create unlearnable, redundant, or overly transferable tasks that obscure genuine continual-learning behavior. To this end, we introduce a systematic framework for reproducible benchmark scenario design from existing tabular anomaly-detection datasets. The framework discovers candidate tasks, filters unsuitable tasks, and derives principled orderings that expose diverse dynamics. The framework allows us to deliver five benchmark-ready scenarios from three large-scale cybersecurity anomaly detection datasets, yielding both single-dataset and multi-dataset CAD settings.

---


### 23. [SechKAN: Kolmogorov-Arnold Networks with Hyperbolic Secant Functions](https://arxiv.org/abs/2607.18290)

**<font color=#1a73e8>作者：</font>** Hoang-Thang Ta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, Kolmogorov-Arnold Networks (KANs) have attracted increasing attention due to their effectiveness in machine learning and scientific computing tasks, offering a new paradigm for neural network design. In this paper, we present SechKAN, a KAN architecture based on hyperbolic secant (sech) functions. The hyperbolic secant basis is used for its smooth bell-shaped form, localized responses, and stable gradients. We employ 1D linear transformations to reduce the number of parameters, allowing SechKAN to remain comparable to multilayer perceptrons (MLPs) in model size. Experimental results indicate the effectiveness of SechKAN in function fitting, PDE problems, and image classification tasks on benchmark datasets, including MNIST, Fashion-MNIST, CIFAR-10, and CIFAR-100. SechKAN achieves superior performance compared to MLPs and other KAN variants while maintaining a similar number of parameters. However, its running time, while better than that of other KAN variants, is slightly longer than that of MLPs.

---


### 24. [Dual-domain fused LSTM modeling for efficient time-dependent reliability analysis](https://arxiv.org/abs/2607.18291)

**<font color=#1a73e8>作者：</font>** Yixin Zhang, Mingyang Li, Zichao Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-dependent reliability analysis is crucial for ensuring the long-term safety and performance of engineering systems under uncertainties. However, traditional surrogate model methods often struggle to incorporate time-independent random variables and capture their complex interactions with time-dependent stochastic processes. To overcome this limitation, this paper proposes a dual-domain fused long short-term memory (DDF-LSTM) model for efficient and accurate time-dependent reliability analysis. A novel network architecture is developed to jointly process information from both time-dependent and time-independent domains. Specifically, the time-independent variables are embedded into the initial hidden states, and a fully connected layer is introduced to map both LSTM outputs and time-independent variables into the final output space. Furthermore, an improved loss function is designed to emphasize the model's sensitivity to minimum responses, thereby improving the precision of failure probability estimation. The proposed method effectively captures the dependencies among random variables, stochastic processes, and the temporal behavior of limit state functions. Once trained, the DDF-LSTM model enables efficient Monte Carlo simulation to estimate time-dependent failure probabilities with minimal computational cost. Four case studies validate the proposed method's enhanced computational efficiency and predictive accuracy.

---


### 25. [Reliability Scales Inversely: Bigger Models Compound Mistakes Faster via a Hidden Auto-Regressive Risk Regime](https://arxiv.org/abs/2607.18292)

**<font color=#1a73e8>作者：</font>** Kushal Chakrabarti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As language models scale, answers start truer but degrade faster: scaling buys capability but erodes reliability. The knowledge-gap account - more data, retrieval, or scale - misses an auto-regressive risk residual that scale sharpens: the model commits to a low-probability token, conditions on it as established, and snowballs. We track this through per-position disagreement $\delta = \log p_M - \log p_O$ against a stronger same-family oracle, whose second moment splits exactly into bias$^2$ $\mathrm{KL}(p_M \,\|\, p_O)^2$ and risk $\mathrm{Var}[\delta]$. We present four findings: (i) under scaling, the knowledge gap falls $\approx$$6\times$ while knowledge degradation grows $11$-$39\times$; (ii) at a fabrication, felt uncertainty $H(p_M)$ relaxes quickly while oracle-referenced risk persists up to $17\times$ longer, leaving a confident-but-precarious risk regime that bridges consecutive fabrications ($+69\%$ at $14$B); (iii) this regime is causal - an on-policy, fixed-$\mathrm{KL}$ variance contraction cuts web-verified hallucination by $35$-$74\%$ across three model families; and, (iv) it structurally evades self-monitoring, with $p_M$-only detectors (e.g. semantic entropy) firing $\approx$$30\%$ less ($p<10^{-16}$) on the risky branch holding nearly $4\times$ more fabrications. Bigger models snowball mistakes faster, through a failure mode that is dominant, self-perpetuating, causal and invisible to the model itself.

---


### 26. [Uncertainty Quantification for AI-Driven Crash Simulation Surrogates: A Comparative Study of Monte Carlo Dropout and Deep Ensemble on Open-Source Bumper Beam Benchmark](https://arxiv.org/abs/2607.18294)

**<font color=#1a73e8>作者：</font>** Sudeep Chavare  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning surrogate models are increasingly being explored in engineering product development to augment simulation-driven design, offering near-instantaneous predictions that complement computationally expensive high-fidelity analyses. However, a critical gap limits their adoption in safety-critical workflows: a point prediction without an accompanying uncertainty estimate cannot tell an engineer when the model should not be trusted. This work presents a systematic, head-to-head comparison of two widely used uncertainty quantification approaches -- Monte Carlo Dropout and Deep Ensembles -- applied to an open-source surrogate pipeline built on NVIDIA PhysicsNeMo. A key contribution is the use of concrete dropout, a built-in PhysicsNeMo capability that eliminates the dropout rate as a manual hyperparameter by learning it end-to-end during training, directly addressing the most common criticism of Monte Carlo Dropout-based uncertainty quantification. Automotive crash simulation is used as the application domain, with a steel bumper beam impact problem serving as the benchmark. Both methods are evaluated on identical held-out simulations and compared on point accuracy, uncertainty band calibration, and computational cost. The results reveal a fundamental trade-off between accuracy and calibration that challenges the common assumption that deep ensembles are the default gold standard for surrogate uncertainty quantification. The findings demonstrate that well-calibrated, hyperparameter-free uncertainty estimates are achievable within a fully open-source engineering workflow at a fraction of the computational cost of ensemble approaches.

---


### 27. [Deep Reinforcement Learning to Master the Asymmetric Strategy of Baghchal](https://arxiv.org/abs/2607.18296)

**<font color=#1a73e8>作者：</font>** Ranjit Raut, Aarav Subedi, Sagun Rai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Baghchal is a two-player asymmetric board game with Nepali origins where four tigers are to capture goats and twenty goats desire to keep tigers in immobility. Although Baghchal has a complex structure which is strategic, has perfect information structure, and has cultural meaning, it has not been adequately covered in deep reinforcement learning (RL) literature. This paper gives a systematic exploration of four deep RL solutions Deep Q-Network (DQN), REINFORCE, Proximal Policy Optimization (PPO) and MuZero that are trained on one side of the asymmetric gameplay of Baghchal and then evaluated on the other side. The algorithms are rated based on win rate, draw rate, average captures, training convergence and computational cost. It is experimentally found that MuZero generates the best performance in both tasks, achieving 86 percent win over these Tiger and 62 percent win over these Goat and the ability to do so is due to the model-based planning machine through the Monte Carlo Tree Search. PPO is the most realistic algorithm and is provided to be competitive over both asymmetric tasks with significantly reduced computational costs compared to MuZero. Emergent strategic behavior analysis shows that model-based strategies are optimal over long-horizon planning, whereas value-based counterparts like DQN are more biased up towards the Tiger role owing to the more substantial reward signal.

---


### 28. [Gradient-Energy Guided Block-Wise Perturbations for Sharpness-Aware Minimization](https://arxiv.org/abs/2607.18306)

**<font color=#1a73e8>作者：</font>** Zhen Huang, Jiaxin Deng, Junbiao Pang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sharpness-Aware Minimization (SAM) improves generalization by minimizing the worst-case loss in a local parameter neighborhood. Standard SAM implicitly allocates its global perturbation budget across parameter blocks according to instantaneous minibatch gradient norms. Such an allocation can be noisy and may not reflect the sensitivity that blocks accumulate throughout training. We propose Gradient-Energy Adaptive Radius SAM (GEAR-SAM), which maintains an exponential moving average (EMA) of squared block gradients as a lightweight, curvature-related sensitivity signal and allocates the fixed SAM budget through a closed-form constrained optimization. GEAR-SAM preserves the global SAM radius, requires no Hessian-vector products or explicit Fisher estimation, and adds only scalar state beyond SAM. Experiments on image classification, transfer learning, noisy-label learning, and partition studies demonstrate improved generalization and robustness across architectures and tasks. More broadly, GEAR-SAM provides a dynamic view of sharpness-aware optimization: a fixed perturbation budget should be redistributed as the sensitivity of functional network blocks evolves during training.

---


### 29. [Spatio-Temporal Prediction of Unsteady Airfoil Aerodynamics Using Augmented Graph Neural Ordinary Differential Equations with Exogenous Controls](https://arxiv.org/abs/2607.18309)

**<font color=#1a73e8>作者：</font>** Henrik Lange, Reik Thormann, Philipp Bekemeyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsteady aerodynamic phenomena, such as gusts, turbulence, and fluid-structure interactions affect an aircraft during flight. For design, optimisation and certification, it is indispensable to quantify such unsteady aerodynamic effects. Industry-standard computational fluid dynamics methods, such as solving the unsteady Reynolds-averaged Navier-Stokes equations or the linearized frequency domain method, are either computationally expensive or restricted by assumptions like linearity. Once trained, machine learning methods are capable of computing non-linear relationships very fast, making them suitable as surrogate models. By autoregressively applying graph neural networks (GNNs), operating on a discretised spatial domain, spatio-temporal predictions can be made. However, autoregressive GNNs suffer from error accumulation leading to unstable rollouts over time. Here we show that combining GNNs with augmented Neural Ordinary Differential Equations yields temporally stable predictions of the surface forces on a pitching airfoil. We found that our approach, called GNODE, based on Graph Neural Ordinary Differential Equations, provides temporally more stable, spatially smoother, and overall more accurate results than an autoregressive GNN baseline. Tests are conducted on a dataset consisting of a simulations of a pitching airfoil, including transonic shocks, transient behaviour and dynamic non-linearities. Augmenting GNODEs with additional latent dimensions improves the expressivity and accuracy by capturing underlying history effects. The developed method demonstrates an approach that is suitable to model non-linear spatio-temporal systems with exogenous inputs.

---


### 30. [Interactive Training 2: Auditable Control Plane for Live Model Training](https://arxiv.org/abs/2607.18314)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Xuanhe Pan, Han Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Experiment trackers show how training is progressing, but changing a live run still usually requires trainer-specific code. We present Interactive Training 2, an open-source control plane for steering training through a shared protocol. Training applications declare which settings and actions they expose, humans and automated controllers submit requests through the same interface, and the training loop validates and applies them at safe control points. A customized Aim workspace combines live metrics and controls with a chronological record of requests and outcomes. We demonstrate the system across five NLP and reinforcement-learning workflows. The released code and traces provide a reusable foundation for auditable human- and agent-guided training.

---


### 31. [Decoding EEG Signals to Explore Next-Word Predictability in the Human Brain](https://arxiv.org/abs/2607.18321)

**<font color=#1a73e8>作者：</font>** Boi Mai Quach, Binh T. Nguyen, Cathal Gurrin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans invented reading and have passed down this complex skill across generations through language. This study provides empirical evidence of the neural mechanisms underlying bottom-up (related to high-order linguistic structure) and top-down (related to next-word predictability) processes, which interact to guide comprehension during reading. While previous studies have focused on either the N400 effects of predictability or lexical categories, research on how predictability influences N400 responses across different lexical categories is limited, mainly due to constraints in publicly available datasets. Here, we examine how predictability influences brain responses, recorded at millisecond resolution using electroencephalography (EEG), with a focus on the N400 time window (300-500 ms post-stimulus) across different lexical and grammatical categories. Our results indicate that significant differences in N400 responses between high and low cloze probability levels were more pronounced for content words than function words. Among the two primary content categories, verbs exhibited greater N400 differences than nouns, while nouns carried more distinct information about their predictability than verbs. Moreover, we demonstrate that the decoding technique is more effective than the event-related potential (ERP) traditional analysis in capturing more detailed and distinct representations of cognitive processes over time.

---


### 32. [Cost Accounting for Reactive Computational Graphs: Exhaustive Sweeps, Sequential Mutation, and the Backward-Locality Gap](https://arxiv.org/abs/2607.18323)

**<font color=#1a73e8>作者：</font>** Abdallah Khemais  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exhaustive site-by-site interventions on a neural network's computational graph -- activation-patching sweeps, circuit-discovery searches, systematic ablation studies -- mutate the graph at every candidate site, and their cost is dominated by recomputation after each mutation. On a reactive graph engine whose invalidation provably touches exactly the downstream cone of a mutated node, we give a complete cost accounting for such workloads. First, the aggregate speedup of an exhaustive sweep over independent full recomputations is not a universal constant: if per-layer weight varies regularly with depth at Karamata index q, the ratio converges to (q+2)/(q+1) when weight concentrates near the output and to q+2 near the input, recovering 2 only in the depth-uniform case; a wall-clock corollary predicts a ceiling of about 1.79, below 2, until interpreter overhead is compiled away. Second, we prove the exact cost of a sequence of persistent mutations, never undone between insertions: the interleaved cost exceeds the isolated sum by an exact overcount summed over comparable site pairs, with closed-form extremes over insertion orders, while batched application is order-independent and sub-additive, costing exactly the union of the sites' cones plus the fresh nodes. Third, we prove the exact mirror of forward locality for the backward pass, showing it collapses the aggregate speedup to 1 under backpropagation on architectures without long skip connections. Every identity is validated on NeuroDSL, a reactive graph engine in Julia: measured sweep ratios converge to the predicted limits under four cost profiles; the training-mode ratio collapses to 1 at the predicted rate; and all 18 per-graft sequential costs and the batched total match the closed forms at zero tolerance across three insertion orders.

---


### 33. [Hazard or Anomaly? Evaluating VLMs for Understanding Dangers and Discrepancies](https://arxiv.org/abs/2607.18325)

**<font color=#1a73e8>作者：</font>** Murali Indukuri, Mohammad Eskandari, Sree Nitya Kollu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern safety-critical systems increasingly rely on human-robot interaction to reduce disaster risk and support decision-making during emergencies. Vision-Language Models (VLMs) are promising for these settings because they can interpret complex scenes and communicate safety-relevant information, but they still require careful evaluation to ensure reliable safety reasoning. In particular, current evaluations often frame danger recognition as a binary decision (Safe/Unsafe), making it unclear whether a model is identifying true physical hazards or merely reacting to unusual scene elements. We address this limitation by introducing an explicit distinction between hazard and anomaly, and by separately recognizing hazardous and anomalous states. We evaluate several state-of-the-art VLMs across two datasets and multiple prompting strategies to test whether this distinction changes model behavior. Our results show that VLMs frequently misinterpret anomalousness as hazardousness, revealing an over-reliance on contextual irregularity as a proxy for danger. We further show that explicitly separating anomaly from hazard provides a more informative evaluation of VLM safety reasoning and exposes failure modes that binary safety judgments can obscure. Our public dataset is available on Roboflow this https URL.

---


### 34. [Dynamic Loss Balancing for Joint SOH and RUL Prediction of Lithium-Ion Batteries via a Rotary SOH-Injected Prior Battery Transformer](https://arxiv.org/abs/2607.18329)

**<font color=#1a73e8>作者：</font>** Shuhao Chen, Tianyu Shi, Yiwen Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deployment of reliable lithium-ion battery management systems is crucial for accelerating electrification, yet the joint prognosis of State of Health (SOH) and Remaining Useful Life (RUL) remains severely hindered by task heteroscedasticity. Conventional multi-task learning frameworks fail to balance the bounded, low-variance noise of SOH estimation with the unbounded, nonlinearly expanding uncertainty of long-term RUL predictions. Here, we present the Rotary SOH-Injected Prior Battery Transformer (RoSIP-Batt), a unified co-estimation framework that resolves these optimization conflicts. By formulating joint prediction as a Bayesian multi-task objective, RoSIP-Batt introduces a homoscedastic uncertainty weighting mechanism to dynamically scale task-specific gradients based on learned residual noise levels. The architecture leverages decoupled dual classification tokens and a per-dimension gated fusion mechanism, secured by a gradient-detachment operator to prevent high-variance RUL updates from corrupting the stable SOH representation space. To capture electrochemical degradation patterns without relying on absolute cycle steps, Rotary Position Embedding (RoPE) is incorporated into a shared Transformer backbone to model translation-invariant relative temporal profiles. Crucially, the intermediate SOH estimate is directly injected into the RUL regression head as a physical degradation prior. Evaluations across the NASA, MIT-Stanford, and HUST datasets show that RoSIP-Batt significantly outperforms state-of-the-art baselines, reducing SOH estimation error to 1.994% MAE on NASA and restricting RUL prediction error to 62.85 cycles on Stanford. These findings establish RoSIP-Batt as a highly generalizable, computationally efficient solution suitable for real-time embedded BMS deployment.

---


### 35. [ChemHyperMag: Physics-informed magnetic hypergraph learning improves molecular ADMET prediction](https://arxiv.org/abs/2607.18332)

**<font color=#1a73e8>作者：</font>** Hexiao Ding, Hongzhao Chen, Jing Lan 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) is important for drug discovery. Most predictors use undirected molecular graphs and pairwise edges. This choice misses asymmetric interactions, nonreversible dynamics, and motif level effects from functional groups and ring systems. We propose ChemHyperMag for multitask ADMET prediction under missing labels. ChemHyperMag builds a functional group hypergraph from rings, BRICS fragments, Bemis-Murcko scaffolds, and bonds. It also defines a potential driven nonreversible flow guided by electronegativity and Gasteiger partial charges. The resulting circulation is encoded by a Hermitian magnetic Laplacian and processed with a magnetic Chebyshev encoder. We perturb magnetic phases to form stochastic views and train with an InfoNCE objective. Experiments on multiple ADMET benchmarks show improvements over recent methods with fewer labeled samples and no conformers. ChemHyperMag is scalable and provides interpretable directional signals through its magnetic phases.

---


### 36. [Shared Vulnerabilities in Robustness-Optimized Defenses: One Breach Exposes the Family](https://arxiv.org/abs/2607.18339)

**<font color=#1a73e8>作者：</font>** Hanrui Wang, Ruihao Zheng, Shuo Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness optimization aims to preserve correct prediction under adversarial perturbations, and has produced substantial robustness gains through methods such as adversarial training and adversarial purification. However, we identify a new security risk: these gains can create shared vulnerabilities across defenses. Once one representative robustness-optimized defense is effectively breached, the broader family may become exposed. Studying this risk requires separating genuine transferability from distortion-induced degradation and from the algorithmic gains of sophisticated attacks. We therefore introduce stricter transfer-only protocols and a deliberately simple adaptive attack, PGDTransfer, to test whether robustness-optimized defenses share transfer-only vulnerability under controlled conditions. We further introduce Adversarial Sensitivity Maps (AdvSMs) to visualize and quantify shared alignment beyond differentiable classifiers, including stochastic and non-differentiable defenses. Across adversarially trained classifiers, purification-based defenses, and LVLMs with robust visual encoders, we identify natural transferability within each robustness family, i.e., transfer that arises even with simple PGD-style optimization rather than specialized transferable-attack design. The risk is already severe for purification: PGDTransfer reaches an average transfer attack success rate of $80.4\%$ across filtering-, compression-, and diffusion-based purifiers under $\epsilon=4/255$, suggesting that purifier defenses may no longer provide reliable protection. As attacks improve, currently stronger robustness families may face the same risk. Future defenses should therefore treat vulnerability diversity and transfer-only isolation as security objectives, rather than optimizing only individual robustness.

---


### 37. [Quantum Cryptanalysis on IBM Quantum Hardware: Extending Even--Mansour Period Recovery from $N=4$ to $N=10$](https://arxiv.org/abs/2607.18340)

**<font color=#1a73e8>作者：</font>** Taebong Kim, Youngsik Hong, Minsik Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We report genuine-un-compiled, textbook-faithful-quantum cryptanalysis of symmetric-cipher structures executed on real IBM quantum hardware (ibm\_kingston, Heron generation). Using Simon's algorithm we recover the hidden period of the Even-Mansour cipher up to security parameter N = 10 on real hardware, beyond the largest previously reported real-hardware key recovery of N = 4, and we cleanly recover the periods of a 3-round Feistel (DES-family) construction at block sizes 6 and 8; a 21-qubit block-10 instance is verified in simulation and submitted to hardware. We further provide a breadth-first benchmark of five genuine quantum attacks spanning four symmetric-cipher design paradigms -- Bernstein-Vazirani (linear structure, single query), Grover (SPN key search, quadratic), and Simon (Even-Mansour, CBC-MAC forgery, and Feistel; exponential-to-polynomial in query complexity) -- validated to the classical-simulation ceiling of 25 qubits. We are deliberately explicit about scope: these attacks target reduced or structured constructions in the Q2 (quantum-query) model, asymptotically follow the birthday bound and therefore do not constitute quantum advantage over classical collision-finding, do not break full AES/RSA or 16-round DES, and rely on error mitigation rather than fault-tolerant error correction. Our contribution is the real-hardware demonstration at record structure sizes, the breadth of genuine algorithmic coverage across four paradigms, and an honest, reproducible benchmark with public artifacts.

---


### 38. [PRISM: Sensitivity-Aware PolynoMial PRuning for EffIcient Neural Network Encryption](https://arxiv.org/abs/2607.18342)

**<font color=#1a73e8>作者：</font>** Sahaj Majavdia, Mahdi Taheri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Structured pruning is essential for making neural network inference feasible under homomorphic encryption (HE), yet its impact on model reliability has remained unexplored. This paper presents a systematic reliability characterization of pruned CKKS-encrypted neural networks and introduces Polynomial-Sensitivity-Aware Pruning (PSAP), a structured pruning method that is inherently reliability-aware. PSAP scores filters jointly by weight magnitude, polynomial activation sensitivity, and rotation cost, which concentrates pruning in fault-tolerant regions. Across two architectures, two datasets, two numerical representations, and five bit-error rates (40 full-model and 108 per-layer experiments), PSAP-pruned models limit catastrophic (>10 pp accuracy drop) layers to at most two versus 5--14 for magnitude-pruned baselines, reducing worst-case vulnerability by up to 29 times under int32 bit-flip injection. Direct CKKS encrypted fault injection indicates a safe operating boundary near BER~ 10^{-5}, supporting int32 injection as a conservative reliability proxy. The fault-critical structural layers account for only 1.1% of parameters, enabling selective hardening at minimal overhead. These reliability gains are obtained alongside competitive efficiency: PSAP reduces Halevi--Shoup rotations by up to 45.2\% on ResNet-32, and an adaptive mixed-degree allocation scheme lowers multiplicative depth from 66 to 56 levels, enabling leveled inference without bootstrapping.

---


### 39. [An Analysis of Residual-Stream Geometry Across Transformer Depth](https://arxiv.org/abs/2607.18348)

**<font color=#1a73e8>作者：</font>** Sunit Bhattacharya, Ravi Shankar Kolli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a transition-centred geometric analysis of transformer residual streams. Relative displacement measures how \emph{far} representations move between consecutive layers, and orthogonal Procrustes analysis separates each transition into a rigid rotation and a non-rigid residual. Across six instruction-tuned models, on code generation and cross-lingual translation, these measurements reveal reproducible depth regularities. Relative displacement is strongly layer-dependent; typically larger early and late, with a quieter middle third; and nearly invariant across conditions within each model. Rotation magnitude is nearly constant across depth, while Procrustes residual and angle concentration remain depth-modulated, with residual peaking at the final transition. During generation, non-English targets show larger final-layer displacement and residual than English targets. We present these as descriptive geometric regularities, not as measures of computational effort or causal explanations. The contribution is a measurement framework for residual-stream transitions and evidence that, in the settings studied here, depth curves are model-dependent and largely condition-stable.

---


### 40. [From Pixel to Prognosis: Convolutional and GLCM Feature Fusion for Automated Four-Class Cataract Severity Classification](https://arxiv.org/abs/2607.18349)

**<font color=#1a73e8>作者：</font>** K. Mithra, Prem Kumar Santhanam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: To develop a low-cost automated cataract severity classification system operating on standard consumer-grade colour photographs of the eye, without specialised ophthalmic hardware. Methods: A hybrid framework was designed that fuses deep features from a Convolutional Neural Network (CNN) with five handcrafted Grey-Level Co-occurrence Matrix (GLCM) and intensity descriptors - mean intensity, uniformity, standard deviation, contrast, and energy - extracted from a Hough-circle-localised pupil Region of Interest (ROI). A multi-class Support Vector Machine (SVM) with Radial Basis Function (RBF) kernel classifies each image into one of four severity grades: normal, immature, mature, or hypermature cataract. Results: The proposed fused system achieved 95.0% accuracy, 93.8% sensitivity, and 96.1% specificity on an ophthalmologist-labelled test set drawn from 300 images (75 per class) collected at an ophthalmology clinic, outperforming texture-only (88.5%) and CNN-only (91.3%) baselines and surpassing recently published deep learning approaches. Conclusion: The CNN-GLCM-SVM fusion framework provides competitive four-class cataract grading without GPU acceleration or specialised cameras, making it suitable for primary-care and telemedicine deployment in resource-limited settings.

---


### 41. [MambaLSTM: A Spatio-Temporal Framework for Enhanced Traffic Accident Risk Prediction](https://arxiv.org/abs/2607.18353)

**<font color=#1a73e8>作者：</font>** Zhen Yu, Yachao Yuan, Zixiang Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In traffic accident risk prediction, most studies overlook the extra noise that could be incorporated when fusing temporal features into spatial features, and some models struggle to capture global correlations among spatial regions. To address these challenges, we propose a novel traffic accident risk prediction framework named MambaLSTM. First, we develop a squeeze-and-excitation temporal feature fusion module to integrate temporal information without compromising spatio-temporal integrity. Second, we introduce a new patch embedding module for effectively capturing semantic relationships among spatially adjacent regions. Additionally, we introduce a Mamba block based on state-space models to model global spatial semantics in urban regions. Finally, we propose a MambaLSTM unit to efficiently capture long- and short-term temporal dependencies for identifying dynamic risk patterns. Extensive experiments on real-world datasets demonstrate the proposed model's superiority over state-of-the-art methods. The code is released at this https URL.

---


### 42. [Multi-layer MIMO Relay as Deep Physical Neural Networks: Power Amplifiers as Activation Functions](https://arxiv.org/abs/2607.18354)

**<font color=#1a73e8>作者：</font>** Meng Hua, Itsik Bergel, Deniz Gündüz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wireless physical neural networks (WPNNs) embed neural computation directly into analog hardware, offering lower energy consumption and latency than conventional digital implementations. In this paper, we propose a deep WPNN in which nonlinear activations are realized by a multi-hop multiple-input multiple-output (MIMO) relay network, in which each relay implements a trainable complex linear gain and bias, followed by the power amplifier's intrinsic nonlinearity acting as an activation function. The cascade of multiple relays therefore realizes an over-the-air fully connected network whose parameters can be trained end-to-end. We develop two transceiver designs for different channel state information (CSI) availability scenarios: a least squares (LS)-based scheme requiring only receiver-side CSI, and a singular-value-decomposition (SVD)-based scheme requiring both transmitter-side and receiver-side CSI. Simulation results show that the proposed architecture enables accurate over-the-air inference for image classification. In particular, the results highlight the advantage of exploiting hardware nonlinearity for enhanced inference capability.

---


### 43. [A Classifier That Teaches Itself: Self-Improving, Frozen-gate Training (SIFT) for Dynamic Document Classification](https://arxiv.org/abs/2607.18358)

**<font color=#1a73e8>作者：</font>** Bogdan Raduta, Horia Velicu, Alexandru Preda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document classification is a solved problem in the laboratory and an unsolved one in the enterprise. The blocker is rarely model architecture; it is the labeling project that must precede a model and the institutional fear of letting a model retrain itself once one exists. We present SIFT (Self-Improving, Frozen-gate Training), a dynamic classifier service, which attacks both. SIFT serves classification from a deliberately cheap, CPU-bound pipeline, a SPLADE sparse encoder feeding a LightGBM head, and escalates only the low-confidence minority of pages to an LLM judge. The judge's verdicts are written back into a labeled corpus, so the expensive model continuously teaches the cheap one: the escalation rate falls, the corpus grows from production traffic rather than from an up-front annotation effort, and accuracy compounds with use. Onboarding a new document family requires only a declarative bundle, label space, anchor phrases, and a judge glossary, not a labeling project. The harder problem is safety: an autonomously retraining classifier can silently regress. SIFT resolves this with a two-part promote gate, a critical-label F1 regression check plus a frozen golden regression set the model is never trained on, either of which vetoes promotion. This turns "retrain monthly without a human" from reckless into routine. We describe the architecture, the self-feeding corpus loop, the frozen-gate promotion mechanism, and an illustrative multi-domain deployment, and we discuss the economics of a classifier whose marginal labeling cost trends toward zero.

---


### 44. [Decentralized Multi-agent Reinforcement Learning for Resilient Critical Infrastructures](https://arxiv.org/abs/2607.18359)

**<font color=#1a73e8>作者：</font>** Minghui Ding, Evangelos Pournaras  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Critical infrastructures are increasingly distributed, interdependent, and exposed to evolving disruptions, making resilience a central requirement for their operation and control. This paper argues that decentralized multi-agent reinforcement learning (MARL) should be understood not merely as a distributed alternative to centralized training with decentralized execution but as a paradigm structurally aligned with the requirements of resilient critical infrastructures. This perspective is grounded in an analysis of the properties of decentralized MARL and the requirements of critical infrastructures, including scalability to large numbers of agents, support for privacy and local autonomy, robustness to failures, and interaction-driven adaptation among interdependent components. However, structural alignment alone is insufficient for practical deployment. This paper identifies credit assignment and communication as two central conditions for its practical feasibility. Credit assignment determines whether local learning remains aligned with system-level objectives, while communication determines whether coordination can be learned and maintained under realistic operational constraints. Building on these challenges, this paper proposes a research agenda focused on structure-aware, causality-aware, and resilience-aware credit assignment; communication for both coordination and credit assignment; and safe, timely, and recoverable decentralized learning under deployment constraints. Overall, this paper reframes decentralized MARL as a promising but conditional foundation for resilient critical infrastructures.

---


### 45. [Physical Self-Supervised Learning: IMU Sensing without Manual Labels](https://arxiv.org/abs/2607.18361)

**<font color=#1a73e8>作者：</font>** Yuyang Leng, Renyuan Liu, Shaohan Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks have become a promising approach for IMU-based sensing, but their scalability is fundamentally limited by costly labeled data and poor robustness to heterogeneous devices, placements, and users. Existing unsupervised and self-supervised methods reduce but do not remove this dependence, still requiring labeled data for domain adaptation and largely ignoring known physical structure. We propose physical self-supervised learning, an autoencoder-style paradigm for label-free IMU sensing. We replace the conventional neural decoder with an auto-adaptive physics decoder, a learnable family of kinematic equations that enforces explicit physical structure while adapting across environments, and adopt a hybrid two-stage IMU encoder with reconstruction in a structured latent space to mitigate sensor noise. Our framework further introduces probabilistic frequency-spatial constraints to disentangle sensor and object motion, a multi-view kinematic tree to exploit sparse physical self-supervised signals, and an uncertainty-aware formulation to handle the inherent ambiguity of IMU inference. Evaluated on inertial tracking and full-body motion capture over public datasets and realistic deployments, physical self-supervised learning reduces errors by up to 5x for tracking and 4x for motion capture in challenging generalization scenarios, consistently outperforming state-of-the-art supervised and self-supervised baselines without any labels.

---


### 46. [A Controlled Study of Attention-Only Transformers](https://arxiv.org/abs/2607.18363)

**<font color=#1a73e8>作者：</font>** Henry Ndubuaku, Karen Mosoyan, Jakub Mroz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feed-forward networks hold two thirds of a transformer's non-embedding parameters, yet the architecture has not received a necessity test that controls parameters, compute, and depth at once. We pretrain attention-only decoder transformers (Simple Attention Networks, SANs) against standard transformers matched separately for parameter count, training FLOPs, and depth (2 to 48 layers), for up to 105B tokens at 6M to 87M parameters. Deleting feed-forward layers in place is costly: the standard transformer leads by 0.47 nats at matched depth and 0.26 nats at matched FLOPs. Reallocating the freed budget into attention depth closes the gap: at matched parameters the difference is 0.006 nats (0.27 percent of loss), reproducible to one part in ten thousand across seed pairs, shrinking across 5B, 30B, and 105B budgets, and holding near 0.02 nats across a 29x size range. Three measurements localize the remaining gap to parametric recall: attention-only models are better on context-grounded answers and worse where knowledge must come from weights. Weight spectra show why: routing matrices (Q/K) crystallize early, content matrices accumulate rank slowly, and removing feed-forward layers relocates this accumulation to the attention output projection. QK-normalization, not feed-forward layers or residual gating, keeps 48-layer attention-only stacks trainable. The deficit concentrates on low-context query prediction and localizes there entirely by the largest budget. A pre-registered test confirms the account: it predicts a 0.02 to 0.05 nat gap on knowledge-dense web text; a matched pair trained on fineweb-edu measures 0.040. Within the tested regime, attention does the rest.

---


### 47. [Neuro-Symbolic Meta-Policies for Temporal Knowledge-Graph Memory under Partial Observability](https://arxiv.org/abs/2607.18368)

**<font color=#1a73e8>作者：</font>** Taewoon Kim, Vincent François-Lavet, Michael Cochez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Partially observable reinforcement learning requires deciding what to retain, retrieve, and forget over time. We introduce a neuro-symbolic meta-policy that learns which symbolic memory heuristic to apply at each decision point while keeping execution symbolic. Our setting uses temporal knowledge-graph memory in RoomKG, where hidden state and observations are represented as Resource Description Framework (RDF) graphs and memory is augmented with temporal RDF triple annotations. The model combines knowledge-graph encoding of memory contents with value heads for question answering, exploration, and forgetting, yielding a controller that is both adaptive and inspectable. This gives the work a direct Semantic Web grounding through RDF-based representation, annotation-compatible graph semantics, and graph-based symbolic operations over explicit memory state. On train/test room splits at long-term memory capacity of 512, the qualifier-aware StarE-GNN configuration achieves the best held-out performance among the compared symbolic, neural, and neuro-symbolic systems while preserving step-level traceability of memory-management decisions.

---


### 48. [Scalable and Efficient Joint Spiking Embedding Predictive Architecture for Large-Scale Dynamic Graphs](https://arxiv.org/abs/2607.18412)

**<font color=#1a73e8>作者：</font>** Huizhe Zhang, Yuchang Zhu, Huazhen Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic graph learning aims to capture evolving structural and semantic patterns in real-world systems, such as fraud detection and recommender systems. Due to the scarcity of labeled data in real-world dynamic graphs, recent studies have introduced generative or contrastive paradigms (e.g., masked graph autoencoders or graph contrastive learning) to generate task-agnostic graph embeddings. However, these methods typically rely on complex edge-level reconstruction objectives and tailored graph augmentation strategies. This incurs substantial computational overhead when scaling to large-scale dynamic graphs. In this paper, we propose SG-JEPA, a joint spiking embedding predictive architecture for large-scale dynamic graphs. In contrast to existing self-supervised methods, SG-JEPA partitions nodes into context and target sets along the temporal dimension to learn embeddings that are predictive of each other via additional spatial-temporal information. Furthermore, through encoding sequential inputs into coarse-to-fine spike count embeddings, spiking neurons enable SG-JEPA to adapt to the varying computational constraints of downstream tasks. Extensive experiments demonstrate that SG-JEPA achieves competitive or even superior performance over discriminative baselines on node classification, while effectively scaling to the dynamic graph with 13 million edges. SG-JEPA avoids the complex machinery (negative sampling, graph augmentations, edge-level reconstruction, etc.), resulting in superior training efficiency and memory scalability compared with prior self-supervised dynamic graph baselines.

---


### 49. [PAC--Bayes Bounds on Quotient Parameter Spaces: Geometry-induced Implicit-Bias Priors](https://arxiv.org/abs/2607.18422)

**<font color=#1a73e8>作者：</font>** Nicola Aladrah, Fabio Anselmi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Overparameterized models often have continuous parameter symmetries, so different parameters define the same predictor. We show that PAC--Bayesian analysis should be performed on the quotient predictor space: pushing a prior and posterior to the quotient preserves the empirical and population Gibbs risks while removing the nonnegative KL contribution caused solely by how the two distributions differ among parameterizations of the same predictor.
Quotienting alone does not determine which prior to use. We construct a canonical choice of one parameterization for each predictor and account for the geometric volume of its equivalent parameterizations. This transforms a neutral reference prior into a data-independent prior that reflects the model's implicit bias. It approximates the ideal but inadmissible posterior-matched prior, which would minimize the KL term by depending on the training data. The resulting certificate is tighter exactly when this geometry-induced prior has smaller KL divergence from the learned quotient posterior than the neutral prior.
We test this prediction in Fourier regression with a Hadamard parameterization and in Query-Key attention, using ordinary SGD without an explicit regularizer. The implicit-bias prior reduces the mean quotient-space KL by \(40.69\%\) and the mean PAC--Bayes certificate by \(21.40\%\) in the Fourier-Hadamard experiment. The smaller, prior-scale-dependent improvement in Query-Key attention confirms the predicted conditional nature of the effect.

---


### 50. [Adversarial Robustness of Phishing Email Detection: A Comparative Study of TF-IDF + Logistic Regression and Fine-Tuned DistilBERT](https://arxiv.org/abs/2607.18429)

**<font color=#1a73e8>作者：</font>** Tanveer Ahmed, Seyedali Pourmoafil  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing emails remain one of the most persistent cybersecurity threats, and machine-learning classifiers are widely used to detect them. Most reported detection accuracies, however, are measured on clean, in-distribution test data rather than on emails deliberately altered to evade detection. This paper reports a controlled, pairwise comparison of two phishing-detection approaches a TF-IDF + Logistic Regression baseline and a fine-tuned DistilBERT transformer trained on a unified corpus of 82,255 emails drawn from six public datasets and evaluated under three conditions: normal in-distribution, synthetic phishing, and adversarial phishing. Both models exceeded 98% accuracy on clean data yet degraded sharply under adversarial testing: TF-IDF + LR fell to 64.00% (a 34.59-percentage-point drop) and DistilBERT fell to 63.64% (a 35.40-percentage-point drop) a gap of only 0.36 percentage points, equivalent to a single email in the 275-sample adversarial test set. LIME, SHAP, and attention-rollout analysis indicate the two models relied on different evidence yet showed similar vulnerability. Pairwise error analysis shows the models agreed on 54.9% of adversarial samples but each made a similar number of exclusive errors (24 and 25 respectively), indicating partly complementary rather than identical failure modes. The results show that clean-data accuracy does not predict adversarial robustness, and that adversarial testing should be a standard part of phishing-detection evaluation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-241](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
