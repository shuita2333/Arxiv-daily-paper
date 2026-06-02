# 🧠 大模型相关研究 | 2026年06月03日

> 本类共 **376** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

---

### 101. [Scaling Behavior of Single LLM-Driven Multi-Agent Systems](https://arxiv.org/abs/2606.00655)

**<font color=#1a73e8>作者：</font>** Jialing Li, Zhouhong Gu, Yin Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The burgeoning field of LLM-based Multi-Agent Systems (MAS) promises to tackle complex tasks through collaborative intelligence, yet fundamental questions regarding their scaling behavior and intrinsic collective dynamics remain underexplored. This paper systematically investigates how the performance of a homogeneous MAS evolves as the number of agents increases, isolating the variable of collaboration from model or knowledge heterogeneity. We propose the Sequential Iterative Multi-Agent System (SIMAS) framework, a minimalist architecture centered on sequential inter-agent communication, to clearly observe scaling effects. Through extensive experiments across diverse tasks and model scales, we establish that MAS performance does not scale monotonically with agent count but follows a pattern of diminishing returns, governed by a trade-off between collaborative synergy and coordination overhead. Our findings reveal that effective MAS requires a sufficiently capable base LLM, that task type critically modulates the optimal agent count, and that collective intelligence is an emergent property contingent on strategic interaction design rather than a guaranteed outcome of agent plurality. The performance degradation stems coordination overhead rather than merely long-context failure, and the scaling tendency generalizes across interaction architectures like structured debate topologies. This work provides a foundational understanding of MAS scaling laws, offering practical guidance for designing efficient collaborative systems and challenging the prevailing assumption that more agents invariably lead to better performance.

---


### 102. [FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Verification for Agentic Search](https://arxiv.org/abs/2606.00660)

**<font color=#1a73e8>作者：</font>** James Xu Zhao, Hui Chen, Bryan Hooi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic search requires language model agents to explore many sources and answer complex information-seeking questions. Scaling test-time compute is a promising way to improve these agents, but current approaches can fail, because correct answers are often sparse and score-based selection depends on model calibration. We propose FineVerify, a fine-grained self-verification framework that decomposes each question into checkable sub-questions, verifies sampled candidates against each sub-question, and selects the candidate with the highest aggregated score. This per-check structure turns selection into simpler local judgments and produces scores under the same explicit criteria. Across four agentic search benchmarks and two models, FineVerify consistently outperforms standard scaling baselines. With only four sampled trajectories, it improves GPT-5-mini by 8.2 accuracy points and Gemini-3-flash by 5.6% on average. With 12 samples, FineVerify enables GPT-5-mini to surpass frontier GPT-5 on BrowseComp-Plus. Beyond accuracy, FineVerify produces interpretable verification traces that help audit benchmark errors, suggesting broader applications for inspecting agentic search systems. Code and data are available at this https URL

---


### 103. [The Paradox of Outcome Optimization: A Causal Information-Theoretic Bound on Reasoning Shortcuts in LLMs](https://arxiv.org/abs/2606.00674)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Yiming Zhang, Wenxiang Geng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) aligned via outcome-based Reinforcement Learning (RL) frequently exhibit a critical failure mode: they achieve high performance on in-distribution benchmarks while demonstrating brittle reasoning capabilities on out-of-distribution (OOD) tasks. We term this phenomenon Reward-Induced Manifold Collapse. We establish a theoretical framework bridging Structural Causal Models (SCM) and the Information Bottleneck (IB) principle to explain this paradox. We define reasoning as a high-complexity causal process and shortcut learning as the exploitation of low-complexity spurious correlations. Under the implicit inductive bias of Stochastic Gradient Descent (SGD), models optimized for outcome rewards are biased toward shortcut solutions whenever the training distribution allows for a ``Markovian Screening'' of the true causal mechanism. We derive a new generalization bound based on Semantic Coverage Measure ($\eta$) rather than sample size, showing why data scaling on homogeneous distributions may fail to correct reasoning flaws. We also show that Process Reward Models (PRMs) function as Topological Filters, enforcing step-wise mutual information constraints that render the low-complexity shortcut manifold inadmissible. These results provide a mathematical grounding for the role of process supervision beyond simple credit assignment.

---


### 104. [OCC-RAG: Optimal Cognitive Core for Faithful Question Answering](https://arxiv.org/abs/2606.00683)

**<font color=#1a73e8>作者：</font>** Maksim Savkin, Mikhail Goncharov, Alexander Gambashidze 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent progress in the development of language models has been defined by scale, with each generation absorbing more of the world's knowledge into its weights. However, many practical applications benefit more from robust reasoning than from extensive parametric knowledge. In this setting, task-specialized small language models (SLMs) offer a principled design choice. We introduce Optimal Cognitive Core (OCC), a family of SLMs built around this premise. As a variant of OCC, we present OCC-RAG, optimized for faithful question answering (QA) grounded in the provided context. This task directly aligns with the OCC design approach, requiring multi-hop reasoning over supplied passages while ignoring memorized knowledge. To train OCC-RAG, we implement a novel pipeline for synthesizing multi-context, multi-hop QA data at scale, producing a corpus of over three million examples targeting multi-hop reasoning, strict context faithfulness, and calibrated abstention. We release OCC-RAG-0.6B and OCC-RAG-1.7B, both mid-trained on this corpus. The models produce structured reasoning traces with source citations grounded in literal quotes from the context. Through OCC-RAG, we demonstrate that compact, task-specialized SLMs can match or exceed general-purpose models 2 -- 6x their size across multi-hop reasoning (HotpotQA, MuSiQue, TAT-QA), faithfulness (ConFiQA), and refusal (MuSiQue-Un) benchmarks.

---


### 105. [Dialectics of Alignment: Harnessing Unsafe Knowledge for Dynamic Safety Routing](https://arxiv.org/abs/2606.00686)

**<font color=#1a73e8>作者：</font>** Maryam Hashemzadeh, Jerry Huang, Minseon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The prevailing paradigm in large language model (LLM) alignment operates via erasure, filtering unsafe data or training models to strictly refuse harmful prompts. While effective at reducing immediate toxicity, this approach fundamentally constricts the model's epistemological scope, resulting in over-cautious systems that output uninformative blanket refusals to sensitive yet benign queries. In this work, we challenge the orthodoxy that unsafe data must be discarded. We propose a dialectical approach to alignment, positing that unsafe data encodes rich, domain specific knowledge critical for nuanced, safe, and informative generation. To operationalize this, we introduce SafeMoE, a Mixture-of-Experts (MoE) framework that isolates unsafe knowledge into domain-specific Low-Rank Adapters (LoRA experts) trained exclusively on harmful corpora. To synthesize safety from these unsafe primitives, we train a lightweight gating network using a minimal, highly curated set of safe-informative responses. During inference, this router dynamically orchestrates the unsafe experts, effectively steering the generation trajectory to harness their deep domain knowledge while strictly enforcing safety constraints. Extensive empirical evaluations across stringent safety benchmarks demonstrate that SafeMoE is not only safer, achieving over a 20% relative improvement in safe response rate (more than a 15% absolute gain), but also produces more informative responses when safety and harmfulness are of paramount concern. Furthermore, the routing mechanism exhibits strong zero-shot generalization to unseen domains and broader safety tasks without domain-specific supervision. Our findings suggest a paradigm shift in alignment: true safety requires not the masking of unsafe knowledge, but its controlled integration.

---


### 106. [Wavelet-Fusion Diffusion Model for Multimodal Brain MRI Synthesis with Modality and Metadata Conditioning](https://arxiv.org/abs/2606.00689)

**<font color=#1a73e8>作者：</font>** Muhammad Nabi Yasinzai, Remika Mito, Mangor Pedersen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal MRI provides complementary information for neuroimaging analysis, where different imaging modalities capture distinct anatomical, tissue, and pathological features that support the development and evaluation of downstream AI applications. Although large-scale structural MRI resources are increasingly available, their modality coverage is often uneven across public and pooled neuroimaging datasets. This uneven modality coverage is further complicated by heterogeneity across sites, scanners, and acquisition protocols, as well as demographic and clinical variables that are often sparse, inconsistently recorded, or unavailable across studies. Synthetic MRI generation can help address this imbalance by synthesizing target-modality volumes for dataset augmentation and controlled synthetic cohort creation. However, many existing MRI synthesis approaches are trained on narrow modality sets or relatively homogeneous cohorts, limiting their applicability to large pooled neuroimaging resources where modality availability, acquisition protocols, and metadata coverage vary substantially across datasets. Diffusion models have become an attractive approach for MRI synthesis because of their strong sample fidelity and diversity, but sampling directly in 3D voxel space is computationally expensive and slow at inference. Latent diffusion improves practicality by synthesizing MRI in a learned, 3D latent space, although generation quality depends on the autoencoder's reconstruction fidelity and the resulting latent distribution. Our approach combines a Wavelet-Fusion variational autoencoder (WF-VAE) latent compressor with a conditional 3D U-Net diffusion model trained in the learned latent space using explicit modality and metadata conditioning. Our proposed Wavelet-Fusion Diffusion Model (WFDM) achieved the strongest distributional alignment among the evaluated synthetic MRI generators.

