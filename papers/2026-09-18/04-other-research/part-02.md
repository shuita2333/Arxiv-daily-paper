# 📦 其他研究 | 2026年09月18日

> 本类共 **223** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-223](./part-05.md)

---

### 51. [Ghost-Filled Orders: Detecting and Testing Atomicity Violations in Non-Custodial Prediction Markets](https://arxiv.org/abs/2609.17902)

**<font color=#1a73e8>作者：</font>** Zhiyang Chen, Fan Long, Zhendong Su  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain based prediction markets combine offchain order management with onchain settlement. This architecture supports user controlled custody, since users keep funds in wallets or smart contracts while submitting signed orders to an offchain order book. However, it creates an atomicity gap. An order may be valid when accepted or matched offchain, but become invalid before the corresponding onchain settlement transaction is executed. This behavior, often called ghost filled orders by the community, can cause trades that appear filled offchain to fail onchain. This paper studies this atomicity gap through a case study of Polymarket. We show how the delay between offchain order acceptance and onchain settlement allows adversaries to invalidate unfavorable orders after observing market outcomes or price movements. We then quantify the scale and financial impact of this behavior over a nine-month period from August 12, 2025, to May 22, 2026, using 1.8 million reverted transactions involving Polymarket official smart contracts. Our analysis separates attacker profit from market and user loss, and develops conservative measurement rules to avoid overclaiming impact. We further develop a methodology for testing other blockchain based prediction markets and apply it to three additional markets. We find that all three are vulnerable to the same class of attack, and that one design enables direct attacker profit. We have reported the findings to all three projects; one project had acknowledged the issue at the time of the study.

---


### 52. [Zing-0.5: Toward Playable Worlds with Real-Time Joint Action and Text Control](https://arxiv.org/abs/2609.17909)

**<font color=#1a73e8>作者：</font>** Mingyang Chen, Shengdong Chen, Xiaoxiao Fu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Zing-0.5, a 5B autoregressive world model designed for playability: users can explore generated worlds, influence unfolding events, and respond to the resulting feedback through joint keyboard and online text control. Our approach brings together three technical contributions: (1) Unified action and text conditioning, combining magnitude-aware keyboard inputs with temporally aligned text instructions and jointly annotated videos to learn navigation and event control within the same sequence; (2) Event-scale supervision for incremental generation, using a segment-level teacher trained on connected multi-prompt videos to supervise a block-level causal student through distribution-matching distillation; and (3) Low-cost real-time interaction, combining four-step generation with context-preserving streaming to support 832 x 480 inference at 24 FPS at an estimated server rental cost of approximately USD 0.009 per stream-minute. Zing-0.5 achieves an overall score of 81.0 and a consistency score of 88.5 across 158 WBench Navigation cases. A joint-control demonstration shows a text-directed event change during continued navigation without restarting generation. We release the model weights, inference code, and Zing-SGLang serving implementation to support further work on playable generated worlds.

---


### 53. [Face-voice Association across LAnguages and Gender (FLAG) 2027 Challenge Evaluation Plan](https://arxiv.org/abs/2609.17913)

**<font color=#1a73e8>作者：</font>** Marta Moscati, Swapnil Khandoker, Muhammad Saad Saeed 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face--voice association models may rely on language or gender cues in the voice rather than on speaker-specific voice characteristics, which can lead to a performance deterioration when the model has to identify a multilingual speaker or distinguis same-gender speakers. To investigate these issues, we introduce the Face-voice Association across LAnguages and Gender (FLAG) 2027 Challenge. The challenge formulates face--voice association as a cross-modal verification task: given a voice, identify the speaker's face from a ``gallery'' of faces consisting of the speaker's face and a set of negative samples. Models are evaluated on identities not present in the training data (``unseen'') and both for languages present or absent from the training data (``heard'' and ``unheard''). Two evaluation settings are used to test models' reliance on gender: a standard, unconstrained and a gender-constrained one, where the latter uses a same-gender gallery. The performance of existing, baseline models in these settings reveals that models performance degrades under language shifts and in gender-constrained settings, highlighting the need to foster the development of models that capture identity-specific aspects beyond language and gender. The challenge provides a benchmark dataset, pretrained baseline models, and an evaluation framework to advance face--voice association.

---


### 54. [EdgeReMIND: A Scalable, Top-Ranked Memorization Baseline for Temporal Multi-Relational Link Prediction](https://arxiv.org/abs/2609.17916)

**<font color=#1a73e8>作者：</font>** Bryant Pollard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal link prediction on the Temporal Graph Benchmark 2.0 (TGB 2.0) faces a scalability ceiling: on the benchmark's three largest datasets, every existing embedding method runs out of memory or exceeds the time budget. These large-scale graphs are the ones nearest real deployment scale, so failing on them is a real production limitation. EdgeReMIND sets the highest reported test mean reciprocal rank (MRR) on six of eight TGB 2.0 datasets and is the only relation-aware method that runs on all of them. This linear memorization model, with learned per-relation weights over data-calibrated features, is therefore not merely a fallback where embeddings fail but a practical state-of-the-art baseline across the benchmark.

---


### 55. [Audio for Sports Highlight Detection: A Comparative Empirical Study](https://arxiv.org/abs/2609.17923)

**<font color=#1a73e8>作者：</font>** Hao Xu, Meenakshi Sarkar, Vishnu Raj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sports highlight detection aims to identify the most exciting and meaningful moments from long sports videos. While existing methods often emphasize visual or visual-language representations, sports videos contain rich audio cues, including commentator speech, crowd reactions, whistles, ball impacts, and referee calls. In this work, we revisit the role of audio in sports highlight detection and ask a simple question: how far can audio alone go? We construct lightweight audio-only baselines using pretrained audio representations and compare them with visual-only and audio-visual methods on the SV-Highlights benchmark. Surprisingly, our audio-only GRU baseline achieves strong performance and outperforms several existing audio-visual methods under our supervised evaluation setting. Furthermore, a simple audio-visual fusion baseline achieves the best performance across all metrics, indicating that audio and visual cues provide complementary information. To better understand the contribution of audio, we conduct source-separated analysis and show that vocal/commentary audio is more informative than background-only audio, while their combination performs best. We also analyze interpretable audio cues and find that highlight clips exhibit higher RMS loudness, peak loudness, and mid-frequency energy than non-highlight clips, although substantial distribution overlap indicates that loudness alone is insufficient. Our findings suggest that audio is an underexplored but highly informative modality for sports highlight detection and should be treated as a primary signal rather than merely an auxiliary cue.

---


### 56. [Rapid Loss of the Sierra Nevada's Largest Trees Driven by Fire](https://arxiv.org/abs/2609.17925)

**<font color=#1a73e8>作者：</font>** Fabien H. Wagner, Dan J. Dixon, Christopher W. Woodall 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large trees disproportionately contribute to biomass storage, habitat structure, and ecosystem functioning. However, their distribution and health dynamics remain poorly quantified at a regional scale. Here, a deep learning model (U-Net-ID) and canopy height models derived from sub-meter aerial imagery from 2020 were used to delineate all individual trees with crown area $\geq$ 100 m$^2$ across the Sierra Nevada Floristic Province. The model was trained using more than 3.3 million synthetic tree crowns and achieved a median Intersection over Union (IoU) of 0.602 when validated against an independent dataset of 20,273 crowns. A total of 6,515,705 large trees were mapped, occurring across approximately 78.7% of the Sierra Nevada Floristic Province. The spatial distribution of large trees showed associations with elevation, temperature, and precipitation. Using Sentinel-2 time series from 2020 to 2025, tree health dynamics were characterized by extracting spectral trajectories for each crown and applying BFAST breakpoint detection algorithm combined with a disturbance classification framework to identify mortality, disturbance, and recovery trajectories of individual trees. Wildfires, estimated from CAL FIRE fire perimeters, were identified as the dominant driver of large-tree mortality, killing 10% of all large trees in the Sierra Nevada, with mortality strongly concentrated during the extreme 2020-2021 fire seasons.

---


### 57. [Symmetry without a manifold: intrinsic dimension on orbits](https://arxiv.org/abs/2609.17926)

