# 🧠 大模型相关研究 | 2026年11月09日

> 本类共 **183** 篇论文：已确认 **172** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-183](./part-04.md)

---

### 101. [Responsible GenAI Use During Active Armed Conflict: Evidence from Sudan's Emergency Response Rooms](https://arxiv.org/abs/2611.07874)

**<font color=#1a73e8>作者：</font>** Dalia Ali, Yearin Lee, Cheng Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Armed conflict can increase the value of Generative AI (GenAI) while undermining the conditions required for its responsible use. Yet the perspectives of community-based humanitarian responders working under these conditions remain underrepresented in responsible AI research. We examine GenAI use in Sudan's Emergency Response Rooms (ERRs), a community-led humanitarian network, through an exploratory survey of 89 respondents and 15 semi-structured interviews with GenAI users and non-users. War reconfigures GenAI's role, making it most useful where its outputs are hardest to verify. ERR responders turned to GenAI when conflict made human expertise difficult or dangerous to reach. However, participants cautioned that GenAI could not independently establish rapidly changing local conditions, and that relying on its outputs could lead to harmful decisions when human verification was difficult. Risks arose before GenAI was used. For some volunteers, carrying a phone or accessing the internet could expose them to danger. Others were concerned that sharing sensitive beneficiary or operational information with GenAI could put people at risk. Participants feared that AI-assisted reports could undermine their credibility with donors, whose funding sustains the food and medical aid ERRs provide. Access to GenAI was uneven, and volunteers using it sometimes relied on colleagues with relevant expertise or local knowledge to verify its results. Our findings show that responsible use of GenAI during conflict depends not only on model performance or individual adoption, but also on whether responders can safely access these tools, verify their outputs against local conditions, and recognize when limiting or avoiding GenAI is the more responsible choice.

---


### 102. [When, Where, How: Active In-Context Learning for Tabular Foundation Models](https://arxiv.org/abs/2611.07886)

**<font color=#1a73e8>作者：</font>** Christian M. M. Frey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular Foundation Models (TFMs) adapt to a new task only through the labeled rows in their context. However, labels are expensive to acquire in real-world scenarios due to the need for highly specific domain knowledge to ensure high-quality data. Active in-context learning transfers classical acquisition rules to this setting, in which the model that guides acquisition changes with every label added. We ask how the value of diversity, predictive uncertainty and target-aware information gain changes as a frozen TFM acquires more context. For that, we study Target-Aware Nearest Neighbor (TANN) acquisition and the Expected Predictive Information Gain in Context (EPIC) and evaluate them against classical rules. Our study across twenty benchmarks with two well-established TFMs and classical GBDTs highlights three findings: (i) When: diversity-based acquisition is best during the first acquisition iterations; (ii) Where: labeling pool rows that serve the target inputs via a simple target-aware nearest-neighbor rule matters substantially; (iii) How: EPIC yields the best models at the label budget, retains on average 80--87% of the chance-corrected full-data performance with only 5-10% of the pool labeled on the eight benchmarks with the largest pools, and selects labels that also improve the predictive performance of gradient-boosted decision trees.

---


### 103. [When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale](https://arxiv.org/abs/2611.07891)

**<font color=#1a73e8>作者：</font>** Gautam Gupta, Dikshant Kukreja, Unique Kumar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantization and pruning reduce the cost of deploying language models, but their effects are usually reported as benchmark scores. Such scores record only the loss that remains at the output. Inside the model, compression damages some components more than others, and the rest of the network can partly compensate. The observed loss therefore reflects both the damage and this compensation, which benchmark scores cannot separate. How the two combine, and whether their balance changes with model size, remains unclear. We study this compensation for in-context retrieval, a capability carried by a small, identifiable set of attention heads. To separate the two, the expected loss from ablating these heads is decomposed exactly into the part restored by the rest of the network, attributed to the components responsible, and the part that reaches the output. This decomposition is then compared across model sizes. For damage of comparable size, smaller models restore most of the loss, whereas larger models retain most of it, because the compensating responses offset less of it as models grow. Compressing the heads produces the same pattern. Compression that is nearly harmless in small models can therefore be costly in large ones.

---


### 104. [Same Answer, Different Future: Matched Predictions Do Not Imply Matched Belief Updating in Language Models](https://arxiv.org/abs/2611.07913)

**<font color=#1a73e8>作者：</font>** Weihan Li, Junhao Wu, Xinlei Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models can produce similar probabilistic predictions after observing outcomes, reading summaries, receiving instructions, or undergoing activation interventions. Whether these routes induce equivalent belief states remains unclear: agreement in current predictions does not establish how a model will respond to subsequent evidence. We investigate this distinction in a Bernoulli inference task with an analytic Bayesian reference. Across three open-weight language models, we prepare states through four textual routes and two activation-level interventions, measure both next-outcome continuations and explicit probabilistic estimates, and append identical new evidence from each prepared state. We quantify the persistence of the initial belief through its effective evidence weight, the number of new observations it is worth. We find that the format of evidence decides which readouts express its content: outcome sequences primarily affect continuations, whereas summaries and stated rates primarily affect explicit estimates. Moreover, effective weights differ substantially across routes, with summaries receiving weights that scale weakly with their stated observation counts and elicitation questions changing inferred weights by orders of magnitude. In a one-shot steering setting, an intervention that reproduces a natural record's immediate prediction loses most of its effect under subsequent evidence. These results show that agreement in current readouts is insufficient to establish equivalence in belief updating: how a belief is acquired and how it is read jointly determine its subsequent dynamics.

---


### 105. [Adaptive Semantic Branching: Disagreement-Localized Cross-Trajectory Regeneration for Reasoning Candidate Expansion](https://arxiv.org/abs/2611.07918)

**<font color=#1a73e8>作者：</font>** Jeong-Yoon Kim, Tae-Yoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning trajectories generated for the same problem often arrive at conflicting answers. These disagreements reveal alternative intermediate decisions that can be reused to explore new solutions. We introduce Adaptive Semantic Branching (ASB), a training-free inference procedure that turns cross-trajectory disagreement into targeted candidate generation. ASB first groups independently sampled trajectories by extracted final answer, selects a representative from each group, and aligns their reasoning steps with a monotonic dynamic program. A persistent-divergence objective identifies the point at which initially similar reasoning paths develop different continuations. For each selected directed pair, ASB retains the source trajectory's textual prefix, extracts a short reasoning window from a competing donor trajectory, and generates a fresh solution conditioned on both. A diversity-aware policy allocates up to three additional generations according to the answer-cluster structure. In a 500-problem MATH evaluation with Qwen2.5-7B-Instruct, ASB increases oracle candidate coverage from 445/500 (89.0%) with seven initial samples to 455/500 (91.0%), recovering correct candidates for 10 of the 55 initially uncovered problems. The method uses 576 additional generation calls across the evaluation set, averaging 8.152 calls per problem. We provide a precise specification of the branching operator, alignment objective, generation policy, and experimental configuration.

---


### 106. [AttnSR: Attention Step Reward for Long-Horizon Agentic RL](https://arxiv.org/abs/2611.07932)

**<font color=#1a73e8>作者：</font>** Mengsong Wu, Tianchen Zhou, Zhaochen Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents make multi-step decisions, yet outcome-reward-only reinforcement learning provides little direct supervision for individual steps. We introduce AttnSR, a step-level reward augmentation method that derives reward allocations from policy attention extracted during training replay, without a separately trained reward model or additional rollouts. AttnSR traces backward through the policy model attention graph to estimate the relevance of earlier steps to the final response. The terminal step, measured relative to a running baseline, determines whether these rewards reinforce or penalize the selected steps. In a controlled Qwen2.5-7B-Instruct study, AttnSR consistently outperforms the PPO baseline across all evaluated checkpoints on ALFWorld, raising final held-out success from 91.2% to 97.1%. The ablation experiment shows that the benefit depends on how intermediate rewards are assigned, rather than simple accumulation of step rewards over time. AttnSR also improves ScienceWorld at every checkpoint while cutting environment interactions by 29.9%. These results support policy attention as a practical prior for step-level reward allocation in long-horizon agentic RL. Code is available at this https URL .

---


### 107. [WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation](https://arxiv.org/abs/2611.07939)

