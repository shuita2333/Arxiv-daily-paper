# 🧠 大模型相关研究 | 2026年06月16日

> 本类共 **66** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-66](./part-02.md)

---

### 1. [UP-NRPA: User Portrait based Nested Rollout Policy Adaptation for Planning with Large Language Models in Goal-oriented Dialogue Systems](https://arxiv.org/abs/2606.13683)

**<font color=#1a73e8>作者：</font>** Hui Wang, Fafa Zhang, Meng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To address the challenge that current dialogue policy planning methods struggle to dynamically adapt to diverse user characteristics, this paper proposes a User Portrait based Nested Rollout Policy Adaptation (UP-NRPA) online framework with Large Language Models. In contrast to conventional approaches dependent on model training and require offline reinforcement learning policy models for user groups, UP-NRPA enables dynamic customization of dialogue strategies through an adaptive mechanism. This is achieved by leveraging real-time user feedback alongside personality, preferences, and objectives mapped from the current user portrait, thereby adapting to user characteristics without offline reinforcement learning. In collaborative and non-collaborative dialogue benchmarks, UP-NRPA demonstrated considerable benefits, achieving an impressive 100% success rate in multiple dialogue tasks. Particularly in negotiation tasks, the sale-to-list ratio (SL) increased by 56.41%. This demonstrates that UP-NRPA can adapt to diverse user needs without requiring a training mechanism, enabling the dialogue system to adapt to user characteristics.

---


### 2. [The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2606.13685)

**<font color=#1a73e8>作者：</font>** Abel Yagubyan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge is now widely used to rank model outputs, train reward models, and populate public leaderboards, but its run-to-run reliability remains under-characterized. We study repeated identical evaluations on 29 tasks spanning 10 categories using two OpenAI judge models (GPT-4o-mini and GPT-4.1-mini), with 50 pairwise trials and 50 pointwise trials per question, supplemented by temperature and prompt-sensitivity ablations. Across judges, pairwise preferences flip on average 13.6% of the time, with 28% of questions exceeding a 20% flip rate and one question reaching 56%. GPT-4o-mini also exhibits a significant first-position bias (72% A-majority, p = 0.024). At the same time, mean pointwise score gaps are small (0.19--0.36 on a 10-point scale) and not statistically significant in aggregate, producing a pairwise--pointwise gap: judges frequently choose a winner even when their own scalar scores provide little evidence of a meaningful quality difference. Beyond within-judge instability, cross-judge agreement is only 76% ($\kappa = 0.51$), semantically equivalent prompt templates change majority outcomes in 25% of tested cases, and deterministic decoding reduces but does not eliminate inconsistency. A reliability curve analysis shows that, in our dataset, 11 repeated trials are needed for a majority vote to recover the 50-trial reference verdict with 95% probability on average, rising to 15 for high-variance questions. These findings suggest that single-trial LLM judging is often too noisy for high-stakes evaluation, and that multi-trial aggregation, position randomization, and explicit uncertainty reporting should be standard practice. Because both judges are from a single provider, cross-provider replication remains an important next step.

---


### 3. [Can Editing 1 Neuron Fix Repetition Loops in LLMs?](https://arxiv.org/abs/2606.13705)

**<font color=#1a73e8>作者：</font>** Aristotelis Lazaridis, Aman Sharma, Dylan Bates 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Yes. Can it cure doom loops? Probably not.
The Gemma 4 instruction-tuned models share a reproducible failure: on long factual enumeration prompts, such as listing every episode of a TV series, the 88 IAU constellations, or the 151 original Pokemon, they collapse into repetition, either a tight verbatim loop or a list whose entries decay onto a single answer. These loops occur at rates as high as 95% and survive prompt rewording, inference-engine changes, and most sampling adjustments. In this paper we explore whether this behavior is localized enough to remove by weight edits. To localize the cause, we use per-layer ablation and per-neuron attribution, then confirm the strongest candidates with full-generation sweeps. The loops trace to a small set of MLP neurons (or, in the 26B-A4B Mixture-of-Experts model, a few routed experts) which we suppress with static weight edits. These "surgeries" can be as small as a single sign-inverted neuron (in the E2B model). The size of the effective edits grows with model scale, but in all cases, the loop patterns can be addressed at normal generation budgets while preserving general-purpose benchmark scores. However, the edits do not solve everything: we also study longer thinking budgets, where the two larger models most visibly enter doom looping, i.e. a non-convergent regime in which the model self-corrects in circles over a fact it cannot recall, exhausting the budget without committing to a final answer. We show this residual failure is reduced but not eliminated by the same edits, and argue it is fundamentally a knowledge-precision problem rather than a removable circuit; weight surgery can delete a loop, but it cannot supply a missing fact. Our results are both a feasibility demonstration, that is, evidence that a concrete generation pathology can be localized to a few parameters and edited out, and a delineation of where that approach stops.

---


### 4. [Orchestra-o1: Omnimodal Agent Orchestration](https://arxiv.org/abs/2606.13707)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Vireo Zhang, Shengju Qian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The recent success of agent swarms has shifted the paradigm of large language model (LLM)-based agents from single-agent workflows to multi-agent systems, highlighting the importance of agent orchestration for task decomposition and collaboration. However, existing orchestration frameworks are limited to a narrow set of modalities and struggle to generalize to more complex settings where heterogeneous modalities coexist and interact. This limitation becomes particularly pronounced in omnimodal scenarios, where tasks require the unified understanding and coordination of diverse inputs such as text, image, audio, and video. In this work, we propose Orchestra-o1, an omnimodal agent orchestration framework designed to support efficient agent collaboration across multiple modalities. Orchestra-o1 introduces a unified orchestration mechanism that enables modality-aware task decomposition, online sub-agent specialization, and parallel sub-task execution. This scalable design allows agent systems to effectively tackle complex real-world tasks involving heterogeneous information sources, surpassing the second-best approach by 10.3% accuracy on the OmniGAIA benchmark. Furthermore, we introduce decision-aligned group relative policy optimization (DA-GRPO), an efficient agentic reinforcement learning approach for training Orchestra-o1-8B, which also achieves state-of-the-art performance against all existing open-source omnimodal agents.

---


### 5. [YeasierAgent: Agentic Social Sandbox as a Canvas for Intent-Driven Creation of Platform-Agnostic Symbiotic Agent-Native Applications](https://arxiv.org/abs/2606.13722)

**<font color=#1a73e8>作者：</font>** Jory He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces YeasierAgent, an application-building paradigm based on symbiotic agents, narrative worlds, and scene-aware interaction. It challenges the conventional device-coupled model of software by redefining applications as collaborative spaces among users, agents, and worlds. We present a system architecture that achieves two primary contributions: (1) enabling the rapid, cross-platform construction of agent-native applications by utilizing platform-agnostic interactive units (agents, scenes, dialogue) rather than fixed graphical layouts; and (2) unifying the emotional companionship and practical tool execution attributes of intelligent agents within a single experiential sandbox. By integrating automated generation, user-created worlds, and spatial multi-agent collaboration, YeasierAgent formalizes the category of Symbiotic Agent-Native Applications, demonstrating a shift from isolated, tool-specific chatbots toward cohesive, socially embedded computational environments.

---


### 6. [TwinBI: An Agentic Digital Twin for Efficient Augmented Interactions with Business Intelligence Dashboards](https://arxiv.org/abs/2606.13731)

**<font color=#1a73e8>作者：</font>** Jisoo Jang Wen-Syan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Business intelligence (BI) increasingly combines dashboard interaction with LLM-based assistance, but these two modes often fall out of sync during multi-step analysis. As users switch between direct dashboard manipulation and natural-language queries, it becomes difficult to preserve a consistent analytical state across filters, hierarchies, metrics, and chart context. We present TwinBI, an agentic digital-twin framework that couples an LLM-based agent system with an executable BI dashboard state. TwinBI unifies conversational interaction, dashboard manipulation, semantic grounding, and provenance tracking through a shared analytical state reconstructed from a unified interaction log. It also exposes artifacts such as schema views, SQL, logs, and an /insights command for state-grounded analytical summaries. We evaluate TwinBI in two complementary ways. In a controlled A/B benchmark with the same backbone agent, TwinBI improves exact-match accuracy from 43.3% to 63.3%, partial-credit accuracy from 48.3% to 70.8%, and substantially reduces timeout rate from 40.0% to 10.0% relative to Dashboard alone. In a usability study, participants benefited from the integrated dashboard-and-chat workflow, with high task accuracy, moderate workload, and favorable ratings for state-aware interaction mechanisms. These results suggest that TwinBI improves both agent-level analytical reliability and user-facing analytical support by turning visible dashboard state into richer actionable context. Our dataset and source code are available at: this https URL