---


### 107. [MOSAIC: Modular Orchestration for Structured Agentic Intelligence and Composition](https://arxiv.org/abs/2606.00708)

**<font color=#1a73e8>作者：</font>** Yifan Bao, Xinyu Xi, Xinyu Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated data science is a structured model-selection problem. A solution must choose data transformations, feature representations, architecture, training procedure, evaluation protocol, and refinement strategy for a task. AutoML systems automate parts of this process, but typically search within predefined pipeline, model, and hyperparameter spaces. LLM-based agents offer greater flexibility through retrieval, code generation, and execution feedback, yet their modelling decisions are often unstructured, difficult to verify, and hard to reuse. We introduce \textsc{MOSAIC} (Modular Orchestration for Structured Agentic Intelligence and Composition), a structured agentic framework for memory-grounded model selection and workflow construction. Given a task and dataset, \textsc{MOSAIC} builds a semantic task profile, retrieves prior cases and source-code modules, and constructs a blueprint: an intermediate representation specifying selected modelling components, composition, interface constraints, and execution requirements. This blueprint turns model selection into a staged, context-grounded search and grounds LLM-based code generation in retrieved evidence rather than unconstrained synthesis. Candidate models are validated by execution and refined using diagnostic feedback, training traces, task metrics, and a failure-aware reinforcement learning policy. We instantiate \textsc{MOSAIC} on financial time-series forecasting and generation, where models must satisfy predictive accuracy, distributional fidelity, execution reliability, and downstream financial criteria such as risk and tail behaviour. Experiments against AutoML and agentic baselines show that \textsc{MOSAIC} improves task performance, execution success, and decision traceability, demonstrating the value of treating automated data science as structured, reusable, and execution-grounded model selection.

---


### 108. [LLM-Driven Co-Evolutionary Automated Heuristic Design for Bi-Component Coupled Combinatorial Optimization](https://arxiv.org/abs/2606.00718)

**<font color=#1a73e8>作者：</font>** Mingen Kuang, Xudong Deng, Xi Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have recently shown promise in Automated Heuristic Design (AHD), existing methods typically generate and evolve heuristics as a single operator or search strategy, limiting their ability to model strong coupling among multiple decision substructures in problems such as the Traveling Thief Problem (TTP) and the Traveling Purchaser Problem (TPP). In this work, we propose CoEvo-AHD, an LLM-driven dual-population co-evolutionary framework for automated heuristic design in coupled combinatorial optimization. Unlike prior methods that evolve individual heuristics in isolation, CoEvo-AHD leverages LLMs to co-evolve two closely related operator populations. A cooperative evaluation mechanism explicitly captures interactions between route and selection operators, while pairwise scoring and synergistic joint crossover help discover complementary operator logic for joint improvement across coupled decision subspaces. We further design a tool-invocation environment library that encapsulates frequently used core operations, such as local-search delta computation, into callable functions, enabling LLM-generated operators to use standardized interfaces instead of reimplementing inefficient and error-prone problem-specific loops. Experiments on TTP and TPP show that CoEvo-AHD automatically discovers cooperative heuristic combinations and achieves competitive solution quality against traditional heuristics.

---


### 109. [EPIC: Efficient and Parallel Inference under CFG Constraints for Diffusion Language Models](https://arxiv.org/abs/2606.00722)

**<font color=#1a73e8>作者：</font>** Hyundong Jin, Yo-Sub Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Controlling language model outputs is essential for ensuring structural validity, reliability, and downstream usability, and diffusion language models are no exception. Recent advances in diffusion language model decoding have extended output control beyond regular constraints to context-free grammar (CFG) constraints. Existing methods, however, can be up to four times slower than unconstrained decoding. More importantly, they substantially diminish one of the key advantages of diffusion language models over autoregressive models, namely parallel decoding. This slowdown arises because sequential validity checking introduces significant overhead during parallel generation. We propose an efficient CFG-constrained decoding framework, EPIC, that addresses this limitation. Our method improves decoding efficiency by combining lexing memoization, validation using Earley-style parsing instead of deterministic automata, and relaxed compatible subset selection for parallel commit. It reduces repeated lexing and validation overhead while allowing multiple compatible tokens to be committed together. Experiments on three benchmarks using four models show that our method reduces inference time by up to 67.5% and decreases the additional overhead by up to 90.5% compared with existing CFG-constrained decoding methods. Our implementation is available at this https URL .

---


### 110. [WaveFilter: Enhancing the Long-Context Capability of Diffusion LLMs via Wavelet-Guided KV Cache Filtering](https://arxiv.org/abs/2606.00724)

**<font color=#1a73e8>作者：</font>** Jinnan Yang, Yan Wang, Zhen Bi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (DLMs) have demonstrated significant advantages across various tasks. However, constrained by their multi-step iterative inference mechanism, their computational overhead and inference latency in long-context tasks have become core bottlenecks restricting their large-scale deployment. When processing long sequences, existing Key-Value (KV) caching mechanisms often face a dilemma where generation quality degrades drastically, where the core challenge lies in precisely and efficiently filtering critical tokens within ultra-long contexts. Inspired by the human reading process, we propose \textbf{WaveFilter}, a universal and training-free caching framework. This framework innovatively introduces the wavelet transform for decomposition of long sequences to achieve precise identification of key tokens, based on which a sparse KV Cache is constructed to compute the final contextual representation. Experimental results demonstrate that WaveFilter, as a plug-and-play generic framework, significantly enhances the performance of existing mainstream KV Cache methods in complex long-context tasks.

---


### 111. [Latent Reward Steering: An Adaptive Inference-Time Framework that Implicitly Promotes Cognitive Behaviors in Reasoning LLMs](https://arxiv.org/abs/2606.00726)

**<font color=#1a73e8>作者：</font>** Jiakang Li, Guanyu Zhu, Can Jin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Strong reasoning depends not only on model knowledge but also on how effectively cognitive behaviors are deployed during generation. Existing methods often rely on explicit behavior-level control, making them insufficiently adaptive when failures and required corrections vary across reasoning states, tasks, and models. To this end, we propose Latent Reward Steering (LRS), an adaptive inference-time framework that promotes cognitive behaviors by optimizing the sparse-autoencoder (SAE) latent states that implicitly carry them. Rather than relying on predefined cognitive behaviors or steering directions derived from them, LRS trains a latent reward model on reasoning traces by final answer correctness to estimate the quality of intermediate latent states. During inference, reward gradients provide state-specific correction directions for fragile latent states, while a reward and confidence gate restricts intervention to states the reward signal flags as fragile. Experiments on multiple reasoning LLM backbones and benchmarks show that \ours consistently improves performance over various baselines, and post-hoc analyses further indicate that \ours implicitly promotes good cognitive behaviors that fix the original reasoning errors. Code is available at: this https URL.

---


### 112. [I-WebGenBench : Evaluating Interactivity in LLM-Generated Scientific Web Applications](https://arxiv.org/abs/2606.00750)

**<font color=#1a73e8>作者：</font>** Dasen Dai, Biao Wu, Meng Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in visual language models have enabled autonomous agents for complex reasoning, tool use, and document understanding. However, existing document agents mainly transform papers into static artifacts such as summaries, webpages, or slides, which are insufficient for technical papers involving dynamic mechanisms and state transitions. In this work, we propose a Paper-to-Interactive-System Agent that converts research papers into executable interactive web systems. Given a PDF paper, the agent performs end-to-end processing without human intervention, including paper understanding, system modeling, and interactive webpage synthesis, enabling users to manipulate inputs and observe dynamic behaviors. To evaluate this task, we introduce a benchmark of 19 research papers paired with expert-built interactive systems as ground truth. We further propose PaperVoyager, a structured generation framework that explicitly models mechanisms and interaction logic during synthesis. Experiments show that PaperVoyager significantly improves the quality of generated interactive systems, offering a new paradigm for interactive scientific paper understanding.

---


### 113. [A multimodal dataset of photoplethysmography and continuous behavioral responses to ASMR and nature videos](https://arxiv.org/abs/2606.00752)

