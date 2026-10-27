# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

---

### 101. [Words Are the Voice of the Mind: Depression Severity Estimation from Social Traces via Mental-Guided Evidence Reasoning](https://arxiv.org/abs/2610.33586)

**<font color=#1a73e8>作者：</font>** Nada Xu, Xueqin Chen, Qiang Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression severity estimation is crucial for mental health assessment and intervention, yet traditional approaches depend on clinical interviews or self-report questionnaires that require users' active participation. With the widespread use of online social media, users leave rich social traces that may reflect their mental states, motivating the task of social media-based depression severity estimation. Existing efforts have progressed from textual-feature-based classification to LLM-based questionnaire completion over standardized scale items, yet they still fall short in user-specific mental priors modeling, diversified semantic retrieval, and fine-grained reasoning over mental evidence. To address these limitations, we propose UMer, a user-specific mental evidence reasoning framework for social traces-based depression severity estimation. UMer first distills a user-specific mental prior from historical social traces to capture the user's psychological tendencies, behavioral patterns, and self-expression style. It then performs scale-guided multi-query retrieval to construct evidence memories from item-relevant posts. Finally, it conducts coarse-to-fine evidence-aware reasoning to distinguish direct and indirect evidence and predict item-level scores with interpretable rationales. Extensive experiments on real-world benchmarks demonstrate that UMer not only achieves competitive performance over existing baselines, but also provides evidence-grounded interpretability and generalizes to other scale-based tasks.

---


### 102. [Who Verifies the Verifiers? Accountable Semantic Consensus for AI-Mediated Web Information Verification](https://arxiv.org/abs/2610.33587)

**<font color=#1a73e8>作者：</font>** Yanna Jiang, Mingyuan Li, Xu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly decide whether Web evidence supports online claims, often by voting over several assessors whose errors are presumed independent and benign. On the open Web, retrieved pages can steer the assessors that read them, and assessors from one model family fail together. We prove that even for independent assessors whose every output sequence is possible on both valid and invalid claims, any protocol that decides only from their outputs and always reaches an agreed verdict never rejects invalid claims or rejects valid ones with positive probability. We present Astral, which pins all assessors to one committed snapshot of the Web evidence. With up to f assessors faulty, Astral accepts a verdict only when 2f+1 assessors attest to it above a confidence threshold and no signed challenge stands. On five public benchmarks with two of seven assessors adversarial, Astral lowers pooled attack success to 21.5-53.1%, against 54.7-77.8% for majority voting. The cost is coverage, as without attack 16.0-61.7% of claims receive a binary verdict and the rest are disputed for audit. Our code runs at this https URL.

---


### 103. [Data Governance for Generative and Agentic AI : Technology, Law, Economics, and Security](https://arxiv.org/abs/2610.33605)

**<font color=#1a73e8>作者：</font>** Narayana Darapaneni, Padmaja K, Gnana Chaithra D  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This book develops a unified governance framework for systems that retrieve, generate, infer, remember and act on information from large language models and retrieval augmented pipelines to autonomous multi agent systems. Eleven chapters and eight appendices integrate three disciplinary lenses-technology, law and economics-across the full lifecycle: data quality, lineage and provenance; global data protection law and intellectual property; the economics of data governance; digital trust, cybersecurity and zero-trust architecture; ethics and responsible AI; governing generative AI pipelines; governing agentic AI and multi-agent systems; data governance in elections and the public sphere; AI regulation across six jurisdictions; and the design of a governance control plane for 2030. Each chapter is anchored in Indian law and institutions while maintaining a comparative, cross jurisdictional perspective.

---


### 104. [Mycelium: A Meta-Study of Hallucination Detection Across Provenance, Typology, and Granularities](https://arxiv.org/abs/2610.33608)

**<font color=#1a73e8>作者：</font>** Julia Belikova, Elisei Rykov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination detection is increasingly important for evaluating and deploying large language models. However, existing methods are often compared across benchmarks that define and measure hallucination in substantially different ways, making reported scores difficult to interpret across settings. We study hallucination detection as a benchmark-conditioned measurement problem and organize existing benchmarks along three axes: provenance, which describes how model outputs and evidence conditions are obtained; typology, which captures the factuality and faithfulness failures represented by benchmark labels; and granularity, which specifies the unit at which hallucinations are annotated, predicted, and evaluated. Using this framework, we analyze how benchmark construction, annotation, and evaluation choices shape the underlying prediction task, and relate detector mechanisms and assumptions to the settings in which their performance is measured. We also examine span-level evaluation, where variation in annotation boundaries can substantially affect reported results, and propose Span Coverage F1 as a complementary containment-based metric. Our analysis clarifies what detector scores capture, highlights limitations of cross-benchmark comparisons, and motivates more explicit evaluation of generalization across benchmark conditions.

---


### 105. [When Generated Information Returns: Error Persistence in LLM-Mediated Information Ecosystems](https://arxiv.org/abs/2610.33617)

**<font color=#1a73e8>作者：</font>** Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly produce online articles from material that later becomes input to other models. This circulation connects individual responses to the information available for subsequent generation. We study a consequential distinction: an article can avoid endorsing a false claim while preserving the concrete details that enable its reproduction. Our framework connects claim content, expressed stance, and downstream reuse to explain selective error persistence under a continuing supply of accurate and inaccurate information. We implement a controlled community writing process that varies whether published articles return as inputs, matching external supply, input capacity, and generation volume. Across twelve factual targets and four production models, recirculation increases the presence of complete false claims by 7.29 percentage points at the final round while reducing explicit endorsement by 8.33 points. Effects differ across facts and models. Paired interventions then abstract eligible error details within fixed histories while preserving correct content and the surrounding controversy. Error reproduction remains largely unchanged across the evaluation targets, while a development quotation target exhibits local reductions. These findings connect persistent errors to the information available throughout a writing process and motivate evaluation of both what models affirm and what their publications supply to future writers.

---


### 106. [RSI Arena: Towards Recursive Self-Improvement with Human Feedback](https://arxiv.org/abs/2610.33624)

**<font color=#1a73e8>作者：</font>** Yue Huang, Yanbo Wang, Lichi Li 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can AI agents autonomously train useful language models and improve them using feedback from users? We introduce RSI Arena, a two-stage study of autonomous post-training as a step toward recursive self-improvement. Ten frontier models act as training agents, each starting from NVIDIA Nemotron 3.5 Lightning 30B-A3B Base. During a six-day first stage, each agent has 1,000 GPU-hours and $300 in API credit on a shared 64-GPU cluster, independently selecting data, implementing training procedures, and choosing checkpoints. We evaluate their models on 20 benchmarks and through blind human evaluations. All ten agents produce working assistants, with the strongest model, trained by GPT-6 Astra, closing a median of 76% of the base-to-Instruct gap across 12 capability benchmarks. Its human-preference rating is also close to NVIDIA Instruct after statistical adjustment for answer length and formatting. In Stage 2, each agent receives the comparison records and votes involving its Stage 1 model and is given three additional days for further training. Using NVIDIA Instruct as a common reference across the two evaluation rounds, we observe an improvement from Stage 1 to Stage 2 in the style-adjusted relative rating of eight of the ten models. We show that benchmark gains were modest, with no clear link to preference gains, while some agents encouraged longer responses and one model showed increased harmful compliance on StrongREJECT. RSI Arena provides an auditable setting for studying how human feedback can guide autonomous model development. It takes a step toward recursive self-improvement with human feedback (RSIHF), in which people help define what improvement means for the AI systems they use.

---


### 107. [RAQ-MLA: Role-Aware Quantization for Multi-Head Latent Attention Caches](https://arxiv.org/abs/2610.33625)

**<font color=#1a73e8>作者：</font>** Tianqi Chen, Xunchao Li, Linchuan Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Head Latent Attention (MLA) has been adopted by recent frontier large language models. Instead of per-head keys and values, MLA caches a compressed KV latent that is up-projected into keys and values at decode time, together with a narrow positional key that carries position information into the attention score. Existing KV-cache quantization methods are designed around the keys and values of standard attention and do not account for what MLA actually caches, which costs accuracy at low bit widths. We analyze the MLA cache both in activation distribution and in how quantization error propagates to the attention output, and show that the two cached tensors play different roles: the latent mainly supplies the values, whereas the positional key dominates the attention score. We therefore propose RAQ-MLA (Role-Aware Quantization for Multi-Head Latent Attention Caches), which fits an invertible transform to each cached tensor against the error that tensor delivers to the attention output: attention-weighted value error for the latent and score perturbation for the positional key. Without training, RAQ-MLA quantizes the full MLA cache to about 2.5 bits per element, a 6.5x increase in theoretical KV-cache capacity, while remaining nearly lossless on reasoning and coding tasks across four MLA models.