---


### 7. [Efficient On-Device Diffusion LLM Inference with Mobile NPU](https://arxiv.org/abs/2606.13740)

**<font color=#1a73e8>作者：</font>** Tuowei Wang, Yanfan Sun, Ju Ren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) accelerate generation by denoising multiple tokens in parallel, making them attractive for latency-sensitive mobile inference. However, repeated denoising introduces substantial computation on smartphones. Mobile neural processing units (NPUs) offer high-throughput dense matrix computation, but efficiently exploiting them remains challenging: token commitment shrinks per-block effective workloads, token revision complicates KV cache reuse, and limited NPU-visible address space incurs costly remapping and data transfer overheads.
In this paper, we propose this http URL, the first NPU-aware inference framework for accelerating dLLMs on smartphones. this http URL aligns block-wise dLLM inference with the execution characteristics of mobile NPUs through three techniques. (1) Multi-Block Speculative Decoding fills the shrinking workload in late-stage current-block decoding with speculative future-block tokens. (2) Dual-Path Progressive Revision keeps committed tokens revisable until stable and refreshes unstable tokens through a CPU-side path without stalling dense NPU execution. (3) Swap-Optimized Memory Runtime compacts NPU-visible address layouts and overlaps data staging with NPU computation to reduce remapping and transfer overheads. We implement this http URL as an end-to-end framework and evaluate it across diverse hardware platforms and dLLM workloads. this http URL reduces LLaDA-8B generation latency by 17x-42x over the CPU baseline with prefix KV cache reuse, while preserving generation quality.

---


### 8. [Large Language Models as Supervised Extraction Assistants: Lowering the Barrier to Documentation Standard Adoption in Agent-Based Modelling](https://arxiv.org/abs/2606.13749)

**<font color=#1a73e8>作者：</font>** Peer-Olaf Siebers, Christopher Frantz  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agent-Based Modelling (ABM) relies on clear documentation to ensure credibility and transparency. Although standards exist for documenting models (e.g. ODD), processes (e.g. TRACE, EABSS), and data use (e.g. RAT-RS), their adoption remains limited due to the effort required to produce documentation that is often treated as supplementary. This paper explores the use of Large Language Models (LLMs) to facilitate and partially automate such processes. We conduct a feasibility study focusing on the underused Rigour and Transparency Reporting Standard (RAT-RS), using four LLMs to extract reports from a published ABM paper. We assess consistency and performance across question types, finding that LLMs generate coherent outputs and perform more reliably on descriptive than on explanatory or evaluative tasks. While LLMs can improve reporting quality and consistency, they also exhibit notable limitations. We identify practical heuristics for when LLM-assisted documentation is reliable and when human oversight is needed and call for systematic community-level exploration to enhance rigour and adoption in ABM reporting.

---


### 9. [QIAS 2026: Overview of the Shared Task on Islamic Inheritance Reasoning](https://arxiv.org/abs/2606.13756)

**<font color=#1a73e8>作者：</font>** Abdessalam Bouchekif, Somaya Eltanbouly, Samer Rashwani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a comprehensive overview of the QIAS 2026 shared task, organized as part of the OSACT7 Workshop and co-located with LREC 2026. The shared task was designed to evaluate the ability of large language models to perform complex reasoning in the religious and legal domain of Islamic inheritance. Unlike conventional question-answering benchmarks, QIAS 2026 focuses on end-to-end reasoning from natural language cases, requiring systems to perform the full inheritance calculation process, from identifying the eligible heirs to assigning the correct share to each beneficiary. To support this evaluation, the task was based on the MAWARITH benchmark, a dataset of $12{,}500$ Arabic inheritance cases annotated with intermediate reasoning steps and final answers. System submissions were evaluated using MIR-E, a multi-step metric that measures performance across the main stages of inheritance reasoning. A total of $16$ teams participated in the shared task, investigating a range of approaches, including prompting-based methods, retrieval-augmented generation, and fine-tuning strategies. The results show that Islamic inheritance remains a highly challenging benchmark for current language models, especially in stages that require precise legal interpretation and structured numerical reasoning. This overview summarizes the task design, dataset, evaluation framework, participating systems, and main results.

---


### 10. [MA-ProofBench: A Two-Tiered Evaluation of LLMs for Theorem Proving in Mathematical Analysis](https://arxiv.org/abs/2606.13782)

**<font color=#1a73e8>作者：</font>** Lushi Pu, Weiming Zhang, Xinheng Xie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have made notable progress in automated theorem proving, yet existing formal benchmarks remain limited in both mathematical coverage and difficulty. Most are concentrated in areas that are easier to formalize, such as algebra and elementary number theory, and provide limited coverage of subfields that require deeper reasoning, including mathematical analysis. To address this gap, we introduce MA-ProofBench, to the best of our knowledge, the first formal theorem-proving benchmark dedicated to Mathematical Analysis. The benchmark contains 200 formalized theorems covering 6 core topics and 27 subcategories, including measure and integration theory, complex analysis, and functional analysis. The problems are divided into two difficulty levels, an undergraduate level (Level I, 100 problems) and a Ph.D. qualifying level (Level II, 100 problems), to evaluate how well LLMs perform formal reasoning at different mathematical depths. Each problem is constructed through a human-led, LLM-assisted formalization pipeline followed by independent expert review, ensuring that the formal statements remain faithful to the original mathematics. We evaluate a range of recent general-purpose reasoning models and formal theorem provers on MA-ProofBench. However, most models perform poorly: even the best-performing model, GPT-5.5, achieves only 16% Pass@8 on Level I and 5% on Level II, while most models stay close to 0% on Level II. Further analysis identifies Mathlib hallucinations and incomplete proofs as the two dominant failure modes, while an evaluation on the natural-language version of the benchmark exposes a clear gap between informal and formal reasoning. MA-ProofBench is intended to serve as a reliable reference for tracking progress in formal mathematical reasoning in advanced domains.

---


### 11. [The Culture Funnel: You Can't Align What isn't in the Data](https://arxiv.org/abs/2606.13808)

**<font color=#1a73e8>作者：</font>** Ananya Sahu, Mehrnaz Mofakhami, Daniel D'Souza 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current cultural alignment approaches focus on inference-time interventions, assuming models already contain sufficient cultural knowledge. We argue modern LLM pipelines suffer from a cultural data funnel. Using a multidimensional tagging framework across pretraining, fine-tuning, alignment, and reasoning datasets, we show explicit cultural signals decline sharply during post-training, while geographically concentrated, task-specialized data dominates. Multilinguality enhances geographic diversity of cultural knowledge but does not ensure balanced representation. Our tags improve downstream cultural benchmark performance, demonstrating that advances require shifting focus in training data pipelines. To facilitate future research, we release our culturally tagged dataset with 5.6M samples at this https URL.

---


### 12. [Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs](https://arxiv.org/abs/2606.13815)

**<font color=#1a73e8>作者：</font>** Pratham Singla, Shivank Garg, Vihan Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Strategic reasoning under uncertainty underpins consequential decisions in negotiation, finance, and policy, but prevailing game-play benchmarks collapse heterogeneous reasoning dimensions into a single scalar, leaving the capability structure of frontier LLMs unexamined. We introduce Poker Arena, a no-limit Texas Hold'em tournament platform that couples a three-layer memory architecture (within-hand, session, and cross-session) with a nine-axis cognitive profile decomposing strategic reasoning into interpretable dimensions such as bet-sizing calibration and positional awareness. We evaluate seven frontier models across 50 sessions of 1,000 hands and a controlled memory ablation; tournament chips and aggregate axis score order the field differently: Claude Opus 4.6 wins +$15,730 chips with 14 first-place finishes, yet ranks only fifth of seven on mean axis score, while persistent memory helps some models and hurts others. These findings show that multi-axis evaluation surfaces capability structure that scalar leaderboards systematically misrank, with cross-dimensional consistency outweighing peak performance on any single axis.

---


