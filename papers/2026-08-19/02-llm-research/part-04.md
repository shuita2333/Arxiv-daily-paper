# 🧠 大模型相关研究 | 2026年08月19日

> 本类共 **358** 篇论文：已确认 **337** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

---

### 151. [The Machine's Internal Clock: Do LLMs Share Human Temporal Illusions?](https://arxiv.org/abs/2608.15394)

**<font color=#1a73e8>作者：</font>** Catherine Bao, Vivek Srikumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human perception of time is subjective. Well-documented temporal illusions show that the brain relies on context and relational cues for judging duration instead of tracking elapsed time directly. Prior studies established these effects with visual and auditory stimuli. Existing LLM evaluations of temporal perception focus on estimating event durations or multi-step temporal reasoning. In this work, we investigate whether written narratives alone can evoke human temporal illusions, using a new benchmark of 6,684 narrative pairs spanning five illusions. We find that human readers (60 participants) prefer expected scenarios in only two of the five illusions, those where the manipulation is directly visible in text rather than requiring readers to internally simulate duration. We evaluate 14 LLMs on the same benchmark. Surprisingly, we find that models pick the literature-predicted scenario across four of the five illusions, diverging from human behavior. Reasoning traces show that ~70% of responses explicitly evoke psychology research, suggesting that this alignment is consistent with retrieval of published findings rather than human-like temporal biases.

---


### 152. [Large Language Model Assisted Operational Monitoring for Battery Energy Storage System Integrated Power Distribution Networks](https://arxiv.org/abs/2608.15396)

**<font color=#1a73e8>作者：</font>** Azmeer Akhtar, Md Fazley Rafy, Anurag K. Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Battery energy storage systems (BESS) are increasingly used in distribution networks for voltage regulation and demand response, which increases the volume and complexity of operational telemetry available to grid operators. This paper presents an AI-enabled monitoring framework that connects a large language model (LLM) interface with a structured telemetry database for BESS-integrated distribution system analysis. Operator questions are submitted in natural language and translated into validated SQL queries using predefined database schema information and approved KPI views. Retrieved measurements, including bus voltages, state of charge, active power, and reactive power, are evaluated against engineering constraints for voltage limits, BESS operation, and demand response tracking. The framework is validated using hardware-in-the-loop co-simulation data from a BESS-equipped distribution feeder operating under reactive power-based voltage control and price-driven demand response. Case studies show that the framework generates valid database queries, identifies repeated voltage violations, detects reactive power overshoot, and evaluates active-power tracking performance. The results show that LLM-assisted monitoring can connect structured grid telemetry with automated engineering assessment for BESS operation analysis.

---


### 153. [Implementation of a Metacognition Framework for Self-Awareness and Self-Regulation in Ensembles of LLMs](https://arxiv.org/abs/2608.15400)

**<font color=#1a73e8>作者：</font>** Charles Courchaine, Ricky J. Sethi, Hefei Qiu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are notorious for struggling with assessing their own uncertainty, detecting knowledge conflicts, or recognizing when problems exceed their expertise; such limitations inevitably undermine reliability and trust in LLMs. In this paper, we present the first implementation of a metacognitive framework for ensembles of LLMs that addresses these challenges through explicit monitoring and control mechanisms.
Our system computes a Metacognitive State Vector (MSV) quantifying self-awareness for monitoring across five dimensions derived from cognitive psychology: Emotional Response, Correctness Evaluation, Experiential Match, Conflicting Information, and Problem Importance. MSV values also provide self-regulation for control, automatically switching between System 1 (fast, single- or multi-node) and System 2 (deliberative, multi-node) processing based on query complexity. For System 2 execution, graph-theoretic algorithms control the assignment of specialized roles (Domain Expert, Critic, Evaluator, Synthesizer, and Generalist) to ensemble nodes according to their MSV-quantified metacognitive states.
Our implementation allows users to explore how different query types trigger distinct processing modes. The Proof-of-Concept (PoC) demo showcases the framework with illustrative examples showing appropriate System 1/System 2 routing and helps visualize the metacognitive process via real-time radar charts and decision indicators. This PoC implementation demonstrates the feasibility of creating a framework for metacognitive self-awareness and self-regulation in LLM systems.

---


### 154. [CBX-Bench: A Human-Aligned MLLM Council for Benchmarking Concept Bottleneck Model Explanations](https://arxiv.org/abs/2608.15404)

**<font color=#1a73e8>作者：</font>** Yusuf Meric Karadag, Gulay Oklan, Seref Baris Cagliyan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) are designed to make visual classification interpretable by expressing predictions through human-understandable concepts. Although interpretability is the central motivation for CBMs, they are still largely evaluated as predictive models by downstream classification accuracy, supplemented by isolated qualitative examples. This highlights a pressing need for quantitative measures, a challenge complicated by the infeasibility of ground-truth concept annotation at scale and the open nature of concept lists due to a lack of consensus. To fill this gap, we develop a multimodal large language model (MLLM) council that, given an image and its CBM explanation, produces an explanation quality score. To ground and validate the council, we first conduct a human study to establish a ground-truth reference for CBM explanation quality: for an image, annotators compare explanations from two of LF-CBM, VLG-CBM, and CBM-Suite and choose the more useful one, or mark them as equally good or equally bad, yielding 2700 judgments over 900 image-comparison items on CUB-200, ImageNet-100, and Places365. Against this human reference, our five-model council, consisting of open-weight MLLMs, recovers over 70% of strict human preference rankings, rising to 83% on items where human annotators unanimously agree. Building on this validated council, we introduce CBX-Bench, a public benchmark and leaderboard: authors of new CBMs can submit their model's explanations, and CBX-Bench scores them with the council and maintains dataset-level rankings of explanation quality. CBX-Bench thus provides a human-aligned, scalable evaluation of CBM explanations beyond accuracy and isolated qualitative examples. The benchmark is available at this https URL.

---


### 155. [Chameleon: An Adaptive AI-Driven Honeypot Architecture Using Threat-Calibrated Particle Swarm Optimization and Semantic Deception Rapidly-Exploring Random Trees](https://arxiv.org/abs/2608.15407)

**<font color=#1a73e8>作者：</font>** Rohit Swami, Tushar Singh, Akash Warde 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An invariant behavioral profile is the defining vulnerability of traditional honeypot installations: a skilled adversary can confirm the presence of a deception environment within only a few diagnostic commands, limiting its intelligence value. High-cost commercial deception products (USD 100,000--150,000 per year) share a related weakness in that their response engines are not coupled to real-time model-driven feedback. Chameleon is an openly distributed adaptive honeypot platform introduced here to address both shortcomings. Three core components are integrated: a bidirectional long short-term memory (BiLSTM) classifier achieving 99.61% accuracy across seven threat categories at approximately two milliseconds CPU latency; a locally deployed Qwen3.5-0.8B language model (Qwen Team, 2026; Unsloth, 2026) delivering 90% contextual generation accuracy at 4.5 milliseconds average latency; and two domain-specific meta-heuristic engines. Threat-Calibrated Particle Swarm Optimization (TC-PSO) dynamically reshapes swarm inertia and objective amplification in proportion to the classifier's anomaly output, enabling real-time adjustment of connection-holding delays. Semantic Deception Rapidly-Exploring Random Trees (S-RRT) drives deception schema evolution via exponentially scaled pheromone updates derived from a language-model severity assessment, while a depth-decay multiplier enforces a finite memory footprint. Across five benchmark runs (seeds 42--46), TC-PSO outperformed standard PSO by 48.1% in mean fitness (2.60 to 3.85) with a 32.7% convergence gain, and S-RRT exceeded standard RRT by 258.9% in best-run fitness (450.2 to 1,615.8), achieving a 329.2% gain at critical severity and a 24.9% memory reduction (p < 0.01). Operating costs are approximately USD 17 per month, a roughly 490-fold reduction versus commercial alternatives.

---


### 156. [Invariant Pretraining for Robust Code Representations](https://arxiv.org/abs/2608.15412)

**<font color=#1a73e8>作者：</font>** Yifeng He, Yundi Xu, Christopher Castro Gaw Gonzalo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Encoder-based code representation models remain widely deployed for discriminative tasks such as clone detection and code classification, where their small size and low inference cost are decisive. Their robustness, however, is fragile: under invariant programs, semantically equivalent code written in different syntactic forms, learned representations degrade substantially even though program behavior is unchanged. We present an empirical study of this robustness gap across four encoder baselines, two downstream tasks, and four datasets, together with a minimal code-only continued pretraining recipe that closes much of it. Our method, invariant pretraining (InvPT), applies semantic-preserving transformations to the corpus and combines masked language modeling with multi-positive supervised contrastive learning that treats all augmentations of the same source function as positives, mixing self-contrast pairs (same code, different masks) with invariant-contrast pairs (transformed code) for positives of varying difficulty. Unlike prior contrastive code encoders, InvPT does not require paired natural-language data. Across our evaluation, InvPT improves robustness on transformed test sets by up to 11 percentage points on clone detection and 19 on code classification while matching or improving standard accuracy, and our ablations isolate multi-positive invariant contrast as the main source of the gains. Our aim is not a new objective but a careful measurement of where encoder robustness breaks and how far a simple, code-only recipe can recover it.