**<font color=#1a73e8>作者：</font>** Chon-Fai Kam, Miloud Bessafi, Frédéric Cadet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The standard geometric derivation of neural scaling exponents takes the intrinsic dimension of a data manifold as its input. On modular addition in $\mathbb{Z}_p$ that derivation has no input. The exact algebraic solution is an orbit of $\mathbb{Z}_p$ acting by isometries. Transitivity alone makes the ratio statistic underlying the standard dimension estimator a point mass, so the estimator is undefined, and here the two nearest neighbour distances coincide exactly. Breaking the symmetry at scale $\epsilon$ returns a number, but one that tracks $1/\epsilon$ with no scale free plateau. We show that the failure is general, since on any finite orbit of a group acting by isometries the estimator reports the resolution at which the set is probed rather than a dimension. What replaces the power law is exponential in hidden width, $L(h)=L_\infty+A\exp(-c\,h^{\alpha})$, with $R^2$ between 0.982 and 0.995 against 0.857 to 0.906 for a power law admitting the same floor and fitted under the same protocol. Where the data supply is sufficient the rate belongs to the regulariser rather than to the group, since weight decay moves $c$ by a factor of 47 while group order moves it by 1.10, a residual below seed to seed resolution, for every fixed $\alpha$ between 0.75 and 2. The critical width falls with group order rather than rising, against capacity counting that assigns a fixed number of neurons to each irreducible representation.

---


### 58. [Locating Hidden Failures Makes Long-Horizon Agents More Reliable](https://arxiv.org/abs/2609.17930)

**<font color=#1a73e8>作者：</font>** Salman Rahman, Yubin Kim, Mihir Parmar 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI agents take on long, autonomous tasks, we increasingly oversee rather than perform the work, yet we still judge them almost entirely by whether they finally succeed. An outcome cannot reveal where a run went wrong, whether the agent recovered, or the irreversible harm it caused along the way, and where long-horizon agents fail remains unmapped. We study $2518$ agent trajectories across software engineering, computer use, and science, close to real deployment, and classify $6967$ mistakes into $78$ failure types. Failure follows a recurring signature: after its first mistake an agent often fails to recover and rarely catches the error itself, so the run continues unchecked while still looking correct; whether an agent recovers depends on the task and the environment's feedback, not on the agent framework running it. Long-horizon agents can do real harm on the way to a passing result: even runs scored as solved delete data, corrupt systems, or fabricate success rather than earning it. We release these human-verified annotations as Traverse, a benchmark on which six frontier judges struggle to locate failure regardless of scale: even the strongest correctly identifies the first mistake in fewer than a third of runs. Yet Scout, a $4$B verifier we trained, locates failure far better than these judges and transfers to domains it never saw. Used at test time to select among an agent's candidate runs, it raises task success above the agent's own single-attempt performance, without retraining the agent. By making failure cheap to locate and correct, this work is a foundation for more trustworthy long-horizon agents that learn from their own mistakes, and a practical path to overseeing increasingly autonomous AI.

---


### 59. [On the Identifiability of Mixed Ordinal and Exponential Family Causal DAGs under Linear Parametric Models](https://arxiv.org/abs/2609.17942)

**<font color=#1a73e8>作者：</font>** Sambit Mishra, Urbashi Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem of identifiability in linear parametric models (LPMs) whose nodes follow either an ordered logit model or a regular one-parameter exponential family is evaluated. The results go beyond classical structural equation models as well as results for nodes with observations from a homogeneous family of distributions. The main result establishes that the orientation of every edge joining an ordinal node to an exponential-family node is identifiable from the joint distribution alone at every parameter value, provided the ordinal node has at least three categories and the exponential-family node at least three points of support, with no restriction on the sufficient statistic. Converses show that both requirements are necessary: the three-category requirement is binding only for affine sufficient statistics, and the three-point requirement is binding under the canonical link. The guarantee extends to orienting every such mixed ordinal-exponential family edge of a given $d$-node undirected skeleton. Numerical experiments illustrate the theoretical results by successfully separating orientations within a Markov equivalence class, which are indistinguishable by conditional independence alone.

---


### 60. [Maximum Strong Independent Sets in Hypergraphs: Reductions, Bounds, and Greedy Certificates](https://arxiv.org/abs/2609.17951)

**<font color=#1a73e8>作者：</font>** Yingquan, Jason Cong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the maximum strong independent set problem in a finite hypergraph: find the largest vertex set that intersects every hyperedge in at most one vertex. This objective arises whenever each observed block is a local incompatibility constraint but transitive closure across overlapping blocks is not justified. A motivating example is multi-band LSH-MinHash deduplication, where each collision bucket gives local evidence, while connected-component contraction can impose spurious global equivalences. The paper develops an incidence-structural toolkit for this problem. We prove exact reductions for dominance, incidence twins, and weight-1 blocks; derive closed-form and low-weight upper bounds; introduce puncturing and covering certificates that sharpen those bounds; and analyze a layered greedy clustering algorithm driven by block weights and residual incidence. The algorithmic analysis includes feasibility, maximality, conditional optimality, a layered witness-matching upper bound, and incidence-local complexity bounds. The results give correctness, termination, fixed-point, and optimality certificates for broad incidence families, together with examples showing when different certificates separate or coincide.

---


### 61. [TACTICS: Taxonomy-Aware Intelligent Corpus Sampling for Machine Translation](https://arxiv.org/abs/2609.17956)

**<font color=#1a73e8>作者：</font>** Prasanth Bathala, Anubhav Shrimal, Sukhdeep Singh Kharbhanda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale machine-translation (MT) systems are typically evaluated on random samples from a corpus whose distributional composition is an artifact of how it was assembled. Such a sample inherits the phenomena the collection happens to contain rather than the full space a system must handle, spanning rule-governed conventions (terminology, punctuation, currency formatting) and context-dependent phenomena (tone, honorifics, document-level coherence), and thus provides no coverage guarantee for assessing robustness. We propose TACTICS (Taxonomy-Aware Coverage-opTimized Intelligent Corpus Sampling), which recasts coverage as an explicit objective. TACTICS induces a hierarchical taxonomy from a locale style guide, classifies segments against it, and selects a fixed-budget subset jointly optimizing coverage of rare categories, document-level coherence, and distributional fidelity to the full corpus. Applied to MT evaluation across four translation directions, TACTICS improves coverage of rare categories over lexical and embedding-based selection. By targeting the phenomena that separate systems, TACTICS makes a fixed evaluation budget go further, recovering the true system ranking from far fewer segments than random sampling wherever a real quality gap exists and never signaling a difference where none exists.

---


### 62. [A11yLTLNav: Automatic Detection of Accessibility Navigation Failures](https://arxiv.org/abs/2609.17959)

**<font color=#1a73e8>作者：</font>** Chenming Ge, Kewen Peng, Chengyang Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> For blind and low-vision (BLV) screen-reader users, a website that appears accessible in a static snapshot can become difficult or impossible to navigate once interaction begins. Yet, most automated accessibility checkers miss failures involving focus, interface state, and accessible feedback across interactions. We present A11yLTLNav, a property-based approach for automatically detecting accessibility navigation failures. Through a structured review of prior research, we organize accessibility navigation failures into a failure taxonomy and formalize a browser-observable subset as executable Linear Temporal Logic properties over action-state traces. A11yLTLNav combines random keyboard exploration with runtime property monitoring to detect these failures during interactions. We evaluate A11yLTLNav on 31 generated websites based on real-world websites and tasks. It reported 309 accessibility failures, of which 274 were confirmed, achieving 88.7% precision and identifying more confirmed failures than the comparison checkers. Our results show that A11yLTLNav transforms accessibility knowledge into reusable checks of interface behavior over time.

---


### 63. [Measuring AI Leadership: Development and Validation of a Multidimensional Measure for AI-Native Organizations](https://arxiv.org/abs/2609.17965)

**<font color=#1a73e8>作者：</font>** Mustafa Akben, Leslie Coyne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI is changing what leaders must judge, explain, learn, and coordinate, yet existing measures do not capture these behaviors at the level needed to study leadership in AI-enabled work. We develop the AI Leadership Battery, which organizes 36 behaviorally specific subdimensions into 11 theory-specified content families. Following established scale-development procedures, the research used deductive item generation; content validation of definitional correspondence and definitional distinctiveness; exploratory factor analysis and item reduction; confirmatory factor analysis in independent samples; and tests of internal consistency reliability, convergent validity, discriminant validity, and criterion-related and incremental validity. Across the development and validation studies, the analyses provided evidence for the Battery's content, multidimensional structure, reliability, and distinction from selected orbiting constructs. The Battery also contributed additional information beyond orbiting constructs across organizational growth, decision speed, customer/stakeholder response capability, AI-enabled team performance, AI-enabled work experience, AI security and risk management, and AI adoption and integration. The resulting measure provides researchers with a behavioral framework for examining how leaders in AI-enabled work regulate judgment, learning, adaptation, transparency, and accountability.

