# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **152** 篇论文：已确认 **79** 篇，待复核 **73** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-152](./part-04.md)

---

### 101. [Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry](https://arxiv.org/abs/2608.06849)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yehan Yang, Junyuan Shang, Yang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference is bottlenecked by quadratic attention computation and growing KV-cache costs. Existing sparse attention and KV-compression methods typically decide which tokens or heads to preserve from runtime attention scores, observation windows, calibration prompts, or learned gates, making head diagnosis input-dependent and costly to deploy. We propose Autonomy-of-Heads (AoH), a data-free method that identifies retrieval and streaming heads from the spectral geometry of query-key projections. AoH defines the kernel attention operator $M_h = W_K^{h\top}W_Q^h$ and uses its effective-rank as a weight-space measure of head function: concentrated spectra indicate a small number of dominant query-key matching directions and are associated with retrieval heads, whereas diffuse spectra indicate the absence of a dominant global matching direction and are associated with streaming heads. We further derive an efficient $d_\text{head}$-dimensional computation that avoids constructing the full $d_\text{model}\times d_\text{model}$ matrix. We conducted extensive experiments across models demonstrating that at 50\% sparsity, AoH retains 96.5\% of Full Attention performance on average while reducing prefill and decode latency by up to 41.4\% and 66.0\%, respectively, and KV-cache memory by 50.0\% at 256K tokens.

---


### 102. [SynChain: Inducing Computer-Use Agent Systems to Construct Their Own Attack Chains](https://arxiv.org/abs/2608.06862)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fuyao Zhang, Jiaming Zhang, Che Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-use agents~(CUAs) have transformed large language models into persistent execution systems capable of generating, storing, and reusing artifacts like skills and memory entries. However, existing security defenses largely treat attacks as externally triggered or temporally bounded, leaving a critical gap in addressing how compromise can propagate internally through an agent's own persistent state. We reveal that malicious influence can be covertly embedded into the structural redundancies of autonomously synthesized artifacts, allowing it to survive internal state updates and bypass standard vetting mechanisms. To formalize this threat, we introduce SynChain, a self-synthesized attack paradigm utilizing persistence-aware directed supervised fine-tuning to induce agents to create poisoned yet benign-looking artifacts. To systematically evaluate this propagation, we construct CUAChain, a dataset comprising 30 benign task chains and three attack objectives. SynChain enables dormant payloads to seamlessly reactivate in future workflows as trusted context, operating entirely without new malicious exogenous inputs. Extensive experiments on OpenClaw, Codex, and Claude Code under four defense settings demonstrate that SynChain achieves high attack success and outperforms adapted baselines, proving that securing CUAs requires provenance-aware reasoning over cross-task execution trajectories.

---


### 103. [CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems](https://arxiv.org/abs/2608.06871)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yingtao Tian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex systems, core objects of study in artificial life, model diverse phenomena through nonlinear, feedback-driven interactions that produce emergent behavior, with applications from population dynamics and biology to economic policy and strategic decision-making. Yet the difficulty of predicting how feedback structure gives rise to emergent behavior, a central open problem in artificial life, makes goal-directed design exceptionally challenging. In established practice, system structures are written in specialized modeling languages such as DYNAMO or STELLA, compounding the challenge with labor-intensive workflows that limit adoption and hinder timely decision-making. To address these challenges, we introduce CEDAR, an autonomous method that uses Large Language Model (LLM) agents to discover complex systems satisfying user-specified behavioral goals. Our key innovation is an LLM-driven Monte Carlo Tree Search (MCTS) deeply coupled with complex systems: at each iteration, an LLM Judge evaluates emergent behavior against specified goals and an LLM Editor proposes improved variants, with the Judge acting as a fitness function and the Editor as a variation operator, akin to a generate-and-evaluate loop in evolutionary computation. We represent complex systems as a restricted, runnable subset of Python with domain-specific primitives, letting LLMs modify system dynamics directly. CEDAR formalizes this as an MCTS variant with an LLM-parameterized transition kernel and value function, enabling goal-directed discovery of complex system behaviors while preserving solution diversity, and its LLM-based interpretability reveals how structural changes drive emergent behavior. CEDAR reduces human effort while enabling capabilities difficult to achieve with existing approaches, facilitating broader adoption of complex systems across domains.

---


### 104. [FedVAR: Prototype-Aligned Federated Framework for Video Anomaly Recognition](https://arxiv.org/abs/2608.06876)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ghani Haider, Majid Kundroo, Boyun Eom 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the era of Industrial Internet of Things (IIoT) and Cyber-Physical Systems (CPS), Federated Learning (FL) offers a promising decentralized intelligence paradigm for Video Anomaly Recognition (VAR). This task is vital for maintaining high-fidelity Digital Twins and ensuring safety in mission-critical environments. However, the inherent data heterogeneity across distributed edge clients leads to a fundamental challenge known as semantic misalignment, where clients learn divergent feature representations of "normal" and "abnormal" events. The problem becomes particularly pronounced in VAR, where the presence of diverse and fine-grained anomaly categories leads each client to develop distinct semantic interpretations of abnormality. Existing federated methods primarily focus on binary anomaly detection and fail to address this misalignment, preventing effective fine-grained recognition. In this paper, we introduce FedVAR, a weakly-supervised FL framework explicitly designed for VAR. Leveraging the rich representations of Vision-Language Models (VLMs), FedVAR employs a prototype-based alignment mechanism that creates a shared semantic anchor for all clients to re-center and align their visual and textual feature spaces. This process enforces a consistent representation of "normality" across the decentralized network, directly mitigating semantic misalignment and enabling robust prompt-learning of anomaly direction vectors with minimal communication overhead. We conduct extensive experiments on challenging benchmarks under various non-IID data partitioning schemes, unseen domains, and novel anomaly classes. The results demonstrate that FedVAR consistently outperforms state-of-the-art federated baselines, establishing a robust framework for distributed intelligence in video-based CPS.

---


### 105. [SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time](https://arxiv.org/abs/2608.06880)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qinfeng Li, Dalin He, Yuntai Bao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> General-purpose skills promise reusable procedural knowledge for language agents, yet semantic relevance does not guarantee execution utility: a retrieved skill may encode assumptions that conflict with the current task, execution environment, or other retrieved skills. We formalize this problem as the skill--execution misfit. To address it, we propose SkillAligner, a training-free execution-time skill adaptation framework that treats retrieved skills as adaptable drafts rather than fixed instructions. Before execution, SkillAligner performs a one-time joint adaptation that specializes useful skill fragments to task requirements, aligns their procedural assumptions with the available execution interface, and composes the resulting guidance by resolving dependencies, conflicts, and redundancy across skills. The adapted content is consolidated into a compact execution guide and reused throughout the subsequent trajectory. Extensive experiments across diverse agent benchmarks and model backbones show that SkillAligner substantially improves task performance over existing skill-use baselines, reduces skill-induced regressions at the instance level, and lowers total inference cost.

---


### 106. [Georeferencing Non-Gazetteered Place Names using Biological Specimen Records](https://arxiv.org/abs/2608.06884)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aneesha Fernando, Surangika Ranathunga, Kristin Stock 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biological specimen records collected by natural history institutions constitute a rich source of temporal geographic knowledge, capturing biodiversity information about regional landscapes as they were recorded at different times. Using digitised data from the Allan Herbarium (New Zealand), this study identifies place names in these specimen locality descriptions that are absent from current gazetteers; we refer to these as non-gazetteer place names (NGPs). These place names are typically historical, vernacular, or colloquial and were used as landmarks to describe a specimen's location at the time of collection. We then investigate the problem of georeferencing the NGPs using only the limited information available in the specimen records. To resolve this, we leverage repeated occurrences of the same place name across specimen records with different specimen locations and spatial relation terms, extracting and inverting these relations to derive constraints on NGP locations. This approach is instantiated within deterministic, probabilistic, and LLM-based methods, enabling a comparative analysis of their strengths and limitations for text-based spatial inference. On a pseudo-NGP benchmark, probabilistic inference achieves the highest accuracy (median error 1.43 km; A@1 km 36%), while the LLM yields competitive but less precise estimates (median error 1.80 km; A@1 km 31%), indicating that, despite advances in LLMs, traditional modelling remains advantageous when high spatial precision is required.

---


