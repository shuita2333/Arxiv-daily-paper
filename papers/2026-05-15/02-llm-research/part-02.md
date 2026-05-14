# 🧠 大模型相关研究 | 2026年05月15日

> 本类共 **159** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-159](./part-04.md)

---

### 51. [Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue](https://arxiv.org/abs/2605.12920)

**<font color=#1a73e8>作者：</font>** Vardhan Dongre, Dilek Hakkani-Tür  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Effective collaboration between embodied agents requires more than acting in a shared environment; it demands communication grounded in each agent's evolving understanding of the world. When agents can only partially observe their surroundings, coordination without communication is provably hard, but communication can, in principle, bridge this gap by allowing agents to share observations and align their world models. In this work, we examine whether LLM-based embodied agents actually realize the ability to communicate. We extend PARTNR, a benchmark for collaborative household robotics, with a natural-language dialogue channel that enables two agents with partial observability to communicate during task execution. To evaluate whether dialogue leads to genuine world-model alignment rather than superficial coordination, we propose a framework for measuring world-model alignment defined over per-agent world graphs: observation convergence (do private world models align over time?), information novelty (do messages convey what the partner lacks?), and belief-sensitive messaging (do agents model what their partner knows?). Our experiments across three LLMs reveal that dialogue reduces action conflicts 40 to 83 percentage points but degrades task success relative to silent coordination. Using our metrics, we characterize the gap between superficial coordination and genuine world-model alignment, and identify where current models fall on this spectrum.

---


### 52. [When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction](https://arxiv.org/abs/2605.12922)

**<font color=#1a73e8>作者：</font>** Vardhan Dongre, Joseph Hsieh, Viet Dac Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can follow complex instructions in a single turn, yet over long multi-turn interactions they often lose the thread of instructions, persona, and rules. This degradation has been measured behaviorally but not mechanistically explained. We propose a channel-transition account: goal-defining tokens become less accessible through attention, while goal-related information may persist in residual representations. We introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens, and combine it with sliding-window ablations and residual-stream probes. When attention to instructions closes, what survives reveals architecture. Across architectures, the transition yields qualitatively distinct failure modes: some models preserve goal-conditioned behavior at vanishing attention, others fail despite decodable residual goal information, and the layer at which this encoding emerges varies from 2 to 27. A within-model causal ablation that force-closes the attention channel in Mistral collapses recall from near-perfect to 11% on a 20-fact retention task and raises persona-constraint violations above an adversarial-pressure baseline without user pressure, with both effects emerging at the predictable crossover turn. Linear probes recover per-episode recall outcomes from residual representations with AUC up to 0.99 across all four primary architectures, while input embeddings remain at chance. Across architectures and model scales, the gap between attention loss and residual decodability predicts whether goal-conditioned behavior survives channel closure. We contribute GAR as a diagnostic, the channel-transition framework as a controlled mechanistic account, and a parametric prediction of failure timing under windowed attention closure.

---


### 53. [IV-ICL: Bounding Causal Effects with Instrumental Variables via In-Context Learning](https://arxiv.org/abs/2605.12924)

**<font color=#1a73e8>作者：</font>** Vahid Balazadeh, Hamidreza Kamkari, Medha Barath 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The instrumental-variables (IV) setting is standard for partial identification of causal effects when unobserved confounding makes point identification impossible. Existing approaches face methodological bottlenecks: closed-form bound estimands are required -- e.g., Balke-Pearl equations in binary IV -- and even when available, designing accurate estimators requires manual effort tailored to each estimand. While direct Bayesian inference of the causal effects, instead of the bounds, circumvents these challenges, it is often computationally intensive and suffers from high prior sensitivity or under-dispersed posteriors. As a remedy, we introduce IV-ICL, an amortized Bayesian in-context learning method that learns the marginal posterior distribution of the causal effects directly and derives bounds as its quantiles. Unlike standard variational inference that optimizes exclusive KL divergence, amortized Bayesian inference minimizes the expected inclusive KL, a mass-covering objective. We empirically observe that optimizing inclusive KL can recover the entire identified set across diverse data-generating processes, while exclusive-KL (e.g. with variational inference) of the same Bayesian formulation collapses onto a single mode and fails to cover the identified set. We evaluate IV-ICL on synthetic and semi-synthetic IV benchmarks and show it produces intervals that are more reliably valid and more informative compared to efficient semi-parametric, Bayesian, and plug-in baselines, at 20-500x lower inference time. Beyond methodology, we propose a procedure to convert randomized controlled trials into IV benchmarks with provably preserved ground-truth causal effects that enables a more realistic evaluation of partial-identification methods.

---


### 54. [The Expressivity Boundary of Probabilistic Circuits: A Comparison with Large Language Models](https://arxiv.org/abs/2605.12940)

**<font color=#1a73e8>作者：</font>** Zhiyu Zhao, Xuejie Liu, Muhan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic Circuits (PCs) are deep generative models that support exact and efficient probabilistic inference. Yet in autoregressive language modeling, PCs still lag behind Transformer-based large language models (LLMs), suggesting an important expressivity gap. In this work, we compare PCs and LLMs under a unified autoregressive formulation. First, an output bottleneck: PCs parameterize predictions as convex combinations in probability space, which struggles to represent the sharp distributions typical of language; adopting a logit-space parameterization substantially narrows this gap. Second, a context-encoding bottleneck: we prove that structured-decomposable PCs can match Transformer separation rank on vtree-aligned partitions, but show, both theoretically and empirically, that this capacity is limited to partitions aligned with the fixed routing structure, leading to severe degradation when the data exhibits heterogeneous dependency topologies. We further prove that decomposable PCs are strictly more expressive than structured-decomposable ones, though effectively optimizing them remains an open challenge.

---


### 55. [From Instance Selection to Fixed-Pool Data Recipe Search for Supervised Fine-Tuning](https://arxiv.org/abs/2605.12944)

**<font color=#1a73e8>作者：</font>** Haodong Wu, Jiahao Zhang, Lijie Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) data selection is commonly formulated as instance ranking: score each example and retain a top-$k$ subset. However, effective SFT training subsets are often produced through ordered curation recipes, where filtering, mixing, and deduplication operators jointly shape the final data distribution. We formulate this problem as fixed-pool data recipe search: given a raw instruction pool and a library of grounded operators, the goal is to discover an executable recipe that constructs a high-quality selected subset under a limited budget of full SFT evaluations, without generating, rewriting, or augmenting training samples. We introduce AutoSelection, a two-layer solver that decouples fixed-pool materialization based on cached task-, data-, and model-side signals from expensive full evaluation, using warmup probes, realized subset states, local recipe edits, Gaussian-process-assisted ranking, and stagnation-triggered reseeding. Experiments on a 90K instruction pool show that AutoSelection achieves the strongest in-distribution reasoning average across three base models, outperforming full-data training, random recipe search, random top-$k$, and single-operator selectors. Additional Out-of-distribution graph-reasoning results, search-stability analyses, structural ablations, and 1.5B-to-7B transfer checks further show that recipe structure matters beyond individual selection operators. Code is available at this https URL.

---


### 56. [Seg-Agent: Test-Time Multimodal Reasoning for Training-Free Language-Guided Segmentation](https://arxiv.org/abs/2605.12953)

**<font color=#1a73e8>作者：</font>** Chao Hao, Jun Xu, Ji Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided segmentation transcends the scope limitations of traditional semantic segmentation, enabling models to segment arbitrary target regions based on natural language instructions. Existing approaches typically adopt a two-stage framework: employing Multimodal Large Language Models (MLLMs) to interpret instructions and generate visual prompts, followed by foundational segmentation models (e.g., SAM) to produce masks. However, due to the limited spatial grounding capabilities of off-the-shelf MLLMs, these methods often rely on extensive training on large-scale datasets to achieve satisfactory accuracy. While recent advances have introduced reasoning mechanisms to improve performance, they predominantly operate within the textual domain, performing chain-of-thought reasoning solely based on abstract text representations without direct visual feedback. In this paper, we propose Seg-Agent, a completely training-free framework that pioneers Explicit Multimodal Chain-of-Reasoning. Unlike prior text-only reasoning, our approach constructs an interactive visual reasoning loop comprising three stages: generation, selection, and refinement. Specifically, we leverage Set-of-Mark (SoM) visual prompting to render candidate regions directly onto the image, allowing the MLLM to ``see'' and iteratively reason about spatial relationships in the visual domain rather than just the textual one. This explicit multimodal interaction enables Seg-Agent to achieve performance comparable to state-of-the-art training-based methods without any parameter updates. Furthermore, to comprehensively evaluate generalization across diverse scenarios, we introduce Various-LangSeg, a novel benchmark covering explicit semantic, generic object, and reasoning-guided segmentation tasks. Extensive experiments demonstrate the effectiveness and robustness of our method.

