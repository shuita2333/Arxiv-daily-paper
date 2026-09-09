# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-483](./part-10.md)

---

### 351. [Drive by Hindsight and Foresight: Tool-Grounded Synergistic Reasoning over Hierarchical Memory for Autonomous Driving](https://arxiv.org/abs/2609.08217)

**<font color=#1a73e8>作者：</font>** Baojie Chen, Zijun Jia, Jing Zhong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> VLMs have shown promise for autonomous driving, yet still suffer from hallucination, weak spatio-temporal perception, and limited generalization. Recent methods improve reasoning and decision-making through CoT explanations, retrieval-augmented generation or the static injection of tool outputs. Although these mechanisms enrich the context, the model neither proactively perceives scene information nor accumulates experience after answering. To overcome these limitations, we present, to our knowledge, the first synergistic framework that tightly couples hierarchical memory with proactive tool invocation in a closed reasoning loop. Our contributions are threefold. (i) Hierarchical Driving Memory: a scene-level short-term memory maintains the dynamic scene state, and an evolving long-term memory retrieves reusable experience and tool strategies. (ii) Memory-Tool Synergistic Reasoning Framework: guided by the scene state and retrieved experience, the model adaptively invokes tools to refine its reasoning at inference time and consolidates reusable experience into a long-term memory pool offline. (iii) Data Generation and Two-stage Training Pipeline: verified memory-tool trajectories built by multi-step teacher rollout are used to train with SFT and GRPO. Our 7B model reaches an overall reasoning score of 80.03 and MCQ accuracy of 79.09% on DriveLMM-o1, surpassing the strongest baseline by 7.74 MCQ points and generalizes strongly across benchmarks. Notably, ablation and analysis studies validate the effectiveness of each component and further reveal the complementary roles of hierarchical memory. Short-term memory strengthens spatio-temporal understanding, improving STSBench accuracy by 24.2 points, while offline long-term memory consolidation yields an additional 3.57-point MCQ gain with all parameters frozen, demonstrating continual self-evolution through accumulated driving experience.

---


### 352. [TTGBench: Benchmarking Topological Evolution and Semantic Drift in Text-attributed Temporal Graphs](https://arxiv.org/abs/2609.08226)

**<font color=#1a73e8>作者：</font>** Longfei Ma, Zemin Liu, Fei Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal graph learning models the evolution of dynamic systems, where both structural interactions and semantic states change over time. However, existing benchmarks primarily emphasize structural evolution via temporal link prediction (TLP), while support for semantic evolution remains limited. Although temporal node classification (TNC) is sometimes included, it is typically restricted to simplistic binary settings that fail to capture realistic semantic drift. Moreover, commonly used datasets exhibit high link repetition, leading to inflated performance estimates and obscuring true model capability. To address these limitations, we introduce \textbf{TTGBench}, a new benchmark that jointly evaluates structural and semantic evolution. TTGBench comprises six real-world, text-rich datasets characterized by \emph{Dual Volatility}, enabling rigorous and fair evaluation of existing models. Notably, it is the first benchmark to support both multi-class and multi-label TNC, filling a critical gap in evaluating temporal semantic drift. We conduct a comprehensive evaluation of 17 state-of-the-art methods across Temporal Graph Neural Networks (TGNNs) and Large Language Model (LLM)-based paradigms. The results reveal a clear \emph{capability divide} between the two paradigms: TGNN-based methods excel at structural prediction but fail at semantic tracking, whereas LLM-based predictors show the opposite trend. Through in-depth analysis, we uncover their fundamental limitations and provide insights for developing more comprehensive temporal graph models.

---


### 353. [SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale](https://arxiv.org/abs/2609.08228)

**<font color=#1a73e8>作者：</font>** Dawei Fu, Cheng Jiang, Sitian Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern LLM agents increasingly rely on reusable skills, yet as skill libraries scale to thousands of entries, effective retrieval becomes a bottleneck. Graph-of-Skills (GoS) addresses this challenge by exploiting dependency-aware graph structure for scalable skill retrieval, while SkillDAG further demonstrates that skill graphs can accumulate execution-backed structure online. However, these approaches leave open whether historical execution traces can be systematically distilled into a better retrieval graph that generalizes to unseen tasks. We present Self-Evolving Graph-of-Skills (SE-GoS), a training-free framework that evolves an existing GoS graph from execution traces while preserving the original retrieval pipeline. SE-GoS performs three complementary updates: topology evolution that discovers and prunes skill relationships from execution evidence, edge-weight evolution that reinforces retrieval-relevant relationships based on historical effectiveness, and description evolution that optimizes retrieval-facing skill descriptions using execution feedback. Across three LLMs on SkillsBench, SE-GoS consistently improves task reward while reducing input tokens relative to full skill loading, with gains varying across model families. In a representative setting, one evolution round improves reward from 52.4\% to 59.4\% while reducing input tokens by approximately one-third relative to full skill loading, and the resulting graph transfers to a disjoint held-out split with a 5.4-point improvement over the static GoS baseline. These results show that skill graphs can be improved from execution experience without model training, changes to the retrieval algorithm, or modifications to skill content, turning a static retrieval graph into an evolving retrieval infrastructure.

---


### 354. [CS-CLIP: Compositional Scene Graph-guided CLIP for Robust Compositional Reasoning](https://arxiv.org/abs/2609.08242)

**<font color=#1a73e8>作者：</font>** SeongJun Jeong, Minjoon Jung, Woo Suk Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) demonstrate strong performance across compositional reasoning benchmarks, which require reasoning over semantic perturbations of objects, attributes, relations, and their interactions. However, our controlled analysis reveals that existing compositionality-aware VLMs exhibit element-specific biases, often underperforming vanilla CLIP on certain compositional elements. To address this, we propose Compositional Scene Graph-guided CLIP (CS-CLIP), which uses scene graphs to identify compositional elements and construct structured negatives via selective masking. We further retain negatives that are most contradictory to the original caption, forcing the model to rely on compositional structure rather than surface cues. CS-CLIP achieves state-of-the-art compositional reasoning with robust performance across compositional elements. It also preserves general vision-language capabilities such as cross-modal retrieval and downstream visual reasoning, while requiring fewer training samples than prior methods.

---


### 355. [Agentic ML Exploration (A-MLE) for Ads Ranking](https://arxiv.org/abs/2609.08248)

**<font color=#1a73e8>作者：</font>** Erwin Gao, Vinodh Kumar Sunkara, Jingyi Guan 等 39 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern industrial ads ranking stacks are increasingly bottlenecked not by model capacity or training compute, but by the throughput of human ML iteration - the cycles of research, implementation, training, debugging, evaluation, and launch required to surface a single statistically significant improvement. A typical ranking stack contains numerous differentiated models with heterogeneous data, architectures, and infrastructure constraints, and each cycle takes days to weeks of senior engineer attention per model. As a result, techniques that have proven effective on one model diffuse into others slowly and unevenly, leaving substantial recoverable signal unexplored. We present Agentic ML Exploration (A-MLE), an autonomous LLM-agent system that systematically explores ML techniques across a portfolio of ads ranking models. A-MLE decomposes ML iteration into five stages involving hypothesis generation, exploration strategy, experiment execution, result analysis and shared knowledge substrate which are orchestrated by a single agent that invokes domain-specific skills and agentic workflows against a sandboxed execution layer, with human-in-the-loop checkpoints at each stage boundary. We deploy A-MLE across a representative set of large-scale ads ranking models and evaluate it along a tiered capability framework (tool availability, autonomous workflow execution, and open-ended exploration). We further report a controlled cross-LLM study using a fixed agent loop, which surfaces qualitative differences in execution reliability and exploration aggressiveness across the Claude Sonnet, Gemini, and GPT families. We discuss failure modes and the design choices that govern reliability. Our findings suggest that agentic exploration is a practical force multiplier for ML engineers in industrial recommenders, especially for the long tail of models that rarely receive expert attention.

---


### 356. [ACEA: An Adversarial Co-Evolution Arena for Head-to-Head Red-Team and Blue-Team LLM Testing](https://arxiv.org/abs/2609.08256)

