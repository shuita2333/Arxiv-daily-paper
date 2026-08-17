# 🧠 大模型相关研究 | 2026年08月18日

> 本类共 **144** 篇论文：已确认 **138** 篇，待复核 **6** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-144**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-144**

---

### 101. [Multi-Objective Bayesian Optimization for Model Merging](https://arxiv.org/abs/2608.14264)

**<font color=#1a73e8>作者：</font>** Utkarsh Agarwal, Vamshi Bonagiri, Raul Astudillo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines trained models directly in weight space, offering a compute-efficient alternative to additional fine-tuning. Selecting merge parameters is nevertheless difficult because downstream evaluations are expensive, gradients are unavailable, and source capabilities can conflict. We formulate merge-parameter selection as a black-box multi-objective optimization problem and introduce MOBO-Merge, a merge-operator agnostic framework that uses multi-objective Bayesian optimization to approximate the Pareto front under a limited evaluation budget. We evaluate Qwen3-4B and Llama-3.1-8B in two-model instruction-math and three-model instruction-math-code settings using Linear, SLERP, TIES, and block-wise merge operators. On held-out benchmark partitions, MOBO-Merge obtains higher mean hypervolume than random search in 11 of 12 reported comparisons. The gain is small for one-dimensional Linear interpolation but substantially larger for several TIES, block-wise, and three-objective searches. No merge operator is uniformly best: TIES leads in three of four family-setting combinations, whereas Block-Linear 4x is strongest for the Llama three-model merge. These results show that multi-objective Bayesian optimization is valuable as a search layer for expressive merge parameterizations.

---


### 102. [TimeSage-EV: A Live Benchmark for Agentic Time Series Analysis in Evolving Environments](https://arxiv.org/abs/2608.14270)

**<font color=#1a73e8>作者：</font>** Qingren Yao, Yaxuan Kong, Yuqi Nie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series analysis in high-stakes domains relies on recurring data releases, where new observations can alter the evidence base and the validity of later conclusions. Existing time series QA benchmarks mostly rely on fixed snapshots, leaving temporal validity and cutoff-aware evidence use unevaluated. We introduce TimeSage-EV, a live benchmark for agentic time series analysis in evolving environments. It tracks 60 real institutional scenarios across 6 domains, comprising 1,485 scenario-period QA pairs from Feb 2023 to May 2026 and spanning monthly, weekly, daily, and irregular release cadences. At each period, large language model (LLM) agents receive time series data and source reports, while the withheld target release provides ground truth. TimeSage-EV evaluates state identification, data summarization, and outlook reasoning. Experiments with frontier LLM agents and TimeSage-1.0, a novel self-evolving agent with a reusable analytical skill library, reveal significant performance gaps across model tiers and recurring failures in temporal validity, exogenous context use, and adaptation. We release TimeSage-EV as a research resource with monthly updates, code, a leaderboard, and failure-mode analyses.

---


### 103. [Designing Mobile and Wearable Sensor-Fused Conversational Agents for Health and Wellbeing](https://arxiv.org/abs/2608.14273)

**<font color=#1a73e8>作者：</font>** Hansoo Lee, Pablo Fonseca, Md Haseen Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobile and wearable devices increasingly collect continuous wellbeing data, including sleep, activity, heart rate, stress, blood glucose, and blood pressure. Yet access to such data does not automatically help people interpret their condition or change behavior. Many health applications remain dashboard-first, presenting charts, thresholds, goals, and alerts while leaving users to decide what a change means and what action should follow. Conversely, generic LLM-based conversational agents (CAs) can provide fluent advice, but without personal sensor grounding, they cannot detect individualized patterns or provide contextual guidance. This three-hour tutorial teaches participants how to move from passive monitoring to actionable wellbeing dialogue. Participants examine a dashboard that combines wearable health-data visualization with conversational-agent feedback, then use Wearable Sensor-Dialogue Wellbeing Agent Studio (WSDWAS) to simulate wearables, generate sensor snapshots, configure agent personas and prompt blocks, and compare dialogue styles. Grounded in Positive Computing, the tutorial emphasizes autonomy, competence, privacy, safety, and boundaries between wellbeing support and medical advice.

---


### 104. [SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Reasoning](https://arxiv.org/abs/2608.14277)

**<font color=#1a73e8>作者：</font>** Haonan He, Haodi Lei, Yun Luo 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) offers a promising way to transfer reasoning capabilities from stronger teacher models, but applying it to long-context reasoning teachers and short-context students introduces practical challenges, including tokenizer mismatch, teacher-student distribution mismatch, response length explosion, and training instability. In this work, we study this setting by transferring proof-reasoning capabilities from the long-context reasoning model SU-01 to short-context student models. To handle tokenizer differences, we perform OPD in a shared text space and align only tokens that occupy identical text spans under the student and teacher tokenizers. To mitigate the problem of excessive generation length and frequent truncation, we introduce a student reference KL loss and mask the advantages of special termination tokens such as </think> and <|im_end|>. This strategy constrains the student from drifting excessively from its initial policy, thereby mitigating the teacher-student distribution mismatch problem and fostering steady length growth. Experiments on both same-family and different-family student models, including Qwen3, Qwen3.5, Intern-S2, GLM-4.7, Gemma-4, show consistent gains in mathematical reasoning, especially natural-language math proving. Notably, Intern-S2-Preview improves by 21.2 points on ProofBench, reaching 55.2 and surpassing Gemini-2.5-Pro. It also improves on science benchmarks such as HLE and HiPhO, suggesting that OPD transfers reasoning capabilities that generalize beyond the mathematical training domain.

---


### 105. [Seeing Red, Thinking Bad: Color Bias in Vision Language Models](https://arxiv.org/abs/2608.14286)

**<font color=#1a73e8>作者：</font>** Kohsuke Ide, Ryousuke Yamada, Yoshihiro Fukuhara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) are increasingly used in industrial decision-making systems, such as recruitment support and recommendation. This motivates careful analysis of how VLMs process visual and textual information. In this work, we study how VLMs interpret text rendered as an image, and investigate the influence of visual styling biases. To this end, we introduce Stealth Visual Prompts, which subtly change visual styling of text, such as color and contrast, while preserving semantic content. Using these prompts, we systematically control the visual styling of words in text and measure their impact on the analysis performed by VLMs. We further analyze how such visual perturbations affect the latent representations of the vision encoder. From our experiments, we observed that coloring positive words in green consistently shifts sentiment predictions toward a positive direction. As a result, VLMs often fail to properly account for negative words present in the text. Our analysis suggests that this behavior is correlated with changes in the latent representations of the vision encoder induced by color variations. In addition, we show that reducing text--background contrast increases reliance on visually salient cues and leads to more incorrect Visual Question Answering (VQA) outputs. These results suggest that the visual styling of rendered text can guide VLMs' interpretation in ways that diverge from human semantic understanding.
Project page: this https URL

---


### 106. [Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning](https://arxiv.org/abs/2608.14290)

**<font color=#1a73e8>作者：</font>** Kai Chen, Jifeng Ding, Ning Ding 等 47 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Mobius-v0, an architecture that comprises a globally shared Memory (FFN) that stores knowledge vectors and multiple Reasoners (Self-Attn) that iteratively achieve compositional reasoning. Using hidden states as cache and carrier, reasoners repeatedly query memory for required knowledge-vectors, while the knowledge is transmitted back to reasoning operators. Through this knowledge-reasoning-separation architecture, Mobius achieves better knowledge compression and reasoning efficiency. Built upon Mobius-v0 architecture: 1) Our 7B model trained-from-scratch achieves similar downstream score as a 7B Transformer baseline with 62.6% of baseline's training data. 2) Our Intern-S2-Mobius, continually-pretrained from Qwen3.5-35B, achieves similar downstream score while delivering nearly 4x end-to-end inference speedup.