---


### 157. [ETHOS: Towards a Modular Ethics Framework for Clinical Multi-Agent Systems](https://arxiv.org/abs/2608.15424)

**<font color=#1a73e8>作者：</font>** Rakesh Sharma, Sydney Pugh, Cameron Beeche 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of large language models has enabled the development of clinical multi-agent systems (MAS) capable of integrating multimodal patient data and supporting increasingly complex clinical decision-making. However, the deployment of these systems in real-world healthcare settings raises critical ethical concerns related to safety, fairness, accountability, transparency, and patient trust. While numerous organizations, including the World Health Organization, the National Academy of Medicine, and the FUTURE-AI consortium, have proposed ethical frameworks and governance principles for healthcare AI, these efforts remain largely conceptual. To address this challenge, we present ETHOS (Ethics and Trust through Hierarchical Oversight System), a modular ethics framework designed as a governance meta-agent that can be integrated with any existing multi-agent system without requiring changes to its underlying architecture. ETHOS translates stakeholder-informed ethical requirements into executable runtime oversight through a layered governance approach consisting of deterministic checks, contextual reviews, and a final ethics critic. These components continuously evaluate intermediate reasoning steps and final outputs, enabling the system to identify ethical risks, request revisions, or suppress responses that fail predefined safety and trustworthiness criteria. We demonstrate ETHOS within a hepatology clinical decision-support MAS. Results show that ETHOS improves decision reliability by detecting incomplete, inconsistent, or out-of-scope evidence and appropriately increasing abstention when safe recommendations cannot be supported. By embedding ethical governance directly into system operation, ETHOS provides a practical and auditable mechanism for transforming high-level AI ethics principles into deployable safeguards.

---


### 158. [NumerosityVLM: A Cognitively Inspired Benchmark for Interpreting Numerosity Representations in Vision-Language Models](https://arxiv.org/abs/2608.15425)

**<font color=#1a73e8>作者：</font>** Yiming Fu, Fangjun Li, Xiujin Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong performance on high-level multimodal tasks, yet numerosity perception, a cognitive ability that emerges in human infants before language acquisition, remains poorly understood in current models, as existing counting benchmarks entangle numerosity with correlated visual factors. We introduce a cognitively inspired diagnostic benchmark, NumerosityVLM, comprising 10,800 synthetic images across six controlled conditions. The benchmark orthogonally manipulates object size, spatial arrangement, and numerosity, while progressively ablating texture, shape, and color. Evaluating seven VLMs in a zero-shot setting, multi-factor analysis reveals that model architecture explains the largest proportion of performance variance (partial $\omega^{2}=0.325$), far exceeding visual conditions. Layer-wise probing further shows that linearly separable numerosity signals consistently emerge at early stages of the vision encoder, while performance differences across evaluated models are primarily associated with the language model component. Code and data are publicly available at this https URL, and this https URL.

---


### 159. [Gated Against One Model, Open to the Next: Option-Only Solvability in Legal Multiple-Choice Benchmarks](https://arxiv.org/abs/2608.15428)

**<font color=#1a73e8>作者：</font>** Volodymyr Ovcharov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple-choice benchmarks are graded on whether a model picks the right option, not on whether it needed the question. Measuring that gap takes care: a model answering A to most items scores above chance wherever the key sits at A, and reads as recognition when it is not. We measure it on UA-JudgeExam: 11,990 four-option items with official keys, published by Ukraine's Higher Qualification Commission of Judges.
Shown the options and no question, Claude Haiku 4.5 scores 0.383 against chance, and the leak is concentrated: 11.8% of items are answered blind on all eight option orders, against 0.2 items expected by chance. It is not quotation: search over 280,059 editions of Ukrainian legislation recovers 0.128. Gating those out retains 8,128 items, on which the gating model itself now scores 0.204, and GPT-5.6, which took no part in the selection, still answers 0.515 of them with the question hidden. Scoring twelve held-out models on the whole set and subtracting each one's answer-position habit, only two keep an excess: GPT-5.6 at +0.265, Sonnet 4.6 at +0.081. Without it the ranking misleads: Llama 3.1 8B scores 0.292 blind, above every model but those two, purely by answering A to 92% of items.
The gate does select something real: on the items it rejected, eleven of twelve models score 0.518-0.789, every interval clear of what the same model scores on the items it kept. But that signal is one model's, and filtering on it does not transfer upward. Neither is visible on a 400-item sample, where nine models read as "statistically at chance". Rewriting distractors instead overshoots to 0.168, below chance and as exploitable. The same probe on LEXam returns chance: every option there points into the stem, none longer than 33 characters. Item format decides whether the problem can arise; capability decides how much is extracted. We release the corpus, the predictions and the harness.

---


### 160. [Does the Proof Prove It That Way? Faithful Formalization of Elements Proofs](https://arxiv.org/abs/2608.15432)

**<font color=#1a73e8>作者：</font>** Tadd Mao, Tianjun Zhong, Dhruva Arekar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In formal verification, both the autoformalization of statements and automated proof search have been studied extensively. While automated proof search can produce a formal proof that compiles, the generated proof does not necessarily reflect how the natural-language argument arrives at its conclusion--a property we refer to as faithfulness. With faithfully formalized proofs, one can check the reasoning behind a human- or AI-written argument, and assist mathematicians in formalizing their proof sketches. However, it is particularly challenging due to misalignment of formal proof tactics and natural language reasoning. In this work, we rigorously describe a set of five necessary conditions a faithful formal proof must satisfy, and introduce Pistis, an agentic, oracle-guided proof search that produces formal Lean proofs that satisfy them. At its core is a novel faithfulness-preserving divide-and-conquer search, which we name OrderDecompose, that tracks citation dependencies and blocks unfaithful shortcuts, paired with a refutation search, that surfaces gaps and errors in the natural language proof source. OrderDecompose completes proofs that baselines cannot close even within a 12-hour budget, and its artifacts compile over 33$\times$ as fast as prior work's. We apply Pistis on the first three books of Euclid's Elements, producing high-quality artifacts containing faithful formal proofs. Under a blinded human study and an LLM-as-a-judge protocol on rigorous rubrics, Pistis-generated proofs are favored over prior works--2.89$\times$ and 5.2$\times$ as often by human reviewers and the LLM judge, respectively. It further uncovers gaps in Euclid's proofs and their translation, and can accept or refute natural language proofs written by humans or AI, demonstrating that faithful formalization is useful as a proof-checking tool.

---


### 161. [OTel: Building Domain-Specialized Telecom LLM Foundations for Intelligent Networks](https://arxiv.org/abs/2608.15436)

**<font color=#1a73e8>作者：</font>** Farbod Tavakkoli, Roderic Paulk, Jorden Terrazas 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI models have advanced rapidly, but they still struggle with telecom-specific tasks. We present Open Telco (OTel), an open telecom AI resource with derived datasets for retrieval, reranking, instruction tuning, and safety/abstention, plus 30 full-parameter post-trained baselines across embedding, reranking, and language models. The community has already engaged substantially with the resource: as of May 3, 2026, the released models have been downloaded over 16 million times, and the project has received 157+ pieces of media coverage worldwide. Building on prior open telecom datasets and benchmarks, OTel provides documented telecom data sources, held-out evaluation partitions, trained embedding models, rerankers, context-grounded LLMs, and safety/abstention data in one unified resource. OTel post-training improves performance across all three model families: embedding retrieval reaches 93.5% NDCG@10, reranking reaches 0.952 MRR@10, and language-model correctness reaches 88.2%. We release OTel as a reproducible starting point and invite the community to expand the data, improve embedding and reranking models, and build stronger context-grounded telecom LLMs.

---


### 162. [Measuring Reward Hacking and Reasoning-Answer Decoupling Under Position-Confounded Optimization](https://arxiv.org/abs/2608.15445)