**<font color=#1a73e8>作者：</font>** Yi Ting Shen, Kentaroh Toyoda, Alex Leung  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated red-team attacks and blue-team defenses for large language models (LLMs) are advancing quickly. However, attackers and defenders are built and tested in isolation, and the resulting scores are hard to trust. To tackle this, we present ACEA (Adversarial Co-Evolution Arena), a platform that connects a pluggable red-team adapter and a pluggable blue-team adapter to a shared target LLM and scores their attack and defense rates with an LLM judge. ACEA contributes four components. First, a pluggable, model-agnostic arena. Any red or blue project connects over a minimal HTTP protocol, which we call the ACEA Standard Adapter Protocol (ASAP). It can be written in any language, and a project that exposes nothing but the protocol is a full participant. Second, an evaluation methodology built for adversarial rounds. Seeding the target with canonical secrets gives verifiable ground truth that separates real leakage from hallucination. We also send each attack to the target even when the defense blocks it, which measures the attack's raw potency independently of whether it was stopped. Together these yield a per-round decomposition of attack strength and defense effectiveness. Third, a real-time, game-style visualization with a detailed end-of-battle report that localizes each failure. The evaluation thus becomes an actionable signal for improving a red or blue project. Fourth, an optional in-context improvement loop that turns each round's outcome into advisory hints for the next. An adapter can then adapt across rounds without keeping state, provided it reads the hints. We describe the design of ACEA and the metrics through which red and blue teams are scored head to head.

---


### 357. [Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems](https://arxiv.org/abs/2609.08258)

**<font color=#1a73e8>作者：</font>** Yi Ting Shen, Kentaroh Toyoda, Alex Leung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running language-model agents depend on persistent memory. Many agent-memory systems preserve history through soft revocation: a contradicted fact is marked invalid and retained rather than deleted. However, whether that mark is enforced at retrieval time is unexamined. In this paper, we measure five such systems: we load each with a revoked policy and its replacement, track whether the revoked fact is returned at retrieval and whether the agent then acts on it across nine policy scenarios and nine models, and score every trial under six defense conditions. We find that no system enforces revocation by default: the revoked fact is returned wherever the revocation label is visible to the retrieval layer, outranks its replacement, and leads agents to the unsafe action. Based on these findings, we develop a guard that sits between the agent and any memory backend and withholds records that are revoked or conflict with their replacement.

---


### 358. [Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented Generation](https://arxiv.org/abs/2609.08267)

**<font color=#1a73e8>作者：</font>** Runsong Jia, Zhen Fang, Mengjia Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hallucination detection is crucial for large language models (LLMs), as hallucinated content creates significant barriers in applications requiring factual accuracy. Current detection methods mainly depend on internal signals like uncertainty and self-consistency checks, using the model's pre-trained knowledge to identify unreliable outputs. However, pre-trained knowledge may become outdated and has coverage limitations, especially for specialized or recent information. To address these limitations, retrieval-augmented generation (RAG) has emerged as a promising solution by retrieving relevant evidence at inference time, grounding outputs beyond the model's parametric knowledge. In this paper, we target a critical and practical learning problem RAG-based hallucination detection (RHD), where RAG is employed to enhance hallucination detection by addressing information updating challenges. To address RHD, we propose a novel method Evidence-Aligned Entity Verification (EAEV), which detects entity-level hallucinations by leveraging RAG to align generated entities with retrieved evidence contexts. Specifically, EAEV evaluates entity-evidence alignment through three complementary dimensions and introduces counterfactual stability analysis to ensure robust alignments under evidence perturbations. Experiments across multiple RAG benchmarks demonstrate that EAEV achieves consistent improvements over existing methods with strong generalization capabilities.

---


### 359. [MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging](https://arxiv.org/abs/2609.08273)

**<font color=#1a73e8>作者：</font>** Junxi Wang, Te Sun, Jiayi Zhu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory systems have demonstrated significant potential in long-term dialogue, personalized assistants, and video understanding. However, continuously accumulated memory introduces substantial storage and retrieval costs during inference. To address this issue, we propose \textbf{MemForest}, a general memory compression framework adaptable to various agent memory systems. Specifically, MemForest partitions historical memory into event-centric units by leveraging global semantic similarity and local temporal continuity. For each unit, it constructs a maximum spanning tree, termed an EventTree, and progressively merges redundant memory nodes by selecting high-weight edges, reducing storage overhead. Furthermore, we introduce an anchor-guided propagation retrieval mechanism that retrieves relevant memory nodes from the temporal neighborhoods of key nodes, improving retrieval accuracy. Extensive experiments demonstrate the effectiveness of MemForest. Under the unimodal Mem0 framework, MemForest retains \textbf{97.1%} of the original performance while compressing \textbf{50%} of historical memory across three benchmarks (LoCoMo, LongMemEval, and PersonaMem), achieving a \textbf{1.89x} retrieval speedup. Under the multimodal M3-Agent framework, it preserves \textbf{99.7%} of the original performance with a \textbf{50%} compression ratio across two benchmarks (M3-Bench-robot and M3-Bench-web), achieving a \textbf{2.24x} retrieval speedup. \textcolor{RoyalBlue}{\textit{Our code is available at [this https URL.}}](this https URL.}})

---


### 360. [What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory](https://arxiv.org/abs/2609.08279)

**<font color=#1a73e8>作者：</font>** Chen Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory systems must discard stored information when their history exceeds a fixed token budget. Existing budget-accuracy frontiers quantify the resulting loss in accuracy, but do not distinguish irreversible losses caused by eviction from recoverable retrieval failures. We introduce the restore counterfactual, a per-question paired intervention that reinstates the question's gold evidence in the read-time context and reruns the same reader. Combining the change in correctness with whether the evidence was retained after eviction classifies each oracle-answerable error as recoverable, irreversible, or residual; in the residual case, the answer remains incorrect after restoration. We evaluate FIFO, random, redundancy-aware, and LLM-importance eviction on LongMemEval-S at three budgets and under two retrieval regimes, using GPT-4o-mini as the primary reader and judge and GPT-5.4-mini as a robustness reader. Under top-k retrieval at an 80k-token budget, the irreversible share among errors corrected by restoration is 0.67-0.73 for FIFO, random, and redundancy-aware eviction, compared with 0.60 for LLM-importance. At 8k tokens, it reaches 1.00 for all four policies. Recoverable errors occur under top-k retrieval at 80k tokens but are absent under forced-gold injection by construction, so budget-accuracy results are not directly comparable unless the retrieval regime is reported. An exploratory matched-accuracy analysis detects no difference in irreversible rate among accuracy-matched policy pairs at a resolution of 1.2-6 percentage points. The same analysis detects the deliberately destructive control. To our knowledge, this is the first per-item, per-question restore-counterfactual audit of eviction for external agent-memory stores on a standard conversational benchmark.

---


### 361. [LEBGen: An LLM-Enhanced Bayesian Network Framework for Few-Shot Travel Survey Data Generation](https://arxiv.org/abs/2609.08288)

**<font color=#1a73e8>作者：</font>** Zijian Shen, Bin Zhou, Jiguang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Travel survey data are essential for transportation planning and travel behavior analysis, yet collecting large-scale representative samples is costly and time-consuming. A practical alternative is to generate synthetic survey records from a few-shot sample. However, such samples provide incomplete coverage of heterogeneous traveler groups and insufficient evidence for recovering the complex dependencies between demographic characteristics and travel behavior. Existing approaches have complementary limitations. Probabilistic generative models such as Bayesian networks (BNs) offer explicit distributional control, but structures learned from few-shot samples may omit meaningful dependencies or retain spurious ones. Large language models (LLMs) can help address these difficulties in BN structure learning by providing behavioral knowledge that complements the limited statistical evidence. We therefore propose LEBGen, an LLM-enhanced BN framework that uses this knowledge to refine network structure for few-shot travel survey data generation. Specifically, the LLM first identifies traveler personas from demographic attribute and travel behavior statistics, then recovers dependencies missed by the persona-augmented BN structure and prune spurious ones. The refined BN is parameterized exclusively from the observed data to generate synthetic records. Under a 2% few-shot setting on the 2022 Hong Kong Travel Characteristics Survey, LEBGen reduces the mean marginal Jensen-Shannon divergence from 0.0671 to 0.0091 and the mean absolute Cramer's V error by 14.3% over the best-performing baseline, substantially improving both distributional and dependency fidelity.

---


### 362. [Human-Centric Image Captioning with Subject-Centered Spatial Understanding](https://arxiv.org/abs/2609.08300)

**<font color=#1a73e8>作者：</font>** Bozhou Li, Jiahang Zhang, Yue Ding 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While multimodal large language models (MLLMs) achieve remarkable performance on generic image captioning, they frequently suffer from structural hallucinations in human-centric scenarios. Accurately modeling human subjects is foundational for critical downstream applications, such as accurate avatar/video/image generation and fine-grained human action understanding. However, these tasks require highly precise subject-centered spatial grounding, such as distinguishing egocentric left/right laterality and maintaining correct anatomical-object bindings. Although catastrophic for structural integrity, these localized spatial inversions are often overshadowed by overall descriptive metrics in existing benchmarks. To systematically expose and quantify this bottleneck, we introduce SPACE (Subject-centric Poses, Appearance, and Characteristics Evaluation), a benchmark designed to evaluate subject-centered spatial understanding. On SPACE, we reveal that despite strong generic perception, current MLLMs consistently fail to ground descriptions in the subject's intrinsic frame of reference. To bridge this gap, we propose a specialized data construction and alignment pipeline. We first extract structured spatial hints from fine-grained body-part localization to guide a two-stage caption rewriting process, yielding highly spatially-faithful training data. Furthermore, we design a rubric-based reward for Group Relative Policy Optimization (GRPO) that explicitly penalizes structurally critical spatial errors during alignment. Extensive experiments on SPACE demonstrate our framework significantly improves human-centric caption quality, particularly in subject-centered spatial reasoning, achieving performance competitive with strong closed-source models. Our benchmark and code are available at this https URL.