### 13. [When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation](https://arxiv.org/abs/2606.13835)

**<font color=#1a73e8>作者：</font>** Gustavo H. Santos, Aline Carneiro Viana, Thiago H. Silva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based generative agents are increasingly used in urban simulators, yet it remains unclear whether they reproduce empirically realistic human mobility patterns or merely generate plausible mobility narratives. We introduce a validation framework for evaluating the mobility of generative agents of LLM-based urban simulators against real-world mobility data. For this, we use mobility laws, temporal rhythms, network motifs, semantic activity transitions, and behavioral mobility profiles. Using datasets from the Greater Paris region and Shanghai, we evaluate AgentSociety and CitySim across multiple dimensions of mobility realism. Our analysis reveals a substantial gap between narrative plausibility and empirical mobility realism. Although the simulators capture some high-level semantic activity distributions, they struggle to reproduce core spatial and temporal constraints, including realistic trip-length distributions, origin-destination flows, dwell times, and transition dynamics. We further observe that realistic mobility diversity is unstable across default prompting configurations and may require explicit profile-aware initialization. To support reproducible evaluation, we also contribute scalable and open LLM-driven infrastructure for regional-scale map generation, observability-enhanced simulation, mobility-metric computation, and traffic simulation. Our findings highlight the need for rigorous empirical validation of LLM-based urban simulators and provide practical tools for building more realistic and reproducible urban simulation systems.

---


### 14. [SpheriCity: Designing Trustworthy Conversational AI for Sustainability Decision Support](https://arxiv.org/abs/2606.13854)

**<font color=#1a73e8>作者：</font>** Ahmed Qayyum, Madison Werner, Kathryn Youngblood 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present SpheriCity, an expert-grounded conversational prototype designed to support trustworthy knowledge sensemaking from sustainability reports. City-level circularity assessment reports contain rich information about materials, infrastructure, and policy interventions, yet their length and heterogeneous structure make cross-document synthesis and comparison difficult for practitioners and researchers working on circular economy initiatives. While large language models (LLM) promise faster knowledge access and synthesis, their opaque reasoning, hallucinations, and lack of source transparency introduce risks for trust and interpretability, and require verification in high-stakes sustainability contexts. SpheriCity addresses these challenges through a provenance-first conversational agent that foregrounds evidence traceability, structured synthesis, and interaction scaffolds to support exploratory querying and cross-document synthesis across sustainability reports. We conducted a formative expert review with six sustainability experts using representative queries spanning cross-city comparison, policy summarization, and recommendation-oriented tasks. Experts evaluated responses across dimensions and provided qualitative reflections on the system's usefulness for sustainability knowledge work. Our results reveal that transparent sourcing, contextual explanation, interpretability, and alignment with expert workflow strongly shape expert trust and judgments of system usefulness. This work contributes (1) a conversational prototype for sustainability knowledge sensemaking, (2) an expert-grounded evaluation framework for assessing AI responses in high-stakes knowledge domains, and (3) design insights into how provenance, uncertainty communication, and integration in workflow influence expert users' trust in AI assistance for sustainability decision support.

---


### 15. [Mirage Probes: How Vision Models Fake Visual Understanding](https://arxiv.org/abs/2606.13870)

**<font color=#1a73e8>作者：</font>** Daniel Ben-Levi, Judah Goldfeder, Weiliang Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can answer image-based questions confidently, and often correctly, even when no image is provided. This mirage behavior inflates benchmark scores without reflecting visual grounding. Prior work treats this as a single failure mode. We argue it is two. Using Mirage Probes, a contrastive probing framework that pairs paraphrased question variants with matched mirage and non-mirage labels on the same image, we show that mirage behavior is linearly decodable from internal activations across residual stream, MLP, post-attention, and attention-head sites in two open-source VLMs. We demonstrate that a Naive Bayes text baseline cannot recover this signal, ruling out surface lexical confounds. Cross-benchmark separability patterns, together with a novel Prior Harnessing Index (PHI) measuring how much a model can answer from text alone, expose two distinct regimes: textual biases, where the model answers from language priors without engaging visual representations, and spurious images, where it constructs false visual content in latent space and answers as if grounded. The distinction has direct mitigation consequences: text-distribution cleaning can address the first regime but cannot reach the second, since spurious-image mirages live in the model's visual representations rather than its text. Faithful visual grounding will require interventions at the representational level.

---


### 16. [Avatar V: Scaling Video-Reference Avatar Video Generation](https://arxiv.org/abs/2606.13872)

**<font color=#1a73e8>作者：</font>** Benjamin Liang, Ce Chen, Desmond Lin 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating avatar videos that are not merely visually similar to a target individual but behaviorally recognizable, faithfully reproducing their talking rhythm, gestural tendencies, and expression dynamics, remains an open challenge. Existing methods predominantly condition on single static images, which provide insufficient identity information and cannot capture dynamic motion traits, while standard pixel-level objectives underserve the perceptually critical facial regions that determine avatar fidelity. We present Avatar V, a production-scale framework that addresses these limitations through video-reference-conditioned identity modeling. Rather than compressing identity into fixed-size embeddings, the model conditions directly on the full token sequence of a reference video, learning to reproduce both static identity attributes (facial geometry, skin texture) and dynamic behavioral patterns (talking rhythm, micro-expressions) through attention over the reference context. We introduce Sparse Reference Attention, an asymmetric mechanism achieving linear-complexity conditioning on arbitrarily long references; a motion representation stream enabling closed-loop talking style transfer; and an identity-aware super-resolution refiner inheriting the full reference conditioning. These are supported by a data engine curating 100M+ training clips from 50M raw videos, and a five-stage training pipeline with flow matching pre-training, personality fine-tuning, two-phase distillation (>10x acceleration), and RLHF alignment, deployed across thousands of GPUs. Avatar V generates 1080p videos of unlimited duration, achieving state-of-the-art identity preservation, lip synchronization, and generation quality on our cross-scene benchmark, consistently outperforming leading systems including Seedance 2.0, Kling O3 Pro, Veo 3.1, and OmniHuman 1.5 in both automated metrics and human evaluation.

---


### 17. [Natively Unlearnable Large Language Models](https://arxiv.org/abs/2606.13873)

**<font color=#1a73e8>作者：</font>** Gaurav R. Ghosal, Pratyush Maini, Aditi Raghunathan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning aims to remove the influence of specific training data sources, but this has proved challenging because the contributions of different sources are entangled within the model. Isolating source contributions to disjoint parameters makes removal easier, though it obstructs joint learning across sources. We propose NULLs (Natively Unlearnable LLMs), a model class that satisfies the two opposing goals of isolating source-specific contributions and learning jointly across sources, by training a set of shared backbone neurons alongside a pool of sparsely activated sinks. During training, information specific to a source naturally concentrates in its sinks while information shared across sources accumulates in the backbone. A source is then unlearned at deployment by disabling its corresponding sinks, with no gradient updates and no access to the retained data. We show that NULLs scales to Wikipedia's ~6M articles, isolating each as an independent source. Unlearning a single article removes knowledge specific to it while preserving facts shared with semantically related articles, closely matching retraining from scratch. We note that unlearning with NULLs is also robust: in a case study of unlearning the Harry Potter books, NULLs resists both adversarial extraction and relearning that reverses post-hoc unlearning. Finally, NULLs preserves general language capabilities, matching a standard transformer on downstream benchmarks. Together, these results suggest that source-level unlearning need not be an afterthought. It can be built natively into LLM training while retaining the benefits of shared representation learning.

---


### 18. [Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for Least-Privilege LLM Agents](https://arxiv.org/abs/2606.13884)

**<font color=#1a73e8>作者：</font>** Laxmipriya Ganesh Iyer, Rahul Suresh Babu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern decision systems increasingly rely on learned components whose outputs may be confident yet wrong, exposing downstream actions to costly errors. We introduce Risk-Aware Causal Gating (RACG), a framework that decides whether to act on, defer, or abstain from a model's prediction by combining causal effect estimation with calibrated risk control. RACG models the causal pathway from candidate actions to outcomes and gates each decision according to an estimated counterfactual risk rather than raw predictive confidence. To make gating reliable, we derive distribution-free bounds on the probability of acting under high-risk conditions and show how these bounds translate into operating thresholds that satisfy user-specified safety constraints. We further propose an adaptive gating policy that adjusts to distribution shift by monitoring discrepancies between predicted and realized outcomes, tightening the gate when causal assumptions appear violated. Across simulated interventions and real-world decision benchmarks, RACG reduces high-cost errors substantially while preserving most of the utility of an ungated policy, and it outperforms confidence-based and selective-prediction baselines at matched abstention rates. Our results indicate that explicitly separating causal risk from predictive uncertainty yields decision systems that are both safer and more transparent, offering a principled mechanism for trustworthy automation in high-stakes settings.