---


### 107. [Detecting Contaminated Code-Generation Prompt Batches via Influence Functions](https://arxiv.org/abs/2608.14303)

**<font color=#1a73e8>作者：</font>** Francesco Quinzan, Noor Munir, Yishun Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for code generation, yet they remain vulnerable to prompts that elicit insecure implementations. Existing defenses typically rely on predefined threat models or known vulnerability patterns, limiting their effectiveness against novel attacks. We propose CodeSIFT, a threat-model-agnostic detection method that leverages influence functions to identify batches of prompts that induce anomalous model behavior. Rather than detecting specific vulnerabilities, CodeSIFT measures the parameter-space influence of generated code and uses a statistical test to determine whether a candidate prompt set deviates from a benign reference distribution. To evaluate our approach, we introduce two benchmark datasets covering a variety of vulnerabilities. We evaluate CodeSIFT on three open-weight code LLMs ranging from 3B to 7B parameters, achieving AUROC scores of up to 0.98 at moderate-to-high injection rates, while maintaining well-calibrated false positive rates and substantially outperforming static analysis baselines. These results suggest that influence-function-based detection is a promising direction for identifying malicious code-generation prompts without requiring prior knowledge of the underlying attack class.

---


### 108. [Spatial Message Passing in Language Space for Pathology Image Interpretation](https://arxiv.org/abs/2608.14309)

**<font color=#1a73e8>作者：</font>** Jing-Cheng Yang, Hao-Jung Wang, Jinhao Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) can generate pathological descriptions from histological images, but gigapixel Whole Slide Images (WSIs) exceed their visual context limits. The standard tiling workaround makes WSIs tractable yet severs the tissue neighborhoods that define tumor-stroma interfaces and morphology. We introduce Spatial Language Message Passing (SLMP), a framework that performs spatial reasoning entirely in language space, human-readable by construction. SLMP represents a WSI region as a spatial text graph: tiles are nodes initialized with MLLM descriptions, and edges encode spatial adjacency. For each tile, an LLM refines its description by integrating language messages from adjacent tiles under a shared aggregation policy that, on the tile grid, acts as an adaptive local kernel operating on text rather than learned embeddings. This policy is an inspectable prompt that can be refined from model-observed tissue phenotypes via textual gradients, enabling automatic semantic optimization from local cellular context to broader tissue morphology without fine-tuning MLLM weights. On representative HER2 and CAMELYON16 regions, SLMP improves tile-level tumor description accuracy in settings spanning general-purpose and pathology-specialized backbones, with gains of +3.3 to +19.6 percentage points. Random-neighbor ablations confirm that these gains stem from spatial context rather than additional text alone, and inspecting the optimized policies reveals interpretable, tissue-specific decision rules. Besides, without any weight updates or fine-tuning the backbone MLLM, SLMP substantially improves general-purpose MLLMs and narrows its gap to pathology-specialized counterparts, offering a transparent and flexible mechanism for incorporating spatial reasoning into MLLM-based pathology analysis.

---


### 109. [Envs-FORGE: Frontier-Optimized Reward-Grounded Environment Synthesis for Agent RL](https://arxiv.org/abs/2608.14312)

**<font color=#1a73e8>作者：</font>** Xiaojun Wu, Cehao Yang, Honghao Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for terminal agents needs executable training environments with reliable rewards and useful difficulty. Fixed recipes such as few-shot, Self-Instruct, and Evol-Instruct apply the same prompting policy to every seed, even when the current policy would benefit from a harder, easier, or simply different task. We present Envs-FORGE, a prompting policy that converts verifier rewards into per-seed environment-synthesis actions. Envs-FORGE estimates seed pass rates, scores six projection--direction actions around a target learning frontier, and solves a per-seed mixed-integer linear program (MILP) to choose the action that conditions generation. The selected action drives synchronized rewriting of the instruction, fixtures, oracle solution, tests, and Docker environment; only gold-verified bundles enter RL training. The indexed MILP form also supports optional soft skill coverage for portfolio planning. On Qwen 3.5 35B, Envs-FORGE improves Pass@1 over Base by 9.2 percentage points on tb-core (40.0% to 49.2%) and 6.4 points on tb-2.0 (23.0% to 29.4%), exceeding the strongest fixed-recipe baseline by 2.4 and 2.1 points. It reaches 77.1% on SWE-bench Verified versus 73.4% for Base, and improves tb-core by 6.8--9.2 points across the evaluated 4B--35B models. All synthesis methods export 100 verified environments and use 2.27M--2.88M synthesis tokens, placing the comparison at the same downstream training-set size and the same operational scale. The source code is available at this https URL.

---


### 110. [AnchorBench: A Multi-Pathway Benchmark for the Anchoring Effect in LLMs](https://arxiv.org/abs/2608.14320)

**<font color=#1a73e8>作者：</font>** Yiderigun Borjigin, Alexander Hermann, Christian Cyron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The anchoring effect is a cognitive bias in which an initial reference value shifts a later judgment toward itself. This effect is well established in human judgment and decision-making, and recent work suggests that large language models (LLMs) exhibit similar behavior. However, existing work on anchoring in LLMs typically evaluates only a narrow set of anchor pathways and rarely distinguishes irrelevant from plausible anchors. We introduce AnchorBench, a benchmark for the anchoring effect in LLMs that evaluates multiple anchor pathways under an explicit anchor relevance axis. Across fourteen models, including ten open-weight models and four frontier API models, and a large set of controlled prompts, we find that (1) anchoring is strongly pathway-dependent, (2) plausible anchors usually induce larger shifts than irrelevant ones when introduced through stronger pathways, (3) anchor influence generally weakens as the anchor moves farther from the evidence-supported answer, most clearly on External and RAG, and (4) high task accuracy on the anchor-free control condition (Acc$_{10}$: answers within 10 points of gold) does not guarantee robustness: even frontier API models above 95% control accuracy remain susceptible to plausible anchors.

---


### 111. [A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation](https://arxiv.org/abs/2608.14329)

**<font color=#1a73e8>作者：</font>** Dipankar Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Principle-based regulation, with evaluative standards such as "fair, clear, and not misleading" or "deliver good outcomes", cannot be reduced to binary predicates, and LLM-as-judge is increasingly used as the substitute. Our position is that any such judge must be evaluated on four axes: accuracy, paraphrase robustness, adversarial robustness, and calibration. We release Principle-Bench, 168 cryptoasset financial-promotion scenarios mapped to two UK FCA principles, with paraphrase, adversarial keyword-stuffing, and boundary perturbations authored under a pre-registered rubric; the first benchmark covering all four axes for principle-based regulation. We also introduce Ceca (Calibrated Exemplar-Cluster Assessment): a calibrated, auditable assessor that emits exact per-exemplar counterfactual attributions. Across keyword counting, three sentence-transformer embedders, an open-weight LLM-judge, and a calibrated cascade, no method dominates all four axes. A 120B LLM-judge, strongest on benign inputs, loses 47 accuracy points (0.74 to 0.27) on keyword-stuffed Consumer Duty inputs: "compliance theatre." A second judge from a different model family agrees only at Cohen's kappa = 0.16 on that split, localising the failure to the model rather than the corpus. Any deployment-grade LLM-judge for principle-based regulation must report per-principle adversarial deception and post-hoc calibration alongside aggregate accuracy.