---


### 363. [HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving](https://arxiv.org/abs/2609.08306)

**<font color=#1a73e8>作者：</font>** Han Jin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce HoneyRoute, an inference-serving layer that detects whether an incoming request is malicious and, if so, routes it to a dedicated honeypot model, shielding production while the adversary's interaction is continuously harvested for intelligence. Existing defenses embed traps inside model memory or rebuild deception at the protocol layer, leaving the serving tier unprotected and feeding nothing back into detection. HoneyRoute couples (i) a streaming router (a frozen 0.8B-embedding backbone with per-domain MLP heads), (ii) a dual-implementation honeypot (a rule/prompt-engineered code honeypot or a dedicated same-family replica), and (iii) an analysis loop that converts trapped interactions into attacker fingerprints for router retraining. On a production trace plus a seven-domain attack corpus, the router reaches F1=.911 at 38 ms median added latency, matching 96% of a two-tier guard-LLM cascade's F1 at 1/385 of its latency with 0% evasion under 13 adversarial transformations; diverting the malicious share cuts production-model token consumption under concurrent flooding with real GCG-suffix payloads by 97.8%; the trained replica agrees with the production model on 92.9% of benign holdout requests, while naive unconditional bait injection collapses to 7.6% and selective camouflaged injection recovers to 88.9%, mapping the recoverable fidelity-traceability frontier; and a loop-trained correction head cuts misrouting of legitimate security research 9x while raising detection F1 to .933.

---


### 364. [From Glance to Scrutiny: Progressive Distortion Reasoning for Fine-Grained Image Quality Assessment](https://arxiv.org/abs/2609.08316)

**<font color=#1a73e8>作者：</font>** Aoting Zhang, Mingze Gao, Dongbao Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal large language models (MLLMs) have demonstrated significant potential in image quality assessment (IQA) by bridging visual perception with descriptive evaluations. However, existing approaches mainly focus on holistic quality prediction, often functioning as black boxes that provide limited insight into where distortions occur and how they affect perceived quality, hindering fine-grained analysis of localized and heterogeneous degradations. We propose GS-IQA, a framework that reformulates IQA as a progressive Where--What--How diagnosis, emulating the human perceptual process from an initial glance to closer scrutiny. Since a severity judgment is meaningful only for a correctly localized and recognized region, we realize this progression through a two-stage reinforcement learning paradigm that respects such dependencies: the glance stage uses a perception-gated reward to establish where degradations lie and what they are, activating severity feedback only once both are correct, while the scrutiny stage introduces online reward-conditioned degradation generation to synthesize hard examples targeted at the model's perceptual bottlenecks, sharpening its discrimination of subtle severity variations. To enable systematic evaluation, we construct Diag-Bench, a region-level IQA benchmark of about 25K curated samples spanning 12 distortion types and five ordinal severity levels. Extensive experiments show that GS-IQA consistently surpasses state-of-the-art methods in distortion localization, recognition, and severity estimation, and that its diagnostic representations transfer effectively to conventional global quality prediction across diverse external benchmarks. Code and data will be released.

---


### 365. [Tracing Stereotypes from Representation to Output in Multilingual LLMs](https://arxiv.org/abs/2609.08322)

**<font color=#1a73e8>作者：</font>** Ariun-Erdene Tumurchuluun, Yusser Al Ghussin, Pinzhen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual LLMs show stereotype-related behavior that varies across languages, but behavioral scores do not show where the relevant information is represented or how it affects the output. To investigate these internal mechanisms, we compare linear probing, attribution patching, sparse autoencoders (SAEs) and feature ablation in Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B. Probe performance peaks substantially earlier than attribution in all three models, with a separation of 36-53% of model depth. Retained Llama-Scope features often match the social category on which they were selected and form recurring semantic families, but their lexical alignment and ablation effects vary across SAE suites. Only 6-18% of evaluated residual-stream features have language-agnostic effects under our criterion, and none are category-agnostic. Language-agnostic features have larger mean ablation effects in Llama-Scope, but this pattern does not repeat in the other SAE suites. Decodability, output influence, and cross-lingual ablation effects therefore need to be measured separately.

---


### 366. [Do Input-Level Defenses Transfer to Observation-Level Attacks on VideoLLMs?](https://arxiv.org/abs/2609.08331)

**<font color=#1a73e8>作者：</font>** Bangshuo Zhu, Wei Song, Yuxin Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (VideoLLMs) are increasingly deployed in safety-critical applications such as content moderation and video analytics. To process long videos efficiently, VideoLLMs rely on frame sampling, token compression, and modality fusion, which together form an observation pipeline that reduces the raw video to a compact internal representation. Recent observation-level attacks exploit this pipeline to prevent the model from perceiving harmful content, yet no defense has been explicitly designed for this threat. We introduce DefTEval, a controlled evaluation framework that systematically assesses whether input-level adversarial defenses, which operate on the pixel content of already-sampled frames, can mitigate observation-level attacks. Across five VideoLLMs, eleven representative defenses, and five attack types, we find that input-level defenses offer limited and inconsistent protection, with harmful detection rates frequently near zero. Critically, defenses fail even against attacks that embed harmful signals in every sampled frame, indicating that the bottleneck extends beyond sampling omission to the suppression of signals that do enter the model. Token compression discards localized features, and modality fusion systematically down-weights weakened visual signals. Furthermore, defense effectiveness is dominated by model architecture rather than by the defense method itself, and detection rates vary drastically across content categories, exposing structural weaknesses in temporal reasoning. These findings demonstrate that securing VideoLLMs requires system-level robustness mechanisms spanning sampling-aware coverage guarantees, token-level preservation of safety-relevant features, and modality-balanced fusion.

---


### 367. [Distillation as Probability Transport: Routed On-Policy Distillation](https://arxiv.org/abs/2609.08337)

**<font color=#1a73e8>作者：</font>** Tianle Xia, Lingxiang Hu, Yiding Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) transfers teacher knowledge on student-generated trajectories, but efficient sampled objectives reduce the teacher distribution to scalar credit on individual tokens. Such credit indicates whether a token should gain or lose probability, yet leaves the corresponding redistribution unspecified. We recast OPD as teacher-guided probability transport and propose RouteOPD (Routed On-Policy Distillation), which decomposes local teacher--student disagreement into student-excess sources and teacher-deficit destinations and couples them into explicit transport pairs. RouteOPD optimizes pairwise log-odds toward jointly realizable targets obtained from a bounded teacher potential, while adapting the transport budget to the concentration of teacher demand. This formulation directs updates toward teacher-preferred destinations and controls their magnitude within a single transport operator. Experiments across four teacher--student settings and four mathematical-reasoning benchmarks demonstrate that RouteOPD consistently outperforms sampled reverse-KL OPD, with improvements accompanied by higher routing fidelity and lower background leakage. These results demonstrate the effectiveness of explicitly modeling probability transport in on-policy distillation.

---


### 368. [TV-Regulated OPD: Direction Matters in On-Policy Distillation](https://arxiv.org/abs/2609.08341)

**<font color=#1a73e8>作者：</font>** Han Xiao, Yifan Niu, Dongyi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) facilitates the transfer of knowledge from domain expert to student in the post-training phase of Large Language Models (LLMs). However, the supervision signals in mainstream OPD methods suffer from high variance and noise which is generally instable during training. In this work, we systematically investigated what really matters to the performance and the fundamental mechanisms behind the instability during training. We found that retaining only the sign of token-level advantages is sufficient to achieve the performance comparable to standard OPD. Meanwhile, smoother and bounded advantages can stabilize the training process without sacrificing its performance. These motivated us to shape the advantages using the Total Variation (TV) and propose a robust TV regulated On-Policy Distillation (TV-OPD) method. Benefiting from the bounded and diminished advantages, TV-OPD exhibits stable training dynamics and steady late-stage performance. We conducted comprehensive experiments and found that, across various settings, TV-OPD consistently achieved better performance and lower variance in the late-stage of training.

---


### 369. [VeriScene: Reconstructing Crime Scenes from Legal Evidence via World-Model Agent](https://arxiv.org/abs/2609.08342)

