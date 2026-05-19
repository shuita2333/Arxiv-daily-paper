# 🧠 大模型相关研究 | 2026年05月20日

> 本类共 **346** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-346](./part-07.md)

---

### 101. [Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents](https://arxiv.org/abs/2605.16986)

**<font color=#1a73e8>作者：</font>** Jingxing Wang, Chenyu Zhou, Zhihui Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents benefit from reusable skills, yet test-time tasks often require guidance more specific than a static skill library can provide. We propose \emph{SkillTTA}, a Test-Time Adaptive Skill Synthesis method that retrieves a small set of training trajectories relevant to the current task and synthesizes them into a temporary, task-specific textual skill. The solver model is kept fixed, so adaptation happens entirely through generated context rather than parameter updates. We evaluate the method on SpreadsheetBench, ALFWorld, and BigCodeBench. Compared with static trajectory-to-skill synthesis using GPT-5.5, task-specific skills improve SpreadsheetBench Pass@1 from 0.397 to 0.505 and BigCodeBench Pass@1 from 0.517 to 0.651. On ALFWorld, the method matches a heavier memory-learning baseline within four points of success rate while producing the shortest successful trajectories among reported methods. Ablations on SpreadsheetBench further show that synthesized skills outperform raw trajectory prompting, that top-$k$ retrieval should stay small, and that failed trajectories are especially useful because they expose recurring evaluator-facing mistakes.

---


### 102. [Evaluation Drift in LLM Personality Induction: Are We Moving the Goalpost?](https://arxiv.org/abs/2605.16996)

**<font color=#1a73e8>作者：</font>** Prateek Rajput, Yewei Song, Iyiola E. Olatunji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can large language models reliably express a human-like personality, or are they merely mimicking surface cues without a stable underlying profile? To investigate this, we induce personality in LLMs by fine-tuning them on the long-form essays, where each essay is associated with a target Big Five personality profile. We then evaluate the stability and fidelity of the induced personality using the IPIP-NEO questionnaire. Specifically, we ask: (i) does post-training (SFT, DPO, ORPO) stabilize questionnaire scores under prompt rephrasings, and (ii) can it induce target Big Five profiles from unguided essays? Our results demonstrate that fine-tuning consistently reduces variance in questionnaire responses across five models, directly mitigating the evaluation fragility reported in pre-trained models. However, this newfound stability reveals a more fundamental limitation: accuracy on the full five-dimensional profile remains near chance, even when single-trait scores improve. This indicates that unguided essays lack the cues needed for faithful personality expression. We therefore argue for scenario-grounded datasets or interactive elicitation that accumulates test-aligned evidence over time.

---


### 103. [Ranking-Aware Calibration for Reliable Multimodal Reinforcement Learning](https://arxiv.org/abs/2605.16999)

**<font color=#1a73e8>作者：</font>** Peng Cui, Boyao Yang, Jun Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning post-training has substantially improved the reasoning accuracy of vision-language models, yet the resulting policies remain poorly calibrated. Terminal correctness rewards provide no gradient that penalizes confident errors more than uncertain ones and no signal that ties confidence to the quality of visual evidence, a gap that becomes especially severe under corrupted or ambiguous inputs where models continue to report high confidence on incorrect answers. We introduce Ranking-Aware Calibration (RAC), a training-time framework that supervises confidence using two comparison signals that group-based RL already produces at no additional labeling cost. The ranking-aware group loss enforces that a better rollout receives higher confidence than a worse one within the same prompt. The clean--corrupted pairwise loss enforces that confidence attenuates as visual evidence degrades. Because the ranking signal forces the policy to distinguish between correct and incorrect reasoning paths, it also reinforces task accuracy beyond what correctness rewards alone produce. Both losses require no external confidence annotations and integrate naturally with group-based RL post-training. We instantiate RAC on Qwen2.5-VL and InternVL-3.5 backbones and evaluate on six multimodal reasoning benchmarks under clean and corrupted inputs. Empirical results show that the ranking-aware loss substantially improves task accuracy by teaching the policy to discriminate between better and worse reasoning, while the pairwise corruption loss reduces calibration error under degraded inputs. Their combination achieves the best calibration across all tested backbones while improving accuracy in the majority of settings.

---


### 104. [BoLT: A Benchmark to Democratize Black-box Optimization Research for Expensive LLM Tasks](https://arxiv.org/abs/2605.17000)

**<font color=#1a73e8>作者：</font>** Ruth Wan Theng Chew, Zhiliang Chen, Apivich Hemachandra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization of LLM training and inference configurations, such as hyperparameters, data mixtures, and prompts, is critical to performance, but it is often approached heuristically in practice, leading to potentially suboptimal outcomes. By framing them as noisy, expensive, and derivative-free optimization problems, Bayesian optimization (BO) and other black-box optimization (BBO) methods offer a promising yet underexplored direction for principled, sample-efficient methods. However, LLM training and inference costs are prohibitively high for most of the BBO research community, and new methods are often only evaluated on synthetic test functions and small-scale datasets that fail to capture the challenges of modern LLM optimization problems. This impedes the development of BBO methods and makes it difficult to assess their effectiveness on modern LLM tasks. We introduce BoLT, the first LLM-centric benchmark that democratizes LLM research for the BBO community. BoLT is released at this https URL. BoLT covers broad and well-motivated LLM optimization problems, involving multi-fidelity, multi-objective, heteroscedastic noise, and high-dimensional search spaces. Each problem in BoLT is grounded in real experimental data and made fully reproducible and accessible through lightweight surrogate models fitted to the results of thousands of real LLM experiments. We benchmark BoLT against an extensive range of BO and BBO methods, showing that selected BO methods consistently outperform others across tasks and highlighting gaps in existing BBO methods on LLM tasks, underscoring the need to modernize benchmarks for the BBO community.

---


### 105. [Learning-Zone Energy: Online Data Selection for Efficient RL Post-Training](https://arxiv.org/abs/2605.17003)

**<font color=#1a73e8>作者：</font>** Peng Cui, Boyao Yang, Jun Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) post-training has emerged as the dominant paradigm for eliciting mathematical reasoning in Large Language Models (LLMs), yet prevailing techniques such as GRPO and DAPO distribute rollout and gradient budgets nearly uniformly across prompts, squandering compute on samples that are already mastered or remain far beyond the model's current capability. To address this fundamental inefficiency, we propose Learning-Zone Energy (LZE), a theoretically grounded, fully online data selection framework that concentrates computation on the model's active learning frontier. At its core, we define a closed-form Learning-Zone Energy Score that fuses three complementary signals, an initial-difficulty anchor, a normalized outcome-uncertainty term, and a pass-rate momentum, into a single scalar that is provably aligned with the expected magnitude of group-relative policy gradient updates. A forward pruner with replay further reduces wall-clock time cost by skipping rollout generation for persistently solved prompts while periodically checking for forgetting. Evaluated on Qwen-family models (1.5B-8B) across GSM8K, MATH and DAPO-MATH, our method retains only 40% of the training data per step yet matches or surpasses full-data baselines, with especially pronounced out-of-distribution gains on AIME25 (+45.9%) and AMC23 (+18.2%), alongside an estimated 36% reduction in training FLOPs. Our code is available at this https URL.

---


### 106. [HalluScore: Large Language Model Hallucination Question Answering Benchmark](https://arxiv.org/abs/2605.17007)

**<font color=#1a73e8>作者：</font>** Aisha Alansari, Hamzah Luqman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable progress in natural language generation, but remain susceptible to hallucination. In response to growing concerns about hallucinations, several benchmarks have been developed, primarily in English and Chinese. However, Arabic remains underrepresented, with limited benchmarks for LLMs hallucination due to scarce annotated resources and the language's morphological complexity. Consequently, existing benchmarks do not adequately reflect the linguistic, cultural, and reasoning characteristics of Arabic. To address this gap, we introduce HalluScore, a structured Arabic question answering benchmark designed to evaluate hallucination behavior in LLMs across different levels of reasoning difficulty, various knowledge domains, historical timelines, and culturally grounded Arabic scenarios. It contains 827 carefully curated questions for evaluating, detecting, and mitigating hallucination in LLMs. The dataset was constructed through a structured pipeline involving quality assurance, filtering for clarity and factual validity, and model-driven selection to retain questions that consistently trigger hallucinations. Each question is linked to verified ground-truth evidence, answer explanations, and multi-label annotations. Using the HalluScore benchmark, we conduct a comprehensive empirical analysis of hallucination patterns across 17 Arabic, multilingual, and reasoning LLMs. Moreover, we provide high-quality human annotations identifying hallucinated, non-hallucinated, and partially hallucinated responses of all evaluated LLMs. These results suggest that hallucination in Arabic LLMs extends beyond factual inaccuracies, encompassing challenges related to cultural understanding, linguistic reasoning, and logical consistency. We release HalluScore to support future research on improving the reliability and cultural competence of LLMs in Arabic.