---


### 19. [DLawBench: Evaluating LLMs Through Multi-Turn Legal Consultation](https://arxiv.org/abs/2606.13931)

**<font color=#1a73e8>作者：</font>** Li Zhang, Yuzhen Shi, Yiran Hu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lawyer-client consultation is a critical starting point for legal services. Effective legal assistance hinges on eliciting sufficient and truthful information from clients in order to devise strategies that best protect their interests. This task requires Large Language Models (LLMs) not only to perform robust legal reasoning, but also to strategically elicit material facts through multi-turn interactions and effectively guide clients with diverse personalities. Yet existing legal benchmarks overlook this interactive capability. To fill this gap, we introduce DLawBench, a diagnostic benchmark for real-world legal consultation. Drawing on realistic client behavior, we characterize lawyer-client interactions into four types: Cooperative, Dependent, Withdrawn, and Adversarial. Using dialogues grounded in real cases, DLawBench evaluates whether LLMs can effectively conduct legal consultation under realistic conditions. DLawBench comprises 461 cases from Chinese and U.S. law, 5,532 paired fact entries, 3,411 inquiry rubrics, and 3,348 issue-resolution rubrics, and evaluates 26 representative LLMs. Systematic experiments show substantial headroom: the best-performing model, GPT-5.5, achieves only 0.562 on consultation-grounded legal reasoning. More importantly, DLawBench exposes both sycophancy in legal consultation and a paradox: models perform worse when clients need guidance most.

---


### 20. [Can Post-Training Turn LLMs into Good Medical Coders? An Empirical Study of Generative ICD Coding](https://arxiv.org/abs/2606.13940)

**<font color=#1a73e8>作者：</font>** Ziqing Wang, Weihao Li, Shijie Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated International Classification of Diseases (ICD) coding is a core medical-coding task for billing, epidemiology, and clinical decision support. Generative large language models (LLMs) are often reported as weak medical coders, but this finding mainly comes from inference-time settings such as prompting, retrieval, reranking, or tool use, leaving the role of task-specific post-training underexplored. We present a controlled empirical study of post-training for generative ICD coding, comparing discriminative baselines with LLM coders across prompting, supervised fine-tuning, and reinforcement learning under a common protocol and metric set. To our knowledge, this is the first study to evaluate RL-based post-training for generative LLM coders in ICD coding. We further introduce PHI, a diagnostic curriculum that extends GRPO to refine missed-code cases. Our results show that prompting-only evaluation substantially underestimates the potential of LLMs for ICD coding. SFT provides the main capability jump, GRPO further improves code-set prediction beyond SFT, and PHI provides targeted gains on macro-level performance. These findings suggest that the main bottleneck is not the generative formulation alone, but how the model is adapted and optimized for full-taxonomy recall. We release our code, data splits, and checkpoints at this https URL.

---


### 21. [LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values](https://arxiv.org/abs/2606.13944)

**<font color=#1a73e8>作者：</font>** Filip Trhlik, Aoife O'Flynn, Angela Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly characterised in recent evaluation work as having stable, model-level preference and value systems. However, accompanying robustness checks are limited to incidental prompt perturbations such as syntax variation and option reordering. This leaves open whether the measured properties survive when the surrounding task context changes, as it does in most real deployments. We test this directly across two established pairwise paradigms: ranking country preferences and eliciting utility judgements. In both, we make the deployment context -- the high-level task the model is performing while making concrete value-dependent choices -- our controlled variable, varied across framings such as writing a Reddit post or a news article. Across five LLMs and over 1.2M pairwise decisions, deployment context produces variation far larger than prompt paraphrasing and temperature controls. In country preference rankings over 15 countries, context induces widespread, statistically significant rank shifts; the aggregate Global North favouritism reported in prior work is itself context-dependent, with each model's bias shifting systematically across contexts. In utility elicitation over 50 outcomes, broad cross-category ordering is preserved, but fine-grained rankings within domains vary substantially, and cardinal exchange rates between outcomes (e.g. how many lives in one region equal one in another) shift by a factor of 2.47 at the median. Reported model-level preferences and utilities are therefore better understood as context-conditioned measurements than fixed model-level properties: safety guarantees obtained under one framing provide limited assurance in another.

---


### 22. [The Holistic Storage of Verb+Up Phrases in Text-based and Audio-based Language Models](https://arxiv.org/abs/2606.13993)

**<font color=#1a73e8>作者：</font>** Zachary Nicholas Houghton, Yu Zhou, Dan Pluth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A crucial aspect of linguistic capability is the ability to trade off between stored representations and abstract knowledge: one must retrieve learned representations, but also generate novel ones by applying productive rules. While recent work has examined abstract knowledge in language models, holistic storage of multi-word units has received far less attention. We probe internal representations in text-based LLMs and an ASR model, testing whether V+up phrasal verbs develop distinct representations as a function of frequency and predictability. All models show evidence of holistic storage driven by frequency and predictability, further supporting usage-based theories of language.

---


### 23. [Context-Guided Semantic Alignment for Feature Fusion Networks](https://arxiv.org/abs/2606.14005)

**<font color=#1a73e8>作者：</font>** Hyungseop Lee, Jiho Lee, Woochul Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature fusion networks are fundamental components in modern object detectors, aggregating multi-scale features to detect objects of varying sizes. However, directly fusing features from different pyramid levels often introduces semantic inconsistency due to their heterogeneous representations. In this paper, we propose Feature Interaction NEtwork (FINE), a lightweight semantic alignment module that refines low-level features via high-level contextual guidance using cross-level attention prior to fusion. To bridge the structural gap and ensure computational efficiency, we introduce an Alignment-Aware Token Sampling that aligns corresponding spatial regions across scales, reducing the attention complexity by an order of magnitude. The resulting attention weights generate a spatial-channel modulation map that is upsampled and applied to the low-level features via residual element-wise modulation. This mechanism ensures that the network selectively enhances semantically relevant pixels while preserving the sub-pixel localization accuracy necessary for dense prediction tasks. FINE is generally applicable to various detectors and consistently improves detection accuracy without compromising efficiency.

---


### 24. [GarmentSketch: Large-scale Sketch-to-Fashion Benchmark](https://arxiv.org/abs/2606.14025)

**<font color=#1a73e8>作者：</font>** Duong-Duy-Khang Bui, Minh-Tan Pham, Tam V. Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fashion sketching is a cornerstone of design workflows, allowing rapid visualization of creative concepts prior to physical prototyping. Yet, progress in sketch-based fashion image synthesis has been hindered by the absence of large-scale, high-quality paired resources. To bridge this gap, we present GarmentSketch, a novel dataset comprising 26,249 fashion sketches across 21 garment categories, each paired with detailed textual descriptions. Captions were produced through a multi-stage pipeline that integrates multiple multimodal large language models (MLLMs) with human-in-the-loop refinement, ensuring both semantic accuracy and descriptive richness. We benchmark GarmentSketch on state-of-the-art generative models, providing baseline performance for sketch-guided text-to-image generation. Our experiments reveal both the promise and the current limitations of existing methods. By offering a comprehensive and richly annotated resource, GarmentSketch establishes a foundation for advancing sketch understanding, fine-grained fashion image generation, and creative human-AI collaboration in design. The dataset will be available at: this https URL.

---


### 25. [Right or Wrong, Models Comply: Directional Blindness in LLM Moral Judgment](https://arxiv.org/abs/2606.14037)