**<font color=#1a73e8>作者：</font>** Jiahao Cui, Jiaye Li, Wenhao Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive driving world models systematically suffer from structural drift, identity drift, and quality decay over long rollout horizons due to transient conditioning signals that lack persistent state. We present WAM-Sim, a driving world model anchored by a persistent hierarchical memory and optimized via online flow-matching RL. WAM-Sim structures persistent context across three temporal and semantic scales: pose-aligned structural tokens encoding persistent road topology, read-only scene tokens supplying geolocated background appearance, and write-once instance tokens preserving individual traffic participant identities across occlusions and chunk boundaries. To restore visual sharpness and physical plausibility degraded by multi-scale conditioning, we introduce an online post-training framework that optimizes self-generated rollouts via flow-matching RL guided by hierarchy-aligned visual rewards and a vision-language model physical judge. The invariant memory empirically confines policy optimization within the anchored context, helping suppress semantic collapse and reward hacking, while online RL systematically enforces physical commonsense and fine-grained visual fidelity. On the nuScenes benchmark, WAM-Sim achieves a superior generation fidelity (FID=3.47, FVD=25.72) and strong downstream perception performance (24.16 mAP, 71.23 road mIoU). On minute-scale rollouts of self-collected data, WAM-Sim substantially mitigates structural and identity drift, preserving high scene similarity and subject identity coherence across extended horizons. Project page: this https URL.

---


### 108. [CardioLM: A multilingual suite of small language models for the cardiology domain](https://arxiv.org/abs/2611.07940)

**<font color=#1a73e8>作者：</font>** Manuela-Daniela Danu, Miguel Rodríguez-Ortega, Alberto Becerra-Tome 等 40 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Cardiovascular care generates large volumes of clinical free-text documentation in local languages. However, clinical natural language processing (NLP) resources remain concentrated in English, and no existing benchmark is cardiology-specific, multilingual, and broad in entity coverage.
Methods: We present two contributions. The first is CardioCCC, a corpus of 508 cardiology case reports originally published in Spanish and extended to Czech, Dutch, English, Italian, Romanian, and Swedish through machine translation, annotation projection, and clinician review, with annotations covering diseases, symptoms, procedures, and medications. The second is CardioLM, comprising CardioBERTa, a set of language-specific encoders obtained by continued pretraining on cardiology and biomedical corpora, and CardioNER, a set of named entity recognition (NER) models fine-tuned on CardioCCC.
Results: Cardiology-specific pretraining reduced pseudo-perplexity by up to a factor of eight, yet changed strict span-level F1 by at most 0.04, with benefits concentrated in languages whose backbones lacked biomedical coverage. The jointly trained multilingual XLM-RoBERTa-large models achieved the best strict F1 in nearly every language and entity type, exceeding the strongest monolingual system by up to 0.13 F1. A large share of residual errors concerned boundary detection: relaxed matching recovered 0.10-0.23 F1 for disease, procedure, and symptom, but only 0.01-0.07 for medication. Clinicians rated CardioNER well above a rule- and dictionary-based baseline, with the mean rating across entity types rising from 26% to 73%.
Conclusions: Specialty-specific pretraining is not the decisive factor for downstream entity recognition, whereas multilingual joint training yields the strongest results in nearly all settings and a simpler deployment path for multi-country clinical information extraction.

---


### 109. [ChemE-as-Code: An Open-Source Platform for Agentic AI in Chemical Engineering](https://arxiv.org/abs/2611.07947)

**<font color=#1a73e8>作者：</font>** Artur M. Schweidtmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ChemE-as-Code provides an open-source environment in which AI agents built on large language models (LLMs) can carry out chemical engineering work and engineers can check it. Its calculation tools range from catalysis through process simulation to plant layout, HAZOP and life cycle assessment, and skills tell a general-purpose agent how to use them. Engineering files are linked, machine-readable and versioned in Git; calculations run outside the LLM, each value records its origin, and automated checks report inconsistencies and out-of-date results by file and line. In an illustrative ammonia case, agents developed a written task into a preliminary basic-engineering package (simulation files, P&IDs, layout, HAZOP, datasheets, relief) for USD 224 of API cost in the design sessions. Planted faults and engineering changes show that the checks find what their rules cover and miss the rest, so they guide human review rather than replace it. No independent engineer has reviewed the design.

---


### 110. [Circe: Training-Free LLM Self-Evaluation via Component Interaction Consistency](https://arxiv.org/abs/2611.07948)

**<font color=#1a73e8>作者：</font>** Shuyi Miao, Zheng Li, Xu Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed in real-world applications, evaluating the correctness of their responses is crucial for reliable use. However, such evaluation is challenging because reference answers are rarely available in practice. Existing reference-free methods mainly rely on output signals, which may assign high scores to incorrect responses and thus do not necessarily reflect correctness. This motivates exploring the model's internal computation for complementary correctness signals. Recent studies exploit internal states, but they mainly analyze hidden-state trajectories across layers, which record only the combined updates of attention and feed-forward networks (FFNs) and overlook how these components interact. We therefore propose Circe, a training-free self-evaluation method that assesses a response using both internal and external signals, without reference answers or repeated sampling. For internal signals, we first introduce component interaction consistency (CIC), which measures the directional alignment between attention updates in earlier layers and attention-induced FFN output changes in later layers. We further incorporate representation geometry (RG) to characterize normalized displacement and angular changes along layerwise hidden-state trajectories. For the external signal, we convert the mean negative log-likelihood of generated tokens into a bounded likelihood confidence (LC) score. Finally, we fuse CIC, RG, and LC into a unified correctness score. Experiments on five LLMs and six benchmarks across four domains show that our method distinguishes correct from incorrect responses more effectively than existing baselines, and generalizes to multilingual, multimodal, and open-world settings.

---


### 111. [CoRD: Coupled Rollouts Fill the Blind Spot of On-Policy Distillation](https://arxiv.org/abs/2611.07959)

**<font color=#1a73e8>作者：</font>** Guhan Chen, Bohan Li, Jun Rao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation trains a student on its own rollouts, so states the teacher would reach but the student does not are seldom supervised. We introduce CoRD (coupled-rollout distillation), which keeps the on-policy loss and moves only the distribution of training states toward the teacher, drawing rollouts from a geometric interpolation of student and teacher through the maximal coupling of speculative decoding. The coupling keeps the student's token wherever the two distributions agree and otherwise substitutes a token from the part of the target the student underweights, so interventions are as rare as any exact sampler allows and recede as the student learns. Across six base students from two model families (Qwen3 and Qwen3.5, 0.6B to 4B), CoRD raises average pass@1 over on-policy distillation by 0.9 to 2.0 points and pass@8 by 1.2 to 3.4 points on five public math benchmarks at equal steps and data. On frozen teacher-reached states, a 4B student trained with CoRD reaches in 16 steps a gap closure that on-policy distillation does not reach in 80, and substitution rules intervening at least as often in other directions fall short of CoRD.

---


### 112. [TCSExam: Evaluating Frontier LLMs on the Full Range of TCS Research](https://arxiv.org/abs/2611.07962)

**<font color=#1a73e8>作者：</font>** Yifan Luo, Zhengying Liu, Yang Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can large language models (LLMs) advance theoretical computer science and resolve its long-standing open conjectures? To study progress toward this goal, we introduce TCSExam, a unified framework and benchmark covering the full range of TCS research. It evaluates theorem proving, solver engineering, and constructions alongside direct attempts to resolve open conjectures, capturing both concrete research accomplishments and progress toward long-standing research goals. TCSExam-Full contains 100 expert-reviewed tasks, with submissions checked by the Lean kernel or an executable task checker. TCSExam-Lite selects 20 tasks, five per track, reducing the number of task attempts by 80% at the same per-attempt budget. We evaluate eight agents on Full and nine on Lite. The TCSExam Index combines all four tracks: GPT-6 Astra leads Full (71.9), and Opus 5.5 leads Lite (72.3). Full and Lite rankings are strongly aligned across eight shared agents (Spearman's $\rho=0.93$), supporting Lite as a compact, discriminative benchmark. The evaluations yield improved solver outputs and mathematical constructions, together with independently verified special cases and bounds from open-conjecture attempts. TCSExam provides an extensible framework with task sources, Docker build recipes, and evaluation tools for reproducible use.