---


### 107. [When Dynamics Shift, Robust Task Inference Wins: Offline Imitation Learning with Behavior Foundation Models Revisited](https://arxiv.org/abs/2605.17017)

**<font color=#1a73e8>作者：</font>** Rishabh Agrawal, Rahul Jain, Ashutosh Nayyar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavior Foundation Models (BFMs) enable scalable imitation learning (IL) by pretraining task-agnostic representations that can be rapidly adapted to new tasks. However, existing BFMs assume fixed environment dynamics, limiting their robustness under real-world shifts such as changes in friction, actuation, or sensor noise. We address this by formulating BFM task-inference as a robust minimax optimization problem, enabling adaptation to worst-case dynamics perturbations without modifying pretraining. To the best of our knowledge, this is the first BFM-based framework that achieves robustness to dynamics shifts while relying solely on offline data from a single nominal environment. Our approach significantly outperforms standard BFM and robust offline IL baselines under dynamics shifts. These results demonstrate that robust policy can be achieved entirely at task-inference time, improving the practicality of BFMs in dynamic settings.

---


### 108. [Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road](https://arxiv.org/abs/2605.17026)

**<font color=#1a73e8>作者：</font>** Ngoc-Hieu Nguyen, Parshin Shojaee, Phuc Minh Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in large language models has led to the emergence of reasoning models, which have shown strong performance on complex tasks through specialized fine-tuning procedures. While these methods reliably improve pass@1 accuracy, prior works have observed that they show a coverage shrinkage behavior, where pass@k degrades relative to the base model. In this paper, we investigate the reasoning shrinkage arise under SFT-based post-training. We hypothesize that this behavior is driven by properties of the fine-tuning data, specifically related to decision points or "forks in the road" scenarios where model faces indecipherable patterns with multiple valid reasoning paths. To test this hypothesis, we design controlled case studies that simulate such decision-point settings, spanning indecipherable nodes in graph branching, and reasoning modes. By tracking post-training dynamics in these settings, we find that the shrinkage phenomenon is tightly correlated with the prevalence of decision-point scenarios in the training data. We also demonstrate that this shrinkage behavior can be partially mitigated through targeted data synthesis design of decision-points, and a more systematic diversity-encouraging decoding mechanism. Our findings identify data-centric factors as a key driver of shrinkage in reasoning models and highlight diversity-aware designs as an effective lever for controlling it.

---


### 109. [Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation](https://arxiv.org/abs/2605.17034)

**<font color=#1a73e8>作者：</font>** Osama Zafar, Alexander Nemecek, Yiqian Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard PII filters often miss contextual data leakage in RAG systems, such as non-regulated attribute clusters that collectively identify individuals. We introduce a Privacy Policy Enforcement (PPE) framework using dual one-class density estimators with fused text embeddings and a calibrated abstain region for out-of-distribution inputs. Using an axis-stratified, multi-LLM synthetic data pipeline across medicine, finance, and law, we found that traditional Gaussian Mixture baselines fail on borderline-safe stress tests by focusing on linguistic register rather than content.
Our proposed T3+OCSVM detector, trained on safe and borderline-safe data, achieves a borderline AUROC of 0.93+ while reducing false positives by 44-55 percentage points and maintaining millisecond latency. Compared to supervised MLP classifiers or 14B-parameter LLM judges, our framework offers superior operational suitability, as the former suffers from high abstention rates and the latter from latency and calibration issues. This methodology provides a robust stress-testing standard for any synthetic-data-trained classifier.

---


### 110. [Reliability and Effectiveness of Autonomous AI Agents in Supply Chain Management](https://arxiv.org/abs/2605.17036)

**<font color=#1a73e8>作者：</font>** Carol Xuan Long, David Simchi-Levi, Feng Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper studies autonomous generative AI agents in multi-echelon supply chains using the MIT Beer Game. We identify four inference-time levers that shape performance: model selection, policies and guardrails, centralized data sharing, and prompt engineering. Model capability is the dominant factor: an out-of-the-box reasoning model exceeds human-level performance, and optimized reasoning models reduce costs by up to 67% relative to human teams. However, strong average performance masks substantial reliability risks. We introduce the agent bullwhip effect, the amplification of decision unreliability across echelons, manifesting along two dimensions: decision variance increases both across facilities at the same point in time and within the same facility across time. We develop a mathematical framework showing that this phenomenon is inherent to multi-agent systems that involve coordination and information delays, and we demonstrate that repeated sampling fails to meaningfully reduce it. To address this limitation, we propose a Group Relative Policy Optimization (GRPO)-based reinforcement-learning post-training framework that trains a shared base LLM using system-level supply-chain rewards. GRPO post-training substantially reduces tail events, curtails agent bullwhip, and improves the reliability of autonomous supply-chain agents.

---


### 111. [Agentic AI Translate: An Agentic Translator Prototype for Translation as Communication Design](https://arxiv.org/abs/2605.17041)

**<font color=#1a73e8>作者：</font>** Masaru Yamada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Agentic AI Translate, an agentic translator prototype that operationalises the thesis of Yamada (forthcoming) -- that the metalanguage of Translation Studies has become an instruction code for generative AI. The system replaces the dominant text-in / text-out paradigm of machine translation with a four-stage agentic cycle (Identify -> Prompt -> Generate -> Verify), preceded by an interactive specification phase in which the user composes -- through model-assisted dialogue -- a structured translation brief grounded in skopos theory, register, audience, and genre conventions. The verification stage adopts the GEMBA-MQM error-span protocol (Kocmi & Federmann, 2023) for evidence-grounded scoring, and document-level coherence is preserved through a DelTA-lite memory of proper nouns and a running bilingual summary, after Wang et al. (2025). We describe the philosophical motivation, the architectural commitments, the four reference-material categories the system consumes, and the principal design tensions the architecture makes explicit. Empirical validation is left for future work; the contribution here is conceptual and architectural -- an executable embodiment of the position that translation in the GenAI era is communication design, not text conversion.

---


### 112. [PersonaArena: Dynamic Simulation for Evaluating and Enhancing Persona-Level Role-Playing in Large Language Models](https://arxiv.org/abs/2605.17044)

**<font color=#1a73e8>作者：</font>** Wenlong Shi, Jianxun Lian, Mingqi Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly serve as interactive social agents, yet their ability to maintain coherent and authentic persona-level role-playing remains limited, particularly in realistic social scenarios. Existing research predominantly focuses on character-level settings and relies on static evaluation formats, failing to capture the complexity of everyday social interactions. In this work, we present PersonaArena, a dynamic simulation framework for evaluating and improving persona-level role-playing in LLMs. PersonaArena leverages a large, filtered corpus of user-generated social content to construct a nuanced persona bank, and elicits multi-turn, context-rich interactions within simulated social environments. Our framework features a multi-agent debating judge for holistic and unbiased assessment. Through extensive experiments, we demonstrate that PersonaArena enables rigorous evaluation and enhancement of LLMs' role-playing capabilities, advancing the development of more authentic and socially adept AI agents.

---


### 113. [1GC-7RC: One Graphic Card -- Seven Research Challenges! How Good Are AI Agents at Doing Your Job?](https://arxiv.org/abs/2605.17046)

**<font color=#1a73e8>作者：</font>** Robin-Nico Kampa, Fabian Deuser, Anna Bößendörfer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous AI coding agents are becoming a core tool for ML practitioners in industry and research alike. Despite this growing adoption, no standardized benchmark exists to evaluate their ability to design, implement, and train models from scratch across diverse domains. We introduce **1GC-7RC** (*Single Graphic Card: Seven Research Challenges*), a benchmark comprising seven ML tasks spanning language modeling, image classification, semantic segmentation, graph learning, tabular prediction, time-series forecasting, and text classification. Each task provides a locked data-preparation and evaluation script together with a baseline training script; the agent may only modify the training code, has no access to pretrained weights (with one controlled exception for semantic segmentation), no internet access, and must complete each task within a task-specific wall-clock budget (40-120 minutes) on a single GPU. We evaluate seven coding agents: five proprietary (Claude Code with Sonnet 4.6, Opus 4.6, and Opus 4.7; Codex CLI with GPT 5.5; and OpenCode with Qwen 3.6+) and two open-source (OpenCode with Kimi K2.5, Kimi K2.6). Across 5 runs per agent-task pair, we report substantial performance differences that reveal varying levels of implicit ML knowledge, planning ability, and time-budget management. The benchmark, harness, and all evaluation artifacts are publicly available on GitHub at this https URL to facilitate reproducible comparison of future agents. Because our benchmark design is modular, the benchmark can be extended to new tasks and domains, adapted to different GPU budgets, and used to study multi-agent settings, making it a flexible platform for future research on autonomous research agents.