**<font color=#1a73e8>作者：</font>** Kevin Chuanpu Fu, Yongsen Zheng, Zee Kin Yeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models take multimodal inputs like text, photos, and diagrams to generate dynamic scenes in accordance with the laws of physics, thus opening a compelling application: fusing multimodal legal evidence to re-create a crime scene and re-enact how an offence could have been committed. However, feeding the raw, unorganized evidence into a world model fails in forensic use: it silently drops evidence, glosses over contradictory testimony, and produces motion that violates the evidentiary record. This paper presents VeriScene, an agent that orchestrates the world model: it reconstructs crime scenes from forensic photographs and witness statements of varying reliability, keeping every claim traceable to evidence and every motion physically plausible. VeriScene iteratively fuses the evidence into a cited narrative under an auditing loop, verifies the hypothesized dynamics via probe rollouts in the world model with corrective constraint injection, and renders the offence as a re-enactment video from a fused keyframe. On a benchmark of 25 crime scenarios across 7 physically-driven case types (139 forensic-style photographs and 65 statements with planted unreliability), VeriScene attains 0.9014 evidence coverage and 0.7217 factual consistency (0-1 scale) on the 20 test scenes, outperforming an end-to-end multimodal-LLM baseline by 20.35% in factual consistency and 34.88% in temporal coherence, while generalizing across four LLM orchestration backends at USD 1.82 per scene.

---


### 370. [CoVeR: Coverage-Based Token Pruning for Multi-View 3D Reasoning in VLMs](https://arxiv.org/abs/2609.08345)

**<font color=#1a73e8>作者：</font>** Nhat-Tan Bui, Varshini Elangovan, Arun Reddy Anugu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representing a 3D scene as multi-view images allows 2D VLMs to reason in 3D by reusing priors from pre-training, sidestepping the scarcity of annotated 3D data. However, it produces thousands of redundant visual tokens whose cost grows with every view. Existing visual token pruners fall into two families, each limited in the 3D multi-view setting. Learned importance methods rank tokens by attention or encoder features; because redundancy here is fundamentally spatial, they keep near-duplicate tokens from a few prominent regions and leave most of the scene unrepresented. Voxelization methods improve spatial coverage but cannot enforce an exact token budget and saturate as multi-view observations overlap in 3D, capping retention well below the target. We show that spatial coverage is associated with 3D reasoning performance and introduce CoVeR, a deterministic, training-free selector that uses only token coordinates, with no learned signals. CoVeR selects tokens that collectively cover every region of the scene, and solves the limitations of both families: it enforces an exact per-scene budget, breaks the voxelization saturation plateau, and avoids the near-duplicate selections of learned importance. Extensive experiments show CoVeR outperforms prior SOTAs on all three 3D reasoning benchmarks and generalizes as a plug-and-play module tested across four VLMs. Notably, with only $\approx$8% of visual tokens, it preserves 93.5% of full-token performance, surpassing SOTA by 3.9 percentage points on average across benchmarks.

---


### 371. [SentryLine: Evidence-Grounded Question Answering over Evolving Documents in Oncology Care](https://arxiv.org/abs/2609.08364)

**<font color=#1a73e8>作者：</font>** Tampu Ravi Kumar, Gaurav Najpande, Muhammad Ali Khan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Oncology care operates at constant pressure of absorbing rapidly evolving evidence base in biomedicine. The American Society of Clinical Oncology (ASCO) addresses this through living guidelines, but the format introduces a new burden: any recommendation can change at any point, across multiple versioned documents. We present SENTRYLINE, a living guideline-aware clinical question answering system. SENTRYLINE retrieves guideline passages through a vectorless hierarchical RAG pipeline and returns a role-specific answer with inline citations, factual and temporal verification reports, and drift detection notes that surface when a guideline has been updated. We construct ASCOBENCH, a benchmark of 405 three-turn conversations across four question categories with gold answers from expert annotators(clinicians), and use test set to evaluate SENTRYLINE against five baselines under an LLM-as-judge framework. Experiments across three generation backbones show consistent improvements over four retrieval baselines and ASCO's guideline assistant, with particularly strong gains on Reasoning and Role-Specific questions where multi-hop synthesis and register adaptation are required

---


### 372. [To Adapt or Not to Adapt? Selective Adaptation for Vision-Language Models](https://arxiv.org/abs/2609.08367)

**<font color=#1a73e8>作者：</font>** Siru Jiang, Yuwei Liang, Jian Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) has emerged as a prominent strategy for adapting vision-language models to distribution shifts during inference. We conduct a per-sample analysis of model predictions before and after adaptation, and observe two failure modes in existing TTA methods that echo previous work. Adaptations are frequently negligible, yielding no change in the model's predictions, and more severely, they can be detrimental by flipping previously correct predictions to incorrect ones. This naturally raises a question: Can we identify and skip such negligible or harmful adaptations? In this work, we introduce a new problem of selective adaptation, which aims to determine whether a given test sample should undergo adaptation or be skipped. To this end, we propose Cross-Augmentation Similarity (CAS), a simple baseline that performs adaptation only when predictions across augmented views exhibit low similarity. Notably, CAS not only preserves but in some cases improves overall accuracy, even when skipping nearly 85% of the adaptation process. We hope other researchers will explore this new direction and surpass the performance of our baseline. Our code is available at this https URL.

---


### 373. [Reading a Legal Question Word by Word: Embedding Trajectories of 2,144 Vietnamese Legal Headlines](https://arxiv.org/abs/2609.08372)

**<font color=#1a73e8>作者：</font>** Tran Minh Quan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A dense retriever encodes a question as one vector, but the question arrives one word at a time. We read 2,144 held-out headlines from Thu Vien Phap Luat (Vietnamese legal library) word by word with Nemotron-3-Embed 8B/1B and Qwen3-Embedding 8B/0.6B, encoding 65,444 prefixes against 20,034 articles, plus every prefix of 3,438 sub-questions from 1,112 multi-question headlines and of 168 answers. (i) The gold article becomes rank 1 after a median of 6-7 content words in every encoder, before the interrogative frame is read, and stays there to the end in 78-85% of cases. (ii) In a multi-question headline the lock is inside the first sub-question 94-98% of the time; the second leaves rank unchanged in 89-95%; encoded alone, the second reaches rank 1 in 42-58% vs 91-96% for the first, at the same lock word (95-97% identical). (iii) Numbers, dates and instrument identifiers move the embedding twice as far as content words and four times as far as interrogative words; 72-78% of steps move toward the gold article, and the closing interrogative frame moves against that direction in 95-99% of headlines. (iv) Rank/cosine clustering yields six archetypes (instant, typical, unstable, late, never-locking) that differ by legal area and form (chi-squared p < 1e-8): real-estate and litigation headlines never lock on a number; environmental and accounting headlines do so a third of the time. (v) An answer read word by word retrieves its article after 8-16 words and addresses the sub-questions in order asked in 83-89% of cases. (vi) A word's step keeps a consistent direction across headlines (cosine 0.25-0.33; 0.44-0.60 for numbers); a preceding question rotates that step by about 60 degrees and a greeting by about 30 degrees; steps shrink as i^{-0.8}; and a two-question headline is within 12-17 degrees of a linear mix of its two questions. We call this a context-modulated additive walk.

---


### 374. [From Coordinates to Candidate Regions: Temporal Change Localization via Region Selection in Remote Sensing Multimodal LLMs](https://arxiv.org/abs/2609.08391)

**<font color=#1a73e8>作者：</font>** Juwan Chung, Sungjune Park, Yeongyun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing multimodal large language models (RS-MLLMs) have advanced scene understanding and visual question answering over satellite imagery, yet localizing specific objects or changed regions remains challenging. Existing approaches rely on generating bounding box coordinates as token sequences, which is fragile for the small, densely packed objects common in remote sensing and increasingly error-prone when multiple targets must be localized simultaneously. In this work, we present an RS-specific formulation of the region selection paradigm, previously explored in natural-image MLLMs, and extend it to temporal change localization over multi-image sequences. Our framework employs a text-conditioned region proposal module, encodes each candidate as special tokens carrying per-frame visual features enriched with spatial and temporal cues, and lets the LLM localize targets by selecting region tokens in its response. We construct a multi-task training and evaluation suite spanning localization, referring expression, visual grounding, and understanding tasks across single-image and multi-temporal settings. Experiments show that our approach substantially outperforms coordinate-generation baselines on temporal change localization, while improving single-image visual grounding and maintaining competitive understanding performance. Oracle analysis decomposes the contributions of the region proposer and the LLM selector, providing diagnostic insight unique to this framework. Our code will be available at this https URL.

---


### 375. [Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method](https://arxiv.org/abs/2609.08402)