---


### 57. [Discovery-Oriented Faceting: From Coverage to Blind-Spot Discovery](https://arxiv.org/abs/2605.12956)

**<font color=#1a73e8>作者：</font>** Youdi Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When people explore large document collections to build understanding, they face a challenge: existing AI tools help them see what is central but tend to hide what is unusual. Summarization and topic modeling optimize for coverage, representing main themes while pushing minority viewpoints and edge cases out of view. This matters because discovery often depends on noticing what does not fit, such as unexpected findings, minority positions, or gaps in the literature. When tools hide this content, users may miss insights that could change their understanding. In this paper, we explore an alternative objective: blind-spot discovery, where the goal is to surface content that coverage methods suppress so that people can judge its significance for themselves. We propose three design goals and illustrate them through DOF (Discovery-Oriented Faceting), a system that organizes documents into categories with explicit boundaries, ranks categories by distinctiveness rather than size, and supports iterative refinement. Comparing DOF against coverage-based ranking across four domains, we find that the two approaches surface fundamentally different content, with DOF promoting specialized categories that coverage methods bury. We discuss how shifting from coverage to discovery may offer a complementary mode of support for people exploring large text collections.

---


### 58. [DiM\textsuperscript{3}: Bridging Multilingual and Multimodal Models via Direction- and Magnitude-Aware Merging](https://arxiv.org/abs/2605.12960)

**<font color=#1a73e8>作者：</font>** Zijing Wang, Mingyang Wang, Ercong Nie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Towards more general and human-like intelligence, large language models should seamlessly integrate both multilingual and multimodal capabilities; however, extending an existing multimodal model to many languages typically requires expensive multilingual multimodal data construction and repeated end-to-end retraining. We study a training-free alternative: injecting multilingual capability into an existing multimodal model by composing residual updates in the shared language model backbone. The key challenge is that multilingual and multimodal updates are heterogeneous, reflecting different functional roles in the shared model. To address this, we propose Direction- and Magnitude-aware Multilingual Multimodal merging (DiM3), which selectively composes the two updates at each parameter dimension while preserving the original vision encoder and multimodal projector. Experiments on multilingual benchmarks in both text-only and vision-language settings, covering 57 languages across LLaVA- and Qwen-based backbones, show that DiM3 consistently outperforms existing merging baselines, substantially improves multilingual performance over the original multimodal model, and remains competitive with dedicated multilingual multimodal fine-tuning while largely retaining general multimodal ability. We further show that DiM3 can be directly applied to already trained multilingual multimodal models and still yield additional gains. Further interpretability analysis shows that DiM3 primarily reshapes intermediate-layer semantic representations, strengthening cross-lingual alignment under both text-only and multimodal inputs while preserving higher-layer task-sensitive structure. Our repository is on this https URL.

---


### 59. [Reducing Bias and Variance: Generative Semantic Guidance and Bi-Layer Ensemble for Image Clustering](https://arxiv.org/abs/2605.12961)

**<font color=#1a73e8>作者：</font>** Feijiang Li, Zhenxiong Li, Jieting Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image clustering aims to partition unlabeled image datasets into distinct groups. A core aspect of this task is constructing and leveraging prior knowledge to guide the clustering process. Recent approaches introduce semantic descriptions as prior information, most of which typically relying on matching-based techniques with predefined vocabularies. However, the limited matching space restricts their adaptability to downstream clustering tasks. Moreover, these methods primarily focus on reducing bias to improve performance, frequently overlooking the importance of variance reduction. To address these limitations, we propose GSEC (Image Clustering based on Generative Semantic Guidance and Bi-Layer Ensemble), a framework designed to reduce bias through generative semantic guidance and mitigate variance via ensemble learning. Our method employs Multimodal Large Language Models to generate semantic descriptions and derive image embeddings via weighted averaging. Additionally, a bi-layer ensemble strategy integrates cross-modal information through BatchEnsemble in the inner layer and aligns outputs via an alignment mechanism in the outer layer. Comparative experiments demonstrate that GSEC outperforms 18 state-of-the-art methods across six benchmark datasets, while further analysis confirms its effectiveness in simultaneously reducing both bias and variance. The code is available at this https URL.

---


### 60. [Position: Agentic AI System Is a Foreseeable Pathway to AGI](https://arxiv.org/abs/2605.12966)

**<font color=#1a73e8>作者：</font>** Junwei Liao, Shuai Li, Muning Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Is monolithic scaling the only path to AGI? This paper challenges the dogma that purely scaling a single model is sufficient to achieve Artificial General Intelligence. Instead, we identify Agentic AI as a necessary paradigm for mastering the complex, heterogeneous distribution of real-world tasks. Through rigorous theoretical derivations, we contrast the optimization constraints of monolithic learners against the efficiency of Agentic systems, progressing from simple routing mechanisms to general Directed Acyclic Graph (DAG) topologies. We demonstrate that Agentic AI achieves exponentially superior generalization and sample efficiency. Finally, we discuss the connection to Mixture-of-Experts, reinterpret the instability of current multi-agent frameworks, and call for greater research focus on Agentic AI.

---


### 61. [Controlling Logical Collapse in LLMs via Algebraic Ontology Projection over F2](https://arxiv.org/abs/2605.12968)

**<font color=#1a73e8>作者：</font>** Hisashi Miyashita, Mgnite Inc  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Do large language models internally encode ontological relations in a formally verifiable algebraic structure? We introduce Algebraic Ontology Projection (AOP), which projects LLM hidden states into the Galois Field F2 under Liskov Substitution Principle constraints, using only 42 relational pairs as algebraic keys. AOP achieves up to 93.33% zero-shot inclusion accuracy on unseen concept pairs (Gemma-2 Instruct with optimized prompt), with consistent 86.67% accuracy observed across multiple model families -- with no model tuning, but through prompt alone.
This algebraic structure is strongly layer-dependent. We introduce Semantic Crystallisation (SC), a metric that quantifies F2 constraint satisfaction relative to a random baseline and predicts zero-shot accuracy without held-out data. System prompts act as algebraic boundary conditions: only their combination with instruction tuning prevents Late-layer Collapse -- a systematic degradation of logical consistency in the final layers, observed in 7 of 10 conditions. These findings reframe forward computation as an iterative process of algebraic organisation, and open a path toward LLMs whose logical structure is not merely approximated, but formally accessible.

---


### 62. [Leveraging Speech to Identify Signatures of Insight and Transfer in Problem Solving](https://arxiv.org/abs/2605.12970)

**<font color=#1a73e8>作者：</font>** Linas Nasvytis, Judith E. Fan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many problems seem to require a flash of insight to solve. What form do these sudden insights take, and what impact do they have on how people approach similar problems in the future? In this work, we prompted participants (N = 189) to talk aloud as they attempted to solve a sequence of five "matchstick-arithmetic" problems. These problems either all relied on the same kind of non-obvious solution (Same group) or a different kind each time (Different group). We found that Same participants improved more rapidly than Different participants, and as they improved, they talked more and talked about different things when solving later problems. Specifically, they were more likely to spontaneously categorize the problem they were working on. Taken together, these findings suggest that a hallmark of transferable insights is their accessibility for verbal report, even if the underlying precursors of insight remain difficult to articulate.

---


### 63. [Retrieval is Cheap, Show Me the Code: Executable Multi-Hop Reasoning for Retrieval-Augmented Generation](https://arxiv.org/abs/2605.12975)

**<font color=#1a73e8>作者：</font>** Jiashuo Sun, Jimeng Shi, Yixuan Xie 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become a standard approach for knowledge-intensive question answering, but existing systems remain brittle on multi-hop questions, where solving the task requires chaining multiple retrieval and reasoning steps. Key challenges are that current methods represent reasoning through free-form natural language, where intermediate states are implicit, retrieval queries can drift from intended entities, and errors are detected by the same model that produces them making self-reflection an unreliable, ungrounded signal.
We observe that multi-hop question answering is a typical form of step-by-step computation, and that this structured process aligns closely with how code-specialized language models are trained to operate. Motivated by this, we introduce \pyrag, a framework that reformulates multi-hop RAG as program synthesis and execution. Instead of free-form reasoning trajectories, \pyrag represents the reasoning process as an executable Python program over retrieval and QA tools, exposing intermediate states as variables, producing deterministic feedback through execution, and yielding an inspectable trace of the entire reasoning process. This formulation further enables compiler-grounded self-repair and execution-driven adaptive retrieval without any additional training.
Experiments on five QA benchmarks (PopQA, HotpotQA, 2WikiMultihopQA, MuSiQue, and Bamboogle) show that \pyrag consistently outperforms strong baselines under both training-free and RL-trained settings, with especially large gains on compositional multi-hop datasets. Our code, data and models are publicly available at this https URL.