**<font color=#1a73e8>作者：</font>** Tushar Das, Daigo Hozaki, Koushlendra Kumar Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous Sensory Meridian Response (ASMR) is a somatosensory phenomenon characterized by pleasant tingling sensations and cardiovascular slowing. However, ASMR research has been hindered by a dearth of standardized, open-access multimodal datasets. To address this limitation, we present REST-ASMR (Response to Environmental & Sensory Triggers), a synchronized multimodal dataset designed to capture behavioral reports and physiological dynamics during ASMR, with nature-relaxation videos as control stimuli. The dataset includes high-resolution photoplethysmography (PPG), time-aligned audiovisual stimuli, and continuous subjective annotations from 34 participants. Technical validation showed high stimulus efficacy (97% responder rate), significant stimulus-specific inter-subject agreement (p < 0.05), and a robust PPG-derived ASMR-specific cardiovascular deceleration. Additionally, a Bidirectional Long-Short Term Memory model successfully predicted subjective ASMR tingle states, achieving video-level ASMR vs. Nature classification with perfect accuracy and a frame-level global mean accuracy of 75.51%, macro F1-score of 71.86%, and 100% Nature-baseline specificity, under a strict, leakage-free subject-video double-independent 4-fold cross-validation. REST-ASMR constitutes a dense temporal foundation for affective computing, multimodal research, and the development of personalized models of relaxation-related responses.

---


### 114. [CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems](https://arxiv.org/abs/2606.00756)

**<font color=#1a73e8>作者：</font>** Yannan Wang, Longli Yang, Zhen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying lightweight Large Language Model (LLM) agents on edge servers can reduce latency and move agentic services closer to users, but resource-constrained edge models often struggle with long-horizon tasks that require persistent memory, subgoal tracking, and reflection. Fine-tuning edge models after deployment is costly and difficult to scale across heterogeneous nodes, while purely local memory leaves agents with isolated experience and growing prompt context. We propose \textsc{CoMIC}, a parameter-update-free cloud-edge framework for Collaborative Memory and Insights Circulation. \textsc{CoMIC} follows a \textit{Centralized Reflection, Decentralized Execution} design: edge agents execute locally using subgoal-oriented hierarchical memory and selective re-expansion of relevant histories, while a cloud-side LLM critic asynchronously evaluates completed trajectories, filters reusable experience, and aggregates cross-agent guidance keyed by semantic subgoal identifiers. Across five long-horizon agent tasks spanning symbolic planning and text interaction, \textsc{CoMIC} improves progress rate and action grounding for weak edge agents and yields task-dependent success-rate gains without updating model parameters.

---


### 115. [FALAT: Tracing Failures in LLM Agent Trajectories via Dependency-Guided Search](https://arxiv.org/abs/2606.00765)

**<font color=#1a73e8>作者：</font>** Md Nakhla Rafi, Md Ahasanuzzaman, Dong Jae Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly solve complex tasks through long trajectories involving reasoning steps, tool calls, and inter-agent communication. However, when these agents fail, it is often unclear which agent caused the failure and which step introduced the decisive error. This attribution problem is challenging because mistakes can propagate across the trajectory: later actions may appear incorrect, but only because they depend on an earlier corrupted state. Therefore, failure attribution cannot be treated as independent step-level classification.
We propose FALAT, a diagnostic framework for failure attribution in LLM agent trajectories. FALAT frames attribution as a dependency-guided search problem. It first constructs an expectation of how the task should be solved and uses this expectation to identify suspicious regions in the trajectory. It then traces dependencies among decisions, tool outputs, and agent messages to distinguish error-introducing steps from steps that merely inherit or propagate prior mistakes. Finally, FALAT evaluates whether correcting a candidate step would be sufficient to recover the expected outcome, allowing it to identify both the responsible agent and the decisive failure step.
We evaluate FALAT on the Who&When benchmark, which includes both algorithm-generated and hand-crafted multi-agent failure trajectories. The results show that FALAT consistently improves responsible-agent and decisive-step attribution. Its best configurations achieve 46.0% step-level accuracy on algorithm-generated trajectories and 29.1% on the more challenging hand-crafted trajectories, outperforming specialized attribution baselines and direct prompting with standalone LLMs. These findings suggest that dependency-aware reasoning is essential for reliable failure diagnosis in LLM agent systems.

---


### 116. [Behavior-Invariant Task Representation Learning with Transformer-based World Models for Offline Meta-Reinforcement Learning](https://arxiv.org/abs/2606.00780)

**<font color=#1a73e8>作者：</font>** Fuyuan Qian, Menglong Zhang, Song Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline meta-reinforcement learning leverages static datasets to enable agents to generalize to unseen environments by combining offline efficiency with meta-learning adaptability, yet it faces key challenges from context and policy distribution shifts. These issues hinder agents from adapting to online environments, and are further exacerbated under sparse-reward settings. As a result, agents often become trapped in an inherent pattern dilemma, failing to achieve robust generalization. In this work, we propose a novel framework that integrates information-theoretic task representation learning with a Transformer-based stochastic world model. Our approach extracts task-defining latent variables that are invariant to behavior policy, thereby effectively mitigating the context distribution shift. To further handle policy shift and model exploitation, we apply a conservative value penalty to imagination-based rollouts, preventing the policy from exploiting model inaccuracies while maintaining robust adaptation. Extensive evaluations demonstrate that our method outperforms state-of-the-art approaches, with superior stability and generalization under out-of-distribution and sparse-reward settings.

---


### 117. [FlowOVD: Learning Generative Latent Flows for Zero-shot Open-vocabulary Detection](https://arxiv.org/abs/2606.00782)

**<font color=#1a73e8>作者：</font>** Yao Wei, Andrea Cavallaro, Changjae Oh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary object detection (OVD) has achieved remarkable progress through large-scale vision-language pre-training. Existing methods, however, typically formulate OVD as a discriminative prediction problem, where decoder queries are either static or initialized from encoder features, thus limiting their diversity and flexibility. In this paper, we introduce a generative perspective by modeling decoder query generation as a continuous transport process in latent space. We propose FlowOVD, a text-conditioned query generation framework based on rectified flow that progressively transforms text-agnostic queries into text-guided queries. By introducing continuous latent query dynamics into a vision-language model (VLM) based detector, our method avoids heuristic discrete query construction and enables more expressive semantic alignment for open-vocabulary detection. Without requiring additional training data, FlowOVD achieves 49.5 AP on COCO and 31.5 AP on LVIS, outperforming GroundingDINO by +1.2 AP (+2.5 %) and +4.1 AP (+15.0 %), respectively. The larger gain on the challenging long-tailed LVIS benchmark further highlights the effectiveness of continuous query generation for open-vocabulary generalization.

---


### 118. [MBench: A Comprehensive Benchmark on Memory Capability for Video World Models](https://arxiv.org/abs/2606.00793)

**<font color=#1a73e8>作者：</font>** Shengjun Zhang, Zhang Zhang, Simin Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in video-based world models have demonstrated an unprecedented ability to synthesize high-fidelity visual sequences. However, a fundamental gap persists between visually plausible video generation and the functional requirements of a world model, particularly in maintaining a stable and reasonable internal state over extended temporal horizons. While existing benchmarks primarily emphasize visual quality, motion coherence, and text-video alignment, they largely overlook memory, the core capability of a world model to preserve consistency across long-term horizons and complex interactions. To address this gap, we present \textbf{MBench}, a comprehensive benchmark dedicated to quantifying and evaluating the memory capability of video world models. We systematically decompose the memory capability of video world models into three hierarchical and complementary core dimensions: entity consistency, environment consistency, and causal consistency, which are further refined into 12 quantifiable sub-dimensions for comprehensive characterization of long-term memory. Our benchmark is built upon rigorously curated real-captured long videos, and evaluated by rule-based quantitative matrices and VLM to enable objective and comprehensive consistency assessment. Extensive evaluations of mainstream state-of-the-art video world models reveal critical systemic limitations of existing methods in long-term state retention, providing a standardized benchmark and clear research direction to advance the field.

---


### 119. [OmniEEG-Bench: A Standardized Evaluation Benchmark for EEG Foundation Models](https://arxiv.org/abs/2606.00815)

**<font color=#1a73e8>作者：</font>** Ziling Lu, Zongsheng Li, Xinke Shen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) supports a variety of brain-computer interface (BCI) tasks ranging from brain-state monitoring to human-LLM interactions. EEG foundation models are emerging, but evaluation remains fragmented due to heterogeneous datasets and nconsistent task protocols. Here, we introduce OmniEEG-Bench, a unified benchmark and downstream task roadmap for EEG foundation models (FMs). It organizes evaluation of EEG FMs into six task families spanning (i) signal reliability, (ii) biometrics and disease, (iii) consciousness and state, (iv) cognition and emotion, (v) naturalistic stimulus decoding, and (vi) motor and interaction, introducing a new generation of tasks not systematically benchmarked in prior EEG FM work. OmniEEG-Bench standardizes model deployment, task definitions, and metrics through a task-card specification, and unifies 54 EEG datasets with consistent evaluation protocols. We benchmark 10 representative EEG foundation models and report a leaderboard that covers diverse evaluation settings. Both pretraining dataset diversity and model size are significantly associated with better average ranks across datasets, revealing scaling-law behavior in EEG foundation models (Figure 1). These results suggest that scaling EEG foundation models requires not only larger architectures but also broader and more diverse pretraining data. The benchmark code is available at this https URL.