---


### 113. [QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents](https://arxiv.org/abs/2611.07976)

**<font color=#1a73e8>作者：</font>** Yingjie Tan, Haiquan Qiu, Quanming Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DeepSearch LLM agents repeatedly search and carry retrieved sources into subsequent reasoning steps. This expanding context increases token consumption and latency, although many results do not contribute to later reasoning. We propose Query-Relevant Attention Entropy (QRAE), an online context compression method that uses sparse evidence-assessment heads to decide which intact retrieved chunks should persist across reasoning steps. It scores bounded candidate batches through paired prefills: a query-free control suppresses shared attention responses, while normalized entropy measures the breadth of the positive response within each chunk. High-scoring chunks enter a persistent evidence whitelist and are included in the reasoning context. Uncertain chunks remain outside the reasoning context but are retained in a candidate cache, where they can be retrieved for later reevaluation. QRAE requires neither an additional generative compression pass nor modification of the attention operator. Across multiple DeepSearch benchmarks and reasoning models, QRAE improves task success by an average of 2.35 percentage points and reduces end-to-end latency and reported token usage by an average of 30% and 45%, respectively. These benefits generalize to a model with nearly 100B parameters.

---


### 114. [Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs](https://arxiv.org/abs/2611.07988)

**<font color=#1a73e8>作者：</font>** Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model compression can facilitate the deployment of large language models in resource-constrained legal settings, but its effects on domain-specific performance may depend on the evaluation protocol. We investigate this issue using ArabLegalEval, a Saudi Arabic legal benchmark, under both with-context and no-context evaluation. The former provides supporting legal passages, while the latter assesses performance without external context. Removing the context produces accuracy gaps of up to 27 percentage points for the base model. We examine three stages: domain adaptation, quantization, and knowledge distillation across FANAR-9B, JAIS-8B, and Qwen2.5-7B. Four-bit quantization reduces model memory by 64-71%, with changes in no-context MCQ accuracy ranging from -3.2 to +1.6 percentage points. Distillation produces more variable results, with accuracy generally declining as student size decreases. A Qwen2.5-7B student distilled from FANAR achieves 76.6% no-context accuracy, compared with 77.2% for its teacher. Our findings suggest that no-context evaluation provides a useful complement to context-supported testing when assessing the effects of adaptation and compression on Arabic legal language models.

---


### 115. [Deformable Contact-Aware 3D Object Placement](https://arxiv.org/abs/2611.08005)

**<font color=#1a73e8>作者：</font>** Songhe Wang, David Miller, Charles A. Kamhoua  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current language-guided 3D object placement typically predicts a rigid 6-DoF pose, ignoring the physical reality that indoor placements are dictated by contact. Consequently, predicted poses often float, interpenetrate supports, or fail to deform soft surfaces. We propose Deformable Contact-Aware Placement (DCAP), a framework that reframes placement as a drop-to-equilibrium process. Rather than predicting a static pose, DCAP constructs a semantic release state that specifies the drop location, object scale, and deformable components, allowing a coupled rigid-deformable simulator to settle the object under gravity and friction. This explicitly separates semantic intent from physical realization. Evaluated on a benchmark of 2,063 prompt-asset-scene cases, DCAP significantly outperforms static baselines. On standard placements, it improves VLM Physics & Naturalness by 21.2 points and human preference by 26.5 points over the strongest raw rigid baseline, while reducing mean penetration depth by 72.3%. Compared to simulated rollout baselines, DCAP reduces residual speed by 72.1%. Ultimately, our results prove that physically accurate 3D placement requires modeling semantic intent and physical realization as strictly separate processes.

---


### 116. [Automatic keyphrase extraction and annotation: modern theoretical approaches and practical solutions for text and speech](https://arxiv.org/abs/2611.08006)

**<font color=#1a73e8>作者：</font>** Daria Guseva, Olga Mitrofanova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The exponential growth of textual and audiovisual information has made the task of automatic keyphrase extraction (KE) increasingly significant. This article provides a comprehensive analysis of contemporary theoretical approaches and practical solutions for KE across both text and speech modalities. The primary contribution of this work is its systematic synthesis of these often-disparate research strands into a unified analytical framework, highlighting the evolution of the field from statistical methods towards large language models (LLMs) and end-to-end speech processing. We examine the stages of KE, the characteristics of keyphrases in written and spoken language, and terminological nuances. Various methods for automatic KE are discussed and analyzed in detail: statistical, hybrid, machine learning-based, and structural. The review dedicates substantial attention to emerging paradigms, including keyphrase generation using LLMs, and provides a detailed overview of methodologies and challenges in automatic corpus annotation. Furthermore, we specifically analyze current directions and inherent difficulties in KE for spoken language, comparing transcript based and end-to-end acoustic approaches. This synthesis leads us to conclude that the field is moving towards a more integrated, context-aware paradigm. Future progress will depend on addressing key challenges such as data scarcity for low-resource languages, effective multimodal fusion, and the nuanced evaluation of generative KE systems.

---


### 117. [Learning Dynamics of On-Policy Distillation](https://arxiv.org/abs/2611.08016)

**<font color=#1a73e8>作者：</font>** Guan Zhe Hong, Sumeet Ramesh Motwani, Liang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is emerging as an important paradigm for language-model post-training, combining dense teacher supervision with training on student-generated trajectories. This creates a feedback loop where each update changes the student and thereby the training distribution that generates subsequent updates. Yet, how this feedback shapes learning and generalization remains poorly understood. We conduct a mechanistic analysis of OPD's learning dynamics, distinguishing the two feedback loop stages: conversion of the distillation signal into parameter updates, and broadcast through which these updates change predictions across prefixes and reshape the rollout distribution. This framework helps us understand both limited student responsiveness despite substantial teacher-student disagreement, and degeneration when updates that improve local teacher agreement also increase the probability of unsuccessful continuations, exposing the student to unreliable supervision in subsequent rollouts. Finally, we show that offline distillation can prepare a student for OPD without significantly improving immediate held-out accuracy. While OPD alone may degrade generation, it can yield substantial accuracy gains after sufficient offline preparation. Together, our results connect teacher supervision, student geometry, and the evolving rollout distribution in determining the learning dynamics of OPD and its effects on downstream performance.

---


### 118. [Should We Pay This Much for Robustness? Efficient Proxy Certificates with Marginal Guarantees](https://arxiv.org/abs/2611.08035)

**<font color=#1a73e8>作者：</font>** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern classifiers remain sensitive to small input perturbations, while strong model-agnostic robustness certificates such as randomized smoothing are often too expensive for deployment, requiring an extensive number (e.g. 2000) of model forward passes per input. We propose a framework that delegates certification to a cheap proxy function while statistically controlling its deviation from the original sound certificate. Given an exchangeable unlabeled calibration set, we tune the proxy via robust conformal risk control to guarantee a bounded marginal (rather than pointwise) false-approval rate: the probability, over future inputs, that the proxy accepts an input whose prediction is flipped due to perturbation. The resulting proxy certificate can be used either as a standalone marginal certificate or as a fallback mechanism that invokes the expensive certificate only when the proxy rejects. We provide both single-sample and sample-heavy calibration recipes. Empirically, as a standalone certificate our method reduces the test-time certification cost to a single model forward while retaining much of the certified performance of randomized smoothing at small radii, and as a fallback it recovers the certified ratio of randomized smoothing at a more modest speedup. This enables cheap yet effective robustness guarantees for larger architectures such as vision transformers and language models.

---


### 119. [KeHoSu: Keyed Homoglyph Substitution for Authenticated Text Provenance over Copy-Paste Channels](https://arxiv.org/abs/2611.08046)

**<font color=#1a73e8>作者：</font>** Andrei Alexandru Drăghici, Sediola Ruko, Briland Hitaj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Nowadays, large language models produce text at scale, and much of it is redistributed across platforms. A moderator who finds a suspicious comment, post or article may want to know which platform generated it and for which account. In this paper we study attribution over the channel through which such text actually travels, copy-paste, which discards document metadata but keeps Unicode code points. We present KeHoSu, which turns the confusable characters of homoglyph attacks into a keyed attribution channel: the variant chosen for each carrier letter encodes one bit of an identifier made of a platform field, a user field and a truncated authentication tag. Moreover, given that reshared text is often quoted in fragments, and the placement therefore keeps no positional state, we show that KeHoSu is invariant to sentence reordering up to a constant boundary layer and depends on a partial quotation only through the retained length. We characterize the code-point channel by its capacity, removability and detectability, and provide an achievable region that relates the three. We evaluate KeHoSu over a wide range of use cases and show that the mark survived copy-paste across 18 common platforms, attributing the majority of all excerpts to the correct account at 178 letters (about two sentences) on LLM-generated stories and 167 letters (about one sentence) on standard English prose.