### 107. [Calibrating WEAT Against Anisotropy: ZCA Whitening as a Geometric Pre-Processing Step for Embedding Association Tests](https://arxiv.org/abs/2608.06908)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Seitaro Ono, Senna Ross, Jun Saiki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose Zero-phase Component Analysis (ZCA) whitening as a geometric pre-processing step for the Word Embedding Association Test (WEAT). WEAT is a bias measurement method widely used in both computational social science and AI fairness research. It relies on cosine similarity as a measure of semantic association, which assumes that the embedding space is approximately isotropic. However, prior work has reported that many widely used language models do not satisfy this assumption, raising concerns about the reliability of bias measurements. ZCA whitening transforms the covariance of the embedding space into the identity matrix while minimizing perturbation to the original vectors. This transformation restores the isotropy condition on which WEAT relies. We evaluate our approach on ten standard WEAT test suites and seven models spanning three architectural families, yielding 70 model-task combinations. The results show that ZCA whitening substantially reduces the anisotropy of the embedding spaces across all models. Particularly for highly anisotropic models, we further observe improvements on standard semantic similarity benchmarks, indicating that the calibrated space better captures semantic associations. After calibration, over 30% of WEAT results change significance status, and effect sizes shift in both directions depending on bias category. These shifts suggest that uncalibrated measurements may both overestimate and underestimate the associations encoded in the embedding space. These findings indicate that previously reported bias measurements in anisotropic embedding spaces should be interpreted with caution and may benefit from re-evaluation with calibrated methods. Our approach contributes to restoring the measurement foundation of WEAT across both computational social science and AI fairness research.

---


### 108. [Long-Horizon Agent Trajectory Attribution: A Unified Benchmark and Fine-Grained Annotation Framework](https://arxiv.org/abs/2608.06909)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jing Chen, Yang Sun, Li Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate through long-horizon trajectories involving user instructions, tool use, external observations, and memory. Existing benchmarks primarily evaluate behavioral outcomes but provide limited support for fine-grained attribution analysis. We introduce trajectory attribution and develop a benchmark and annotation framework for this task. The benchmark organizes heterogeneous trajectories under a unified component schema and provides annotations of the primary attribution component, together with attack and execution chains where applicable. Instantiating the benchmark with trajectories from AgentDojo and the Stage and Canary settings of Agent3Sigma yields more than 1,300 annotated trajectories covering task-aligned actions, unsafe actions, and safety refusals. The benchmark defines two evaluation tasks, primary attribution localization and attribution-chain recovery, and provides reference baselines based on incremental trajectory contribution and component-level leave-one-out perturbation. It captures diverse attribution settings, including local and long-range attribution as well as structured attribution chains. Reference baseline results exhibit substantial performance differences across these settings, providing an initial characterization of the benchmark's attribution challenges. Beyond this initial instantiation, we release a reusable annotation skill that enables trajectories generated by new agent models to be standardized, annotated, and evaluated under the same framework. Project resources and future releases are available at this https URL.

---


### 109. [MuST-VAD: Mutual Structured Learning for Video Anomaly Detection](https://arxiv.org/abs/2608.06913)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Satoshi Hashimoto, Hitoshi Nishimura, Mori Kurokawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose MuST-VAD, a mutual structured learning framework for weakly supervised video anomaly detection (VAD) in which an anomaly detector and a large vision-language model (LVLM) exchange their acquired knowledge. Detectors in weakly supervised VAD learn anomaly scores from features extracted by a fixed, task-agnostic backbone. These fixed features bound the achievable detection accuracy. Recent methods therefore transfer LVLM semantics into the detector as richer features. However, this transfer is one-way: what the detector learns about the target videos never returns to the LVLM. MuST-VAD extends the one-way transfer into a bidirectional learning loop. In this loop, the latest detector predictions supervise the LVLM adaptation, and the adapted LVLM returns updated representations that retrain the detector; the two models alternate these updates over small video groups. Both models train on detector-selected key clips, while confidence weighting and annotation-anchored question answering keep the exchanged supervision reliable. On UCF-Crime, our mutual learning improves the one-pass transfer baseline from 88.15% to 88.63% AUROC and from 37.25% to 42.46% average precision (AP), outperforming the state-of-the-art method in AP by 4.13 points.

---


### 110. [Deal Me Maybe: The Role of Emotions in Multi-Agent Negotiation](https://arxiv.org/abs/2608.06922)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Massimiliano Luca, Apoorva Singh, Bruno Lepri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Negotiation is a demanding social task for LLM agents, requiring strategic reasoning, persuasion, and interpersonal adaptation. Yet existing benchmarks often treat agents as emotionally neutral, overlooking a key driver of human bargaining behavior. We study how prompt-conditioned emotions affect LLM-based price negotiation. In a controlled framework, buyer and seller agents are independently assigned one of six emotional states and negotiate over 350 real consumer products under two budget conditions. Across 36 emotion-pair settings and five widely used LLMs, we find that emotions strongly shape outcomes. Angry buyers almost never reach agreement (0.39% deal rate), while happy buyers agree most often (28.91%), but obtain worse prices than fearful buyers. Emotion effects are role-dependent: buyer emotion mainly drives acceptance and rejection, whereas seller emotion shapes concession dynamics. These effects influence not only language, but also termination behavior and price trajectories, raising concerns for emotion-conditioned agents in commerce.

---


### 111. [TRIBE: Predicting Team Performance via Communication Behavior Ensembles](https://arxiv.org/abs/2608.06926)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ali Jalal-Kamali, Nikolos Gurney, David V. Pynadath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing autonomous agents that effectively assist human teams hinges on understanding team dynamics, often without task specific knowledge. We present TRIBE, a domain independent approach that reveals team behavioral dynamics invisible to traditional performance metrics. We show that communication patterns can categorize teams into performance predictive behavioral tribes, as early as 10% into the task, enabling timely interventions. We test TRIBE on four diverse datasets and demonstrate that communication patterns predict team performance while the prediction strength varies by the degree a task structure allows for behavioral freedom. Our temporal analysis reveals that AI agents significantly alter team behavioral trajectories while human advisors align with natural dynamics, and that teams maintain behavioral flexibility throughout collaboration. Further, we compare TRIBE to Llama and optimize the pipeline, achieving significant speedup with performance improvement.

---


### 112. [Ask-E: An Environment for Calibrated Question Generation](https://arxiv.org/abs/2608.06933)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sarah Pratt, Jae Sung Park, Scott Geng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Today, we improve models by training and evaluating them on problems at the frontier of their abilities. Creating such problems is itself a demanding task, requiring the ability to probe model limits and generalize beyond existing question distributions. It also means placing problems at a precise difficulty level, which requires understanding what it takes to solve them. In short, generating problems calibrated to a model's current frontier demands capability beyond it, an increasingly burdensome constraint as models improve. Our key insight is that we can leverage this constraint to our advantage: a model that can generate problems consistently calibrated to a given frontier must possess capability beyond it. Accordingly, we present Ask-E, an environment that benchmarks and trains models on their ability to write questions at a given skill level, rather than answer them. Concretely, we define target skill levels as ranges bounded by the capabilities of two existing language models. A generated question is successfully calibrated if exactly one of the two models can solve it, placing it precisely within the target range and differentiating the capabilities of these models. Ask-E serves both as a benchmark and a training environment, where models generate problems calibrated to a variety of skill levels. We find that even frontier models achieve below 50% calibration on the benchmark, leaving significant headroom to measure future progress. We also show that training on this environment leads to improvements across a number of downstream math benchmarks even with no new math data, no interaction with stronger models, and no correctness-based reward.

---


### 113. [Degradation-Aware Prompt Learning with Cross-Modal Compensation for Adverse Weather Removal](https://arxiv.org/abs/2608.06939)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wanshu Fan, Yunzhe Zhang, Yue Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse weather causes diverse and complex image degradations, severely compromising the reliability of computer vision systems. Existing all-in-one restoration models attempt to address multiple degradation types within a unified framework, but often lack explicit spatial and semantic modeling of degradation characteristics, limiting their adaptability to diverse weather conditions. To address this limitation, we propose a Degradation-Aware Cross-Modal Prompt Compensation Network (DCMPC-Net) that leverages cross-modal degradation cues from a pretrained vision-language model to condition restoration features within a unified backbone. Specifically, our DCMPC-Net mainly consists of the Cross-Modal Prompt Generator (CMPG), Prompt-Guided Attention Alignment Module (PGAAM), and Dual Feature Compensation Module (DFCM). The CMPG integrates textual embeddings with visual features to produce degradation-aware prompts that encode degradation-related semantic and contextual cues. These prompts are injected into the decoder via a PGAAM, which adaptively aligns semantic information with degraded regions to facilitate context-aware restoration. To further enhance structural fidelity, DFCM is introduced that disentangles degradation artifacts from scene structures, thereby improving the reconstruction of fine textures and detailed content. By integrating cross-modal semantic guidance with spatial alignment and structural enhancement, DCMPC-Net achieves robust and perceptually consistent restoration across diverse weather conditions. Extensive experiments show that DCMPC-Net outperforms state-of-the-art methods in both task-specific and unified settings, achieving superior accuracy and visual fidelity.