---


### 112. [Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents](https://arxiv.org/abs/2608.14339)

**<font color=#1a73e8>作者：</font>** Zhizhao Guan, Chen Huang, Ziming Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study proactive exploration in LLM agents, i.e., the ability to explore an environment to acquire information that improves future decision-making. In this regard, we first identify two fundamental bottlenecks that hinder this capability and then propose \ours, a novel method designed to instill and refine proactive exploration. Specifically, \ours\ consists of two components: (1) Exploratory Data Construction, which synthesizes exploration-rich trajectories to mitigate the hindsight bias of standard demonstrations; and (2) RL Optimization with Contrastive Signal Guidance, which leverages contrastive trajectory pairs to distinguish productive exploration from redundant wandering. Extensive experiments demonstrate the effectiveness of \ours\ and provide insights into the characteristics of proactive exploration. Our code is available at: this https URL.

---


### 113. [ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond](https://arxiv.org/abs/2608.14354)

**<font color=#1a73e8>作者：</font>** Mingming Zhao, Jiqian Dong, Kangping Xu 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enabling LLM agents to sustain productive, stable, and goal-aligned research over extended horizons is a central challenge for autonomous machine learning and scientific discovery, as progress hinges on continuously managing evolving state, exploration decisions, and computational resources. Pioneering autoresearch agents, despite great success, still lack mechanisms for continuity, recovery from dead ends, and value-driven compute allocation, which inherently undermines overall search efficiency, wastes computational resources, and lowers the chance of ultimate success. To bridge this gap, we introduce ScienceFlow, an end-to-end autoresearch agent framework that organizes long-horizon research work into research segments grounded in executable workspaces. It represents research progress as recoverable executable states, enabling efficient exploration, revision, and execution. Transitions between research segments are governed by Executable-State Transition through Re-Anchoring (ESTRA), which selects either the live state or an archived state as the next anchor and determines whether to continue or redirect the research trajectory. An evidence-aware execution controller allocates resources to physical jobs based on resource availability, remaining budget, and validated progress. We evaluate ScienceFlow on tasks spanning machine learning, scientific modeling, and mathematical optimization. Results on diverse long-horizon benchmarks demonstrate its ability to sustain effective research processes, highlighted by a SOTA 70.22 percent Any-Medal score on the full MLE-bench within a 24-hour budget, outperforming prior reported results by 4.92 percentage points. The efficacy of ScienceFlow further demonstrates that efficient state management, adaptive exploration, and objective-aligned execution are critical for scaling autonomous research beyond short-horizon interactions.

---


### 114. [Local and Global Regimes of Geometric Complexity in Language Model Representations](https://arxiv.org/abs/2608.14361)

**<font color=#1a73e8>作者：</font>** Arwa Osman, Marco Baroni, Iuri Macocco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Intrinsic dimensionality (ID) is widely used to probe the representational complexity of language models, but it remains unclear whether ID differences reflect properties of language itself or artefacts of how the underlying dataset was constructed. In this paper, we focus specifically on how lexical diversity, the number of unique last-token items present in a dataset, affects ID estimates of that dataset. We find a scale-dependent transition between two regimes: at low lexical diversity, conditions with fewer unique final words produce higher ID, while at high lexical diversity, this ordering reverses, and conditions with more unique words produce higher ID. We derive an exact, parameter-free formula for the point at which this reversal occurs, which matches the observed transition point at every scale tested. On the one hand, our results highlight how care must be taken when interpreting the intrinsic dimensionality of a set of representations as a straightforward cue of their complexity. On the other hand, our discovery of the two ID regimes reveals a general principle of organisation of linguistic data in LLMs that sheds new light on their inner manifold structures.

---


### 115. [A Hybrid LLM-Based Framework for Automated Security Annotation Generation in Business Process Models](https://arxiv.org/abs/2608.14370)

**<font color=#1a73e8>作者：</font>** Md Kamrul Islam, Tiphaine Henry, Mattia Salnitri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The modelling and analysis of secure business processes require the incorporation of security annotations into process models. Although BPMN extensions, including SecBPMN2, exist for this purpose, the derivation of accurate and complete security annotations from natural-language specifications remains a manual, expert-intensive, and error-prone task. This paper presents a hybrid framework that takes a BPMN process model and a security requirements document as input and automatically generates security annotations adhering to the SecBPMN2 specification. The approach combines Large Language Model (LLM)--based semantic extraction with schema-constrained mapping, rule-based normalization, and deterministic validation. The framework is evaluated comprehensively on a curated dataset of 27 process models from various domains. The results indicate that it consistently produces structurally valid SecBPMN2 annotations with high schema completeness. Compared to human security analysts, the system achieves substantially higher precision (0.58 vs. 0.29) while maintaining comparable recall (0.52 vs. 0.50) and reduces erroneous or misplaced annotations by nearly 50%. In addition, annotation generation is significantly faster than manual annotation. These findings demonstrate that hybrid LLM- and rule-based automation can reduce modeling effort while improving consistency and reliability, thereby providing a scalable foundation for security-by-design BPM.

---


### 116. [Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages](https://arxiv.org/abs/2608.14375)

**<font color=#1a73e8>作者：</font>** Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Cheng-Hau Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent reasoning systems often use agreement, confidence, or automated scores to decide which messages should shape a final answer. Such filtering assumes that a message likely to be correct is also worth keeping. Yet a wrong answer can contain a useful decomposition, constraint, or scientific principle. We test this distinction with Diverse Hypothesis Deliberation (DHD), a controlled measurement protocol that caches five independently generated messages and replays the same downstream solver, called the integrator, with each message available or hidden. The replay comparison measures a message's trajectory value: whether making the message available helps or harms subsequent reasoning. Across five mathematics and science benchmarks and two openly available model families, gpt-oss-120b and gemma-4-31B-it, wrong-helpful messages appear in every benchmark-model combination. Among wrong-answer messages that change final correctness, more than four in ten changes are helpful in each model. Controlled repeats show that the number of repeatable message effects is unlikely to arise from replay variation alone (p=0.0002). A focused intervention on repeatable wrong-helpful messages finds that the complete message works best, while retaining its reasoning preserves more success than retaining only its answer; the source of the complete-message advantage remains open. Within the same problem, repeated trajectory-value evidence also identifies a better keep-or-remove choice than answer correctness alone. Answer correctness is therefore informative but does not determine trajectory value. DHD measures this missing property and produces reusable labels for learning when agents should listen.

---


### 117. [A Survey of Large Models in Sports](https://arxiv.org/abs/2608.14377)

**<font color=#1a73e8>作者：</font>** Yichen Xu, Jianzhe Ma, Chuhan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sports have witnessed growing global enthusiasm in recent years, serving as a vital force for physical health, cultural exchange, social connection, and economic growth. The rapid advancement of large models, particularly (multimodal) large language models (M)LLMs, has demonstrated transformative potential to reshape sports understanding, analysis, and interaction across diverse domains. This paper presents a comprehensive survey of large models in sports, including (i) an overview of tasks and applications across different participant groups; (ii) a detailed analysis of sports-related datasets and benchmarks; and (iii) a critical discussion of current challenges and future directions. Our goal is to establish a foundation for advancing research and practical development of large-model-driven sports intelligence. An open-source GitHub repository is maintained at: this https URL.