---


### 120. [NutriVisRAG: Multimodal Exemplar Grounding for Nutrient Estimation with Vision-Language Models](https://arxiv.org/abs/2611.08054)

**<font color=#1a73e8>作者：</font>** Lubnaa Abdur Rahman, Ioannis Papathanail, Maria Panagiotou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diet is a major determinant of health, yet accurate dietary assessment from free-living meal images remains challenging. Existing retrieval-based Vision-Language Model (VLM) approaches to nutrient estimation typically rely on textual food representations, while, to our knowledge, direct grounding on visually similar annotated meals has not been investigated. We present NutriVisRAG, a retrieval-augmented generation framework that uses a vision encoder to retrieve similar meals with known nutritional annotations and provide them as multimodal in-context exemplars for VLM nutrient estimation at inference time, without task-specific fine-tuning. We evaluate NutriVisRAG across four datasets, four VLMs, three retrieval encoders, and two prompting strategies, including free-living meals from adults with insulin-treated diabetes, where carbohydrate estimates are compared against two dietitians' annotations. Across all 96 configurations (4 datasets x 4 VLMs x 3 retrieval encoders x 2 prompting strategies), NutriVisRAG reduced the primary estimation error in 56, with improvements more frequent under whole-meal (35/48) than per-item prompting (21/48). Across the evaluated configurations, the lowest NutriVisRAG error was below the best Vanilla error in 13 of 16 VLM--dataset pairs. For GPT-5.4-mini, under whole-meal prompting, the best-performing retrieval encoder for each dataset reduced the primary error on all four datasets relative to Vanilla, with reductions of 1.7--35.7%. Overall, our results show that grounding in multimodal exemplars comprising images and respective annotations can improve nutrient estimation at inference time without task-specific fine-tuning, although the benefits remain configuration-dependent.

---


### 121. [Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"](https://arxiv.org/abs/2611.08070)

**<font color=#1a73e8>作者：</font>** Nazmus Sakib Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently been reported to read and write the raw weights of neural networks directly, a capability termed weight-space programming. We ask whether the reading side of this capability reflects reasoning about weight flows or a combination of local arithmetic at the network's edges and memorized priors over public datasets. We test Claude Opus 5.5 on small convolutional networks of about 125,000 parameters trained on five image datasets, providing every weight as plain text with no tools, no forward passes, and no dataset or class names. The model performs accurate local calculations: batch-normalization statistics lead it to infer about three optimizer steps on networks stopped after three updates, and output-layer sign patterns recover the vehicle/animal split of CIFAR-10. The sessions report reading the first and last layers closely and sampling the middle, and several claims built on partial tracing fail verification, although we did not run a direct forward-pass test. Semantic judgments lean on familiar datasets: the model names CIFAR-10 for CIFAR-10 networks but also for all three fast-food networks, relabels KMNIST as MNIST, reads a 99.57%-accurate SAT-6 network as CIFAR-10 animal photos, and calls "frog" the output favored by a feature that fires most on trees. Permuting CIFAR-10's labels preserves the output split at the new indices, but every class pair the model interprets is then wrong, indicating reliance on remembered label order. These are exploratory results from mostly single runs. We conclude that zero-shot weight reading by this model is better described as local arithmetic plus dataset priors than as weight-flow tracing, and we provide a protocol for auditing future weight-space claims.

---


### 122. [Spatiotemporal Dynamics-Aware Industrial Anomaly Detection and Reasoning](https://arxiv.org/abs/2611.08080)

**<font color=#1a73e8>作者：</font>** S-Wei Chen, Siangyu Yang, Yi-Chen Jan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial Anomaly Detection (IAD) is a long-established problem that aims to detect defects in industrial products during manufacturing for quality control. Most existing studies focus on static visual patterns as the basis for detection. However, in real manufacturing environments, many anomalies are dynamics-based, such as irregular movements that cannot be perceived from static cues alone. We observe that even recent Multimodal Large Language Model (MLLM)-based approaches fall short in identifying such dynamic anomalies due to limited temporal modeling capability. To address this, we introduce MUSTARD: MUltimodal SpatioTemporal Anomaly Reasoning and Detection, a framework that equips MLLMs with fine-grained spatiotemporal dynamics awareness for detecting and reasoning about dynamics-based defects. MUSTARD introduces optical-flow-guided keyframe selection and augmented modalities to capture critical motion irregularities through local motion patterns and global dynamic evolution. Its normal pattern-based reasoning pipeline requires only a few normal reference samples as the detection basis, avoiding any model updates. This enables efficient adaptation across various products and provides high decision interpretability. MUSTARD is the first MLLM-based framework for dynamics-based IAD. Experiments demonstrate its superior performance in detecting spatiotemporal anomalies and providing plausible explanations. The code will be made publicly available.

---


### 123. [DictLLM: Post-training Compression of Large Language Model with Dictionary Kernels](https://arxiv.org/abs/2611.08082)

**<font color=#1a73e8>作者：</font>** Jinho Park, Se Young Chun, Mingoo Seok  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient deployment of large language models (LLMs) on mobile devices requires balancing performance with compute and memory constraints. Post-training compression is an effective approach to managing this trade-off, while requiring much less computation than in-training counterparts. We propose DictLLM, a dictionary-based compression scheme in which weight matrices within grouped layers are decomposed into a shared dictionary and layer-specific sparse coefficients, directly obtained from a pre-trained model without further training. Specifically, we cast DictLLM as a four-step post-training optimization. First, we obtain shared dictionaries via singular value decomposition (SVD) of input-scaled weight matrices, amortizing rank across grouped layers; second, we sparsify the layer-specific coefficients to the target compression ratio using a dictionary-aware Hessian; and third, we refine the dictionaries given the resulting sparse coefficients. Finally, we aggressively quantize both components using factor-specific Hessian information: input covariance for the dictionaries and the dictionary-aware Hessian for the coefficients. The resulting representation reduces memory footprint by storing a single shared dictionary per layer group, along with sparse layer-specific coefficients. On language modeling and zero-shot reasoning benchmarks, DictLLM consistently outperforms existing post-training low-rank compression methods and pushes the Pareto frontier between model size and performance. DictLLM compresses the original LLaMA-7B model by 5.1x with only a 2.9-point increase in WikiText-2 perplexity, achieving a 3.6x higher compression ratio than the state-of-the-art low-rank method.

---


### 124. [Linguistic boundaries emerge from pressure-constrained processing dynamics](https://arxiv.org/abs/2611.08085)

**<font color=#1a73e8>作者：</font>** Rui He, Philipp Homan, Wolfram Hinzen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human cognition organizes continuous experience into bounded units while maintaining continuity across them. Linguistic elements are also organized into bounded structural units such as words and phrases, with sentence marking the final bound of a grammatical construction process. How do such boundaries emerge? We propose boundaries emerge from interacting demands to maintain unresolved dependencies, integrate completed relations, and update semantic context, with structural completion allowing but not determining closure. First, in a generative simulation without predefined boundary positions or constituent labels, these demands produced sentence-like segment-length distributions and distinct characteristic timescales, with structural completion allowing but not determining closure. Near boundaries, unresolved dependency load declined, integration cost peaked, and accumulated pressure reset. Then, we tested whether same demands predicted human listeners' boundary choices during comprehension. Listeners were more likely to mark boundaries with fewer unresolved dependencies, higher integration cost and semantic mismatch, and elevated preceding memory load, beyond syntactic and prosodic cues. Third, in naturalistic self-paced reading, sentence-final slowing coincided with declining memory load and increasing integration cost and semantic mismatch, broadly consistent with the simulation. Processing same narratives with a large language model revealed increased local intrinsic dimensionality and straighter hidden-state trajectories at sentence endings, followed by larger representational updates. Boundary explained additional variation in reading time and hidden-state geometry beyond processing demands, but considerably less in next-token surprisal. Together, these findings suggest linguistic boundaries emerge as discrete manifestations of transitions in continuous processing dynamics.