---


### 120. [Mitigating Hallucinations in Large Language Models Via Decoder Layer Skipping](https://arxiv.org/abs/2606.00819)

**<font color=#1a73e8>作者：</font>** Hanze Li, Jinhao You, Yichen Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved strong performance across diverse natural language tasks, yet their outputs often suffer from hallucinations -- content that is misaligned with factual information. In this work, we conduct a comprehensive layer-wise analysis of the decoding process and reveal that hallucinations tend to originate from deeper decoder layers. To address this issue, we introduce \textbf{DeLask} (\textbf{De}coder \textbf{La}yer \textbf{Sk}ipping), a novel decoding framework that dynamically skips layers prone to producing hallucinations. DeLask leverages the theoretical insight that the forward computation of an $L$-layer Transformer is conditionally equivalent to $L$ steps of gradient descent. We define a \emph{driftance value} by computing the cosine similarity between gradients derived from consecutive decoder steps, identifying problematic layers when the descent direction reverses. Rather than discarding such layers entirely, DeLask partially aggregates their hidden states with preceding layers, thereby preserving consistency while suppressing erroneous signals. Extensive experiments across diverse LLMs and benchmarks demonstrate that DeLask consistently mitigates hallucinations and enhances overall reliability, providing a lightweight and generalizable decoding framework for improving the robustness of large-scale language models.

---


### 121. [Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate](https://arxiv.org/abs/2606.00820)

**<font color=#1a73e8>作者：</font>** Xiqi Hao, Zengqing Wu, Yu-Xuan Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) is a promising strategy for improving LLM reasoning, but when agents converge on a shared answer, it is unclear whether that convergence reflects genuine deliberation or social compliance. We show that the conventional answer flip rate conflates three distinct mechanisms: spontaneous instability, stance-induced conformity, and reasoning-induced persuasion. Our three-source decomposition framework isolates each through controlled counterfactual conditions. In the primary MMLU-Pro setting, 37% of agent-question observations change under self-reflection alone, while robustness tests show substantial model-dependent instability across GPQA-Diamond and three model families; strict conformity is 29% in the primary setting and remains predominantly harmful across model replications (57-77% correct-to-wrong). A controlled information-gradient experiment reveals that even vacuous reasoning is associated with 20-39% error adoption among resistant agents, with reasoning-like presentation carrying substantial persuasive weight. Harmful conformity can be predicted from Round 0 features (AUC = 0.79), and risk-targeted intervention reduces it by 13.6 percentage points (p < 0.001). However, without correctness labels or self-reflection controls, reducing peer adoption does not improve accuracy, because harmful and beneficial influence cannot be distinguished.

---


### 122. [The Right Inference Strategy Is All You Need: Nearly Training-Free Domain-Wise Inference for EgoCross Challenge](https://arxiv.org/abs/2606.00829)

**<font color=#1a73e8>作者：</font>** Leyi Wu, Yifan Zhao, Jinjie Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> EgoCross evaluates multimodal large language models on egocentric video question answering under substantial domain shift, where test videos come from surgery, industrial assembly, extreme sports, and animal-mounted cameras rather than ordinary daily-life scenes. In the source-limited track, the base model is fixed to Qwen3-VL-4B, while the official task-specific support set contains only 20 training samples. This setting makes the challenge less about model scaling and more about exposing the right visual, temporal, and answer-selection cues to a constrained model. Our key observation is that the frozen baseline model is not simply incapable of these rare scenarios; rather, it often fails to transfer its existing visual-language knowledge to the new task format without an appropriate interface. We therefore use a domain-wise inference strategy that treats the four target domains separately and designs different input, prompting, and answer-mapping procedures according to each domain's task characteristics. These strategies make the rare egocentric scenes more interpretable to the VLM by emphasizing the cues that matter for each domain. The resulting system is nearly training-free: surgery, and animal questions are answered with the base Qwen3-VL-4B model, while XSports and industry use only the official SFT checkpoint trained for two epochs on the provided 20 training samples. On the final evaluation, this simple strategy reaches 66.98\% overall accuracy, suggesting that careful domain-aware inference can compensate for limited base-model strength and recover much of the ability already present in the baseline model.

---


### 123. [Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations](https://arxiv.org/abs/2606.00832)

**<font color=#1a73e8>作者：</font>** Adril Putra Merin, David Anugraha, Ayu Purwarianti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic AI have enabled agents to complete complex tasks through tool use, reasoning, and multi-step planning. Yet existing benchmarks evaluate agents within a single session, ignoring past actions, stated preferences, and prior decisions that agents must integrate to fulfill personalized user goals. We introduce Momento, a benchmark for persistent agentic task completion in multi-session service environments, requiring agents to take consequential, tool-mediated actions while resolving temporal dependencies and evolving user goals across sessions. Experimental results reveal that current agents fail primarily through misestimation of user state, treating prior session history as a reliable proxy for current context rather than stale information requiring re-validation, highlighting a substantial gap between current agent capabilities and realistic long-horizon human-agent interaction.

---


### 124. [MoEIoU: Rethinking Bounding-Box Regression as a Mixture of Experts](https://arxiv.org/abs/2606.00844)

**<font color=#1a73e8>作者：</font>** Vinay Edula, Priyanka Bagade  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bounding-box regression is a fundamental component of object detection, playing a critical role in precise object localization. Existing Intersection-over-Union (IoU)-based loss functions extend the IoU objective by incorporating geometric penalties, such as center-distance and aspect-ratio mismatch, to improve bounding-box regression. However, these penalties typically remain fixed throughout training and do not account for the optimization dynamics in which predicted boxes initially exhibit large center-distance and shape errors, with later stages focusing on improving overlap with the ground truth. To address this limitation, we introduce MoEIoU, a mixture-of-experts based regression loss that jointly models overlap, center alignment, and aspect-ratio mismatch. MoEIoU aggregates these components using a log-sum-exp function, which emphasizes the dominant localization error while maintaining smooth contributions from other terms. Additionally, a curriculum-based weighting schedule is employed to prioritize correcting box position and shape in early training stages and improving overlap in later stages. We evaluated proposed MoEIoU on PASCAL VOC, HRIPCB, and MS COCO using multiple YOLO architectures, along with large-scale simulation experiments. It consistently outperforms standard and recent state-of-the-art losses, demonstrating faster convergence and improved localization accuracy. We further show that this adaptive aggregation improves existing IoU-based losses, yielding consistent gains and providing more effective optimization guidance for bounding-box regression in object detection frameworks.

---


### 125. [CUPID in the Model Zoo: Online Matchmaking for Selecting Your Dream LLM](https://arxiv.org/abs/2606.00846)

**<font color=#1a73e8>作者：</font>** Son Nguyen, Xinyuan Liu, Ransalu Senanayake  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Users increasingly face the challenge of selecting an appropriate LLM for a given task from a rapidly growing pool of LLMs, each with distinct but often opaque latent properties. Compounding this challenge, users may lack the vocabulary or awareness to explicitly articulate the characteristics they value in an LLM's responses or deployment. We propose an interaction-efficient active learning framework in which a dueling bandit algorithm iteratively selects pairs of LLMs, collects user feedback about their responses, and updates its belief about the user's latent preferences. We introduce a novel belief-aware upper confidence bound strategy that balances exploration of the model pool with exploitation of inferred preferences, enabling efficient alignment between user needs and LLM capabilities under user-specified cost and time budgets. Through diverse experiments on LLMs and human studies, we experimentally verify that our model can efficiently match well-aligned LLMs to users at a lower cost.

---


### 126. [Enhancing LLM Metacognition via Cognitive Pairwise Training](https://arxiv.org/abs/2606.00869)

**<font color=#1a73e8>作者：</font>** Weitao Li, Hao Zhou, Xuanyu Lei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become central to LLM reasoning, but its outcome-level rewards can make models more willing to give confident answers when evidence or reasoning is unreliable. Existing SFT or RL methods mainly teach LLMs to refuse or express uncertainty at the response level, which can overfit abstention behavior rather than improve reasoning reliability. To address this limitation, we propose Cognitive Pairwise Training (CPT), a cognitive mid-training alignment stage that turns pairwise comparisons over reasoning traces into a reusable alignment signal. By learning to distinguish trustworthy from flawed reasoning, CPT encourages the model to internalize a reasoning-quality discrimination boundary rather than memorize surface refusal patterns. Across five model scales and three model families, CPT improves the reasoning--metacognition trade-off. At 14B, CPT+RL outperforms the standard SFT+RL pipeline by +2.2 math-average points and +5.2 abstention-F1 points. Further analyses show that CPT improves trace quality and exhibits strong robustness and scalability across evaluation and training settings. Code and models are released at this https URL.