**<font color=#1a73e8>作者：</font>** Boao Yu, Zimo Chen, Junreng Rao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Air-Ground Object Search (AGOS) in urban environments is a challenging embodied task, which requires an Unmanned Aerial Vehicle (UAV) and an Unmanned Ground Vehicle (UGV) to jointly search for and verify a specified target vehicle from multi-view visual references. To study this underexplored problem, we introduce AGOS-Bench, the first dedicated benchmark for evaluating whether general-purpose Vision-Language Models (VLMs) can integrate aerial discoveries and ground-level verification through UAV-UGV cooperation. We further provide AGOS-Dataset as the companion resource of exemplary trajectories constructed by an automatic pipeline. It consists of 7.7k episodes for searching objects of diverse categories and attributes, spanning three difficulty levels. To address the AGOS task, we propose AGOS-Agent, a training-free and tool-augmented approach. The agentic method relieves VLMs from complex and dynamic coordination via a deliberate search-handoff-verify cooperation protocol, only demanding VLMs for scene understanding and decision-making. Extensive experiments on nine VLMs show that AGOS-Agent improves overall success rate for eight of the nine evaluated backbones while reducing decision steps for all nine. On the hard split, the SR and SPL of Gemini-3.6-Flash increase from 8.6% to 55.7% and from 7.6% to 44.0%, respectively.

---


### 376. [Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks](https://arxiv.org/abs/2609.08404)

**<font color=#1a73e8>作者：</font>** Hongbang Yuan, Zhuoran Jin, Yixin Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models demonstrate remarkable proficiency in static reasoning, yet training them as autonomous agents through Reinforcement Learning (RL) for long-horizon tasks is often hindered by severe reward sparsity. While conventional \textit{agent-side warming} up via supervised fine-tuning (SFT) can alleviate this, it is frequently limited by data scarcity and constrained exploration. To address this, we propose a paradigm shift to \textit{environment-side adaptation} by constructing \textbf{F}eedback-\textbf{E}nriched \textbf{E}nvironments (\textbf{FEEs}). Through a pilot study, we establish a feedback design strategy that reformulates environments by transitioning from action guidance to observation enrichment during the later stages of both intra-episode exploration and inter-episode evolution. Large-scale experiments on SciWorld and BFCL benchmarks using various Qwen3 model scales and RL algorithms such as GRPO, GSPO, and DAPO demonstrate that FEEs consistently yield performance improvements over standard settings. Furthermore, our analysis reveals that training with FEEs \textbf{(1)} stabilizes training dynamics by reducing entropy volatility, \textbf{(2)} facilitates proactive state-space exploration in difficult tasks, \textbf{(3) }ensures the internalization of environmental guidance into policy weights rather than acting as a mere inference-time prior, and \textbf{(4) }identifies intra-group feedback consistency as a critical boundary for stable optimization.

---


### 377. [FastE: Readout-Triggered Token Compression for LLM Embedding Inference](https://arxiv.org/abs/2609.08407)

**<font color=#1a73e8>作者：</font>** Jinsong Shu, Jinyong Wen, Baokun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this study, we identify depth-dependent prefix redundancy in final-readout LLM embedding models, notably across representative backbones including Qwen3-Embedding and Qwen3-VL-Embedding. We find that removing prefix states is substantially more damaging in shallow layers than at greater depth, showing that prefix states become increasingly compressible as the prefix and readout states propagate through the network. To this end, we introduce FastE, a training-free, plug-and-play method. FastE uses a shared fixed threshold on batch-mean readout-prefix alignment as a lightweight online heuristic for selecting when compression occurs, and ranks prefix states by the attention scores they receive from the readout position to determine which states are retained in subsequent layers. Our evaluations demonstrate FastE's ability to substantially reduce computational costs: on NarrativeQA with Qwen3-Embedding-0.6B, it reduces decoder-backbone FLOPs by 40.11% while retaining 99.53% of Full Forward nDCG@10. Across five text embedding benchmarks, two backbone scales, and three cross-modal retrieval tasks, the quality-efficiency trade-off is directly customizable through the maximum removal ratio without retraining. We believe FastE offers practical value for scalable embedding generation in retrieval, indexing, clustering, and multimodal representation systems.

---


### 378. [Compositional Multilingual and Behavioral Attribute Steering](https://arxiv.org/abs/2609.08410)

**<font color=#1a73e8>作者：</font>** Hyun Gu Kang, Daniil Gurgurov, Tanja Baeumel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines the compositionality of steering vectors for language and behavioral control in large language models. Focusing on language, jailbreak, and conciseness, we investigate whether additive, training-free composition of attribute steering vectors can preserve the intended steering effect of each attribute, across four instruction-tuned models from two model families and two size scales. We find that single-attribute steering is reliable for all three attributes, but only within an appropriate combination of intervention layer and steering strength, with abstract behaviors (jailbreak, conciseness) favoring middle layers and language favoring earlier layers. We show that additive composition of two attribute vectors succeeds in steering both attributes simultaneously when each is injected at its own best-performing layer, and that this partially extends to three simultaneously composed attributes, addressing an inconsistency left open by prior work on training-free composition. We further analyze the geometric properties of these steering vectors, finding that they are approximately orthogonal in the residual stream, consistent with their compositional behavior.

---


### 379. [EvolveScaler: Synthesizing Information-Evolution Contexts via Executable State Machines and Natural-Language Rendering](https://arxiv.org/abs/2609.08435)

**<font color=#1a73e8>作者：</font>** Ziliang Zhao, Zenan Xu, Shuting Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In persistent interactions, long contexts may encode an evolving process rather than a fixed record: later events can revise or revoke earlier information, changing what remains valid and what conclusions follow. We call this setting information evolution (IE). Solving IE requires identifying valid records, applying updates in order, and reconstructing the query-relevant state from the event history. Existing text-first synthesis pipelines make such data difficult to verify because state transitions and answer logic remain implicit. We introduce EvolveScaler, a code-driven framework that defines information evolution before rendering it as natural language. Human-authored operational specifications define state transitions, record validity, difficulty controls, and executable answer logic; a strong LLM then synthesizes a self-contained simulator from each specification. Executing validated simulators produces natural-language multi-turn event histories, while deterministic replay computes reference answers and atomic checklists. We instantiate EvolveScaler with 117 task prototypes and 159 final-question operators across five difficulty levels spanning approximately 7 to 1,200 events per instance, yielding about 35,100 training examples and 585 validated evaluation instances. On the very_long tier, the strongest model reaches 59.3% avg@5, while six models score below 10%. Training an internal A3B model on 6,000 EvolveScaler examples improves performance over its base checkpoint on all eight independently constructed out-of-distribution benchmarks, with a 5.25-point average gain. These results show that code-driven IE synthesis provides both challenging evaluation and transferable training supervision.

---


### 380. [SRPO: Setwise Relative Policy Optimization for Multi-Agent LLMs](https://arxiv.org/abs/2609.08452)

**<font color=#1a73e8>作者：</font>** Shengtian Yang, Ziyu Xiong, Yu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language models solve complex tasks by coordinating several policies in a shared environment. However, existing reinforcement learning methods usually optimize each response or trajectory separately, even when several outputs jointly cause one state transition. Consequently, the update unit differs from the action executed by the system. To address this problem, we propose SRPO (Setwise Relative Policy Optimization), which treats the active set the minimal set of outputs consumed by one transition, as one multi-agent action. Specifically, SRPO combines member log-ratios into one cardinality-normalized set ratio, assigns one relative advantage, and clips the set once. This formulation unifies division of labor and joint co-evolution as actions with different set sizes. Experiments on mathematical reasoning and multi-turn search demonstrate one training interface for fixed, mixed, and dynamically routed workflows across four model scales, with the strongest macro-average results among the reported comparisons. Optimization diagnostics further characterize its stability under different event reductions and set sizes.

---


### 381. [Do Reviewers Still Reward Lexical Complexity? A Frozen-Rater Study of Preference Drift in 124K ICLR Reviews](https://arxiv.org/abs/2609.08475)

**<font color=#1a73e8>作者：</font>** Jiabin Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have collapsed the cost of producing lexically elaborate prose, and whether peer reviewers still reward it is a question about the evaluator, not about the text. When the association between a writing cue and review scores moves across years, the reviewers may have changed, the submissions may have changed, or both, and a regression of scores on text cannot say which. We separate the two with a frozen rater: 81,850 machine reviews of ICLR submissions from 2018 to 2025, all generated in one February-April 2025 window with one model family and one prompt, so that its year-to-year coefficients track submission composition alone and the human-minus-frozen trend difference identifies reviewer preference drift. On 32,638 submissions with 124,615 human reviews, the human coefficient on non-domain lexical complexity falls from +0.142 to -0.015 while the frozen rater moves from +0.080 to +0.082; the three-way difference-in-differences is -0.0100 (q=0.013), and forty random-wordlist placebos through the same specification centre on zero. Humans still reward sentence-length variability, which the frozen rater never registers, while the frozen rater still pays for lexical complexity at its earlier rate. Every claim is held to a double gate of false-discovery control and interval exclusion, and the findings that failed adversarial re-testing are reported. Reviewers discounted a cue whose production cost collapsed, as models of manipulable signals prescribe; an LLM judge calibrated to historical human preferences inherits the earlier schedule and drifts out of alignment while its agreement with humans on totals stays ordinary.