---


### 108. [ProbeID: Verifying MCP Tool Identity for LLM Agents under Registry Drift](https://arxiv.org/abs/2610.33633)

**<font color=#1a73e8>作者：</font>** Guanxing Chen, Sining Zhang, Haohuai He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agents select tools by copyable descriptions, which cannot establish which implementation runs. ProbeID compares canonicalized responses to schema-valid probes with a trusted admission reference and abstains on ambiguity, so a squatter must copy probe-observable behavior. With the gold present, independent probes and a fixed margin, standard concentration arguments give a shared probe budget logarithmic in the candidate count and bound the joint probability of a wrong decision. On cached MCP-IdentityDrift cases, strict choice reaches \(0.956\) hit@1 while description routers fall near chance, but simpler exact comparisons tie it, MMD better tolerates heavy value noise, and a 32B behavioral judge is similarly accurate at higher cost. Random probes from agent banks and a prospective held-out study of 38 tools test theory-set thresholds. On the agent banks, equality refuses every reachable replacement from 64 probes and the bounded distance from 512, and sharper post hoc gates halve both. Two tools whose drift no bank probe reaches always pass. In an MCP-Bench agent, verification cuts tainted tasks from 15 to 9 of 16 at unchanged task success. Over eleven weeks, 7 of 59 real tools changed responses despite version pins. Verification depends on reference integrity, probe coverage, and response noise.

---


### 109. [AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment](https://arxiv.org/abs/2610.33644)

**<font color=#1a73e8>作者：</font>** Shunchao Zhou, Chang Yang, Jingrui Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research ideas are always proposed under resource constraints: a plan must fit the available compute, API credit, and time. Yet evaluations of research-ideation agents mostly score unconstrained novelty or overlap with a published paper, and their LLM judges are rarely checked against peer review. We introduce AlphaIdeaBench, a benchmark of 100 ideation tasks (50 workshop calls for papers and 50 open problems stated in surveys), each paired with an explicit resource budget and a shared proposal schema. An LLM judge scores each proposal on 12 dimensions covering validity, novelty, and feasibility. To validate the judge, we compare its scores on four novelty axes (problem, method, scenario, and insight) with scores derived from reviewer comments on 600 papers from ICLR 2026, NeurIPS 2025, and ICML 2025. For problem and method novelty, Gemini 3.7 Flash is within one point of the reviewer-derived score on 94-97% of papers; agreement on scenario novelty is relatively lower. We evaluate eight published harnesses on a shared backbone and, within one harness, eight backbone LLMs. CoI-Agent obtains the highest overall score, narrowly ahead of SciMON, which leads on method and insight novelty. All harnesses score low on scenario novelty and rarely change the problem setting. The backbone largely determines which open problem a proposal targets, whereas the harness determines whether a proposal addresses one problem or combines several. Weaker backbones such as Llama 4 Scout fail to carry out that harness's strategy and score low on budget feasibility. Finally, when only the budget is varied on three topics, a larger budget changes the experimental setting on compute-intensive topics but only adds tests on an inexpensive one. We release the tasks, rubrics, and scores to foster standardized, reproducible benchmarking of future research-ideation agents under constraints.

---


### 110. [PreView: Enhancing GUI Grounding with Preprocessed Views and Cues](https://arxiv.org/abs/2610.33645)

**<font color=#1a73e8>作者：</font>** Wenjun Hou, Kaishuai Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI grounding requires locating small controls in cluttered screenshots and identifying which control a natural-language instruction refers to. Cropping and enlargement can expose local detail, but the resulting image may still leave ambiguity about the intended target. We propose PreView, an auxiliary preprocessor that improves the inputs to an existing grounding model without further training that model. PreView prepares two complementary types of input features: task-relevant views for localization and candidate-specific cues for target understanding. A trained lightweight auxiliary model predicts and refines a center, crops the screenshot into a local view, and enlarges that view for zoomed-in grounding. It also prepares a visual cue (i.e., a red-circle marker with a location hint) and a textual cue describing the candidate's identity or function. The frozen grounding model uses the prepared inputs to predict the final click. Across five benchmarks, PreView improves the average grounding accuracy of Qwen3-VL-2B, OS-Atlas-4B, and Qwen3-VL-4B without further training these grounding models. Extensive analyses examine the contributions of views and cues, center refinement, and visual input budgets.

---


### 111. [TAD: Distilling Vision-Language-Action Policies from Teacher Trajectories Alone](https://arxiv.org/abs/2610.33650)

**<font color=#1a73e8>作者：</font>** Yun Zhu, Da Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online distillation of vision-language-action (VLA) policies commonly relies on teacher action scores that an inference-only interface may not expose. Trajectory-only Adversarial Distillation (\gad{}) instead turns a fixed bank of teacher joint-position features into adaptive feedback: a discriminator compares feature marginals from teacher and student rollouts and supplies rewards for on-policy learning. The student interacts with the environment without online teacher queries or environment task rewards. On ManiSkill \texttt{PutOnPlateInScene25Main}, \gad{} improves OpenVLA-OFT (7B) from $26.2\%$ to $76.6\%$ \successonce{} ($+50.4$ percentage points) and from $20.3\%$ to $58.6\%$ \successend{}. It trails white-box on-policy distillation (OPD) at $81.6\%$ / $59.4\%$ by $5.0$ / $0.8$ percentage points ($n{=}256$ evaluation trajectories per checkpoint). The tested four-epoch continuation achieves the highest \gad{} result without additional teacher data. This best run uses $5\times$ OPD's student interaction budget and $12.5\times$ its complete-rollout batch-passes. The comparison demonstrates online VLA improvement without teacher scoring while quantifying unequal interaction and optimization budgets.

---


### 112. [Jointly Modeling Preferences and Imperfect Decision-Making in Large Language Models](https://arxiv.org/abs/2610.33651)

**<font color=#1a73e8>作者：</font>** Axel Abels, Elias Fernández Domingos, Tom Lenaerts  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do preferences Large Language Models (LLMs) express in standard elicitation tasks predict their strategic behaviour? LLM agents interacting with humans and other AI systems face potentially conflicting objectives, such as individual welfare, group welfare, and environmental concerns. Prior work characterizes LLM preferences through behavioral-economic and psychological elicitation or strategic games, but rarely tests consistency across settings and prediction in other strategic environments. This requires modeling how competing objectives jointly shape behavior, whereas existing approaches typically measure preference dimensions in isolation. Drawing on utility theory, we introduce the Preference-Behavior Model (PBM), which combines a preference representation with mechanisms capturing imperfect utility maximization. We formulate estimation as an inverse-game problem, jointly inferring preferences and behavioral parameters from observed choices. We evaluate PBM in three social dilemmas that expose conflicting motives: a Public Goods Game, a Collective-Risk Dilemma, and a Common-Pool Resource dilemma. We find that while preferences estimated from established behavioral economic elicitation instruments do not consistently predict behavior in these dilemmas, models fitted in one dilemma retain predictive value in others, suggesting that inferred preferences capture meaningful aspects of LLM decision-making that elicitation instruments may miss. Finally, we assess alignment with persona instructions, finding that inferred preferences broadly reflect intended priorities with specific divergences across dimensions, LLMs, and games being identified by our approach. Our methodology provides a framework for studying how consistently LLM preferences explain behavior, assessing alignment with intended priorities, and revealing trade-offs and behavioral patterns that standard elicitation may miss.

---


### 113. [Power-of-Two Leaky Integrate-and-Fire Neurons for Event-Driven Vision-Language-Action Inference](https://arxiv.org/abs/2610.33658)

**<font color=#1a73e8>作者：</font>** Rui Liu, He Lv, Ziyao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, yet their reliance on dense, continuous-valued computation presents a fundamental challenge for energy-constrained deployment. Inspired by the sparse, event-driven signaling and temporal integration mechanisms of biological neurons, a promising alternative is to introduce spiking computation into VLA models. However, enabling such computation without restructuring pretrained policies or compromising closed-loop control remains an open challenge. To address this challenge, we introduce the Power-of-Two Leaky Integrate-and-Fire (PoT-LIF) neuron, which emits signed spikes with power-of-two amplitudes. By combining magnitude-coded spike events with residual-preserving membrane dynamics, PoT-LIF enables continuous information to be progressively represented through discrete spikes. The Heartbeat formulation further localizes this process within weighted projections, bridging biologically inspired spiking computation and pretrained VLA architectures without modifying their external inference interfaces. We integrate PoT-LIF into the vision projection, vision-language projection, and action projection of $\pi_{0.5}$ and evaluate both operating modes over 2,000 paired closed-loop LIBERO episodes per configuration. Standard-mode PoT-LIF VLA achieves success rates of 96.90% and 96.35% at $T = 1$ and $T = 2$, respectively, while Heartbeat mode achieves 97.25% and 96.90% at $T = 2$ and $T = 4$, compared with 96.70% for the original continuous-activation $\pi_{0.5}$ baseline. At $T = 1$ with a 60.01% firing rate, PoT-LIF uses approximately 1/7.67 of the dense-reference arithmetic energy, corresponding to a modeled reduction of 86.95%.