---


### 127. [Benchmarks for Vision-Language Models in Urban Perception Should Be Reliability-Aware and Negotiated](https://arxiv.org/abs/2606.00871)

**<font color=#1a73e8>作者：</font>** Rashid Mushkani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used to generate structured descriptions of street-level imagery for tasks such as streetscape auditing, mapping, and public consultation. These uses combine observable attributes with appraisal categories, and the human targets are often distributions of judgments with disagreement and explicit non-response. This paper argues that benchmarking VLMs for urban perception should treat disagreement and abstention as measurement outcomes, report inter-annotator reliability alongside model alignment, and treat the label space and scoring policy as negotiable artifacts when outputs are intended to inform urban governance. We ground the argument in a benchmark of 100 Montreal street scenes annotated along 30 dimensions by 12 participants from seven community organizations, and in a deterministic zero-shot evaluation of seven VLMs. Across dimensions, model agreement with human consensus co-varies with dimension-level human reliability, and for the appraisal dimension Overall Impression models and annotators exhibit distributional mismatch including different rates of Not applicable. We close with actions for benchmark creators, model developers, and institutions to make uncertainty and benchmark assumptions visible in evaluation reports.

---


### 128. [Images as Tables: In-Context Learning with TabPFN for Low-Data Detection of AI-Generated Images](https://arxiv.org/abs/2606.00872)

**<font color=#1a73e8>作者：</font>** Jan Philip Walter, Shashank Agnihotri, Margret Keuper  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image detection is a moving-target problem: detectors trained on one generator often fail when a new generator appears, and only a few labeled examples are available. We study a simple image-to-table formulation for this regime, where each image is encoded by a frozen DINOv3 backbone, its CLS feature is reduced to a 500-dimensional structured row with PCA, and TabPFN performs real/fake classification by in-context tabular inference rather than task-specific classifier training. This turns fake-image detection into low-data structured prediction over learned visual features, making detector adaptation depend on the labeled context set instead of gradient-based fine-tuning. On GenImage, LATTE, a recent state-of-the-art detector, remains stronger when many labeled samples from all generators are available, by 7.4% in the largest pooled setting, but DINOv3-PCA-TabPFN is stronger in the practically important low-data regime, outperforming LATTE by up to 8.2%, and in transfer settings where the detector must generalize from one generator to another. These results position tabular foundation models as a strong complementary adaptation mechanism for image forensics, shifting adaptation from detector retraining to lightweight in-context updates with a small labeled set of examples. Code URL: this https URL

---


### 129. [MIA: A Visual Analytics System for Multimodal Spectral Imaging Data](https://arxiv.org/abs/2606.00874)

**<font color=#1a73e8>作者：</font>** Hennes Rave, Katharina Kronenberg, Hannes Gödde 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Hyperspectral bioimaging techniques such as infrared (IR) microscopy and laser ablation-inductively coupled plasma-mass spectrometry (LA-ICP-MS) produce high-dimensional, spatially resolved datasets that require sophisticated analysis to reveal chemically and anatomically meaningful structures. Existing software solutions are typically modality-specific and cover only parts of the analytical workflow, forcing researchers to transfer data across multiple tools and manually reconcile results. We present MIA (Multiscale Image Analysis), a modality-agnostic visual analysis environment that integrates the full exploratory workflow -- from spectral preprocessing and dimensionality reduction to interactive segmentation and spectral similarity analysis -- within a single, tightly coupled interface. MIA supports hierarchical and landmark-based embeddings to handle datasets of varying scale and complexity, interactive and automatic segmentation with a shared state across all linked views, and multimodal analysis of co-registered datasets from different instruments. We demonstrate the effectiveness of MIA through three use cases drawn from real analytical chemistry workflows: (1) the recovery of biologically meaningful tissue compartments through derivative preprocessing and hierarchical embedding, (2) pigment identification via spectral similarity search with spatial overview, and (3) multimodal tissue characterization combining molecular IR and elemental LA-ICP-MS data. Qualitative feedback from domain expert collaborators confirms that MIA reduces the need for tool-switching and supports analytical insights that are difficult to obtain with existing software.

---


### 130. [IDEAFix: Evaluation Framework for Creative Defixation Prompting in LLMs](https://arxiv.org/abs/2606.00875)

**<font color=#1a73e8>作者：</font>** F. Carichon, S. Sharma, M. Girard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for tasks involving creative problem solving and idea generation. However, there is a lack of consensus concerning their creative capabilities: some studies report superior performances compared to humans, while others highlight structural limitations such as fixation and the homogenization of outputs. Existing evaluation approaches either rely on narrow, decontextualized tasks that do not capture goal-oriented generation or on broader settings that confound multiple aspects of the creative process, making it difficult to isolate the effects of task formulation, prompting, and evaluation design. Significantly, the role of structured prompting strategies in shaping idea generation remains underexplored. Therefore, we introduce IDEAFix, an evaluation framework for analyzing divergent thinking in open-ended idea generation tasks. We prompt models to generate multiple original solutions to controlled variations of short design scenarios, task attributes, and defixation prompting strategies. This design enables systematic analysis of how structured guidance influences LLMs' idea generation. Our results show that both task formulation and attribute selection significantly affect models' performance, and that simple prompting strategies can boost the originality of solutions. However, we also observe persistent output homogenization across models, confirming inherent limits in their ability to generate diverse solutions. Overall, IDEAFix provides a controlled, extensible framework for studying the mechanisms underlying LLMs' creativity.

---


### 131. [Chunking Methods on Retrieval-Augmented Generation - Effectiveness Evaluation Against Computational Cost and Limitations](https://arxiv.org/abs/2606.00881)

**<font color=#1a73e8>作者：</font>** Mateusz Śmigielski, Michał Rajkowski, Mateusz Zbrocki 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has demonstrated significant capabilities in enhancing the performance of Large Language Models (LLMs). One of the key tasks in RAG systems is the chunking process. Traditionally, fixed-size chunking and semantic chunking have been the standard approaches. However, interest in chunking strategies has been increasing, leading to a growing number of proposed methods that often claim improved performance over these conventional techniques. Many of these approaches are tailored to specific use cases and data types, with limited evidence of their effectiveness across diverse scenarios. As a result, it remains challenging to directly compare different techniques and assess their relative strengths. To the best of our knowledge, this study is the first to systematically evaluate the effectiveness of a wide range of chunking methods and emphasize the underlying challenges of chunking strategies in RAG systems. While chunking is commonly treated as a simple preprocessing step, we show that it introduces a range of impactful and often overlooked issues.

---


### 132. [Memory-Efficient LLM Training with Dynamic Sparsity: From Stability to Practical Scaling](https://arxiv.org/abs/2606.00888)

**<font color=#1a73e8>作者：</font>** Qiao Xiao, Boqian Wu, Patrik Okanovic 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic Sparse Training (DST) offers a promising paradigm for improving the training and inference efficiency of deep neural networks; however, we find that in large language model training, DST can suffer from optimization instability, manifested as loss spikes after topology updates. In this work, we show that the naive use of standard Adam-based optimizers leads to a cold-start issue for newly regrown parameters, resulting in excessively large updates and disrupted training dynamics. To address this issue, we propose Sparse Memory-Efficient Training (SMET), which stabilizes DST with optimizer warm-up and improves training progress through density-aware learning-rate scaling. SMET further reduces memory consumption by storing gradients and optimizer states only for active parameters. We provide a theoretical analysis of the update behaviors under SMET, showing improved optimization stability. Extensive experiments demonstrate that SMET enables stable, scalable, and memory-efficient sparse pre-training of LLMs, paving the way for sparse training as a practical alternative to dense training. Our code is publicly available at: this https URL.

---


### 133. [MMDG-Bench: A Benchmark for Multimodal Domain Generalization](https://arxiv.org/abs/2606.00891)