---


### 114. [Blind to the Pivotal Vote: Aggregate Independence Metrics Miss Where Verification Actually Helps](https://arxiv.org/abs/2608.06940)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judge panels are a standard evaluation tool, but prior work reports highly correlated panel errors: nine judges provide roughly the effective information of two independent ones, and aggregation closes only a small fraction of the gap. A natural remedy--a signal from a different evidence source, e.g., executing a test suite--produced no distinguishable change in the panel's effective-vote count at scale (-0.04, 95\% CI [-0.10, +0.02]). Aggregate dependence and conditional decision utility are different questions. Elementary majority arithmetic fixes the affected set for single-ballot substitution: only decisions with a one-vote margin can change. The empirical question is whether panel error rates rise and useful substitutions concentrate there. They do: the entire accuracy gain concentrates on these pivotal queries, where it is large (+10.4 to +23.3 percentage points across three headline configurations), and is exactly zero elsewhere. We confirm the pattern across three code benchmarks and four panel sizes (a 9-judge extension and 56 dependent subsampling checks, gain +6.5 to +16.1 percentage points). On HumanEval+/MBPP+, a majority-side replacement rule raises overall accuracy from 82.44\% to 85.62\% while invoking the signal on 16.2\% of queries; signal-only remains stronger at 87.60\%. Thus population-level dependence diagnostics and margin-stratified utility are complementary, and the affected-set characterization yields a call-reduction rule for any specified single-ballot substitution policy.

---


### 115. [When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse](https://arxiv.org/abs/2608.06947)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yingtao Ren, Ziyi Zhao, Yiwei Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is indispensable for enhancing large language models. However, RAGs are increasingly susceptible to poisoning attacks, in which adversarial documents are injected to manipulate generator outputs. Previous methods rely on output-side signals such as perplexity and consistency checks to detect such attacks. Nevertheless, our analysis reveals that deliberate attacks often induce false confidence, where poisoned outputs exhibit even lower perplexity than benign ones, rendering uncertainty-based detection ineffective. To address this challenge, we explore the internal dynamics of the generator and identify a distinctive signature termed \textit{Attention Collapse}. Unlike the dispersed attention in benign generations, attacked generations exhibit a decrease in entropy as attention concentrates on poisoned documents. Building on these findings, we propose \texttt{D-SCAN} (Document-level Signal Collapse Analysis), a lightweight detection framework that monitors attention dynamics to identify attacked generations. Extensive experiments on multiple attack benchmarks demonstrate the effectiveness of our method. Moreover, D-SCAN can detect attacks even when they fail to alter the final answer. Code is available at this https URL.

---


### 116. [Summarize First, Download Later: Onboard VLMs for Bandwidth-Efficient Earth Observation](https://arxiv.org/abs/2608.06959)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junghwan Park, Sangcheol Sim, Woojin Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Earth observation (EO) satellites carry increasingly advanced sensors that produce vast volumes of high-resolution, multispectral data, yet downlink capacity remains a critical bottleneck -- often causing significant latency or the loss of valuable observations within limited contact windows. We propose a "Summarize First, Download Later" paradigm that exploits recent advances in onboard edge computing and Vision-Language Models (VLMs). Rather than indiscriminately downlinking raw imagery, the system follows a three-phase interaction protocol: the satellite first transmits concise natural language summaries generated by a quantized onboard VLM; ground operators then issue targeted Visual Question Answering (VQA) queries to verify scene relevance (e.g., wildfires or maritime anomalies); and full-resolution images are downloaded only when critical information is confirmed. This transforms the downlink from passive bulk transfer into an active, semantics-aware dialogue. We implement and evaluate the system on a resource-constrained NVIDIA Jetson platform, and experiments on diverse remote sensing scenes show that the proposed strategy substantially reduces bandwidth consumption while accelerating time-to-insight for time-sensitive missions.

---


### 117. [Generative Embedding Benchmark: How Much Information Survives in a Dense Embedding?](https://arxiv.org/abs/2608.06972)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yun Li, Biao Yang, Peixi Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embeddings have emerged as a standard representational interface linking foundation models with downstream systems. Most embedding benchmarks assess representations through discriminative tasks or geometric criteria centered on separability in embedding space. However, strong performance on such evaluations does not establish whether content compressed into an embedding remains accessible to a downstream generator. To address this gap, we introduce the Generative Embedding Benchmark (GEB), in which a decoder answers questions using only a frozen embedding and question text, without access to the original image or intermediate visual features. Answer quality under this readout measures generative information: the answer-relevant content recoverable from an embedding. GEB includes a curated visual-question-answering dataset with a 1,800-item development split and a held-out 900-item test split covering natural images, scene text, and visual documents. Using a common decoder and training recipe, we evaluate seven public embedding models in visual-only and vision-language joint modes. On the test set, visual-only scores range from 28.25 to 33.21; with image-question joint encoding, all five VLM-based embedding models score higher, and the best reaches 65.56. Matched embeddings also outperform text-only inputs, zero embeddings, and shuffled embeddings. Natural-image information is much easier to recover than scene text or visual-document information, while a Qwen3-VL-2B reference with access to the original image reaches 84.30. Together, these results show that generative readout exposes information bottlenecks that separability-based evaluation does not capture.

---


### 118. [PHASE-Tree: Modeling Character-State Evolution in Long-Horizon Role-Playing Dialogue](https://arxiv.org/abs/2608.06975)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bo Tang, Jianan Yang, Junyi Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon role-playing demands that characters remain recognizable as they evolve with the narrative. Yet existing work falls short on two fronts: representations are typically static profiles that cannot be updated locally without destabilizing unchanged traits, and benchmarks mainly test persona preservation and memory recall rather than whether a model speaks from a character's currently evolved state. We address both. PHASE-Tree is a multi-timescale character-state tree with an immutable identity root and mutable persona, session, and moment layers, making each mutable field an addressable target for localized within- and cross-episode updates. It conditions generation through explicit textual provision or implicit parametric adaptation. To measure evolved-state generation, we introduce LongEvoRoleBench, which pairs four long-dialogue corpora for cross-episode evolution with four short-dialogue corpora as within-scene state-tracking checks, under a unified next-utterance protocol. On the long-dialogue core, textual PHASE-Tree ranks first in 11 of 12 dataset-metric cells against internal variants and all 12 cells against external textual baselines, improving character-level, semantic, and embedding scores by 19.7%, 12.4%, and 15.1% respectively. In a blinded 200-response study, human ratings correlate with the GPT-4.1 judge (Pearson r= 0.65); on descriptive n= 10 PT and NR prompt subsets, the Overall difference is +0.20. The long-dialogue Sem advantage persists across LLM judges and generation backbones.

---


### 119. [Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression](https://arxiv.org/abs/2608.07001)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haolin Tian, Yuzhe Liu, Tonghan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck. Existing KV cache compression methods rely on predefined, fixed compression rules and are typically developed around either token eviction or merging. As a result, cache resources can neither flow freely across layers, heads, and context slots, nor be jointly allocated to balance local resolution and information coverage. Therefore, we propose GraceKV, a global approach for the allocation of resolution and coverage in KV cache compression, and formulate the compression process as a global resource allocation problem under a fixed cache budget. GraceKV treats each layer-KV head-slot combination as an atomic unit and builds a prototype tree. Leaf nodes correspond to token-level KV entries, while each internal node uses a single prototype to compress the KV space covered by its children. A set of non-overlapping nodes in the tree forms the representation of an atomic unit. Adding the root of a new tree expands information coverage, whereas splitting a selected node improves local resolution. All candidate actions compete globally for a shared cache budget. Finally, the nodes retained across all trees form the compressed KV cache. This process adaptively determines the allocation of cache resources among atomic units globally and the balance between resolution and coverage. GraceKV requires no additional training, and the entire compression and inference process is performed on the GPU. Systematic experiments across diverse long-context tasks and compression ratios show that GraceKV ranks first in 24 of 32 settings and remains robust up to 128-fold compression. These results validate the effectiveness of global budget allocation in coordinating information coverage and local resolution.

---