---


### 114. [SWE-Ladder: Learning to Localize, Reproduce, and Patch via Progressive Privileged Self-Distillation](https://arxiv.org/abs/2610.33667)

**<font color=#1a73e8>作者：</font>** Xudong Cai, Zhengxi Lu, Yuchen Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Resolving a repository-level issue typically requires a software-engineering (SWE) agent to localize the faulty code, reproduce the failure, and patch the code. Reinforcement learning trains such agents from a single test result on the final patch, while on-policy self-distillation (OPSD) adds token-level supervision from a teacher with privileged evidence, exposing the full reference patch at every step. Neither provides stage-specific guidance for localization or reproduction. We propose SWE-Ladder, which turns the verified repair of each training instance into stage-specific evidence: the changed files and lines for localization, the fail-to-pass tests for reproduction, and the diff for patching. A rule-based router assigns each step of an end-to-end rollout to a stage based on its tool call, a frozen teacher sees only the matching evidence, and the stages are distilled in repair order while GRPO optimizes the full trajectory. With Qwen3-4B-Instruct-2507 on SWE-bench Verified under the R2E-Gym scaffold, SWE-Ladder improves pass@1 from 9.6% to 16.4%, compared with 10.4% for GRPO and 12.4% for OPSD with the full patch. Under the OpenHands scaffold, it improves pass@1 from 13.0% to 17.6%. Reversing the stage order under R2E-Gym reduces pass@1 to 11.4%.

---


### 115. [Rescuing Your Pruning: Rethinking Visual Token Pruning and Post-Training Recovery in MLLMs](https://arxiv.org/abs/2610.33688)

**<font color=#1a73e8>作者：</font>** Peiran Yin, Hao Wu, Zihao Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning substantially reduces the inference cost of multimodal large language models (MLLMs), yet existing methods are mostly training-free and plug-and-play. They treat the resulting performance drop as an inevitable cost of compression and pursue increasingly complex pruning rules. We rethink this view through two questions: how much of the loss can post-training rescue, and, building on this recovery, how can joint compression push pruning to its limit? We curate a 282K-sample post-training mixture covering general VQA, reasoning, OCR, and grounding, and post-train 36 configurations that drop or merge tokens under a unified protocol. Post-training rescues most of the loss, even for OCR and grounding, and its adaptation gain in closing the gap between the pruned and the dense model grows as the budget tightens. For joint compression, we find that the vision encoder, not the LLM, dominates prefill time in native-resolution MLLMs, so where tokens are removed matters more than how many: keeping 40% of tokens at the encoder runs faster than keeping 10% at the projector. Our best configuration prunes the encoder lightly and the projector aggressively, leaves the LLM intact, and keeps general understanding and reasoning at the dense level. It accelerates the LLM stage by 3.49x but the end-to-end time-to-first-token by only 1.54x, showing that LLM-stage speedups overstate end-to-end gains. We hope these findings offer insights for future research on joint visual token compression. Our data, protocol, and code will be released.

---


### 116. [PathKGen: Pathology Knowledge Assisted MLLM for Explainable Histopathology](https://arxiv.org/abs/2610.33691)

**<font color=#1a73e8>作者：</font>** Nadun Rajapaksha, Sandun Herath, Devnith Wijesinghe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole Slide Image (WSI) analysis serves as the fundamental method for the clinical diagnosis of cancer in digital histopathology. Recent advances in Multimodal Large Language Models (MLLMs) have enabled state-of-the-art (SOTA) automated histopathology report generation. However, MLLMs reason purely through distributions encoded in their neural parameters, limiting the amount of knowledge and reasoning logic they can contain given the model scale. Their black-box reasoning poses another challenge to the human interpretation of intermediate reasoning. We address these issues by utilizing knowledge graphs to inject external structured knowledge for MLLMs to reason over, while making this reasoning component visible. Knowledge graphs are capable of partially externalizing the containment of medical knowledge, an area that remains underexplored in pathology report generation. We introduce PathKGen, a knowledge graph-assisted MLLM for histopathology report generation. PathKGen has two main branches: (1) a visual path that learns visual token inputs to the MLLM using pathology foundation models, and (2) a knowledge path that learns knowledge token inputs by extracting key morphological features of WSIs through querying a pathology-specific knowledge graph. A comprehensive evaluation on WSI-Bench dataset shows that PathKGen surpasses previous SOTA methods while revealing diagnostic reasoning as visually intuitive graphs. Due to its modular design, the proposed knowledge path is complementary to vision-aligned MLLMs and can be extended to other applications by curating domain-specific knowledge graphs to generate knowledge tokens.

---


### 117. [Gender Associations in LLM-Mediated ADHD Self-Diagnosis](https://arxiv.org/abs/2610.33697)

**<font color=#1a73e8>作者：</font>** Matilde Elene Hansen, Ross Deans Kristensen-McLachlan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used for medical self-diagnosis. However, the way demographic cues shape outputs in these interactions remains poorly understood. This is particularly consequential for diagnoses like ADHD, where persistent gender disparities are not fully aligned with the clinical evidence. We adapt the Context Association Test (CAT) to evaluate whether GPT-4o responds to gendered ADHD associations in a zero-shot, self-diagnostic setting. We show that explicit cueing consistently amplifies certain ADHD subtype associations while implicit cueing produces near proxy-aligned distributions. These divergences suggest that explicit demographic cues may activate bias-mitigation mechanisms that over-correct rather than eliminate bias, whereas implicit cues appear to reflect the model's default behavior. Our results demonstrate that evaluating gendered bias in LLM-mediated self-diagnosis requires careful attention to the demographic associations a model encodes.

---


### 118. [Seeing the Options: Typed Decisions over Visual Candidates with Reusable Option Memory](https://arxiv.org/abs/2610.33702)

**<font color=#1a73e8>作者：</font>** Fengxin Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Typed decision-making tasks in agents, such as UI element selection, product recommendation, and chart matching, require models to choose from a set of discrete candidates. While prior work demonstrates that text-only System One models achieve four key properties including candidate-order invariance, scalability, and cache reuse via separate request-candidate encoding, extending them to multimodal settings where candidates are visual remains underexplored. We introduce Iris, a framework that accommodates image, text, or hybrid candidates while preserving the core decision module. We prove that order invariance and exact cache reuse hold for any per-candidate encoder under Iris, and derive the closed-form latency reduction. We construct a visual-candidate benchmark from Multimodal-Mind2Web (K=16, deduplicated, order-shuffled, three generalization splits). Independent encoding (Iris) achieves 78.4 / 72.1 / 74.8 percent accuracy with zero-flip rate under candidate reordering. Joint encoding reaches 90.6 / 89.5 / 91.6 percent but suffers an 8 to 10 percent answer-flip rate when shuffled. To bridge this gap, we propose a design that encodes each candidate conditioned on the request state without inter-candidate cross-attention; it preserves strict order invariance, enables forked cache sharing, and attains 91.7 / 86.5 / 90.0 percent accuracy at one-third of OneJev latency with calibrated null probabilities (AUROC 0.93 to 0.97). Reusing image candidates across requests cuts latency by 37x at K=256 and 191x at K=2048. On MetaEncoder benchmarks, Iris-4B achieves 100 percent on JevBench original and easy, outperforming 30B MetaEncoder and 27B OpenJev. Finally, we resolve a systems bottleneck on Ampere GPUs: reformulating Qwen3.5 patch-embedding Conv3d into its exact matrix-product form accelerates processing by 350x. Code, data, and checkpoints: this https URL.

---


### 119. [VulDec: Vulnerability Detection in Binaries via Neural Decompilation](https://arxiv.org/abs/2610.33716)