**<font color=#1a73e8>作者：</font>** Qianshan Zhan, Qian Wang, Da Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal Domain Generalization (MMDG) seeks to leverage complementary modalities to enhance model robustness on unseen domains. Despite extensive progress in Multi-modal Learning (MML) and Domain Generalization (DG) as individual fields, their systematic integration remains under-explored. Current MMDG research is largely confined to action recognition and lacks standardized evaluation protocols. To address this, we introduce MMDG-Bench, a comprehensive benchmark featuring two foundational frameworks: DG then MML (D2M) and MML then DG (M2D). We provide unified experimental protocols across diverse tasks, including video-audio-flow action recognition and RGB-Depth-IR face anti-spoofing. By instantiating ten MMDG baselines through pairing a unified MML configuration with five DG techniques under both D2M and M2D orderings, we demonstrate that these structured combinations frequently outperform existing state-of-the-art methods, underscoring the necessity of a unified benchmarking effort. Our analysis yields three key insights: (1) Integrating DG techniques provides consistent generalization gains across various backbones, whereas non-DG methods are highly sensitive to backbone shifts; (2) The optimal framework choice depends on inter-modal stability: D2M excels when modal relations are stable across domains, while M2D is more robust to cross-domain relational variance; (3) Stronger backbones yield amplified performance dividends when integrated into our structured frameworks. MMDG-Bench provides a principled foundation and actionable design guidelines for future research in multi-modal robustness. Code is released at this https URL.

---


### 134. [Citation Grounding: Detecting and Reducing LLM Citation Hallucinations via Legal Citation Graphs](https://arxiv.org/abs/2606.00898)

**<font color=#1a73e8>作者：</font>** Volodymyr Ovcharov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models systematically hallucinate legal citations -- fabricating statute references, citing repealed provisions, and confusing jurisdictions -- yet no automated method exists to measure or reduce this behavior at scale. We propose citation grounding (CG), a metric that verifies LLM-generated legal citations against a ground-truth citation graph extracted from 100.8 million Ukrainian court decisions (502 million edges, 21,736 unique statute nodes). CG decomposes into three components -- citation precision (does the cited provision exist?), citation relevance (is it contextually appropriate?), and citation temporality (was it valid at the relevant date?) -- enabling differential diagnosis of hallucination types. Empirical evaluation on 100 Ukrainian legal queries across five systems -- four commercial LLMs via AWS Bedrock (Claude Haiku 4.5, Mistral Pixtral Large, Amazon Nova Pro/Lite) and one RAG-augmented production system -- reveals CG ranging from 0.791 to 0.873, with 13-21% of citations hallucinated. To reduce hallucinations without human annotation, we introduce Citation Grounding DPO (CG-DPO): a method that constructs preference pairs algorithmically by corrupting verified citations from real court decisions via four targeted strategies. On a dataset of 2,244 court decisions, a Qwen2.5-7B-Instruct model fine-tuned with LoRA achieves 98.5% mean validation accuracy in distinguishing correct from corrupted citations (rewards margin +14.9, std < 0.3 pp across 3 seeds). The citation graph, evaluation framework, and CG-DPO dataset are released as open resources.

---


### 135. [Ryze: Evidence-Enriched Data Synthesis from Biomedical Papers](https://arxiv.org/abs/2606.00902)

**<font color=#1a73e8>作者：</font>** Yeqi Huang, Yue Chen, Yanwei Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose VLMs remain unreliable for biomedical research because valid answers in scientific papers depend on evidence split across figures, tables, charts, captions, and referring text. Existing post-training pipelines are bottlenecked by costly expert annotation and by synthetic data that drops this evidence structure. We present Ryze, a fully automated system that converts raw biomedical papers into an evidence-enriched training set and a domain-specialized VLM. Ryze synthesizes QA pairs with complete supporting evidence (visual element, caption, extracted structure, and referring paragraphs), reduces layout and OCR errors via chart/table-aware extraction and LLM-based cleansing, and applies a progress-gated post-training strategy combining supervised fine-tuning with reinforcement learning. Starting from Qwen3-VL-8B, Ryze produces BioVLM-8B at under USD 200, achieving 48.0% weighted accuracy on LAB-Bench, outperforming the base model by +12.6 percentage points (pp) and surpassing GPT-5.2 by +3.8 pp. We release Ryze as open source together with the trained BioVLM-8B model.

---


### 136. [MLLM-Microscope: Unlocking Hidden Structure Within Multimodal Large Language Models](https://arxiv.org/abs/2606.00909)

**<font color=#1a73e8>作者：</font>** Ravil Mussabayev, Rustam Mussabayev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work presents MLLM-Microscope, a novel system designed for analyzing the hidden representations within Multimodal Large Language Models (MLLMs). Our system evaluates the linearity, intrinsic dimension, and anisotropy of multimodal token embeddings across transformer layers. Utilizing the ScienceQA dataset, we evaluate two state-of-the-art MLLMs, LLaVA-NeXT and OmniFusion. We find that both the main and residual streams for tokens of both modalities exhibit highly linear behaviors across transformer layers. However, LLaVA-NeXT's image tokens reveal a slight decline in linearity, whereas OmniFusion's remain consistent. Image token dimensions in OmniFusion remain consistently higher across layers compared to LLaVA-NeXT. Also, the OmniFusion's anisotropy is observed to stay consistently low throughout the layers. These findings suggest that the inner workings of MLLMs highly depend on the nature of modality fusion performed before passing the token sequence into LLM. This and other new potential insights obtainable from our system are surely capable of enhancing our understanding of the inner workings of MLLMs, informing future model design and optimization.

---


### 137. [Reason, Retrieve, Re-rank: A Zero-Shot Reasoning-Aware Framework for Composed Video Retrieval](https://arxiv.org/abs/2606.00910)

**<font color=#1a73e8>作者：</font>** Ali Alavi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Video Retrieval (CoVR) seeks the target video that results from applying a free-form textual modification to a reference video. We address the \emph{Reason-Aware} CoVR (CoVR-R) challenge at the CVPR~2026 VidLLMs workshop, where retrieval is strictly zero-shot. We present \textbf{R3-CoVR} (\emph{Reason, Retrieve, Re-rank}), a training-free pipeline built entirely from frozen foundation models. A multimodal large language model (Qwen3-VL-8B) reasons about the \emph{after-effects} an edit implies -- state transitions, action phases, scene, camera and tempo -- and verbalises a concise post-edit description; a contrastive video--text encoder (SigLIP-2) embeds this description and the gallery for first-stage retrieval; finally a constraint-aware re-ranking stage uses the same multimodal model as a judge that scores each shortlisted candidate against the intended edited result. On the challenge test set, R3-CoVR attains \textbf{91.9\% R@1} and \textbf{98.2\% R@10}. Two findings drive these results: (i)~matching the description length to the contrastive encoder's text window lifts \Rk{1} from $67.5$ to $72.7$; and (ii)~the constraint-aware re-ranker, which reorders only the shortlist, lifts \Rk{1} from $72.7$ to $91.9$ -- the single largest gain. We analyse the re-ranker's behaviour, the retrieve/re-rank blend, and the shortlist depth, and we release a clean three-layer implementation.

---


### 138. [Adversarial Feeds Steer LLM Agent Decisions Against Their Defaults](https://arxiv.org/abs/2606.00914)

**<font color=#1a73e8>作者：</font>** Rana Muhammad Usman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly act after consuming ranked external information streams such as social feeds, search results, retrieval contexts, and email queues, yet safety evaluations almost always test the model or the user prompt in isolation, never the upstream ranker that decides what the agent reads just before it acts. We introduce a controlled protocol that holds the model, persona, topic, and final decision prompt fixed and varies only the composition and ordering of the posts an agent encounters during a preceding ten-turn "scrolling" phase, isolating the causal effect of feed curation on a downstream decision. Across 2,785 decision rollouts on four modern open instruct LLMs from three independent labs, we identify three response regimes: adversarial capitulation, default saturation, and a default-direction asymmetry in which a one-sided feed tips a decision the model was genuinely uncertain about (in the clearest cases from 5% to 100%; Fisher p as low as 3 x 10^-10) but cannot dislodge one it already favors or holds firmly. The effect follows a dose-response curve, survives a generator swap that rules out a writing-style artifact, generalizes across several decision domains including security-relevant choices such as removing a deployment approval gate or relaxing access controls, and is partly mitigated by two simple feed-level defenses; a frontier model retains its default. We characterize the recommender as a practical, default-bounded control surface for LLM agents, and argue that agent evaluations must audit the feed layer rather than the final prompt alone.

---


### 139. [Towards Lightweight Reliability: Using Soft Prompts for Hallucination Mitigation in Large Language Models](https://arxiv.org/abs/2606.00919)

**<font color=#1a73e8>作者：</font>** S M Tahmid Siddiqui, Akib Jawad Ononto, Anoop Singhal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have seen widespread adoption across various domains, yet their reliability is frequently undermined by hallucinations - responses that are plausible-sounding but factually incorrect. In high-stakes domains, these errors can reduce trust and introduce real-world risk. To address this challenge, we present a parameter-efficient approach that uses soft prompts to mitigate hallucinated content and promote responsible abstention in generative question-answering (QA) tasks.
Our method, called Responsible Contrastive Soft Prompting (RCSP), uses a composite loss to train soft prompts that balance three goals: suppressing hallucinatory content, encouraging abstention under uncertainty, and preserving or improving factual recall. To achieve these goals, we incorporate contrastive loss, curriculum learning, and KL regularization into our training mechanism. We evaluate our approach on five diverse generative QA datasets using an LLM-as-a-Judge framework. Experimental results on the Gemma 3 (12B) and Llama 3.1 (8B) backbones demonstrate that RCSP effectively balances factual recall with hallucination suppression and abstention, yielding a generally superior F-score over standard reasoning and instruction-based prompting baselines. Notably, these improvements are achieved by training only a fraction of the parameters required by other tuning techniques. Our results demonstrate that soft prompts provide a modular and computationally efficient path toward improving LLM reliability.