---


### 118. [AgentRewind: Recoverable Execution for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.14380)

**<font color=#1a73e8>作者：</font>** Yu Zhuang, Kefei Chen, Yitong Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many real-world tasks require LLM agents to interact with their environments over long execution horizons. Errors that occur early in execution may propagate through both the agent context and environment state, and their effects may be difficult to reverse through subsequent actions. Existing methods mainly seek to reduce such errors through plan refinement and safety checks but provide little support after errors occur. To enable recovery during long-horizon execution, we present AgentRewind, a runtime recovery framework that records aligned checkpoints of the agent context and controlled environment, allowing agents to return to an earlier state and resume execution with information from previous attempts. We also construct MettleBench, a benchmark for evaluating task completion and partial progress on long-horizon engineering assignments containing a series of related requirements. Experiments across tasks, multiple models, execution strategies, and agent harnesses show that AgentRewind improves task success rate and average checklist progress over the compared baselines.

---


### 119. [DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding](https://arxiv.org/abs/2608.14385)

**<font color=#1a73e8>作者：</font>** Zewen Jin, Shen Fu, Zeping Duan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models have been widely adopted in real-time interactive applications such as coding assistants, real-time audio-video interaction systems. To meet the extremely low response latency requirements of these scenarios, practitioners commonly employ small-batch decoding, under which MoE inference becomes memory-bound and is severely bottlenecked by expert weight loading. However, this bottleneck has received limited attention, and existing solutions such as post-training weight compression or fine-grained expert design during pre-training either degrade model accuracy or introduce additional computation and communication overhead. To tackle this issue, we propose DeaMoE, a decoding-efficient MoE architecture, in which the experts are grouped into several departments, and the experts belonging to the same department share most parameters since they come from the same professional field, and additionally each expert contains a few private parameters to reflect its uniqueness. Moreover, we design customized two-stage routing strategy for DeaMoE to avoid redundant loading, under which DeaMoE greatly improves the efficiency during LLM decoding. Compared with vanilla MoE, DeaMoE reduces per-step loaded weights by up to 50.9% and achieves up to 1.33 end-to-end TPOT speedup for the pre-trained 7B model on A40, and up to 2.00x and 1.97x peak speedup for DeepSeek-V3 on A40 and H100 in microbenchmarks.

---


### 120. [Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A Systematic Evaluation of Detectors, Generators and Social Dissemination](https://arxiv.org/abs/2608.14391)

**<font color=#1a73e8>作者：</font>** Shuo Liang, Yixing Ma, Pengfei Zhou 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generators can fabricate realistic depictions of wars, disasters, public emergencies, and other real-world crises, creating substantial risks of misinformation. Existing benchmarks, however, provide limited evidence on detector and generator behavior in such settings, including how detectability varies with generation conditions, how people perceive generated videos, and whether detectors remain reliable during social dissemination. To address this gap, we introduce RA-Bench, a benchmark for AI-generated video detection that uses Real videos as Anchors. RA-Bench contains 17,886 videos, comprising 1,830 real-video anchors across 10 social-risk categories and 16,056 generated clips from four open-source and five closed-source generators. Based on RA-Bench, we organize our evaluation along three dimensions. We first assess detector generalization across seven traditional detectors, ten zero-shot multimodal models under three review settings, and two MLLMs specifically fine-tuned on AI-generated video detection. Across these methods, none of the three detector families generalizes consistently across RA-Bench instances. We then examine how detectability varies with generation quality, conditioning information, and sampling seeds. These analyses show that generation properties affect detector families differently, while source-level detection patterns remain stable across seeds. Finally, we study human authenticity judgments and detector reliability during social dissemination. We find that videos that mislead people are also difficult for current detectors, and that social dissemination makes detection harder. Together, these findings show that current methods struggle to detect realistic AI-generated videos, highlighting the need for detectors robust to evolving video generators.

---


### 121. [Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons](https://arxiv.org/abs/2608.14392)

**<font color=#1a73e8>作者：</font>** Wei Zhao, Zhe Li, Peixin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neuron- and path-level interventions offer the finest-grained route to defending large language models (LLMs) against jailbreak attacks, yet existing methods fall short of this promise, i.e., they often compromise model utility significantly. Specifically, one line of work suppresses toxic neurons to erase harmful semantics, but since such semantics are distributed across the network, blocking every pathway forces a large intervention footprint. An alternative line of research focus on identify safety neurons using external classifiers. While promising, the existing approaches suffer from compromising neurons that are important for the model utility as well. Moreover, both approaches remain always on and thus perturb every benign request even when no attack is present. To address these limitations, we present \ours{}, a training-free defense that first identifies safety-specific neurons through per-neuron hypothesis tests under false-discovery-rate control together with a utility-specificity filter. Based on this identification, a trigger-style clamp holds the selected neurons at their harmful-conditional mean activations, injecting an internal harmful-input signal that triggers the refusal behavior learned during alignment. The clamp is then realized by two provably equivalent deployment modes, namely a detector-gated inference-time intervention and an offline bias-patch weight edit. Extensive experiments across four safety-aligned LLMs and four representative attacks demonstrate that \ours{} reduces the average attack success rate to at most 2.0\% while incurring a utility drop of only 0.5\% to 5.3\% on MT-Bench, the smallest among all defenses. Code is available at this https URL.

---


### 122. [LLMs Don't Pay for the Jump](https://arxiv.org/abs/2608.14397)

**<font color=#1a73e8>作者：</font>** Paras Balani, Subhrakanta Panda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Zahavy [2026] argues that Large Language Models, despite their capabilities in induction and deduction, cannot perform the abductive "Jump" that produced Einstein's equivalence principle, and attributes this limitation to the absence of embodied simulation. Zheng-Xin [2026] and Farmer [2026] question whether embodiment is necessary for abduction, pointing to alternative routes to General Relativity and forms of abduction that require no sensorimotor grounding. Max Planck resolved the blackbody radiation problem in 1900. Planck's move to E = h{\nu} required no embodied simulation. It was motivated by a mathematical consequence of classical theory, an infinite predicted energy for a finite measured quantity, that could not be physically accepted. We show that neither induction nor deduction could have produced the postulate and argue that its adoption required a coupling between epistemic error and physical cost. We formalize this distinction through thermodynamic coupling and show that fixed-weight transformer inference lacks such coupling, regardless of model scale. This is consistent with empirical results showing that output entropy remains nearly unchanged across tasks with sharply increasing causal difficulty, even as accuracy falls from 100% to 17%. We therefore argue that the missing ingredient in machine abduction may lie deeper than embodiment: a system must have some physical mechanism through which epistemic error becomes costly enough to force revision.

---


### 123. [CRAFT: Constrained Reward via Attention Fine-Tuning for Subject Personalization without Composed Targets](https://arxiv.org/abs/2608.14403)