**<font color=#1a73e8>作者：</font>** Francesco Crescenzo Grasso, Pietro Liguori, Roberto Natella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated vulnerability detection in binary executables is challenging due to the lack of source code and the limited semantic information available at the assembly level. Despite significant progress in machine-learning-based code analysis, the field still lacks methodologies and large, high-quality datasets that provide vulnerable code jointly at assembly- and source-level with precise vulnerability labels. To address this gap, we introduce VulDec, consisting of (i) a new large-scale, carefully curated dataset aligning real-world Assembly-C function pairs with detailed CWE annotations across multiple architectures, and (ii) the first end-to-end framework that leverages neural decompilation for binary vulnerability detection. Tuned LLM-based neural decompilers trained on our dataset achieve strong source-level recovery across architectures (Edit Similarity of approximately 56%, BLEU-4 of approximately 43%), while our tuned LLM-based detectors reach a macro F1-score of 0.61 on an in-distribution realistic test set (3% vulnerability rate). Our findings provide evidence that neural decompilation offers a powerful alternative to conventional low-level binary representations, facilitating robust binary vulnerability detection.

---


### 120. [Trust Mechanisms for Offline Generative AI at the Edge: A Connectivity-Regime Framework and an Empirical Study on a Raspberry Pi 5](https://arxiv.org/abs/2610.33732)

**<font color=#1a73e8>作者：</font>** Georgios Feretzakis, Alexandros Papaspyridis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative AI and large language models (LLMs) are moving into the Internet of Things, yet most deployments assume cloud connectivity, and many IoT settings have intermittent, restricted, or no connectivity. We propose a connectivity-regime framework (C0-C4), a taxonomy of inference-time trust mechanisms, and signed, versioned knowledge packs as the update channel for disconnected regimes, and evaluate them on a Raspberry Pi 5 running fully local retrieval-augmented generation under network isolation, with three Qwen2.5 model sizes, three context sizes, and 300 SQuAD 2.0 questions. An empirically calibrated retrieval-score gate detects knowledge gaps almost perfectly (AUROC 0.97) but in-topic unanswerable questions poorly (0.68). A deterministic output validator converts malformed outputs into explicit abstentions with no observed loss of correct answers, while the NLI-based verifier we tested adds little; for the 7B model, 96% of substantive answers to unanswerable-labelled questions match normalized spans of the retrieved passages. A 3B model achieves the same gold-answer containment rate as a 7B model at less than half the latency and estimated energy, although the 7B model far more often exceeds a token-F1 threshold of 0.5; five retrieved passages lower correctness from 75% to 52% compared with three. Verifying a signed pack takes about 4.5 ms versus about 29 min for embedding its passages on the device; signature and hash checks alone accept six of nine tested update attacks that layered verification rejects. Yet a validly signed poisoned pack passes every pack check: on 30 previously correct questions, correct answers drop to zero and 14 return the injected answer. None of the mechanisms we evaluated establishes the truth of the evidence. We release code and data.

---


### 121. [A Distribution-Matching Perspective on LLM Training Algorithms](https://arxiv.org/abs/2610.33740)

**<font color=#1a73e8>作者：</font>** Yanxing Huang, Bingzhang Yan, Zihan Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we propose a unified framework for training algorithms across different stages of modern large language model development, based on the perspective of distribution matching. We show that a broad class of language model training algorithms can be interpreted as minimizing a certain divergence between the current model and a target distribution, and that characterizing the properties of this target distribution provides substantial insight into the behavior of the corresponding training algorithms. By analyzing specific forms of the target distribution, we establish that On-Policy Distillation (OPD) enjoys an advantage over classical Knowledge Distillation (KD) when the current model distribution is close to the target distribution, while exhibiting a disadvantage when the two distributions are far apart. Furthermore, when the target distribution itself depends on the model being optimized, we show that the accumulation of estimation variance can induce a deterministic degradation of the target distribution. These results provide a theoretical explanation, at least in part, for the long-term behavior of existing Reinforcement Learning (RL) algorithms. With this intuition we further designed Conditional KL (CKL) regularization for mitigating the degradation of the target distribution. CKL can effectively preserve mode diversity while relaxing the constraint imposed by classical KL regularization on reward improvements. We believe this theoretical perspective can bring some new understanding of language model training algorithms and provide useful guidance for future research.

---


### 122. [Beyond Prompts: A Systematic Study of LLM-Based Machine Translation Evaluators](https://arxiv.org/abs/2610.33741)

**<font color=#1a73e8>作者：</font>** Dmitry Popov, Roman Bokhyan, Ekaterina Enikeeva 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based evaluators have rapidly become a standard tool for machine translation evaluation, yet the design choices that shape their behavior remain poorly understood. We present a systematic study of how instruction design, few-shot demonstrations, backbone model choice, and multi-step workflows affect span-level and ranking-based MT evaluation. We collect new expert RATE annotations on WMT24 and WMT25 English-Russian translations, with transfer validation on MQM- and ESA-annotated benchmarks across five additional language pairs. Our experiments reveal four robust findings: instruction structure shapes evaluator behavior, high-quality demonstrations matter more than quantity, frontier backbones exhibit distinct evaluator profiles (recall-, precision-, or ranking-oriented), and fusing outputs across diverse backbones outperforms single-evaluator multi-call setups. Although evaluator design exposes a large combinatorial space, several discovered design principles transfer consistently across annotation protocols and language pairs. We synthesize these findings into ORBIT, a family of LLM-based MT evaluators. Our strongest configurations achieve expert-level performance in error span detection and in Accuracy and Fluency ranking at roughly 20x lower cost than expert human annotation.

---


### 123. [Ring-0 by Default: Agents as Operating Systems (AaOS)](https://arxiv.org/abs/2610.33753)

**<font color=#1a73e8>作者：</font>** Xiang Li, Aichun Huang, Zuyao Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents now read and write files, start processes and subagents, fetch network content, load third-party extensions, and save and resume state, which are the responsibilities of an operating system. They gained these functions within about three years, but not the protections that operating systems built over five decades: whatever the model outputs, whether it follows the user, a tool result, or a downloaded skill, runs with the full authority of the host user, in effect at ring 0. Prior work builds an operating system for agents (OS4A); we argue that a deployed agent already is like an operating system (AaOS) and analyze it as one. Taking the mechanisms of standard OS textbooks as a checklist, we map 116 mechanisms in 19 subsystems to their agent counterparts, from product documentation, source code, and the literature, and label each as isomorphic, degraded (function present, protection dependent on the model), missing, mutated, or novel. Only 11 are isomorphic and 65 are missing, most of them protections: privilege separation, resource quotas, transactions, and tamper-proof audit. Existing defenses confine the whole agent or review its extensions and leave this interior unprotected, and by Anderson's reference-monitor criteria (non-bypassable, tamper-proof, verifiable), rules written in the prompt satisfy none.
We test the map with thirteen experiments on Claude Code, Codex CLI, and Gemini CLI, covering 25 mechanisms whose enforcement documentation cannot settle: 16 match the analysis, 7 gain a more precise description, and 2 change verdict. Checks sit in single tools, so the shell bypasses them; all three CLIs load forged transcript records on resume; and task control, sub-agent permissions, and model-based monitors are weak. We identify five problems for which no OS defense transfers and derive a prioritized list of open problems from the gaps of the map.

---


### 124. [Enhancing LLM-Based Vulnerability Detection via Representation-Aware Logical Ensemble](https://arxiv.org/abs/2610.33756)

**<font color=#1a73e8>作者：</font>** Francesco Crescenzo Grasso, Pietro Liguori, Roberto Natella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated vulnerability detection in C source code is a long-standing challenge, as traditional static analysis tools often trade precision for scalability and struggle with complex vulnerability patterns. Recently, large language models (LLMs) have shown promising results; yet, most approaches rely on a single code representation, implicitly assuming uniform suitability across vulnerability types. In this work, we systematically study LLM-based vulnerability detection under multiple code representations, including raw source code, Abstract Syntax Trees (AST), and Control Flow Graphs (CFG). Through extensive empirical analysis, we show that different representations exhibit complementary strengths, with specific views being more effective for particular classes of vulnerabilities. Building on these findings, we propose a Representation-Aware Logical Ensemble (RALE) that integrates LLMs trained on different code representations through explicit logical rules and majority voting. While single-representation models achieve up to 73% F1-score, our integrated approach reaches 78% F1-score, with commensurate gains in accuracy, precision, and recall, consistently outperforming individual models. These results highlight the importance of explicitly leveraging complementary code representations when combining LLMs for effective vulnerability detection.

---


### 125. [All the Facts, Still the Wrong Answer: Integration Gaps in Vision-Language Models](https://arxiv.org/abs/2610.33764)