---


### 64. [Useful Memories Become Faulty When Continuously Updated by LLMs](https://arxiv.org/abs/2605.12978)

**<font color=#1a73e8>作者：</font>** Dylan Zhang, Yanshan Lin, Zhengkun Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning from past experience benefits from two complementary forms of memory: episodic traces -- raw trajectories of what happened -- and consolidated abstractions distilled across many episodes into reusable, schema-like lessons. Recent agentic-memory systems pursue the consolidated form: an LLM rewrites past trajectories into a textual memory bank that it continuously updates with new interactions, promising self-improving agents without parameter updates. Yet we find that such consolidated memories produced by today's LLMs are often faulty even when derived from useful experiences. As consolidation proceeds, memory utility first rises, then degrades, and can fall below the no-memory baseline. More surprisingly, even when consolidating from ground-truth solutions, GPT-5.4 fails on 54% of a set of ARC-AGI problems it had previously solved without memory. We trace the regression to the consolidation step rather than the underlying experience: the same trajectories yield qualitatively different memories under different update schedules, and an episodic-only control that simply retains those trajectories remains competitive with the consolidators we test. In a controlled ARC-AGI Stream environment that exposes Retain, Delete, and Consolidate actions, agents preserve raw episodes by default and double the accuracy of their forced-consolidation counterparts; disabling consolidation entirely (episodic management only) matches this auto regime. Practically, robust agent memory should treat raw episodes as first-class evidence and gate consolidation explicitly rather than firing it after every interaction. Looking forward, reliable agentic memory will require LLMs that can consolidate without overwriting the evidence they depend on.

---


### 65. [Leveraging Multimodal Self-Consistency Reasoning in Coding Motivational Interviewing for Alcohol Use Reduction](https://arxiv.org/abs/2605.12987)

**<font color=#1a73e8>作者：</font>** Guangzeng Han, James G. Murphy, Benjamin O. Ladd 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> BACKGROUND: Coding Motivational Interviewing (MI) sessions is essential for understanding client behaviors and predicting outcomes, but it requires substantial time and labor from trained MI professionals. Recent advances in audio-language models (ALMs) offer new opportunities to automate MI coding by capturing multimodal behavioral signals. OBJECTIVE: This study aims to develop an automatic MI coding approach based on ALMs that analyzes raw audio input and integrates predictions from multiple reasoning trajectories using self-consistency to improve coding robustness. METHODS: We experimented with five recorded sessions from de-identified MI audio tapes. We deployed ALMs with four complementary analytic prompts to support utterance-level reasoning: analytic prompting for verbal cues, prosody-aware prompting for acoustic cues, evidence-scoring prompting for quantitative hypothesis testing, and comparative prompting for contrastive reasoning. Three stochastic samples were drawn for each prompt, generating 12 independent reasoning trajectories per utterance. Final predictions were determined by majority voting across all trajectories. RESULTS: Performance was evaluated using accuracy, precision, recall, and macro-F1 scores. The proposed multimodal self-consistency approach achieved 52.56% accuracy, 54.03% precision, 47.45% recall, and a macro-F1 score of 46.40%, exceeding baseline methods. Systematic ablation experiments that removed individual modules consistently degraded performance on the primary metrics. CONCLUSIONS: Multimodal self-consistency outperforms single-pass baseline prompting approaches for MI coding. These findings suggest that incorporating both what clients say and how they say it can support more reliable automatic MI coding.

---


### 66. [Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI Education](https://arxiv.org/abs/2605.12988)

**<font color=#1a73e8>作者：</font>** Mragisha Jain, Tirth Bhatt, Griffin Pitts 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Students learning algorithms often need support as they interpret traces, debug reasoning errors, and apply procedures across unfamiliar problem instances. In this paper, we present KITE (Knowledge-Informed Tutoring Engine), a Retrieval-Augmented Generation (RAG)-based intelligent tutoring system designed to serve as a classroom teaching assistant for algorithmic reasoning and problem-solving tasks. KITE uses an intent-aware Socratic response strategy to tailor support to different student needs, responding with targeted hints, guiding questions, and progressive scaffolding intended to strengthen students' algorithmic problem-solving ability. To keep responses aligned with course content, KITE uses a multimodal RAG pipeline that retrieves relevant information from course materials. We evaluate KITE using three forms of assessment: RAGAs-based metrics for response grounding and quality, expert evaluation of pedagogical quality, and a simulated student pipeline in which a weaker language model interacts with KITE across two-turn dialogues and produces revised answers after receiving feedback. Results indicate that KITE produces contextually grounded and pedagogically appropriate responses. Further, using simulated students, KITE's feedback helped the student models produce more accurate follow-up responses on procedural and tracing questions, suggesting that its scaffolding can support algorithmic problem-solving. This work contributes a tutoring architecture and an evaluation approach for assessing retrieval-grounded explanations and scaffolded problem-solving feedback.

---


### 67. [Not Just RLHF: Why Alignment Alone Won't Fix Multi-Agent Sycophancy](https://arxiv.org/abs/2605.12991)

**<font color=#1a73e8>作者：</font>** Adarsh Kumarappan, Ananya Mujoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent pipelines flip from correct to incorrect answers under simulated peer disagreement at rates we term yield, a vulnerability widely attributed to RLHF-induced sycophancy. We test this attribution across four model families and find it largely wrong: pretrained base models exhibit the same substitution pattern as their Instruct variants, averaging higher yield than Instruct. Using activation patching, we localize the corruption to a narrow mid-layer window where attention carries the causal weight and MLP contribution is negligible; patching above this window restores 96% of the clean-to-pressured P(correct) gap. The attack surface decomposes into two independent factors (channel framing and consensus strength) whose interaction produces a 47.5 percentage-point yield gap at majority consensus, preserved across jury sizes $N \in \{4, 5, 6\}$. Two converging activation-space interventions show that pressure suppresses clean-reasoning features rather than activating a new sycophancy circuit. A single correctly-arguing dissenter reduces yield by 54-73 percentage points across all framings tested, whereas the strongest prompt-level defense fails on attack variants outside its design surface. Mitigations should target the mechanism, structured dissent at the pipeline level, rather than prompt-level defenses.

---


### 68. [F-GRPO: Factorized Group-Relative Policy Optimization for Unified Candidate Generation and Ranking](https://arxiv.org/abs/2605.12995)

**<font color=#1a73e8>作者：</font>** Rohan Surana, Gagan Mundada, Junda Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional retrieval pipelines optimize utility through stages of candidate retrieval and reranking, where ranking operates over a predefined candidate set. Large Language Models (LLMs) broaden this into a generative process: given a candidate pool, an LLM can generate a subset and order it within a single autoregressive pass. However, this flexibility introduces a new optimization challenge: the model must search a combinatorial output space while receiving utility feedback only after the full ranked list is generated. Because this feedback is defined over the completed sequence, it cannot distinguish whether a poor result arises from failing to generate a relevant subset or from failing to rank that subset correctly. This credit assignment gap makes end-to-end optimization unstable and sample-inefficient. Existing systems often address this by separating candidate generation from ranking. However, such decoupling remains misaligned with downstream utility because ranking is limited by the candidate set it receives. To bridge this gap, we propose a unified framework that performs both within a single autoregressive rollout and optimizes them end-to-end via factorized group-relative policy optimization (F-GRPO). Our framework factorizes the policy into candidate generation and ranking while sharing a single LLM backbone, and jointly trains them with an order-invariant coverage reward and a position-aware utility reward. To address the resulting phase-specific credit assignment problem, we use separate group-relative advantages for generation and ranking within a two-phase sequence-level objective. Across sequential recommendation and multi-hop question answering benchmarks, F-GRPO improves top-ranked performance over GRPO and decoupled baselines, outperforms supervised alternatives, and remains competitive with strong zero-shot rerankers, with no architectural changes at inference time.

---


### 69. [JEDI: Joint Embedding Diffusion World Model for Online Model-Based Reinforcement Learning](https://arxiv.org/abs/2605.13013)