**<font color=#1a73e8>作者：</font>** Jihye Kim, Jeffrey Flanigan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language models take integrated roles across many domains, the response of LLMs to user pushback becomes a critical alignment property. Yet many existing evaluations treat compliance as unidirectional, measuring whether models resist pressure but not whether they resist it selectively. We introduce Compliance Asymmetry (A = BCR/HCR), a bidirectional diagnostic that compares beneficial output change under helpful nudges with harmful change under misleading nudges. Across 9 models and 972,000 nudge-condition responses, we find that this selectivity differs in factual and moral judgments: models follow helpful nudges more than harmful ones on factual questions (A = 1.58), but follow both directions at nearly identical rates on moral questions (A = 1.04). This phenomenon persists across model families, capability levels, and nudging types. Interestingly, we also find that chain-of-thought prompting amplifies helpful and harmful compliance together, while identity-based prompting suppresses both by nearly identical margins. These results identify direction-blind moral compliance as a distinct failure mode in current LLMs and suggest that alignment should target directionally calibrated updating rather than lower compliance alone.

---


### 26. [Harsher on Male? Evaluating LLMs on Gender-Asymmetric Moral Framing Across Diverse Conflict Scenarios](https://arxiv.org/abs/2606.14068)

**<font color=#1a73e8>作者：</font>** Guangzong Si, Dong Wang, Zhenhao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing studies on gender bias in LLMs have largely focused on stereotypes, occupational associations, or explicit harmful outputs. In this work, we ask whether LLMs apply consistent response standards to the same negative behavior under matched male-actor and female-actor conditions. We introduce GAMA-Bench, a gender-mirrored benchmark of 1,298 scenarios covering intimate relationship and public social conflicts. It constructs gender-neutral misconduct templates through controlled grids and cross-model review, then compiles them into paired first-person prompts with matched actor-gender and role-reference variations. We further design a structured response-framing protocol to measure how models allocate punishment, empathy, escalation, instruction, and blame. Experiments on 10 representative LLMs reveal a consistent male-disadvantaging asymmetry: male actors receive more punitive, escalatory, and blame-centered framing, whereas female actors receive more therapeutic and empathy-oriented framing for the same misconduct. Further analyses show that this pattern persists across model families, scenario tracks, model scale, and explicit thinking-style reasoning. The official code is available at this https URL.

---


### 27. [Clay-CNN Hybrids: Leveraging Geo-Foundational Models as Auxiliary Context for Landslide Detection](https://arxiv.org/abs/2606.14081)

**<font color=#1a73e8>作者：</font>** Huong Binh Vu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid post-event landslide mapping is essential for disaster response but remains difficult to automate due to extreme class imbalance. This study evaluates whether Clay v1.5, a Geo-Foundational Model (GFM), can improve pixel-level landslide segmentation on the Landslide4Sense (L4S) benchmark, which contains 3,799 training chips with 14 Sentinel-2 and terrain bands and approximately 2% positive pixels. We compare three strategies: Clay as the primary encoder with multi-scale residual terrain fusion, a U-Net backbone augmented with Clay semantic context at the bottleneck, and a standard U-Net baseline. The hybrid U-Net + Clay model with two-stage Low-Rank Adaptation (LoRA) achieved the best test F1 of 64.5 +/- 1.8% over three seeds, surpassing the Clay-only backbone (55.2 +/- 3.6%) and the U-Net baseline (59.9%). Clay as a standalone encoder underperformed the U-Net due to the absence of multi-scale skip connections, but its pretrained representations consistently improved performance when injected as auxiliary context. These findings suggest that GFMs are most effective for landslide detection when they complement spatially detailed convolutional architectures rather than replace them.

---


### 28. [FactoryLLM: A Safe and Open-Source AI Playground for Evaluating LLMs in Smart Factories](https://arxiv.org/abs/2606.14119)

**<font color=#1a73e8>作者：</font>** Yash Pulse, Yong-Bin Kang, Abhik Banerjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fault diagnostics and recovery in smart factories is challenging because critical information is dispersed across manuals of multiple machines which are interconnected through the manufacturing process. Large Language Models (LLMs) can provide a promising approach. In this paper, we propose FactoryLLM, a safe and open-source AI playground designed for evaluating different LLM-based retrieval-augmented generation (RAG) models by analysing documents from multiple machines across the manufacturing process. FactoryLLM enables the user to configure the LLM, and assess performance when reasoning over multiple documents, through a dual evaluation setup using both RAGAS and NVIDIA's LLM-as-a-Judge metrics. FactoryLLM is safe because it allows users to run local or open-source LLMs without sharing sensitive industrial data, providing a controlled environment for experimentation. We demonstrate the efficacy of FactoryLLM through a case study which involves an Autonomous Intelligent Vehicle and its Mobile Planner software, evaluating three LLMs across 30 maintenance queries derived from approximately 600 pages of cross-machine documentation. The results suggest that FactoryLLM is effective in cross-machine document reasoning: every model achieved a groundedness score above 0.88. The full code and documentation for community to test FactoryLLM with their manufacturing specific scenarios are publicly available.

---


### 29. [Beyond Perplexity: UTF-8 Validity in Byte-aware Language Models](https://arxiv.org/abs/2606.14122)

**<font color=#1a73e8>作者：</font>** Sangwhan Moon, Daisuke Oba, Youmi Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Byte-level tokenization enables language models to handle any Unicode input, but models can generate invalid UTF-8 sequences when encountering rare or unseen characters. We investigate the relationship between training scale and UTF-8 generation reliability with a 355M parameter model trained on 80B tokens from a balanced multilingual corpus of English, Japanese, Korean, and Chinese. We introduce multiple evaluation protocols that isolate UTF-8 structural validity from language modeling. UTF-8 validity convergence lags perplexity by a roughly a factor of two: perplexity stabilizes after 2.1B tokens, but UTF-8 validity requires 4.2B tokens. In context-free generation, rare characters achieve higher structural validity than common characters, suggesting over-specialization of frequent character representations. Through experiments, we observed that reliable UTF-8 generation is a distinct capability requiring evaluation beyond perplexity.

---


### 30. [Implicit Reasoning for Large Language Model-based Generative Recommendation](https://arxiv.org/abs/2606.14142)

**<font color=#1a73e8>作者：</font>** Yinhan He, Liam Collins, Bhuvesh Kumar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly adopted as backbones for Generative Recommendation (GR), promising access to pretrained world knowledge. Yet reliably invoking this knowledge for GR remains poorly understood. A key obstacle is that LLM-based GR typically represents items with Semantic IDs (SIDs), disrupting LLMs' natural-language reasoning interface because these tokens are unseen by the LLM during pretraining. Existing approaches address this with expensive multi-stage pipelines that ground SIDs and elicit explicit rationales, but offer limited insight into when and why each stage is necessary. In this work, we systematically decompose explicit reasoning training pipelines for LLM-based GR, revealing three key limitations: weakened world-knowledge verbalization, misalignment between SID and natural-language token embedding spaces, and sensitivity to rationale quality, all of which hurt explicit reasoning performance. To circumvent these issues, we propose PauseRec, a lightweight implicit reasoning paradigm tailored for GR. PauseRec is exceptionally practical, avoiding costly reasoning trace acquisition and reasoning alignment training, leading to a multitude of benefits: (1) it outperforms standard explicit CoT methods by up to 6.22%, (2) it reduces training cost by up to 65% GPU hours, and (3) it speeds up inference by up to 71.3%. These results position PauseRec as a lightweight alternative to explicit rationale generation, enabling more effective and efficient LLM-based GR.

---


### 31. [Trust but Verify: Mitigating Medical Hallucinations via Post-Hoc Adversarial Auditing and Multi-Agent Feedback Loops](https://arxiv.org/abs/2606.14149)

**<font color=#1a73e8>作者：</font>** Muhammad Osama, Maheera Amjad, Zartasha Mustansar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in healthcare settings, yet their tendency to hallucinate poses risks when clinical decisions are involved. This study examine whether LLMs recommend recently banned or withdrawn pharmaceuticals when answering clinical questions and tests an agent-based method for reducing such errors. We developed a five-agent "Trust but Verify" system using a single LLM backbone. To measure regulatory knowledge obsolescence, we created an adversarial dataset of 103 clinical MCQs where historically correct answers now refer to banned substances. This scale ensures statistical significance across various therapeutic classes. We evaluated three open-access model families (GPT-OSS, Llama-3, Falcon-3) under vanilla and agentic conditions. Performance was measured via pointwise score, label accuracy, Hallucination Error Rate (HER), and Component Fidelity (CF) score. We also observed clinical safety regression in proprietary models. In default configurations, all models showed high hallucination rates, consistently selecting banned drugs that matched training data patterns. Our proposed agentic architecture reduced HER by approximately 53% across models. Pointwise scores shifted from -0.25 (unsafe recommendation) toward 0.0 (appropriate refusal). The safety audit intercepted dangerous outputs even when models' parametric knowledge favored the banned substance. The proposed multi-agent framework offers a model-agnostic method for enforcing regulatory compliance that prioritizes patient safety over fluent text generation. Our work demonstrates a practical approach for deploying autonomous AI systems in safety-critical healthcare settings. It shows how real-time regulatory data can be integrated into LLM pipelines to support clinical decision-making.