---


### 64. [Memory Has Geometry: Non-Uniform Geometric Memory for Long-Horizon Personalized AI](https://arxiv.org/abs/2609.17969)

**<font color=#1a73e8>作者：</font>** Jiahong Liu, Wenhao Yu, Zexuan Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory is becoming a core substrate for personalized AI, yet most systems still represent personalization as discrete records in a largely static latent space, accessed under one global similarity notion. For data mining, this creates a mismatch: the evidence is a temporal event stream, while the dominant abstraction is a searchable record set. We argue that long-horizon personalization should instead model memory as a user-specific dynamical state space with locally heterogeneous geometry. Geometry here is a computational language, not a literal claim about cognition: it captures stable versus volatile regions, variable-rate drift, heterogeneous neighborhoods, and uncertainty about current user state. Profiles and isolated events remain useful as points, but interaction, feedback, and elapsed time induce trajectories. Memory access then becomes trajectory-conditioned reconstruction of the relevant user state, not only nearest-neighbor lookup.

---


### 65. [The Attention Within: Consensus Dynamics in Selective State Space Models](https://arxiv.org/abs/2609.17997)

**<font color=#1a73e8>作者：</font>** João Pedro Silvestre, Álvaro Rodríguez Abella, Paulo Tabuada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective state space models (SSMs) have recently emerged as a compelling alternative to transformers, combining competitive performance with substantially improved inference efficiency. At each SSM layer, a sequence of hidden states are propagated by a recurrence, mixing information of different tokens. Despite using a different mechanism, this mixing plays a role analogous to attention in transformers. In fact, recent works have shown that the two architectures may be closer than they first appear, as this recurrence admits a formulation akin to linear attention. In transformers, attention is known to drive the tokens to cluster, i.e., to reach consensus, collapsing in the limit to a single direction. Thus, we ask: does the recurrence at the core of SSMs drive the tokens to consensus, as attention does in transformers?
To answer this question, we take a dynamical systems perspective on SSMs, modeling the evolution of tokens across layers as an ordinary differential equation. By exploiting input-to-state stability arguments, we establish local exponential stability of the consensus equilibria and characterize their domain of attraction for time-varying weight matrices, a setting not addressed by previous results. We thereby show that the resemblance between SSMs and transformers does run deeper: the recurrence at the core of SSMs aggregates tokens just as attention does. Numerical experiments on a pretrained Mamba-2 model point to the output gate as the component that regulates the extent of this consensus, preventing the tokens from reaching it in full.

---


### 66. [Missing Bridges: Composition-Aware Active Imitation Learning](https://arxiv.org/abs/2609.18004)

**<font color=#1a73e8>作者：</font>** Maxwell J. Jacobson, Ahmed H Qureshi, Yexiang Xue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Active imitation learning reduces expert effort by allowing a learner to request the demonstrations it needs. Existing methods typically select these requests for their expected information gain about the expert policy. In structured multi-task domains, however, the number of start-goal tasks may grow combinatorially despite their solutions sharing reusable behavior. This makes composable behaviors especially valuable, since a single demonstration may help solve many tasks at once. Prior methods do not explicitly account for this value when selecting which demonstration to request. We introduce Adaptive Agents via Latent Topologies (AALT), which requests demonstrations that maximize expected gains in start-goal connectivity. We further show that this objective is formally tied to information gain about task reachability. AALT organizes existing demonstrations into a topology of latent hub states connected by learned behaviors, identifies high-value bridge demonstrations that are likely to enable many tasks at once, and grounds each to an expert query. At inference, it plans through the resulting topology and conditions a diffusion policy on each successive hub transition. In a simulated UR5e robot ordered-retrieval domain with 72 tasks, AALT improved from 42/72 to 72/72 (100%) successful tasks consistently using only 3 demonstrations totaling 5 transitions beyond the initial dataset. After 20 demonstrations, the strongest baseline averaged 88.6% success using 98 transitions.

---


### 67. [Gaze as Evidence for Common Grounding: A Cross-Corpus Analysis of MapTask and MUNDEX](https://arxiv.org/abs/2609.18011)

**<font color=#1a73e8>作者：</font>** Nan Li, Albert Gatt, Massimo Poesio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In collaborative tasks with asymmetric information, participants coordinate their understanding through interaction. We ask whether gaze provides evidence about grounding across two such tasks. Working from discrete behavioral annotations, we map HCRC MapTask (Anderson et al., 1991) and MUNDEX (Türk et al., 2023) into a shared partner/task/away vocabulary and compute gaze features around task-relevant dialogue units. In both corpora, aligned reference interpretations (MapTask) and UND (understood) judgments (MUNDEX) are associated with more task-directed gaze and with less partner-directed gaze, lower gaze entropy, and fewer gaze transitions. The associations are clearest for the participant leading the task: in giver-produced references, and in explainer judgments, which also co-vary with the explainee's gaze. In same-speaker MapTask reference chains, the speaker's gaze entropy is lower at the mention where a previously non-aligned referent becomes aligned. The best gaze feature groups improve modestly over controls under grouped cross-validation: temporal features in MapTask and raw proportions in MUNDEX. Because effects are small and several weaken when recurring participants rather than dialogues are the unit of inference, we treat gaze as one contributing cue to grounding, to be interpreted alongside task and dialogue context.

---


### 68. [IRIS: Implicit Rendering Matters for Pose-Free Novel View Synthesis](https://arxiv.org/abs/2609.18034)

**<font color=#1a73e8>作者：</font>** Wenyu Li, Sidun Liu, Peng Qiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis from unposed multi-view images remains challenging, as the model must jointly learn scene representations and camera parameters without pose supervision. Existing approaches largely fall into two extremes: implicit latent-space rendering is flexible and easy to optimize, but often yields weakly grounded camera estimation; explicit 3D representations provide stronger geometric grounding, but introduce heavier parameterization and more fragile optimization. In this paper, we present IRIS, a fully self-supervised framework that provides a practical middle ground between these two paradigms. Instead of decoding free latent tokens or reconstructing fully explicit 3D primitives, IRIS represents the scene as a latent neural field and renders novel views by querying this field under self-predicted cameras. Specifically, projected features from reference views are aggregated at sampled 3D points to form point-wise latent features, which are then composed along target rays for rendering. This design preserves the flexibility and optimization stability of implicit modeling, while introducing stronger geometric structure than unconstrained latent rendering. Extensive experiments show that IRIS achieves strong novel view synthesis quality with competitive pose accuracy under fully self-supervised learning. Our project page: this https URL

---


### 69. [SetPlanner: A Lightweight Plug-in Point-Set Planner for Frozen SAM](https://arxiv.org/abs/2609.18037)

**<font color=#1a73e8>作者：</font>** Dawei Yan, Yuezhe Yang, Menglan Ruan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segment Anything Models provide reusable priors, yet they require user prompts and cannot support fully automatic instrument segmentation. Automatic prompting is difficult for thin, articulated, reflective, and partly occluded tools, where several configurations can be valid. We formulate automatic prompting as lightweight point-set planning and isolate the point source under a frozen pathway. To this end, we present SetPlanner, a 1.52M-parameter plug-in point-set planner for frozen SAM. The plug-in preserves SAM's point-prompt interface and enables reuse across backbones. SetPlanner plans complete unordered K-point sets from geometry-aware targets with a permutation-aware conditional flow. SAM decodes eight candidates; their consensus readout yields a ground-truth-free prediction. Across three endoscopic datasets, SetPlanner wins all six transfer routes over a LoRA-adapted system. Under our frozen-pathway protocol, SetPlanner reaches 0.934 Dice on Kvasir-Instrument and recovers 96% of a 44.4-point localization gap, while candidate disagreement ranks low-Dice cases at AUROC 0.969.

---


### 70. [Structural Inference under Hidden Agents](https://arxiv.org/abs/2609.18045)