---


### 114. [Towards Human-Level Book-Writing Capability](https://arxiv.org/abs/2605.17064)

**<font color=#1a73e8>作者：</font>** Jan Zierstek, Matteo Batelic, Maya Medjad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models optimized for instruction following and agentic tasks remain poorly aligned with the requirements of high-quality creative writing. Fiction frequently depends on behaviors that assistant-tuned models are explicitly trained to avoid, particularly deception, moral ambiguity, and unreliable narration. As a result, generated stories often appear structurally correct while remaining stylistically generic, overly explanatory, or weakly grounded in human literary behavior. We present a dataset construction and training framework for book-scale creative writing that reframes supervised fine-tuning as a prompt-to-book generation task grounded in human-authored fiction. Starting from public-domain novels, we derive a multi-resolution planning scaffold by summarizing each book at progressively finer levels, from a high-level premise to chapter- and scene-level structure. We then invert this hierarchy during training: the model learns to expand a prompt into increasingly detailed plans and finally into the original human-authored book text. This formulation preserves human prose as the final supervised target while using intermediate summaries to make book-scale generation learnable. We train a long-context language model on these prompt-to-book trajectories and study whether this objective shifts generation away from assistant-style prose and toward human literary writing.

---


### 115. [PyraVid: Hierarchical Multimodal Memory for Long-Horizon Video Reasoning](https://arxiv.org/abs/2605.17065)

**<font color=#1a73e8>作者：</font>** Sikuan Yan, Sicheng Dong, Haotong Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Memory has become an increasingly important component of agentic systems, as these systems are expected to reason over long-term experience. However, prior work has largely focused on unimodal memory, leaving multimodal memory relatively underexplored despite its central role in real-world applications. Compared with unimodal settings, multimodal memory introduces additional challenges, including heterogeneous input integration, person-centric information alignment, and evidence aggregation across different granularities. We present PyraVid, a hierarchical multimodal memory framework inspired by Event Segmentation Theory from cognitive science. PyraVid organizes long videos into a coarse-to-fine pyramid structure, enabling structured memory access and effective evidence aggregation. It further supports structure-guided memory expansion with pruning, allowing the retrieval of related events with strong causal connectivity but low semantic similarity while reducing noise. Experiments on multiple long-video understanding benchmarks show that PyraVid consistently improves performance across datasets, model scales, and question types, highlighting the effectiveness of hierarchical multimodal memory for long-horizon reasoning.

---


### 116. [EPIC-Bench: A Perception-Centric Benchmark for Fine-Grained Embodied Visual Grounding in Vision-Language Models](https://arxiv.org/abs/2605.17070)

**<font color=#1a73e8>作者：</font>** Haozhe Shan, Xiancong Ren, Han Dong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While large vision-language models (VLMs) are increasingly adopted as the perceptual backbone for embodied agents, existing benchmarks often rely on question-answering or multiple-choice formats. These protocols allow models to exploit linguistic priors rather than demonstrating genuine visual grounding. To address this, we present EPIC-Bench, Embodied PerceptIon BenChmark, a fine-grained grounding benchmark designed to systematically evaluate the visual perceptual capabilities of VLMs in real-world embodied environments. Comprising 6.6k meticulously annotated tuples (Image, Text, Mask), EPIC-Bench spans 23 fine-grained tasks across three core stages of the embodied interaction pipeline: Target Localization, Navigation, and Manipulation. Extensive evaluations of over 89 leading VLMs reveal that while advanced reasoning models show promise, current VLMs universally struggle with complex visual-text alignment for physical interactions. Specifically, models exhibit critical bottlenecks in multi-target counting, part-whole relationship understanding, and affordance region detection. EPIC-Bench provides a robust foundation and actionable insights for advancing the next generation of vision-driven embodied models.

---


### 117. [RAGA: Reading-And-Graph-building-Agent for Autonomous Knowledge Graph Construction and Retrieval-Augmented Generation](https://arxiv.org/abs/2605.17072)

**<font color=#1a73e8>作者：</font>** Chengrui Han, Zesheng Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing LLM-driven knowledge graph (KG) construction methods predominantly employ stateless batch processing pipelines, exhibiting structural deficiencies in cross-chunk semantic relation capture, entity disambiguation, and construction process interpretability. These limitations undermine KG quality, retrieval precision, and deployment trust in high-stakes domains.
We propose RAGA (Reading And Graph-building Agent), an LLM-based autonomous KG construction and retrieval fusion framework. RAGA provides an atomic toolset supporting full KG lifecycle CRUD operations and embeds a Read-Search-Verify-Construct cognitive constraint into a ReAct tool loop. A KG-vector synchronization mechanism enables hybrid symbolic-vector retrieval, while evidence-anchored verification links every knowledge entry to its source text for auditable provenance.
Preliminary experiments on a subset of the QASPER scientific QA dataset indicate that RAGA's fusion retrieval outperforms zero-shot baselines, with KG integration providing measurable gains in both answer and evidence quality. The framework design and experimental baseline serve as a reference for agent-driven autonomous KG construction.

---


### 118. [S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination](https://arxiv.org/abs/2605.17076)

**<font color=#1a73e8>作者：</font>** Sajjad Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concurrent LLM agents sharing mutable natural-language state produce Structural Race Conditions (SRCs): write-write and cross-shard stale-read conflicts that silently corrupt agent output. Existing multi-agent frameworks (LangGraph, CrewAI, AutoGen) provide no write-ownership semantics over shared state.
We present S-Bus, an HTTP middleware whose central mechanism is a server-side DeliveryLog: a per-agent log of HTTP GET operations that automatically reconstructs each agent's read set at commit time without agent SDK changes under HTTP/1.1. The consistency property the DeliveryLog provides -- Observable-Read Isolation (ORI), a partial causal consistency over the HTTP-observable projection of the read set -- prevents structural race conditions when agents collaborate via shared shards.
Three contributions: (C1) The DeliveryLog mechanism for automatic HTTP-traffic-based read-set reconstruction, with three-tier mechanised evidence: ReadSetSoundness and ORICommitSafety machine-checked in TLAPS (modulo one retained typing axiom); exhaustive TLC at N=3 (20,763,484 distinct states, zero violations); Dafny discharges 9 inductive soundness lemmas. (C2) Empirical structural-conflict prevention parity against PostgreSQL 17 SERIALIZABLE and Redis 7 WATCH/MULTI on shared-shard contention sweeps with 427,308 active HTTP-409 conflicts: zero Type-I corruptions across all three backends. (C3) ORI's operating envelope is topology-conditional: semantically neutral in dedicated-shard workloads; harmful in single-shard collaborative writing because preservation propagates concurrent contradictions.
Source code: this https URL

---


### 119. [Can LLMs Think Like Consumers? Benchmarking Crowd-Level Reaction Reconstruction with ConsumerSimBench](https://arxiv.org/abs/2605.17079)

**<font color=#1a73e8>作者：</font>** Tianyu Wang, Jiajun Li, Jianghao Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used as ``digital consumers'' to simulate public opinion, pre-test marketing decisions, and anticipate audience response. However, existing evaluations rarely ask whether a model can reconstruct the concrete reaction patterns that real consumers surface in public discourse. We introduce ConsumerSimBench, a benchmark built from 1,553 real Chinese social-media topics and 23,122 atomic, rule-audited criteria spanning four reaction families. Rather than scoring open-ended generations with a holistic preference judge, ConsumerSimBench decomposes each task into auditable yes-no decisions over concrete reaction points, raising three-judge agreement from 65.8% to 92.1% with 98.4% agreement between pointwise judge decisions and human-majority labels. Across 13 frontier generators, the strongest model, Gemini-3.1-Pro, covers only 47.8% of real reaction criteria, while GPT-5.2 and Claude-4.6 trail far behind despite their strength on technical benchmarks. The failures reveal a sharp gap between technical-benchmark performance and socially grounded consumer intuition. A direct structured reasoning prompt decreases coverage, while a generate--reflect multi-agent pipeline improves MiMo-V2.5-Pro from 32.9% to 37.6% on a subset. ConsumerSimBench reframes consumer simulation as a forecasting problem over real public-discourse reactions, showing that frontier LLMs remain far from reliably predicting what consumers will actually care about in high-context Chinese consumer discourse.