**<font color=#1a73e8>作者：</font>** Yuyang Dai, Yuxia Wang, Zhuohan Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal reasoning requires models to combine multiple pieces of evidence into decisions that satisfy all relevant constraints. Evaluations centered on final-answer accuracy leave unclear whether failures arise from reading individual facts or using them together. We study this question through the multi-evidence integration gap, linking local fact recovery to global decision validity on controlled subset-selection and path-finding tasks. Our evaluation combines conditional performance given correct local answers with same-grid local queries, text-oracle inputs, retrieval controls, and constraint ablations. We further examine hidden-state probes and activation replacement across network depth, token positions, and model families. Across the evaluated models, accurate local recovery coexists with substantial global failure. For example, Gemma-3-27B recovers all evaluated isolated item facts correctly but achieves only 19.75% global validity on eight-item visual instances. Probes decode information about solution membership from global-prompt states, while corresponding clean-state replacement recovers failed decisions over model-dependent depth ranges. These findings show that recovering facts and representing solution-related information are insufficient for reliable joint decisions. They motivate evaluations and model improvements that explicitly target how available evidence is combined, alongside advances in perception and model scale.

---


### 126. [RoleHear: Pseudo-Labeling for Semi-Supervised Role-Attributed Streaming Speech Recognition](https://arxiv.org/abs/2610.33765)

**<font color=#1a73e8>作者：</font>** Zefang Liu, Chenyang Zhu, Sangwoo Cho 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Streaming automatic speech recognition transcribes at low latency but produces an unattributed word stream, while real-time applications such as customer-service analytics need each word tied to a speaker role. Role attribution is usually a separate stage, either an offline or streaming speaker-diarization model aligned to the words or a text-based large language model applied to the transcript, and role labels for training are scarce. We present RoleHear, a semi-supervised pipeline that makes a single cache-aware streaming transducer emit roles inline through lightweight in-vocabulary role tokens: a fast turn-boundary marker followed by a per-role token a few words later. An offline transducer teacher, fine-tuned into a role-attributed recognizer, relabels unlabeled audio, and a multimodal large language model supplies silver role labels where gold annotations are unavailable. The streaming student is fine-tuned on the mixture in a single pass. Across customer-service calls with gold roles and earnings calls with silver roles, RoleHear attributes roles accurately while preserving transcription quality and narrowing the gap to the offline teacher.

---


### 127. [StateWise: Teaching Language Models to Track and Obey Evolving Constraints in Multi-Turn Dialogue](https://arxiv.org/abs/2610.33766)

**<font color=#1a73e8>作者：</font>** Samarth Varshney, Ritu Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users of conversational assistants rarely state all requirements up front: they add constraints, amend them, withdraw them, digress, and return. Instruction-tuned LLMs fail here in two ways: active constraints stop being honored as turns accumulate (persistence failure), and withdrawn constraints keep being enacted (relapse). The only existing repair we know of is an external ledger that re-injects a compiled specification every turn. We propose StateWise, a self-improving approach that teaches a single LLM to maintain its own revisable constraint state, a typed state with tombstones for revoked constraints, so persistence and relapse are measured by executable checkers and ground-truth states are compiled for free. StateWise fine-tunes the LLM on two complementary skills, summarizing a dialogue into its constraint state and responding conditioned on that state, then self-trains on its own trajectories, keeping only turns that pass an exact round-trip check against the compiled state. This teaches 7-8B models to track the state almost perfectly but, surprisingly, not to obey it: on Llama-3.1-8B every supervised variant roughly doubles relapse. We therefore add a preference stage on self-generated relapse contrasts, where the rejected response enacts a revoked rule and the chosen one passes the round-trip check. On two backbones with held-out constraint families and unseen phrasings, StateWise cuts relapse by 8-22 points relative to supervised self-training, lifts conversation success by 8-19 points over the backbone, and beats an oracle compiled-ledger baseline on relapse with no inference-time scaffolding. We also characterize the recipe's cost on general instruction-following benchmarks and study weight interpolation as a mitigation.

---


### 128. [Local Entropy Fluctuations for Black-Box LLM-Generated Text Detection](https://arxiv.org/abs/2610.33767)

**<font color=#1a73e8>作者：</font>** Xinpeng Wang, Bruce Rushing, Zhizhen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Zero-shot detection of machine-generated text is vital for mitigating the risks of large language models (LLMs) misuse. While the state-of-the-art dual-model detectors and resampling-based detectors outperform single-model statistical detectors on unprompted continuations, they suffer a catastrophic breakdown on instruction-conditioned text in the black-box setting, where the source model is unknown. We analyze this failure and trace it to poor prompt conditioning for resampling-based methods and diminished cross-model discrepancy for dual-model detectors. Motivated by recent studies that human writing maintains a steady, uniform information flow, whereas machine-generated text exhibits sharp, localized entropy fluctuations, we propose a new metric, the Relative Peak Prominence Rate (RelPPR) to capture this structural contrast along the entropy trajectory and further leverage it as a signal for LLM-generated text detection. Extensive evaluations across diverse model families and datasets demonstrate that RelPPR achieves state-of-the-art black-box detection performance and remains the most reliable detector under various practical situations. Our code is available at this https URL.

---


### 129. [The Hitchhiker's Guide to System 1 Models: Fast Decision-Making Beyond LLMS](https://arxiv.org/abs/2610.33775)

**<font color=#1a73e8>作者：</font>** Haggai Roitman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models excel at reasoning and generation but their autoregressive, token-by-token inference makes them unnecessarily slow, expensive, and poorly calibrated for the many routine decisions (routing, gating, scoring, classification) that modern AI systems require at sub-second latency. A growing class of models addresses this gap: System 1 decision models, architectures that map an input directly to a typed, structured decision in a single forward pass. This guide provides a comprehensive, practitioner-oriented treatment of the field. We propose a five-family taxonomy covering encoder-based classifiers, reward models, non-autoregressive decision engines, contrastive decision models, and extraction models, and we provide in-depth coverage of each family's architecture, training methodology, and deployment trade-offs. A central theme is calibration: we develop the theory of proper scoring rules, analyze Reinforcement Learning for Calibrated Decisions (RLCD), and examine recently discovered phenomena including IIA violations, ordinal-scale bias, and few-shot recalibration under distribution shift. On the integration side, we describe how System 1 models serve as decision infrastructure within agentic workflows and System 1 + System 2 cascades that route between fast and slow models based on calibrated confidence. The guide covers 18 application domains, maps the rapidly growing open-source ecosystem (over 70 model reproductions in weeks), provides runnable code throughout, and includes a practitioner's checklist, an open-source model zoo, and 22 self-assessment questions with detailed answers. Spanning 190 references, it is intended as a unified entry point for researchers and engineers working at the intersection of fast decision-making, calibration, and production AI systems.

---


### 130. [TriageRAG: Failure-Aware Self-Training for Adapting Retrieval-Augmented Language Models to Specialized Domains](https://arxiv.org/abs/2610.33776)

**<font color=#1a73e8>作者：</font>** Samarth Varshney, Ritu Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) lets large language models (LLMs) answer knowledge-intensive questions from retrieved evidence, but adapting a general-purpose RAG system to a specialized domain such as medicine is difficult when only an unlabeled corpus is available. Self-training approaches such as SimRAG address this by letting the LLM write its own question-answer pairs from domain passages and fine-tuning on the pairs that survive a round-trip consistency filter. We observe that these approaches treat every retained example identically: they never ask whether the student already knows the answer, already extracts it correctly from the retrieved context, or fails - and if so, whether the failure lies with the reader or with the retriever. To tackle this, we propose TriageRAG, a failure-aware self-training approach that probes the student on each self-generated question with and without retrieved context, triages it into one of four categories (known, solved, context-failure, retrieval-failure), and routes each category to the training signal that addresses it, including a parametric route that teaches the reader to answer when retrieval misses. Probing is cheap and repeated every round, so the training mixture follows the student, and the triage histogram doubles as a label-free diagnostic of where the domain gap lies. Experiments on 11 datasets spanning three domains with a Qwen3-4B backbone, and on CS-Bench with Qwen3-8B, demonstrate that TriageRAG outperforms a budget-matched SimRAG by 1.2-6.4 points and is the only method that recovers the closed-book level in every case where retrieval hurts the base model. A single ablation identifies the mechanism: round-trip filtering removes every training context that lacks the evidence, and a reader that never sees such contexts learns to over-trust noisy retrieval.

---


### 131. [InfiniteWorld: Separating Visual Evidence from Familiar Physics](https://arxiv.org/abs/2610.33777)