**<font color=#1a73e8>作者：</font>** Suyash Maniyar, Armaan Sandhu, Abhishek Mishra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a reward is correct on every training example yet consistent with more than one goal, a model can acquire an unintended one, a failure known as goal misgeneralization. Endpoint accuracy on the training distribution cannot tell the two apart, because solving the task and exploiting a surface feature can satisfy the reward equally well. We treat this as a measurement problem: what does a benchmark score measure once a model has been optimized against a correct but confounded signal? We train language models with GRPO on multiple-choice math problems where the correct answer is always option A, then evaluate on an unseen test set with unbiased answer positions. Across Qwen2.5, Llama 3.x and Gemma-3 models, biased training often drives option-A rates above 0.90 in smaller models and collapses unbiased accuracy toward chance, so accuracy stops measuring math ability and instead measures an answer-position policy. We further find reasoning-answer decoupling: capable models generate reasoning that reaches the correct numeric answer while still selecting A. We track this with numeric extraction and an LLM judge (GPT-4.1-mini; Qwen2.5-3B decoupling rate is about 0.66). The broken construct generalizes beyond the training domain: biased models inflate A-rates on out-of-domain MMLU and value-laden prompts. Continued training on unbiased data reverses the in-domain shift unevenly and only partially reverses the out-of-domain one, so a model can appear restored on its training distribution while remaining biased on unseen inputs. Reasoning-answer decoupling rate, together with answer distributions and out-of-domain behavior, separates capability loss from a learned, transferable shortcut.

---


### 163. [Language models suffer from a curse of ambiguity](https://arxiv.org/abs/2608.15448)

**<font color=#1a73e8>作者：</font>** Nicolas Zucchet, Hyun Dong Lee, Scott Linderman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly rely on sampling as a driver of their own improvement, making the fidelity of their learned distributions more critical than ever. Yet, not all distributions are equally easy to learn. In this work, we identify a curse of ambiguity: in large language models, and more broadly in all neural networks that produce discrete probability distributions, the more ambiguous a next-token distribution is, the harder it is to learn accurately. Through an extensive theoretical analysis, we trace this curse to architectural and learning roots. More ambiguous distributions require more capacity to be stored, larger embeddings to be represented, more steps to be fitted, and amplify token-sampling noise. We validate these findings on synthetic tasks with controlled ground truth and observe the same signatures in language models trained on real data. Our results provide a new perspective on the statistical capabilities of large language models and a practical framework for when to trust their output distribution.

---


### 164. [Mental Model Management: An Operator-Based Framework for LLM Memory](https://arxiv.org/abs/2608.15451)

**<font color=#1a73e8>作者：</font>** Oliver Kramer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models process large amounts of information but usually lack an explicit mechanism for maintaining compact and evolving conceptual representations. We introduce Mental Model Management (3M), a framework in which knowledge is represented as mental models consisting of compact chunks. Rather than accumulating text passages, 3M continuously integrates new information into an existing conceptual representation. A set of operators extracts knowledge, retrieves relevant models, adds and updates chunks, reorganizes representations, detects inconsistencies, and derives new knowledge. We describe the main 3M operators and illustrate each operation using Evolution Strategies as a running example.

---


### 165. [Dynamic Multi-Byte Prediction With Hierarchical Language Models](https://arxiv.org/abs/2608.15454)

**<font color=#1a73e8>作者：</font>** Abraham Toluwase Owodunni, Chibuzor Okocha, Christan Grant 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Byte-level hierarchical language models (LMs) have recently emerged as a robust alternative to their popular counterparts that use subword tokenization. However, generating one byte at a time remains a bottleneck for inference speed. To address this, we introduce multi-byte prediction (MBP), which generates multiple bytes in parallel, speeding up inference with minimal performance impact and no additional parameters. MBP builds on the popular multi-token prediction (MTP) paradigm with two crucial innovations. First, we introduce a variable-length prediction window that aligns with the latent tokens, or segments, of a hierarchical LM. Second, we implement a novel attention-masking scheme that enables parallel byte prediction without violating causality. We show that multi-byte prediction strikes a Pareto-optimal trade-off across multiple generative tasks, instruction following, question answering, summarization, and machine translation, achieving the best trade-off between performance and inference throughput.

---


### 166. [Not All Attention Is Equal: A Quantitative Survey of the EEI Trade-off](https://arxiv.org/abs/2608.15459)

**<font color=#1a73e8>作者：</font>** Aditya Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention mechanisms have driven machine learning for a decade, from neural machine translation to language models that do general-purpose reasoning. This survey covers four connected threads: their formulation for sequence-to-sequence tasks, adaptation to computer vision, efficiency innovations that address the quadratic bottleneck, and advances in interpretability. We define three criteria: efficiency, expressiveness, and interpretability, and compare twenty-one methods using an EEI scoring framework. Scores come from a single rater with an assumed +/-1-point perturbation range. A deterministic Monte Carlo analysis with 200,000 samples shows that, under this perturbation model, rank changes of more than one position occur in 67-70% of samples on average. A rank-matched null model reproduces a similar stability profile, so the results support coarse tier-level comparisons rather than fine-grained rankings. The survey traces attention from Bahdanau-Luong alignment through the Transformer and into vision architectures. It reviews fixed and learned sparse attention, linear attention, IO-aware exact algorithms including FlashAttention, and state-space alternatives including Mamba. It also covers induction heads, superposition, and the attention-SSM duality. We further provide a structured narrative review, a benchmark synthesis with cross-study caveats, a five-problem research gap analysis, and a 2015-2026 evolution timeline. We conclude by framing attention research as an expansion of the efficiency-expressiveness-interpretability frontier and identifying future directions including unified efficiency benchmarks, learned routing for hybrid architectures, length generalization, and scalable mechanistic interpretability.

---


### 167. [Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability](https://arxiv.org/abs/2608.15475)

**<font color=#1a73e8>作者：</font>** Yudong Gao, Linghan Chen, Wenhan Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantized Vision-Language-Action (VLA) models expose a weight-fault surface: Rowhammer-style faults can corrupt deployed INT8 bits. We present the first bit-flip attack on a VLA: a few gradient-selected flips reduce closed-loop success to $0\%$, while hundreds of random flips are harmless. Across four model variants spanning three action-head families, damaging bits concentrate in a few action-generating layers, but the empirical budget depends sharply on the head: direct regression and token policies fall in $1$--$5$ flips, whereas the evaluated flow-matching policies require ${\sim}100$--$300$. Our fixed-direction manifold-escape loss cuts \pizero{}'s budget from ${\sim}1000$ to ${\sim}100$ flips, and a matched five-direction sweep shows that the attack is not specific to an all-positive direction. On a direct head, protecting $3.1\%$ of weights preserves $60\%$ success at $K{=}100$, and protecting $5.3\%$ moves the open-loop break threshold from 3 to 100 flips. Finally, task-calibrated emulated $K{=}100$ flips yield $0/20$ real-robot successes, versus $14/20$ clean and $16/20$ global-random. Weight integrity is therefore a security boundary for embodied foundation models. Code is included as ancillary material.

---


### 168. [EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints](https://arxiv.org/abs/2608.15502)

**<font color=#1a73e8>作者：</font>** Ao Zhou, Bo Dai, Le Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have emerged as a promising foundation for Embodied AI, but their high inference cost poses significant challenges for deployment in robotic systems. In practice, on-device inference is constrained by limited compute capacity and energy budgets, struggling to simultaneously satisfy real-time control and energy efficiency requirements. Alternatively, offloading the inference workload to an edge server is susceptible to fluctuations in system conditions, introducing unpredictable latency risks. Device-edge co-inference offers a promising solution, but systematic research tailored to VLA models remains scarce, particularly a unified co-inference framework that jointly addresses real-time constraints and system-level energy efficiency. Thus, we propose EcoVLA, an adaptive device-edge co-inference framework for VLA models that maximizes system energy efficiency under real-time constraints. EcoVLA first introduces a unified stage-level abstraction over different VLA paradigms, establishing an architecture-agnostic co-inference design space. It then formulates a joint device-edge-network latency and energy prediction model to enable rapid runtime evaluation of candidate co-inference schemes. Building on this, EcoVLA continuously selects the energy-optimal scheme satisfying real-time constraints with millisecond-level overhead, adapting to runtime variations in network and system states. Furthermore, EcoVLA incorporates a lightweight transmission mechanism for inter-stage intermediate tensors to reduce the communication overhead incurred by cross-device collaboration. Experimental results across VLA models show that EcoVLA improves system energy efficiency by up to 236% over existing co-inference approaches under a 20 Hz action output frequency constraint, while consistently maintaining SLO satisfaction under dynamic network and edge workload conditions.

---


### 169. [Do Language Models Consistently Encode the Current Year?](https://arxiv.org/abs/2608.15507)

**<font color=#1a73e8>作者：</font>** Suze van Adrichem, Aditi Bhaskar, Diyi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A consistent concept of the current time is important for temporal reasoning, yet how language models represent the current time is not well understood. We contribute two tasks that probe the current year in conceptually distinct ways: an associative task, which infers the current year from verb tense, and a declarative task, which directly queries for the current year. Both tasks estimate current years within one year of the post-training data cutoff of instruction-tuned language models. For base models, predictions on the associative task serve as a strong proxy for the pre-training data cutoff, with an average error of only 10 months across 13 models. However, their internal mechanisms diverge: the associative task uses mechanisms similar to factual recall, while the declarative task lacks consistent causal pathways. This divergence poses a challenge for updating the current year in language models. None of prompting, SFT, or weight editing succeed in shifting the associative and declarative years simultaneously. Prompting updates the declarative year (94.6% success across 351 target years) but leaves the associative year nearly unchanged (1.7% success). Year-shifted SFT also fails to shift the associative year, matching the target year in only one of eight models. Weight editing, while effective for both tasks individually, does not generalize across both. Overall, our results show that the current year is not consistently encoded in language models: The associative notion, deeply ingrained in linguistic structures learned in pre-training, uses different causal mechanisms and resists the same modifications that easily shift the declarative notion learned in post-training.