**<font color=#1a73e8>作者：</font>** Jihun Park, Kyoungmin Lee, Jongmin Gim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject-driven image personalization---generating new images that preserve the identity of one or several reference subjects in novel scenes---is a foundational capability for modern visual content creation. It is currently dominated by generalized methods that fine-tune a pretrained multimodal diffusion transformer (MMDiT) on hundreds of thousands to millions of paired \emph{(reference, composed-target)} examples, where each composed target is a synthesized image of the subject in a novel scene. Producing such targets demands a costly multi-stage curation pipeline---LLM-based prompt generation, T2I-based composed-target synthesis, reference-subject extraction, VLM-based quality filtering, and correspondence labeling---and tightly couples each method to a particular target synthesizer and curation choice. We introduce \emph{CRAFT} (Constrained Reward via Attention Fine-Tuning), a single-step ReFL framework that fine-tunes a pre-trained \emph{reference-aware} MMDiT via LoRA adapters using a compact reference-only data construction---$10$K reference images and subject masks, with no composed-target supervision. CRAFT realizes a \emph{Where to look} principle: attention-level rewards align noise- and phrase-token attention with the correct reference subject, and the resulting per-subject attention masks gate a pixel-level identity reward to keep image-space supervision consistent with the learned attention routing. Applied to FLUX.2-klein-9B, CRAFT achieves state-of-the-art performance on XVerseBench \rev{while using no composed-target supervision---only $10$K reference-only samples, whereas prior generalized methods require $150$K to over $2$M composed-target pairs}. The same recipe transfers to other reference-aware backbones, consistently improving performance. Project page: this https URL.

---


### 124. [From Style Replication to Style Exploration: Enabling Art Style Exploration with Analyze-Experiment-Resituate Framework](https://arxiv.org/abs/2608.14405)

**<font color=#1a73e8>作者：</font>** Wen-Fan Wang, TsaiHsuan Lin, Chi-Lan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Art style is a signature of professional digital artists that develops through repeated experimentation, reflection, and adaptation. While generative AI (GenAI) can reproduce styles with high fidelity, current tools provide limited support for exploring new stylistic directions and may encourage style replication over exploration. To address this gap, we propose Analyze-Experiment-Resituate (AER), a framework for AI-assisted style exploration derived from interviews with 10 professional digital artists. Rather than prioritizing visually appealing outputs alone, AER supports three core practices of style exploration, including interpreting references, trying out stylistic possibilities, and reflecting on how emerging styles may be received. Specifically, AER enabled artists to (1) analyze artworks into interpretable stylistic elements, (2) have controllable experimentation guided by their own choices, and (3) resituate emerging styles through simulated social perspectives. We implemented AER in a prototype system and evaluated it in a controlled study with 16 artists. Compared with a direct style-transfer workflow, AER increased artists' agency and reflection as they pursued new stylistic directions. A two-week field study with four artists revealed how the AER framework influenced daily style exploration, such as reflection, experimentation, and stylistic decision-making at each stage. We discuss opportunities and challenges in designing AI-assisted style-exploration workflows, and outline implications for future artistic support tools.

---


### 125. [STINER: Automated Extraction of Strategic Cyber Threat Intelligence from X](https://arxiv.org/abs/2608.14418)

**<font color=#1a73e8>作者：</font>** Yasir Ech-Chammakhy, Oussama Azrara, Jaafar Chbili 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Strategic Cyber Threat Intelligence (CTI) focuses on high-level insights, such as identifying targeted industries, attributing attacks to specific ransomware groups, and assessing the scale of data loss. Today, X (formerly Twitter) has become the fastest source for this intelligence, often hosting real-time breach announcements days before formal vendor reports. Converting this raw chatter into actionable intelligence requires navigating a complex linguistic landscape. Conventional Named Entity Recognition (NER) models struggle to parse the informal and highly irregular dialect of social media, creating a blind spot for automated defense systems. To address this challenge, we introduce STINER, a taxonomy and expert-annotated corpus for extracting strategic intelligence from social media streams. We construct a high-quality, expert-annotated dataset of 2,100 real-world alerts and propose a granular taxonomy of eight entity types centered on strategic pivots such as Threat Actor, Sector, and Location. We benchmark nine models across 12 evaluated configurations, spanning general-purpose and domain-adapted encoders, open-schema extraction, and generative LLMs in both zero-shot and fine-tuned settings. Domain-adapted encoders such as DarkBERT reach a strict F1-score of 89.33%, outperforming both general-purpose baselines and fine-tuned Large Language Models, which additionally incur substantially higher inference latency. Leveraging STINER-DarkBERT, we conduct a European threat landscape analysis for H1 2025. Our results align with official reporting on major targets while highlighting the distinct visibility profile of attacks in Spain, and illustrate how social-media-driven extraction can surface early signals of the SafePay ransomware campaign prior to its retrospective characterization in vendor threat landscape reports.

---


### 126. [More Correct Mass, Worse Answers: Why Power Sampling Can Fail and How to Fix It](https://arxiv.org/abs/2608.14420)

**<font color=#1a73e8>作者：</font>** Haohui Yang, Jiaxing Sun, Xiujun Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power Sampling sharpens a language model's distribution over complete generation trajectories, offering a verifier-free way to improve reasoning at inference time. It also has the potential to serve as a general-purpose front end for a broad range of downstream sampling methods. However, we uncover a striking paradox: Power Sampling can drive more probability mass toward correct trajectories while degrading the downstream inference it is intended to enhance. Using self-consistency as a representative case, we observe accuracy drops of up to 18.5 percentage points across models and reasoning benchmarks. We trace this paradox to two mismatches. Dose mismatch arises because a fixed exponent induces drastically different amounts of distributional change across problems. Coverage mismatch arises because global sharpening concentrates mass on a narrow set of dominant paths: high pass@k, often interpreted as evidence of preserved diversity, can therefore coexist with the loss of broad reasoning-path support required for downstream aggregation, search, and selection. Guided by this diagnosis, we replace uniform trajectory exponentiation with a deformation-controlled, support-preserving Power target that calibrates sharpening across problems while limiting the suppression of moderate-probability paths. In a same-budget instantiation with weighted self-consistency, the repaired sampler reverses the losses caused by global Power and outperforms standard multi-sample inference across reasoning benchmarks.

---


### 127. [Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations](https://arxiv.org/abs/2608.14425)

**<font color=#1a73e8>作者：</font>** Toby D. Pilditch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM evaluations often use fixed sampling budgets, testing every item the same number of times even after estimates are precise. We introduce optstop, a precision-based adaptive stopping framework that treats evaluation as a sequential measurement problem: keep sampling where uncertainty remains high, and stop where estimates are precise or stable enough. The framework builds on hierarchical Bayesian inference, supports binary, ordinal, and continuous outcomes, and keeps every benchmark item eligible for sampling, without requiring a calibrated item bank. It runs live or retrospectively, and includes a safeguard that samples more cautiously as measured performance approaches zero, where rare successes matter most. In an illustrative 200-item, 10-epoch evaluation, it removes 57%-97% of planned trials across nine validation settings, with overall conclusions equivalent to the full run. These results show that LLM evaluation compute can be allocated by uncertainty rather than by fixed repetition counts, with the magnitude of savings depending on evaluation design.

---


### 128. [Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View](https://arxiv.org/abs/2608.14430)