**<font color=#1a73e8>作者：</font>** Jing Yu Lim, Rushi Shah, Zarif Ikram 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion world models have recently become competitive for online model-based reinforcement learning, but current approaches expose a tension: pixel diffusion is effective but computationally expensive while the latest latent diffusion approach improves efficiency yet performs subpar. The latter also relies on separately trained latents rather than the end-to-end world-model objectives that have driven much of modern MBRL progress. In particular, JEPA-style predictive representation learning has emerged as an especially promising direction for world modeling and MBRL. Concurrently, diffusion-style objectives have gained traction across multiple domains, with iterative refinement as a promising approach for multimodal and stochastic targets. Taken together, these trends motivate Joint Embedding DIffusion (JEDI), the first online end-to-end latent diffusion world model. JEDI learns its latent space directly from the diffusion denoising loss with a JEPA framework, using denoising to learn and predict future latents rather than relying on reconstruction and pretrained models. We provide a theoretical motivation showing that conventional JEPA objectives induce a predictive information bottleneck, and that conditional diffusion denoising admits a closely related predictive-compression decomposition. Empirically, JEDI is competitive on Atari100k and outperforms the baseline with seperately trained latents where directly comparable. Relative to the pixel diffusion baseline, JEDI uses 43% less VRAM, over 3$\times$ faster world-model sampling, and 2.5$\times$ faster training. JEDI also exhibits a markedly different task-level performance profile from the pixel baseline, suggesting that end-to-end predictive latents change more than compute alone.

---


### 70. [Understanding and Accelerating the Training of Masked Diffusion Language Models](https://arxiv.org/abs/2605.13026)

**<font color=#1a73e8>作者：</font>** Chunsan Hong, Sanghyun Lee, Chieh-Hsin Lai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) have emerged as a promising alternative to autoregressive models (ARMs) for language modeling. However, MDMs are known to learn substantially more slowly than ARMs, which may become problematic when scaling MDMs to larger models. Therefore, we ask the following question: how can we accelerate standard MDM training while maintaining its final performance? To this end, we first provide a detailed analysis of why MDM training is slow. We find that the main factor is the locality bias of language: the predictive information for a token is concentrated in nearby positions. We further investigate how this bias slows learning and suggest a simple yet effective remedy: bell-shaped time sampling as a training strategy. Notably, MDMs trained with our training recipe reach the same validation negative log-likelihood (NLL) up to $\sim4\times$ faster than standard training on One Billion Word Benchmark (LM1B). We also show faster improvements in generative perplexity, zero-shot perplexity, and downstream task performance on various benchmarks.

---


### 71. [ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence](https://arxiv.org/abs/2605.13034)

**<font color=#1a73e8>作者：</font>** Zhuofan Shi, Peilun Jia, Baoqin Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent deep research systems have improved the ability of large language models to produce long, grounded reports through iterative retrieval and reasoning. However, most text-centered systems rely mainly on textual evidence, while multimodal systems often retrieve images only weakly or generate charts themselves, leaving source figures underused as evidence. We present ViDR, a multimodal deep research framework that grounds long-form reports in source figures. ViDR treats source figures as retrievable, interpretable, routable, and verifiable evidence objects, while still generating analytical charts when needed. It builds an evidence-indexed outline linking claims to textual and visual evidence, refines noisy web images into source-figure evidence atoms through context-aware filtering, outline-aware reranking, and VLM-based visual analysis, and generates each section with section-specific evidence. ViDR further validates visual references to reduce hallucinated or misplaced figures. We also introduce MMR Bench+, a benchmark for evaluating visual evidence use in deep research reports, covering source-figure retrieval, placement, interpretation, verifiability, and analytical chart generation. Experiments show that ViDR improves overall report quality, source-figure integration, and verifiability over strong commercial and open-source baselines. These results suggest that source visual evidence is important for multimodal deep research, as it strengthens evidential grounding, visual support, and report verifiability.

---


### 72. [Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models](https://arxiv.org/abs/2605.13043)

**<font color=#1a73e8>作者：</font>** Yejin Lee, Yo-Sub Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) provide a promising alternative to autoregressive language models by generating text through iterative denoising and bidirectional refinement. However, this iterative generation paradigm also introduces unique safety vulnerabilities when harmful tokens generated at intermediate denoising steps propagate through subsequent refinement processes and eventually induce unsafe outputs. While there are a few attempts to remedy this issue, they either fail to generate safe outputs or generate safe yet low-quality outputs. This motivates us to propose an inference-time defense framework based on the step-wise intervention during the denoising process, which then improves the safety without compromising the output quality. The key component of our framework is a contrastive safety direction (SGD), a latent direction that captures the semantic boundary between harmful and safe generations. We leverage SGD to assess the alignment of generated tokens with harmful semantics at each denoising step. When harmful alignment is detected, our method remasks the corresponding tokens and resumes the denoising process with adaptive steering, where the steering strength is modulated according to the estimated degree of harmfulness. As a plug-and-play module, our method circumvents the need for additional fine-tuning and can be directly incorporated into off-the-shelf diffusion models. The experimental results show that our approaches reduce jailbreak success rates to 0.64% while preserving generation quality close to the original model performance. This confirms the effectiveness of step-wise intervention for safe diffusion language model generation. Our code is available at this https URL.

---


### 73. [Large Language Models Lack Temporal Awareness of Medical Knowledge](https://arxiv.org/abs/2605.13045)

**<font color=#1a73e8>作者：</font>** Zihan Guan, Qiao Jin, Guangzhi Xiong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The existing methods for evaluating the medical knowledge of Large Language Models (LLMs) are largely based on atemporal examination-style benchmarks, while in reality, medical knowledge is inherently dynamic and continuously evolves as new evidence emerges and treatments are approved. Consequently, evaluating medical knowledge without a temporal context may provide an incomplete assessment of whether LLMs can accurately reason about time-specific medical knowledge. Moreover, most medical data are historical, requiring the models not only to recall the correct knowledge, but also to know when that knowledge is correct. To bridge the gap, we built TempoMed-Bench, the first-of-its-kind benchmark for evaluating the temporal awareness of the LLMs in the medical domain through evolving guideline knowledge. Based on the TempoMed-Bench, our evaluation analysis first reveals that LLMs lack temporal awareness in medical knowledge through the key findings: (1) model performance on up-to-date medical knowledge exhibits a gradual linear decline over time rather than a sharp knowledge-cutoff behavior, suggesting that parametric medical knowledge is not strictly bounded by knowledge cutoffs; (2) LLMs consistently struggle more with recalling outdated historical medical knowledge than with up-to-date recommendations: accuracy of historical knowledge is only 25.37%-53.89% of up-to-date knowledge, indicating potential knowledge forgetting effects during training; and (3) LLMs often exhibit temporally inconsistent behaviors, where predictions fluctuate irregularly across neighboring years. We also show that the temporal awareness problem is a challenge that cannot be easily solved when integrated with agentic search tools (-3.15%-14.14%). This work highlights an important yet underexplored challenge and motivates future research on developing LLMs that can better encode time-specific medical knowledge.

---


### 74. [An Agentic LLM-Based Framework for Population-Scale Mental Health Screening](https://arxiv.org/abs/2605.13046)

**<font color=#1a73e8>作者：</font>** Giuliano Lorenzoni, Paulo Alencar, Donald Cowan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mental health disorders affect millions worldwide, and healthcare systems are increasingly overwhelmed by the volume of clinical data generated from electronic records, telemedicine platforms, and population-level screening programs. At the same time, the emergence of novel AI-based approaches in healthcare calls for intelligent frameworks capable of processing domain-specific unstructured clinical information while adapting to patient-specific needs. This paper proposes an agentic framework for building robust LLM-based pipelines, where each stage is encapsulated as a LangChain agent governed by explicit policies and proxy-guided evaluation. Stages are incrementally locked once validated, ensuring that later adaptations cannot overwrite configurations without demonstrated improvement. The proposed framework evolves from feature-level exploration, through proxy-based tuning and freeze/rollback mechanisms, to full orchestration by an Orchestrator Agent that coordinates preprocessing, retrieval, selection, diversity, threshold optimization, and decoding. A proof-of-concept in transcript-based depression detection demonstrates that the framework converges to stable configurations, such as cosine similarity, dynamic Top-k, and threshold 0.75, while controlling evaluation costs and avoiding regressions. These results highlight the potential of agentic AI to enable population-level mental health screening over large clinical datasets, addressing critical challenges in trustworthiness, reproducibility, and adaptability required in healthcare environments.

---


### 75. [The Cost of Perfect English: Pragmatic Flattening and the Erasure of Authorial Voice in L2 Writing Supported by GenAI](https://arxiv.org/abs/2605.13055)