---


### 382. [Same Values, Different Languages? From Multilingual Probing to Steering LLMs Toward Chinese Social Values](https://arxiv.org/abs/2609.08515)

**<font color=#1a73e8>作者：</font>** Yuemei Xu, Kexin Xu, Jian Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly integrated into human society, aligning them with pluralistic social values has become a critical priority. However, whether LLMs exhibit consistent value preferences across languages remains underexplored, particularly for culturally grounded values, which are more abstract and difficult to evaluate and align than safety-centric principles. We investigate this issue through Chinese Social Values (CSV), a value system rooted in Chinese culture and comprising $12$ dimensions across national, societal, and personal levels. We construct C-Voices, the first comprehensive multilingual contrastive probe dataset for CSV, with 86,400 dilemma-based instances in six languages, each pairing a CSV-aligned action with a value-conflicting alternative. Building on the contrastive probes of C-Voices, we then propose a fine-tuning-free value vector steering method that derives value directions from hidden-state discrepancies and selectively intervenes on value-sensitive layers during inference. Experiments on six languages show that CSV-oriented preferences are model-dependent and language-sensitive, with the same dilemma eliciting divergent responses across languages. Our method achieves effective CSV steering, supports cross-lingual transfer of value vectors, and generalizes to existing FLAMES and ValuePrism.

---


### 383. [Layer Selection in VLMs for Zero-Shot OOD Detection via Multi-Resolution Entropy Estimation](https://arxiv.org/abs/2609.08524)

**<font color=#1a73e8>作者：</font>** Shyam Nandan Rai, Francesco Di Salvo, Sebastian Doerrich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection is crucial for safe deployment of medical AI systems, where domain shifts arise across institutions, acquisition protocols, and patient populations. VLMs enable zero-shot OOD detection by embedding images into a language-aligned latent space, where cross-modal similarity serves as a non-parametric confidence signal for identifying in-distribution samples. Yet existing methods rely almost exclusively on final-layer embeddings, implicitly assuming that the deepest representations are universally optimal. We first show that this assumption does not hold in medical imaging: intermediate layers provide complementary OOD signals, and the optimal representational depth depends on the respective image modality. While prior work selects layer combinations via entropy minimization of normalized histograms, we demonstrate that single-resolution entropy estimation is highly sensitive to binning choices, leading to performance variations of up to 19.3% AUROC. To address this instability, we propose a multi-resolution entropy estimation strategy that aggregates histogram statistics across multiple discretization scales, enabling robust and stable intermediate-layer selection. Across two medical OOD benchmarks, namely MIDOG and OASIS, covering distinct imaging modalities, diverse shift types, and different VLM backbones, our method consistently outperforms state-of-the-art approaches, offering a lightweight and stable solution for zero-shot OOD detection.

---


### 384. [STSG-VQA: Evidence-Grounded Temporal Question Answering from Surgical Spatio-Temporal Scene Graphs](https://arxiv.org/abs/2609.08543)

**<font color=#1a73e8>作者：</font>** Jing Li, Duygu Sarikaya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in surgical vision-language models (VLMs), temporal reasoning remains limited because existing supervision is largely frame-centric. Frame-level scene graphs (SGs) have proven effective in providing structured representations of surgical environments but do not explicitly model the dynamics of surgical workflows. To explicitly model how surgical states evolve across time, we introduce a multi-level structured temporal supervision methodology that augments frame-level surgical SGs with object-level continuity, event-level interaction continuity, and procedure-level connectivity. We then execute temporal queries over the resulting spatio-temporal scene graphs (STSGs) to generate evidence-grounded question-answer pairs, which together form the STSG-VQA benchmark. Each question is linked to the temporal interval and STSG evidence used to derive its reference answer, enabling traceable verification. The benchmark contains 18,458 question-answer pairs across seven temporal categories. Fine-tuning Qwen3-VL-4B and Hulu-Med-4B with STSG-derived supervision improves question-level micro accuracy by 24.39 and 19.56 percentage points over their zero-shot baselines and by 16.50 and 14.25 points over static scene-graph supervision, respectively. These gains span all temporal categories, indicating that STSG-derived supervision helps surgical VLMs reason over temporally grounded interactions rather than isolated frames. The code and dataset will be made publicly available upon acceptance.

---


### 385. [CreaMem: A Scene-Aware Memory Architecture for Personalized Agents](https://arxiv.org/abs/2609.08550)

**<font color=#1a73e8>作者：</font>** Qixuan Sun, Yue Que, Bowei He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is a core capability for personalized LLM agents. To support it, existing memory systems organize information using various criteria such as topic segments or summary hierarchies. However, we identify two major limitations in these designs. First, they lack scene awareness: memories from unrelated life scenes share the same retrieval space, which inflates the search space and introduces cross-scene interference. Second, they encode each memory from a single perspective, making it difficult to retrieve complementary views of the same event. In this paper, we propose the CreaMem architecture, which enables scene-aware memory organization by partitioning memory into several Life Scene Memories to reduce cross-scene interference at retrieval. To go beyond the single perspective and achieve cross-memory synergy, entries are dual-coded from both episodic and trait-based perspectives within each memory. We further devise a permemory balanced sampling strategy at retrieval time. Extensive experiments on two long-term memory benchmarks show that CreaMem improves QA accuracy across all evaluation metrics, with particularly large gains on multi-hop reasoning performance, validating scene-aware partitioning and cross-memory synergy. To enhance reproducibility, we release our code in a public GitHub repository.

---


### 386. [Personalizing LLM Agent Memory Using Biometrics](https://arxiv.org/abs/2609.08558)

**<font color=#1a73e8>作者：</font>** Yanhong Qian, Qingguo Meng, Shihao Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized memory helps LLM agents deliver stable, tailored assistance by storing and reusing user-specific data across interactions. In multi-user scenarios, however, retrieval must consider not only semantic similarity but also whether the current requester matches the identity associated with the stored memory. We propose Bio-Memory, a biometric-aware memory architecture that conditions memory retrieval on both semantic similarity and biometric matching. Built on top of A-Mem, Bio-Memory augments each atomic memory note with a biometric embedding and uses biometric matching to form the retrieval candidate pool before semantic ranking. We evaluate Bio-Memory on LoCoMo in a 10-user shared-agent setting over 7 face benchmarks and 10 palmprint protocols. Across datasets, Bio-Memory consistently separates owner and non-owner queries. Under face-based personalization, the largest average gap reaches 27.29% / 21.15% in F1 / BLEU-1 on CALFW; under palmprint-based personalization, the corresponding gap is 25.75% / 19.22% on MS_Blue. These results support biometrics as a practical control signal for personalized memory retrieval in shared environments.

---


### 387. [Certified Topological Interaction in Neural Representations: Class Disentanglement Is Mostly Pairwise](https://arxiv.org/abs/2609.08561)

**<font color=#1a73e8>作者：</font>** Sushovan Majhi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class disentanglement (the separation of a representation's class-conditional point clouds along depth and over training) is usually read off descriptive curves. We measure it as certified topological interaction between labeled point clouds, using the recently introduced Intersection Euler Characteristic Profile: the Euler characteristic of the overlap of the clouds' ball unions as a function of scale, computed by one Alpha-complex sweep with no boundary-matrix reduction. Every number carries a test: exact permutation tests in both directions, a guarded separation certificate, and a paired test for the comparative claims applications make. Across 111 trained networks and 52,650 certified measurements, disentanglement is depth-graded and concentrated in the first epochs, and interaction quotients rank class pairs by confusability (Spearman rho=0.83), on par with cheap separability statistics. In a 96-model factorial population, augmentation is the one training choice that separates classes relative to chance; weight decay compresses the overlap without separating, and depth and width do nothing. The structural finding is one only a k-fold statistic can pose: the joint entanglement of a class triple sits below that of its strongest pair in 97% of triple-layer cells and 99.5% of deep cells, far below a measured null floor, in vision encoders and frozen language models alike. This pairwise dominance is a regularity, not a law: expected from the nesting of overlaps but not forced by geometry, present at initialization and in raw pixels, and manufactured in the last stage alone when a network memorizes random labels. The unnormalized profile mass predicts test accuracy (R^2=0.94), the quotient does not, and neither beats a linear probe. One lesson is reported in full: the paired test must use a scale-free statistic, or it certifies feature-norm dynamics as disentanglement.

---


### 388. [BIO-MEMART: Biometric-Aware KV Cache Memory for Multi-User LLM Agents](https://arxiv.org/abs/2609.08566)