---


### 120. [Scale Determines Whether Language Models Organize Representation Geometry for Prediction](https://arxiv.org/abs/2605.17084)

**<font color=#1a73e8>作者：</font>** Weilun Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In language models, what a representation encodes is determined by the geometry of its representation space: distances, not activations, carry meaning. Existing tools characterize the shape of this geometry but do not ask what that shape is organized for. We introduce Subspace PGA, a metric that tests whether a layer's distance structure aligns with the readout subspace of the unembedding matrix $W_U$ more than with random subspaces of equal size. Across seven Pythia models (70M--6.9B) and three cross-family models, intermediate geometry is significantly organized for prediction (peak $z = 9$--$24$), but the degree is scale-dependent: small models ($d \leq 1024$) progressively lose it at late layers during training -- even as loss keeps improving -- while large models ($d \geq 2048$) preserve it throughout. We trace this to a capacity trade-off: a few dominant directions migrate away from $W_U$'s readout, masking rather than destroying the predictive structure beneath, and removing them restores alignment. Neither spectral metrics nor loss curves capture this distinction. Scale thus determines not only how well a model predicts, but how its representation geometry is organized to do so.

---


### 121. [ACIL: Auto Chain of Thoughts for In-Context Learning](https://arxiv.org/abs/2605.17088)

**<font color=#1a73e8>作者：</font>** Rui Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have shown that Chain-of-Thought (CoT) reasoning can substantially improve performance on complex reasoning tasks. At the same time, In-Context Learning (ICL) has become an important mechanism for adapting LLMs to new tasks without updating model parameters, using only examples provided in the prompt. However, standard ICL often struggles on tasks that require multi-step reasoning, because the demonstrations usually contain only input-output pairs and lack explicit intermediate reasoning steps. This paper introduces an Automatic Chain-of-Thought (Auto-CoT) framework to improve ICL by automatically constructing reasoning-enhanced demonstrations. Auto-CoT generates reasoning chains for input-output examples, augments the prompt context with structured intermediate explanations, and removes irrelevant or low-quality demonstrations through a systematic selection process. By incorporating high-quality reasoning examples into the ICL prompt, Auto-CoT guides the model toward more reliable reasoning and improves prediction accuracy. Experiments across multiple reasoning tasks demonstrate that the proposed framework improves ICL performance by providing explicit intermediate reasoning guidance.

---


### 122. [HEED: Density-Weighted Residual Alignment for Hybrid Vision-Language Model Distillation](https://arxiv.org/abs/2605.17093)

**<font color=#1a73e8>作者：</font>** Yihao Liang, Niraj K. Jha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilling vision-language models into faster hybrid architectures, such as 3:1 Mamba-2/attention mixes, is now standard practice for making inference efficient. Aggregate benchmarks suggest that this works but they hide selective failures. When we distill Qwen3-VL-8B-Instruct into a 3:1 Mamba-2/attention hybrid, student model stays within 2 points of the teacher across visual reasoning benchmarks like MMStar, MMBench, and MMMU-Pro, while dropping 13 points on optical-character-recognition and document tasks. The student can still understand the scene but loses the fine-grained text needed to answer. We localize much of the failure to a specific kind of position. In a high-resolution image, most patches are sky, wall, or smooth texture, while a small fraction carries text, edges, object boundaries, or other local details. In a token-level diagnostic, the top 10% highest-density patches have 3.6$\times$ larger residual drift than the bottom 10% lowest-density patches and 3.5$\times$ larger teacher-masking answer contribution. Uniform weighting devotes many loss terms to low-information background patches, whereas sparse answer-bearing patches receive no special protection. The required intervention is minimal: we replace uniform residual alignment with density-weighted residual alignment, using patch self-dissimilarity as a training-free proxy for position importance. We call this HEED. Compared with normal end-to-end distillation, HEED increases performance by 8.7 points on OCRBench v2 and 5.13 points on a 10-benchmark average. The gain is realized on different teacher models and hybrid architectures. After standard post-training, the student reaches teacher-level performance on the 10-benchmark average with a 4.12$\times$ throughput and a 68% memory saving at 128k context, with no additional parameters and no inference-time cost.

---


### 123. [SEMA-RAG: A Self-Evolving Multi-Agent Retrieval-Augmented Generation Framework for Medical Reasoning](https://arxiv.org/abs/2605.17101)

**<font color=#1a73e8>作者：</font>** Yongfeng Huang, Ruiying Chen, James Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is widely employed to mitigate risks such as hallucinations and knowledge obsolescence in medical question answering, yet its predominantly single-round, static retrieval paradigm misaligns with the multi-stage process of clinical reasoning. This compressed workflow induces two structural deficiencies: question-to-query translation often lacks clinically grounded semantic interpretation, and retrieval lacks iterative sufficiency feedback, making it difficult to form reliable evidence chains. We argue that both issues stem from a deeper cause: overloading a single reasoning chain with heterogeneous tasks of interpretation, exploration, and adjudication. The remedy is to reconstruct the workflow via task decoupling and dynamic multi-round exploration. To this end, we propose SEMA-RAG, a Self-Evolving Multi-Agent RAG framework for medical question answering, which assigns these roles to three specialist agents: the Interpreter Agent for clinical schema interpretation, the Explorer Agent for sufficiency-driven self-evolving retrieval, and the Arbiter Agent for evidence adjudication and answer selection. Across five benchmarks and five LLM backbones, SEMA-RAG improves the strongest baseline by +6.46 accuracy points on average, measured per backbone.

---


### 124. [Scientific Logicality Enriched Methodology for LLM Reasoning: A Practice in Physics](https://arxiv.org/abs/2605.17104)

**<font color=#1a73e8>作者：</font>** Zhaoxin Yu, Nan Xu, Kun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the continuous advancement of reasoning abilities in Large Language Models (LLMs), their application to scientific reasoning tasks has gained significant research attention. Current research primarily emphasizes boosting LLMs' performance on scientific QA benchmarks by training on larger, more comprehensive datasets with extended reasoning chains. However, these approaches neglect the essence of the scientific reasoning process -- logicality, which is the rational foundation to ensure the validity of reasoning steps leading to reliable conclusions. In this work, we make the first systematic investigation into the internal logicality underlying LLM scientific reasoning, and develop a scientific logicality-enriched methodology, including a set of assessment criteria and data sampling methods for logicality-guided training, to improve the logical faithfulness as well as task performance. Further, we take physics, characterized by its diverse logical structures and formalisms, as an exemplar discipline to practise the above methodology. For data construction, we extract scientific problems from academic literature and sample a high-quality dataset exhibiting strong logicality. Experiments based on three different backbone LLMs reveal that: 1) the training data we constructed can effectively improve the scientific logicality in LLM reasoning; and 2) the enriched scientific logicality plays a critical role in solving scientific problems. Code is available at \href{this https URL}{this https URL}.

---


### 125. [HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools](https://arxiv.org/abs/2605.17106)

**<font color=#1a73e8>作者：</font>** Aashna Garg, Siddharth Singha Roy, Jinu Jang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production LLM deployments increasingly maintain heterogeneous model pools spanning order-of-magnitude cost differences. Existing routers make binary strong-vs-weak decisions and couple learned parameters to specific model identities, requiring retraining whenever the catalog changes. We present HyDRA (Hybrid Dynamic Routing Architecture), a framework that predicts fine-grained, multi-dimensional capability requirements per query and matches them against configuration-defined model profiles via shortfall matching. A ModernBERT encoder with K=4 independent sigmoid heads scores each query along reasoning, code generation, debugging, and tool use; a shortfall-matching algorithm then selects the cheapest model whose capabilities meet the predicted requirements. The deployed predictor runs at 86 ms median CPU inference latency in production, and is fully decoupled from the model catalog -- adding or removing models requires only a configuration change, with zero retraining. On SWE-Bench Verified (5-model pool: GPT-5.4-mini, Claude Haiku 4.5, GPT-5.3 Codex, Claude Sonnet 4.6, GPT-5.4), HyDRA's tunable shortfall threshold spans three regimes: peak-quality exceeds the always-strong Claude Sonnet 4.6 baseline (75.4% vs. 74.2% resolution) at 12.9% cost savings; iso-quality matches Sonnet at 54.1% cost savings, a 6x improvement over our prior in-house binary router at 9.1%; aggressive pushes savings to 72.5% for a 3.2-point quality trade. Results generalize across LiveCodeBench, BigCodeBench, and tau-bench. HyDRA is deployed to all users in GitHub Copilot's VS Code Chat auto-mode and -- to our knowledge for the first time in the LLM routing literature -- demonstrates language-invariant routing across CJK, European, and other script families.