**<font color=#1a73e8>作者：</font>** Ao Liu, Shanhua Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The integration of Generative AI (GenAI) into language learning offers second language (L2) writers powerful tools for text optimization. However, pursuing native-like fluency often sacrifices sociopragmatic diversity. Investigating "pragmatic flattening" - the systematic erasure of culturally preferred politeness and authorial stance - this study conducts a comparative analysis of argumentative essays by Chinese B2-level university students from the ICNALE corpus. The original texts were polished via the APIs of four leading Large Language Models at a zero-temperature setting for reproducibility. Findings reveal a nuanced "dimensional divergence" within the Semantic Preservation Paradox. While models corrected lexicogrammatical errors and retained propositional meaning, sociopragmatic interventions were bifurcated. In the interactive dimension, all models showed a drastic collapse of dialogic engagement markers, turning negotiated discourse into monologic assertions. Conversely, in the epistemic stance dimension, models showed architecture-based variability: some aggressively scrubbed epistemic markers, while others reinforced tentative hedging as decontextualized algorithmic caution. This confirms that while GenAI enhances accuracy, it systematically overwrites L2 writers' unique rhetorical identities into a homogenized Anglo-American paradigm. We argue that future instruction must move beyond error correction, advocating for Critical AI Literacy to empower multilingual writers to use GenAI for linguistic enhancement while safeguarding sociopragmatic diversity and rhetorical agency.

---


### 76. [Ergodic Trajectory Design by Learned Pushforward Maps: Provable Coverage via Conditional Flow Matching](https://arxiv.org/abs/2605.13063)

**<font color=#1a73e8>作者：</font>** Ehsan Aghazadeh, Masoud Malekzadeh, Ahmad Ghasemi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing continuous trajectories whose time-averaged occupancy provably matches a prescribed spatial density (the \emph{ergodic coverage} problem) is central to UAV-assisted data collection and sensing, robotic exploration, and mobile monitoring. For flying agents in particular, this challenge is acute: trajectories must balance coverage fidelity against tight energy budgets, no-fly zones, and acceleration limits. Existing methods either re-optimize each trajectory online (with cost growing in the horizon and re-running for every target, agent, and realization) or rely on bespoke analytical constructions that must be re-derived for each new constraint. We propose a \emph{epushforward} framework that decouples ergodicity from density matching: an analytic latent trajectory provides exact uniform ergodicity on a simple annular domain, and a single map, learned offline by optimal-transport conditional flow matching, transports this latent occupancy onto the prescribed target density. The composed trajectory is then asymptotically ergodic with respect to the learned pushforward distribution, with deviation from the target controlled by the flow-matching training loss. Once trained for a given target density and constraint set, the map serves an unbounded number of trajectories and a multi-agent fleet without per-agent retraining, and many differentiable operational constraints (no-fly zones, acceleration ceilings, or fairness penalties) enter as additive soft penalties in the training loss without re-deriving the design. We prove three results (an acceleration-energy bound, an $O(1/\sqrt{K})$ ergodic convergence rate in the number of trajectory cycles $K$, and an approximation-error bound) that combine into an end-to-end coverage bound estimable from CFM training diagnostics (certified given an architectural Lipschitz bound on $v_\theta$).

---


### 77. [TruncProof: A Guardrail for LLM-based JSON Generation under Token-Length Constraints](https://arxiv.org/abs/2605.13076)

**<font color=#1a73e8>作者：</font>** Yoshio Kato, Shuhei Tarashima  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The LLM-based generation of machine-readable outputs such as JSON has attracted significant attention for integration with external systems. However, existing approaches cannot strictly enforce the maximum number of tokens to be generated, leading to infinite generation or truncated outputs that cause a system malfunction. To address this limitation, we propose TruncProof, a novel grammar-constrained generation method that enables LLMs to produce grammatically valid JSONs while adhering to a predefined token limit. By leveraging the properties of LL(1) parsers, TruncProof efficiently approximates the minimum number of tokens required to complete a grammatically valid output at each decoding step. Experiments on the Text-to-JSON instruction tasks demonstrate that TruncProof successfully generates syntactically correct outputs even under strict token constraints. Furthermore, we show that TruncProof can be effectively combined with advanced decoding strategies, resulting in outputs that are not only grammatically valid but also semantically accurate.

---


### 78. [Learning to See What You Need: Gaze Attention for Multimodal Large Language Models](https://arxiv.org/abs/2605.13080)

**<font color=#1a73e8>作者：</font>** Junha Song, Byeongho Heo, Geonmo Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When humans describe a visual scene, they do not process the entire image uniformly; instead, they selectively fixate on regions relevant to their intended description. In contrast, current multimodal large language models (MLLMs) attend to all visual tokens at each generation step, leading to diluted focus and unnecessary computational overhead. In this work, we introduce Gaze Attention, a novel mechanism that enables MLLMs to selectively attend to task-relevant visual regions during generation. Specifically, we spatially group visual embeddings-stored as key-value caches-into compact gaze regions, each represented by a lightweight descriptor. At each decoding step, the model dynamically selects the most relevant regions and restricts attention to them, reducing redundant computation while enhancing focus. To mitigate the loss of global context caused by localized attention, we further propose learnable context tokens appended to each image or frame, allowing the model to maintain holistic visual awareness. Extensive experiments on image and video understanding benchmarks demonstrate that Gaze Attention matches or surpasses dense-attention baselines, while using up to 90% fewer visual KV entries in the attention computation.

---


### 79. [GRACE: Gradient-aligned Reasoning Data Curation for Efficient Post-training](https://arxiv.org/abs/2605.13130)

**<font color=#1a73e8>作者：</font>** Junjie Li, Ziao Wang, NingXuan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing reasoning data curation pipelines score whole samples, treating every intermediate step as equally valuable. In reality, steps within a trace contribute very unevenly, and selecting reasoning data well requires assessing them individually. We present GRACE, a gradient-aligned curation method that views each reasoning trace as a sequence of optimization events and scores every step by two complementary signals: its alignment with the answer-oriented gradient direction, and its consistency with the preceding reasoning trajectory. Step-level scores are aggregated into a sample-level value for subset selection, using only the model's internal optimization signals and no external reward models or step annotations. To make this scalable, GRACE introduces a representation-level gradient proxy that estimates step-level alignment from token-level upstream signals in a single forward pass. Post-training Qwen3-VL-2B-Instruct on MMathCoT-1M, GRACE reaches 108.8% of the full-data performance with 20% of the data and retains 100.2% with only 5%, with subsets that transfer effectively across model backbones.

---


### 80. [GateKD: Confidence-Gated Closed-Loop Distillation for Robust Reasoning](https://arxiv.org/abs/2605.13136)

**<font color=#1a73e8>作者：</font>** Kasidit Sermsri, Teerapong Panboonyuen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distilling multi-step reasoning abilities from large language models (LLMs) into compact student models remains challenging due to noisy rationales, hallucinated supervision, and static teacher-student interactions. Existing reasoning distillation methods, including mentor-based approaches, predominantly operate in an open-loop manner, implicitly assuming uniform teacher reliability and consequently propagating erroneous intermediate reasoning. We propose GateKD, a confidence-gated closed-loop distillation framework that enables robust reasoning transfer by treating the teacher as a dynamic gatekeeper rather than a static oracle. GateKD introduces three complementary mechanisms: (i) confidence-gated soft supervision that selectively distills reliable predictive signals, (ii) gated hidden-state evolution that aligns intermediate representations only when teacher confidence is high, and (iii) reliability-filtered attention distillation that preserves stable reasoning structures while suppressing noisy patterns. These components jointly form a closed feedback loop in which teacher confidence continuously modulates the distillation process, reducing hallucination transfer and stabilizing student reasoning. Extensive experiments across commonsense, logical, and symbolic reasoning benchmarks, using T5 and Flan-T5 backbones of varying sizes, demonstrate that GateKD consistently outperforms strong open-loop distillation baselines. Notably, GateKD yields substantial gains in logical and symbolic reasoning, remains robust under low-resource distillation settings, and shows clear performance degradation when any gating component is removed. Our results highlight that confidence-gated closed-loop supervision is critical for building reliable and scalable small reasoning models.

---


### 81. [Pareto-Guided Optimal Transport for Multi-Reward Alignment](https://arxiv.org/abs/2605.13155)

**<font color=#1a73e8>作者：</font>** Ying Ba, Tianyu Zhang, Mohan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generation models have achieved remarkable progress in preference optimization, yet achieving robust alignment across diverse reward models remains a significant challenge. Existing multi-reward fusion approaches rely on weighted summation, which is costly to tune and insufficient for balancing conflicting objectives. More critically, optimization with reward models is highly susceptible to reward hacking, where reward scores increase while the perceived quality of generated images deteriorates. We demonstrate that optimizing against a unified global target under heterogeneous reward upper bounds can induce reward hacking, a risk further exacerbated by the inherent instability of weak reward models. To mitigate this, we propose a Pareto Frontier-Guided Optimal Transport (PG-OT) framework. Our method constructs a prompt-specific Pareto frontier and maps dominated samples toward it via distribution-aware optimal transport. Furthermore, we develop both online and offline optimization strategies tailored to diverse reward signal characteristics. To provide a more rigorous assessment, we introduce the Joint Domination Rate (JDR) and Joint Collapse Rate (JCR) as principled metrics to quantify multi-reward synergy and reward hacking. Experimental results show that our approach outperforms strong baselines with an 11% gain in JDR and achieves a near 80% win rate in human evaluations.