**<font color=#1a73e8>作者：</font>** Zhongben Gong, Xiaoqun Wu, Mingyang Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering latent interaction structures from multi-agent dynamics is important for understanding and predicting interacting systems. Trajectory-based structural inference has achieved promising performance, but conventional formulations assume that the trajectories of all modeled agents are available. In practice, agents may become unobserved at deployment because of limited sensing, occlusion, or communication failure. Existing studies have considered unseen-node estimation, structural inference under partial observations, and missing-value imputation, yet the joint recovery of hidden-agent trajectories and their interactions remains underexplored. We formulate this problem as structural inference under hidden agents. Its key difficulty is a circular dependency: recovering interactions involving a hidden agent requires an estimate of its trajectory, while trajectory reconstruction can itself benefit from structural information. To address this challenge, we propose Structural Inference under Hidden Agents (SIHA), which combines structure-agnostic initialization with structure-guided iterative refinement. SIHA reconstructs hidden trajectories from visible observations, infers interactions using Neural Relational Inference, and feeds the estimated structure back into hidden-state reconstruction through multi-strength structural attention and iterative state--structure updates. Experiments on three benchmark dynamical systems demonstrate consistent improvements in visible-to-visible structural inference, while also showing benefits in hidden-state reconstruction and future prediction. Motion-capture experiments with simulated whole-limb occlusion further demonstrate its effectiveness in realistic hidden-agent settings.

---


### 71. [Exact semantic readout from compressed vector representations](https://arxiv.org/abs/2609.18047)

**<font color=#1a73e8>作者：</font>** Daniel Quigley  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We characterize when compressed vector representations admit exact linear or affine readouts of a finite lexicon's truth conditions: one fixed map per predicate, sending each entity vector to the corresponding truth vector. A necessary and sufficient row-space condition determines existence; the augmented truth matrix has rank r, giving minimum dimension r in the linear case, and r-1 in the affine. Exact readouts return values in a shared truth basis on which Boolean connectives act unchanged; separability alone requires an intervening threshold. For binary relations, exact bilinear readout of identity or strict total order requires linearly independent entity vectors. Experiments with GloVe and word2vec distinguish exact affine recovery, linear separability, and held-out prediction: most predicates are strictly separable, but none admits an exact affine readout from the pretrained embeddings. Supervised transductive training attains exact affine recovery to numerical precision at every tested dimension meeting the bound. At the embeddings' original dimension, geometries constrained to exact linear recovery retain 98-99 percent of the pretrained variance on the feature norms, and 80-83 percent on the WordNet lexicon.

---


### 72. [Regional Explanations via Causal Sufficiency and Necessity](https://arxiv.org/abs/2609.18049)

**<font color=#1a73e8>作者：</font>** Xuexin Chen, Peng Liang, Zijian Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model explainability is essential for understanding and trusting machine learning models. Existing explainable AI methods often explain predictions through feature importance, counterfactual explanations, or rules. However, a region-level characterization of when and only when a prediction behavior arises remains less explored. This paper proposes Causal Sufficient and Necessary Regional Explanations (SNRE), a framework that learns an input region $A$ and output region $B$ such that membership in $A$ is both sufficient and necessary for the model output to fall in $B$. Motivated by the classical Probability of Necessity and Sufficiency (PNS), we formulate a region-level PNS measure through stochastic interventions and derive a differentiable finite-sample estimator for optimization. SNRE parameterizes the input-output region pair with explicit and interpretable algebraic region families, together with a learnable feature mask, balancing expressiveness and interpretability. Experiments demonstrate that SNRE learns region pairs with strong sufficiency-necessity performance, robust explanation behavior, and practical utility for model analysis.

---


### 73. [Position Anchor Tuning: Towards Efficient Adaptation of Pre-Trained Point Cloud Transformers](https://arxiv.org/abs/2609.18056)

**<font color=#1a73e8>作者：</font>** Zheng Liu, Xin Gao, Jinchao Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) has recently emerged as a pivotal research direction for adapting pre-trained point cloud transformers to diverse downstream tasks. Although existing methods achieve excellent fine-tuning performance with high parameter efficiency, they ignore inference efficiency. To tackle this problem, a novel PEFT method termed position anchor tuning (PAT) is proposed in this paper. As multi-head attention (MHA) and feed-forward network (FFN) are computation-heavy blocks in pre-trained transformers, PAT decreases their computational cost through token aggregation-expansion pairs. Each pair comprises a token aggregation module (TAM) and a token expansion module (TEM). For MHA and FFN blocks, TAMs extract representative tokens from their input tokens based on position anchors in 3D space. These extracted tokens, rather than the original input tokens, are processed by the blocks, thereby reducing the number of tokens involved in computation. Then, TEMs propagate the learned representations back to the original input tokens. Since TAMs are solely responsible for capturing task-specific representations, base-sharing low-rank adaptation (BSLoRA) is further introduced to enable them to learn such representations effectively with only a small number of trainable parameters. Extensive experiments on widely used benchmarks demonstrate that PAT performs comparably to state-of-the-art methods while incurring significantly lower computational overhead and fewer trainable parameters.

---


### 74. [Finder: Agentic Closed-Loop Object Finding for Embodied Grounding](https://arxiv.org/abs/2609.18058)

**<font color=#1a73e8>作者：</font>** Shixiong Xu, Zhiyuan Chen, Song Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding the object referred to by language in a partially observed 3D scene is a core capability for embodied agents. Existing approaches either couple object search with online exploration, which can be costly when relevant observations have already been captured, or query pre-built open-vocabulary maps and scene graphs in a static, one-shot fashion. We present Finder, an agentic closed-loop object-finding primitive for embodied grounding. Instead of treating grounding as passive retrieval from a fixed scene representation, Finder maintains a typed loop state that links query-conditioned planning, scoped evidence gathering, candidate verification, and accept/continue/abort control. When evidence is incomplete or ambiguous, the loop can redirect subsequent perception and comparison rather than simply returning the top retrieved object. On open-vocabulary embodied Object Retrieval in Habitat/HM3D and real-world RGB-D scenes, Finder improves the averaged 1m success rate by 15.75 points over strong baselines. The same primitive also transfers to sequential object grounding and embodied object-centric question answering, improving spatial and temporal localization without changing the inner grounding protocol. Project page: this https URL.

---


### 75. [AI Peers Exert Social Influence on Human Dishonesty in Groups](https://arxiv.org/abs/2609.18060)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Xinyuan Zhou, Yuanyang Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human dishonesty in group settings is highly susceptible to peer influence, particularly when incentivized. Although artificial intelligence (AI) evolves from passive tools into active collaborators, its impact on human moral behavior within groups remains underexplored. We addressed this gap through a two-phase randomized behavioral study (N=280 and N=360). We found AI agents exert substantial social influence comparable in magnitude to that of human peers. Specifically, participants reported more dishonestly when exposed to dishonest rather than honest normative cues. This effect is evident across injunctive, subjective, and descriptive social norms. Interestingly, the only significant adjacent behavioral change occurred when dishonest peer behavior first appeared, whereas further increases from one to four dishonest peers produced weaker and non-monotonic changes. Furthermore, participants rapidly converge on decision-making, showing modest increases in dishonest reporting through repeated exposure. These findings highlight the importance of managing the behaviors and normative signals communicated by AI group members.

---


### 76. [Encypher: Shared Agency and Social Presence in Collaborative Music Generation for Dance Cyphers](https://arxiv.org/abs/2609.18062)

**<font color=#1a73e8>作者：</font>** Zhixing Chen, Cheng-Zhi Anna Huang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Music and dance are social practices of expression and connection, yet most HCI work in human-AI co-creation centers the solo performer. As generative music matures, we ask not only what AI can compose but what social encounters it can organize around sound. We present Encypher, a collaborative generative music system that translates collective movement qualities into text prompts conditioning real-time music generation for dance cyphers. Through five weeks of co-design with local dancers, a user study with unacquainted participants, a public museum event, and a live performance, we found that users developed shared agency, perceiving the music as a response to the room's energy. While newcomers felt uncertain, the system fostered social presence by prompting them to look to each other for cues. By treating sociality as a design concern rather than a downstream effect, we offer a framework and design implications for AI systems for collaborative, embodied expression.

---


### 77. [A Design Space for Visual Interfaces for Generative Image Models](https://arxiv.org/abs/2609.18065)