**<font color=#1a73e8>作者：</font>** Yixian Xu, Yuanrui Zhang, Shengjie Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training provides a direct way to align diffusion models with human preferences and task-specific rewards. However, current RL algorithms for diffusion models remain fragmented: reverse-trajectory methods rely on discretized likelihood ratios, whereas forward-matching methods train on reward-labeled noising versions of the rollout samples. This paper shows that these seemingly different losses arise from a single path-space principle. Starting from the regularized diffusion-RL objective, we use importance sampling between sampling SDEs to obtain an explicit policy-gradient estimator on trajectory space. The estimator contains the stochastic Itô integral underlying Flow-GRPO-type updates; we derive an equivalent variance-reduced value-gradient form that recovers the forward-matching structure of AWM and DiffusionNFT. This identifies the empirical gap between these method families as a variance-reduction effect rather than a difference in RL principle. The derivation yields a unified design space organized by value-gradient estimation, weight functions, and sampling choices. Within this space, we propose a multi-sample KDE value-gradient estimator that reuses rollout groups, together with scale-bounded weight families that retain stable existing recipes while excluding singular ones. Experiments on SD3.5-M and Qwen-Image models validate the variance-reduction explanation and show that the resulting recipe improves over prior diffusion-RL baselines.

---


### 129. [PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments](https://arxiv.org/abs/2608.14441)

**<font color=#1a73e8>作者：</font>** Yuhao Zhan, Bingxiang He, Zecong Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents improve future behavior from interaction experience, yet existing evaluations typically optimize under fixed execution conditions and do not test recovery after those conditions change. To address this gap, we introduce PACE-Bench (Physics Adaptation via Code Evolution), a simulator-grounded benchmark of 144 source-to-target adaptation pairs across six physics domains. Each pair links a source environment to a mutated target environment with the same goal and interface. A code-driven design that succeeds in the source fails in the target, where agents must iteratively adapt it into a working target design using diagnostic sandbox feedback within a limited attempt budget. We compare ten self-evolving methods from four paradigms. The benchmark remains far from saturated: Reflexion + Qwen3-14B succeeds on only 35.9\% of full-benchmark pairs, while GPT-5.5 solves 66.7\% of the Statics subset under the full budget. Together, these results show that simulator-grounded reflection is more reliable than unverified self-revision, while memory anchors agents to early designs and broad tree search explores without converging. Even revealing exact physical changes does not raise the performance ceiling, pointing to mechanism redesign rather than parameter inference as the central bottleneck. Data and code are available at this https URL.

---


### 130. [SheetCompass: Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning](https://arxiv.org/abs/2608.14452)

**<font color=#1a73e8>作者：</font>** Panjing He, Mingyue Cheng, Yucong Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spreadsheets are widely used to organize, analyze, and manipulate semi-structured data, yet automated spreadsheet reasoning remains challenging for large language models (LLMs). Real-world workbooks often contain implicit cross-table associations, fine-grained column dependencies, and complex spatial layouts. Existing methods typically flatten these multidimensional structures into sequential strings, losing important intra-sheet boundaries and inter-sheet semantics. Consequently, LLMs cannot exploit the global spatial context that human experts naturally use when inspecting spreadsheets. We propose SheetCompass, a graph-guided and memory-driven agentic framework for spreadsheet reasoning and automation. SheetCompass explicitly models structural relationships within and across worksheets while maintaining task-relevant information in memory, enabling agents to reason more effectively over complex workbooks.

---


### 131. [Information Satisfaction: A Reader-Centered Axis for Summarization Evaluation](https://arxiv.org/abs/2608.14457)

**<font color=#1a73e8>作者：</font>** Isabel Cachola, William Walden, Reno Kriz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The majority of work on summarization evaluation focuses on general summary quality (e.g., ROUGE, BERTScore) or specific desired properties (e.g., readability, factuality). However, these metrics fail to measure the utility of a summary to an individual user. For example, a biomedical researcher learning about the latest vaccine research will have different informational needs from a family doctor. Query-focused summarization captures part of this need, but in practice, users rarely state everything relevant in a query: a single short query is likely inadequate to distinguish the needs of a researcher from those of a physician. By contrast, a reader's background or persona (their role and expertise) is comparatively stable across queries and recovers much of this missing context, which makes it a practical signal for assessing whether a summary satisfies that reader's needs. In this work, we assess how sensitive popular summarization metrics are to both informational and persona differences, and find that many popular metrics, including strong LLM-as-judge metrics, fail basic perturbation tests of informational content. We additionally conduct an expert human evaluation, measuring summary preferences based on information satisfaction given a specific person's background and use case. We find that both traditional and LLM-based metrics are insufficient measures of information satisfaction and agree poorly with human judgment.

---


### 132. [You Only Pass Once: Answering and Abstaining Together in a Single Forward Pass of a Frozen Language Model](https://arxiv.org/abs/2608.14465)

**<font color=#1a73e8>作者：</font>** Ziyang Luo, Zhongyao Chu, Xinjie He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A frozen language model on reasoning tasks has two coupled weaknesses: it under-uses evidence its own residual stream already encodes, and it fails to detect when the input is insufficient to answer, so it confabulates. This paper consolidates two research lines that address these on the same residual stream: a conditional steering probe writes the stream at mid-stack layers and recovers reasoning accuracy from a frozen backbone, and a zero-shot sufficiency direction reads the stream and abstains when information is insufficient. Deployed in one forward pass they interfere: the steering write shifts the state the direction reads, costing up to 8 AUROC points of cross-domain transfer on small models; a separate clean pass doubles inference cost. We keep the direction fixed and train a small network to reconstruct the pre-steering residual from the steered one -- mean-squared error on (steered, clean) pairs, no sufficiency labels -- and read the direction on the reconstruction. The resulting system, YOPO (You Only Pass Once), answers, steers, and abstains in one forward pass of a frozen Qwen2.5 backbone (1.5B/3B/7B). End to end, three-way accuracy more than doubles the frozen baseline (0.375->0.798 on 1.5B alphaNLI) and one pass beats the two-pass reference at every scale (0.798/0.830/0.893 vs 0.753/0.790/0.863) and on ten backbones across six model families. We chart the capacity-transfer frontier quantifying the principle that abstention should not be trained in; a source-side audit catches our own alphaNLI construction leaking a surface artifact, so architectural claims are anchored on native-label replications (SQuAD2, RepLiQA, MuSiQue); and on the standard four-domain suite we contribute, to our knowledge, the first answer-or-abstain benchmark, where our gate tops every in-domain dataset and the label-free direction is the only gate family to survive domain transfer.

---


### 133. [Twin: Playing an Unknown Game with a Test-Time Digital Twin](https://arxiv.org/abs/2608.14490)

**<font color=#1a73e8>作者：</font>** Alexy Skoutnev, Kirill Acharya, Gaston Longhitano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a Test-time World-model Inference (Twin) system, in which a frontier coding agent writes an executable world model for completing continual learning tasks, such as ARC-AGI-3 games. Traditional approaches hand-engineer such models, one custom design per task. Each game hides its rules and goal, and our system constructs them from simulation and interaction alone. Its inductive prior over grid games is strong enough to recover the true transitions of the game and the goal on nearly all levels. Replay validation happens in a twin world model. The harness enforces that an action is not made until the program reproduces every previous observed game transition. Each mismatch between a world model prediction and the actual action result becomes a counterexample that is used to repair the world model. Twin clears 179 out of 183 levels (97.8%), and does so more efficiently than humans in 158 out of 179 levels (88.3%). The system infers the goal before any reward on 156 of the levels it clears (87.2%), and in the remaining levels automatically discovers the goal by search. The benchmark scores completion and action efficiency, between 0 and 100, against humans playing each game for the first time. Played directly, the base model scores only 7.8%; an off-the-shelf harness increases it to 61.1%, whereas our twin world model increases the same base model to 93.3%, clearing 23 out of 25 games. Building a usable world model is simpler than anticipated, whereas the harder problem is inferring the right goal.

---


### 134. [Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training](https://arxiv.org/abs/2608.14498)