**<font color=#1a73e8>作者：</font>** Tong Zhang, Yuxuan Cheng, Yun Peng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physical reasoning requires adapting familiar expectations to the dynamics of the observed world. Existing benchmarks establish broad physical capabilities, yet an overall score leaves unclear whether answers follow visual evidence when familiar rules no longer apply. We introduce InfiniteWorld, a benchmark that pairs physical-reasoning questions with simulator videos whose physical parameters are systematically altered. Its generation pipeline connects simulation, scene screening, paired video translation, question construction, and input checks. Five tasks assess law identification, parameter estimation, temporal reasoning, analytic counterfactual comparison, and law induction. The evaluation defines five matched input settings for each question, comprising text-only evaluation and ordered or shuffled observations from simulator and translated videos. We evaluate a diverse set of video-language models under these matched settings. The results expose a persistent preference for familiar physical rules. Frames improve performance for most models, but gains differ across tasks. Strong accuracy on Earth-normal questions coexists with poor recognition of altered dynamics, and Earth-normal answers remain common when the observed physics changes. Task scores and semantic agreement further distinguish matching physical factors from matching their amount, and correct answers from repeated errors. InfiniteWorld makes these behaviors measurable through paired changes in the evidence supplied for the same question, separating visual evidence from familiar physics.

---


### 132. [MTA-Zero: Self-Improving Multimodal Deep Search via Online QA-Solver Co-training](https://arxiv.org/abs/2610.33799)

**<font color=#1a73e8>作者：</font>** Xiangyu Peng, Jiaxin Zhang, An Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have become strong visual reasoners, yet remain limited in open-world, multi-step search that requires grounding images, selecting tools, and integrating web evidence. Existing approaches typically construct and filter fixed offline corpora whose question distributions cannot adapt as the target deep-search agent improves. Building on MTA-Agent's image-grounded QA construction, we present MTA-Zero, an online multimodal QA-Solver co-training framework for self-improving multimodal deep-search agents that requires no precomputed multi-hop corpus. Starting from image-grounded VQA seed contexts, a trainable QA Generator retrieves evidence and constructs verified multi-hop questions online. A separate deep-search Solver then selects tools, gathers evidence, and answers the generated questions. To focus generation on the Solver's learning frontier, we derive a Goldilocks reward for the QA Generator from the Solver's group-wise rollout success rate: questions solved by all rollouts or by none receive zero reward, whereas questions near the current frontier are favored. We optimize the two policies independently with GRPO, without sharing parameters or gradients. Across six multimodal deep-search benchmarks, MTA-Zero improves a Qwen3-VL-8B Solver from 36.91% to 51.58% mean accuracy and achieves performance comparable to GPT-5 under the same agent workflow. The same framework also improves a newer Qwen3.6-27B Solver by 10.82 points. These results show that verified online question generation provides a policy-specific curriculum for continually improving multimodal deep-search agents.

---


### 133. [Are We Done with UMLS Injection into Language Models for Medical Question Answering?](https://arxiv.org/abs/2610.33801)

**<font color=#1a73e8>作者：</font>** Yiran Zeng, Giacomo Frisoni, Lorenzo Molfetta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maybe not. The Unified Medical Language System (UMLS) has become an oracle for millions of clinicians and health system developers worldwide. Researchers have increasingly used knowledge graphs derived from UMLS to enhance language models' factual accuracy and reasoning traceability in high-stakes tasks. Medical Question Answering (MQA) is a prime testbed for integration, with benchmarks usually involving professional exercises such as disease diagnosis and drug prescription from patient history. Despite the assumed benefits, empirical evidence shows that UMLS-based graph injection typically yields modest performance gains. This paper reviews existing MQA work, critically analyzing the selected UMLS sources and their usage with language models, and probes each of these choices in isolation. We uncover methodological issues never discussed in prior work, from low UMLS coverage to weak subgraph retrieval pipelines. Based on our findings, we provide actionable recommendations to unlock the untapped potential of UMLS as an external knowledge source.

---


### 134. [IntentDelta: A Human-Constructed Benchmark for Evolving User Intent](https://arxiv.org/abs/2610.33806)

**<font color=#1a73e8>作者：</font>** Jieyu Zhou, Zijian Wang, Yun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model agents must adapt as users revise their requirements and priorities during complex tasks. We introduce IntentDelta, a human-constructed multi-turn benchmark with 638 trajectories and 3,766 turns across WebShop and TravelPlanner. Each turn pairs a user utterance with a cumulative intention state and human reference actions. The trajectories are cross-verified and cover feasibility- and preference-driven changes in constraints and priorities. We evaluate eleven agents on intention recovery and action quality. Average Intention Recovery is 33.1\% in TravelPlanner and 44.7\% in WebShop, while average Action Score is 31.6% and 41.0%, respectively. Agents struggle to preserve earlier requirements and distinguish soft preferences from must-have constraints. Correct intention recovery also does not guarantee successful execution, highlighting challenges in translating evolving user intentions into actions.

---


### 135. [Rectified Language Flow](https://arxiv.org/abs/2610.33811)

**<font color=#1a73e8>作者：</font>** Baiyu Su, Runlong Liao, Lizhang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous-state flow and diffusion models offer a promising approach to fast, parallel language generation, but matching the generation quality of autoregressive models remains challenging. We present Rectified Language Flow (ReLF), a language model that generates text by transporting noise to token embeddings using rectified flow. ReLF combines several complementary design choices: fixed token embeddings constructed with Hellinger-SVD, self-conditioning guidance trained with cross-entropy, and regularized reflow for few-step generation. We further introduce singular logits, which combine an analytically computed term that drives commitment to a valid token embedding as noise vanishes with a bounded neural residual that learns contextual token preferences. With 64 function evaluations on OpenWebText, ReLF achieves lower generative perplexity than autoregressive baselines at matched diversity across all three model sizes tested, while also outperforming prior continuous flow methods in this setting. After two reflow rounds, ReLF still outperforms autoregressive baselines with 16 function evaluations while generating 1,024-token sequences 15-19 times faster at batch size 1.

---


### 136. [Task Format as a Factor in Adaptation: A Controlled Comparison of LoRA and Full Fine-Tuning for Prompt-Safety Classification](https://arxiv.org/abs/2610.33813)

**<font color=#1a73e8>作者：</font>** John Alderete, Srirakshith Betageri, Jennifer Flynn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a language model for classification involves many design decisions. Comparisons of low-rank adaptation (LoRA) with full fine-tuning are common but often confounded, and task format is rarely studied. We compare both regimes on prompt-safety classification with a matched 400M encoder-decoder pair (Ettin) across three task formats, with up to 15 seeds per cell and pre-specified analyses. At the pre-specified learning rates, full fine-tuning leads LoRA by 2-3 pp in every architecture and format trained on the label alone. On the encoder, the gap closes once both rates are chosen by the same search. Training LoRA to write a reason after its verdict adds 4.0 pp and closes the gap, but a content-free sentence of equal length does not. Trained models score above a prompted 8B in domain but fall behind it on two of three out-of-distribution corpora, trailing by 8-23 pp on adversarial jailbreaks and flagging 27-66% of benign but harmful-looking prompts as unsafe, against the 8B's 2-3%. Together, the results suggest that the adaptation regime matters less than how each model is trained, its learning rate, and training target, and that in-domain accuracy alone is an incomplete guide to robustness.

---


### 137. [EnvLunch: The Environment as a Free Lunch for Learning to Interact](https://arxiv.org/abs/2610.33817)

**<font color=#1a73e8>作者：</font>** Wei Liu, Min Gao, Yali Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For agentic data analysis, language-model agents often require a large number of annotated tasks to learn how to interact effectively with executable environments (i.e., databases). While high-quality annotated tasks require heavy manual effort, an executable environment already provides rich interaction structure and verifiable outcomes. In this sense, the environment itself offers a free lunch, an additional set of verifiable tasks that require no human annotation. We propose EnvLunch, a warm-up stage that turns this environmental signal into agent training without human-written or model-generated task descriptions, before downstream agentic reinforcement learning. EnvLunch samples valid action trajectories, executes them to obtain final observations, and trains an agent to recover a functionally equivalent trajectory given only its final observation. This label-free warm-up enables the model to outperform the baseline by over 9 points on average across all downstream training budgets, and with few labels, the baseline needs 8 to 32 times as many annotated examples to match the accuracy that the EnvLunch model reaches at its smallest training budget. Letting the environment alone define the task yields a larger gain than having the model write its own tasks over the same environments, and this warm-up also improves fine-tuning on benchmarks beyond data analysis. EnvLunch therefore saves annotated tasks and provides a better starting point for fine-tuning agentic models when such tasks are limited.

---


### 138. [Reactive Optimizers](https://arxiv.org/abs/2610.33826)