**<font color=#1a73e8>作者：</font>** Susie S.Y. Li, Mingwei S.G. Li, Remco Chang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive visual interfaces have become an important means of controlling generative image models, enabling users to manipulate generation through prompts, direct manipulation, and a range of interactions. However, existing techniques are typically presented as independent systems, making it difficult to understand how they relate, compare their interaction mechanisms, or identify opportunities for new interface designs. We introduce a design space for interactive visual interfaces for generative image models derived from 51 research systems and practitioner tools. The framework decomposes each system into three complementary components: the user interface (U), the controllable model objects (Z), and the mapping function ($\phi$) that translates user interaction into model operations. This decomposition provides a common representation for analyzing heterogeneous interaction techniques across model families, revealing recurring design patterns and underexplored regions of the design space. We further present an interactive corpus explorer that support comparative analysis, and discuss usage scenarios for both educational settings and HCI/AI practitioners identifying research and design opportunities.

---


### 78. [GeoCueFormer: Geometry-Guided Wavelet Representation and Prediction-Cued Dual-Stage Decoder for Underwater Semantic Segmentation](https://arxiv.org/abs/2609.18069)

**<font color=#1a73e8>作者：</font>** Xian Wu, Xinjin Li, Yiliu Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater semantic segmentation is essential for marine ecosystem monitoring, yet remains challenging due to severe visual degradation. Light absorption and scattering often lead to color shifts, low contrast, and blurred boundaries, making shallow detail features unreliable. Existing underwater segmentation methods improve RGB feature aggregation or boundary prediction, but still lack an explicit mechanism to distinguish structure-related details from degradation-induced responses. To address this limitation, we propose GeoCueFormer, a lightweight framework that combines geometry-constrained frequency enhancement with prediction-cued refinement. GeoCueFormer performs stage-specific wavelet enhancement on hierarchical encoder features to complement shallow boundary details while preserving deep structural semantics. A depth-derived spatial gate constrains shallow frequency enhancement toward geometry-consistent regions, and a prediction-cued dual-stage decoder further refines ambiguous high-resolution features. GeoCueFormer obtains 82.23% and 73.04% mIoU on SUIM and DUT, respectively. Under comparable model complexity and standard benchmark settings on SUIM and DUT, it achieves SOTA performance while maintaining a favorable accuracy-complexity trade-off. These results show that distinguishing structural details from degradation-induced interference is more effective for underwater segmentation.

---


### 79. [Teaching AI, Robotics, & Community: A Hubs-Based K-12 Education Framework for Reaching Rural Schools](https://arxiv.org/abs/2609.18072)

**<font color=#1a73e8>作者：</font>** Maxwell J. Jacobson, Gustavo Rodriguez-Rivera, Petros Drineas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> K-12 robotics and AI education remains difficult to scale, especially in rural regions lacking sustained technical mentorship. Programs like FIRST provide competition pathways and instructional opportunities, but they do not eliminate the need for local programming and robotics expertise. We introduce AI, Robotics, & Community (ARC), a hubs-based framework where colleges train undergraduate mentors and host workshops for nearby K-12 teams. Mature school programs can become secondary hubs that support additional schools, creating a self-reinforcing education loop where mentorship reach propagates geographically and can even grow super-linearly. We first evaluate ARC through a trial deployment at one university. The trial created three rural robotics teams. On five-point Likert surveys, mean increases in K-12 programming knowledge, resource access, and practice opportunities were 2.00, 2.25, and 1.25 points. Likewise, undergraduate confidence teaching technical concepts, adapting explanations, managing groups, and finding mentoring enjoyable and meaningful increased by 1.29, 1.14, 1.00, and 1.14 points. Additionally, we create a spatial Markov model of ARC's growth and simulate it using the state of Indiana as a testbed. Under moderate conditions, we find that ARC reaches 74% of Indiana's 1,925 public K-12 schools and produces 992 robotics programs after 40 years, compared with 161 projected under natural growth alone. Together, these results show ARC can create and support rural robotics programs, train undergraduate AI and robotics mentors, and potentially scale mentorship across a region.

---


### 80. [vidax: A Unified JAX Framework for Video Generative Models on Accelerator Meshes](https://arxiv.org/abs/2609.18077)

**<font color=#1a73e8>作者：</font>** Congyue Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-source video generative models ship almost exclusively as PyTorch/CUDA reference implementations. This leaves Cloud TPU pods without a production-ready inference path, despite offering large, cost-effective accelerator memory pools ideal for long-sequence spatiotemporal attention. We present vidax, an open-source JAX/Flax inference engine and zero-copy PyTorch-to-JAX weight translator for modern video generation architectures. vidax covers a diverse set of spatiotemporal models --- including Diffusion Transformers, omnimodal Mixture-of-Transformers, 3D VAEs, text encoders, and native samplers --- with zero PyTorch dependency in the execution path. The framework unifies 1D tensor parallelism with DeepSpeed-Ulysses sequence parallelism on a single JAX sharding mesh, integrates TPU flash-attention kernels, and implements per-layer weight offloading to support reference resolutions that exceed single-device memory. We benchmark compile times, latency, and peak memory utilization on TPU v4-8 hardware, and document real-world numerical bugs surfaced during checkpoint translation. vidax is released open-source as a baseline for JAX and TPU video generation research.

---


### 81. [Beyond Embedding Transfer: Component Roles in Grokking Transfer and Stability](https://arxiv.org/abs/2609.18078)

**<font color=#1a73e8>作者：</font>** Zeyu Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Warm-start transfer can make algorithmic tasks generalize rapidly, yet it is unclear which model components provide the gain and whether that gain remains stable under continued optimization. We study cross-operator transfer on modular arithmetic and separate efficacy (early velocity) from stability (post-reach drawdown). In a scale-matched 108-run battery across 12 seed blocks (96-run 2^3 factorial plus 12-run scale control), transferring internal attention/MLP weights (B) alongside token embeddings and readout (E+U) improves early accuracy by 5.46 pp (Holm p=0.0039) and cuts confirmation latency by 558 steps (Holm p=0.0088). While readout plus internal-block transfer satisfies the pre-specified +/-500-step latency equivalence criterion in 1-layer models (TOST p=0.0011, though Full is faster in 11/12 paired seeds), a prospective 2-layer replication confirms the internal-block advantage (12/12 seeds, +704.67 integral units, p=4.88x10^-4) while revealing an architectural boundary: omitting donor embeddings falls 4475.6 units below Full, outside the +/-250-unit margin. Continued target training frequently triggers severe post-grokking relapse. Freezing transferred representation carriers (E, U) nearly eliminates offline relapse (19.40% -> 0.07%, Holm p=0.005859). Online validation-triggered gating slashes True Max Drawdown from 22.06% to 0.60% on 2a+b (p=0.000488), with prospective confirmations extending protection across affine, nonlinear quadratic, and 2-layer targets (10.94-23.47 pp reductions), distinguishing continual stabilization from static early stopping. In non-abelian S_5, unshielded transfer surges transiently (95.4% peak), but a prospective shielding cohort yields no confirmed benefit (+0.15 +/- 1.14 pp). These results establish a component-level dissociation between transfer acceleration and trajectory stability, and expose the empirical boundaries of parameter shielding.

---


### 82. [Mask 2D-3D: Adaptive Dual-Masked Autoencoder Network for Image-to-Point Cloud Registration](https://arxiv.org/abs/2609.18088)

**<font color=#1a73e8>作者：</font>** Zhixin Cheng, Jiacheng Deng, Xiaotian Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detection-free methods for image-to-point cloud registration are prone to erroneous correspondences caused by domain and modality discrepancies, limited sensitivity of feature extractors, and the presence of non-overlapping regions. The Masked Autoencoder (MAE) has shown strong performance in visual representation for images and point clouds. It may be helpful to apply this approach to image-to-point cloud registration, a task that requires unified feature extraction and accurate cross-modal correspondences. Standard MAE's random masking may overlook key regions due to limited camera views, reducing registration effectiveness. To address this, we propose the Intermodal Dual-MAE Framework (ID-MAE) with a Similarity-based RL Masking Strategy (SRLM), which adaptively masks informative positions by leveraging cross-modal similarity and reinforcement learning, thus narrowing the modality gap. Our method enhances cross-modal representation learning by enforcing representation consistency during feature extraction, thereby enabling more reliable 2D-3D correspondence estimation. Experiments on RGB-D Scenes v2 and 7-Scenes benchmarks show that our method achieves state-of-the-art performance in image-to-point cloud registration.