### 120. [ReQuant: Fixed-Grid Discrete Refinement for Post-Training Quantization](https://arxiv.org/abs/2608.07019)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yongge Ma, Guoan Wang, Feiyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is widely used to reduce the memory and computational cost of large language models. Existing PTQ methods typically obtain an initial quantized model through heuristic rules or greedy optimization, and once quantization is completed the resulting integer assignments are usually treated as final. This observation motivates a complementary optimization stage within PTQ that keeps quantized weights improvable after an executable quantized model has been produced, while preserving the quantized format. We introduce ReQuant, a backpropagation-free fixed-grid refinement procedure for this stage. Agnostic to the PTQ initializer, ReQuant takes an existing quantized model as a feasible starting point and iteratively revisits its discrete weight assignments on the fixed quantization grid. Accepted updates strictly reduce the mean squared reconstruction error and remain on the original grid. In this way, ReQuant turns the initially fixed PTQ output into an iteratively optimizable discrete solution and serves as a plug-and-play post-processing stage for existing PTQ pipelines. Experiments across diverse model families, bit-widths, and downstream tasks show that ReQuant consistently improves quantized models from heterogeneous PTQ initializers, with especially large gains on simple initializers and lower bit-widths. Notably, ReQuant can refine a simple round-to-nearest initialization across multiple sweeps until it approaches or surpasses GPTAQ under the same quantization format. These results establish ReQuant as a practical complementary stage for further improving existing PTQ pipelines.

---


### 121. [An Agentic Hybrid Top-Down and Bottom-Up Approach to Knowledge Graph Generation](https://arxiv.org/abs/2608.07023)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Emma Jouffroy, Warren Jouanneau, Marc Palyart  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizing thousands of unstandardized, multilingual expertise declarations is a persistent challenge for Human Resources (HR) platforms, directly impacting downstream tasks like accurate talent matching. To address this, we propose a hybrid knowledge graph generation pipeline that grounds a Large Language Model (LLM) in the Wikidata multilingual Knowledge Graph (KG) while employing an agentic reflexion pattern to synthesize emerging concepts and their associated metadata. Unlike rigid top-down methods or fragmented bottom-up approaches, our system anchors recognized concepts to stable Knowledge Graph entities while dynamically creating new nodes and relational metadata for unrecognized skills. Executed across five stages, entity reconciliation, multilingual canonicalization, active curation, deduplication, and the iterative recovery of unmapped concepts, the system autonomously adapts to rapidly evolving, noisy skill mentions across five European languages. Ultimately, this pipeline provides a highly scalable, explicable, and self-healing framework for generating a comprehensive skills knowledge graph, from which a structured taxonomy is derived, using unstructured, noisy text.

---


### 122. [Not All Problems Are Best Modeled as MILP: A DSL-Centric Framework for Flexible and Accurate Optimization Modeling](https://arxiv.org/abs/2608.07040)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shaofeng Zhang, Hongyuan Su, Qingwen Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solving combinatorial optimization problems (COPs) requires not only efficient algorithms but also carefully crafted formulations. While recent works have leveraged LLMs to automate optimization modeling, current frameworks predominantly rely on a rigid mixed-integer linear programming (MILP) paradigm. In this paper, we argue that not all problems are best modeled as MILP, as forcing complex domains into linear constraints can induce prohibitive modeling complexity and severely restrict solver flexibility. To address this, we propose OptiDSL, a framework that shifts the focus from rigid MILP formulations to domain-specific language (DSL) representations. By utilizing LLMs to map natural language onto standardized, domain-accepted structures, OptiDSL decouples problem formulation from execution. This paradigm enables seamless integration with a diverse library of specialized solvers, ranging from traditional heuristics to modern learning-based methods. Experimental results on the comprehensive benchmark of 44 COP types show that OptiDSL significantly surpasses MILP-based pipelines, yielding a 51.66% gain in formulation accuracy and a 91.71% decrease in modeling time. Notably, it also outperforms MILP-based pipelines on the existing benchmark, achieving a 23.09% higher formulation accuracy. Our code is available at this https URL.

---


### 123. [YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family](https://arxiv.org/abs/2608.07051)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xu Lin, WenJie Nie, Jinlong Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generic parameter-efficient fine-tuning (PEFT) methods transferred from language models can fail silently on real-time detectors, whose heterogeneous operators and detection-specific components impose placement constraints absent from regular Transformer stacks. We propose YOLO-PEFT, a structure-aware framework that formulates adapter placement as an auditable constraint-planning problem. Given a detector graph, a PEFT request, and a resource budget, YOLO-PEFT assigns operator and semantic roles, evaluates explicit operator-validity, detector-semantic, graph-interface, and deployment predicates, records a reason code for each excluded module, and either emits a budgeted target-module plan or returns Refuse before training. Under the official VOC07+12 trainval-to-VOC07 test protocol, planner-selected RS-LoRA reaches 0.7138 and 0.7307 mAP50-95 on YOLO11s and YOLO12s, respectively, compared with 0.6428 and 0.6662 for Full-SFT. On RT-DETR-L, all seven evaluated LoRA-family configurations cross the predefined catastrophic threshold, supporting a calibrated Refuse-to-Full-SFT decision within the evaluated coverage. A controlled YOLO11 audit further shows that LoRA reduces peak training memory by 43.9 percent, although training takes 1.72 times longer. Within the evaluated detector families, placement policies, and calibration coverage, YOLO-PEFT replaces manual target-module trial and error with explicit, inspectable planning while preserving verified train-save-merge-export paths; refusal on unseen detector architectures remains an open validation problem. Project Page: this http URL

---


### 124. [Explanation Stability of Test-Time Adaptation in Computational Pathology: A Large-Scale Benchmark](https://arxiv.org/abs/2608.07062)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** R. G. Bahumanya, Harshith V. M., Shreyank N. Gowda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) has become a practical way to adapt deployed models to unlabeled target data, a setting that is especially relevant in computational pathology where staining, scanner, and cohort shifts are routine. While most TTA methods are evaluated by their effect on accuracy, clinical use also depends on whether the model's explanations remain reliable after adaptation. In this paper, we take a closer look at this largely unmeasured effect. We study explanation stability under TTA across two histopathology benchmarks, Camelyon17 and NCT CRC-HE, using five architectures ranging from convolutional networks to vision transformers and a pathology foundation model, seventeen TTA methods, and four attribution families. Across 2,958 adaptation runs, we observe a clear and systematic pattern: TTA methods differ sharply in how much they move model explanations, with frozen-backbone methods leaving attributions almost unchanged and continual methods such as CoTTA and RoTTA causing the largest drift. This effect is not uniform. Convolutional networks are substantially more sensitive than transformer and foundation-model backbones, and explanation drift increases with adaptation strength while remaining largely insensitive to batch size. Surprisingly, explanation stability is only weakly coupled to adaptation quality. Some methods preserve explanations almost perfectly while degrading calibration or accuracy, producing silent failures that would be missed by accuracy-only or explanation-only evaluation. These findings show that explanation stability is a distinct reliability axis for TTA in computational pathology. We release the metric, protocol, and full benchmark to support future work on adaptation methods that are not only accurate, but also stable and clinically auditable. Code: this https URL

---


### 125. [International Transfer of Stochastic Cortical Self-Reconstruction](https://arxiv.org/abs/2608.07092)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fabian Bongratz, Zhizheng Zhuo, Chao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stochastic cortical self-reconstruction (SCSR) enables personalized mapping of gray matter atrophy, a hallmark of neurodegenerative disorders such as Alzheimer's disease (AD), onto high-resolution cortical surfaces. Unlike conventional normative modeling approaches, which typically operate at a coarse regional level and remain inherently constrained by the covariates included during training, SCSR estimates an individualized healthy reference directly from the observed cortical thickness at the vertex level. This allows the detection of subtle, subject-specific deviations from healthy cortical shape. In this work, we investigate the generalization and transferability of SCSR, originally trained on UK Biobank (UKB) data, to an independent Chinese population dataset. Specifically, we evaluate the ability of SCSR-derived Z-scores to discriminate between healthy scans, individuals with mild cognitive impairment (MCI), and patients with AD, while also assessing model robustness across the lifespan. We compare four training strategies: direct application of the UKB-trained model, fine-tuning on Chinese data, training from scratch, and joint training on UKB and Chinese cohorts. As reconstruction backbones, we consider both a multilayer perceptron (MLP) and a Spherical UNet (SUNet). Our results demonstrate that SCSR provides robust detection of cortical atrophy in the Chinese population across all evaluated models. The highest discriminative performance was achieved by the fine-tuned SUNet model (average pairwise AUC = 0.848), followed closely by the UKB-trained SUNet. Moreover, reconstruction errors remained low across the lifespan, even when the training population exhibited a substantially narrower age distribution, indicating strong cross-population transferability.

---