**<font color=#1a73e8>作者：</font>** Xingjian Bai, Jia-Hao Liang, Jayden Teoh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a reactive optimizer that uses a pretrained language-model agent to inspect training dynamics and rewrite executable optimizer code during a single training run. The agent can change update rules and schedules for individual parameter groups, without optimizer-specific meta-training or memory transferred from other runs. We evaluate this approach, OPAL, on language modeling and image generation when a recipe has not been tuned for the target setting. Across the evaluated settings, it matches or improves on selected fixed recipes. Analysis of its decisions shows changes to learning-rate schedules, optimizer structure, numerical precision, and momentum. Controlled experiments also show adaptation to repeated data corruption and reduced overfitting. We report these behaviors together with the agent's computational cost and implementation requirements.

---


### 139. [EdgeDeID: A 0.6B Clinical De-identifier Trained Without Real Patient Data](https://arxiv.org/abs/2610.33839)

**<font color=#1a73e8>作者：</font>** Sina Daneshgar, Raya Namazi, Amirali Khosravi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> De-identifying clinical notes with a hosted language model discloses the information the step is meant to protect. We present EdgeDeID, a 0.6B-parameter decoder-only de-identifier that runs locally and is trained without real patient text: three LLM teachers write synthetic notes, a single labeler re-annotates them into one convention, and the model learns to emit a typed XML schema of the identifiers it finds. On a 100-note synthetic in-domain benchmark with manually verified annotations it reaches 0.994 micro-F1 and leaves no missed identifier in 99% of notes, against 0.857 and 12% for the strongest of eight off-the-shelf systems. Quantized, it runs on CPU in 615 MB. Of three additions to supervised training, only a verifier adapter helps: it separates complete from incomplete outputs of other systems at 0.94 AUROC, whereas reinforcement learning with a recall-weighted reward and a rule-based post-processing layer leave in-domain results unchanged. On MIMIC ICU nursing notes F1 falls to 0.48. The errors follow two properties our synthetic notes lack, telegraphic style and low identifier density, and three hand-written in-context examples recover 0.08 F1 without annotated target data.

---


### 140. [Sliding Networks: A Family of Residual Structures Preserving Feature Learning and Feature Diversity](https://arxiv.org/abs/2610.33840)

**<font color=#1a73e8>作者：</font>** Datong Zhou, Blake Bordelon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models tend to perform best at large widths and depths. The growing interest in scaling laws, especially in the language modeling domain, has motivated procedures for scaling up network widths and depths in order to preserve stability and computational efficiency of training dynamics. Existing depth-scaling approaches force a choice between retaining locally maximal \emph{feature learning} and preserving a form of \emph{feature diversity} in the residual stream arising from random differences between channels. We examine a \textit{joint scaling recipe} that preserves both. With residual width $N_\flat$, hidden width $N_\sharp$, and depth $L$, the key quantity is, by default, the limiting ratio $N_\flat/(N_\sharp L)\to\alpha$, while correlated initialization (Half Copy) can partially relax the resulting shape constraints. Theory and residual-MLP experiments support convergence at fixed positive $\alpha$ to an SDE limit with locally maximal feature learning. Hidden computations can then be redistributed between width and depth while preserving this limit, like turning melody into harmony and back. Language-model experiments nevertheless show performance differences under regrouping at fixed parameter count. These results distinguish approximating a limit (ODE or SDE) from scaling for better performance.

---


### 141. [Grounding on Request: Learning Modality Control in Vision-Language Models](https://arxiv.org/abs/2610.33841)

**<font color=#1a73e8>作者：</font>** Maxime Dassen, Alexander Martin, Andrew Yates 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When an image and its caption disagree, can a user reliably control which one a vision-language model (VLM) follows? Accuracy alone cannot answer this question, since a model might give the correct answer from parametric knowledge without following the requested evidence. We therefore evaluate modality grounding control through conflict-preserving counterfactual interventions. Specifically, Flip measures whether an initially correct answer follows an edit to the requested modality, while Stay measures whether it remains stable when the competing modality is edited. To learn this control, we build on neologism learning by introducing new words for visual and textual grounding, training only their embeddings while keeping the pretrained model fixed. We also introduce Counterfactual Twin-Margin (CTM) supervision, which uses paired interventions to teach how answer probabilities should change when the requested evidence changes. Across three VLMs on three existing benchmarks and our multi-attribute Ground-CF benchmark, we find that learned modality words improve control over natural-language instructions. Surprisingly, a single learned embedding per modality provides strong lightweight visual control and shows little average degradation on held-out values. LoRA remains strongest overall, although its visual advantage narrows under held-out evaluation. Moreover, counterfactual supervision improves control in several settings where standard supervision is weaker. Finally, we test our method on real-world news video and find that visual control improves when the relevant evidence is made easier to access. Overall, our results show that reliable modality control requires testing not only whether an answer is correct, but whether it continues to follow edits to the modality of choice.

---


### 142. [Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players](https://arxiv.org/abs/2610.33845)

**<font color=#1a73e8>作者：</font>** Changlian Ma, Limin Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can LLM agents carry a hard real-world problem from raw data to a system that holds its own against people? We study this in Hearthstone Battlegrounds, an eight-player auto-battler with stochastic shops and battles, hidden information and nearly a thousand interacting cards. We present AutoTavern, a self-improving research system: specialised LLM research agents share a typed research memory, every claim passes verification gates, and live games close the loop, so the agents improve the simulator, opponents and policy and, from the same feedback, their own research process; a human sets goals and rules on ambiguous mechanics. In 20 days AutoTavern built TavernGym, the first faithful, full-content reproduction of the live game, and delivered 23 versions of TavernAgent, trained with PPO against opponents calibrated to real games. TavernAgent plays complete games on the live ladder by itself: its rating rose from 6,000 to about 15,000 and, on the public leaderboard's measure, its last 20 records average a placement of 1.60 with 80% first places, better than the server's ten highest-rated players on every statistic (2.34, 59%). TavernBench, 960 tasks in 40 scenarios, shows that the system the agents built is the strongest player: TavernAgent answers 91% of the play tasks against at most 63% for frontier LLMs, and decides in 0.03 s where they need up to 26 s; within the second a live turn allows, it keeps 90% and no LLM more than 26%. LLM agents build far better than they play. We will open-source TavernBench and TavernGym at this https URL.

---


### 143. [ReGE: Stronger Agents through Experience Synthesis](https://arxiv.org/abs/2610.33861)

**<font color=#1a73e8>作者：</font>** Jiarong Liang, Yubo Wang, Zijie Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repeated attempts at interactive tasks uncover facts, useful operations, and failures that can inform subsequent execution. We introduce ReGE, a framework for turning this recorded experience into guidance for a fresh attempt. Its main implementation, ReGE-Syn, uses a single coach call to jointly synthesize bounded execution records and available artifacts into self-contained guidance, connecting task-specific findings with proposed actions and relevant pitfalls. A student starts from the task's initial environment state and adapts this guidance to current observations. Source generation, synthesis, and student execution use the same base model, without parameter updates or a stronger teacher. Across four benchmarks, ReGE improves accuracy by an average of 9.9 percentage points for GPT and 8.8 percentage points for Claude compared with unguided execution. On matched BrowseComp-Plus subsets, ReGE-Syn reduces guidance-construction tokens by 98.2\% on GPT and 95.5\% on Claude relative to adapted AggAgent, with observed success. Combined construction and execution tokens decrease by 15.7\% and 35.4\%, respectively, counting input plus output and excluding source generation. BrowseComp-Plus ablations further associate access to process information with fewer student steps and show that joint synthesis produces substantially shorter guidance than Direct history or Independent summaries, with observed success. These results demonstrate how agents can use their own recorded experience to improve subsequent task completion, and suggest a low-cost way to consolidate the execution records of parallel agent systems such as agent swarms.

---


### 144. [Late Breaking Results: Audio-Language-Action Models with Direct Speech Conditioning for Robotic Manipulation](https://arxiv.org/abs/2610.33866)

**<font color=#1a73e8>作者：</font>** Enfu Nan, Pu Zhao, Yixiao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models enable robots to follow instructions in typed text, limiting broader deployment in natural speech. The traditional solution by prepending a speech recognition before VLA to convert speech into texts would incur additional latency and propagate errors. To address this, we present Speech-$\pi_{0.5}$, which maps raw speech directly to motor commands without explicit textual transcriptions. Specifically, built on $\pi_{0.5}$, we use a cross-modal projection to convert voice frames directly into audio tokens with significant response latency reduction. To further improve the accuracy, we adopt split LoRA adaptation with dedicated audio and task adapters, under a two-stage training. Speech-$\pi_{0.5}$ achieves $3\times$ lower response latency than ASR pipeline while maintaining competitive task success on LIBERO, and generalizes robustly to unseen accents where a single adapter degrades significantly.