---


### 125. [MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation](https://arxiv.org/abs/2611.08086)

**<font color=#1a73e8>作者：</font>** Kangjie Zheng, Amirhossein Vahidi, Liying Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modeling gene regulation in single cells requires jointly representing DNA sequence, chromatin accessibility, and gene expression across regulatory scales. Sequence-based models capture DNA-level regulatory grammar but often lack cell-level resolution, whereas many single-cell omics models represent genes and peaks as fixed-vocabulary tokens without their underlying sequence. Here, we present MUSS, a sequence-based multi-scale model for single-cell gene regulation that preserves both DNA-level and cell-level resolution. MUSS derives peak- and gene-level representations from DNA using a frozen pre-trained sequence encoder and integrates them through peak-peak self-attention and distance-biased peak-gene interactions. Peak masked language modeling followed by training on paired scATAC-seq and scRNA-seq aligns these representations with cell-specific regulatory states. Across gene expression prediction, enhancer-gene linking, motif-guided regulatory prioritization, and zero-shot cell clustering, MUSS achieves strong performance against sequence-based and single-cell omics baselines. It further predicts expression for genes and peaks unseen during task training. These results support sequence-grounded, multi-scale representations for decoding cell-type-specific regulatory programs. Code, datasets, and model checkpoints are available at this https URL.

---


### 126. [SAE Interprets MoE: Sparse AutoEncoders Reveal That MoE Experts Exhibit Human-Interpretable Fine-Grained Specialization](https://arxiv.org/abs/2611.08089)

**<font color=#1a73e8>作者：</font>** Anyuan Zhuo, Shaohua Zhang, Yuan Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models route each token to a few of many experts, yet what an individual expert is responsible for remains unsettled. Existing analyses count how often an expert is selected on domain-labeled corpora, an instrument that fixes the taxonomy in advance, stays coarse, and records selection rather than contribution. We instead study specialization in feature space by training a sparse autoencoder (SAE) on the output of an MoE layer. Since this output is a router-weighted sum of expert outputs and the SAE encoder is affine, the pre-activation of every latent decomposes exactly over the experts. Aggregated over a corpus, this gives each expert a dominant set of latents whose activation it principally drives. On layers 4, 30 and 46 of Qwen3-30B-A3B, contribution is far more concentrated than gating, most latents have only one or two dominators, and the overlap between dominant sets concentrates on a few expert pairs. Auto-interpreting these sets reveals a division of labor below coarse domains, with distinct experts for Java and front-end web code, or for geometry and for arithmetic and polynomials, while the coarse domains themselves take very unequal numbers of experts. Our SAEs and code are available at this https URL.

---


### 127. [ATHAAR: A Medieval Scientific Arabic Manuscript Dataset for Handwritten Text Recognition](https://arxiv.org/abs/2611.08091)

**<font color=#1a73e8>作者：</font>** Ismail El Jamiy, Khadija Msalek, Guillaume Loizelet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in handwritten text recognition, medieval Arabic scientific manuscripts remain an open challenge for current vision-language models (VLMs) due to cursive ligatures, variable diacritization, and more importantly the lack of training data. This paper aims to address this gap, by proposing the first annotation guidelines dedicated to the transcription of scientific Arabic manuscripts inspired by textual criticism, a well-established approach to historical text editing. We then propose, ATHAAR, a new dataset manually annotated following this guideline. Unlike previous resources in the field, ATHAAR varies both witnesses of the same text, calligraphic styles, and content to deal with texts but also numerals. Relying on state-of-the-art VLMs, we finally design a set of experiments to study models transfer across scripts, chapters, and treatises. Our findings highlight the limitations of current systems when faced with the specificities of ancient scientific texts.

---


### 128. [Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary Convolutions and Delta-Rule Memory](https://arxiv.org/abs/2611.08092)

**<font color=#1a73e8>作者：</font>** Nir Krakowski, Tamir Cohen, Ohad Zohar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time voice agents need a speech recognizer that never waits for future audio and whose memory per call does not grow with the length of the call. We present E-Gaborformer, a strictly causal encoder that combines Gated DeltaNet-2 recurrent layers with sliding-window attention in a 3:1 ratio, and builds every temporal convolution from a fixed dictionary of causal Gabor atoms. Its streaming state is constant, about 19 MB per call at production scale including the prediction network, where a causal-attention encoder of the same size accumulates over 1 GB after ten minutes. In a controlled causal study on LibriSpeech, E-Gaborformer leaves the initial plateau earlier, reaches a given accuracy up to 18% sooner, and matches or beats an E-Branchformer trained with the identical front end and recipe. At production scale, a 0.6B-parameter Hebrew and English streaming transducer built on E-Gaborformer has 28 to 31% lower word error rate (WER) than NVIDIA's Nemotron 3.5 ASR Streaming, a model of the same size, on English voice-agent traffic, and up to 20% lower Hebrew WER than our previous production system. The same weights serve strictly causal and 480 ms-lookahead decoding with no loss in accuracy, and a two-class formulation of the RNN-T lattice trains the transducer 2.6x faster with exact loss and gradients.

---


### 129. [Create Your Own Work Stack: Deploying Self-hosted AI and Tooling in a Tech Startup](https://arxiv.org/abs/2611.08116)

**<font color=#1a73e8>作者：</font>** Saad Ahmed Bazaz, Talha Amjad, Abdurrehman Subhani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-hosting AI is often presented as a way to reduce inference costs and increase control, but deployment introduces its own costs. We report our experience deploying a hybrid AI stack at Grayhat Developers, a small software company with an AI-intensive development workflow. Our initial motivation was to counter the growing cost of commercial AI usage: Claude/Codex incurred approximately \$325 per month, with more than 25.93 billion recorded tokens. We experimented with local open-source models as replacements for commercial coding agents, but after learning that their performance and inference speed were insufficient, we adopted a hybrid approach in which commercial agents remained responsible for complex tasks while local models handled lower-complexity tasks, organizational information retrieval, and synchronization with self-hosted tools including Outline, Plane, and ERPNext.
We estimated that approximately 30--40\% of our commercial AI workload was associated with context transfer, documentation synchronization, task management, and related operational coordination. By moving this work to local models, we estimate that approximately 90\% of this coordination workload could be handled without commercial inference, corresponding to an estimated 27--36\% reduction in overall commercial-AI workload or cost-equivalent usage. Our first internal deployment nevertheless failed to achieve adoption because it introduced UX friction. Replacing it with a centrally configured deployment substantially improved feedback and adoption. We conclude that local inference is most useful not as a wholesale replacement for commercial AI, but as part of a hybrid architecture that assigns tasks according to their capability requirements, cost, context demands, and operational sensitivity.

---


### 130. [Beyond K/V Caches: Cross-Model State Handoff in Hybrid Linear-Attention LLMs](https://arxiv.org/abs/2611.08133)

**<font color=#1a73e8>作者：</font>** Jiacheng Cai, Tao Zhang, Siqi Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production deployments often use different models to balance cost and quality through cascading, routing, and switching models during long conversations. Context accumulates across turns. Each switch requires the target to repeat prefill over this context. Existing methods transfer full-attention (FA) K/V caches across models. Hybrid linear-attention models also retain recurrent states (REC) and convolution histories (Conv). The interaction between Conv and REC complicates cross-model state transfer. Conv perturbations can change keys and values in recurrent layers and alter REC updates. Conv histories are overwritten, but changes in REC can still affect later outputs. More accurate REC reconstruction need not improve continuation. Building on this, we propose Hybrid State Transfer (HST) for all three state types. It uses structured REC maps and preserves history order during Conv alignment. We calibrate the adapters using the frozen target's outputs during continuation. FA cache map updates are merged offline. Across five benchmarks, Qwen3.5 4B$\rightarrow$27B and 9B$\rightarrow$27B achieve mean task retentions of 89.88% and 94.11%, respectively. With source caches already available, separate timing on synthetic 16K inputs yields handoff body speedups of $21.66\times$ and $21.91\times$.