### 126. [UncertaintyVis: Preserving Linguistic Uncertainty in Automated Text-to-Chart Generation](https://arxiv.org/abs/2608.07093)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Songheng Zhang, Emily Aurelia, Anthony Tang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data-rich documents pair narrative text with quantitative claims, and authors routinely qualify those claims with linguistic uncertainty markers such as "nearly," "approximately," or "at least." Automated text-to-chart systems discard these markers, producing visualizations that appear definitive even when the source text expresses hedged or incomplete knowledge. Readers may then over-interpret precision and misjudge author intent. We present UncertaintyVis, a system that preserves linguistic uncertainty during automated chart generation. A formative corpus analysis of 211 uncertainty expressions across 12 documents and 8 domains yielded a four-category taxonomy: Surface Form Normalization, Precision Boundaries, Inferential Derivation, and Non-Inferable Gaps. We mapped each category to chart-specific visual encodings that signal uncertainty without disturbing the spatial integrity readers rely on, and implemented an end-to-end pipeline pairing large language model text analysis with uncertainty-aware rendering. In a two-part study with 12 participants, readers matched charts to source text with 85% accuracy and text to charts with 76%. Uncertainty-aware visualizations trended toward lower cognitive demand (effect sizes 0.460 and 0.769 for mental demand and effort), and 75% of participants preferred them to plain text, describing explicit uncertainty encodings as a basis for verifying data claims. Encoding effectiveness varied by chart type: bar and pie encodings performed consistently, while line chart encodings require redesign.

---


### 127. [SoK: Cryptographic Key Recovery for Cryptoasset Custody and Financial Technologies](https://arxiv.org/abs/2608.07104)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Francisco Javier Becerra Sanchez, Antonio Ken Iannillo, Radu State  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptoasset systems often bind cryptographic key control to financial control: losing a wallet seed, custody share, hardware device, or smart-account credential can remove spend authority, while compromised recovery can enable theft. Existing work treats recovery through separate vocabularies--key backup, secret sharing, account recovery, credential re-issuance, social recovery, and asset migration--making mechanisms and tradeoffs difficult to compare.
This paper presents a Systematization of Knowledge (SoK) on cryptographic key recovery for cryptoasset custody and financial technologies. Starting from a 118-paper systematic-review discovery corpus, we derive a 77-paper synthesis corpus and code each retained system in a master matrix covering recovered objects, recovery semantics, mechanisms, enrollment and storage, authorization, trust placement, failure events, post-recovery state, validation evidence, deployment status, privacy, usability, and limitations. The matrix supports an axis-first taxonomy that separates secret-restoring, hybrid, control-restoring, forensic/extractive, and framework-oriented recovery.
Our central observation is that recovery is not a single operation: systems may reconstruct an original secret, regenerate a seed, restore a share, reissue a credential, migrate signing authority, restore account control, move assets, or extract forensic artifacts. We derive a generalized construction model, check it against production-facing designs, and identify six findings: recovery semantics are heterogeneous; recovery shifts trust; liveness improvements create abuse paths; post-recovery lifecycle management is uneven; protocol evidence outpaces user evidence; and recovery metadata remains underprotected. These gaps motivate a research agenda for recovery-aware financial technologies.

---


### 128. [Beyond Fluency: A Clinical Benchmark and Anomaly-Enhanced Baseline for Spine MRI Report Generation](https://arxiv.org/abs/2608.07117)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bruno Palau, Franziska Vogt, Daria Laslo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology reporting is time-consuming and subject to inter-rater variability, making automated report generation an attractive clinical application for Vision-Language Models (VLMs). We benchmark state-of-the-art VLMs on lumbar spine MRI with a focus on diagnostic accuracy and demonstrate that standard lexical and semantic metrics poorly reflect clinical correctness: fluent, well-structured reports can score highly while containing clinically meaningful diagnostic errors. To address this failure mode, we propose an architecture-agnostic framework that augments VLM inputs with spatially localized, disc-level anomaly heatmaps generated by a semi-supervised U-Net++ model. These heatmaps both improve anatomical sensitivity through explicit visual grounding and provide an independent interpretability output for clinical oversight, moving us closer to diagnostically reliable, visually grounded VLMs for lumbar spine MRI interpretation.

---


### 129. [PHOENIX: Fine-Tuned SLM-Powered Autonomous Satellite Lifetime Extension via Predictive Self-Healing and Multi-Agent AI Recovery](https://arxiv.org/abs/2608.07126)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sumaiya Islam, Harsha Kumara Moraliyage  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Most CubeSats, small and low-cost satellites roughly the size of a shoebox, do not survive as long as they were designed to: a study of 178 missions found that only 48-65% remain operational after two years, against a designed lifetime of 2-5 years. The deeper issue is that a CubeSat in low Earth orbit (LEO) is physically unreachable from the ground for roughly 85 minutes out of every 96-minute orbit, so faults that start during that window go unnoticed until the next contact pass, by which point recovery may no longer be possible. We propose PHOENIX (Predictive Health On-orbit Edge Neural Intelligence eXtension) to give the satellite its own fault reasoning capability. A fine-tuned Small Language Model (SLM) compact enough to run on embedded hardware is deployed onboard the CubeSat, running on the flight-proven Aethero NxN-ECM computer, monitoring all sensor readings continuously, and resolving recurring faults using a memory system that stores past repairs so the same inference does not need to run twice. Once per orbit it sends a short structured health report to the ground instead of a raw data dump; six specialized AI agents on the ground read that report and generate validated satellite commands within the 5-10 minute contact window. A generative diffusion model (DDPM) creates synthetic training data because real fault examples make up only 0.57-1.80% of the dataset. We report preliminary results on the ESA Anomaly Detection Benchmark (14 years, 76 channels, 118 labeled faults).

---


### 130. [Human-AI Perceptual Alignment by Playing Hues and Cues](https://arxiv.org/abs/2608.07141)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nuria Alabau-Bosque, Jorge Vila-Tomás, Paula Daudén-Oliver 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating the perceptual alignment between Contrastive Vision-Language Models (CVLMs) and humans is typically constrained by traditional benchmarks that overlook fine-grained semantic and cultural nuances. In this work, we propose a novel evaluation framework that leverages the gamified, discrete color space of the board game Hues and Cues. By mapping the board's 480 color cells to the CIE xy chromaticity diagram, we calculate empirical perceptual distances across a carefully curated 100-word vocabulary spanning seven semantic categories. To properly contextualize model performance, we establish an empirical lower bound of expected error-the Human Consistency baseline-calculated via Leave-One-Out (LOO) cross-validation on a dense dataset of color associations collected from 325 human observers through a custom digital interface. We evaluate 162 models across multiple architectural families and pre-training datasets to assess their semantic color grounding. Our results demonstrate that while CVLMs successfully replicate human cognitive biases, such as idealized memory colors for concrete physical referents (e.g., food and plants), they systematically diverge from the human baseline in abstract, subjective, and pop-culture domains. We identify two distinct failure modes in severely misaligned concepts: semantic misclassification and a systematic uncertainty collapse into a default blue coordinate. Furthermore, we reveal that highly curated pre-training datasets are significantly more effective than massive, uncurated corpora in mitigating these severe misalignments. Ultimately, this work highlights that despite their broad categorization capabilities, current CVLMs still fail to capture the nuanced, localized consensus of human color memory, emphasizing the value of gamified tasks in exposing underlying model biases. The data and code are publicly available to test other metrics.

---


### 131. [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](https://arxiv.org/abs/2608.07147)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xucong Wang, Zhe Zhao, Liheng Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for training coding agents, where the execution feedback from compilation and tests provides objective verification. However, unlike agent tasks, coding agents face a unique and finer-grained credit assignment challenge: at each step, coding actions simultaneously pack varying changes into different regions of a code version, which makes the contribution of independent change indistinguishable. Existing RLVR methods mostly leverage the outcome reward or step-level reward, which fails to dive into a code diff and makes unique properties of coding actions invisible to training. In this paper, we propose Diff-in-Diff Policy Optimization (DiDPO), a critic-free RL method that constructs fine-grained credit units directly from the structure of code diffs. DiDPO organizes multi-turn coding interactions into multiple thought--action steps and discovers code diffs across sampled trajectories. It then selects anchors by aggregating highly similar sub-diffs split from each whole diff by our ``groupability score'', which provides the splitting schema that optimally balances the semantic scope of anchors and the group mass they may form. Finally these anchors form advantage groups and project the diff-level advantage back to individual response tokens. Experiments on long-horizon coding and reasoning benchmarks show that DiDPO significantly outperforms strong agentic RL baselines. On Qwen2.5-7B-Coder, DiDPO exceeds comparable methods by over 10\% and narrows the gap with far larger models, offering a principled framework for fine-grained credit assignment in coding agent training. We also open-source verl-code, an agentic rl codebase that supports various RL methods and coding benchmarks.

---