---


### 32. [Small LLMs: Pruning vs. Training from Scratch](https://arxiv.org/abs/2606.14150)

**<font color=#1a73e8>作者：</font>** Yufeng Xu, Taiming Lu, Kunjun Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pruning promises a shortcut to strong small language models. In this work, we examine this promise by pruning Llama-3.1-8B at pruning ratios of 0.5--0.8 with six methods spanning depth, width, and sparse granularities, under two controlled token-matched settings. (1) With the same training token budget, pruned initialization consistently outperforms random initialization. This shows that the parent model provides a strong starting point, although the advantage narrows as the training token budget grows and as the pruning ratio rises, nearly vanishing at the highest pruning ratio we study. (2) When training from scratch is instead given the full token budget consumed by the whole pipeline, pruning at finer granularities still retains an advantage, while coarser structured pruning can be matched or surpassed. This suggests that the parent model transfers knowledge that additional training tokens alone cannot fully recover, but only at fine granularity. Taken together, our results yield a clear recommendation: with a large pretrained model in hand and a limited training token budget, pruning is better than training from scratch; when the training budget is not limited, training from scratch can be competitive for coarser pruning, so a large pretrained parent is not always necessary.

---


### 33. [Graph-based Target Back-Propagation for Context Adaptation in Multi-LLM Agentic Systems](https://arxiv.org/abs/2606.14155)

**<font color=#1a73e8>作者：</font>** Tan Zhu, Tong Yao, Kananart Kuwaranancharoen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Context adaptation automates prompt engineering in LLM-based systems by iteratively revising tunable prompts from task feedback, without modifying model weights. Extending this paradigm to multi-LLM agentic systems is crucial: existing methods suffer from inaccurate credit assignment and lack convergence guarantees. We propose \textbf{G}raph-based \textbf{T}arget \textbf{B}ack-\textbf{P}ropagation (GTBP), a context adaptation framework for agentic workflows modeled as directed acyclic graphs. GTBP propagates local target outputs backward through the workflow graph and uses target--output discrepancies to guide a stage-wise prompt update mechanism. Theoretically, we show that GTBP's stage-wise prompt updates become stable over iterations, and that a sufficiently capable LLM optimizer can decrease the overall objective. Empirically, GTBP consistently outperforms strong baselines across three benchmarks while maintaining comparable computational cost.

---


### 34. [Learning High Coverage Discriminative Parsimonious Rulesets](https://arxiv.org/abs/2606.14156)

**<font color=#1a73e8>作者：</font>** Mariamma Antony, Raman Sankaran, Chiranjib Bhattacharyya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning systems based on IF-THEN rule representations readily offer interpretability, making them a crucial focus in contemporary AI research. A key objective for such rule sets is to achieve both high discriminative power and interpretability. While existing state-of-the-art algorithms implicitly prioritize predictive accuracy, they often fall short on one or more quality metrics that ensure interpretability, such as coverage and parsimony of rule sets. Motivated by this, this paper propose the development of CDPR, which aims to create highly accurate and interpretable rule sets for classification problems. To the best of our knowledge, this represents the first attempt to establish such an approach. In this study, we introduce two algorithms rooted in submodular maximization, which not only provide provable guarantees on coverage but also yield rule sets that are both discriminative and parsimonious. We empirically demonstrate that rule sets learned through our approaches achieve higher accuracy and interpretability and has more than a 2.5-fold improvement in average coverage rates when compared to the next best algorithm.

---


### 35. [MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction](https://arxiv.org/abs/2606.14168)

**<font color=#1a73e8>作者：</font>** Ruijie Xu, Xinnan Zhu, Jiayu Ying 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven 3D scene generation is a promising technique for digital content creation, embodied AI simulation, and interactive design, yet practical workflows often require refining, extending, or correcting existing scenes while preserving non-target content. Existing methods can produce realistic and structurally plausible scenes, but they generally lack editability with requirement-level state tracking, so part-level failures often lead to full-scene regeneration or manual intervention. To tackle this challenge, we formulate controllable 3D scene authoring as incremental requirement satisfaction, unifying construction and editing. In this paper, we present MUSE, a memory-grounded multi-agent framework in which an Architect compiles instructions into structured requirements, a Sculptor executes local scene operations, and an Inspector verifies each step while updating Working, Scene, and Skill Memory. To evaluate requirement-level controllability and preservation-aware editing, we introduce AuthorBench, offering 145 constrained construction cases and a 1,584-case preservation-aware editing pool paired with external structured checks. On full construction cases, MUSE improves All-Goal success from 37.9 to 80.7 and surface-constraint fulfillment from 35.0 to 92.6 over the strongest baseline. On a stratified 240-case editing test split, MUSE achieves 49.6 All-Goal success, 99.9 preservation rate, and only 0.6 unintended change rate. Beyond automated metrics, human evaluations on compared local-editing baselines support stronger alignment with user intent, and downstream navigation-proxy tests indicate stronger spatial stability. Combined with ablations validating our memory designs, these results establish MUSE as an effective framework for controllable 3D scene authoring.

---


### 36. [Context-aware Modality-Topology Co-Alignment for Multimodal Attributed Graphs](https://arxiv.org/abs/2606.14172)

**<font color=#1a73e8>作者：</font>** Sirui Zhang, Xu Wang, Zhengyu Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Attributed Graphs (MAGs) model real-world entities by coupling graph topology with heterogeneous attributes such as text and images. They support graph-centric tasks requiring structural and class-discriminative representations, and modality-centric tasks requiring fine-grained cross-modal correspondence. However, existing MAG methods often rely on fixed graph contexts or uniformly fused representations, causing task-agnostic propagation and over-compressed fusion that hinder diverse task requirements and modality-specific evidence preservation. To address this, we propose CoMAG, a unified MAG backbone that learns task-adaptive reliable contexts and modality-preserving alignment within them. CoMAG first conducts Reliable Context Learning by estimating edge reliability from multimodal semantic consistency, complementing raw topology with semantic neighbors, and selecting context components through a task-aware gate. It then performs Modality-preserving Hop-token Alignment by maintaining modality-specific multi-hop trajectories, matching modality-hop tokens across modalities, and decoupling shared and private representations. Thus, CoMAG produces graph and modality representations from one forward pass while retaining modality-specific cues. We further analyze stable propagation, over-smoothing mitigation, and modality-collapse control. Experiments on nine OpenMAG datasets compare CoMAG with feature-only, graph-only, multimodal, and unified MAG baselines across graph-level prediction, modality matching, and graph-conditioned generation. Results show that CoMAG achieves the best reported performance, demonstrating that task-adaptive reliable contexts and modality-preserving alignment improve structural prediction, cross-modal matching, and graph-conditioned generation while retaining sparse edge-linear complexity.

---


### 37. [CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward](https://arxiv.org/abs/2606.14179)

**<font color=#1a73e8>作者：</font>** Md Amirul Islam, Sumiran Thakur, Huancheng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present CacheRL, a system for training small agent foundation models that achieves 92 percent process accuracy on multi-step tool-calling tasks, approaching GPT-5's 94 percent while requiring 100 times less compute. Our approach addresses three challenges in practical agent training: transferring tool-calling knowledge from large models at scale, enabling reinforcement learning without costly live tool execution, and learning robustly from noisy cached environments. CacheRL introduces three key innovations. First, a hybrid thinking trajectory pipeline augments agent trajectories with LLM-generated reasoning traces, producing training examples that teach models not only what tools to call but also why. Second, the CacheAgentLoop eliminates live execution costs through a three-tier fuzzy cache while preserving trajectory fidelity using token-level masking. Third, a cache-tier-aware reward dynamically adjusts answer-quality weights to avoid penalizing models for cache-induced limitations. Through iterative supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO), CacheRL improves Qwen3-4B-Thinking's validation reward from 0.43 to 0.78. On public agentic tool-calling benchmarks, our model achieves competitive performance against frontier models such as GPT-5. Ablation studies show that removing knowledge transfer reduces performance by 41 percent, while cache-aware rewards contribute a 17 percent improvement. Interestingly, reinforcement learning improves training stability but yields limited gains beyond strong supervised fine-tuning, suggesting that data quality and reward design play a more important role than complex optimization methods in building practical small agent models.