---


### 82. [Dual-Pathway Circuits of Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2605.13156)

**<font color=#1a73e8>作者：</font>** Jiaxin Liu, Ding Zhong, Yue Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated remarkable capabilities in bridging visual perception and natural language understanding, enabling a wide range of multimodal reasoning tasks. However, they often produce object hallucinations, describing content absent from the input image, which limits their reliability and interpretability. To address this limitation, we propose Dual-Pathway Circuit Analysis, a framework that identifies and characterizes hallucination-related circuits in VLMs for mechanistic understanding and causal probing. We first apply activation patching across five architecturally diverse VLMs to identify a visual grounding pathway that supports correct predictions and a hallucination pathway that drives erroneous outputs. We then introduce Conditional Pathway Analysis (CPA) to characterize pathway-level interactions, revealing that grounding components remain strongly redundant in both correct and hallucinating samples but undergo a consistent polarity flip, shifting from supporting the ground truth on correct samples to aligning with the hallucinated answer on erroneous ones. We further perform targeted suppression of hallucination-pathway components, showing that scaling these components reduces object hallucination by up to 76% with minimal accuracy cost, and validate that the same circuit selectively transfers to relational but not attribute hallucination. Evaluations on POPE-adversarial and AMBER show that the identified circuits are consistent across architectures, support causal intervention, and transfer selectively across hallucination types.

---


### 83. [Continual Fine-Tuning of Large Language Models via Program Memory](https://arxiv.org/abs/2605.13162)

**<font color=#1a73e8>作者：</font>** Hung Le, Svetha Venkatesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-Efficient Fine-Tuning (PEFT), particularly Low-Rank Adaptation (LoRA), has become a standard approach for adapting Large Language Models (LLMs) under limited compute. However, in continual settings where models are updated sequentially with small datasets, conventional LoRA updates struggle to balance rapid adaptation and knowledge retention. Existing methods typically treat the low-rank space as a homogeneous update region, lacking mechanisms to regulate how short-term updates are consolidated over time. We propose a continual LoRA framework with \textbf{Pro}gram memory, inspired by \textbf{C}omplementary \textbf{L}earning Systems in neuroscience. Our approach, dubbed \textbf{ProCL}, organizes LoRA adapters into structured program memory slots that are dynamically retrieved through input-conditioned attention. This enables rapid and localized adaptation, encouraging similar inputs to reuse shared adapter regions while reserving unused capacity for future data. The slots are then combined with the underlying adapter, which maintains a distributed representation that gradually accumulates knowledge across tasks to balance plasticity and stability. Our method operates entirely within the LoRA parameterization and incurs no additional inference cost. Experiments on diverse benchmarks demonstrate improved retention and reduced catastrophic forgetting over other continual LoRA strategies.

---


### 84. [STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes](https://arxiv.org/abs/2605.13165)

**<font color=#1a73e8>作者：</font>** Chenjun Xu, Zhennan Zhou, Zhan Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long chain-of-thought (Long CoT) reasoning improves performance on multi-step problems, but it also induces overthinking: models often generate low-yield reasoning that increases inference cost and latency. This inefficiency is especially problematic in low-data fine-tuning regimes, where real applications adapt reasoning models with limited supervision and cannot rely on large-scale teacher distillation or heavy test-time control. To address this, we propose STOP (Structured On-policy Pruning), an on-policy algorithm for analyzing and pruning long-form reasoning traces. STOP constructs self-distilled traces from the model. Then it maps each trace into a structured reasoning interface through node segmentation, taxonomy annotation, and reasoning-tree construction. On top of this interface, we introduce ECN (Earliest Correct Node), which retains the shortest prefix ending at the earliest node that both functions as an answering conclusion and yields the correct final answer, removing redundant post-solution reasoning while preserving semantic continuity. Experiments on DeepSeek-R1-Distill-Qwen-7B and DeepSeek-R1-Distill-LLaMA-3-8B across GSM8K, Math 500, and AIME 2024 show that STOP reduces generated tokens by 19.4-42.4% while largely preserving accuracy in low-data fine-tuning. Beyond efficiency, our analyses show that STOP induces much smaller distributional shift than teacher-guided pruning, improves the structural efficiency of generated reasoning, and reallocates reasoning effort away from redundant verification and backtracking toward more productive exploration.

---


### 85. [PanoWorld: Towards Spatial Supersensing in 360$^\circ$ Panorama World](https://arxiv.org/abs/2605.13169)

**<font color=#1a73e8>作者：</font>** Changpeng Wang, Xin Lin, Junhan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large laboratory models (MLLMs) still struggle with spatial understanding under the dominant perspective-image paradigm, which inherits the narrow field of view of human-like perception. For navigation, robotic search, and 3D scene understanding, 360-degree panoramic sensing offers a form of supersensing by capturing the entire surrounding environment at once. However, existing MLLM pipelines typically decompose panoramas into multiple perspective views, leaving the spherical structure of equirectangular projection (ERP) largely implicit. In this paper, we study pano-native understanding, which requires an MLLM to reason over an ERP panorama as a continuous, observer-centered space. To this end, we first define the key abilities for pano-native understanding, including semantic anchoring, spherical localization, reference-frame transformation, and depth-aware 3D spatial reasoning. We then build a large-scale metadata construction pipeline that converts mixed-source ERP panoramas into geometry-aware, language-grounded, and depth-aware supervision, and instantiate these signals as capability-aligned instruction tuning data. On the model side, we introduce PanoWorld with Spherical Spatial Cross-Attention, which injects spherical geometry into the visual stream. We further construct PanoSpace-Bench, a diagnostic benchmark for evaluating ERP-native spatial reasoning. Experiments show that PanoWorld substantially outperforms both proprietary and open-source baselines on PanoSpace-Bench, H* Bench, and R2R-CE Val-Unseen benchmarks. These results demonstrate that robust panoramic reasoning requires dedicated pano-native supervision and geometry-aware model adaptation. All source code and proposed data will be publicly released.

---


### 86. [CLIP Tricks You: Training-free Token Pruning for Efficient Pixel Grounding in Large VIsion-Language Models](https://arxiv.org/abs/2605.13178)

**<font color=#1a73e8>作者：</font>** Sangin Lee, Yukyung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In large vision-language models, visual tokens typically constitute the majority of input tokens, leading to substantial computational overhead. To address this, recent studies have explored pruning redundant or less informative visual tokens for image understanding tasks. However, these methods struggle with pixel grounding tasks, where token importance is highly contingent on the input text. Through an in-depth analysis of CLIP, we observe that visual tokens located within referent regions often exhibit low similarity to the textual representation. Motivated by this insight, we introduce LiteLVLM, a training-free, text-guided token pruning strategy for efficient pixel grounding inference. By reversing the ranking of CLIP's visual-text similarity, LiteLVLM effectively retains visual tokens covering the referent regions, while recovering context tokens to enable clear foreground-background separation. Extensive experiments demonstrate that LiteLVLM significantly outperforms existing methods by over 5% across diverse token budgets. Without any training or fine-tuning, LiteLVLM maintains 90\% of the original performance with a 22% speedup and a 2.3x memory reduction. Our code is available at this https URL.

---


### 87. [STAR: Semantic-Temporal Adaptive Representation Learning for Few-Shot Action Recognition](https://arxiv.org/abs/2605.13202)

**<font color=#1a73e8>作者：</font>** Hongli Liu, Yu Wang, Shengjie Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot action recognition (FSAR) requires models to generalize to novel action categories from only a handful of annotated samples. Despite progress with vision-language models, existing approaches still suffer from semantic-temporal misalignment, where static textual prompts fail to capture decisive visual cues that appear sparsely across sequences, and from inadequate modeling of multi-scale temporal dynamics, as short-term discriminative cues and long-range dependencies are often either oversmoothed or fragmented. To address these challenges, we propose Semantic Temporal Adaptive Representation Learning (STAR), a unified framework, consisting of a semantic-alignment component and a temporal-aware component, effectively bridging the semantic and temporal gaps and transferring the sequence modeling capability of Mamba into the FSAR. The semantic alignment module introduces a Temporal Semantic Attention (TSA) mechanism, which performs frame-level cross-modal alignment with textual cues, ensuring fine-grained semantic-temporal consistency. The temporal-aware module incorporates a Semantic Temporal Prototype Refiner (STPR) that integrates semantic-guided Mamba blocks with multi-frequency temporal sampling and bidirectional state-space refinement, yielding semantically aligned prototypes with enhanced discriminative fidelity and temporal consistency. Furthermore, temporally dependent class descriptors derived from large language models (LLMs) provide long-range semantic guidance. Extensive experiments on five FSAR benchmarks demonstrate the consistent superiority of STAR over state-of-the-art methods. For instance, STAR achieves up to 8.1% and 6.7% gains on the SSv2-Full and SSv2-Small datasets under the 1-shot setting, and 7.3% on HMDB51, validating its effectiveness under limited supervision. The code is available at this https URL.