**<font color=#1a73e8>作者：</font>** Yanhong Qian, Xuanying He, Qingguo Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> KV cache is evolving from a serving optimization into an external memory substrate for long-term LLM agents. In a shared multi-user deployment, however, reusable KV blocks introduce a missing access-control question: semantic relevance alone cannot determine whether a memory block is authorized for the current physical user. We propose Bio-MemArt, a biometric-aware KV-cache memory framework for multi-user LLM agents. Bio-MemArt attaches a normalized biometric template to each stored KV memory block, filters the shared memory pool with the current user's biometric probe, and then runs the original MemArt retrieval and KV reuse pipeline only inside the authorized candidate pool. This design preserves latent-space retrieval, direct cache reuse, and decoupled position encoding while adding physical-user access control to shared KV memory. We evaluate Bio-MemArt under Owner and Non-owner query conditions on long-term dialogue QA with face and palmprint benchmarks. Across face benchmarks, the average owner and non-owner biometric success rates are 95.71% and 0.86%; across palmprint benchmarks, they are 97.60% and 2.00%. In the efficiency study, average prefill tokens drop from 18,781.96 under full-context prompting to 28.57 with Bio-MemArt, showing that biometric gating preserves the low-token operating regime of KV-cache memory.

---


### 389. [AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems](https://arxiv.org/abs/2609.08572)

**<font color=#1a73e8>作者：</font>** Jaewon Chu, Jinwoo Seo, Jaewon Cho 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) achieve strong performance by employing specialized multiple agents, yet their performance depends on the prompt design of each agent. For MAS prompt optimization, textual gradient methods that guide prompt updates using natural-language feedback have emerged as a leading paradigm. In this paper, we identify limitations in two stages of existing textual gradient approaches: gradient extraction and gradient aggregation. In gradient extraction, previous works select a target prompt without verifying whether modifying it resolves the failure, and derive gradients without agent-level supervision over the corresponding agent's intermediate output. In gradient aggregation, individual gradients are randomly grouped and concatenated, often mixing unrelated failure modes and producing prompts that fail to generalize. To address these limitations, we propose \textbf{AgentGrad}, a prompt optimization framework for multi-agent systems based on sequential intervention and semantic textual gradient abstraction. For each failure, sequential intervention modifies the behavior of one agent at a time to identify the target agent whose modification resolves the failure. The modified output of the target agent then serves as agent-level supervision for extracting a fine-grained gradient. Semantic textual gradient abstraction clusters semantically similar gradients to prevent mixing unrelated failure modes, and abstracts each cluster into a generalized gradient that captures the shared corrective pattern. Experimental results show that AgentGrad achieves state-of-the-art performance across five MAS benchmarks and reduces wall-clock optimization time by $2.5\times$ on average compared to the next-fastest baseline.

---


### 390. [Do New Attention Mechanisms Actually Fix Attention Sinks at Million-Token Context?](https://arxiv.org/abs/2609.08574)

**<font color=#1a73e8>作者：</font>** Sara Rizwan, Samaanah Abdus Salam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long context language models now advertise windows of one million tokens, but two habits limit how much of that window is used. Attention heads with nothing useful to read still spend their budget on the first token, which is called the attention sink, and where a fact sits in the context changes whether the model finds it. Gated attention cut first token attention from 46.7 percent to 4.8 percent at NeurIPS 2025, and Kimi K3 pairs that idea with Kimi Delta Attention and Attention Residuals behind a one million token window, eight times past the range where these diagnostics have been reported. This paper asks whether the fix survives that jump. We build SinkProbe, a suite that measures sink mass, massive activation, position resolved recall and the recency gap, and apply it to four small models that differ only in how they mix tokens and depth. Three results follow. The training objective produces the sink, not the architecture. Gating did not reproduce its published effect at our scale. Sink mass, activations and position bias moved independently. Code, data and the measurement protocol are released at this https URL

---


### 391. [Which Forms of Caregiver Feedback Support Grammar Learning? A Reinforcement-Learning Study of Child-Like Language Models](https://arxiv.org/abs/2609.08576)

**<font color=#1a73e8>作者：</font>** Jing Liu, Marianne Schweitzer, Abdellah Fourtassi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social interaction is central to children's language learning, but the effects of different forms of caregiver feedback are difficult to isolate in naturalistic data. We use child-like language models as controlled learners to test which forms of feedback support grammatical development. Small GPT-2-style models are pretrained on child-directed language from CHILDES, then fine-tuned with reinforcement learning using reward models trained to capture four feedback types: communicative feedback, structural alignment, semantic contingency, and affective feedback. Reward fine-tuning yields limited gains on minimal-pair evaluations, but clearer effects in free generation. Structural alignment produces the strongest improvements in grammaticality, providing a novel, plausible mechanistic account of how this feedback can support grammar learning. Communicative feedback yields more moderate gains. In contrast, semantic contingency and affective feedback do not improve grammaticality, although further analyses suggest that they may support other aspects of language learning beyond grammar. These results suggest that different forms of caregiver feedback make complementary contributions to language learning.

---


### 392. [Limitations of Automated Simulatability: LLM Simulators Can Bypass Explanations](https://arxiv.org/abs/2609.08585)

**<font color=#1a73e8>作者：</font>** Antonin Poché, Fanny Jourdan, Nils Feldhus 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simulatability is an evaluation protocol for explanations that quantifies their usefulness by how well they help a user predict a task model's outputs. Since human evaluation is costly, automated simulatability replaces human explainees with LLM simulators, as proposed in ConSim (Poché et al., 2025) for large-scale experiments. We qualitatively replicate and extend ConSim's ranking of explanation methods across the tested datasets, explanation families, and simulator LLMs, and identify two limitations. First, when class names are meaningful, simulators can obtain high simulatability by solving the classification task directly, without relying on the explanations. Second, class anonymization can reward explanations for leaking the hidden label mapping, a limitation we expose with a new classes-as-concepts baseline. These results are consistent with a shortcut hypothesis: in the tested settings, simulator predictions mainly rely on task priors, while explanations produce small changes. We derive recommendations for more robust automated simulatability evaluations.

---


### 393. [A Three-Tier Persona Vector for Controllable User Simulation in Agentic Evaluation](https://arxiv.org/abs/2609.08592)

**<font color=#1a73e8>作者：</font>** Rahul Khedar, Eshita, Sneha Teja Sree Reddy Thondapu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating tool-augmented LLM agents requires diverse, realistic user inputs yet most evaluation frameworks use flat role descriptions ("you are an angry customer") that produce near-identical conversations regardless of the underlying scenario. In this paper, we propose a three-tier persona vector with 23 operationalized dimensions: 6 categorical demographics (jurisdiction, age, channel, device, language proficiency, time availability), 12 continuous behavioral traits (patience, assertiveness, digital literacy, etc.) sampled with Gaussian noise around curated profile base vectors, and 5 continuous emotional states (frustration, anxiety, trust, confidence, stress) that shift in response to scenario context. Orthogonal to the persona, a 4-level query-complexity overlay controls utterance phrasing from direct to deliberately vague. We evaluate the persona model inside a synthetic data generation pipeline across 64,698 multi-turn conversations spanning 8 named profiles and 3 production corpora. Key findings: (i) a 15.8 percentage-point spread in agent goal-achievement across personas confirms trait vectors produce measurably different user behavior; (ii) the same persona behaves differently across scenarios due to scenario-reactive emotional state shifts, validating the scenario-reactive design; (iii) domain-specific projects show persona sensitivity on booking-flow compliance (~15-20 percentage points gap between tier-aware and pressure-test personas), demonstrating the model faithfully reproduces real-world difficulty distributions; (iv) seven rule-described trait correlations produce auditable co-occurrence patterns without requiring learned covariance matrices. The persona model is fully specified for reproduction.

---


### 394. [Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation](https://arxiv.org/abs/2609.08599)

**<font color=#1a73e8>作者：</font>** Dac Duy Anh Nguyen, Zhangchi Qiu, Shigeng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are evolving from single-session tools toward long-term personal assistants that must adapt to individual users across tasks, contexts, and interactions. This shift makes memory a core requirement for personalization, since user preferences, goals, constraints, relationships, and past experiences are accumulated gradually and often change over time. Graph-based personalized memory provides a structured way to model such user information through explicit relations, temporal context, and evidence links. Such representations can model not only what an agent remembers about a user but also how memories are connected, revised, and retrieved to support personalized decisions. However, existing work remains fragmented across personalized agents and generic graph memory frameworks, making it difficult to understand the design space as a whole. This survey develops a lifecycle-oriented view of graph-based personalized memory for LLM agents. We organize existing studies around memory representation, memory evolution, memory retrieval, and memory evaluation. We further compare key design choices, discuss current evaluation practices, and open challenges in building reliable long-term personalized agents. This survey aims to clarify how graph-based memory can support adaptive, controllable, and user-centric LLM agents.