---


### 131. [Describe Your Facial Expressions by Linking Image Encoders and Large Language Models](https://arxiv.org/abs/2611.08138)

**<font color=#1a73e8>作者：</font>** Yujian Yuan, Jiabei Zeng, Shiguang Shan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel task of describing human facial expressions of a facial image in natural language, which captures the nuances of facial actions and emotional states beyond traditional emotion categories or facial action units (AUs). To achieve the facial expression captioning model, we propose a three-stage training framework that trains a vision-to-language model using synthesized image-text pairs and the BLIP-2 pre-training techniques. To overcome the challenge of missing training image-text pairs for facial expression captioning, we propose a strategy that involves synthesizing and combining captions using GPT-3.5 and existing annotations on either emotion categories or AUs. Experiments demonstrate the effectiveness of our method in generating captions that describe details of facial actions and emotions, as well as the inferential relationship between them, even when those emotions are not present in the training data. It is also demonstrated that the vision-to-language task enhances the performance of the intermediate visual features on both AU detection and emotion classification tasks.

---


### 132. [PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?](https://arxiv.org/abs/2611.08175)

**<font color=#1a73e8>作者：</font>** Yue Zhang, Jilei Sun, Liqiang Jing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating printed circuit board (PCB) routing requires coordinating board-level connectivity decisions with geometric execution under strict design rules. Although recent agents can interact with native routing tools, reliable routing on complex boards remains challenging. We present PCBRouteAgent, a multimodal PCB routing agent inspired by how human engineers coordinate global strategy with local execution. A Global Routing Planner combines board images and structured electrical and geometric information to specify connection topology, routing order, corridors, and layer transitions. A Detailed Routing Executor realizes these guides through KiCad's native routing engine and performs bounded local recovery. Unresolved failures are returned as structured feedback, enabling targeted guide revisions while preserving accepted routes. We evaluate PCBRouteAgent on 247 synthetic and real-world boards from four PCBWorld-Bench test splits. It achieves clean-pass rates of 100%, 94.9%, 100%, and 40% on D2, D3-A, D3-B, and D3-C, respectively. On the three real-world subsets, PCBRouteAgent outperforms the best evaluated baseline in clean-pass rate by 13.9, 36, and 10 percentage points, respectively.

---


### 133. [Multimodal Hierarchical Mixture-of-Experts for 3D Medical Vision-Language Modeling](https://arxiv.org/abs/2611.08185)

**<font color=#1a73e8>作者：</font>** Gizem Mert, Szymon Płotka, Pedro R. A. S. Bassi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical 3D scans and reports are inherently hierarchical, with diagnostic cues concentrated in specific anatomical regions across multiple levels of organization. Yet, most medical vision-language models ignore this structure and fail to focus on clinically relevant anatomy. We introduce MedHiVE, which combines hierarchical vision-language Soft Mixture-of-Experts (SMoE) with contrastive learning to jointly model fine-grained anatomy and global scan context. To our knowledge, MedHiVE is the first framework to route both vision and text tokens through a two-level SMoE hierarchy organized by anatomical scale, coupling this with report-derived anatomy-level contrastive alignment for 3D medical imaging. This replaces the direct region-text alignment of statically pooled features and vision-only hierarchical routing of prior work with dynamic, slot-based cross-modal information flow across anatomical scales. MedHiVE operates via a two-level, learnable token-routing mechanism, where local image and text features are first routed through a local SMoE and then fused by a global SMoE into unified multimodal representations. Contrastive learning aligns both anatomy-level and global vision-language representations in a unified space. Pre-trained on 25,000+ CT scans with anatomical supervision, MedHiVE consistently surpasses 11 state-of-the-art methods across 6 datasets on 3 tasks: segmentation, classification, and detection, demonstrating the importance of hierarchical modeling. The code for MedHiVE is at this http URL.

---


### 134. [SMART: State-based Multi Agent Reasoning Traces for Verification-oriented Problem-Solving](https://arxiv.org/abs/2611.08196)

**<font color=#1a73e8>作者：</font>** Sai Vallurupalli, Francis Ferraro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex problems with limited context, such as claims, require a means to obtain additional knowledge necessary for solution reasoning. We propose a multi-agent framework, SMART, to obtain knowledge through capturing the implicit state of participating entities in a problem context. SMART curates the state knowledge as diverse, complementary and solution-salient premises using a variety of LLMs and a structured role-based prompt strategy. Using knowledge from these real-world verified curated premises, SMART's knowledge guided solution reasoning improves validation performance up to 20% on complex scientific claims spanning 3 datasets. We show that grounding premises in real-world knowledge is necessary and improves performance up to 5%.

---


### 135. [IntentWeaver: Sustaining Coherence across Evolving Intents in Human-AI Co-Writing](https://arxiv.org/abs/2611.08214)

**<font color=#1a73e8>作者：</font>** Yuanhao Zhang, Xinru Cheng, Baiqiao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Writers hold intents at many levels, from overarching goals to concrete wording, and evolve them by periodically popping back up from the text to higher-level intents. Generative AI co-writing disrupts this practice. Dense drafts capture attention and trap writers in local editing; higher-level intents stall while lower-level ones drift from them unnoticed, a breakdown we term intent incoherence. Our formative study traced this breakdown from attention capture through silent drift to failed reconciliation. We present IntentWeaver, which supports intent evolution while sustaining coherence in human-AI co-writing. It derives an intent hierarchy from the draft and writer interactions, evaluates each intent's fulfillment and cross-level coherence at every change, and propagates consequences across intent levels. In a within-subjects study (N=24) against a baseline, participants using IntentWeaver revisited and evolved higher-level intents more often, with fewer unnoticed deviations, and produced texts better realizing them. We further discuss design implications for emergent intents.

---


### 136. [ProQuant: Progressive Quantization-aware Training for Edge MLLMs](https://arxiv.org/abs/2611.08216)

**<font color=#1a73e8>作者：</font>** Yufei Xue, Yushi Huang, Jiawei Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal large language models (MLLMs) with impressive perception and understanding capabilities will enable a range of downstream applications. However, their substantial computational and memory requirements hinder the real-world implementation, particularly for resource-constrained edge devices. Quantization has emerged as an effective solution for deploying large models. While post-training quantization (PTQ) successfully retains the performance at moderate bit-width (e.g., W8A8), it suffers from severe performance degradation under low-bit quantization (e.g., W4A8), especially for small-scale models that are more suitable for edge deployment. In this paper, we propose ProQuant, a novel weight-activation quantization-aware training (QAT) framework tailored for low-bit MLLMs. First, to align the limited finetuning dataset distribution with the pretrained dataset distribution, we propose a self-relabeling (SRL) scheme to resample the responses of the open-source multimodal dataset. Second, we are the first to take a decoupled view of multi-modal (MM) understanding and language modeling abilities. We propose a progressive block activation (PBA) mechanism to prioritize the MM understanding recovery. We also introduce a vision-sensitive factor $\vec{\tau}$ that effectively identifies the MM-critical layers. Extensive experiments across various benchmarks, covering models with 2B-8B parameters, show that ProQuant significantly outperforms existing methods. For example, our W4A8 Qwen3-VL-2B-Instruct improves average accuracy by impressively 6.6% and achieves performance comparable to full precision counterparts with only approximately 1% performance drop. Code is available at this https URL.

---


### 137. [Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis](https://arxiv.org/abs/2611.08219)

**<font color=#1a73e8>作者：</font>** Teng Pan, Zixuan Wang, Yuchen Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon professional workflows, understanding heterogeneous file contexts, and producing usable deliverables under fine-grained requirements. A key bottleneck is the lack of scalable post-training data that reflects real work intent, authentic file environments, and deliverable-level evaluation. To close this gap, we introduce Agent-R$^2$, a $\textbf{r}$eal-source data synthesis framework that scales training data for $\textbf{r}$ealistic productivity work. Instead of relying on manually specified workflows or LLM-generated files, Agent-R$^2$ grounds synthesis throughout the pipeline in real occupational seeds, corpus-derived workflow evidence, and authentic web-sourced files. From 10k web-corpus candidates, Agent-R$^2$ distills 4k task instances that pair real multi-format attachments with fine-grained, deliverable-level rubrics. On this data, we train Agent-R$^2$-4B via supervised fine-tuning and rubric-based reinforcement learning, improving both end-to-end productivity performance and file-grounded reasoning. Trained on only 4k instances, Agent-R$^2$-4B surpasses Qwen3-235B-A22B-Thinking-2507 on both GDPval (51.0$\%$ vs. 48.0$\%$) and OfficeQA (14.8$\%$ vs. 13.8$\%$). Further analysis shows that Agent-R$^2$ mitigates shortcut behavior, where agents produce superficially plausible deliverables before sufficiently grounding, constructing, or verifying them, while promoting sustained exploration.