---


### 126. [Capturing LLM Capabilities via Evidence-Calibrated Query Clustering](https://arxiv.org/abs/2605.17110)

**<font color=#1a73e8>作者：</font>** Fangzhou Wu, Sandeep Silwal, Qiuyi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Query clustering organizes queries into groups that reflect shared latent capability demands, enabling capability-aware LLM evaluation. Existing clustering methods, which primarily rely on semantic taxonomies or embeddings, often fail to capture such latent capability requirements due to a misalignment between surface-level semantics and actual model performance. We propose ECC, an algorithm that calibrates prior semantic embeddings using limited posterior model comparisons to bridge the gap between surface-level semantics and latent capability requirements. ECC characterizes each cluster through a capability profile parameterized by a Bradley-Terry model and uses trainable mixture weights to accommodate queries with mixed capability demands, jointly learning a flexible, capability-aware clustering structure that supports query-specific inference of LLM capabilities. Extensive quantitative and qualitative evaluations demonstrate that ECC significantly improves LLM capability ranking quality, outperforming human-labeled and embedding-based baselines by an average of 17.64 and 18.02 percentage points, respectively, and proves effective in downstream tasks such as query routing.

---


### 127. [F2IND-IT! -- Multimodal Fuzzy Fake Indian News Detection using Images and Text](https://arxiv.org/abs/2605.17115)

**<font color=#1a73e8>作者：</font>** Kushal Trivedi, Murtuza Shaikh, Khushi Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biased manipulation of facts across regional and national media outlets complicates misinformation detection in diverse landscapes like India. This paper introduces a novel multimodal framework combining visual and textual modalities for enhanced fake news detection on Indian media. The architecture utilizes a ResNet-50 Convolutional Neural Network to extract visual features from news images, a DistilBERT encoder to obtain textual semantic embeddings, and an Adaptive Neuro-Fuzzy Inference System (ANFIS) to generate a fuzzy reliability score. A lightweight attention-based fusion module assigns learnable weights to each modality prior to classification. Evaluated on the IFND dataset, the proposed model is validated through an in-depth comparative analysis against previous research. Experimental results demonstrate superior performance across accuracy, precision, recall, and $F_1$-scores, confirming the efficacy of the architecture.

---


### 128. [CAM-VFD: Cross-Attention Multimodal Video Forgery Detection](https://arxiv.org/abs/2605.17133)

**<font color=#1a73e8>作者：</font>** Hoda Osama Elkhodary, Sherin Mostafa Youssef, Marwa Elshenawy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Deepfake technologies and video manipulation tools poses a critical challenge to multimedia forensics, judicial evidence integrity, and information authenticity. Current detectors rely on single-modality signals, treating appearance, geometry, and motion independently. However, advanced generators maintain within-modality consistency while producing cross-modal contradictions, which are forensically discriminative but invisible to any single-modal detector. We propose CAM-VFD, a Cross-Attention Multimodal Video Forgery Detection framework that models cross-modal contradiction as a directional forensic signal. The framework uses a cross-attention fusion mechanism in which CLIP-based appearance representations serve as queries against VideoMAE motion features and MiDaS depth features, enabling the identification of contradictions between visual, temporal, and geometric evidence. We examine this design through cross-modal attention discrepancy analysis, observing statistically separable real and fake distributions ($p<0.001$, Cohen's $d=0.68$). Experimental results on two generative video benchmarks indicate consistent performance, with 95.31\% Top-1 accuracy on GenVidBench and 93.43\% accuracy, 90.63\% F1-score, and 96.56\% AUROC on GenVideo. Moreover, CAM-VFD demonstrates stable performance under compression, noise, blur, and adversarial perturbations, suggesting that cross-modal reasoning may improve robustness in media forensics. The code is publicly available at \url{this https URL}.

---


### 129. [Multilingual and Multimodal LLMs in the Wild: Building for Low-Resource Languages](https://arxiv.org/abs/2605.17152)

**<font color=#1a73e8>作者：</font>** Firoj Alam, Shammur Absar Chowdhury, Enamul Hoque Prince  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs are evolving from vision-language to tri-modality that see, hear, and read, yet pipelines and benchmarks remain English-centric and compute-heavy. The tutorial offers an overview of this emerging research area for multilingual multimodality across text, speech, and vision under limited data/compute budgets, synthesizing foundations, recent multilingual models (PALO, Maya), speech-text LLMs. We cover low-cost data creation/curation; adapter stacks for tri-modal alignment; culture-aware evaluation beyond English and hands on resources for fine-tuning a compact multilingual VLM and wiring a speech->text->LLM pipeline. The content will be delivered as an interactive half-day tutorial, designed for researchers and practitioners working on multilingual, multimodal AI in low-resource language settings.

---


### 130. [MADP: A Multi-Agent Pipeline for Sustainable Document Processing with Human-in-the-Loop](https://arxiv.org/abs/2605.17159)

**<font color=#1a73e8>作者：</font>** Diego Gosmar, Giovanni Zenezini  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Document processing automation remains a critical challenge in enterprise environments, where traditional manual approaches are labor-intensive and error-prone. We present MADP, a multi-agent architecture that addresses the challenge of automating document processing in enterprise settings by combining deep learning-based classification and parsing with large language model extraction, while maintaining accuracy through selective human validation. Our system integrates five specialized agents--Classificator, Splitter, Parser, Extraction, and Validator--with a Human-in-the-Loop (HITL) mechanism and a novel Prompt Fine Tuning with Feedback Inheritance (PFTFI) approach. The operational analysis on a production use-case scenario of 100,000 invoices per year indicates a potential reduction of Full-Time Equivalent (FTE) requirements by approximately 70%. Production deployment on 955 real-world documents processed through January 2026 achieves a 97.0% full-pipeline automation rate, with only 3% requiring non-AI fallback. Ablation evaluation on a stratified 100-document subset (5 documents per each of 20 supplier/document-type categories) demonstrates that the full MADP configuration with Human-in-the-Loop supervision attains 98.5% document-level accuracy. Additionally, we present a comprehensive sustainability analysis showing that our hybrid AI+HITL approach reduces CO2 emissions by 69%, energy consumption by 69%, and water usage by 63% compared to traditional manual processing. Benchmark comparisons of multiple LLM backends (Granite-Docling, Mistral-Small, DeepSeek-OCR) provide practical insights for deployment in production environments.

---


### 131. [Responsible Agentic AI Requires Explicit Provenance](https://arxiv.org/abs/2605.17169)

**<font color=#1a73e8>作者：</font>** Jinwei Hu, Xinmiao Huang, Qisong He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI is rapidly proliferating across diverse real-world domains such as software engineering, yet public trust has not kept pace. The central reason is that responsibility, despite being widely discussed, remains a subjective and unenforced concept, as no current agentic framework produces the quantifiable, traceable, and interventionable provenance needed to assign it when harm emerges from compositions no single party designed. We position that what is missing is not better benchmark-level evaluation but $\textbf{explicit provenance}$ across the full agentic lifecycle, which is the only viable basis for making responsibility computable and actionable. We advance this agenda along four axes: establishing $\textit{why}$ such provenance is a structural necessity by identifying responsibility gaps across sociotechnical dimensions, formalizing $\textit{what}$ it must encode through a causal attribution function and responsibility tensor, discussing $\textit{how}$ it can be made computable across four lifecycle layers with preliminary experiments showing that provenance is estimable and interveneable online before irreversible harm accumulates, and examining $\textit{who}$ bears responsibility through a concrete agentic incident. Explicit provenance is not a discretionary refinement but the necessary condition for responsible agentic AI, and no stakeholder across its ecosystem can afford to treat it as optional.

---


### 132. [TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks](https://arxiv.org/abs/2605.17170)

**<font color=#1a73e8>作者：</font>** Hanzhang Shen, Haoran Wu, Yiren Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic workloads have emerged as a major workload for LLM inference. They differ significantly from chat-only workloads, requiring long-context processing, the ability to handle multimodal inputs, and structured multi-turn interactions with tool calling capabilities. As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or reasoning. These axes capture distinct token behaviors and lead to different sensitivities to KV-cache compression. However, existing KV-cache quantization methods are typically homogeneous or exploit only heterogeneity on a single dimension, such as temporal proximity or modality, overlooking the interactions among them. To this end, we introduce TriAxialKV, a novel mixed-precision KV-cache quantization scheme that assigns each token a triaxial tag, calibrates per-tag sensitivity, and allocates INT2/INT4 bitwidths under a fixed memory budget. We implement TriAxialKV as an end-to-end serving system, comprising calibration, mixed-precision quantization and memory management, and custom fused Triton decode kernels. When using Qwen3-VL-32B-Thinking as a computer-use agent operating the OSWorld, TriAxialKV matches the accuracy of SGLang with BF16 KV cache while supporting 4.5$\times$ KV cache size and achieving 30% higher end-to-end throughput, when running on real GPU systems.