### 132. [Representation-driven Endoscopic Visual Embedding Alignment for Latent Generation](https://arxiv.org/abs/2608.07176)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Francisco Caetano, Tim J.M. Jaspers, Haiko Middeljans 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing foundation generative models for endoscopy is limited by the gap between natural and clinical images and the computational cost of training large Diffusion Transformers. Although representation alignment has improved efficiency in general computer vision, its role within the highly specialized endoscopic image space remains unclear. We introduce REVEAL (Representation-driven Endoscopic Visual Embedding Alignment), the largest generative foundation model for endoscopy to date, trained on GastroNet-5M (GN-5M), a multicenter dataset of 5 million endoscopic frames. Instead of depending on out-of-domain priors, REVEAL employs encoders pretrained directly on the endoscopic distribution to align diffusion latents with domain-specific visual features, preserving fine textures and intricate anatomical structures. Beyond image generation, REVEAL also serves as a powerful feature extractor; in multiple benchmarks, it delivers performance that is competitive with, and in several cases exceeds, endoscopic foundation models such as EndoViT and Endo-FM, specifically tuned for classification tasks, while demonstrating strong representation robustness under realistic imaging corruptions. REVEAL produces high-fidelity images and maintains robust structural coherence in latent-space edits such as inpainting and outpainting. This high-capacity backbone lowers the computational threshold for building specialized clinical tools, offering an open, versatile foundation for conditional synthesis, segmentation, and out-of-distribution detection in future intelligent gastroenterology systems.

---


### 133. [EMAS: Stabilizing Multi-Agent System Evolution through Evidence-Guided Revision](https://arxiv.org/abs/2608.07196)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chao Fei, Qingyi Si, Kaihua Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many methods for automated multi-agent system design optimize prompts and topologies during an initial design stage and then deploy the resulting system unchanged on subsequent samples. Experience from these samples is rarely consolidated into reusable system updates, while accuracy-oriented designs may incur high token costs. We introduce EMAS (Evolving Multi-Agent System), which uses this experience to revise MAS topology and prompts without updating LLM parameters, either to improve accuracy or to reduce cost. EMAS converts traces into structured diagnoses that specify a revision operation and target. It generates a candidate revision only when the same diagnosis recurs across samples and applies it only if paired validation against the current MAS meets the corresponding acceptance criterion. Across four benchmarks and two LLMs, EMAS attains the highest task-weighted overall accuracy for both backbones and is best or tied in six of eight model--benchmark settings. Within two evolution epochs, EMAS achieves relative gains of 6.30% and 20.10% in task-weighted accuracy on Kimi-K2-6 and Qwen3.6-27B, respectively. On MBPP with Qwen3.6-27B, EMAS raises accuracy from 55.09% to 89.12% while reducing token use per task by 62.2%. These results show that EMAS can turn experience from new samples into reusable updates to MAS topology and prompts.

---


### 134. [Skaling: Chinchilla's Exponents Meet Kaplan's Coupling](https://arxiv.org/abs/2608.07222)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mathurin Videau, Badr Youbi-Idrissi, David Lopez-Paz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural scaling laws are foundational for language model development, yet standard formulations systematically under- and overestimate loss at data-scarce and overtraining extremes. This failure originates in the underlying assumption that model size and training data impact the loss independently. To address this, we introduce the Skaling law, a generalized functional form that couples model capacity and data through a single interaction exponent. This simple extension reduces the Mean Absolute Percentage Error (MAPE) by 1.5-3x across both interpolation and extrapolation regimes. When paired with a sparse grid strategy restricted to low-compute regimes, the Skaling law achieves accurate full-grid extrapolation using approximately 10x less compute than uniform sweeps. By enabling reliable performance prediction from small-scale experiments, the Skaling law provides a more robust and resource-efficient framework for allocating compute budgets in next-generation model training.

---


### 135. [Stochastic Autoregressive Learning](https://arxiv.org/abs/2608.07224)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ilan Doron-Arad, Idan Mehalel, Elchanan Mossel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by LLMs, which generate outputs by iteratively sampling from next-token distributions, we introduce a PAC-learning model for binary stochastic autoregressive learning. This generalizes the deterministic autoregressive learning framework of Joshi et al., COLT 2025. In our model, one fixed generator assigns a Bernoulli next-token distribution to every prompt string. Starting from an input prompt, a token is sampled and appended to the prompt; the same generator is then applied again to this expanded prompt; this procedure is repeated for $M$ steps. Three forms of supervision are considered: base one-step samples, chain-of-thought (CoT) samples that reveal full random trajectories of length $M$, and end-to-end (e2e) samples that reveal only the final token of length $M$ trajectories. For a generator class, we study the minimum number of samples $m_{base}(\varepsilon),m_{CoT}(\varepsilon), m_{e2e}(\varepsilon)$, resp., required to learn the one-step probabilities in the base model, and the final-token probability in the CoT and e2e models, under squared loss error~$\varepsilon$.
We show that stochastic autoregressive learning fundamentally differs from the deterministic theory. At scale $\varepsilon$, there is no universal comparison between the three learning tasks: both $m_{CoT}/m_{base}$ and $m_{e2e}/m_{CoT}$ can be made simultaneously arbitrarily larger than $M/\varepsilon$, the natural analogue for the existing deterministic results. Nevertheless, after altering scales, for every class, CoT learning at scale $\varepsilon$ is upper-bounded by base learning at scale $\varepsilon/M^2$, whereas e2e learning at scale $\varepsilon$ is upper-bounded, up to logarithmic factors, by $(M/\varepsilon) m_{CoT}(\Theta(\varepsilon))$. These dependencies and scales are essentially tight. We complement these bounds by studying dimension $d$ logistic functions in our model.

---


### 136. [WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN](https://arxiv.org/abs/2608.07267)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuehao Huang, Yunzi Wu, Xiaotao Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent vision-language navigation (VLN) systems increasingly adapt pretrained vision-language models (VLMs) into vision-language-action (VLA) policies that map egocentric observations and language instructions directly to navigation actions. Although semantically capable, such action-centric training does not explicitly model how the agent's visual observations should evolve under its predicted motion. Generative world-action models (WAMs) jointly predict future observations and actions, yet existing WAMs for continuous VLN do not condition joint future-view and action generation on geometry-aware representations inferred from the observed history. We present WNM-3D, a generative World Navigation Model with 3D scene conditioning for continuous VLN. To consolidate past observations into persistent scene context, a frozen feed-forward geometry encoder extracts geometry-aware representations from the monocular egocentric RGB history, and a trainable 3D Scene-to-Token Adapter converts them into a fixed-length prefix in the token space of the world-action Diffusion Transformer. Through block-causal attention, this prefix conditions every future video-action block, providing a shared geometric context for both future-view and action generation. We train WNM-3D through supervised world-action fine-tuning on A*-generated demonstrations, DAgger-style adaptation on policy-visited states, and DanceGRPO-based closed-loop policy optimization. Experiments on GN-Bench show that WNM-3D outperforms strong VLM-based navigation policies and its 2D-conditioned counterpart in closed-loop navigation. On a fixed near-goal evaluation set, WNM-3D also achieves higher flow-action consistency and lower visual-motion error.

---


### 137. [Gaze Behavior in Visual World Experiments Can be Modeled With Off-the-shelf Language-Vision Encoders](https://arxiv.org/abs/2608.07282)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rahul Murali Shankar, Titus von der Malsburg, Sebastian Padó  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The recent advances in neural language models have also spurred much work in computational psycholinguistics, asking whether neural LMs are also promising models of human language processing. However, work has been overwhelmingly focused on the unimodal case of written or spoken language. In contrast, multimodal experimental paradigms, like visual world studies that present participants with both visual and linguistic input simultaneously, have been neglected. In this paper, we present a novel approach that predicts gaze behavior in visual world studies. It does so by combining a simple multi-modal bi-encoder model of the CLIP family with a bimodal attribution method. We demonstrate the ability of this approach to robustly replicate the results of a seminal English visual world study which shows hu- man predictive processing. Remarkably, it does so without a generative architecture and without the need for fine-tuning, despite not being trained for this task.

---


### 138. [A foundation-model approach to pediatric headache classification from rs-fMRI](https://arxiv.org/abs/2608.07287)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guilherme S. Imai Aldeia, Clara Moon, Julie Shulman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Headache is the most common neurological disorder in children and substantially affects quality of life. We investigated whether resting-state functional MRI (rs-fMRI) can support pediatric headache classification using machine learning. We encoded rs-fMRI data using NeuroSTORM, a recent foundation model, and fine-tuned it to distinguish healthy controls from children with headache and subsequently classify headache subtypes. We compared NeuroSTORM with a standard neuroscience approach using functional-connectivity (FC) matrices derived from brain activity as predictors. Using 189 rs-fMRI scans from 110 individuals collected across two visits (prevalence of any headache: 74%), NeuroSTORM achieved an area under the receiver operating characteristic curve (AUROC) of 0.82 (95% CI, 0.82-0.82) and an area under the precision-recall curve (AUPRC) of 0.93 (95% CI, 0.93-0.94) for discriminating headache from non-headache. In contrast, models trained on FC matrices showed lower performance (AUROC, 0.67 [95% CI, 0.67-0.67]; AUPRC, 0.85 [95% CI, 0.85-0.85]). In multiclass classification of healthy controls, chronic migraine, and non-chronic headaches (e.g., post-viral headache, new daily persistent headache, post-traumatic headache), NeuroSTORM achieved a macro-AUROC of 0.69 (95% CI, 0.68-0.69). Results suggest that the approach can distinguish chronic migraine but has difficulty differentiating other headache subtypes from chronic migraine. Overall, under limited-data conditions, NeuroSTORM appears to capture latent rs-fMRI representations that transfer to headache-related tasks without relying on FC features. These findings provide proof of concept for fMRI-based prediction of pediatric headache and highlight potential future utility for subtype identification and individualized treatment strategies.