---


### 88. [GAGPO: Generalized Advantage Grouped Policy Optimization](https://arxiv.org/abs/2605.13217)

**<font color=#1a73e8>作者：</font>** Siyuan Zhu, Chao Yu, Rongxin Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a powerful paradigm for post-training large language model agents, yet credit assignment in multi-turn environments remains a challenge. Agents often receive sparse, trajectory-level rewards only at the end of an episode, making it difficult to determine which intermediate actions contributed to success or failure. As a result, propagating delayed outcomes back to individual decision steps without relying on costly auxiliary value models remains an open problem. We propose Generalized Advantage Grouped Policy Optimization (GAGPO), a critic-free reinforcement learning method for precise, step-aligned temporal credit assignment. GAGPO constructs a non-parametric grouped value proxy from sampled rollouts and uses it to compute TD/GAE-style temporal advantages, recursively propagating outcome supervision backward through time. Combined with group-wise advantage normalization and an action-level importance ratio, GAGPO extracts stable, localized optimization signals directly from multi-turn trajectories. Experiments on ALFWorld and WebShop show that GAGPO outperforms strong reinforcement learning baselines. Further analyses demonstrate faster early-stage learning, improved interaction efficiency, and smoother optimization dynamics, suggesting that GAGPO offers a simple yet effective framework for multi-turn agentic reinforcement learning.

---


### 89. [Machine Learning-Driven Multimodal Spectroscopic Liquid Biopsy for Early Multicancer Detection](https://arxiv.org/abs/2605.13218)

**<font color=#1a73e8>作者：</font>** Alejandro Leonardo García Navarro, Javier Cachón Ortiz, Javier González Colsa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cancer is one of the leading causes of death worldwide, making the development of rapid, minimally invasive, label-free and scalable diagnostic strategies a major challenge in modern oncology. In this context, spectroscopic liquid biopsy has emerged as a promising alternative, as it enables the holistic characterization of biochemical alterations in biological fluids. In this work, we propose a multimodal spectroscopic liquid biopsy framework for multicancer detection based on the combination of Fourier Transform Infrared (FTIR) spectroscopy, Raman spectroscopy, and Excitation-Emission Matrix (EEM) fluorescence spectroscopy together with Machine Learning (ML) methodologies. Serum samples from breast cancer patients, colorectal cancer patients, and healthy controls were analyzed through the three spectroscopic modalities. After modality-specific preprocessing, low-level data fusion (LLDF) was employed to integrate the complementary biochemical information encoded within the different spectroscopic measurements, and classification was performed using XGBoost models. Seven experimental configurations were evaluated, including the three unimodal approaches, all pairwise bimodal configurations, and the full multimodal approach of FTIR, Raman, and EEM fluorescence. The results show that although several individual modalities achieved high discrimination performance, the multimodal fusion provided the most balanced overall results, reaching a ROC-AUC of 0.997 for breast cancer and 0.994 for colorectal cancer, together with highly balanced sensitivity and specificity values.

---


### 90. [An Agentic AI Framework with Large Language Models and Chain-of-Thought for UAV-Assisted Logistics Scheduling with Mobile Edge Computing](https://arxiv.org/abs/2605.13221)

**<font color=#1a73e8>作者：</font>** Hanwen Zhang, Dusit Niyato, Wei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In cloud manufacturing, unmanned aerial vehicles (UAVs) can support both product collection and mobile edge computing (MEC). This joint operation forms a hybrid scheduling problem, where physical logistics decisions are coupled with computational task scheduling. In this paper, UAVs collect finished products from manufacturing stations and transport them back to a central depot. Meanwhile, computational tasks generated by industrial sensor devices at these stations are processed locally, at UAVs, or offloaded via UAVs to the cloud. This coupling makes the problem challenging. A UAV can provide MEC services only during its service window at a station, so routing decisions directly determine when UAV-assisted offloading is available. Routing decisions also affect the UAV energy budget and the availability of onboard computing and communication resources for computational task execution under task deadline constraints. To address this, we propose an agentic-AI-assisted optimization framework with two components. First, we develop an agentic AI that combines large language models, retrieval-augmented generation, and chain-of-thought reasoning to translate user input into an interpretable mathematical formulation for the hybrid scheduling problem. Second, we design a hierarchical deep reinforcement learning approach based on proximal policy optimization (PPO), where the upper layer learns UAV routing and the lower layer optimizes per-slot task execution and resource allocation. Simulation results show that the proposed framework yields more consistent formulations, while the hierarchical PPO achieves full product collection in 99.6% of the last 500 episodes and maintains a 100% deadline satisfaction rate, with more stable performance than the advantage actor-critic approach.

---


### 91. [Mix, Don't Tune: Bilingual Pre-Training Outperforms Hyperparameter Search in Data-Constrained Settings](https://arxiv.org/abs/2605.13225)

**<font color=#1a73e8>作者：</font>** Paul Jeha, Anastasiia Sedova, Louis Béthune 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For most languages of the world, language model pre-training operates in a data-constrained regime where models must repeat their training data many times, degrading generalization. Two remedies exist: aggressive hyperparameter tuning such as high weight decay, and mixing in data from a high-resource auxiliary language to directly aid the low-resource target. While hyperparameter tuning regularizes the model by shrinking weights to restrict network capacity, auxiliary data mixing uses a tunable mixing ratio to expand the training distribution and diversify the training signal with new knowledge. Both offer a principled way to improve training in a data-constrained domain. We compare these levers systematically across four model scales from 150M to 1.43B parameters, using Arabic as the low-resource target and English as the auxiliary, over approximately 1000 pre-training runs. Three findings emerge. First, mixing yields larger improvements than hyperparameter tuning on both validation loss and downstream task accuracy, and the gap grows with model size. Second, we quantify how much mixing helps: it boosts performance by an amount equivalent to 2--3$\times$ the unique target data on validation loss and 2--13$\times$ on downstream task accuracy, with the gain scaling steeply with model size. Third, this divergence reveals that target-language validation loss systematically underestimates mixing's value. Mixing regularizes by diversifying the training signal and contributes knowledge the repeated target corpus cannot supply; validation loss captures only the first effect. Our practical recommendations are: mix in a high-resource language, prioritize the mixing ratio over hyperparameter tuning, and transfer hyperparameters from a small proxy model via $\mu$P.

---


### 92. [Teacher-Guided Policy Optimization for LLM Distillation](https://arxiv.org/abs/2605.13230)

**<font color=#1a73e8>作者：</font>** Xinyu Liu, Kechen Jiao, Chunyang Xiao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The convergence of reinforcement learning and imitation learning has positioned Reverse KL (RKL) as a promising paradigm for on-policy LLM distillation, aiming to unify exploration with teacher supervision. However, we identify a critical limitation: when the student and teacher distributions diverge significantly, standard RKL often fails to yield meaningful improvement due to uninformative negative feedback. To address this inefficiency, we propose Teacher-Guided Policy Optimization (TGPO), an on-policy algorithm that incorporates dense directional guidance by leveraging teacher predictions conditioned on the student's rollout. Because TGPO remains on-policy, the algorithm integrates seamlessly with existing RLVR frameworks without requiring additional data annotation. Experiments on complex reasoning benchmarks demonstrate that TGPO significantly outperforms standard baselines and is robust to different teachers.

---


### 93. [It's not the Language Model, it's the Tool: Deterministic Mediation for Scientific Workflows](https://arxiv.org/abs/2605.13245)

**<font color=#1a73e8>作者：</font>** Marios Adamidis, Danae Katrisioti, Yannis Tzitzikas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models can produce convincing scientific analyses, but repeated generations on the same data do not guarantee the same result. A researcher may regenerate an identical query and receive a different fit, a different peak position or a different analysis procedure, without an obvious way to decide which output to trust. We propose typed mediation, a pattern in which the model orchestrates deterministic tools rather than generating analytical code. Each tool encodes one researcher's exact procedure for one instrument, ported through structured interviews. The model selects which tool to call and with what parameters. The tool produces the result. Regeneration does not change it. We evaluate this claim by running the same photoluminescence analysis on four platforms, including three commercial foundation models, four times each with the same prompt. The typed tool produces identical results across all runs. The commercial platforms either vary in numerical output and analytical methodology across runs, or fail to produce valid results on the task. We deploy this pattern on two instruments serving users over approximately six months, with very positive user feedback. Both cases are very challenging: they involve proprietary binary formats and per-seat licensed software, which force the tool to remain on local infrastructure alongside the data and the instrument it operates. We argue that deployment topology is not just a preference, but a structural requirement of scientific tool mediation. The result is a practical pattern for deploying language models in scientific workflows where reproducibility is mandatory, reducing analysis time from weeks to minutes while guaranteeing identical outputs across runs.