---


### 133. [OpenJarvis: Personal AI, On Personal Devices](https://arxiv.org/abs/2605.17172)

**<font color=#1a73e8>作者：</font>** Jon Saad-Falcon, Avanika Narayan, Robby Manihani 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personal AI stacks, like OpenClaw and Hermes Agent, are becoming central to daily work, yet they route nearly every query (often over sensitive local data) to cloud-hosted frontier models. Replacing frontier models with local models inside existing stacks does not work: swapping Claude Opus 4.6 for Qwen3.5-9B drops accuracy by 25-39 pp across personal AI tasks like PinchBench and GAIA. Existing stacks bundle agentic prompts, tool descriptions, memory configuration, and runtime settings around a specific cloud model. Only the prompts can be tuned, and state-of-the-art prompt optimizers close just 5 pp of the local-cloud gap on their own. This motivates a decomposed personal AI stack: one that exposes individual primitives which can be optimized individually or jointly to close the local-cloud gap. We present OpenJarvis, an architecture that represents a personal AI system as a typed spec over five primitives: Intelligence, Engine, Agents, Tools & Memory, and Learning. Each primitive is an independently editable field, making the stack end-to-end optimizable and measurable against accuracy, cost, and latency. Towards closing the local-cloud gap without surrendering local-model properties, OpenJarvis introduces LLM-guided spec search, a local-cloud collaboration in which frontier cloud models propose edits across the spec at search time, only non-regressing edits are accepted, and the resulting spec runs entirely on-device at inference time. With LLM-guided spec search, on-device specs match or exceed cloud accuracy on 4 of 8 benchmarks and land within 3.2 pp of the best cloud baseline on average. They also reduce marginal API cost by ~800x and end-to-end latency by 4x.

---


### 134. [CAREBench: Evaluating LLMs' Emotion Understanding by Assessing Cognitive Appraisal Reasoning](https://arxiv.org/abs/2605.17176)

**<font color=#1a73e8>作者：</font>** Zhaoyue Sun, Hainiu Xu, Andero Uusberg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotion understanding is a core capability for LLMs to interact effectively with humans, yet existing evaluation paradigms rely on discrete emotion label prediction and fail to capture the cognitive processes underlying emotion generation. Grounded in appraisal theory, we introduce CAREBench, the first benchmark with complete inferential chain annotations from both first- and third-person perspectives on real-world narratives, spanning appraisal reasoning, appraisal ratings, and multi-label emotion annotation. We propose a process-level evaluation framework and conduct systematic experiments across six LLMs organized around four research questions. We find that stronger models match or surpass human observers on certain tasks, yet fall short on appraisal reasoning and positive emotion recognition; performance across chain steps and sensitivity to appraisal interventions exhibit dissociations across models; and current models have not internalized the mechanisms needed to capture human subjective heterogeneity. These findings suggest that downstream emotion prediction metrics may overestimate LLMs' true emotion understanding, and CAREBench provides a foundation for more diagnostically informative evaluation of LLMs' affective cognitive capabilities.

---


### 135. [Substantial, Decomposable, and Invisible: Visual Context Misalignment in Instructional Videos for Physical Tasks](https://arxiv.org/abs/2605.17184)

**<font color=#1a73e8>作者：</font>** Yayuan Li, Chenglin Li, Jingying Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Instructional videos are the dominant medium for learning physical tasks, yet they rarely match the user's real-world visual context. Motor simulation and cognitive load theories predict this mismatch should matter, but we do not know (1) how much it could affect task completion, (2) which visual attributes are responsible, and (3) how users experience it. We conduct two complementary studies (56 participants, 86+ hours, four first-aid and culinary tasks) in which we use Wizard-of-Oz recordings to control the degree of visual alignment in instructional videos. In Study 1 (N=16), we prepare In-Context instructional videos (ICON) -- fully aligned with the user's visual perception -- to compare against business-as-usual Internet videos. ICON yields statistically significant improvements: 11.1% higher completion quality and 15.5% faster completion. Qualitative analysis reveals four visual context attributes responsible for the effect: Task Object Intrinsics, Task Object State, Environmental Context, and Observational Context. Study 2 (N=40) ablates each attribute by systematically misaligning one at a time from an otherwise fully aligned video, confirming all four produce consistent degradation. However, we find users fail to perceive the effect of single-attribute misalignment on task performance despite clear drops in objective measurement. Visual context misalignment is substantial, decomposable, and invisible to the user. These findings help understand the effect of visual context mismatch and how we should evaluate instructional videos for physical task guidance.

---


### 136. [PluRule: A Benchmark for Moderating Pluralistic Communities on Social Media](https://arxiv.org/abs/2605.17187)

**<font color=#1a73e8>作者：</font>** Zoher Kachwala, Bao Tran Truong, Rasika Muralidharan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media are shifting towards pluralism -- community-governed platforms where groups define their own norms. What violates rules in one community may be perfectly acceptable in another. Can AI models help moderate such pluralistic communities? We formalize the task as a multiple-choice problem, mirroring how human moderators operate in the real world: given a comment and its surrounding context, identify which specific rule, if any, is violated. We introduce PluRule, a multimodal, multilingual benchmark for detecting 13,371 rule violations across 1,989 Reddit communities spanning 2,885 rules in 9 languages. Using this benchmark, we show that state-of-the-art vision-language models struggle significantly: even GPT-5.2 with high reasoning performs only slightly better than a trivial baseline. We also find that bigger models and increased context provide marginal gains, and universal rules like civility and self-promotion are easier to detect. Our results show that moderation of pluralistic communities on social media is a fundamental challenge for language models. Our code and benchmark are publicly available.

---


### 137. [Multi-LLM Systems Exhibit Robust Semantic Collapse](https://arxiv.org/abs/2605.17193)

**<font color=#1a73e8>作者：</font>** Weiyi Kong, Shiyang Lai, Jinghua Piao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Whether machines can originate novel content has been debated for nearly two centuries, from Lovelace's assertion that no engine can "originate anything" to Turing's question of whether a machine can amplify ideas brought in from outside. Multi-large language model (LLM) systems, increasingly deployed for autonomous generation, reopen this question empirically. Here we show that such systems, operating in closed loops, exhibit semantic collapse: systematic convergence in semantic representations despite apparent lexical variation. Across model families, extended simulations of 200 to 1,000 rounds, the pattern remains consistent. Twelve intervention strategies, spanning decoding parameters, prompt design, agent composition, activation engineering, and reinforcement learning, fail to restore semantic diversity. Mechanistic analyses suggest that semantic collapse is not explained by alignment or conformity biases, but is consistent with intrinsic properties of autoregressive generation. Our results point to fundamental constraints in the ability of multi-LLM systems to sustain open-ended knowledge production in closed-loop settings.

---


### 138. [LLMs for automatic annotation of Mandarin narrative transcripts](https://arxiv.org/abs/2605.17205)

**<font color=#1a73e8>作者：</font>** Qingwen Zhao, Hongao Zhu, Yunqi He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistic annotation of transcribed speech is essential for research in language acquisition, language disorders, and sociolinguistics, yet remains labor-intensive and time-consuming. While Large Language Models (LLMs) have shown promise in automating annotation tasks, their ability to handle complex discourse-level annotation in non-English languages remains understudied. This study evaluates whether LLMs can reliably annotate narrative macrostructure-the hierarchical organization of story grammar elements-in spoken Mandarin, using the Multilingual Assessment Instrument for Narratives (MAIN) as a testbed. We compared four LLMs against trained human annotators on narratives produced by children, young adults, and older adults. The best-performing model achieved agreement with human raters (k=.794) approaching human-human reliability levels (k=.872) while reducing annotation time by 65%, whereas the locally deployable lightweight model performed substantially worse. Annotation difficulty varied systematically by macrostructure element type, with categories requiring subtle semantic differentiation posing persistent challenges. Furthermore, model reliability decreased on young adult narratives, which exhibited greater lexical variation, semantic ambiguity, and multi-element integration within single utterances. These findings suggest that LLMs can effectively support discourse-level annotation in non-English spoken corpora, while highlighting the continued need for human oversight in semantically complex tasks. Our prompt templates are open sourced for future use.