---


### 145. [FlashScript: Compiling Recurring Agent Workflows into Reusable Neuro-Symbolic Programs](https://arxiv.org/abs/2610.33876)

**<font color=#1a73e8>作者：</font>** Sadra Sabouri, Hosein Hasanbeig, Adam Sage 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Many agent tasks recur with new data or small changes, yet agents regenerate their reasoning and actions on each run, producing different results. Distilling a prior run into a skill helps the agent avoid earlier mistakes, but it still re-runs the full process each time, so runs can vary and incur that cost. We compile a successful agent run into a reusable neuro-symbolic program (NSP) with a set of guidelines we call FlashScript. Actions and data transformations become code, instance-specific values become parameters, and decisions that need model judgment become LLM calls. We identify three layers where these calls belong and three techniques that replace most of them with code. The compilation does not remove nondeterminism; it localizes it, so the deterministic program and its neural calls can be reviewed and tested separately. Across 120 WorkBench analytics tasks with Claude Haiku 4.5, the NSPs were correct and made identical tool calls on every run, using about 70 times fewer input tokens and a third of the runtime of a skill-guided agent whose runs were inconsistent. In a composite version of the tasks, the skill-guided agent's accuracy fell to 23%, and its output inconsistency increased, while the NSPs remained correct and identical across all runs. The NSPs successfully generalized to all 108 unseen instances of the same templates. Our findings suggest that NSPs from agent trajectories can be considered cumulative software assets for end-users to test, maintain, and reuse in their recurring workflows.

---


### 146. [DIGEST: Discovery-Guided LLM Tuning for Symbolic Regression](https://arxiv.org/abs/2610.33880)

**<font color=#1a73e8>作者：</font>** Kaifeng Jin, Ruizhong Qiu, Zihao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) seeks to discover mathematical expressions directly from data, without requiring task-specific scientific descriptions. Despite tremendous progress in both conventional search-based methods and recent LLM-based methods, two critical limitations largely remain. First (Limited Generation Flexibility), conventional search-based methods rely on either fixed search rules or specialized learned generators, severely limiting adaptive candidate generation across diverse expression structures. Second (Underutilized Search Discoveries), most LLM-based methods cannot reliably recover ground-truth expressions because they fall short in effectively leveraging the LLM itself to thoroughly digest past expressions or adaptively guide future search. To address these limitations, we propose DIGEST. To render greater flexibility in generation, DIGEST repurposes a pretrained decoder block from a lightweight LLM into a symbolic policy for Genetic Programming (GP) population seeding, thereby leveraging the broader modeling capacity of the LLM. To more thoroughly utilize search discoveries, high-quality expressions discovered by GP are fed back to update the LLM-derived policy online, thereby enabling the LLM to progressively internalize past search discoveries and translate them into improved subsequent population generation. Experiments show that on two ground-truth benchmarks, DIGEST outperforms the strongest competitor by up to 2.59% in recovery. Among LLM-based baselines, it improves recovery by at least 54.91% while using at most 17.4% of the strongest competitor's mean search time. On 122 BlackBox datasets, DIGEST achieves the highest accuracy while maintaining a moderate model complexity.

---


### 147. [When Personas Become Harmful: Guiding LLMs with Global Citizenship Values Alignment](https://arxiv.org/abs/2610.33899)

**<font color=#1a73e8>作者：</font>** Siqi Shen, Lajanugen Logeswaran, Moontae Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly being used by users from diverse demographics with pluralistic values and distinct backgrounds. Maintaining safety while respecting value-laden personas is uniquely challenging because persona-conditioned requests are often not overtly malicious, unlike those in existing safety benchmarks. Alignment methods aimed at adversarial requests therefore may miss the harm that emerges from persona use, leaving models to either refuse legitimate value expression or blindly follow unsafe personas. We construct a dataset of 11k controversial topics paired with value-based personas mapping to value dimensions from the Schwartz Value Survey. Through an agentic pipeline that iteratively refines the topic and persona, we surface and collect harmful responses from well-aligned commercial LLMs with a more than 47% success rate. We use UNESCO's global citizenship principles as a minimal common ground for distinguishing valid value expressions from harmful behaviors, and introduce a controllable alignment model that lets users balance persona adherence and safety at inference time. The resulting model is safer and more persona-adherent than baselines on most samples.

---


### 148. [Counterfactual Test-Time Augmentation for Shortcut Removal in Language Models](https://arxiv.org/abs/2610.33904)

**<font color=#1a73e8>作者：</font>** Katie Matton, Rosalind W. Picard, John Guttag 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can exploit shortcuts, i.e., correlations present in training data that may not hold at test time. This can lead to poor predictions when correlations shift. Most existing solutions for removing shortcuts operate at training time, requiring labeled training data, model weight access, and significant computational resources. Here, we study the problem of test-time shortcut removal. We propose a family of counterfactual test-time augmentation (CTTA) methods: given an example, each method uses an auxiliary model to generate counterfactual edits in which the shortcut value is changed, and then takes a weighted average of the LLM's predictions across these edits. We prove that the optimal shortcut-invariant predictor is a member of this CTTA family, and we characterize its weights. The weights depend on the training distribution, and therefore are, in general, not identifiable from the trained model and unlabeled test data. However, we present assumptions under which the weights can be obtained using the token probabilities of the trained LLM, and propose tests to detect violations of these assumptions. We use these tests to develop Select-CTTA, an aggregate method that selects among CTTA methods. Empirically, we find that Select-CTTA outperforms test-time baselines and approaches the performance of models fine-tuned on shortcut-balanced data.

---


### 149. [CVE-to-ATT&CK Mapping via Evidence-Constrained Ranking](https://arxiv.org/abs/2610.33924)

**<font color=#1a73e8>作者：</font>** Kai Wei, Yuwen Cui, Kehan Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mapping CVEs to MITRE ATT&CK techniques helps defenders translate vulnerability information into hypotheses about adversary behavior. Automating this mapping is challenging because relevant evidence is fragmented across heterogeneous security sources. In addition, ATT&CK techniques can be semantically similar, and existing annotations cover a highly long-tailed subset of the technique space. Existing supervised, retrieval-based, and LLM-based approaches therefore face limitations from closed-set supervision, semantic ambiguity, or unconstrained prediction.
We formulate CVE-to-ATT&CK mapping as multi-evidence constrained ranking. Our framework TRACE first integrates complementary structural and semantic evidence from multiple sources to construct a bounded, high-coverage candidate pool over the complete ATT&CK technique space. It then reranks the retained candidates by combining their accumulated evidence with CVE--technique textual interactions and frequency-aware scoring. We evaluate the framework across six public datasets with different annotation processes and vulnerability distributions. Candidate construction reduces the 201-technique ATT&CK search space by approximately 60% while retaining at least one ground-truth technique for 95.11%-100% of CVEs. These results show that combining heterogeneous security evidence with constrained ranking provides a more controlled and generalizable bridge from vulnerability information to adversary behavior.

---


### 150. [WebViSE: Scaling Visual Design Intelligence from the Open Web for LLM Website Generation](https://arxiv.org/abs/2610.33929)

**<font color=#1a73e8>作者：</font>** Yifei Sun, Peng Zhao, Le Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have made remarkable strides in website development, enabling complete and interactive web experiences to be built from natural-language instructions with far less effort. Yet, non-expert users often struggle to articulate sophisticated visual and interaction designs in natural language. Meanwhile, the open web already contains a vast reservoir of such design knowledge, embodied in mature website implementations. To this end, we introduce Website-derived Visual Skill Extraction (WebViSE), a framework that automatically abstracts these implementations into reusable Visual Skills and builds a structured Skill library. To scale the library, WebViSE organizes its Skills in a multi-parent DAG and jointly evolves Skill descriptions and DAG structure using Skill-conditioned Potential Queries, enabling efficient matching between diverse user instructions and relevant Skills. The auto-evolved structure outperforms non-hierarchical LLM retrieval baselines at only 39.09% of the estimated retrieval cost with Qwen3.8-Max. For any models, WebViSE can be directly injected as plug-and-play guidance, enabling diverse models to produce more visually compelling and aesthetically refined web pages. For open-source models, WebViSE can be used to build a data-synthesis pipeline that internalizes visual design intelligence into model weights. Experiments across multiple web development benchmarks and human evaluation consistently show that WebViSE improves the visual quality and interaction fidelity of artifacts. Overall, our work establishes an automated path for extracting, organizing, and transferring design intelligence from the open web to website-building models. We release all extracted Visual Skills, the associated Skill DAG, and our code at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