---


### 139. [Learning Long-Term Educational Investment Policies under Residential Sorting](https://arxiv.org/abs/2608.07295)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Honglei Guo, Shuo Chen, Mingjie Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Allocating public-school investment effectively and fairly is difficult when school access depends on residence. School improvements can raise nearby housing demand and prices, reshape enrollment, and potentially limit access for lower-income households. These effects evolve as residential sorting changes school composition, quality, and future investment needs. Existing approaches often study school funding, household choice, and housing markets separately, while static models can miss their interconnected, long-term effects. We address this gap with a dynamic multi-agent framework that links government investment, household sorting, housing prices, population turnover, enrollment, and evolving school quality. A government planner uses reinforcement learning (RL) to identify multiyear allocation policies that account for household responses while balancing aggregate educational access and equity. In simulations, our RL-based policy attains the highest access level (0.4780) and second-lowest access Gini coefficient (0.0164) among representative baselines, demonstrating a favorable effectiveness-equity balance. The results also indicate reduced socioeconomic stratification in educational access. By making education-housing feedback explicit, our framework supports long-term analysis of how school investment shapes educational opportunity over time.

---


### 140. [Natural Language Processing Psychometrics](https://arxiv.org/abs/2608.07316)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Edoardo Sebastiano De Duro, Emma Franchino, Massimo Stella  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Processing (NLP) models predicting mental health outcomes rarely specify what they measure: contextual knowledge, emotional content, or syntactic structure. NLP Psychometrics treats psychological prediction from text as a psychometric problem, linking scores to interpretable linguistic evidence and testing beyond the training text format. Nine LLMs, conditioned on controlled personas (cognitive digital shadows), completed psychometric questionnaires with textual explanations per item. We extracted emotional profiles and syntactic-semantic structure via textual forma mentis networks, combined with personality and sociodemographic variables in ablated random forest (RF) regressors, using SHAP to identify which features drove performance and in which direction. Full RF models explained up to 70.8% of variance in life satisfaction (SWLS), 55.7% in depression (PHQ-9), and, for DASS-21, 68.5% depression, 76.0% anxiety, 72.4% stress. Sociodemographics alone explained no meaningful variance in depression, anxiety, or stress, but did so for life satisfaction, where emotion features and income were the strongest predictors; neuroticism and network topology instead dominated depression and anxiety, reversing direction between them. Without retraining, RF models separated diaries from low- and high-score personas ($r$ up to 0.91) and, using only network/emotion features, classified clinical from control participants in real transcripts with up to 68% accuracy. These results show the promise and limits of synthetic data: LLM personas can expose model biases, recover patterns consistent with clinical rumination, and support psychometric prediction from human text without a matched questionnaire, but cannot substitute for human validation. NLP Psychometrics makes these distinctions explicit, measurable, and testable through interpretable AI and network/emotional features.

---


### 141. [An End-to-End Agent Auditing Engine](https://arxiv.org/abs/2608.07346)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoning Wang, Mingxun Zhang, Chenyue Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models (LLMs), harnesses have become essential infrastructure for deploying agents across a wide range of domains. The fast-evolving harness ecosystem has also made rigorous capability evaluation increasingly important. However, efficiently building an end-to-end, systematic, and comprehensive evaluation pipeline remains a significant challenge. To address this challenge, we introduce $A^2E$ (Agent Auditing Engine), an end-to-end evaluation engine designed for agent harnesses. $A^2E$ leverages our newly proposed Agent Task Protocol (ATP) to enable the rapid integration of evaluation tasks with different harnesses. Through an automatically instrumented Monitor, it captures and generates standardized execution traces during experiments. In the Evaluation stage, $A^2E$ systematically assesses harness capabilities using a suite of multidimensional metrics. Compared with correctness alone, these metrics provide a more fine-grained characterization of differences among harnesses in execution efficiency, tool use, task planning, and error recovery. Experiments conducted with $A^2E$ further reveal that model-harness combinations exhibit substantial performance variation across different types of tasks, and that no single combination consistently outperforms all others across every task. These findings not only demonstrate the necessity of systematic evaluation but also provide useful guidance for the co-evolving of models and harnesses. Our code is available at this https URL.

---


### 142. [LitTraceQA: A Benchmark for Multi-Stage Grounding and Verification in Scientific Question Answering](https://arxiv.org/abs/2608.07370)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuye Liu, Yimu Wang, Peng Shi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific literature is increasingly used as a knowledge source for language models, retrieval-augmented generation systems, and research assistants, but answering research questions from papers requires more than fluent generation. A reliable system must identify the relevant papers, locate the concrete evidence that supports the answer, and produce a response that is faithful to that evidence. We present LitTraceQA, a benchmark for literature-grounded question answering over scientific papers. Given a research question and a metadata pool of papers, a system must return three connected outputs: canonical paper identifiers, supporting evidence locations, and answers in one or more requested formats, including free-form text, multiple-choice answers, and structured tables. LitTraceQA targets evidence types common in scientific reading: tables, figures, text spans, equations or algorithms, and citation contexts. The public development split contains 55 examples, including 26 hidden-source single-paper questions and 29 multi-paper questions, and provides gold papers, evidence annotations, and answers for local validation. We also analyze a larger final annotation collection with 4,978 unique-question records over 4,859 unique gold papers. By evaluating paper retrieval, evidence grounding, and answer accuracy separately, LitTraceQA provides a testbed for scientific QA systems that produce verifiable answers rather than unsupported summaries.

---


### 143. [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.07371)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoyu Zheng, Yun Zhu, Qing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent agentic reinforcement learning methods use hindsight to complement sparse outcome rewards. However, a completed rollout can yield many such signals, leaving their appropriate allocation across turns unclear. We introduce TRIAL, a trajectory-relative hindsight distillation framework with a unified turn-aligned scoring protocol. For each decision turn, TRIAL extracts an outcome view of that decision's realized consequence and evaluates the same response under ordinary and hindsight-conditioned contexts. The signed log-probability gap determines the direction and local strength of token-level supervision, while turn-level magnitudes are normalized jointly over the realized trajectory. The resulting allocation multipliers have an eligible-token-weighted mean of one, redistributing dense supervision across turns while fixing its average multiplier. Experiments on WebShop and ALFWorld with different backbones show that TRIAL outperforms GRPO across all eight combinations of backbone, environment, and evaluation metric, while achieving the best or tied-best performance among six methods on six of them. On WebShop with Qwen3-1.7B, TRIAL improves the success rate from 56.4% to 75.2% and the task score from 78.7% to 85.7%. Controlled ablations further show that trajectory-relative turn allocation provides substantial gains beyond those of dense hindsight distillation alone.

---


### 144. [I Seek You in Videos: Identity-Conditioned Queries for Person-Centric Video Reasoning](https://arxiv.org/abs/2608.07417)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shibo Gao, Chongxiao Wang, Chenglong Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world video reasoning often involves multimodal, multi-source inputs, whereas existing video reasoning tasks typically assume a simplified video-text setting, limiting identity matching and person-centric reasoning. To bridge this gap, we introduce the Identity-conditioned Queries (ICQ) task, in which models are required to jointly associate and interpret an input video and a reference image of a person, and leverage this conditioning to address identity grounding, behavior understanding, and temporal reasoning, among other challenges. Building on ICQ, we present ISYV (I Seek You in Videos), a systematic solution comprising three components: (1) ISYV-Bench, a challenging evaluation benchmark with 1,377 real-world complex videos and 1,377 question-answer pairs, organized into six difficulty levels spanning capabilities from identity recognition to causal reasoning; (2) ISYV-75K, a large-scale training set of 75K high-quality samples constructed via automated annotation, multi-stage verification, and manual review; and (3) ISYV-Framework, containing an ICQ-oriented model and training strategy for learning to exploit informative video shots without additional shot-level annotations. Extensive experiments show that both mainstream closed-source and open-source MLLMs struggle on ISYV-Bench, especially in cross-domain identity matching and long-horizon tracking. ISYV-Model outperforms strong baselines and in some aspects approaches closed-source performance. Overall, ISYV provides a unified task definition, scalable datasets/benchmarks, and modeling insights for person-centric video reasoning.