---


### 139. [ChemVA: Advancing Large Language Models on Chemical Reaction Diagrams Understanding](https://arxiv.org/abs/2605.17214)

**<font color=#1a73e8>作者：</font>** Mingyang Rao, Kehua Feng, Zhihui Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have revolutionized scientific text processing, they exhibit a significant capability gap when interpreting chemical reaction diagrams. We identify two fundamental bottlenecks restricting current systems: a Visual Deficit, where generic vision encoders struggle to resolve the strict topological connectivity of dense molecular graphs, and a Semantic Disconnect, where standard linear strings, such as SMILES, fail to effectively activate the model's latent chemical reasoning. To bridge these gaps, we propose the Chemical Visual Activation (ChemVA) framework, which employs a Visual Anchor mechanism to ground functional groups via hybrid-granularity detection, followed by a semantic alignment approach that translates visual features into entity names to maximize knowledge activation in LLMs. We evaluate our approach on OCRD-Bench, a newly constructed dataset featuring dense visual-semantic contexts and comprehensive reaction coverage to evaluate the full spectrum from recognition to reasoning. Extensive experiments on OCRD-Bench demonstrate that ChemVA achieves 92.0% structural recognition accuracy. By bridging visual and semantic bottlenecks, our framework delivers a consistent performance gain of approximately 20 percentage points across 9 diverse LLMs, enabling open-weight models to rival proprietary SOTA systems in complex chemical reasoning tasks.

---


### 140. [Artificial Intolerance: Stigmatizing Language in Clinical Documentation Skews Large Language Model Decision-Making](https://arxiv.org/abs/2605.17228)

**<font color=#1a73e8>作者：</font>** Jen-tse Huang, Didi Zhou, Faith Kamau 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in high-stakes domains such as clinical decision support and medical documentation. However, the robustness of these models against subtle linguistic variations, specifically stigmatizing language (SL) commonly found in human-authored clinical notes, remains critically under-explored. In this work, we investigate whether frontier LLMs inherit and propagate this human bias when processing clinical text. We systematically evaluate nine frontier LLMs across four stigmatized medical conditions, utilizing clinical vignettes injected with varying intensities and phenotypes of SL (doubt, blame, and maligning). Our results demonstrate that all evaluated models exhibit substantial bias, with clinical decision-making significantly skewed towards less aggressive patient management. Notably, we observe a high sensitivity to linguistic framing, where a single SL sentence is sufficient to alter model outputs, revealing a clear dose-response relationship. Furthermore, we evaluate standard prompt-based mitigation strategies, including Chain-of-Thought (CoT) reasoning and model self-debiasing. These approaches show limited efficacy; models struggle to explicitly identify SL while remaining implicitly influenced by it. Our findings expose a critical vulnerability in current LLMs regarding fairness and robustness in clinical NLP, underscoring the need for rigorous algorithmic guardrails to prevent the automation of health disparities.

---


### 141. [Fidelity Probes for Specification--Code Alignment](https://arxiv.org/abs/2605.17246)

**<font color=#1a73e8>作者：</font>** Ferhat Erata, Hao Zhou, Luke Huan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce fidelity probes: natural-language questions generated from a reference artifact with code-derived ground-truth answers, answered from a candidate specification. The fraction of agreeing probes, which we call the fidelity, decomposes into contradiction and coverage-gap rates that drive targeted spec edits to convergence. On a 15-program, roughly 12k-line COBOL benchmark (AWS CardDemo), we raise frozen-test specification fidelity from 0.63 to 0.94 over eight iterations, with the plateau location predicted by a two-state Markov fixed point $F^\dagger$ from just four iterations of rate data. Probes come from an LLM reading the code or from a static-analysis pipeline over its control-flow, data-flow, and system-dependence graphs, with a tunable mixture. A probe-resampling protocol with a frozen held-out set gives a Hoeffding-bounded overfitting discriminant; our measured train/test gap stays more than an order of magnitude below this envelope. Three graph-grounded mixtures lift fidelity by +16 to +30 points; cross-distribution evaluation shows the LLM and symbolic channels are empirically complementary. A cross-family generator sweep on five independent LLM lineages (Anthropic, DeepSeek, Google, Alibaba, OpenAI) confirms the convergence behaviour is not tied to any single model family: three of five non-Claude generators produce trajectories consistent with the Markov fixed-point prediction, and the frozen-test protocol actively falsifies the two generators whose probe distributions drift across iterations. The method applies to any pair of artifacts that are supposed to describe the same behaviour.

---


### 142. [CatalyticMLLM: A Graph-Text Multimodal Large Language Model for Catalytic Materials](https://arxiv.org/abs/2605.17254)

**<font color=#1a73e8>作者：</font>** Yanjie Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Property prediction and inverse structural design of catalytic materials are typically modeled as two independent tasks: the former predicts target properties from given structures, whereas the latter generates candidate structures according to desired properties. Although the decoupled paradigm facilitates the implementation of a ``generation--evaluation--screening'' workflow, the inconsistency between the generative model and the property prediction model in terms of representation spaces and training objectives can readily introduce data distribution shifts and evaluator bias, thereby limiting the stability of closed-loop optimization.
In this work, we propose QE-Catalytic-V2, a unified graph--text multimodal large language model for catalytic materials, which integrates property prediction and inverse design within the same model and shared representation space. Under this unified framework, QE-Catalytic-V2 can not only perform reliable property prediction by leveraging three-dimensional structures and textual information, but also generate and screen physically feasible CIF candidates conditioned on target properties, thereby forming a closed-loop optimization workflow of ``inverse design--prediction--screening--redesign.'' Experimental results demonstrate that this unified paradigm outperforms decoupled baselines on both catalytic relaxed-energy prediction and inverse design tasks, validating the effectiveness of jointly modeling property prediction and structure generation within a single multimodal model.

---


### 143. [CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean](https://arxiv.org/abs/2605.17255)

**<font color=#1a73e8>作者：</font>** Wentao Long, Yunfei Zhang, Chenyi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formal theorem-proving benchmarks enable mechanically verifiable evaluation of mathematical reasoning in large language models. However, existing benchmarks mainly focus on Olympiad-style problems and algebraic domains, leaving computational and applied mathematics underrepresented. We introduce CAM-Bench, a Lean 4 theorem-proving benchmark of 1,000 Lean proof targets in computational and applied mathematics, with coverage spanning optimization, numerical linear algebra, and numerical analysis. These problems are adapted from textbook exercises and often depend on locally introduced definitions, notation, algorithms, and elementary results. To construct CAM-Bench, we develop a dependency-recovery pipeline that reconstructs the local textbook context needed to state each problem faithfully. It then normalizes each problem into a standalone informal theorem and translates it into a Lean target. We validate the resulting formal problems through Lean compilation and semantic review, checking both formal correctness and semantic alignment with the original exercises. For each problem, we release the raw exercise, recovered context, normalized informal theorem, and final Lean target. CAM-Bench complements existing formal mathematics benchmarks by targeting applied mathematics problems that rely on textbook concepts and elementary theorems, many of which are not directly available as standard Mathlib4 lemmas. We evaluate widely used large language models and formalization agents on CAM-Bench, and analyze common failure modes in tracking local assumptions, applying elementary results, decomposing proofs, and maintaining long-horizon control in Lean.

---


### 144. [LiteFrame: Efficient Vision Encoders Unlock Frame Scaling in Video LLMs](https://arxiv.org/abs/2605.17260)

**<font color=#1a73e8>作者：</font>** Jihwan Kim, Nikhil Parthasarathy, Danfeng Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The fundamental challenge in scaling Video Large Language Models (Video LLMs) to long-form video lies in managing the explosion of visual-token context length. Existing strategies predominantly focus on "post-hoc" token reduction -- reducing visual tokens after feature extraction to alleviate the LLM's computational overhead. While these methods effectively reduce the number of visual tokens, we observe that the primary latency bottleneck then shifts from the LLM to the expensive per-frame processing of the vision encoder. To address this, we introduce LiteFrame, a strong, yet highly efficient video encoder backbone for Video LLMs. To train LiteFrame, we propose Compressed Token Distillation (CTD), a novel training framework that teaches a compact student vision encoder to directly predict information-dense, spatio-temporally compressed representations produced by a large teacher vision model, effectively bypassing redundant computation. When coupled with further Language Model Adaptation (LMA), this approach results in a new latency-accuracy Pareto frontier -- compared with InternVL3-8B, LiteFrame provides a 35% reduction in end-to-end latency while processing 8$\times$ more frames and improves average video understanding accuracy across multiple benchmarks. Our results demonstrate a new potential path to unlocking longer-form video understanding under fixed compute budgets.