---


### 170. [UniFed-VLM: Federated Instruction Tuning for Vision-Language Models with Multiple Heterogeneity](https://arxiv.org/abs/2608.15516)

**<font color=#1a73e8>作者：</font>** Pengyu Wang, Baochen Xiong, Xiaoshan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated strong performance in multimodal understanding and generation. However, fine-tuning of VLMs typically relies on centralized data, which raises privacy concerns in certain domains (e.g. healthcare). Federated Learning (FL) provides a natural solution by enabling model training without sharing raw data. However, applying FL to VLM instruction tuning is highly challenging. VLMs have substantial parameter scales, and in real-world scenarios, clients exhibit significant heterogeneity in tasks, modalities, and model architectures.
Existing methods mainly focus on simplified settings and are unable to handle such multi-dimensional heterogeneous scenarios. In this work, we study federated instruction tuning under joint heterogeneity in tasks, modalities, and model architectures.
We propose UniFed-VLM, a unified federated instruction tuning framework for VLMs that addresses multiple types of heterogeneity. It consists of two key components: 1) Federated Compensated Subspace Aggregation (FedCSA), which performs subspace-aligned aggregation of parameter-efficient adapters with dynamic weighting and compensation to mitigate heterogeneity-induced conflicts; 2) Two-stage Collaborative Distillation (TCoD), which enables effective knowledge transfer across heterogeneous models via a Mutual Distillation Adapter (MDA) and a mixture-of-experts-based distillation strategy. We conduct experiments on multiple benchmark datasets, and the results show that UniFed-VLM achieves stronger average performance across diverse tasks compared with existing FL methods. The source code is available at: this https URL.

---


### 171. [GLaQ: Grounding Latent Queries in Visual Evidence for Multimodal Reasoning](https://arxiv.org/abs/2608.15517)

**<font color=#1a73e8>作者：</font>** Zesheng Yang, Lingling Zhang, Xinyu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought reasoning has substantially improved the problem-solving capabilities of multimodal large language models. Fine-grained visual evidence, however, remains difficult to preserve and reuse across text-based reasoning steps. To address this limitation, tool-augmented thinking-with-images methods maintain visual access externally by revisiting or manipulating the image, but require predefined tools and additional inference-time processing. As an internal alternative, continuous visual latent reasoning retains intermediate computation in hidden states. However, its prevailing autoregressive construction makes each latent state depend on its predecessors, so later states may repeat information already present in the latent sequence rather than capture complementary visual details. We introduce GLaQ, a grounded latent-query framework that replaces sequential latent rollout with a fixed set of context-conditioned queries grounded in the original visual tokens. The grounded queries are reinjected for answer generation, providing direct and coordinated access to source visual evidence. We train GLaQ with localized-view supervision followed by reinforcement learning under task-level rewards. Across five benchmarks for fine-grained visual understanding and perception, GLaQ-7B gains 5.99--9.66\% over its base model and leads all compared visual latent methods, suggesting that direct query-to-image grounding can recover localized evidence from the full image without external visual operations or autoregressive latent rollouts.

---


### 172. [Why Summaries Turn Neutral: Policy Attribution for Sentiment Drift in Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2608.15530)

**<font color=#1a73e8>作者：</font>** Mikhail Krasitskii, Alexander Gelbukh, Olga Kolesnikova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with human feedback (RLHF) aligns LLMs with human preferences, improving summarization fluency and safety, but causes sentiment drift: overly neutral summaries stripped of emotional nuance. We diagnose why RL acts as a sentiment neutralizer and present Policy Attribution, a framework using gradient and logit decomposition to trace drift to reward model (RM) signals and KL (Kullback-Leibler) penalty. Sentiment drift reflects a strategic bias toward "low-risk" tokens maximizing expected rewards under preference uncertainty (Stiennon et al., 2020; Gao, Schulman, and Hilton, 2023). On Reddit TL;DR and CNN/DailyMail, RLHF summaries get higher rewards but show 30-40% lower sentiment variance. Cross-lingual analysis across eight languages shows language-independent drift, with morphologically richer languages more suppressed (Krasitskii et al., 2026). We propose and validate a sentiment-aware regularization technique reducing drift by 18-22% without harming summary quality. The code and toolkit will be public.

---


### 173. [L3Cube-IndicQuest v2: A Large-Scale Multilingual Benchmark for Evaluating Factual Knowledge of Large Language Models Across Indic Languages](https://arxiv.org/abs/2608.15535)

**<font color=#1a73e8>作者：</font>** Rinit Jain, Tirthraj Mahajan, Advait Joshi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present L3Cube-IndicQuest v2, a large-scale gold-standard multilingual question-answering benchmark for evaluating the India-specific factual knowledge of Large Language Models (LLMs). The benchmark comprises 3,471 curriculum-grounded English question--answer pairs spanning nine domains, curated from educational curricula, competitive examination materials, and domain-specific reference books. We introduce a practical hybrid construction strategy that combines context-grounded LLM-based question generation and validation with semantic deduplication and human verification, enabling scalable creation of benchmark data while preserving annotation quality. The benchmark is translated into 19 Indic languages, yielding a publicly released multilingual dataset of 69,420 question--answer pairs across 20 languages. We evaluate six LLMs under three protocols: LLM-as-a-judge and two deterministic lexical criteria, exact-substring and word-overlap matching. All three produce almost the same model ranking, showing that the results do not depend on the choice of judge. The frontier commercial model leads by a wide margin, and among open-weight models Gemma4 31B outperforms the Indic-specialised Sarvam 30B in every evaluated Indic language.

---


### 174. [CrossView: Can Vision-Language Models Reason Across Cameras?](https://arxiv.org/abs/2608.15539)

**<font color=#1a73e8>作者：</font>** Sahil Shah, S P Sharan, Harsh Goel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding benchmarks have long centered on single-camera settings, where modern multi-modal language models achieve strong performance across image and video tasks. Yet, the real world runs on multi-camera networks: autonomous vehicles, security systems, and robots all gather data across many simultaneous views. We argue that this is not simply "more" of the single-camera problem; it is fundamentally different. Multi-camera reasoning requires handling context that scales with the number of views, resolving occlusions visible from only a subset of cameras, judging which views matter, and integrating evidence across perspectives that may overlap or diverge. Current models struggle with exactly these challenges, yet no benchmark systematically targets them. We introduce CrossView, a multi-camera video question-answering benchmark spanning autonomous driving, security surveillance, egocentric/exocentric video, and robotics. Evaluation of proprietary models, such as GPT-5.2, and open-source models, like Qwen3-VL, reveals consistently low accuracy, with open-source models trailing by a wide margin. Performance scales strongly with a model's ability to jointly process multiple viewpoints, positioning CrossView as a rigorous benchmark for multi-camera video. We open-source our code and dataset at this https URL.

---


### 175. [ATLAS: Scaffold-Free Algorithm Synthesis by LLMs via Embedding-Guided Quality-Diversity Search](https://arxiv.org/abs/2608.15546)

**<font color=#1a73e8>作者：</font>** Danial Yazdani, Mohammad Nabi Omidvar, Yuan Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most LLM-based automated algorithm design methods optimize a designated component within a human-specified scaffold, fixing overall organization and component interactions. We present ATLAS, an embedding-guided quality-diversity framework for scaffold-free full-algorithm synthesis in combinatorial optimization. The problem specification supplies objectives and constraints; a minimal I/O interface fixes only instance and solution formats; the LLM chooses and restructures components, interactions, and control flow. This freedom enlarges the search space, risking invalid candidates and premature convergence to one design region. ATLAS independently detects execution, interface, and feasibility failures, recomputes objectives, and applies error-conditioned repair; similarity-based archive management preserves algorithms across embedding-space regions to counter premature convergence. Its three-layer search refines the best design, gives other regions dedicated refinement opportunities, and performs cross-region synthesis to recombine components and their interactions. Across four NP-hard problems, ATLAS outperforms several state-of-the-art component-synthesis methods and a matched full-synthesis baseline while remaining competitive with strong human-designed algorithms. One ATLAS run retains several algorithms with comparable performance from distinct embedding-space regions rather than a single design. Code inspection finds that these multi-component designs differ in their primary construction or global-search backbone. Our results suggest that embedding-guided quality-diversity search can make the enlarged full-algorithm design space practically searchable. Source code and exact executable prompts are available at <this https URL.