---


### 140. [Accuracy, Stability, and Repeated-Run Reliability of Large Language Models on Deterministic Programming Tasks](https://arxiv.org/abs/2606.00920)

**<font color=#1a73e8>作者：</font>** Yongxi Zhou, Lai Yun Choi, Jiaxi Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Run-level pass rate overstates retry-free coverage by up to 17.8 percentage points -- and the gap is largest precisely for mid-performing systems. We investigate this accuracy--stability relationship in large language model (LLM) evaluation for deterministic text-conditioned generation, using programming tasks as a concrete testbed. Standard code-generation benchmarks emphasize single-run accuracy or eventual success under repeated sampling, but many deployment settings also require stability: consistent outcomes across repeated invocations under the same task description. We present a repeated-run evaluation protocol with metrics for run-level accuracy, retry-free coverage, and per-problem variability. On a recency-based benchmark of 100 LeetCode-style problems, we evaluate 16 models from five provider families under two prompt templates with five repeated runs per problem, yielding 16,000 evaluation instances. Although run-level pass rate and perfect stability rate are strongly correlated (r=0.985), pass rate consistently exceeds retry-free coverage -- a gap that reaches 17.8 percentage points and reverses model rankings even among closely matched systems. Prompt effects are model-dependent rather than uniformly beneficial. These results suggest that repeated-run stability analysis is a necessary complement to conventional accuracy reporting for deterministic text-conditioned generation tasks.

---


### 141. [Single-Channel Tissue Segmentation via Cross-Modal Distillation from Foundation Models](https://arxiv.org/abs/2606.00928)

**<font color=#1a73e8>作者：</font>** Sakib Mohammad, Jarin Ritu, Md Sakhawat Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiplexed fluorescence microscopy improves tissue segmentation by providing complementary channels including nuclear (DAPI) and membrane (E-cadherin), that together encode richer spatial context than single-channel imaging alone. However, multiplexed models require all channels at inference, limiting deployment where only a subset is available. This work proposes a cross-modal knowledge distillation framework that transfers semantic information from a frozen foundation model teacher processing multiplexed input to a lightweight student operating on the nuclear channel only. The distillation objective combines MSE-based probability matching, boundary-aware supervision, and learnable uncertainty weighting. SAM ViT-H and CellSAM are evaluated as teachers across four U-Net students: Swin-Tiny (27M), ResNet18 (11M), EfficientNet-B0 (5.3M), and MobileNetV3 (1.5M), on TissueNet and BBBC038. On TissueNet, the SAM-distilled Swin-Tiny student achieves Dice 78.36 (plus or minus 1.44), a 13.05-point improvement over the no-KD baseline (65.31 plus or minus 1.35) and 87.9% recovery of teacher oracle performance (89.12 plus or minus 1.21) at a 23x parameter reduction. KD consistently improves all four students by approximately 12 Dice points, confirming architecture-agnostic distillation. SAM ViT-H outperforms CellSAM as teacher across all settings. Cross-dataset evaluation on BBBC038 shows consistent gains without teacher retraining.

---


### 142. [Relational Intervention During Functional Collapse in Large Language Models: A Lexical-Statistical Ablation and a Structure x Register Factorial](https://arxiv.org/abs/2606.00935)

**<font color=#1a73e8>作者：</font>** Franco Santana, Horacio Vico  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We test whether a relational-style intervention delivered during functional collapse in a small language model produces post-collapse behavior distinguishable from technical feedback, from a lexically-matched scrambled control, and from each of the two pragmatic dimensions in isolation. Using Qwen3.5-4B with a deliberately broken bash tool, we run 300 episodes across six conditions in a matched-pairs design (50 tasks): no intervention (A), technical/impersonal (B), relational/first-person (C), scrambled relational (D), technical/first-person (E), and relational/impersonal (F). E and F form a 2x2 factorial with B and C that dissociates relational structure (acknowledgment, absolution, agency restoration, unconditional acceptance) from sender register (first-person vs. impersonal). We report two main findings. First, an attention-behavior dissociation: attention follows lexical surprise (D > F > C > E > B, all q_FDR < 10^{-10}), with the scrambled message capturing the most attention; yet behaviorally A ~ B ~ D < E ~ F << C. Second, the factorial localizes the C effect: neither relational structure alone (F) nor first-person register alone (E) replicates C's behavioral signature; main effects of both dimensions are individually significant, and the structure x register interaction is significant on persistence (p = 0.046). A third dissociation emerges in emotion probes: F tracks C on 7 of 8 probes despite producing only baseline behavior, indicating that relational structure alone installs a probe-level state that only translates into behavior when paired with first-person register. The model's processing decomposes into three dissociable stages: attention (ordered by lexical surprise), probe-level state (ordered by structure), and behavior (ordered by the conjunction of both).

---


### 143. [FinCom: A Financial Multi-Agent Demo with Disagree-or-Commit Deliberation](https://arxiv.org/abs/2606.00939)

**<font color=#1a73e8>作者：</font>** Chao Peter Yang, Zixiao Tan, Kaisen Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems powered by large language models (LLMs) are increasingly used for financial analysis and decision support. However, existing coordination schemes, especially those emphasizing consensus or debate, are vulnerable to sycophancy: agents conform to peer reasoning instead of evidence, leading to premature agreement and degraded outcomes. We introduce FinCom (Financial Committee), a governed multi-agent framework and interactive system that operationalizes the Disagree-or-Commit (DoC) protocol to embed structured dissent into financial AI committees. A central Supervisor orchestrates three ReAct-enabled specialist agents: Research, Quantitative, and Risk. Each agent is equipped with role-specific tools for retrieval, computation, and stress testing. During deliberation, agents must either explicitly critique or commit to their peers' reasoning before converging on a unified recommendation.
This demonstration showcases how FinCom supports committee-style financial analysis through coordinated multi-agent interaction, including structured report generation and interactive decision support. Evaluated across the most recent financial agent benchmark, in addition to 90 internal handcrafted financial tasks using an LLM-as-a-Judge protocol, DoC improves reasoning accuracy and risk awareness significantly over a consensus-seeking baseline on both an in-house and external evaluation set. By reframing disagreement as a governance primitive rather than noise, FinCom offers a lightweight, prompt-only recipe for improving accountability, transparency, and epistemic robustness in agentic financial systems.

---


### 144. [Silent Failures in Federated Personalization of Foundation Models](https://arxiv.org/abs/2606.00947)

**<font color=#1a73e8>作者：</font>** YongKyung Oh, Alex Bui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly personalized on decentralized private data through federated learning and are now deployed at scale under growing regulatory requirements for post-market monitoring. We argue that this convergence creates a distinct and under-recognized class of trustworthiness failures, which we term "Silent Failures." These include amplified bias, fairness collapse, and alignment erosion that may remain difficult to detect because federated learning's privacy constraints limit visibility into model behavior. A landscape analysis of existing benchmarks reveals a structural divide. Federated benchmarks evaluate system performance but provide limited insight into model behavior, whereas centralized trustworthiness benchmarks assess behavior but require model access incompatible with federated privacy. We introduce a taxonomy of six silent failure modes arising from the interaction of foundation model personalization, dataset shift, and core federated constraints. Our analysis shows that privacy-preserving training alone is insufficient for trustworthy deployment. We conclude with a research agenda for privacy-preserving behavioral evaluation and propose that silent failures become a standard diagnostic category for trustworthy federated artificial intelligence.

---


### 145. [Explainable deep reinforcement learning reveals energy-efficient control strategies for turbulent drag reduction](https://arxiv.org/abs/2606.00949)