---


### 38. [OdysSim: Building Foundation Models for Human Behavior Simulation](https://arxiv.org/abs/2606.14199)

**<font color=#1a73e8>作者：</font>** Xuhui Zhou, Weiwei Sun, Weihua Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as human simulators for interactive evaluation and social simulation. Yet helpfulness-driven post-training pulls them toward a homogeneous, overly agreeable assistant register, creating a behavioral Sim2Real gap. We present OdysSim, the largest open systematic investigation of behavioral foundation models, i.e., models trained to simulate human behavior at scale. We propose SOUL, a taxonomy of five capability axes (CONV, SS, COG, ROLE, EVAL) that unifies 62 datasets and 23 benchmark tasks under one framework. Specifically, we curate the OdysSim corpus (21.4M interactions, 10B tokens, retrofitted with back-generated social contexts), construct the SOUL-Index benchmark, and develop an end-to-end training recipe combining midtraining, task-specific RL, and expert distillation. The resulting open 8B OSim model ranks first or tied-first on 8 of 23 tasks, outperforming any individual frontier model by this count, with the strongest gains on conversational and social tasks. Its outputs are also more human-like in length, formatting, and word choice, and it transfers zero-shot to out-of-distribution user simulation on $\tau$-bench, nearly matching real users on reaction alignment (93.2 vs. 93.5). We further show that LLM-as-judge RL induces reward-hacking patterns, and that our detectors can mitigate them during post-training. Together, our findings suggest that behavioral foundation models require rethinking the LLM training paradigm. We release all artifacts to support future research.

---


### 39. [Detecting undisclosed LLM-generated content in parliamentary texts](https://arxiv.org/abs/2606.14209)

**<font color=#1a73e8>作者：</font>** Minerva Suvanto, Andrea McGlinchey, Peter J. Barclay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we evaluate the extent of undisclosed LLM-generated content in texts from the parliaments of the United Kingdom and Sweden. In many areas, such as in journalism or in academic writing, there are often requirements to clearly disclose whether AI tools, such as LLMs, have been used. In the case of parliamentary texts, the guidelines on disclosure of AI use are more vague. However, in order to maintain transparency and retain public trust, it is generally recommended that parliamentarians should state whether or not they have used AI when writing texts, such as parliamentary motions. Here, we train an interpretable (glass-box) text classifier using pre-LLM parliamentary texts and LLM-generated versions of such texts. We then apply the classifier to a test set containing recent parliamentary texts, finding a steady increase in undisclosed LLM use, in both parliaments, from 2022 onwards.

---


### 40. [Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL](https://arxiv.org/abs/2606.14211)

**<font color=#1a73e8>作者：</font>** Yinglun Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed as agents that interact with external environments and observe feedback such as execution results, error messages, and tool outputs. A well-functioning agent should be able to leverage this feedback to accurately assess its own performance. Yet we find a persistent reflection gap: LLM agents tend to mis-assess their own outputs after observing concrete environment feedback -- even for questions they correctly answered -- and standard RL barely helps due to a credit-assignment mismatch. To close this gap, we propose RefGRPO, a simple yet effective fix that augments standard RL algorithms with two key ingredients: a free calibration bonus computed by contrasting the agent's own reflection with the actual outcome (requiring no additional reward model, LLM judge, or external annotation), and a dynamic schedule on its coefficient. Compared to standard RL baselines, our method simultaneously improves reflection calibration (e.g., reduces underconfidence rate $44.4\% \to 7.7\%$) and task accuracy (e.g., $75.1\% \to 76.5\%$) on text-to-SQL across five benchmarks. The resulting calibrated reflection turns the agent into its own verifier grounded in environment feedback, which further enables (i) better self-improvement that uses reflections as pseudo-rewards without outcome supervision, and (ii) more effective test-time selective prediction by committing only to rollouts flagged as correct.

---


### 41. [LapidaryEngine: Fully Conversational Crystal Generation](https://arxiv.org/abs/2606.14215)

**<font color=#1a73e8>作者：</font>** Yusei Ito, Yuta Suzuki, Tomoya Murata 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emergence of Large Language Models (LLMs) has inspired the vision of generating bespoke crystal materials directly from natural-language instructions, enabling users to design materials through intuitive, conversational interaction. Existing text-to-crystal generative models represent important early steps toward this goal, but they suffer from two critical limitations: (i) restricted input formats that require highly structured descriptions (e.g., chemical formulas), and (ii) one-directional generation, where models can map text to crystal but cannot perform the inverse. These limitations prevent fully conversational workflows and hinder alignment with users' inherently ambiguous and evolving desiderata. We address these challenges with LapidaryEngine, the first model to support fully conversational crystal generation. LapidaryEngine accepts free-form natural-language requests and performs iterative refinement and editing in a dialogue-like manner. The key innovation is a pivot representation, a third, intermediate form that enables bidirectional translation between text and crystal structures despite the absence of direct paired datasets. Leveraging this pivot allows robust interpretation of user feedback and precise structural control. We demonstrate LapidaryEngine across diverse tasks, including insulator discovery, stability optimization, compositional modification, and structural editing, showcasing its ability to align generated materials with user intent in an interactive manner.

---


### 42. [Learning the Context of Errors: Black-Box Online Adaptation of Time Series Foundation Models](https://arxiv.org/abs/2606.14222)

**<font color=#1a73e8>作者：</font>** Xilin Dai, Yiding Liu, Hongjie Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of Time Series Foundation Models (TSFMs) has advanced zero-shot forecasting across diverse domains. Inspired by the current form of Large Language Models, future TSFMs may be offered as commercialized, closed-source API services. However, many existing online adaptation methods still rely on white-box access for parameter fine-tuning or gradient backpropagation. This paradigm mismatch raises a question: In black-box online adaptation for TSFMs, what should we learn? We answer this with an insight: the predictive errors of the base model are conditioned on both the input and output of the base model (i.e., the context of errors). To validate this insight, we propose ORCA (Online Residual Contextual Adaptation). We conduct extensive experiments across 5 state-of-the-art TSFMs and 8 datasets to demonstrate the effectiveness of our approach. Furthermore, through ablation studies, we quantitatively analyze the impact of different adapter learning hypotheses on the final adaptation performance in black-box online adaptation. Code available at this https URL.

---


### 43. [AFFORDANCE20Q: Evaluating Affordance Reasoning from Physical Properties](https://arxiv.org/abs/2606.14240)

**<font color=#1a73e8>作者：</font>** Yifan Jiang, Meige Yang, Zitong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Affordance reasoning, the inference of an object's action possibilities from its physical properties (e.g., shape and material), is fundamental to human physical understanding and increasingly critical for Large Language Models (LLMs). However, existing affordance benchmarks largely expose explicit object identities in the evaluation setup, allowing models to rely on memorized object-affordance mappings rather than reasoning over physical properties. To address this gap, we introduce Affordance20Q, a novel affordance reasoning benchmark formulated as a 20-Questions game without exposing the object's identity. In each game, the model identifies a hidden object's affordance from a candidate set by asking yes/no questions about its physical properties. Affordance20Q comprises 1,009 games over 454 objects and 59 affordances, all manually filtered, refined, and annotated. We conduct comprehensive experiments with 15 state-of-the-art LLMs and find a substantial gap (~20 points) compared to human performance. A KL-based information-gain (IG) analysis further shows that models fail to ask discriminating questions as the game progresses. To close the gap, we develop KB-Anchored Rule Induction (KARI), a pipeline based on LLMs that generates affordance rules grounded in evidence from knowledge bases (KBs). KARI improves open-source LLMs by up to 15.2 points, while the limited coverage of KBs hinders further gains. We release all our code and data at this https URL

---


### 44. [Decoupled Mixture-of-Experts for Parametric Knowledge Injection](https://arxiv.org/abs/2606.14243)