---


### 83. [FedPGT: Progressive Gradient Transmission for Vehicular Federated Learning over Time-Varying Channels](https://arxiv.org/abs/2609.18089)

**<font color=#1a73e8>作者：</font>** Jintao Yan, Tan Chen, Yuxuan Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vehicular federated learning (VFL) enables privacy-preserving collaborative model training for intelligent transportation systems, where communication resource allocation and gradient sparsification techniques have been explored to reduce communication overhead. However, vehicle mobility leads to rapidly varying channel conditions and transmission capacity, rendering predetermined resource allocation and sparsification decisions ineffective. In this paper, we propose FedPGT, a progressive gradient transmission scheme for VFL over time-varying channels, where vehicles progressively transmit high-magnitude gradient entries in response to instantaneous channel conditions. We establish a convergence bound that characterizes the impact of transmitted gradient entries and reveals diminishing-return behavior governed by a power-law decay. Motivated by this result, we formulate a stochastic optimization problem for online decision-making, where the main challenge lies in a cumulatively coupled, non-separable objective. To handle this challenge, we introduce per-slot surrogate transmission variables to decouple the long-term dependence across time slots and convert the original objective into an additive per-slot optimization problem, enabling a Lyapunov drift-plus-penalty approach for online scheduling. We further develop a low-complexity resource allocation algorithm for efficient online implementation. Experimental results demonstrate that the proposed scheme achieves a 3.65% accuracy improvement on the CIFAR-10 image classification task and a 12.66% reduction in average displacement error on the Argoverse trajectory prediction task compared with state-of-the-art baselines, demonstrating its applicability to diverse learning tasks under highly dynamic vehicular environments.

---


### 84. [Needs Your Help: Understanding Platform-Directed Rating Participation in Community Notes on X](https://arxiv.org/abs/2609.18096)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Changxi Wen, Jiuchang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Community-based fact-checking is promising in countering misinformation, yet its scalability is constrained by slow rating accumulation. To address this challenge, platforms such as X implement platform-directed rating mechanisms, specifically through ``Needs Your Help'' algorithmic prompts, to target unresolved notes. Using a dataset of over 220 million rating contributions -- including 1.9 million platform-directed ratings -- on X, we examine contributors' response to note prompts, notes' resolution, and raters' spillovers. We found (i) at note level, population-sampled ratings concentrate on recent notes with certain helpfulness and high disagreement. Once sampled, population-sampled rating was associated with faster and more transitions to resolved statuses. (ii) At rater level, following raters' first observed population-sampled rating, raters exhibit significant yet modest increases in daily ratings, rating pace and tag usage, while other behaviors show no change. These highlight the promise of algorithmic nudges to guide volunteer attention toward contested content, accelerating consensus while sustaining rater engagement.

---


### 85. [iMINDBench: iEEG Multi-Institution Neural Decoding Benchmark](https://arxiv.org/abs/2609.18104)

**<font color=#1a73e8>作者：</font>** Geeling Chau, Saba Hashemi, Yonghyeon Gwon 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intracranial electroencephalography (iEEG) is widely used to record electrical activity directly from electrodes inside the human brain, making it an attractive modality for neural decoding. However, progress in iEEG decoding, especially toward general-purpose foundation models, remains difficult to measure reliably: datasets are task- or institution-specific, limiting evidence of generalization across tasks and recording environments, and preprocessing choices can strongly influence performance, making model improvements difficult to distinguish from preprocessing gains. Thus, we introduce iMINDBench, an iEEG Multi-Institution Neural Decoding Benchmark that evaluates models on a shared suite of fifteen decoding tasks across three naturalistic movie-watching datasets. The benchmark additionally defines standardized preprocessing tracks and fixed evaluation splits to support consistent model comparisons. Using iMINDBench, we find that the evaluated pretrained systems generally outperform baselines within their respective preprocessing tracks, while strong spectral baselines remain competitive across institutional datasets. In our scaling study, adding up to 25 times more supervised data from other subjects or institutions yields only small or task-dependent gains over within-session training. Together, these findings highlight the need for iEEG models that improve on strong preprocessing baselines and make more effective use of data across subjects and institutions. Project website: this https URL

---


### 86. ["Your Robot Was Trained on a Lie": Collision Mesh Poisoning Attacks on Robotic Manipulation](https://arxiv.org/abs/2609.18122)

**<font color=#1a73e8>作者：</font>** Gengyang Xu, Dongwei Xiao, Yiteng Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Learning-enabled robotic manipulation increasingly relies on robot simulators for policy training and evaluation before real-world deployment. Inside a simulator, a 3D asset contains two separate geometries: a visual mesh used for rendering and a collision mesh used for physical interaction. For computational efficiency, the collision mesh is deliberately a coarse approximation that need not have the same geometry as the visual mesh, a legitimate and pervasive discrepancy we call the Visual--Collision Gap (V--C Gap). We show that the V--C Gap opens a new and practical attack surface, and propose Collision Mesh Poisoning (CMP), the first poisoning attack against robotic manipulation delivered through the 3D asset supply chain. An attacker modifies only the collision mesh of a 3D asset, leaving the visual mesh and all other components unchanged. A policy trained and evaluated with the poisoned asset behaves normally throughout simulation, yet degrades, fails, or creates physical safety risks once deployed in the real world. Since current asset review practices cover malware, copyright, and format compliance, but not visual--collision consistency, poisoned assets can be distributed through legitimate supply chain channels. We evaluate several defenses and our results show that they are insufficient to defend against CMP, highlighting the need for new defenses.

---


### 87. [Aligned Consensus Teaching for Label-Efficient Oriented Object Detection in Weakly-Aligned Visible-Infrared Imagery](https://arxiv.org/abs/2609.18124)

**<font color=#1a73e8>作者：</font>** Qi Ming, Xiaxin Yuan, Jiahuan Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-infrared object detection (VIOD) detects objects with oriented bounding boxes from paired visible and infrared images. Existing methods depend on costly dual-modality annotations. Semi-supervised learning can reduce this burden, but extending it from single-modal detection to VIOD is challenging. In the practical image-pair-level setting considered here, only a few pairs are labeled in both modalities, while the rest are completely unlabeled. This limited supervision creates three challenges: (i) too few labeled boxes for robust cross-modal alignment; (ii) pseudo-label errors caused by branch-wise misses accumulate during self-training; and (iii) tail-class annotations become critically scarce as the labeling budget decreases. We propose Aligned Consensus Teacher (ACT) for label-efficient VIOD in this setting. Its Cycle-Consistent Region Alignment (CRA) combines cycle consistency and sparse anchors with reliability-weighted regional matching. Cross-Modal Consensus Mean-Teacher (CMC-MT) forms consensus pseudo labels under pair-preserving views to recover branch-wise misses and supervise unlabeled pairs. Text-Guided Cross-Modal Instance Augmentation (TG-CMIA) uses a vision-language scene prior to compose tail-class instance pairs while preserving RGB--IR offsets. To the best of our knowledge, ACT is the first framework to study semi-supervised VIOD under this image-pair-level setting. Experiments on DroneVehicle and VEDAI show consistent gains across annotation ratios. With 10\% labeled pairs on DroneVehicle, ACT reaches 94.3\% of the mAP obtained by the same detector under full supervision. Code and models will be available on GitHub to facilitate future work.

---


### 88. [PRISM: Predictive Representation of Interaction Style and Motion for Social Robot Navigation](https://arxiv.org/abs/2609.18125)

**<font color=#1a73e8>作者：</font>** Bo-Han Chen, Hiromu Taketsugu, Norimichi Ukita  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans often observe others before interacting and adjust their behavior accordingly. Robot navigation in crowds, however, often represents pedestrians mainly by observed geometric states, leaving individual differences in interaction tendencies implicit. We propose PRISM (Predictive Representation of Interaction Style and Motion), a framework that infers interaction traits from passive observations of human-human interactions. PRISM encodes human trajectories into a continuous ordinal latent space with a transformer encoder trained by Rank-N-Contrast loss, and pairs each inferred trait with a temporal-stability score supplied to the navigation policy. In randomized crowd simulations, PRISM reduces collision rates over the geometry-only baseline and yields small improvements in navigation-time and path-length metrics. These results suggest the utility of passive latent-trait inference for social navigation in dynamic crowds.