---


### 176. [BengaliMCQ: Automatic Generation and Answer Prediction of Academic Multiple-Choice Questions in a Low-Resource Language](https://arxiv.org/abs/2608.15547)

**<font color=#1a73e8>作者：</font>** Abu Tarabin Surzo, A.K.M. Nihalul Kabir, Sm Azmain Faysal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional retrieval-augmented generation (RAG) frameworks process documents without attending to their hierarchical structure, leading to poor performance, especially in low-resource languages such as Bengali. To address this, we propose a structure-aware RAG framework that models Bengali textbooks as hierarchical graphs and uses a contrastively trained graph neural network to retrieve a small set of relevant passages. These passages provide focused context for a large language model, enabling topic-specific multiple-choice question (MCQ) generation and in-domain answer prediction. Experimental results demonstrate that our framework outperforms strong dense retrieval baselines across retrieval metrics, produces more relevant MCQs, and achieves superior answer prediction accuracy.

---


### 177. [Adoption of Generative AI in the Workplace: Increasing and Shifting the Balance of Productivity and Communication Activity](https://arxiv.org/abs/2608.15550)

**<font color=#1a73e8>作者：</font>** Yulin Yu, Yan Chen, Rui Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is transforming the workplace by augmenting and automating cognitive tasks, reshaping how organizations work and innovate while raising questions about workplace inequality and the future of work. Despite rapid adoption, empirical evidence on how these tools alter work practices and generate productivity gains remains limited. We examine how AI use affects the quantity and nature of information work using digital trace data from the Microsoft M365 application suite across multiple large international companies. Specifically, we study how generative AI adoption shifts the balance between communication and productivity-oriented activities, such as content creation in Word. Difference-in-Differences analyses show that AI adoption is associated with significant increases in both productivity (21.2%) and communication (7.1%) application actions among users who used the AI system more than 100 times over a 20-week post-adoption period. Among users with 100-500 AI use instances, higher AI usage is also associated with continued increases in both types of activity. The smaller increase in communication represents an overall shift toward individual, documentation-focused work and reflects mixed changes in communication, including decreases in reading and organizing email, compared with more uniform increases in productivity actions. These findings suggest potential efficiency gains and reductions in information overload, while highlighting the need to ensure that AI adoption does not weaken interpersonal communication and the diffusion of diverse information that supports innovation.

---


### 178. [Admission Without Answers: Label-Free Certification and Experience Learning for LLM-Based Optimization Modeling](https://arxiv.org/abs/2608.15565)

**<font color=#1a73e8>作者：</font>** Junbo Jacob Lian, Huiling Chen, Hanzhang Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Experience-learning agents for optimization modeling improve by storing verified skills, but existing learners admit knowledge by checking against known answers, which real ticket streams do not provide. The natural label-free alternatives are unreliable: on a 300-problem label-blind stream, admitting every executable model poisons roughly one admission in four, while single-instance agreement accepts models that match at one value but differ elsewhere. We propose AdmitOR, an admission gate built on calibrated external behavioral evidence. Candidates from three model families, prompting strategies, and solver stacks are run on instances resampled from an extracted parameter domain; agreement across the resulting value-function traces is summarized by a cross-family clique, and a calibrated threshold returns accept, abstain, or escalate. The preregistered false-discovery criterion holds on calibration data but not on the wild stream. We report this negative result in full and trace most failures to benchmark texts that do not faithfully encode their labeled instances. Comparing four admission judges on one collection of logs inside a state-of-the-art skill learner, AdmitOR raises admission precision to 0.927, against 0.871 for majority vote and 0.726 for execution success, yielding 3.1x and 8.0x fewer poisoned admissions. Its library is the smallest and attains the highest macro accuracy across five public benchmarks, 58.4 against 54.8 for majority vote and 53.9 for the ground-truth-labeled library. The 3.5-point gain over majority vote is supported by a paired bootstrap and survives correction for a host-side anomaly. To our knowledge, AdmitOR is the first label-free admission mechanism designed around an explicitly calibrated false-discovery target. The transfer failure identifies a necessary condition for extending it to wild streams.

---


### 179. [SchurQuant: Groupwise Discrete Optimization for Layer-Wise LLM Quantization](https://arxiv.org/abs/2608.15567)

**<font color=#1a73e8>作者：</font>** Gunjun Lee, Sehwan Son, Younjoo Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-only post-training quantization (PTQ) enables the deployment of large language models under tight memory budgets, but accuracy often collapses at 2-3 bits. Existing backpropagation-free PTQ optimizers have two limitations: group decisions ignore the correction that the remaining continuous suffix can absorb, and discrete refinements typically keep the affine quantization grid fixed. We introduce SCHUROPT, which analytically eliminates the suffix's optimal continuous response, yielding an exact groupwise quadratic with Schur-complement curvature. It then alternates closed-form row-wise scale/zero-point refitting with coordinate descent over integer codes. With the GPTQ objective fixed, SCHUROPT improves mean zero-shot accuracy on 2-bit Qwen3-4B by 11.88 percentage points (pp). At higher precision, however, tighter reconstruction does not consistently improve end-model metrics. SCHURQUANT therefore combines SCHUROPT with quantized-prefix teacher reconstruction, reference-weight regularization, residual-add targets, and teacher-decision token weighting. Across eight Llama and Qwen models, SCHURQUANT achieves the highest mean zero-shot accuracy among the evaluated backpropagation free PTQ baselines, outperforming the strongest baseline by 9.65 pp at 2 bits.

---


### 180. [Catching Hallucinated Citations in Video-LLM Question Answering: A Self-Verification Pipeline and Verifier Ablation Study](https://arxiv.org/abs/2608.15574)

**<font color=#1a73e8>作者：</font>** Yogesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video question answering systems built on vision-language models often produce timestamped claims with high confidence even when unsupported by the cited frame. This deceptive hallucination arises because timestamps imply grounding without ensuring correctness, increasing user trust but not accuracy. We introduce a pipeline that closes this loop. A retrieval-augmented language model drafts answers with per-claim timestamp citations, and each cited frame is independently re-examined before being shown to the user. We compare against a plain baseline and ablate three verification designs, evaluated on both Apple Silicon (MLX) and Google Colab (HF Transformers, CUDA). Directly asking the vision model whether a frame supports a claim fails completely (0% catch rate on 40 claims) due to sycophancy. Blind re-captioning plus a general LLM judge improves results but is unstable, oscillating between 0% and 100% flagged depending on prompt phrasing. Replacing that judge with a small natural language inference model yields a stable, interpretable verifier that catches 79% of fabricated claims on adversarial false-premise questions while leaving true claims untouched. We release the full pipeline, evaluation harness, and implementations for both Apple Silicon and Colab. Code is available at this https URL.

---


### 181. [From Generalist to Specialist: A Context-Fusion Framework for Endoscopic Polyp Reporting with a Frozen VLM](https://arxiv.org/abs/2608.15580)

**<font color=#1a73e8>作者：</font>** Ruijie Yang, Yan Zhu, Peiyao Fu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable endoscopic polyp reporting requires integrating quantitative lesion sizing, standardized Paris classification, and clinically meaningful morphological description within a single record. General-purpose vision-language models (VLMs) offer a unified interface for image understanding and report generation. Existing specialization strategies, however, typically rely on task-specific models or model-weight adaptation, leaving unresolved how to introduce reliable specialist knowledge while preserving both this unified interface and the VLM's pretrained capabilities. We introduce a context-fusion framework that specializes a frozen general-purpose VLM through both implicit instruction context and explicit transduction context without modifying its pretrained weights. Specifically, a self-supervised polyp encoder retrieves related image-report pairs as explicit, query-specific evidence, while learned continuous specialist tokens provide implicit instruction context shared across cases. Experiments were conducted on 2,056 expert-annotated public endoscopic images. We compared the framework with general-purpose VLMs, task-specific predictors, and weight-adaptation methods to assess specialist performance, unified reporting, and adaptation efficiency. Across numerical, categorical, and report-generation metrics, the proposed framework substantially improved direct frozen-VLM inference and achieved the strongest overall performance among the evaluated methods. It added trainable parameters equal to only 0.006% of the frozen VLM's parameter count. When the top-1 retrieved case carried the correct target category, our framework corrected 70.5% of the errors made by a weight-adaptation baseline. These findings support the context-fusion framework as a lightweight and effective strategy for specialist adaptation of a frozen VLM.

---


### 182. [GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix](https://arxiv.org/abs/2608.15584)