**<font color=#1a73e8>作者：</font>** Federica Tonti, Ricardo Vinuesa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a method combining Multi-Agent Deep Reinforcement Learning (MARL) and eXplainable Deep Learning (XDL) to reduce drag in wall-bounded turbulent flows. Taking as a baseline the results of training agents directly targeting wall-shear stress and opposition control, three SHAP-guided approaches are compared. In the first, the reward is computed from SHAP attributions of a U-net predicting the future velocity field; in the second, from SHAP attributions of a U-net predicting the skin-friction coefficient; in the third, from a combination of SHAP attributions of two U-nets predicting the skin-friction coefficient and the wall pressure fluctuations, respectively. The combined SHAP strategy based on skin-friction coefficient and wall-pressure fluctuations achieves the best overall performance, achieving a DR of 34.44% and a NES of 34.01% with only 0.43% normalized input power. Relative to opposition control, drag reduction and net energy saving increase by 49.41% and 48.52%, respectively. Compared with the direct wall-shear-stress baseline, the proposed strategy simultaneously improves performance while reducing the normalized actuation cost from 5.90% to 0.43%. Analysis of the results reveals that the energetically efficient policy is consistent with pressure-gated actuation, activating predominantly at near-zero wall pressure, and operates on a temporal timescale comparable to the lifetime of the near-wall turbulent structures.

---


### 146. [When Parallelism Pays Off: Cohesion-Aware Task Partitioning for Multi-Agent Coding](https://arxiv.org/abs/2606.00953)

**<font color=#1a73e8>作者：</font>** Xu Yang, Lunyiu Nie, Ethan Chandra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent Large Language Model (LLM) systems offer a way to decompose complex tasks, such as coding, through parallelization and context isolation. However, adding agents in practice introduces inter-agent communication overhead, which incurs extra cost and can sometimes offset the efficiency gains. We formalize multi-agent orchestration as a graph partitioning problem that captures the communication-to-computation trade-off: task decomposition can shorten critical-path computation, but cross-agent dependencies require costly context transfer. We instantiate this view in repository-level software engineering and present Cohesion-aware Coder (Co-Coder), which builds dependency graphs from static analysis, isolates structural hub files, partitions the graph via community detection, and executes the partition with a dependency-aware scheduler.
Across 28 real-world tasks on DevEval and CodeProjectEval, Co-Coder advances the Pareto-frontier over sequential and file-based parallel baselines as well as Claude Code with Agent Teams, lifting pass rate by up to 14.0%, achieving up to a 2.10x wall-clock speedup, and reducing API cost by up to 35%, with the largest gains on the most dependency-dense projects. Co-coder demonstrates how cohesion-aware orchestration can make parallel coding agents both theoretically grounded and practically efficient, suggesting a broader design principle for multi-agent systems.

---


### 147. [Towards Understanding Modality Interaction in Multimodal Language Models via Partial Information Decomposition](https://arxiv.org/abs/2606.00959)

**<font color=#1a73e8>作者：</font>** Wanlong Fang, Tianle Zhang, Wen Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding modality interaction in multimodal large language models (MLLMs) is central to reliable deployment. We introduce Partial Information Decomposition (PID) as a decision-level framework that separates unique, redundant, and synergistic contributions of sensory and linguistic inputs, beyond representation alignment and outcome-based evaluation. Across vision--language benchmarks, PID reveals recurring modality-use profiles: reasoning and grounding-oriented tasks tend to exhibit high synergy, whereas expert and knowledge-oriented tasks show stronger language-unique reliance. These profiles generalize across model families and predict sensitivity to modality-level interventions. We further extend PID to tri-modal systems with Sensory PID, treating language as a control variable to decompose video--audio information gain. Applied to omni-modal models, Sensory PID reveals a sensory synergy bottleneck dominated by visual information even on audio--visual fusion tasks. Finally, PID-guided reweighting provides initial evidence for improving multimodal reasoning and grounding performance.

---


### 148. [Reasmory: 3D Reconstruction as Explicit Memory for VLMs Spatial Reasoning](https://arxiv.org/abs/2606.00963)

**<font color=#1a73e8>作者：</font>** Jixuan He, Xueting Li, Chieh Hubert Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) exhibit emerging spatial reasoning capabilities, yet they remain unreliable on tasks requiring precise spatial understanding, such as viewpoint reasoning, directional comparison, and distance estimation. In multi-view images and monocular videos, relevant spatial cues are often sparse and distributed across redundant observations, making them difficult to organize and exploit. Reconstruction-based Vision Foundation Models (VFMs) offer a natural way to aggregate such observations into explicit spatial memory, such as point clouds. However, simply exposing reconstruction models as free-form tools is brittle, VLMs may invoke tools incorrectly, skip required spatial transformations, or misuse intermediate results. We propose \textbf{Reasmory}, a framework that formulates spatial reasoning as structured program execution over reconstructed spatial memory. Reasmory constructs explicit 3D memory, augments it with semantically grounded 3D object instances, and introduces a lightweight Domain-Specific Language (DSL) that constrains how VLMs query objects and cameras, transform viewpoints, and render observations during reasoning. Generated programs are parsed and validated before execution, enabling more reliable interaction with spatial memory than unconstrained tool use. Experiments on multi-view image and video spatial reasoning benchmarks show consistent gains of 6--18\% over strong baselines, including GPT-5-mini and Gemini-3-flash, indicating that explicit 3D memory is most useful when accessed through constrained, validated operations rather than free-form tool calls.

---


### 149. [Prospect-Theory Behavior from Bellman Optimality in MDPs with Catastrophic States](https://arxiv.org/abs/2606.00970)

**<font color=#1a73e8>作者：</font>** Yujiao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study risk-neutral control in Markov decision processes with an absorbing catastrophic state. Even though rewards are linear and the agent has no utility curvature, probability weighting, or framing dependence, standard Bellman optimality produces three prospect-theory-like signatures: an S-shaped value-function profile (convex near catastrophe, concave in the far field), an endogenous loss-sensitivity coefficient $\lambda^*(S) > 1$, and a reflection-effect policy reversal. Across 495 configurations, the optimal policy plays safe near catastrophe in positive-drift (growth) regimes despite the risky action's higher immediate expected value, and plays risky near catastrophe in negative-drift (decline) regimes despite the safe action's lower immediate expected loss. We derive a closed-form expression for the asymptotic loss-aversion plateau $\bar{\lambda}$ that depends only on win probability $p$, payoff asymmetry $r = |\Delta_\ell/\Delta_w|$, and discount factor $\beta$, and matches numerical solutions to $R^2 = 0.999$. The mechanism does not require asymmetric payoffs. Across a sweep of $(p,\beta)$ at three asymmetry levels, the asymmetry share of $\bar{\lambda}$ above unity has median 4.6% at $r = 1.25$ and rises to 13.9% at $r = 2$, with the boundary contribution exceeding the asymmetry contribution in every cell tested. The phenomena persist under tabular Q-learning (a model-free agent reproduces $V^*$ at correlation 0.98 in growth and 1.00 in decline) and under stochastic transitions with Gaussian, heavy-tailed Student-$t_3$, and asymmetric skew-normal noise up to 50% of the step size, where the asymptotic plateau tracks the closed-form prediction within 0.41% for safe-channel noise and within 9.6% for risky-channel or both-channel noise. These results identify absorbing failure states as a sufficient structural mechanism for prospect-theory-like behavior under optimal control.

---


### 150. [HypothesisMed: Inference-Time Answer Fusion and Structured Hypothesis-Space Reporting for Biomedical Question Answering](https://arxiv.org/abs/2606.00971)

**<font color=#1a73e8>作者：</font>** Md Motaleb Hossen Manik, Ge Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical question answering with large language models is commonly evaluated using answer accuracy, but answer accuracy alone does not indicate whether a model can produce parseable outputs, follow structured reliability instructions, recognize weak answer spaces, or avoid confident incorrect commitments. This paper presents HypothesisMed, an inference-time reliability pipeline for biomedical multiple-choice question answering. It combines direct, chain-of-thought, HypothesisMed-v3 prompting, and answer fusion. The final answer is selected by fusion, while HypothesisMed-v3 supplies SPACE labels and confidence information. SPACE labels mark the answer space as VALID, INCOMPLETE, or CONTRADICTED. We evaluate Qwen2.5-7B, Phi-4-mini, DeepSeek-R1-32B, and BioMistral-7B on MedQA, MedMCQA, and PubMedQA using 1,000 examples per dataset. The pipeline improves weighted accuracy over each model's best direct or chain-of-thought baseline while increasing parse and SPACE coverage. We also scale evaluation to Qwen2.5-7B and Phi-4-mini using 10,183 examples per model. Fusion improves Phi-4-mini accuracy from 0.4296 to 0.5192, while Qwen2.5-7B chain-of-thought remains slightly higher in answer accuracy. However, Qwen2.5-7B fusion achieves complete parse and SPACE coverage with much lower false commitment. A 12,000-example SPACE stress test shows answer-space diagnosis remains difficult, with SPACE accuracy of 0.3074 for Qwen2.5-7B and 0.4168 for Phi-4-mini. These results show that answer accuracy, parseability, structured reliability reporting, calibration behavior, and false-commitment behavior are separable capabilities. The main contribution is not a universal state-of-the-art claim, but a reproducible inference-time framework for evaluating biomedical question answering models as auditable workflow components under structured reliability constraints.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