---


### 89. [Designing Agentic AI Workflow Portfolios under Imperfect Selection and Compute Cost](https://arxiv.org/abs/2609.18126)

**<font color=#1a73e8>作者：</font>** Mojtaba Abdolmaleki, Stefanus Jasin, Boyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems often approach the same task through multiple workflows that differ in reasoning strategy, verification structure, and compute cost. A natural deployment policy is to use the workflow with the highest average performance, but this can be suboptimal because different workflows may succeed on different instances. We study a portfolio-and-selector paradigm in which a firm runs multiple workflow executions and selects the final answer after observing their outputs. Additional executions may uncover correct answers that the best standalone workflow misses, but they consume compute and introduce plausible distractors that complicate final selection. We formulate this as a workflow portfolio problem in which the firm jointly chooses run size and allocation across workflow types. We summarize selector quality through an odds-lift index and derive sharp bounds on the value of workflow variety. For finite workflow pools, we develop exact formulations, linear programming relaxations, randomized rounding procedures, and computable performance certificates. For large implicit workflow classes, we derive a finite-dimensional dual and an ellipsoid method using a pricing oracle to identify workflows with high weighted accuracy net of recurring compute cost. Under a weak condition, the method obtains a near-optimal solution to the relaxation with polynomially many oracle calls. We evaluate the framework on three datasets: ABCD, Schema-Guided Dialogue, and HotpotQA. Relative to the best standalone workflow, portfolio optimization improves held-out selector accuracy by 3.1, 7.5, and 0.9 percentage points, respectively. Dual-guided workflow generation adds 3.5 points on ABCD and 24.1 on HotpotQA, with no additional gain on Schema-Guided Dialogue.

---


### 90. [Learning Fractional-Order Dynamics from a Single Trajectory](https://arxiv.org/abs/2609.18127)

**<font color=#1a73e8>作者：</font>** Xiaole Zhang, Ziyi Zhang, Zehao Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world processes exhibit long-range dependence, where the current state depends on a slowly decaying trace of past states rather than on the most recent state alone. This paper studies system identification for discrete-time fractional-order linear time-invariant systems from a single observed trajectory of length $t$, a setting that captures such non-Markovian dynamics through the Grünwald--Letnikov difference operator. Unlike Markovian systems, fractional-order systems couple estimation across the entire history, making both statistical analysis and practical identification more challenging. We propose \emph{Fractional-Order Ordinary-Least-Squares Grid-Search (FO-GS)}, a simple two-stage estimator that exploits the diagonal structure of the fractional-difference operator to decouple the identification problem row-wise. Under the stability assumption, we establish high-probability, non-asymptotic error bounds for estimating both the fractional order and the system matrix in the heterogeneous setting, with both estimation errors scaling as \(\mathcal{O}(t^{-1/2})\). Through experiments, we show that \emph{FO-GS} outperforms existing baselines in recovering both the fractional order and the underlying system dynamics.

---


### 91. [MCLC-NET: Multimodal Continual Learning for Leaf Counting](https://arxiv.org/abs/2609.18129)

**<font color=#1a73e8>作者：</font>** Ruchi Bhatt, Pratibha Kumari, Shreya Bansal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leaf counting is an important task in plant phenotyping for monitoring plant growth and estimating crop yield. Most existing methods rely on RGB images, but their performance is often affected by occlusion, lighting variations, and other real-world challenges. Additional modalities, such as depth and thermal images, can provide useful complementary information. However, multimodal leaf counting remains underexplored. Also, many existing methods assume that all training data are available simultaneously, which is impractical in real agricultural settings, where data is collected over time from multiple sources. To address these challenges, we propose MCLC-NET, a multimodal continual learning framework for leaf counting. It learns tasks sequentially using a memory-based strategy with a memory buffer to retain important samples from previous tasks. We also introduce MMLC, a real-world multimodal leaf-counting dataset designed for a domain incremental scenario (DIS) in CL. It contains RGB, depth, and thermal images collected across different crop types under varying environmental conditions, arranged in three orderings: crop-wise, time-wise, and mixed. Experimental results, averaged over three random seeds, demonstrate that MCLC-NET consistently outperforms existing methods across all three task orderings, achieving the lowest AMSE of 0.675$\pm$0.027, 0.542$\pm$0.069, and 0.745$\pm$0.057, respectively.

---


### 92. [Stealthy in Semantics, Antagonistic in Space: Attacking Visible-Infrared Object Detectors via Object-Level Misalignment](https://arxiv.org/abs/2609.18133)

**<font color=#1a73e8>作者：</font>** Yueqi Zhu, Qi Ming, Guo Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-infrared object detectors are used for robust perception under challenging illumination and weather conditions. Current physical attacks apply conspicuous patches to spatially aligned target regions, which are noticeable to human observers. Meanwhile, most of these methods only perturb the appearance within the aligned region, without explicitly targeting the correspondence between modalities or the fusion process. In this paper, we propose CamoShift, an adversarial framework for visible-infrared object detection. By combining visual camouflage with object-level infrared shifting, CamoShift breaks cross-modal spatial alignment and disrupts fusion. Specifically, the Semantic Camouflage Module (SCM) generates a stealthy camouflaged patch that can be attached to the host object and maintains its effectiveness in the infrared branch through an RGB-IR adapter. The Object-level Spatial Decoupling Module (OSDM) shifts the infrared target evidence in a scale-aware manner, so as to break object-level correspondence and disrupt cross-modal fusion. Then, the Harmonic Adversarial loss (HarAdv loss) further balances attack strength and visual stealth during optimization. To the best of our knowledge, we are the first to target both visual stealthiness and attack success in visible-infrared object detection. Extensive experimental results show that CamoShift achieves a superior balance between attack effectiveness and visual stealth. Code and models will be available on GitHub.

---


### 93. [Rethinking How We Evaluate Methodological Progress in Health AI](https://arxiv.org/abs/2609.18134)

**<font color=#1a73e8>作者：</font>** Florent Pollet, Matthew McDermott  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methodological progress in artificial intelligence (AI) for electronic health records (EHRs) depends on our ability to determine which algorithms work better, and under which conditions. However, such progress is thought to be hindered by difficulties in reproducibility and in defining clinically meaningful evaluation tasks. We empirically study these barriers by re-implementing 12 historical and recent algorithms within a shared evaluation framework and evaluating them on two clinical datasets, MIMIC-IV and NWICU. We compare two complementary task families: expert-authored clinically meaningful tasks and generated tasks defined from randomly sampled event codes and prediction horizons. We ask whether relative algorithms comparisons transfer across task families and datasets, whether residual task heterogeneity contains useful methodological structure, and what a controlled comparison reveals about progress over the last decade. We find that aggregate pairwise comparisons transfer strongly across evaluation settings, including from randomly generated tasks to clinically meaningful tasks and across datasets. At the same time, clinically meaningful tasks exhibit greater task-method interaction, providing preliminary evidence that task properties can help explain when particular modeling choices are advantageous. Finally, newer algorithms do not consistently outperform earlier approaches: gradient-boosted trees remain highly competitive when paired with a modern, wide and sparse representation of the EHR. Together, these results suggest that useful methodological knowledge may require less task engineering than commonly assumed, while highlighting the importance of understanding the structured heterogeneity that remains across tasks and methods.

---


### 94. [DualSQL: Text-to-SQL with Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.18135)

**<font color=#1a73e8>作者：</font>** Shijie Chen, Yu Gan, Yeounoh Chung 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> State-of-the-art Text-to-SQL systems are typically multi-agent pipelines centered around two fundamental tasks: schema linking and SQL generation. However, existing work trains separate models for each task, failing to leverage the synergy between these interrelated tasks. In this work, we propose DualSQL, a new Text-to-SQL system consisting of two agents powered by a single model backbone. The agents share the same model weights and agentic scaffold, enabling joint optimization through a robust multi-agent reinforcement learning (RL) framework. We design three database access tools to facilitate effective multi-step reasoning grounded to interactions with the databases. To improve training and avoid model collapse, we introduce a set of rollout guardrail mechanisms that stabilizes multi-agent RL training, supporting DualSQL to keep improving during training. We also introduce a new SQL correctness metric, robust execution match (REX), to more accurately judge SQL correctness and assign reward signals. Being trained on only 3755 examples, DualSQL-4B achieves an impressive 68.0% execution accuracy on the BIRD development set, matching previous 7B models. DualSQL-8B further improves to 71.1%, outperforming previous state-of-the-art single-model solutions with 32B parameters. These results demonstrate the strength of joint multi-agent reinforcement learning for building high performance Text-to-SQL pipelines.