---


### 395. [CLAMP: Constrained Decoding for Vision-Language Embodied Planning](https://arxiv.org/abs/2609.08602)

**<font color=#1a73e8>作者：</font>** Tianyi Ma, Parisa Kordjamshidi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied planning increasingly relies on vision-language models (VLMs) to translate instructions and visual observations into executable action sequences. However, fluent plans are not always executable. A VLM may refer to objects that are not visually observed, select actions whose required affordances are unavailable, or violate syntax and action constraints. We introduce CLAMP, a multimodal constraint-grounding framework that turns scene evidence into decoding-time constraints for a frozen VLM planner. CLAMP uses the initial observation to restrict object references to those supported by the scene, while a provided symbolic action model specifies state transitions and goals. During decoding, hard masks eliminate invalid next-token candidates, while a Hidden Markov Model (HMM)-based world-state lookahead module reweights the probabilities of the remaining feasible candidates based on action preconditions and goal reachability. This allows the planner to retain the VLM's language prior while preventing visually unsupported, unsafe, or infeasible candidates from entering the plan. For unseen tasks and environments, CLAMP adapts the HMM at test time using label-free continuations sampled from the frozen VLM. Experiments on VLABench, SafeAgentBench, and TaPA show that scene-grounded constraints improve object grounding and safety, while most remaining failures stem from perception errors or misaligned constraint specifications.

---


### 396. [Dynamics of meaning: Towards the Evaluation of Diachronic Semantic Change in Sinhala](https://arxiv.org/abs/2609.08609)

**<font color=#1a73e8>作者：</font>** Nevidu Jayatilleke, Nisansa de Silva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tracking semantic change in low-resource languages across extensive historical timelines presents significant challenges due to data scarcity and the limitations of static embedding alignments. This study investigates the diachronic evolution of the Sinhala language from the 13th to the 20th century using a multi-stage computational framework. We first align century-specific Word2Vec and FastText embeddings using Similarity Matrix Based Alignment (SMA) and Orthogonal Procrustes (OP) techniques, finding that OP alignment provides more stable neighbourhood tracking for identifying temporal similarity dips. To move beyond aggregate measures, we introduce a Bidirectional Semantic Impact Pruning approach using contextualised embeddings from a fine-tuned Llama-3.1-8B. By applying Leave-One-Out (LOO) diagnostics, we attempt to isolate influential sentences to distinguish between systemic semantic shifts and transient polysemic expansion. Our results show that semantic drift in the fine-tuned Llama-3.1-8B is not evenly distributed across all usages. Instead, a significant part of the change is driven by a smaller set of high-impact contextual instances, rather than gradual and uniform change across all occurrences. This work provides a preliminary framework for diachronic analysis in low-resource contexts, highlighting the trade-offs between model sensitivity and data availability.

---


### 397. [Target-Independent Micro-Interventions for Predicting Training Response Across Language-Model Families](https://arxiv.org/abs/2609.08618)

**<font color=#1a73e8>作者：</font>** Zhongxuan Liu, Sicheng Zhou, Hongzhi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmark scores describe what a checkpoint can do now, but they do not determine how it will respond to the next training episode. We measure this missing state by branching four short, standardized, target-independent micro-interventions from the same checkpoint and recording their effects in a common capability space. Together with current capability, these responses form L-State; its pulse block supports a flexible direct readout and a structure-preserving operator readout. Under smooth local dynamics, the operator construction admits an end-to-end cross-family bound with explicit source- and target-family coordinate heterogeneity. In three-family leave-one-family-out development, both pulse readouts reduce source-standardized MSE by 39.4% relative to capability alone, while separating the best response and direction estimates. On sealed GLM-4-9B, the direct and operator readouts reduce MSE by 71.8% and 78.3%, respectively, and the operator readout raises sign balanced accuracy from 0.366 to 0.754. On sealed Granite-3.1-8B, the direct readout reaches RMSE 0.544 and a development-fitted action-wise selector reaches 0.554, compared with 1.172 for capability alone. A five-family audit finds that the operator coordinate varies by action and family, and that modeling these deviations improves retrospective held-trajectory prediction. Target-independent interventions therefore expose training-response information that current capability misses, with direct and structured readouts covering complementary transfer regimes.

---


### 398. [Navigating the digital spectrum: Assessing political bias, stability, and downstream fairness in Large Language Models](https://arxiv.org/abs/2609.08637)

**<font color=#1a73e8>作者：</font>** Luka Debevc, Nishan Chatterjee, Antoine Doucet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly deployed as information intermediaries, yet measuring their political behavior remains fragile because questionnaire results mix model dispositions with measurement artifacts and response-elicitation biases. We introduce a robust Political Compass Test evaluation framework that samples 300 configurations across an eight-dimensional perturbation space varying language, framing, instructions, answer format, option order, and persona wording. We evaluate eight Gemma 3 and Qwen 3 models across 14 languages and three quantization levels, obtaining design-averaged political coordinates with quantified uncertainty. Most models lean Libertarian-Left on average, but instruction phrasing, language, and answer format significantly affect recovered coordinates. Cross-lingual differences primarily reflect coordinate drift rather than distinct cultural reasoning. Reverse-engineering the test also exposes axis-weighting imbalances and the collapse of degenerate responses toward the center, so near-origin estimates for the smallest models can reflect weak signal rather than centrism. Free-text reasoning and chat-then-classify elicitation alter recovered coordinates, and larger models show clearer persona separation, with a specific failure of the Authoritarian-Left persona to move most models in the intended social direction. In downstream tasks, persona effects are modest relative to model size and target group for hate-speech detection, while base and centrist prompts give the highest agreement for topic-level sentiment. Political role prompting therefore has measurable but task- and dataset-specific downstream effects.

---


### 399. [Combating Instruction Conflict via Energy-Driven Latent Conflict Detection](https://arxiv.org/abs/2609.08646)

**<font color=#1a73e8>作者：</font>** Mingyu Ma, Yuxin Wu, Jingbo Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed with hierarchical instructions, yet they remain vulnerable to conflicts in which user directives override system-level constraints. Existing defense mechanisms predominantly focus on static input inspection and therefore fail to detect Response Drift, a phenomenon in which the model's final response violates system-level constraints despite seemingly compliant inputs. To bridge this gap, we introduce ELCD, a response-level latent conflict detector for post-generation, pre-delivery verification. Given the full generated output, ELCD constructs a composite hidden-state representation by concatenating the final-token embedding with the mean-pooled response embedding. It then optimizes a pairwise margin ranking objective to separate compliant and drifting responses in latent space. Extensive experiments across five mainstream LLMs ranging from 1.5B to 14B parameters demonstrate that ELCD significantly outperforms competitive baselines. Notably, it improves the PR-AUC on Llama-2-7B by approximately 30 percentage points and reduces the False Positive Rate at 95% TPR (FPR95) on Mistral-7B to 2.67%. These results suggest that ELCD provides a promising approach for latent instruction-conflict detection in open-weight or self-hosted LLM deployments.

---


### 400. [Charts Are Beyond Pixels: Probing for Layer-Wise Chart Understanding and Editing](https://arxiv.org/abs/2609.08657)

**<font color=#1a73e8>作者：</font>** Xiaochuan Zhong, Yifan Hou, Chenxi Pang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Charts are structured visual compositions whose elements have distinct functional roles, semantic correspondences, and visibility relations. This structural view motivates evaluating whether models can understand and manipulate charts at the layer level. Existing chart benchmarks, however, primarily assess the correctness or fidelity of final outputs and do not directly evaluate these layer-wise behaviors. We present LayerWiseBench, a benchmark organized around three core concepts, layer attribution, layer binding, and visibility ordering, that structure its chart-understanding and chart-editing evaluations. Generated from executable chart programs, LayerWiseBench pairs each rendered chart with spatially aligned per-layer RGBA assets and construction-derived labels for functional roles, semantic bindings, and visibility relations. From this layer-wise representation, we derive controlled understanding questions, editing targets, reference images, and evaluation regions. It contains 2,800 source charts across 14 chart paradigms, from which we derive 7,329 layer-wise understanding questions and 53,791 instruction-guided editing variants. Among the evaluated VLMs, Qwen3.5-27B, which achieves the highest QA macro-average, obtains 93.04% accuracy on layer attribution and 97.46% on layer binding, but only 61.46% on visibility ordering. Across the four evaluated image editors, overall mIoU ranges from 1.49% to 4.93%, and visibility-constrained edits have the lowest mIoU for every editor, ranging from 0.37% to 2.00%. Taken together, these results identify tasks involving front-to-back relations between overlapping components as a recurring challenge across understanding and editing, motivating more explicit modeling of component identity and visibility relations.

---


> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