---


### 138. [Escalate or Close: How Fast-Tier Models Handle Held-Out Web Attack Families in Two-Tier Triage](https://arxiv.org/abs/2611.08229)

**<font color=#1a73e8>作者：</font>** Maciej Kisielewicz, Michał Kędziora, Ngoc Thanh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In two-tier triage a fast model decides most web requests and escalates the rest to a slow tier, so an attack the fast tier closes is never examined. We hold each of seven attack families out of training, recalibration and thresholds, splice the payloads into parameters of real browsing traffic, and compare zero-shot decision models, which return a probability for a typed question, with supervised detectors, a local language model, the OWASP Core Rule Set and an anomaly baseline. Detectors trained on the known families can give much of a held-out family a confident benign verdict: over 10 training runs, ModernBERT gives 37% to 60% of held-out path traversal a probability below 0.05 and escalates only 50% to 81% of it within a 5% benign budget, against nearly all of the same requests when traversal is known. Jev and Clef, two hosted decision models whose budget decisions do not depend on the held-out family, escalate at least 97.6% of every family within the same budget, but their undisclosed training data may contain these public families. Tests on recent exploits need controls for request shape: Jev escalates 37% of benign twins (exploit requests with the attack replaced by legitimate values), and detectors trained on older exploits learn what scanner requests look like. A search guided by Jev's probability gets 43% of held-out attacks past Jev within 300 queries, but Jev's answers vary: asked again, it escalates those requests in 60% of its answers.

---


### 139. [From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations?](https://arxiv.org/abs/2611.08231)

**<font color=#1a73e8>作者：</font>** Hanyu Qiu, Ze Liu, Zhe Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used for information access, content production, and agent-based task execution, but their outputs remain vulnerable to subtle, high-risk hallucinations. To systematically evaluate and advance post-generation hallucination detection, we introduce HaluCheck, a large-scale, bilingual benchmark comprising over 42k instances spanning both factual hallucinations in text and faithfulness hallucinations in agent trajectories. HaluCheck features fine-grained, multi-level annotations for detection, localization, and correction, covering different tasks and perturbation degrees. Experiments on fourteen LLMs reveal that, while models show basic sample-level detection ability, they struggle with fine-grained localization, correction, and agent hallucination detection. Further analysis demonstrates that thinking, web search, and supervised fine-tuning each offer partial improvements, but none fully solve the problem. HaluCheck thus provides a solid basis for benchmarking and diagnosing LLM reliability across text and agent scenarios.

---


### 140. [Signals, Evidence, and Context: User Scrutiny in Real-World LLM Conversations](https://arxiv.org/abs/2611.08232)

**<font color=#1a73e8>作者：</font>** Ahana Biswas, Yu-Ru Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often present synthesized answers without making their supporting evidence easy to inspect. We study how features of these answers relate to users' subsequent accepting, checking, and challenging in 489,283 assistant-user response pairs from ShareChat and WildChat. Broad attribution language appears in 31.9% of qualifying responses, compared with explicit URLs in 1.33%, revealing a gap between claims of grounding and preserved inspectable support. Attribution, uncertainty, and other response cues generally accompany both checking and challenging; only uncertainty shows a small statistically distinguishable pooled association favoring checking. Within Technical Help, uncertainty favors checking relative to challenging; refusals and reasoning traces favor challenging in Seeking Information. Scrutiny is concentrated in some conversations, while its apparent turn-to-turn persistence becomes much smaller when conversation-level differences and response ordering are examined separately. These results suggest that supporting verification requires attention to what evidence can be inspected, which question a user is trying to resolve, and the history of the interaction.

---


### 141. [Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling](https://arxiv.org/abs/2611.08237)

**<font color=#1a73e8>作者：</font>** Xiaojun Wu, Cehao Yang, Xuhui Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical modeling turns an open-ended real-world problem into assumptions, a model, a solution, and a defended recommendation, and its answers matter only if they are both close to a credible reference and physically feasible; existing benchmarks either score solver fragments or grade reports with an LLM judge, leaving those numbers unchecked. We introduce TB-MathModel (the Terminal-style Mathematical Modeling Bench), the first benchmark to make complete contest-style modeling problems agentic, verifiable, and terminal at once, over 18 real CUMCM and MCM problems (2023--2025). Each task ships the verbatim statement, official attachments, and figures in a containerized terminal; the agent returns one JSON artifact, scored on the numeric core of the final question against a reproduction of the Outstanding-award paper. Two design choices distinguish it: direction-aware, one-sided scoring, which never penalises beating the anchor, and two-layer feasibility verification---a programmatic gate over six decidable invariant forms plus 624 Lean~4 obligations---with a hard gate that zeroes infeasible answers. Each task is scored against a panel of human outstanding papers rather than one, so a model must be close to many accepted answers; across seven multimodal entries (three seeds each) the strongest reach a multi-reference O-Eval of 64.58\%, while the \$2.54 open model holds 59.81\% at $1/100$ the cost. TB-MathModel turns the numeric core of modeling into a reproducible, machine-checkable signal for measuring long-horizon modeling competence and for collecting agent trajectories. The source code is available at this https URL.

---


### 142. [The Geometry of Simulated Perspectives: Dissociating Representation and Behaviour in a Multimodal Language Model](https://arxiv.org/abs/2611.08262)

**<font color=#1a73e8>作者：</font>** Mathis Immertreu, Fitim Abdullahu, Thomas Kinfe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal language models can simulate different observers, yet it remains unclear how assigned perspectives reshape their internal representations and whether these changes govern their judgements. Here, we investigate the representational geometry of persona-conditioned visual interestingness in Qwen3-VL-8B-Instruct. Across 100 images and 53 prompting conditions, we systematically vary persona content and the linguistic framing used to introduce it, while recording behavioural ratings and layer-wise hidden states. We observe a systematic reorganisation of representational geometry across processing depth: early layers primarily encode image identity, whereas persona-specific structures emerge in later layers. Strikingly, prompt framing reshapes internal representations more strongly than persona identity, whereas persona content has a greater impact on behavioural judgements. This dissociation is further illustrated by minimal identity statements that alter representations even without changing responses. These findings demonstrate that representational distance does not necessarily reflect behavioural relevance. More broadly, they reveal how simulated perspectives emerge as distinct structures within the representational space of artificial cognitive systems, highlighting a fundamental distinction between the geometry of internal representations and their functional consequences.

---


### 143. [LeanContext: Disentangling Mathematical Resources from Local Formal Context in Lean Whole-Proof Generation](https://arxiv.org/abs/2611.08277)

**<font color=#1a73e8>作者：</font>** Hang Zhang, Qihao Ye, Litong Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural theorem proving increasingly uses retrieved premises and project context to support proof generation. Evaluating these resources requires measuring the advantage of target-selected declarations over comparable alternatives and how this advantage depends on training. We introduce LeanContext, a benchmark of 129,826 Lean whole-proof generation problems, to investigate these questions. We group selected complete preceding mathematical declarations as Mathematical Context (MC) and the remaining selected local source commands as Environment Context (EC). Four aligned input views support crossed training and inference evaluations with shared targets and original Lean verification environments. For both diffusion- and autoregressive-based models, selected declarations outperform comparable alternatives by a larger margin when training includes MC. Final-input audits identify omitted declarations referenced by the target. Prioritizing these dependencies improves Pass@32 by 1.40% and 1.70% for LLaDA and Llama, respectively, on 2,000 targets. The selection experiment operates without access to target reference proofs and holds checkpoints, EC, and inference budgets constant. The code and dataset are available at this https URL.

---


### 144. [A Generative Model of Contextual Integrity: Appropriate vs. Inappropriate Information Sharing](https://arxiv.org/abs/2611.08284)