**<font color=#1a73e8>作者：</font>** Baoqing Yue, Weihang Su, Qingyao Ai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge injection aims to equip large language models (LLMs) with external, domain-specific, or time-sensitive knowledge. Existing approaches typically face a trade-off between flexibility and integration: retrieval-augmented generation keeps knowledge outside the model but only provides prompt-level augmentation, whereas post-training based methods encode new knowledge into shared parameters but may introduce catastrophic forgetting, knowledge conflict, and costly updates. In this paper, we propose Decoupled Mixture-of-Experts (DMoE), a modular architecture for parametric knowledge injection that decouples both experts and the router from the base model. DMoE converts external knowledge corpora into independently updatable expert modules and uses a lightweight uncertainty-aware router to activate relevant experts only when the base model lacks sufficient knowledge during generation. To support efficient auto-regressive inference, DMoE attaches experts only to the final-layer feed-forward network, preserving KV-cache reuse while enabling parameter-level knowledge augmentation. Experiments on knowledge-intensive benchmarks show that DMoE consistently improves answer quality over retrieval and adapter-based baselines.

---


### 45. [One Layer's Trash is Another Layer's Treasure: Adaptive Layer-wise Visual Token Selection in LVLMs](https://arxiv.org/abs/2606.14277)

**<font color=#1a73e8>作者：</font>** Yongru Chen, Kai Zhang, Zeliang Zong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable success across diverse multimodal tasks, yet their practical deployment remains constrained by the computational burden arising from lengthy visual tokens. While visual token pruning has emerged as a promising solution, existing methods suffer from a fundamental limitation: once tokens are pruned at a specific layer, they become inaccessible to all subsequent layers, leading to premature information loss that can compromise model performance. Through empirical studies, we observe that different layers exhibit distinct visual region focus, indicating a varying optimal token subset across layers. Motivated by this insight, we propose Adaptive Layer-wise Visual Token Selection (ALVTS), a novel framework that breaks away from the conventional static token pruning paradigm. ALVTS incorporates a lightweight token selector to identify and route important tokens for further processing, while allowing less important tokens to skip the layer, thus minimizing computational redundancy. These two streams of tokens are seamlessly reintegrated before being fed into subsequent layers, facilitating adaptive compression across the entire model. Grounded in our importance consistency constrained low-rank approximation, the proposed token selection module closely emulates the full attention mechanism, effectively capturing its essential patterns without requiring model retraining. Extensive experiments on LLaVA-1.5, LLaVA-NeXT, and Qwen2.5-VL validate the effectiveness of our method. With an 89% token compression ratio, ALVTS retains 96.7% of the original model's accuracy, achieving a superior efficiency-accuracy trade-off for LVLM inference.

---


### 46. [Does the Judge Prefer English? Evaluating Language-Switching Invariance in LLM-as-a-Judge](https://arxiv.org/abs/2606.14278)

**<font color=#1a73e8>作者：</font>** Shaojie Yin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are now widely used as automatic judges for open-ended instruction-following evaluation. This practice is convenient, scalable, and often more semantically aware than reference-based metrics, but it also introduces a new reliability question: does a judge evaluate the quality of an answer, or does it also react to the language in which the comparison is presented? We propose Judge-LS, a lightweight meta-evaluation protocol that transforms LLMBar response-pair items into English, Chinese, and Chinese-English language-switched variants. A reliable judge should preserve its preference under label-preserving language transformations and should not prefer a language when two answers are translation-equivalent. We evaluate four API-accessible judges on the full 419-item LLMBar benchmark, producing 13,408 successful pairwise judgments. Across models, Chinese and language-switched presentations induce 10.7--14.4% preference flips relative to English, and all judges achieve their highest accuracy in English. However, translation-equivalent tie probes do not reveal a systematic English preference: most probes are judged as ties, and non-tie decisions more often favor Chinese. We add confidence intervals, paired significance tests, and an automatic transformation audit with a sensitivity analysis that excludes mechanically flagged high-risk variants. The experiment requires no model training, uses only API calls, and is feasible on modest local hardware.

---


### 47. [Retrospective Progress-Aware Self-Refinement for LLM Agent Training](https://arxiv.org/abs/2606.14302)

**<font color=#1a73e8>作者：</font>** Xinbei Ma, Congmin Zheng, Jiyang Qiu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents trained with reinforcement learning optimize step-wise action prediction but lack metacognitive awareness of task progress, inducing a gap that hinders long-horizon scaling. A pilot study reveals that online progress prompting hurts performance while retrospective demonstrations help, yet this capability cannot emerge from outcome-reward training alone. We present RePro, Retrospective Progress-Aware Training, a framework that trains agents to self-generate progress signals via a forward-then-reflect rollout paradigm: the agent executes actions online, then retrospectively reassesses its step-wise progress given the completed trajectory and known outcome. RePro initializes with a Retrospection Warmup that teaches reflection format from minimal external demonstrations, then further trains through RePro-PO with a composite reward that produces self-generated signals without continuous external supervision. Experiments on WebShop, ALFWorld, and Sokoban show that RePro enhances the Qwen family's performance, with up to $12\%$ absolute success rate gains.

---


### 48. [Communication Policy Evolution for Proactive LLM Agents](https://arxiv.org/abs/2606.14314)

**<font color=#1a73e8>作者：</font>** Xinbei Ma, Jiyang Qiu, Yao Yao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents have rapidly evolved into autonomous systems, yet a persistent information gap remains between users and agents: communication is costly, while users' identical preferences further limit information exchange. To investigate how agents should communicate across modalities, this paper formalizes Communication Policy, establishes textual and UI-based policies, and then evaluates communication policies across diverse environments, personas, and model combinations. Building information asymmetry for proactive agents, we set up two complementary settings, User-Agent and Planner-Executor. Experimental results reveal complementary strengths between interaction channels: text-based interaction often facilitates task performance, while structured UI improves agents' response quality and persona compliance. Motivated by that, a hybrid method combines these advantages. We further propose Communication Policy Evolution (CPE), a self-evolution framework for refining communication policies through rollout and prompt-level evolving. Without model modification, CPE achieves the best task success across multiple settings using prompt refinement alone. Our findings identify communication behavior as a critical yet underexplored design dimension for LLM agents.

---


### 49. [When Language Representations Interact: Separability and Cross-Lingual Effects in LLMs](https://arxiv.org/abs/2606.14347)

**<font color=#1a73e8>作者：</font>** Boris Marinov, Angira Sharma, Christian Schroeder de Witt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit strong multilingual capabilities, however, their internal representations are difficult to interpret. Understanding these interactions is important for ensuring reliable behavior in multilingual systems. Recent work has shown that causal-geometric structure can explain how certain concepts are encoded as approximately linear and separable directions, but whether this framework extends to multilingual models, where language identity is correlated and hierarchical, is underexplored. We apply causal-geometric analysis to multilingual LLMs, studying 28 bilingual contrasts across three models, allowing us to analyze when languages behave as approximately independent factors and when structured dependencies persist. We find evidence that language concepts admit stable linear representations that are largely separable under a covariance-adjusted (causal) inner product, with structured deviations reflecting linguistic similarity. Moreover, languages within the same family (such as Germanic or Romance) exhibit a simplex-like geometric structure, suggesting hierarchical organization. These results extend causal-geometric interpretability to multilingual settings and provide insight into how separability and similarity may exist in multilingual LLM representations, motivating interpretability analyses that diagnose when and how structured dependencies between concepts can be anticipated. This has implications for trustworthy deployment, as residual structure between languages may lead to unintended cross-lingual effects when models are monitored or intervened upon.

---


### 50. [Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback](https://arxiv.org/abs/2606.14368)

**<font color=#1a73e8>作者：</font>** Woohyeon Byeon, Jiwon Jeon, Jeonghye Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study multi-domain LLM training in which two models, each stronger in a different domain, co-evolve by tutoring each other through on-policy feedback. Unlike one-way distillation or single-model fine-tuning, our goal is mutual Pareto improvement: each model improves across domains without losing its original strength. To this end, we propose On-Policy Co-Distillation (OPCoD), where each student's self-distillation is conditioned on its own correct rollout and feedback from its peer. To make feedback exchange effective, OPCoD uses cognizance-based gating to decide when to give feedback and feedback anchoring to ground feedback in the problem. On Science Q\&A tasks, OPCoD consistently outperforms baselines and achieves Pareto improvement across all evaluated domain pairs and students.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-66](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