---


### 145. [EgoIntrospect: An Egocentric Dataset and Benchmark for User-Centric Internal State Reasoning](https://arxiv.org/abs/2605.17262)

**<font color=#1a73e8>作者：</font>** Zeyu Wang, Chang Liu, Eduardus Tjitrahardja 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite extensive efforts on egocentric video datasets and benchmarks, understanding users' internal states, which is crucial for enabling seamless AI assistant experiences, remains largely overlooked. In this work, we introduce EgoIntrospect, the first egocentric dataset captured in user-driven scenarios with self-annotations that explicitly reveal users' interactive intentions with AI assistants. EgoIntrospect was collected using a cross-device setup, providing synchronized video, audio, gaze, motion, and physiological signals. It consists of 180 hours of recordings from 60 subjects, with an average recording duration of 3 hours per subject. Leveraging EgoIntrospect, we formalize a suite of tasks centered on user internal states, including affective experience, interactive intent, and cognitive memory. We further process the annotations to construct benchmarks that evaluate the ability of modern multimodal large language models to reason about users' internal states from egocentric observations. Experiments on our benchmark suggest that existing multimodal large language models struggle to effectively leverage multimodal signals to infer users' subjective internal states. The dataset and annotations will be made publicly available to advance research in egocentric vision and wearable AI assistants. Project page: this https URL

---


### 146. [OProver: A Unified Framework for Agentic Formal Theorem Proving](https://arxiv.org/abs/2605.17283)

**<font color=#1a73e8>作者：</font>** David Ma, Kaijing Ma, Shawn Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent progress in formal theorem proving has benefited from large-scale proof generation and verifier-aware training, but agentic proving is rarely integrated into prover training, appearing only at inference time. We present OProver, a unified framework for agentic formal theorem proving in Lean 4, in which failed proof attempts are iteratively revised using retrieved compiler verified proofs and Lean compiler feedback. OProver is trained through continued pretraining followed by iterative post-training: each iteration runs agentic proving, indexes newly verified proofs into OProofs and the retrieval memory, uses repair trajectories as SFT data, and uses unresolved hard cases for RL. OProofs is built from public Lean resources, large-scale proof synthesis, and agentic proving traces, containing 1.77M Lean statements, 6.86M compiler-verified proofs, and serialized trajectories with retrieved context, failed attempts, feedback, and repairs. Across five benchmarks, OProver-32B attains the best Pass@32 on MiniF2F (93.3%), ProverBench (58.2%), and PutnamBench (11.3%), and ranks second on MathOlympiad (22.8%) and ProofNet (33.2%) more top placements than any prior open-weight whole-proof prover.

---


### 147. [LEAP: Learnable End-to-End Adaptive Pruning of Large Language Models](https://arxiv.org/abs/2605.17289)

**<font color=#1a73e8>作者：</font>** Mohammad Mozaffari, Younes Hourri, Mohammad Rastegari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unstructured sparsity is now natively accelerated by recent GPU kernels and dataflow hardware, shifting the bottleneck from inference execution to the pruning algorithm. State-of-the-art methods for unstructured LLM pruning are layer-wise surrogates derived from the Optimal Brain Surgeon principle, and they sacrifice end-to-end accuracy, especially under aggressive sparsity. End-to-end alternatives such as MaskLLM and PATCH show that learnable masks can close this gap, but their categorical-over-patterns parameterization scales with the number of valid masks per row and does not port to the unstructured setting. We introduce LEAP, which replaces this intractable parameterization with a per-weight Bernoulli-via-Gumbel- sigmoid relaxation that makes end-to-end unstructured mask learning tractable. Across five LLM families from 0.5B to 8B parameters at 50% and 60% sparsity, LEAP improves six-task average zero-shot accuracy by +2.59 points on average over ADMM, the best layer-wise baseline in our sweep.

---


### 148. [Step-wise Rubric Rewards for LLM Reasoning](https://arxiv.org/abs/2605.17291)

**<font color=#1a73e8>作者：</font>** Weichu Xie, Haozhe Zhao, Wenpu Liu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) is widely used to improve reasoning in large language models, but rewards only final-answer correctness with no supervision over intermediate steps. Rubric-based methods such as Rubrics as Rewards (RaR) introduce finer-grained supervision by scoring rollouts against structured criteria, yet the rubric scores are still aggregated into a single scalar applied to the entire response, causing three weaknesses: loss of multi-criterion structure, uniform supervision of correct and incorrect steps, and reward hacking through unbounded self-correction. On 1,000 problems, we find 18.2% of steps in correct-answer responses are wrong yet positively rewarded, while 49.9% of steps in incorrect-answer responses are correct yet penalized. We introduce Step-wise Rubrics as Rewards (SRaR), an RLVR framework that (i) uses an LLM judge to attribute each rubric item to a specific reasoning step, (ii) normalizes per-step rubric scores across rollouts so only steps whose quality varies produce a learning signal, and (iii) combines the per-step reward with the outcome reward through a decoupled advantage estimator that keeps the outcome baseline stable. We further build a 16K-problem rubric dataset by contrastively distilling rubric items from correct and flawed reasoning paths sampled from a strong model. Across six mathematical reasoning benchmarks, SRaR improves average accuracy over RaR by 3.57 points on Qwen3-8B and 2.75 points on Qwen3-32B, raises the Faithful Reasoning Rate on AIME 2025 from 34.5% to 46.7%, and reduces self-correction looping from 48.1% to 26.5%.

---


### 149. [MetaCogAgent: A Metacognitive Multi-Agent LLM Framework with Self-Aware Task Delegation](https://arxiv.org/abs/2605.17292)

**<font color=#1a73e8>作者：</font>** Chenyu Wang, Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems have shown promise for solving complex tasks through agent collaboration. However, existing frameworks assign tasks based on predefined roles without considering whether an agent can accurately assess its own competence boundaries, leading to overconfident execution on tasks beyond its expertise. Inspired by metacognition theory from cognitive science, we propose MetaCogAgent, a multi-agent LLM framework where each agent is equipped with a Metacognitive Self-Assessment Unit that evaluates task-capability alignment before execution. The framework introduces three contributions: (1) a self-assessment mechanism that estimates per-task confidence by combining verbalized uncertainty with historical capability profiles; (2) an adaptive delegation protocol that routes low-confidence tasks to better-suited agents through cross-agent evaluation; and (3) a capability boundary learning module that iteratively refines each agent's competence model via cybernetic feedback. Experiments on our constructed MetaCog-Eval benchmark (700 tasks across 5 cognitive dimensions) demonstrate that MetaCogAgent achieves 82.4% task accuracy -- 8.7% above the best routing baseline -- while using 5% fewer API calls than AutoGen and 34% fewer than ensemble voting. Ablation studies confirm that each metacognitive component contributes to overall system performance.

---


### 150. [DISA: Offline Importance Sampling for Distribution-Matching LLM-RL](https://arxiv.org/abs/2605.17295)

**<font color=#1a73e8>作者：</font>** Shaobo Wang, Yujie Chen, Yafeng Sun 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern reasoning agents are increasingly evaluated on their ability to generate multiple valid solution paths, plans, or tool-use traces for a given input. Standard reward-maximizing RL tends to collapse onto the most easily reinforced high-reward mode, whereas distribution-matching RL aims to allocate probability mass across the entire reward-shaped solution set. Achieving this objective requires computing a prompt-dependent partition function over the trajectory space. Because existing distribution-matching methods learn this partition function online alongside the policy, calibration errors in the partition function directly distort policy updates and remain impossible to diagnose independently. We introduce DISA, short for Decoupled Importance-Sampled Anchoring, which moves this calibration problem outside the RL loop. DISA draws proposal trajectories offline, estimates the partition function via importance sampling, and freezes the resulting partition-function estimate before policy optimization begins. This decoupling preserves the distribution-matching objective while strictly separating partition-function estimation from policy learning in data, gradients, loss, and diagnostics. Empirically, on two open-weight backbones across six math and three code benchmarks, DISA matches or exceeds the online-coupled distribution-matching baseline FlowRL, outperforms rewardmaximization baselines GRPO and GSPO on math averages, and exceeds LoRASFT distillation by up to 13.8 Mean@8 points on the same offline trajectories. An LLM-as-judge evaluation further shows that DISA retains substantially more strategy-level diversity than reward-maximization baselines, and sensitivity studies on the proposal strength and inverse temperature follow the bias-variance pattern predicted by the analysis.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-346](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