**<font color=#1a73e8>作者：</font>** Hanfeng Lu, Tianyu Feng, Suyi Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) enable embodied agents to reason and act from visual observations and language instructions. Reinforcement learning (RL) post-training enhances these capabilities using task feedback, but current on-policy RL runtimes execute rollout, reference scoring, and actor training in strict serial phases. While effective for text-only RL, this phase-granular execution is wasteful for VLMs, where processing dense video inputs and prompt prefixes occupies a large fraction of each phase. Because prefix processing is independent of the generated response, it can be run alongside rollout decoding, which leaves GPU compute capacity underutilized, without breaking synchronous on-policy semantics.
We present Rollplex, a runtime that decomposes the reference and training phase and moves the prefix computation into the rollout decode window. Realizing this schedule requires more than concurrent kernel launches: naive colocation of Qwen2.5-VL-32\,B requires roughly 165\,GiB per GPU, while rollout and training prefer different tensor-parallel (TP) degrees and weight layouts. Rollplex addresses these constraints with two mechanisms. Phase-aware memory management controls HBM residency according to producer--consumer lifetimes. Parallelism-aware weight sharing uses the same physical storage for layout-compatible tensors across distinct TP degrees and reconstructs only incompatible tensors, avoiding a complete second actor copy. On 32 H800 GPUs, Rollplex achieves $1.23\times$--$1.30\times$ speedup over serial colocation and $1.57\times$--$2.24\times$ over disaggregation under the same GPU budget, while preserving the synchronous RL update.

---


### 135. [Split the Labor: Separating Evidence Interpretation from Decision Aggregation](https://arxiv.org/abs/2608.14509)

**<font color=#1a73e8>作者：</font>** Zhelun Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systems that ask a language model to reach a conclusion from many sources usually concatenate them into one prompt. This conflates two operations with different requirements. Interpreting a source rewards capacity and context. Combining interpretations rewards fixed arithmetic, comparability across instances, and the option to return nothing. Once separated, the design problem becomes the interface between them. We propose a four-field evidence tuple (hypothesis, reliability bucket, rationale, provenance) and show that fixing it determines both halves. The separation also reveals a failure mode in how such systems combine, which we call count-scale drift. Thresholding a sum of unnormalized weights is exactly posterior thresholding, but at an operating point that slides with the number of sources consulted. The slide grows with reader reliability. When source reliabilities differ, the vote rule and the posterior order instances differently, and no threshold reconciles them. Pooling calibrated log-likelihood ratios addresses both problems. The fix is arithmetic rather than architectural, and applies to a class of rules beyond language models: score-summing triage engines, diagnostic panels scored by counting positives, and additive multi-signal detectors. We then instantiate the principle twice on one longitudinal corpus, once after outcomes resolve and once before. The same partition helps in both, at different granularities: over reading in the first, over learning capacity in the second. There, a small sequence encoder on an easy auxiliary objective plus a tree ensemble carrying the censored survival loss reaches 0.921 AUPRC against 0.805 for a hand-crafted baseline. We separate what transfers from what must be re-estimated per domain, and state five predictions that would falsify the framework, three negative results, and which comparisons remain confounded.

---


### 136. [Participatory Moral AI Is Not Neutral: The Invisible Hand of Developers](https://arxiv.org/abs/2608.14522)

**<font color=#1a73e8>作者：</font>** Taenyun Kim, Edyta Bogucka, Daniele Quercia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems make more morally loaded decisions across society, one response has been moral preference elicitation. In this approach, researchers poll participants on hypothetical dilemmas and use the aggregated votes to train a policy that an AI model then applies at scale. Before any vote is cast, developers make three key choices in the moral AI elicitation pipeline: feature scoping, voter sampling, and question framing. In other words, they decide which features go to a vote, which voters to include, and how to present the question. These choices are often opaque, undocumented, and treated as technical details rather than normative ones. We examine each of these choices within a common empirical study and show that each can shape the preferences produced by moral AI elicitation. Across two phases (N = 809) in three deployment contexts (i.e., AI kidney allocation, AI agents simulating absent workers, and generative AI depictions of the deceased), we examine the three main stages of the moral AI elicitation pipeline. First, morally relevant features shift across contexts. This suggests that feature schemas should not be assumed to transfer across deployment domains. Second, preferences differ by political ideology for roughly one-third of features, with some differences reversing direction. The ideological composition of the voter pool can therefore affect the resulting aggregated preference profile. Third, the wording of the elicitation question can narrow or widen ideological gaps by up to a full scale point. The framing conditions also change how moral foundations are associated with participants' judgments. Taken together, these findings suggest that voting-based alignment cannot deliver fair or transparent AI by aggregation alone; at minimum, each stage of the moral AI elicitation pipeline should be audited and disclosed.

---


### 137. [Handover of In-Context Learning State Across Session Boundaries](https://arxiv.org/abs/2608.14528)

**<font color=#1a73e8>作者：</font>** Masahiro Kato, Taka Kato  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study investigates the methodological and theoretical properties of session handover in applications that use large language models. A task may continue in a new session when the context reaches the model's input limit, when the application restarts, or when another agent is asked to finish the task. The application must then decide which information from the earlier session to pass on. We formulate handover as the transfer of a task-relative in-context learning (ICL) state and distinguish exact recovery of earlier material from preservation of the target distribution. Under an exogeneity condition, predictive equivalence characterizes the coarsest deterministic sufficient handover and gives a fixed-length bit requirement. The analysis isolates the effects of the memory constraint, the writer, and the continuation procedure, and quantifies the cost of writing before the realized downstream query is known. We propose a three-part record that stores decisions and constraints exactly, uses task-justified statistics for repeated evidence, and retains original observations whose effect is not preserved by those statistics. Gaussian linear regression gives an exact finite-dimensional handover and finite-bit perturbation bounds, while nonparametric regression gives upper and lower bounds that relate memory to squared prediction error. These results provide a theory and method for deciding what a handover must retain and how its memory requirement depends on the continuation task.

---


### 138. [Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking](https://arxiv.org/abs/2608.14533)