---


### 94. [EMO: Frustratingly Easy Progressive Training of Extendable MoE](https://arxiv.org/abs/2605.13247)

**<font color=#1a73e8>作者：</font>** Linghao Jin, Chufan Shi, Huijuan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) models offer a powerful way to scale model size without increasing compute, as per-token FLOPs depend only on k active experts rather than the total pool of E experts. Yet, this asymmetry creates an MoE efficiency paradox in practice: adding more experts balloons memory and communication costs, making actual training inefficient. We argue that this bottleneck arises in part because current MoE training allocates too many experts from the beginning, even though early-stage data may not fully utilize such capacity. Motivated by this, we propose EMO, a simple progressive training framework that treats MoE capacity as expandable memory and grows the expert pool over the course of training. EMO explicitly models sparsity in scaling law to derive stage-wise compute-optimal token budgets for progressive expansion. Empirical results show that EMO matches the performance of a fixed-expert setup in large-scale experiments while improving wall-clock efficiency. It offers a surprisingly simple yet effective path to scalable MoE training, preserving the benefits of large expert pools while reducing both training time and GPU cost.

---


### 95. [Respecting Self-Uncertainty in On-Policy Self-Distillation for Efficient LLM Reasoning](https://arxiv.org/abs/2605.13255)

**<font color=#1a73e8>作者：</font>** Junlong Ke, Zichen Wen, Weijia Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation trains a reasoning model on its own rollouts while a teacher, often the same model conditioned on privileged context, provides dense token-level supervision. Existing objectives typically weight the teacher's token-level signal uniformly across a chain-of-thought sequence, despite substantial variation in the entropy of the teacher's predictive distribution. We propose EGRSD (Entropy-Guided Reinforced Self-Distillation), which unifies token-level updates through three signals: a reward-grounded direction, a teacher-student likelihood-ratio magnitude, and the proposed teacher-entropy confidence gate that down-weights high-entropy token positions while maintaining a nonzero lower bound on every token weight. We further introduce CL-EGRSD, a causal-lookahead variant that distinguishes sustained high-entropy spans from transient high-entropy positions whose following context rapidly becomes low entropy. Experiments with Qwen3-4B and Qwen3-8B in thinking mode show that EGRSD and CL-EGRSD advance the accuracy-length frontier among the compared trainable methods.

---


### 96. [Utility-Oriented Visual Evidence Selection for Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2605.13277)

**<font color=#1a73e8>作者：</font>** Weiqing Luo, Zongye Hu, Xiao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visual evidence selection is a critical component of multimodal retrieval-augmented generation (RAG), yet existing methods typically rely on semantic relevance or surface-level similarity, which are often misaligned with the actual utility of visual evidence for downstream reasoning. We reformulate multimodal evidence selection from an information-theoretic perspective by defining evidence utility as the information gain induced on a model's output distribution. To overcome the intractability of answer-space optimization, we introduce a latent notion of evidence helpfulness and theoretically show that, under mild assumptions, ranking evidence by information gain on this latent variable is equivalent to answer-space utility. We further propose a training-free, surrogate-accelerated framework that efficiently estimates evidence utility using lightweight multimodal models. Experiments on MRAG-Bench and Visual-RAG across multiple model families demonstrate that our method consistently outperforms state-of-the-art RAG baselines while achieving substantial reductions in computational cost.

---


### 97. [CANTANTE: Optimizing Agentic Systems via Contrastive Credit Attribution](https://arxiv.org/abs/2605.13295)

**<font color=#1a73e8>作者：</font>** Tom Zehle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems have demonstrated strong performance across complex real-world tasks, such as software engineering, predictive modeling, and retrieval-augmented generation. Yet automating their configuration remains a structural challenge, as scores are available only at the system level, whereas the parameters governing agent behavior are local. We argue that optimizing these systems is fundamentally a credit-assignment problem. We therefore introduce CANTANTE, a framework that decomposes system-level rewards into per-agent update signals by contrasting rollouts of multiple joint configurations on the same query. We instantiate it for prompt optimization, treating agent prompts as learnable system parameters. We evaluate CANTANTE against GEPA and MIPROv2 on programming (MBPP), mathematical reasoning (GSM8K), and multi-hop question answering (HotpotQA). Across these benchmarks, CANTANTE achieves the best average rank among all evaluated optimizers and consistently outperforms unoptimized prompts. It improves over the strongest baseline by +18.9 percentage points on MBPP and +12.5 percentage points on GSM8K, while incurring a lower inference cost. It remains within one standard deviation of the strongest baseline on HotpotQA. Crucially, our credit correlation analysis confirms that the attributer produces meaningful per-agent signals rather than echoing the global system score.

---


### 98. [PRISM-X: Experiments on Personalised Fine-Tuning with Human and Simulated Users](https://arxiv.org/abs/2605.13307)

**<font color=#1a73e8>作者：</font>** Hannah Rose Kirk, Liu Leqi, Fanzhi Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalisation is a standard feature of conversational AI systems used by millions; yet, the efficacy of personalisation methods is often evaluated in academic research using simulated users rather than real people. This raises questions about how users and their simulated counterparts differ in interaction patterns and judgements, as well as whether personalisation is best achieved through context-based prompting or weight-based fine-tuning. Here, in a large-scale within-subject experiment, we re-recruit 530 participants from 52 countries two years after they gave their preferences in the PRISM dataset (Kirk et al., 2024) to evaluate personalised and non-personalised language models in blinded multi-turn conversations. We find preference fine-tuning (P-DPO, Li et al., 2024) significantly outperforms both a generic model and personalised prompting but adapting to individual preference data yields marginal gains over training on pooled preferences from a diverse population. Beyond length biases, fine-tuning amplifies sycophancy and relationship-seeking behaviours that people reward in short-term evaluations but which may introduce deleterious long-term consequences. Replicating this within-subject experiment with simulated users recovers aggregate model hierarchies but simulators perform far below human self-consistency baselines for individual judgements, discuss different topics, exhibit amplified position biases, and produce feedback dynamics that diverge from humans.

---


### 99. [Supervised Deep Multimodal Matrix Factorization for Interpretable Brain Network Analysis](https://arxiv.org/abs/2605.13312)

**<font color=#1a73e8>作者：</font>** Amjad Seyedi, Lifang He, Songlin Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Supervised Deep Multimodal Matrix Factorization (SD3MF), an interpretable framework for integrative brain network analysis that generalizes Symmetric Nonnegative Matrix Tri-Factorization (SNMTF) from unsupervised single-graph clustering to supervised prediction over populations of multimodal graphs. SD3MF learns deep hierarchical factorizations for each modality together with a shared latent representation that aligns subjects across views. An encoder-decoder formulation jointly optimizes graph reconstruction and supervised prediction, while adaptive weights enable data-driven multimodal fusion. By representing each subject through community-level interaction matrices, the model yields interpretable and discriminative features. Experiments on multimodal connectome datasets show that SD3MF consistently outperforms strong deep learning baselines such as CNNs and GNNs, while enabling biologically interpretable insights. Code for reproducibility is available at: this https URL.

---


### 100. [KamonBench: A Grammar-Based Dataset for Evaluating Compositional Factor Recovery in Vision-Language Models](https://arxiv.org/abs/2605.13322)

**<font color=#1a73e8>作者：</font>** Richard Sproat, Stefano Peluchetti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Kamon (family crests) are an important part of Japanese culture and a natural test case for compositional visual recognition: each crest combines a small number of symbolic choices, but the space of possible descriptions is sparse. We introduce KamonBench, a grammar-based image-to-structure benchmark with 20,000 synthetic composite crests and auxiliary component examples. Each composite crest is paired with a formal kamon description language - "kamon yōgo" - description, a segmented Japanese analysis, an English translation, and a non-linguistic program code. Because each synthetic crest is generated from known factors, namely container, modifier, and motif, KamonBench supports evaluation beyond caption-level accuracy: direct program-code factor metrics, controlled factor-pair recombination splits, counterfactual motif-sensitivity groups under fixed container-modifier contexts, and linear probes of factor accessibility. We include baseline results for a ViT encoder/Transformer decoder and two VGG n-gram decoders, with and without learned positional masks. KamonBench therefore provides a controlled testbed for sparse compositional visual recognition and factor recovery in vision-language models.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-159](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