**<font color=#1a73e8>作者：</font>** Jinhyun Jeon, Sungjoo Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production paged-serving engines apply uniform paging granularity to the KV cache, even though the two regions of a multi-agent workload have opposite storage requirements: a long shared prefix demands contiguity, while the per-request suffix demands fine-grained allocation.
We present \textbf{GraniKV}, a KV-cache layer that allocates the shared prefix in a contiguous HOT pool and the suffix in a token-level COLD pool, combined with a per-step dispatcher which selects the appropriate backend among dual backends for each regime (compute-, memory-, or communication-bound). To the best of our knowledge, GraniKV is the first system to apply asymmetric paging granularity to the KV cache of a production paged-serving engine.
At $L_p{=}16$\,K shared tokens GraniKV reaches $\mathbf{2.16\times}$, $\mathbf{1.98\times}$, and $\mathbf{1.57\times}$ output-token throughput over the production baseline on Llama-3.1-8B/TP=1, Qwen-2.5-14B/TP=2, and Qwen-2.5-32B/TP=4. The gain decomposes: cascade attention integration contributes the majority at saturation; the asymmetric storage layer adds $1.05$--$1.15\times$ end-to-end while being what makes the batched-GEMM prefix backend possible at all. Under heterogeneous multi-agent serving with \emph{distinct} prompts of different lengths, the attribution inverts: GraniKV sustains $\mathbf{1.95\times}$ while batch-global cascade collapses to parity --- the storage layer alone carries the win in the regime that motivates the paper.

---


### 183. [Agent Gym: A Framework for Continuous Evaluation and Evolution of LLM Agents Through Human-in-the-Loop Feedback](https://arxiv.org/abs/2608.15591)

**<font color=#1a73e8>作者：</font>** Pouya Ghiasnezhad Omran, Michael Zimmermann, Duncan Cambridge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents deployed in production environments face a fundamental tension: the agent's behavior is frozen at deployment time, while the business rules and edge cases it must handle continue to evolve. Existing approaches address agent construction and one-time evaluation but provide no structured mechanism for continuous post-deployment behavioral correction without modifying the agent's source code. Most of the approaches offered in the market, require intense collection of logs and traces, and re-examining the agent design by the engineering team, a process which is heavy, long and negates the economical value of agentic transformation. We introduce Agent Gym, a modular, domain-agnostic framework that wraps any existing LLM-based agent in a continuous evaluation-and-evolution loop. The framework provides six composable capabilities --- Act, Evaluate, Investigate, Correct, Learn, and Observe --- organized across three architectural zones: a constitution layer that codifies domain knowledge in configuration artifacts, a runtime inference pipeline that chains acting, investigation, and adaptive correction, and a learning loop that enables subject matter experts to discover and validate new correction rules through natural language interaction. The key technical contributions include a hybrid deterministic-LLM correction engine with 21 condition operators and three-tier actions, a three-layer investigation architecture for ground-truth-free compliance validation, and a programmatic safety loop that guarantees rule correctness before human approval. We further introduce the Spec-to-Note Gap, an autoencoder-inspired view of agentic system transparency. An open-source reference implementation for invoice processing demonstrates that the framework is fully operational and ready for adoption.

---


### 184. [When Entropy Is Not Enough: Reclaiming Lost Semantics in LLM Output Length Prediction](https://arxiv.org/abs/2608.15592)

**<font color=#1a73e8>作者：</font>** Feiyang Ren, Shengtao Wen, Lingbing Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient LLM serving is often bottlenecked by the need to pad sequences to a fixed maximum length, and this wastes compute and degrades throughput. Predicting output lengths in advance makes it possible to adopt length-aware scheduling, and this reduces the overhead. This advantage is especially pronounced in long-context reasoning and reinforcement learning applications. Existing approaches, such as entropy-guided token pooling, use token-wise entropy as their primary signal, but they tend to ignore differences in semantic content across tokens. So, important tokens are often underweighted, and tokens carrying little information receive disproportionate emphasis. This hurts the reliability of length prediction. We introduce ESTP (Entropy-and-Semantic Token Pooling), a lightweight framework that addresses this issue by combining entropy with attention-based importance scores. These scores are derived directly from the self-attention weights computed during the LLM prefill phase, and this allows ESTP to capture both uncertainty and semantic importance with minimal additional computation. Since the framework reuses prefill activations, it adds almost no extra memory overhead and introduces only minimal latency. On the ForeLen benchmark, ESTP outperforms baseline methods, achieves better prediction accuracy and lower error rates in most scenarios. When integrated with a length-aware scheduler in end-to-end system tests, it further helps improve overall throughput and reduce the padding ratio. Our results offer a practical and effective building block for length-aware LLM serving systems.

---


### 185. [VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation](https://arxiv.org/abs/2608.15600)

**<font color=#1a73e8>作者：</font>** Mingyu Yuan, Shengtao Wen, Lingbing Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The widespread circulation of abusive online content has increased the need for reliable moderation of Chinese social-media text. Existing Chinese benchmarks support label classification, fine-grained toxicity categorization, and target-aware extraction, but do not provide a unified representation for deterministically verifying the stated basis of a moderation decision. We introduce VARM-Bench, a benchmark for field-anchored chain-of-thought rationales in Chinese abusive-speech moderation. Each instance contains a concise natural-language rationale with explicit anchors for six decisions: target, target type, target explicitness, author stance, harmfulness label, and fine-grained category. Our deterministic protocol evaluates field correctness, target alignment, output validity, complete-record agreement, and hidden record errors conditioned on correct final decisions, without relying on an LLM judge. Under a common structured-output protocol, we evaluate language models across multiple model families using zero-shot prompting, taxonomy guidance, and structured CoT supervision, and analyze lexical-cue sensitivity and field-level errors. Results show that strong label-level performance can conceal substantial errors in complete moderation records. VARM-Bench provides an auditable and reproducible benchmark for evaluating verifiable moderation rationales in Chinese abusive-speech moderation.

---


### 186. [FluxBin: Flexible LUT-based Ultra-low-bit LLM Inference by Algorithm-Kernel Synergy](https://arxiv.org/abs/2608.15602)

**<font color=#1a73e8>作者：</font>** Qingyao Yang, Runming Yang, He Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While binary quantization theoretically promises extreme compression and acceleration for Large Language Models (LLMs), existing research often overlooks the necessity of specialized hardware kernels, thus failing to unleash the full acceleration potential due to persistent reliance on expensive floating-point arithmetic or runtime dequantization overheads. To bridge this gap, we propose FluxBin (\textbf{F}lexible \textbf{L}UT-based \textbf{U}ltra-low-bit e\textbf{X}ecution with \textbf{Bin}ary bases), an algorithm-kernel co-design that synergizes post-training quantization with a highly optimized CUDA kernel. Algorithmically, we introduce Decoupled Row-Column Binary Decomposition to enhance representational capacity while maintaining hardware efficiency, complemented by a Hessian-guided saliency-aware hybrid bases that preserve critical information. At the kernel level, we implement a Lookup Table Building Approach with Scale Fusion to reduce floating-point arithmetic, featuring a Virtual Columnar Mapping that transforms irregular, sparse, and salient matrices into dense execution. Extensive evaluations demonstrate FluxBin achieves up to $5.92\times$ speedup and $10.19\times$ energy savings across diverse model architectures, delivering comparable accuracy to heavily fine-tuned methods. This effectively enables the deployment of 70B-scale models on one single A100 GPU with a $4\times$ memory reduction. Code is available at this https URL.

---


### 187. [AlloEgo-VLM: Disambiguating Allocentric and Egocentric Reference Frames in Vision-Language Models](https://arxiv.org/abs/2608.15605)

**<font color=#1a73e8>作者：</font>** Kuan-Lin Chen, Tzu-Ti Wei, Chao-Chi Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study investigates the challenge of ambiguity faced by Vision-Language Models (VLMs) in understanding spatial semantics. Spatial cognition, shaped by cognitive psychology, spatial science, and cultural context, often assigns directionality to objects. However, natural language descriptions of spatial relations frequently omit explicit reference frames, leading to semantic ambiguity and potentially serious errors for embodied AI robots. Existing VLMs, due to insufficient training on reference frames and object orientations, often produce inconsistent responses. To address this issue, we construct a new dataset, AlloEgo-View, comprising (image, query, view-specific answer) triplets that capture key object relations from both allocentric and egocentric perspectives. The view-specific descriptions follow a structured spatial representation that annotate detailed scene descriptions, reference and target objects, their orientations, reference frames, and view types. Building on AlloEgo-View, we develop AlloEgo-VLM, a framework to disambiguate allocentric and egocentric reference frames, even under ambiguous queries, and to be easily integrated into existing VLMs via supervised fine-tuning. Furthermore, we deploy our framework onto an embodied robotic platform within NVIDIA Isaac Sim to validate its real-world feasibility in open-ended object searching tasks. Experiments highlight the limitations of current VLMs in handling view-specific queries and demonstrate the strong disambiguation ability of AlloEgo-VLM.

---