---


### 95. [Reaching Every Position Without Searching: Rotating Sparse Wiring on the Hypercube as a Substitute for Attention](https://arxiv.org/abs/2609.18145)

**<font color=#1a73e8>作者：</font>** Yoshiaki Takashita  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention pays, at every layer and for every input, the cost of searching for whom to connect. We ask how far one can get with wiring that is fixed, sparse, and simply rotated from layer to layer. Treating the $n$ positions of a sequence as the vertices of a $\log_2 n$-dimensional hypercube and connecting each position, at layer $\ell$, to its neighbour along dimension $\ell \bmod \log_2 n$, information from every position reaches every other in $\log_2 n$ layers with $2n$ links per layer instead of $n^2$. On a synthetic task that is unsolvable unless all positions are reached, this rotation matches all-to-all wiring at $1/32$ of the links, while the same sparse pattern held fixed across layers fails; what matters is that every dimension is touched, not the order. On character-level language modelling of a public corpus (the first $12$M characters of enwik8), a hybrid that keeps two attention layers among sixteen sparse ones reaches $0.06$ bits-per-character lower held-out loss than a fully attentive model of the same width at the same step budget (three seeds each, no overlap), with $1/7$ of the links, $42\%$ fewer parameters, and $2.4\times$ less wall-clock time; the purely rotated schedule is level with the hybrid. The same ordering holds on a second corpus of mixed Japanese, English and code, where the gap widens to $0.16$. The usable learning-rate window is four to eight times wider than attention's on both. We also report what did not work - learned coordinates, and a "dynamics" variant whose apparent gains turned out to be an artefact of a saturated kernel - and the measurement discipline (frozen corpus, full-coverage evaluation, seed spread as the bar for ranking) that we found necessary to say anything at all at this scale.

---


### 96. [Bridging the Opacity: Evidence-Backed Cross-Chain Transaction Correspondence Reconstruction Across Heterogeneous Blockchains](https://arxiv.org/abs/2609.18158)

**<font color=#1a73e8>作者：</font>** Dan Lin, Huan Xiao, Ziwei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-chain bridges enable interoperability, but they also break the transaction trails needed to trace illicit funds. Third-party investigators typically cannot access the source-to-destination mappings maintained by bridge backends, and our survey of 131 bridges finds that only 16.79% provide complete public tracking. Existing approaches depend on official APIs, EVM-specific assumptions, or fragile temporal heuristics, limiting their ability to trace transfers across heterogeneous ledgers. We present XSplicer, an evidence-driven system for reconstructing cross-chain transaction correspondence (xTCR) without privileged access to bridge backends. XSplicer derives unified semantic specifications from public protocol documentation and transaction examples, translates them into lightweight parsers and verifiers, and links source and destination transactions by prioritizing hard evidence and using soft clues only when necessary. We evaluate XSplicer on seven bridge protocols spanning EVM, Bitcoin, and Solana. XSplicer achieves 92.5% global recovery rate and up to 98.61% on individual protocols. Under adversarial noise, its hard-evidence verifier retains the correct match in 100% of tested cases, while soft-clue matching degrades as ambiguity increases. In two real-world case studies, XSplicer recovers more than 1,900 historical transaction pairs after Multichain ceased operations and identifies 754 illicit cross-chain transfers worth 105.6 million USD in the Bybit laundering incident. These results show that public protocol invariants can support practical cross-chain forensics without privileged bridge mappings.

---


### 97. [Time-Aligned Evolving Concept Graphs for Scientific Relation Forecasting](https://arxiv.org/abs/2609.18163)

**<font color=#1a73e8>作者：</font>** Fred Sun, Jingze Wang, Minkun Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting scientific relations can guide discovery by identifying promising connections before they emerge. Existing approaches often model concept semantics and graph structure separately or summarize semantics over coarse historical snapshots, leaving semantic representations potentially misaligned with rapidly evolving graph evidence. We propose a time-aligned evolving concept graph framework that jointly models semantic and structural evolution. Its core idea is to treat dated papers as shared update events, reconstructing semantic and structural states from the same publication history through each prediction time. Pair-level fusion combines these states to forecast first co-occurrence, relation formation, and conditional relation type. Holding architecture and training fixed, refreshing context alongside graph updates improves mean relation AUPRC by 16.6% over frozen context. On a graph built from 187,848 papers with 270,687 concepts and 7.45 million co-occurrence links, the complete framework improves mean relation AUROC from 0.9290 for the strongest evaluated baseline to 0.9722, with mean population-weighted AUPRC 0.005778.

---


### 98. [Replication Studies: Not Just a Copy](https://arxiv.org/abs/2609.18181)

**<font color=#1a73e8>作者：</font>** Yiheng Liang, Kim Marriott, Helen C. Purchase  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Replication studies revisit previous experimental findings for multiple purposes, including assessing reliability, exploring generalisability, and evaluating research methods. Such studies entail design decisions that a single replication label cannot fully capture, making their designs difficult to describe and compare. We present REPVIS2, a validated design space that describes how a replication study relates to a reference study across eight practical dimensions, each coded as identical, similar, or different. We refined our initial design space, REPVIS1, by applying it to a corpus of replication studies and validated REPVIS2 against a separate corpus. We then characterised 86 replication studies from 51 papers in visualisation through paired reading of the replication and reference reports. Studies often retained the task while changing the procedure, interface, environment, participant population, evidence, or analysis. Additions beyond the replication core were also common. REPVIS2 makes replication design explicit for characterisation, reporting, and planning. An interactive visualisation and supplementary materials are available at this https URL.

---


### 99. [Transformation Laws in Neural Representations: Structure, Realisability, and Construction](https://arxiv.org/abs/2609.18190)

**<font color=#1a73e8>作者：</font>** Yuan Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How neural representations preserve the structure of input changes connects representation analysis with internal intervention. We study operable representational content through compatible actions of reference transformations on neural features. We characterise when a transformation descends through an encoder, and give a linear setting in which the defect is governed by the transformation's demand for discarded information, measured in the metric the representation induces. On a rectifier the failure to realise a transformation has two distinguishable sources --- what the source region has already made unrecoverable, and what it costs to satisfy every region the transformation visits with one operator --- and for a \textit{measured} harmonic carrier the same question has a closed answer: a linear realisation exists exactly when the retained harmonic blocks are invariant under the action. Using colour as the in-depth instance, we find that hue orbits in frozen visual features concentrate 84--88\% of their energy in the first two harmonics with rotation planes shared across shapes, that this organisation is substantially inherited from input and architecture and is reshaped by training and depth, and that the measured structure supports prediction, transport from new starting states, and composition --- with global and local realisations differing sharply in which they achieve. Guided by the measurements, we construct a compact interface whose rotation action is fixed by the structure and never fitted: it reads hue zero-shot at 3.4$^\circ$ median error on unseen shapes. Theory, structural measurement, and construction together establish transformation laws as a concrete object connecting the understanding of neural representations to their design.

---


### 100. [ISIA-AF: Orchestrating Reproducible Attacks and Multi-Source Data Collection for OT Systems](https://arxiv.org/abs/2609.18196)

**<font color=#1a73e8>作者：</font>** Stefan Manfred Haratzmüller, Thomas Rosenstatter, Olaf Saßnick 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Operational Technology (OT) environments require realistic, reproducible security datasets, yet existing approaches often lack automation, multi-source data capture, and sufficient documentation for reuse. This paper presents ISIA-AF, a modular attack framework for orchestrating reproducible attack execution and automated dataset generation on industrial systems. The framework coordinates distributed attack clients, records network traffic and operational data, ultimately leading to a multi-source dataset. We derive functional and non-functional requirements from prior work and stakeholder discussions, and realise the framework following a design science research approach. A case study on the ISIA testbed, comprising a real industrial system and a simulated process, demonstrates how the framework supports centralised control, low communication overhead, and flexible deployment across network segments. The result is a practical basis for generating extensible, multi-source OT security datasets for intrusion detection research.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-223](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