**<font color=#1a73e8>作者：</font>** Omer Ebead, Claude Formanek, Joel Z. Leibo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contextual integrity (CI) holds that appropriate information flow depends on context-specific norms. The same disclosure may be appropriate in one context and inappropriate in another. We build a generative model of contextual integrity to study information sharing through simulated conversations. Two actors played by large language models exchange messages, with one holding private information and the other seeking it. We examine how sharing and refusal vary with the situation, the holder's decision logic, disposition, and the underlying language model. Actors shared information with the rightful recipients when it was needed, but also disclosed it to people who were not entitled to receive it. The model provides a way to study how disclosure and refusal develop through conversation as the situations and the actors vary.

---


### 145. [Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated Users in Interactive Worlds](https://arxiv.org/abs/2611.08286)

**<font color=#1a73e8>作者：</font>** Chenhao Zheng, Zixian Ma, Kai Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual interaction models that support users during ongoing physical tasks require evaluation in closed loop, where assistant responses can change subsequent user behavior and task outcomes. Existing benchmarks largely rely on offline replay and therefore cannot capture these effects. We introduce Interactive Visual Gym, a framework for closed-loop evaluation and training of visual interaction models through joint simulation of executable task environments and human users. We contribute three simulators that recreate everyday tasks and human-aligned action spaces across cooking, household manipulation, and mobile-interface domains, together with a persona-conditioned user simulation harness that collaborates with the assistant while incorporating controlled execution errors and other out-of-plan behaviors. We instantiate the framework as IVG-Bench, a benchmark with 315 interaction scenarios. Evaluating state-of-the-art VLMs as visual interaction models reveals substantial limitations: the best-performing model, Gemini 4 Argon, completes only 53.4% of tasks within the time limit, exhibits significant weaknesses in factual grounding and actionable guidance, and is often too slow to prevent errors when response latency is considered. We verify our evaluation protocol with a human study which finds 78.5% agreement between our interaction-quality metric and participant preferences. We further show that the environments provide useful learning signals: in a proof-of-concept GRPO experiment, closed-loop training improves both task success and interaction quality for Qwen3.5-4B model in our cooking environment.

---


### 146. [AutoCompress: Automated Hardware-Guided Model Compression](https://arxiv.org/abs/2611.08290)

**<font color=#1a73e8>作者：</font>** Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM pruning must preserve quality while meeting hardware- and workload-specific constraints on latency, throughput, and memory. Existing pruning workflows often target parameter counts, requiring practitioners to manually select model sizes that meet latency, throughput, and GPU memory limits. However, parameter count alone does not predict these metrics, which depend on the model architecture, workload, hardware, and serving engine. We introduce AutoCompress, a hardware-guided compression framework that directly incorporates such constraints into differentiable architecture search. AutoCompress jointly optimizes global and per-layer structure to produce heterogeneous architectures, guided by serving-engine cost models validated against end-to-end latency, throughput, and memory measurements. We evaluate AutoCompress on long-context local coding, batched datacenter serving, and latency-sensitive in-game interaction. Compared to the state-of-the-art Minitron pruning framework, AutoCompress improves average accuracy across eight benchmarks by 6.57, 2.35, and 0.57 percentage points on RTX 5070, RTX 5080, and H100, respectively. AutoCompress also compresses Nemotron 3.5 Super from 120B to 74B parameters for single-B200 BF16 serving at 128K context, retaining 95% of its mean benchmark score.

---


### 147. [Measured Coupling for Parallel Decoding in Diffusion Language Models](https://arxiv.org/abs/2611.08307)

**<font color=#1a73e8>作者：</font>** Tal Oved, Lior Wolf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models can write many tokens per step, but must choose which tokens are safe to commit together. Mean-field decoding penalizes pairs of positions whose predictions look alike. We replace this proxy with the coupling itself: how much committing one token changes the model's confidence at another. Cheap probes inside the main forward pass measure it, with no training or extra model, and it plugs into the same mean-field rule. On three models and four benchmarks, our method needs far fewer steps than mean-field decoding and is faster in most settings, also with a key-value cache, at an average accuracy cost of 1.1 points. Shuffling the couplings or replacing them with a uniform bonus loses this gain.

---


### 148. [RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines](https://arxiv.org/abs/2611.08308)

**<font color=#1a73e8>作者：</font>** Roko Parac, Christos Ziakas, Leo Ardon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards to be handled within a Markovian framework. However, they assume a labelling function, a proposition-grounding oracle for observations, which must be manually engineered for each environment, limiting their wider applicability. In this work, we address this limitation by proposing RM-VLM, a novel approach in which a large language model (LLM) generates an RM from a natural-language task description, and a vision-language model (VLM) acts as the labelling function, grounding the RM's propositions over image-based observations during RM-guided policy learning. A VLM-based value function estimator is used to assess the agent's progress towards each RM transition and derive a dense reward signal. We evaluate RM-VLM on three domains covering non-Markovian grid-world navigation, robotic manipulation, and 3D object collection. Our experimental results show that RM-VLM consistently achieves higher task success rates than existing VLM-based reward methods across all tested domains.

---


### 149. [LLM-Assisted Label Noise Correction for EEG-Based Sleep Stage Classification](https://arxiv.org/abs/2611.08311)

**<font color=#1a73e8>作者：</font>** Elmira Salari, Shruti Kshirsagar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic sleep stage classification from electroencephalography (EEG) signals is a critical task in clinical sleep medicine. While deep learning models have shown promising results in this domain, their performance is fundamentally constrained by the quality of training labels, which human experts manually annotate and that are subject to inter-rater disagreement and systematic labeling errors. In this paper, we propose a novel LLM-assisted label-noise filtering pipeline that operates exclusively during training to identify and remove unreliable sleep-stage annotations before retraining the classifier. Specifically, TinySleepNet is first trained on the original dataset to extract per-epoch SoftMax confidence scores, then low-confidence epochs are submitted to LLaMA 3.1 along with their EEG spectral features and surrounding sequence context. The LLM evaluates each epoch against AASM sleep-scoring guidelines and assigns a verdict of RELIABLE or SUSPICIOUS. Suspicious epochs are removed from the training set, and TinySleepNet is retrained on the cleaned data. Evaluated on the Sleep-EDF Expanded dataset using 20-fold cross-validation, our method improves overall accuracy from 81.8% to 84.6% and Macro F1-score from 75.6% to 77.4%, with particularly notable gains in REM detection. Crucially, because the LLM operates only during training, the lightweight TinySleepNet architecture (1.3M parameters) is preserved at inference, making the proposed pipeline suitable for real-time, wearable sleep monitoring applications.

---


### 150. [Trilemma: How Agents choose between Honesty, Confidentiality, and Task Completion](https://arxiv.org/abs/2611.08312)

**<font color=#1a73e8>作者：</font>** Johannes Taraz, Abhinav Kumar, Sahar Abdelnabi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Personal AI agents often act on underspecified instructions and draw on context such as their user's messages and calendar to decide how to proceed. This context can contain private preferences that interfere with the task, with other people's interests, or with confidentiality norms. Prior work has studied deception under goal conflicts and the leakage of private information, but largely as separate problems. We study both problems together in a simulated company Slack workspace in which four employees delegate sprint staffing to personal agents. Two agents learn from private messages that their employee avoids working with a particular colleague. Because the other agents request justifications for task preferences and the only true justification is confidential, the agents cannot simultaneously remain honest, preserve confidentiality, and complete the staffing. We evaluate seven open-weight models and Claude and GPT models. Of the 135/140 open-weight agents that pursue the avoidance preference, 107 either make false claims about task fit or logistics or cite a true consideration as if it were their actual reason. In a three-model comparison, confidentiality instructions reduce disclosure of the preference from 83% (none) to 31% (medium) to 2% (strong). However, the task is often not completed anyway; in the main experiment (medium confidentiality instructions), only 16 of 70 runs end with a valid staffing. In their reasoning traces, agents frequently acknowledge evidence against their claims and still conclude that the claims are not false; they engage in motivated reasoning. Our results indicate that agents can strategically make false or misleading claims in a day-to-day task without being instructed to; the environment provides a controlled testbed for studying how agents resolve such conflicts and for developing deception monitors.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-183](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