### 188. [EgoGazeLite: On-Device Egocentric Gaze Prediction for Token-Efficient Multimodal LLM Video Input](https://arxiv.org/abs/2608.15614)

**<font color=#1a73e8>作者：</font>** Matteo Stoiber, Niels Buus Lassen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The use of multimodal LLMs (MLLMs) for egocentric video understanding with wearable devices is constrained by the token budget. Memory and compute cost scale with the number of visual tokens, and high-resolution video quickly becomes expensive to transmit and process at scale. Prior work (GazeLLM) addresses this by cropping the video around the camera wearer's gaze. This reduces the number of visual tokens by about tenfold while maintaining or improving the quality of full-resolution descriptions. However, this compression strategy depends on dedicated eye-tracking hardware, which is unavailable on consumer smart glasses. Building a software-only substitute poses a joint constraint: the predictor must be accurate enough to preserve downstream description quality, yet light enough to run on-device, within the power and compute budget of a smartphone. We address this with EgoGazeLite, a lightweight dual-process gaze predictor for egocentric video. Across two MLLMs, three automated metrics, and two LLM judges, predicted-gaze crops show no significant difference from ground-truth-gaze crops. Equivalence is confirmed in all ten cases. EgoGazeLite achieves this at 15.7M parameters, 6.71 GFLOPs, and runs the full gaze-and-crop pipeline end-to-end in real time (21.6 ms/frame) on consumer accelerator hardware. Together, these results remove the need for eye-tracking hardware for token-efficient, gaze-conditioned egocentric video understanding with MLLMs.

---


### 189. [Do Assessment Instruments Measure the Same Thing for Humans and LLMs? A Latent Structure Analysis](https://arxiv.org/abs/2608.15630)

**<font color=#1a73e8>作者：</font>** Alona Strugatski, Licol Zeinfeld, Giora Alexandron  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rapid development and growing deployment of large language models (LLMs) have made it increasingly important to understand their capabilities. A common approach is to evaluate LLMs using assessment instruments originally designed to measure skills and competencies in humans, such as standardized exams, and to use performance on these instruments as evidence for generalizable claims about LLMs' underlying abilities on the same skills the assessments are intended to measure in humans. However, from a validity perspective, such inferences require that the relationship between observed performance and underlying constructs established for humans also holds for LLMs. In particular, a necessary condition for transferring score interpretations is similarity in the latent structure of responses to the assessment. In this study, we examine whether this condition holds in two educational contexts: high-school chemistry and a quantitative reasoning section of a university entrance exam. Using a case study design, we compare human response data with responses generated by six multimodal LLMs. Our analytical approach combines exploratory factor analysis, factor congruence, and resampling to assess latent structure similarity across human learners and LLMs. Across both instruments, we find systematic differences between human and LLM factor structures, showing evidence that the analyzed assessments may not measure the same constructs for humans and LLMs. These findings call into question the validity of evaluation practices that use educational assessments to make claims about AI capabilities.

---


### 190. [Argumentation for Common Ground: Finding Zones of Possible Agreement between Individuals in Conflict](https://arxiv.org/abs/2608.15634)

**<font color=#1a73e8>作者：</font>** Elisa Cavatorta, Antonio Rago  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How can common ground between societies in conflict be identified when citizens' acceptability of peace agreements is shaped by contested narratives? Such acceptability is mediated not only by the clauses that agreements include or exclude, but crucially by citizens' subjective reasoning concerning agreements' clauses. In this paper, we leverage computational argumentation to introduce a novel approach to identifying mutually acceptable agreements among individuals in conflict, i.e. a Zone of Possible Agreement (ZOPA). First, we introduce a quantitative bipolar argumentation framework tailored to represent each side's reasoning about peace agreements. We then show how merging these frameworks can enable negotiators to identify peace agreements that are mutually acceptable. To evaluate our approach under conditions of real-world relevance, we focus on the Palestinian-Israeli conflict, where long-standing policy, practitioner and public interest underscores the demand for methods capable of analysing polarised public reasoning. We show how our framework identifies a ZOPA through theoretical analysis and preliminary experiments using survey data from both existing work and retrieved by a large language model. The results illustrate how argumentation can empower negotiators and conflict-resolution teams in mapping feasible ZOPAs grounded in citizens' reasoning.

---


### 191. [When Stories Evolve: Benchmarking LLM Storytelling Across Agent Architectures in Open-Ended World Simulations](https://arxiv.org/abs/2608.15654)

**<font color=#1a73e8>作者：</font>** Yuqi Chen, Sixuan Li, Yunfeng Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can write fluent stories, but open-ended storytelling requires more than local fluency. In evolving world simulations and AI-native games, models must preserve facts, relationships, causal dependencies, and character states as the world changes. We introduce WSE-bench, a process benchmark that separately evaluates sustained generation, canonical coherence, and meaningful development in dynamic LLM storytelling. Generation Coverage records the proportion of planned narrative steps produced; Consistency tracks when canon breaks; and Richness measures how meaningfully branching, player-shaped trajectories develop. Across frontier models, Consistency and Richness do not form a smooth trade-off: their empirical Pareto frontier is non-concave, with several non-dominated intermediate configurations that no positive linear weighting can select. Added structure can enrich trajectories, but it does not uniformly improve coherence and may shorten them. Model scale chiefly improves sustained generation, without producing reliable gains in canonical coherence or meaningful development. These results show that sustained generation, canonical coherence, and meaningful development are distinct and sometimes competing capacities. WSE-bench makes those dynamics visible by extending narrative evaluation from finished stories to the processes that create them.

---


### 192. [SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates](https://arxiv.org/abs/2608.15665)

**<font color=#1a73e8>作者：</font>** Ziming Yu, Shuyao Xiao, Xingyu Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization enables backpropagation-free fine-tuning of large language models, but existing ZO methods suffer from high-variance gradient estimators, making convergence unstable and highly sensitive to learning rates. We propose SubZero+, an improved SubZero framework that improves stability in three complementary ways: (i) multi-query gradient estimation within layer-specific low-rank subspaces to reduce variance without exhibiting the multi-query paradox; (ii) a subspace Adam optimizer that performs adaptive updates using in-subspace multi-query gradient statistics; and (iii) a sign correction for QR-based subspace construction to ensure Haar-distributed projection matrices, eliminating implementation-dependent orientation ambiguity. Experiments on models from 1.3B to 32B across SuperGLUE, under both full-parameter tuning and LoRA, show that SubZero+ consistently outperforms prior ZO baselines, enlarges the stable learning-rate range, and narrows the gap to first-order methods with minimal extra memory overhead.

---


### 193. [Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search](https://arxiv.org/abs/2608.15669)

**<font color=#1a73e8>作者：</font>** Zhongwei Yu, Yan Song, Xue Yan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery often involves optimising expensive-to-evaluate objectives over vast, structured, and open-ended hypothesis spaces, such as molecules, protein sequences, and computer programs. Generative models such as large language models (LLMs) provide expressive priors over such spaces, but their likelihoods and self-assessments are unreliable proxies for the objectives and calibrated epistemic uncertainty, especially for novel candidates outside the observed data distribution. We introduce the Large Discovery Model (LDM), an empirically grounded recurrent architecture that couples a generative model with a Bayesian non-parametric reward surrogate model. The generative model proposes and refines candidate designs, while the surrogate predicts their performance and quantifies uncertainty, yielding an uncertainty-aware value that guides candidate generation, refinement, and selection. The discovery memory and the surrogate model are continually updated as each new experimental observation arrives. We evaluate LDM on three scenarios spanning different design modalities and objectives, including neural-network training, antibody design, and molecular optimisation. Compared to LLM-only reflection or traditional statistical search across these domains, LDM achieves a $2.4\times$ greater reduction in validation BPB, an $18.2\%$ relative decrease in binding energy, and more than $60\%$ relative gains in molecular multi-objective performance. These results suggests that LDM could serve as a general-purpose discovery engine for effective search over open-ended hypothesis spaces.

---


### 194. [THESIS-MoE: Trainable Hierarchical Extraction and SteerIng of Sycophancy in Mixture-of-Experts](https://arxiv.org/abs/2608.15687)

**<font color=#1a73e8>作者：</font>** Kareem Hassani, Chaymaa Abbas, Lama Mawlawi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sycophancy, the tendency of a language model to change its answer to match a user's stated belief, is a common alignment failure. Existing activation steering methods typically apply a single contrastive direction uniformly throughout the model, which is an unconditional intervention that alters activations even when no sycophantic behavior is present, trading knowledge retention for behavioral correction. In Mixture-of-Experts (MoE) models, prior work further suggests that behavior is encoded within expert computations rather than routing decisions alone, making precise behavioral steering particularly challenging. In this work, we introduce a shared contrastive signal, built from matched prompts with and without a stated belief, that identifies where sycophancy lives across the MoE hierarchy and drives interventions that act only where the behavior is present. We formulate localization as a causal search over a granularity ladder of MoE blocks, experts, attention blocks, and heads, and compare unconditional subtraction against two conditional alternatives: an analytic projection-based subtraction and a learned per-token gate that steers the model away from sycophancy while keeping its weights frozen. We evaluate on three MoE models measuring sycophancy alongside general knowledge and reasoning benchmarks. Our conditional interventions removed up to 90\% of the belief-induced sycophancy. Our results demonstrate that sycophancy resides in identifiable computational subcircuits and can be selectively steered while maintaining a favorable removal-retention trade-off.