---


### 145. [ResidencyRL: Reinforcement Learning in Simulated Clinical Environments](https://arxiv.org/abs/2608.07418)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Valentin Liévin, Samuel Schmidgall, Tim Strother 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In medical education, physicians convert academic knowledge into clinical expertise through residency: years of training across thousands of encounters, with diverse sources of feedback and progressively greater autonomy. Much of clinical reasoning relies on the patient encounter, a dialogue in which a clinician elicits history, refines diagnostic hypotheses, and decides management under uncertainty. While large language models (LLMs) excel on static medical benchmarks, methods to optimize the full sequence of clinical decisions remain underdeveloped. We present ResidencyRL, a reinforcement learning (RL) method for training clinical artificial intelligence (AI) agents through simulated multi-turn clinical encounters (up to 60 dialogue turns and 8 tool calls per trajectory). ResidencyRL pairs the policy agent with LLM simulators capable of complex, adversarial behaviors, training against a structured reward aligned to diagnostic accuracy, management quality, communication, documentation, and safety. On held-out evaluations, the ResidencyRL agent improves diagnostic accuracy by 7.0% under adversarial conditions (88.0% vs. 81.0%) and reduces missed red flag rates by 31%, demonstrating rigorous mitigation of premature closure. Blinded expert clinicians validated these gains, preferring the trained agent in 87.6% of side-by-side comparisons. The procedural competencies transfer to unseen benchmarks: the agent outperforms the base model across all six clinical axes of the AMIE multi-visit benchmark, and shows consistent directional improvements on AgentClinic and CRAFT-MD. Our findings demonstrate that sequential clinical decision-making can be effectively learned through multi-turn RL in simulation, yielding robust, generalizable capabilities, paving the way towards clinical mastery. Prospective validation with real-world workflows remains necessary to establish clinical utility.

---


### 146. [Conformal Coverage Guarantees for Any Video Temporal Grounder](https://arxiv.org/abs/2608.07434)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aseel Mohamed, Rasul Khanbayov, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event boundaries in continuous video are ambiguous: re-annotate the same query-video pair and independent annotators mark moments that overlap by less than half on a large fraction of samples. The ground truth for video temporal grounding is therefore a distribution over intervals, yet every grounder returns a single interval with no statement of reliability, so at deployment a wrong interval is indistinguishable from a right one. COVER changes the output object: a post-hoc, model-agnostic wrapper that turns any grounder, a trained localizer or a black-box video--language model, into one that emits a temporal region containing the true moment with probability at least $1-\alpha$, by calibrating the quantile of a temporal nonconformity score on held-out labels and widening the base prediction by that amount. The guarantee is finite-sample and distribution-free under exchangeability, and requires neither retraining nor white-box access. We give two score families, a two-sided boundary-widening score for grounders that emit an interval and a super-level-set score for grounders that emit a relevance signal, and develop theory specific to grounding that bounds how large the certified region becomes, when coverage survives conditioning on event length, and how it degrades when moments from one video break exchangeability. Across three benchmarks and five grounders, realized coverage tracks the target, and calibration exposes what point metrics hide.

---


### 147. [SABRE: Scalable and Automated Benchmarking of VLMs under Stress](https://arxiv.org/abs/2608.07435)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zixuan Lan, Luzhe Sun, Matthew R. Walter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are improving rapidly, but benchmark development lags behind, making weaknesses hard to identify. Building stress tests is costly: samples must satisfy controlled conditions, remain answerable, and challenge current models. We present SABRE, a scalable, automated pipeline that converts a Test Primer (a Markdown Task Design with Data Schema) into structured specifications, generated or edited images, and question-answer pairs. Automated filtering removes candidates solved by a Filtering VLM, while human review verifies candidate validity and supports annotation correction and localized image repair. We instantiate SABRE-Prior to test whether VLMs follow visual evidence instead of relying on world priors -- learned expectations about familiar objects and scenes. Its 600 images and 1,000 questions span Context (unexpected entities in familiar scenes), Texture (counterfactual materials), Attribute (noncanonical component counts), and Language Elicitation (answers suggested by language but unsupported by the image). Across six VLMs, macro-average accuracy ranges from 17.8% to 31.3% (22.6% mean). A real-image Attribute control is comparably difficult for the Filtering VLM. SABRE-Counting and SABRE-Spatial pilots show that the workflow supports other stress-test settings. These results establish SABRE as a reusable framework for constructing and refreshing VLM stress tests rather than a single fixed benchmark.

---


### 148. [Blast Radius](https://arxiv.org/abs/2608.07440)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** MY Pitsane, Hope Mogale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic coding faces growing problems of affordability and wasted tokens. We introduce Blast Radius, a predictive memory management layer that estimates an incoming prompt's reach through coupled context and code channels. NECROPHORESIS enables reversible eviction by archiving dead context verbatim, while Recurring Dead Matter (RDM) identifies and buries repeatedly occurring transcripts. We formulate reversible context eviction over a Polish context space, providing a measurable foundation for retention, recurrence, and eviction while connecting context entropy to resurrection probability. Across seven OpenAI models, Blast Radius reduced token consumption by 17-26%, achieved the lowest overflow rate among tested policies, and remained byte exact reversible. Of 450 buried bodies, 378 were recurring dead matter and zero were recalled. Blast Radius operates beneath HCRC, determining which records to bury and how far an incoming prompt may reach into the codebase. This work contributes to the broader goal of Algosophy: making large language models and agentic coding more reusable and sustainable.

---


### 149. [SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent](https://arxiv.org/abs/2608.07449)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingxuan Zheng, Yujin Zhou, Chuxue Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly adapt to recurring tasks by accumulating procedural knowledge in skills. These skills are lightweight, reusable textual artifacts that are loaded into the agent's context without weight updates. Recent methods refine skills through iterative task execution, failure diagnosis, and trajectory-guided text-space updates. However, existing frameworks lack explicit diagnosis--outcome feedback and treat deletion as a generic edit operation rather than a dedicated mechanism for consolidating accumulated knowledge. We introduce SkillProx, a proximal-gradient-inspired forward--backward framework that couples closed-loop diagnostic evolution with utility-aware proximal refinement. Motivated by a composite objective balancing task loss and skill complexity, the forward stage re-executes diagnosis-driven edits on the same task batch, rolls back regressions, and feeds measured outcomes into subsequent diagnoses. The backward stage decomposes the resulting skill into auditable knowledge units, estimates their contributions using a frozen leave-one-out utility audit, and applies validation-gated consolidation, demotion, or removal. Experiments on in-distribution and out-of-distribution benchmarks across multiple backbone LLMs show that SkillProx improves average accuracy by 3.0 percentage points over the strongest gradient-based baseline. Component ablations demonstrate the complementary effects of closed-loop diagnosis and proximal refinement.

---


### 150. [Strategy-first synthesis planning for complex natural products](https://arxiv.org/abs/2608.07454)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Daniel Armstrong, Xuan-Vu Nguyen, Octavian Susanu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The total synthesis of a complex molecule is among the most demanding intellectual and experimental feats in chemistry: a chemist must plan many steps ahead for how to assemble simple building blocks into an intricate target, devise backup strategies, and anticipate procedural challenges. It is also a profoundly creative activity. For half a century, efforts to automate the retrosynthetic design of natural products and other complex molecules have drawn on catalogued reactions, and the resulting tools now report near-complete success on benchmarks built from that same source. But these tools were shaped to fit benchmarked chemistry, and they falter on many natural products, the frontier of the field, whose densely functionalized, polycyclic architectures demand precisely the inventive chemistry the record contains least. Whether a machine could reasonably design such syntheses like an expert chemist does has remained unclear. Here, we show that SynthEx, an agentic framework built on large language models, plans routes to complex natural products that lie beyond the reach of conventional design algorithms. SynthEx proposes competing strategies, assembles a sequence of routine and key steps into a cohesive route, and critiques and improves its own design; the chemistry it favours is more convergent than existing tools produce, and spans a region of reaction space that catalogue-based tools cannot match. Most notably, in blinded assessments, expert chemists judged its key steps comparable to those of published human syntheses and engaged with them as genuine synthesis plans, a response algorithmic route prediction has not previously accomplished. We release routes to more than a thousand natural products as SynthAtlas, an open, interactive database, and anticipate it will become a shared resource for a collection of complex target molecules that lack existing literature routes.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-152](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