**<font color=#1a73e8>作者：</font>** Ruizhe Wang, Meng Xu, N. Asokan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability detection via static analysis traditionally relies on security experts encoding insecure coding patterns into algorithmic rules. However, this approach often focuses on syntactic patterns and overlooks deeper semantic information in the code, such as the meanings of variable and function names. As software systems grow more complex, modeling vulnerabilities using only syntactic rules becomes increasingly challenging.
In this paper, we propose a semantics-aware approach to detecting software vulnerabilities. We present SETYPE, a semantics-aware type system that can be derived directly from source code based solely on the meanings of symbols and expressions in natural language. In the SETYPE type system, both type inference and checking are performed by Large Language Models (LLMs), and a failed type check indicates a potential vulnerability.
We prototype PYSETYPE to demonstrate the feasibility of SETYPE for detecting vulnerabilities in Python web applications. Our evaluation on real-world applications achieves 87% detection precision and 88% detection accuracy. Using PYSETYPE, we identified 15 potential zero-day vulnerabilities, nine of which were confirmed by developers.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 139. [EEG-PRISM: Physiologically-Grounded Interpretability of Predictions by EEG Foundation Models](https://arxiv.org/abs/2608.13676)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Deeksha M Shama, Punnisa Amornsirikul, Archana Venkataraman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: Foundation models represent the next advancement in AI for EEG analysis; however current explainable AI techniques provide attribution scores in the time-channel input space, which is mismatched to clinical intuition about EEG. Thus, there is a critical need for a universal method that can extend the interpretability of any foundation model to alternative and physiologically relevant domains without modifying or retraining the underlying model. Methods: EEG-PRISM leverages linear transformations and established backpropagation rules to map time-channel attribution scores into alternative domains. We derive mappings to the frequency domain via an invertible DFT and to the source domain via an approximately invertible EEG generative model. We evaluate EEG-PRISM in simulated and real data, assessing recovery of ground-truth phenomena across domains with five foundation models and four AI explainers. Results: In simulation, EEG-PRISM achieves near-perfect spectral recovery and 69.2% spatial accuracy. In epilepsy, EEG-PRISM correctly determines that delta-theta activity is most salient and correctly localizes the seizure onset region with 50% accuracy. In autism, EEG-PRISM localizes the predictive delta-alpha biomarkers to frontal and temporal regions, consistent with prior work. Conclusion: EEG-PRISM is a theoretically-grounded post-hoc attribution method with accurate mapping into the spectral and spatial domains. It supports window-level analysis of transient events (e.g., seizures) and group-level identification of clinically relevant biomarkers (e.g., autism), thus advancing interpretable EEG foundation models. Significance: This work enables physiologically-grounded interpretation of EEG foundation models and supports clinically relevant insights such as event localization and biomarker identification.

---


### 140. [CoDS: Robust Collaborative Perception via Expert-driven Detection and BEV Segmentation](https://arxiv.org/abs/2608.14085)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jinlong Wang, Yuang Jia, Junhong Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception breaks through single-view limitations via multi-agent information exchange. However, multi-source noise such as pose errors and communication delays degrades fusion feature quality, constraining perception performance. Joint training of detection and BEV segmentation provides a natural remedy, where segmented road regions help constrain target distributions and detection bounding boxes help recover ambiguous segmentation boundaries. To this end, we propose a robust Collaborative perception framework with expert-driven Detection and bev Segmentation (CoDS). To address spatial inconsistency in fusion quality, we first introduce the Collaborative Reliability Map (CoRM) to explicitly quantify feature quality distribution. Based on CoRM, we design the Semantic Mixture-of-Experts (S-MoE) module to extract differentiated features for inconsistent feature demands. Finally, to further mitigate feature noise degradation, the Bidirectional Task Complementary Interaction (BTCI) refines task-aware features through bidirectional injection. Extensive experiments on OPV2V and V2V4Real datasets show that our CoDS surpasses existing baselines on both tasks and maintains stable robustness under multi-source noise. Code: this https URL and this https URL.

---


### 141. [Forecast Collapse in Time-Series Foundation Models](https://arxiv.org/abs/2608.14106)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shu Wan, Miles Ma, Hank Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When forecasting hourly returns for 1,000 US equities, we observe an unexpected phenomenon: predictions become nearly flat and show poor stock ranking, as measured by cross-sectional correlation. We call this forecast collapse. Surprisingly, the phenomenon largely disappears when forecasting trading volume under the same setting. We investigate forecast collapse across time-series foundation models (TSFMs), twelve deep-learning forecasting models, and 97 public benchmark configurations, and find that it is closely tied to target predictability. We identify two distinct reasons behind it: low predictability limits the amplitude of calibrated point forecasts, while per-series objectives leave cross-series structure unidentified. These findings reveal a calibration-ranking tradeoff: optimizing squared error leads to flat predictions, whereas directly optimizing cross-sectional correlation improves ranking but can inflate forecast amplitude by more than an order of magnitude. To address this tradeoff, we introduce CalibRank, a simple objective that balances calibration and ranking. On Finance1K, CalibRank nearly triples cross-sectional correlation while keeping amplitude close to the target, and improves correlation on all tested models. Our results reveal a blind spot in conventional time-series evaluation: per-series metrics can hide failures in cross-series structure needed by downstream decisions.

---


### 142. [Training Fair Tabular Foundation Models](https://arxiv.org/abs/2608.14211)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Patrik Kenfack, Jesse C. Cresswell, Anthony L. Caterini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular Foundation Models (TFMs) have emerged as leading methods for tabular predictive tasks, leveraging in-context learning to predict on new data without task-specific training. Despite the increased use of TFMs in high-stakes decision-making, their fairness properties remain largely unexplored. In this work, we incorporate fairness constraints directly into TFM training, enabling fair predictions in a single forward pass. Our approach addresses two key challenges: limited access to sensitive attributes in training data, and the incompatibility of existing fairness techniques with the in-context learning paradigm. We propose FairTFM, a scalable training strategy based on synthetic fairness tasks and a fairness-aware architecture using a gradient reversal layer, which encourages the model to learn representations invariant to sensitive attributes. Experiments on 132 fairness tasks show consistent improvements in fairness while maintaining competitive accuracy.

---


### 143. [Attributing Preprocessing Invariance in Spectral Foundation Models](https://arxiv.org/abs/2608.14227)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dongjun Wei, Hongyi Wu, Yinuo Zou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Preprocessing invariance is an appealing goal for spectral foundation models: a frozen model should remain useful when laboratories preprocess spectra differently. It is usually measured by training a classifier under one preprocessing pipeline and testing it under another, with preserved accuracy read as evidence of learning. We revisit that reading, using a Raman foundation model as a case study. Such models normalize their inputs before any learned parameter is applied. If that normalization maps two differently preprocessed spectra to the same vector, the encoder receives identical inputs, so the invariance cannot be attributed to learning. For a normalization that uses each spectrum's own statistics, this happens exactly when one spectrum is a positive multiple of the other plus a constant. Several standard preprocessing operations take that form. The encoder should therefore be measured against the normalization alone, which has no learned parameters. On six Raman evaluation datasets, the model does not measurably outperform its own normalization. It improves on raw spectra, but so does the normalization alone. Training does improve the encoder over random initialization, and a controlled experiment shows that it learns to ignore a transformation only when that transformation reaches it. A numerical test settles which transformations a given normalization removes. Across released systems in five modalities, most normalizations already remove transformations of that form, and several of those systems claim that invariance as learned. Replicating the comparison on two of them shows no gain either.

---


### 144. [CytoBERT: A Foundation Model for Cytometry Data](https://arxiv.org/abs/2608.14414)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Syed Abdul Haseeb Qadri, Bjarne C. Hiller, Felix Blanke 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cytometry measures the complex characteristics of single cells (e.g., counts and protein expression of immune cells) and is widely used across immunological research and clinical settings. However, cytometry data is highly heterogeneous and unstandardized due to experimental protocols and the choice of measured features. While machine learning methods hold the potential to gain deeper insights into cell biology, these challenges make them difficult to apply and transfer across studies. Recent advances in foundation models can alleviate these issues, but corresponding approaches are still scarce in this field. To address this, we provide CytoBERT, a publicly available, open-source, open-weight foundation model for single-cell cytometry data with variable marker panels. CytoBERT is pretrained in a self-supervised manner on a large-scale cytometry corpus (15 human datasets with heterogeneous marker panels and more than 50 million cells) curated through marker standardization, enabling it to learn transferable inter-marker relationships within cells. Fine-tuning CytoBERT for sample-level classification demonstrates that transfer learning across heterogeneous cytometry datasets is feasible, providing a starting point for scalable, generalizable cytometry analysis. Code is available at GitHub.

---


> [!TIP]
> 当前位于：**101-144**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-144**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