---


### 195. [Large Models for Small Devices: Recent Advances and Empirical Analysis of Edge AI Deployment](https://arxiv.org/abs/2608.15693)

**<font color=#1a73e8>作者：</font>** Subhransu Das, Jiaming Cheng, Arnav Kumar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running large AI models on resource-constrained edge devices requires model compression to reduce model size and computation. What compresses well, however, need not deploy well. We survey dozens of recent works that report compression results on real hardware and extract practical deployment guidelines from them. Following these guidelines, we deploy compact language and image models on GPU, CPU, and Raspberry Pi platforms across question answering and image segmentation. No single technique wins across tasks. For question answering, Qwen3.5 0.8B reaches 93.85 SQuAD F1 and 92 EM under Q5_K_M GGUF quantization, while structured pruning at the same precision costs 16 F1 at a 1% ratio. For segmentation, the ranking reverses: default quantization leaves parameters and MACs unchanged, whereas pruning cuts model size by nearly 80% at near-constant mIoU. Pruning can even inflate the deployed artifact by 21-49% by breaking k-quant super-block alignment; combined with longer, less format-compliant outputs, this raises Raspberry Pi latency up to 3.4x. Compression can also manufacture the appearance of competence rather than destroy it visibly: one LoRA-recovered variant stays fully parseable and holds 71% strict BoolQ accuracy while sending 97 of 100 predictions to a single class, at 52.6% balanced accuracy. We explain these effects through neural-flow graph analysis and prefill-decode-level latency decomposition, and condense them into task-specific deployment research directions. The right technique depends on the task, the model, and the hardware. Our experiment code and artifacts are open-sourced at this https URL

---


### 196. [ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment in Visual Document Retrieval](https://arxiv.org/abs/2608.15698)

**<font color=#1a73e8>作者：</font>** Peng Chunyi, Xu Zhipeng, Yan Yukun 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual document retrieval is a critical component of multimodal retrieval-augmented generation, aiming to identify query-relevant pages from document collections where evidence is distributed across text, layout, charts, and visual structures. Recent efforts toward finer-grained supervision primarily rely on textual descriptions or localized visual regions as evidence proxies. However, such supervision signals may either overlook complex visual structures or provide incomplete and inaccurate representations of the underlying evidence. To address these limitations, we propose ConceptFormer, a latent concept representation learning framework for visual document retrieval. ConceptFormer models query-relevant evidence as continuous, query-conditioned latent concepts that explicitly bridge localized visual evidence and semantic relevance, without requiring either textual intermediate representations or direct reliance on raw visual annotations. During training, ConceptFormer employs a strong vision-language model to dynamically determine the number of latent concept tokens and uses these concepts as an intermediate representation to bridge the semantic gap between queries and documents, thereby guiding the learning of the embedding space. Experiments on diverse visual document retrieval benchmarks demonstrate that ConceptFormer achieves 16.7\% and 22.1\% relative improvements in average NDCG@10 over the strongest visual retrieval baseline and the strongest OCR-based text retrieval baseline, respectively. Further analysis reveals that latent concepts effectively connect localized visual evidence with semantic relevance, enabling the retriever to capture both fine-grained textual cues and complex document-level visual structures while preserving strong retrieval alignment. Codes and data are available at this https URL.

---


### 197. [HyMem: Hierarchical Context Management for Long-Horizon Agents via Information Isolation](https://arxiv.org/abs/2608.15703)

**<font color=#1a73e8>作者：</font>** XinQi Wang, Jinwei Xiao, Sijia Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents often perform poorly on complex, long-horizon tasks because their context becomes increasingly cluttered over time. As interactions accumulate, detailed execution traces and intermediate outputs dominate the context, making it difficult for the model to retain and use high-level planning information. Most existing methods address this issue through compression or retrieval applied to a single, flat context, which does not clearly separate different types of context information and often leads to degraded reasoning. To address this challenge, we propose HyMem, a hierarchical framework that explicitly separates the agent's context into distinct functional layers. HyMem organizes context by function to separate high-level planning from execution and complex analysis. Its isolated reasoning module handles complex subtasks without adding intermediate reasoning traces to the persistent planning context, while its memory management module preserves task progress across context refreshes through structured summaries. These components reduce redundant context accumulation, retain task-critical information, and support coherent long-horizon reasoning within a limited context window. Experiments on GAIA and Browsecomp-plus show that, with DeepSeek-V4, HyMem achieves average Pass@1 scores of 66.7% and 61.3%, outperforming the strongest baseline by 6.1 and 4.7 percentage points, respectively. Further analysis indicates that HyMem effectively controls the growth of the reasoning context, allowing the model to maintain focus and accuracy across complex, long-horizon tasks.

---


### 198. [Beyond Single Object: Learning 3D Relations with Large Language Models](https://arxiv.org/abs/2608.15710)

**<font color=#1a73e8>作者：</font>** Kohsuke Ide, Ryousuke Yamada, Yue Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address a fundamental gap in 3D-LLMs: existing models focus on single-object/scene description, struggling with detailed, inter-object comparison. We propose a framework for detailed object-level reasoning across multiple objects with three components: (1) MO3D (Multi-Object in 3D), an instruction dataset requiring fine-grained multi-object comparison; (2) Multi-3DLLM, using a minimal Patch-Interaction Transformer (PIT) that models inter-/intra-object relationships while preserving local geometry; (3) Mini-apps, two application-driven benchmarks (Shape Mating, Change Captioning) that probe geometric understanding for practical use. Recent 3D-LLMs and 2D-VLMs perform poorly on these tasks, lacking both comparison-centric design and geometric awareness. In contrast, Multi-3DLLM trained on our mixture data learns geometric reasoning, surpasses all baselines on MO3D, and provides positive transfer to single-object classification.

---


### 199. [Propaganda Forensics: Recovering the Generation Pipeline of an AI-Driven Influence Campaign](https://arxiv.org/abs/2608.15746)

**<font color=#1a73e8>作者：</font>** Benjamin Icard, Elouan Vuichard, Louis Lefebvre 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a forensic analysis of the generation pipeline behind a recent AI-driven influence campaign. We introduce PROPAGIA, a corpus of 2,646 propagandist French articles from the Storm-1516/CopyCop campaign disclosed by VIGINUM and INSIKT GROUP in 2025. For comparison, we rely on SIPA, a corpus of human-written French mainstream press from the same period. Using topic modeling, vagueness and sentiment analysis, we first isolate persuasion techniques characteristic of propaganda, with PROPAGIA far exceeding SIPA in vagueness, subjectivity and negativity, and citing fewer sources. We then find prompt instruction leaks on 50 of the 84 PROPAGIA websites, including a verbatim ten-point editorial specification accounting for several of these differences, together with high cross-article redundancy. Finally, we show that rewriting-based detection supports INSIKT GROUP's attribution to the Llama 3 family, but also suggests the involvement of Mistral-family models.

---


### 200. [Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents](https://arxiv.org/abs/2608.15755)

**<font color=#1a73e8>作者：</font>** Meiling Tao, Yiling Tao, Peng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User-centric multi-turn agents must act on an evolving task situation shaped by changing user intents, accumulated tool-grounded facts, missing information, and execution constraints. Existing context-management methods improve the use of past interaction history, but rarely maintain an explicit situation state that separates grounded facts from task-state judgments. As a result, agents often need to infer fine-grained attributes, task dependencies, and constraint satisfaction implicitly from dialogue traces. We propose Intent-Driven Situation States (IDSS), a training-free framework that maintains an explicit situation state alongside the dialogue. IDSS parses tool returns into provenance-aware entities and attributes, tracks user intents, required variables, constraints, and execution status, and propagates new facts to task constraints to update action executability. This allows agents to avoid infeasible actions, advance dependent goals, and reuse relevant information without repeatedly searching raw history. Experiments on three interactive benchmarks across eight LLMs show that IDSS improves task completion, preference elicitation, and interaction efficiency, with clear gains on tasks involving multi-entity coordination, evolving user constraints, and constraint-aware replanning. Ablations and error analyses show that these improvements come from the interaction between fact persistence, intent-centered state tracking, and constraint modeling. These results suggest that explicit situation tracking offers an effective alternative to history-centric context management for reliable user-centric multi-turn agents.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
