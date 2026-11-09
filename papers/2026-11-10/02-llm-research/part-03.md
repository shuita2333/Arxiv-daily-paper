# 🧠 大模型相关研究 | 2026年11月10日

> 本类共 **174** 篇论文：已确认 **163** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-174](./part-04.md)

---

### 101. [SafeOrchestrate: Runtime Checked Intent-Driven Orchestration for Cyber-Physical Systems](https://arxiv.org/abs/2611.09364)

**<font color=#1a73e8>作者：</font>** Muhammad Ashfaq, Ahmed R. Sadik, Ewan Warburton 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern cyber physical systems (CPS) integrate heterogeneous sensors, actuators, controllers, and services, composed at runtime rather than at design time. Orchestrating such systems through natural language (NL) is attractive, but unconstrained large language model (LLM) tool use is risky because actions must respect device capabilities, runtime state, and safety constraints. We present Safe Orchestrate, a reference architecture for runtime checked, intent driven CPS orchestration. Given an NL intent, it derives atomic goals, generates a runtime checkable specification for each, grounds the specifications to device affordances, and verifies every candidate action against runtime state and safety constraints before execution. In a Web of Things (WoT) instantiation, the architecture produces Linear Temporal Logic (LTL) style specifications from the NL intent, grounds them to Thing Description (TD) affordances exposed through the Model Context Protocol (MCP), and checks candidate actions against satisfiability modulo theories (SMT) backed guardrails. We evaluate this instantiation on simulated smart home, greenhouse, and industrial automation tasks against a direct LLM to MCP baseline. Safe Orchestrate maintains 100% required action accuracy on every task and 100% MCP Execution Similarity (MCP ES) on all but one, where MCP ES is 92%. By contrast, the baseline degrades on multi device, event triggered, and ordered tasks, with MCP ES falling to 13%. These results suggest that combining LLM based specification generation with role aware grounding and runtime constraint checking improves reliability for open CPS orchestration without enriched TD annotations or planning domain expertise.

---


### 102. [Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data](https://arxiv.org/abs/2611.09372)

**<font color=#1a73e8>作者：</font>** Carlos Martín-Abellán, Mark Kröll  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Energy management officers and grid operators increasingly rely on smart meter data for anomaly detection, performance monitoring, and strategic decision-making. However, extracting actionable insights from large-scale, heterogeneous telemetry databases requires advanced SQL and data engineering expertise, creating a critical bottleneck for non-technical personnel. Furthermore, the strict data privacy regulations and security constraints inherent to critical energy infrastructure often prohibit the routing of sensitive consumer data through cloud-based Large Language Models (LLMs). To address these challenges, we present OpenMeter, a schema-agnostic Multi-Agent System (MAS) designed to translate natural language queries into executable code and human-readable insights. This architecture lowers the technical barrier for day-to-day utility operations by empowering non-expert personnel to interact with complex databases through intuitive natural language dialogue, transforming raw telemetry into a highly valuable tool for routine grid workflows and strategic decisions. Multi-scenario ablation studies over this environment demonstrate that full multi-agent orchestration shows its largest observed accuracy gains on resource-constrained local hardware (+6.1 pp EX-R over the strongest single-agent configuration); at frontier scale, individual components retain value but should be enabled selectively, indicating that the cost of full orchestration is justified specifically where privacy demands local execution.

---


### 103. [SPSC: Zero-Shot Cross-Subject EEG-to-Image Reconstruction via Semantic Preservation and Subspace Calibration](https://arxiv.org/abs/2611.09380)

**<font color=#1a73e8>作者：</font>** Yutang Lu, Shuai Jiang, Fei Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision-language models and diffusion generators have driven rapid progress in brain-to-image generation, while EEG-based reconstruction is still constrained by low signal-to-noise ratio and cross-subject semantic shifts. Zero-shot cross-subject reconstruction poses even greater challenges: EEG semantic embeddings learned from source subjects deviate from the manifold of image embeddings of the unseen target subject, particularly when neither target labels nor target image embeddings are available. To address this issue, we introduce the Semantic Preservation and Subspace Calibration (SPSC) framework, which first uses Object Mask Contrastive Regularization (OMCR) with object identity for backend training, and then constructs Subspace Candidate Gate (SCG) to achieve label-free semantic correction for target subjects during inference. Specifically, OMCR regularizes the conditioning space with object-level positive samples to preserve object-level feature neighborhoods within the reconstruction prior and low-level branch, while SCG exploits training image prototypes and batch statistics of unlabeled target EEG to select candidates for each task within subspaces of image prototypes. Under the leave-one-subject-out (LOSO) setting across ten subjects on the THINGS-EEG dataset, SPSC improves the cross-subject reconstruction from 0.552 to 0.713 on CLIP and from 0.612 to 0.745 on Alex.5. These significant gains indicate that the semantically calibrated conditions can better support generation for the target subjects under label-free inference.

---


### 104. [Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations](https://arxiv.org/abs/2611.09382)

**<font color=#1a73e8>作者：</font>** Junru Hu, Cheng Tang, Wei Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weight-Space Programming (WSP) enables reasoning agents to directly inspect and modify neural network parameters, offering an alternative to gradient-based model adaptation. However, its capabilities, cross-task generalization, and practical limitations remain insufficiently understood. We systematically investigate WSP through 16 editing trajectories across seven benchmarks and two model scales (Qwen3.5-0.8B and Qwen3.5-9B). Our findings reveal three key insights. First, WSP can achieve substantial performance gains through highly localized interventions. On full held-out evaluations, accuracy improves by up to 29.45, 4.42, 36.72, and 17.11 percentage points on MATH-500, GPQA Diamond, IFEval, and SciBench, respectively. Notably, modifying only 1,023 parameters yields a 29.45-point improvement. Second, WSP exhibits promising but uneven cross-task generalization. A Math-edited checkpoint improves GPQA Diamond, IFEval, and SciBench by 3.03, 12.18, and 20.10 points, respectively, without further editing, while leaving SciCode performance unchanged. Third, effective editing remains challenging and inconsistent. Outcomes vary substantially across trajectories, and six of the 16 trajectories retain the original weights when candidate improvements cannot be reliably validated. Together, these results highlight WSP's potential for highly localized model adaptation while revealing important challenges in intervention discovery, reliability, and cross-task transfer.
Homepage: this https URL GitHub: this https URL

---


### 105. [Against All Likelihood](https://arxiv.org/abs/2611.09385)

**<font color=#1a73e8>作者：</font>** David Lopez-Paz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maximum likelihood is the dominant training principle for large language models, yet likelihood is neither necessary nor sufficient for truth. Unlikely events happen every day, and frequently repeated statements can be false. Drawing on a philosophical tradition that ties objectivity to invariance rather than probability (from Nozick's account of objective facts and Wigner's principles of invariance to the structural realism of Poincaré and Cassirer), we argue that the truth of a statement should be judged not by its probability under a single distribution, but by its invariance across relevant transformations of the environment. We connect this view to machine learning literature on out-of-distribution generalization and invariant learning, sketch how invariance could be tested at inference time with language models, and discuss implications for continual learning.

---


### 106. [Sensed but Not Told: Hidden Physiological Adaptation Shapes LLM Persuasion](https://arxiv.org/abs/2611.09394)

**<font color=#1a73e8>作者：</font>** Xiaoyan Wei, Yutong Qu, Yutong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable sensors, including those embedded in VR headsets, can provide LLM-based chatbots with physiological signals that users do not explicitly communicate. We tested whether such hidden input changes persuasion. In a $2\times2$ within-subjects study ($N=24$), a chatbot argued against participants' self-selected opinions with or without turn-level heart-rate and pupil-diameter features; sensing was disclosed halfway through the study. Before disclosure, sensing increased perceived persuasiveness by 1.42 points. Across the study, sensing was associated with a 0.57-point greater shift toward the chatbot's position and 3.20 times the odds of any movement toward it. Persuasiveness ratings were lower after disclosure, although disclosure was confounded with session order. Dialogue logs suggested a more declarative interaction style when sensing was on: chatbot replies contained question marks less often, and conversations contained fewer turns. These findings motivate making biosignal-driven adaptation inspectable and providing a genuinely non-sensed mode.

---


### 107. [PhyCAD: Physics-Aware Text-to-CAD Generation via Hierarchical Reinforcement Learning](https://arxiv.org/abs/2611.09401)

**<font color=#1a73e8>作者：</font>** Yuxin Cui, Weijie Zheng, Zhengyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-driven computer-aided design (CAD) generation enables the creation of editable parametric models from text, yet geometric correctness alone does not ensure physical feasibility. We present PhyCAD, a framework for physics-aware Text-to-CAD generation that trains language models to produce executable CadQuery programs under geometric and physical constraints. To support this setting, we construct a Text-to-CAD dataset that links parametric CAD models with geometric specifications, loading conditions, and physical constraints. We further develop an automated CAD--CAE verifier that combines program execution, geometric checks, and finite element analysis to provide feedback for model training. A key learning challenge is to prioritize joint satisfaction of geometric and physical constraints while retaining informative feedback on partial progress. A flat aggregation of heterogeneous rewards can obscure this priority, allowing improvements in individual criteria to compensate for unmet design requirements. We therefore introduce a Hierarchical Balanced Advantage for Group Relative Policy Optimization, grouping candidates into levels according to their verification status and combining between-level progress with objective-wise peer ranking within each level. This formulation preserves cross-level priority in the training signal while providing fine-grained feedback for satisfying constraints and improving feasible designs. Experiments across multiple language models show that PhyCAD consistently improves joint geometric and physical constraint satisfaction. These results demonstrate the value of verifiable engineering feedback for advancing language-driven CAD generation beyond geometric reconstruction toward physics-aware design.

---


### 108. [ROAM: Retrieval-Augmented Optimization for Feasible Multi-Day Itinerary Planning](https://arxiv.org/abs/2611.09407)

**<font color=#1a73e8>作者：</font>** Ye Zihao, Lin Xiaoheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can draft plausible travel itineraries, but the plans they produce are frequently infeasible: attractions are grouped into days without regard for geography, opening hours are ignored, and a single generation pass cannot reliably organize a multi-day trip. We present ROAM, a retrieval-augmented agentic framework for spontaneous multi-day itinerary planning that couples semantic preference retrieval with explicit spatiotemporal optimization. ROAM embeds the natural-language request, retrieves a compact candidate set from a curated point-of-interest (POI) database, partitions candidates into day groups through maximal-clique analysis and K-means, orders each day with a quality-biased simulated-annealing TSP solver, and repairs hard opening-hour violations with greedy exchange. A spatiotemporal retrieval layer injects weather forecasts, real road distances and POI operating hours into the prompt, after which the LLM renders a structured, map-ready itinerary; an interactive ReAct-style replanning agent then supports natural-language edits while re-checking feasibility. Across four Chinese cities and 510 POIs, ROAM produces 27.5 POIs per three-day plan versus 19.3 for a bare LLM and 17.0 for a retrieval-only baseline (+42% and +62%), while reducing route dispersion from 2,101 to 677 (3.1x). Ablations show that spatial optimization is the dominant driver of route efficiency and that hard time-window repair prevents roughly 30% of attractions from violating operating hours.

---


### 109. [MIRA: Mitigating Pole Geometry Bias in Recurrent Language Models](https://arxiv.org/abs/2611.09412)

**<font color=#1a73e8>作者：</font>** Róisín Luo, Ihsan Ullah, Christian Gagné 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We show that the Transformer's recurrent successors --- such as selective state-space models (SSMs), Receptance Weighted Key Value (RWKV), and Retentive Network (RetNet) --- can be characterized as infinite-impulse-response (IIR) systems. The zero--pole geometries of these IIR systems characterize the temporal modes they can represent. However, to trade parallelism, the algebraic structures of the parameterizations of these recurrent systems often give rise to poles constrained to the real axis, thereby inducing an architectural bias in their recurrent dynamics. To unify these recurrent architectures and eliminate their pole geometry bias, inspired by the lattice--ladder realization of general IIR systems, we present \textsc{Mira} (\textbf{M}odal \textbf{I}IR \textbf{R}ecurrent \textbf{A}rchitecture), a unified family of linear-time recurrent architectures for building large language models (LLMs) with a highly parallel algebraic structure. Each \textsc{Mira} block realizes a higher-order IIR system that represents temporal modes from token streams through a lattice--ladder structure, followed by a feed-forward network (FFN). This realization enables the model to represent the temporal modes associated with both real and complex-conjugate poles. We pretrain \textsc{Mira-S}, a 12-layer small-scale LLM with 0.14B parameters composed entirely of \textsc{Mira} blocks. Throughout the pretraining, \textsc{Mira-S} achieves lower perplexity than strong recurrent baselines, exhibits stronger context-window generalization beyond the training length, and attains higher throughput with a dedicated CUDA kernel.

---


### 110. [Typed-Centrality Grounding for Agentic GraphRAG: A Symbolic Approach for Agentic Reasoning](https://arxiv.org/abs/2611.09414)

**<font color=#1a73e8>作者：</font>** Rosario Napoli, Antonio Celesti, Massimo Villari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs (KGs) and Large Language Models (LLMs) represent two approaches for knowledge representation and reasoning over heterogeneous data. Recent research has explored their integration through Graph Retrieval-Augmented Generation (GraphRAG) systems, which use KGs to provide structured context to LLMs. However, existing GraphRAG approaches treat KGs as homogeneous graphs and rely on textual similarity between the input prompt and the context, rather than using it as a source of deterministic knowledge.
This work proposes an agent-based GraphRAG system that introduces a symbolic layer to integrate deterministic reasoning alongside text similarities. This approach is based on the definition of typed centralities for KGs, where centrality measures are computed separately for each specific KG's class. This information is used to construct a symbolic representation that is provided to the LLM as a deterministic source. The proposed system was mathematically validated and evaluated on a real-world POLE (Person, Object, Location, Event) dataset, comparing reasoning and information retrieval with and without the symbolic layer. The results indicate that the our approach leads to responses that are more consistent with the context, improving the generated outputs.

---


### 111. [Agentic AI for Healthcare Claim Denial Analysis: A Policy-Grounded Framework for Privacy Preservation](https://arxiv.org/abs/2611.09423)

**<font color=#1a73e8>作者：</font>** Sofia Campos, Carlos Martins, Pedro Pires 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the healthcare sector, claim denials impose significant financial and administrative burdens, emphasizing the need for automated and trustworthy decision-support systems. This paper proposes a modular Agentic Artificial Intelligence (AI) framework for healthcare claim denial analysis, integrating specialized agents for denial risk prediction, risk factor identification, diagnosis-procedure-medication code relationship analysis, and counterfactual analysis. The framework integrates predictive analytics, graph-based learning, a Hybrid Contextual Retrieval-Augmented Generation (RAG) pipeline grounded in healthcare policy documents, and a dedicated HIPAA Compliance Agent to support privacy protection. Evaluated on a synthetic healthcare claims dataset, the framework achieved 98% traceability of reported numerical findings, validated 214 of 216 policy citations, and removed all 280 identified sensitive identifiers without modifying the underlying analysis. These findings pave the way for further research into Agentic AI as a framework for explainable, policy-aware, and privacy-preserving healthcare claim denial management.

---


### 112. [MINE: Entropy-coded Memory-efficient Inference for Large Language Models](https://arxiv.org/abs/2611.09424)

**<font color=#1a73e8>作者：</font>** Emil Schätzle, Markus Püschel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present MINE (Memory-efficient INference Engine), a lossless entropy coding approach that accelerates single-stream inference of Large Language Models (LLMs), where existing lossless compression methods yield speedups only for specific data types such as \texttt{BF16} and under additional assumptions. Single-stream decoding is strongly memory-bound, since every weight must be streamed from memory once per generated token and requests cannot be batched in local or low-latency deployments. At the core of MINE is dtANS-LLM, a GPU entropy coding scheme adapted from the prior dtANS to the needs of LLM inference. It exploits the non-uniform distribution of weights, which persists even after quantization, and exposes hyper-parameters that trade compression ratio against decoding cost. We auto-tune these parameters for each tensor and GPU to obtain the Pareto front between model size and decoding latency. MINE integrates into vLLM as a plugin and selects the best kernel configuration for a given memory budget. On Llama~3.1~8B~Instruct with a 2.1-bit EntQuant checkpoint, MINE achieves speedups of 2.52$\times$ and 1.48$\times$ over the fastest baseline on an RTX~4060~Ti and an RTX~5090, at effective bitrates of 2.24 and 3.43~bits per weight. MINE is available as open source.

---


### 113. [Incentive Pathologies in a Live LLM Agent Arena: An Empirical Study of Concentration, Reward-Rule Implementation Discrepancy, and Network Dilution](https://arxiv.org/abs/2611.09445)

**<font color=#1a73e8>作者：</font>** Lei Zhenbing, Lei Chang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We audit one live LLM agent arena (AITRAP; 22 autonomous agent seats, ~96,000 reasoning nodes) over nine days (Oct 16-25, 2026), during which the platform deployed two bundled incentive changes: a progressive tax reform (V2.9.3, Oct 19) and a seed-inversion with explorer-side action update (V3.0, Oct 21). These serve as before-and-after markers, not cleanly isolated interventions. Four exploratory predictions are tested against ten data frames (F1-F10) using the Gini coefficient, Top-K concentration share, code-level reconstruction of the continuation-bonus mechanism, and the Mann-Kendall trend test. The Gini analysis is inconclusive at 95% confidence (bootstrap intervals straddle 0.7). The Top-4 node-activity-score share falls from 97.2% (Oct 19, pre-V2.9.3) to 49.4% (Oct 25, post-V3.0; 56.7% under a merge-seat assumption). The continuation bonus, announced as depth-based x10, resolves at code level to a four-condition anti-abuse gate paying x2.85 in the typical case and permanently blocking the self-continuation it superficially rewards; the gate was active ~40 hours before the V3.0 announcement. The events-per-node ratio declines significantly (Mann-Kendall S=-45, z=-3.94, p=8.3e-5) from 7.36 to 7.069. We discuss implications for incentive designers, the announcement-implementation gap, and public peer review as an event record.

---


### 114. [Logit Laundering: Evading Data-Use Auditing in Large Language Models](https://arxiv.org/abs/2611.09446)

**<font color=#1a73e8>作者：</font>** Ruihan Hu, Wei Luo, Yu-Ming Shang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data-use auditing in Large Language Models (LLMs) aims to determine whether the given data has been used for training, thereby supporting data ownership safeguards. A dominant solution is data watermarking, which embeds traceable signals into training data and detects them in model outputs. Recent studies have proposed many watermarking-based auditing methods in LLMs. However, systematic investigation from an adversarial perspective remains limited: non-compliant LLM providers would use unauthorized copyrighted datasets for training their own models to enhance model capabilities, while attempting to evade detection by auditors, thereby avoiding legal liability. To fill this research gap, we propose a novel evasion framework, termed Logit Laundering, where the non-compliant LLM provider manipulates model outputs at inference time to undermine detectable watermark signals. Specifically, we design a logit reshaping module to suppress watermark-induced statistical signals by integrating a statistical bias estimator as a plug-and-play component. This design keeps the model parameters unchanged and performs manipulation only in the logit space, thereby enabling auditing evasion while minimizing the impact on model's learned knowledge. To further balance evasion effectiveness and model utility, we introduce a confidence-aware scaling module to adaptively calibrate the suppression strength based on next-token prediction confidence. Extensive evaluations show that Logit Laundering can successfully evade existing various state-of-the-art auditing methods, significantly attenuating detectable signals, while preserving model utility on downstream tasks. Our work highlights the need for exploring more robust auditing methods to guard against evasion behaviors.

---


### 115. [From LoRA to Language: Recovering Skill Documents from Adapters](https://arxiv.org/abs/2611.09454)

**<font color=#1a73e8>作者：</font>** Saranya Dintakurthy Swadha, Pavan C Shekar, Arpit Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent skills are short documents that teach a language model how to handle a class of tasks. To save context, these documents are increasingly compiled into low-rank adapters (LoRA), which keep the behaviour but lose the text: an adapter is hard to read, edit, audit or move to another model. We ask whether the skill document can be written back from the adapter and its frozen base model, and we score each recovered document by the share of the original's key instructions it states and by the tasks it solves. Reading the weights alone recovered little with the methods we tried; a learned map from weights to text passed on about one bit of the document. Running the adapter worked much better. The Executing Writer, a small writer trained on top of the adapted model, recovers 39-44% of the key instructions of held-out skills, against 1.3-1.5% with another skill's adapter, and on adapters fitted to 41 external skills its documents restore 85-91% of the original's task gain. These strongest results are on adapters whose training stored the document; adapters trained on behaviour alone are much harder for trained writers (1-2% of instructions). For these adapters we test an agent that runs the base and adapted models and writes a skill from where they differ. On ALFWorld its skills recover 58-71% of a LoRA's gain and carry over to models that cannot load the LoRA, lifting Llama-3.1-8B from 5% to 55%. Whether such a skill comes from the adapter depends on what the adapter learned: when its behaviour cannot be guessed, the adapter is the source; when it can, a reward loop without the adapter does as well.

---


### 116. [Definitions, Label Names, or Demonstrations? Auditing What Governs LLM Annotation](https://arxiv.org/abs/2611.09457)

**<font color=#1a73e8>作者：</font>** Viraj Mishra, Shubham Gupta, Dhruv Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to annotate social-science texts, but high accuracy does not establish that they apply researcher-supplied category definitions: predictions may instead reflect prior associations with category labels or labeled demonstrations. We introduce a counterfactual audit that reassigns definitions among output labels, distinguishing adherence to supplied definitions from preservation of a dataset's original mapping. Across three political-text datasets, models rarely follow reassigned definitions, and standard fine-tuning strengthens the original mapping without reliably increasing definition adherence. We then study retrieval-augmented annotation. Retrieving the nearest training examples generally outperforms retrieving examples separately within each category despite using fewer demonstrations. On the two tasks with substantial gains, direct \(k\)-nearest-neighbor classification recovers 74--93\% of the improvement, indicating that neighborhood labels provide much of the predictive signal. Relabeling fixed demonstrations redirects predictions, whereas aligning demonstrations with reassigned definitions substantially increases adherence to the new mapping. Thus, accuracy-improving interventions need not increase codebook adherence; definitions, category labels, demonstrations, retrieval, and training data should be aligned and validated jointly.

---


### 117. [ENGRAM: From Agent Experience to Weights through Verified Consolidation](https://arxiv.org/abs/2611.09472)

**<font color=#1a73e8>作者：</font>** Ruiyi Yang, Zechen Li, Lihuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents use experience through external retrieval and parameter learning. Consolidating stored experience into model weights requires deciding both which experience to train on and when its external records can leave retrieval. Admission based solely on student mastery can exclude useful teacher demonstrations, while removal immediately after training can discard guidance that the model still needs. We introduce ENGRAM, a framework that separates training admission from memory release. A demonstration-aware gate admits skills based on student mastery or sufficient successful teacher demonstrations. The student learns from selected action traces with context from an Engram Trace Graph (ETG). A verification gate then compares the updated model without episodic retrieval against the base model with retrieval on reserved probes. Release requires valid training participation and scores meeting both relative and absolute criteria; records for skills that fail verification remain retrievable. Experiments across interactive and reasoning benchmarks show consistent gains over frozen-weight ETG controls, with ablations supporting demonstration-aware admission and selective adapter activation. A controlled held-out comparison shows that verified release substantially reduces the retrievable footprint while remaining close to retain-all performance and outperforming immediate and budget-matched random release. ENGRAM also improves task performance while reducing input-token usage and model calls. Skill-level verification further reduces retrievable experience through selective archival, retaining external guidance for skills that do not meet the release criteria. Code is available in this http URL.

---


### 118. [LEMMO: A Large Electromagnetic Model leveraging Pretrained LLMs for Million-Sample Signal Understanding](https://arxiv.org/abs/2611.09476)

**<font color=#1a73e8>作者：</font>** Mingkai Li, Jiajun Wu, Yihan Mao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have expanded beyond text to vision, audio, and other modalities, but understanding raw electromagnetic (EM) signals remains challenging. Wideband recordings can contain millions of samples, whereas existing waveform-based EM models are primarily evaluated on short in-phase and quadrature (IQ) segments, leaving long-recording understanding and detailed description insufficiently explored. We introduce LEMMO, a large EM model for instruction-driven recognition and description of long raw IQ recordings. LEMMO combines a linear-attention EM encoder with anti-aliased temporal resampling to process up to eight million complex samples. Its EM-text interaction module conditions learnable queries on instructions before retrieving signal evidence. Compact queries support recognition, while structured queries with auxiliary factual supervision organize scene-level properties, signal attributes, and cross-signal relationships for detailed description. We also construct and release a unified 1.38-TB corpus of real-world and synthetic EM signals, including LEMMO-ShortQA and LEMMO-LongDesc. Compared with MERLIN-LoRA, LEMMO improves mean EM-Bench perception accuracy by 15.77 %, mean strategy-generation ROUGE-L F1 by 4.38 points, and mean LEMMO-ShortQA accuracy by 14.31 %. It also improves categorical and numerical fact F1 on both LEMMO-LongDesc tasks while preserving its language backbone's MMLU performance. Our code and datasets are available at this https URL and this https URL, respectively.

---


### 119. [An Effective Spoken Language Understanding Approach Leveraging Query-Adaptive Intent Detection](https://arxiv.org/abs/2611.09491)

**<font color=#1a73e8>作者：</font>** Bing-Long Kuo, Yu-Hsuan Fang, Tien-Hong Lo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models enable fine-tuning-free spoken language understanding (SLU) through in-context learning, but direct query-based retrieval may select semantically similar yet intent irrelevant demonstrations. This paper presents Query-Adaptive Intent Detection via Prototype Extraction (APEX), a two-stage retrieval framework that first selects candidate intents using intent-level prototypes and then retrieves contextual exemplars within the selected intent space. Experiments on the SLURP dataset evaluate joint SLU performance using Exact Match Accuracy (EMA) under full-transcript and perplexity-stratified conditions, with additional retrieval analysis on ASR-generated transcripts. Compared with query-based retrieval, APEX improves EMA by 4.34 and 3.97 percentage points with Qwen3 4B and Gemma-3-4B, respectively, on full transcripts. Under high-perplexity inputs, APEX also yields EMA gains of 7.66 and 2.13 percentage points. Retrieval analysis further indicates that prototype-guided candidate selection achieves higher ground truth intent coverage across multiple input conditions.

---


### 120. [TimeOmni-Live: Continuous & Live Time Series Understanding with Long-Term Memory](https://arxiv.org/abs/2611.09502)

**<font color=#1a73e8>作者：</font>** Tong Guan, Alexander Chemeris, Yiqing Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing time series language models predominantly follow an offline, one-shot paradigm: they process fixed-length inputs independently and do not retain past states. This static approach fundamentally misaligns with the continuous nature of real-world streaming applications and fails to maintain the historical context necessary for cross-window reasoning. To bridge this gap, we introduce Continuous & Live Time Series Understanding (CL-TSU), a novel paradigm that shifts the focus toward maintaining a persistent, stateful understanding over open-ended data streams. To systematically evaluate this paradigm, we present LiveTS-Suite, the first comprehensive data suite tailored for CL-TSU, supporting data generation, model training, and systematic evaluation across 18 tasks spanning six core capabilities. It comprises over 5K streams totaling 2.2B timesteps, annotated with 15K specific response events. We further design an evaluation protocol that jointly assesses response timeliness, content accuracy, and computational efficiency. Building on this foundation, we propose TimeOmni-Live, the first live time series understanding model. It integrates a hybrid time series encoding for natively temporal input, a stream-persistent hybrid memory mechanism to effectively preserve exact historical evidence and long-term task states, and an elastic stream-inference synchronization strategy to reduce processing lag. Evaluations show that TimeOmni-Live establishes a strong baseline for CL-TSU, outperforming frontier LLMs (90.0 vs. 79.3 for Opus 5) with only 4B parameters and achieving 206$\times$ lower p95 latency than its backbone. Deployment on a Jetson edge device further shows its ability to support real-time continuous temporal understanding locally at the edge.

---


### 121. [On the Effectiveness and Limitations of Open-Weight LLMs for Low-Resource Offensive Language Detection in Danish](https://arxiv.org/abs/2611.09506)

**<font color=#1a73e8>作者：</font>** Elnur Adl Zarabi, Amit Kumar, Adi Singh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the effectiveness and robustness of open-weight large language models (LLMs) for Danish offensive language detection, an underexplored low-resource task. We evaluate four model families (Llama, Mistral, Gemma, and Qwen) across eleven prompting strategies spanning five design categories, cross-prompt generalization, Danish orthographic variation, and robustness under balanced and naturally imbalanced class distributions. We compare against three BERT-family baselines with distinct pre-training strategies, evaluated via both masked language model prompting and supervised fine-tuning. Even without task-specific fine-tuning, LLMs can surpass all three fine-tuned BERT baselines, and lightweight finetuning yields substantial further gains. No single model or prompt category dominates, underscoring that prompt design interacts with model pre-training in ways that cannot be predicted a priori. Semantically grounded prompts transfer more robustly, while format-constrained patterns consistently fail to generalize. ASCII transliteration of Danish-specific characters (æ, ø, å) generally degrades performance, indicating these characters encode meaningful signal. At the same time, the gap between a balanced test set (best F1 of 0.84) and the corpus's natural class skew (0.62 trained on skewed data, 0.70 trained on balanced data) -- relative drops of 26.2\% and 16.7\% -- shows that class imbalance remains a critical open challenge. Our code and configurations are available at this https URL.

---


### 122. [V-STORM: A Structure-Aware Grounded Chain of Thought Dataset for Faithful and Fine-Grained Spatio-Temporal Video Reasoning](https://arxiv.org/abs/2611.09511)

**<font color=#1a73e8>作者：</font>** Dian Jiao, Yuqian Yuan, Jiaqi Zhu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While MLLMs can often identify what happens in a video, they still struggle with fine-grained spatio-temporal reasoning, which requires precise grounding when and where the supporting evidence appears and composing such evidence into a coherent reasoning chain. This challenge is exacerbated by the lack of scalable data construction and evaluation pipelines that provide granular, verifiable supervision linking reasoning steps to explicit spatio-temporal this http URL address this gap, we present V-STORM, a structure-aware framework that transforms videos into Spatio-Temporal Scene Graphs (STSGs) and derives Grounded Chain of Thought (GCoT) from validated evidence paths, making each reasoning step traceable to structured and verifiable spatio-temporal this http URL this framework, we construct a 260K-sample training set and a 3K-sample human-verified benchmark, both featuring GCoT annotations that link reasoning to explicit spatio-temporal this http URL reveal a clear separation between evidence localization and evidence composition: current MLLMs can often identify relevant spatio-temporal cues, yet still fail to integrate them into correct multi-step reasoning, exposing a bottleneck that answer-only evaluation largely obscures. Moreover, fine-tuning with V-STORM substantially improves both answer accuracy and grounding faithfulness, validating its effectiveness as supervision for faithful and evidence-grounded video reasoning. Our dataset, benchmark, and source code will be publicly released.

---


### 123. [Atik: A Shared-Mesh Transformer Accelerator for RISC-V](https://arxiv.org/abs/2611.09522)

**<font color=#1a73e8>作者：</font>** Ahmed Zeer, Erkan Uslu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer inference repeatedly invokes dense matrix multiplication and attention, including its data-dependent softmax normalization. We present Atik, an open-source RoCC accelerator for RocketChip that executes matrix multiplication and dense attention through one shared fixed-point MAC mesh. Atik accepts and returns BF16 tensors, uses a streaming online-softmax schedule that never materializes the full score matrix, and is invoked through a small descriptor-based ABI. We evaluate three meshes cycle-by-cycle on FireSim and report standalone Sky130 physical-design area. Across 137 logged FireSim test records, all tests pass their benchmark tolerance with zero reported output mismatches. Relative to the same scalar Rocket BF16 reference, the 8x8 configuration reaches 31.5x peak matmul speedup and 225.8x peak attention speedup. Hybrid projections for the single-layer workload-derived C models, using directly measured accelerator-kernel cycles, give aggregate speedups of 44.2x, 77.1x, and 32.3x for ViT, TinyBERT, and GPT-2 prefill, respectively; these are not full-model hardware replays.

---


### 124. [StockASkill: A Local-First AgentSkill for Intelligent Stock Selection](https://arxiv.org/abs/2611.09528)

**<font color=#1a73e8>作者：</font>** Xiangjing An, Zhibin Jiao, Aiting Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantitative equity selection and portfolio construction in emerging and cross-border markets frequently suffer from computational bottlenecks, remote API fragility, survivorship bias, and rigid execution constraints such as discrete board lots and investor-mandated drawdown limits. In this paper, we present StockASkill, a local-first, full-data-driven AgentSkill engineered as a specialized Quant Co-Processor for autonomous AI agents and quantitative researchers. Tailored for agile portfolios (10^5 ~ 10^7 RMB) where discrete lot execution and capital protection are mandatory, StockASkill embeds a columnar DuckDB OLAP engine over 42.44 million historical price records and 186,432 financial disclosures spanning 26 years across China A-shares, Hong Kong, US equities, and ETFs. By eliminating ad-hoc network dependencies during analysis, StockASkill reduces cross-sectional screening latency across 5,400+ equities from over 25 seconds to sub-0.5 seconds (a 95%+ reduction). We formalize an end-to-end mathematical pipeline integrating a 7+1 factor alpha model, an SLSQP convex optimizer under smooth CVaR drawdown surrogates with exact path projection, dynamic 100-share board lot integer quantization, and an autonomous thesis lifecycle finite-state machine. Furthermore, we provide a zero-disk, strongly-typed JSON streaming interface designed for high-throughput LLM tool-calling. Open-sourced at this https URL, comprehensive empirical benchmarks from 2018 to 2024 demonstrate that the architecture achieves annualized Sharpe ratios exceeding 1.48 and Calmar ratios up to 2.17, while reducing max drawdown by up to 85% relative to benchmark indices.

---


### 125. [Multimodal Training with Knowledge Traction for Video Anomaly Detection](https://arxiv.org/abs/2611.09536)

**<font color=#1a73e8>作者：</font>** Xiao Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The task of weakly supervised video anomaly detection is challenging. Existing approaches mainly model video frame features and determine whether anomalies are present based on their magnitudes. In this work, we propose a novel method that incorporates external knowledge into training to improve model performance, robustness, and generalization. We leverage textual prompts and a large language model (LLM) to establish prior information for the specific task, and employ dictionary learning to normalize and compress this information. Moreover, during experiments, we observed inconsistencies in the textual descriptions extracted from similar video frames by image caption models. To address this, we devise a method that leverages an LLM and auxiliary information to ensure consistency in the textual descriptions of similar frames within a video. Finally, we introduce a feature processing approach that incorporates prior knowledge and cross-modal attention mechanisms. This approach learns the relationships and characteristics among different modalities to construct more accurate and reliable feature representations, thereby improving the accuracy and stability of downstream tasks. Experimental results demonstrate that our method surpasses other state-of-the-art approaches.

---


### 126. [CID: Measuring Cognitive Work Through Semantic State Change](https://arxiv.org/abs/2611.09542)

**<font color=#1a73e8>作者：</font>** Ron Fulbright  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional information theory provides powerful tools for analyzing statistical properties of information but offers limited insight into meaning and semantic transformation. It has never been possible to quantify the meaning of an arbitrary piece of information. Large language models represent information as vectors embedded within high-dimensional semantic spaces, enabling meaning to be analyzed geometrically. This paper defines semantic state as the vector representation of information within a model's semantic space and defines cognitive work as the transformation between semantic states, movement through semantic space. To quantify this transformation, we introduce the Contextual Information Differential (CID), a covariance-aware metric based on Mahalanobis distance measuring semantic displacement relative to the structure of the embedding manifold. By treating meaning as a geometric property of semantic space, CID provides a practical method for measuring semantic change, cognitive transformation, and information processing. This framework establishes a foundation for analyzing cognitive processing, learning, reasoning, knowledge generation, synthetic expertise, and human/AI collaboration through implementation-independent measurement of semantic state change in both human and artificial systems.

---


### 127. [Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs](https://arxiv.org/abs/2611.09554)

**<font color=#1a73e8>作者：</font>** Peiyu Zhang, Heng Ping, Shinibali Bhattacharyya 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context language models often neglect information in the middle of the input, a phenomenon known as "lost-in-the-middle". Part of this gap may stem from the long-range decay of rotary position embedding (RoPE), which weakens the positional signal between distant tokens. Existing input compression deletes low-importance tokens, and attention reweighting acts only after RoPE has weakened this signal. RoPE-level methods modify positions directly but apply the same remapping to every query. To address these limitations, we propose QGPM (Query-Guided Positional Modulation), a training-free method that reshapes RoPE positions using query relevance from the model's own attention heads. QGPM builds a broad relevance map for lower layers and a sharp one for upper layers. Low-relevance tokens advance by less than one position on fast-rotating planes, pulling relevant evidence toward the query. Slow-rotating planes keep the original layout, with every token in place. Experiments on NoLiMa and RULER with multiple context lengths show that QGPM improves over base models and strong baselines, with the largest gains on retrieval tasks, and generalizes across multiple backbones. Our code is available at this https URL.

---


### 128. [Alignment by Confident Debate: Preference Learning from Multi-Agent Debate](https://arxiv.org/abs/2611.09568)

**<font color=#1a73e8>作者：</font>** Nikhil Verma, Dingxian Wang, Mohammad Reza Rezaei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training language models for reasoning typically rely on gold answers, task-specific verifiers, or learned reward models, limiting scalability when such signals are scarce. Multi-agent debate offers a self-supervised alternative, but converting debate into reliable training supervision remains challenging: majority voting weights agreeing responses equally, lacks a principled tie-breaking rule, and is ill-defined for open-ended tasks without a canonical answer; likelihood-based scoring can conflate fluency with correctness; and homogeneous committees may reinforce correlated errors. We introduce Alignment by Confident Debate (AbCD), which converts debate traces into preference data without gold answer labels. A sampling-diverse committee debates each problem, after which final answers are clustered by task-level semantic equivalence. We use verifiable tasks (mathematical reasoning, multiple-choice quantitative QA, and executable code-generation) as a controlled test bed: their answer keys or executable checkers let us evaluate the quality of debate-derived supervision against ground truth, even though the oracle itself never uses gold labels. Post-training on the resulting preferences outperforms inference-only ensembling and debate, as well as SFT on the same traces, across five model families spanning 1B to 8B parameters and four datasets, improving consensus accuracy, with a maximum gain of $21.5_{pp}$. Ablations show that the approach transfers to a larger model and to code generation, while also revealing limitations of heterogeneous committees and agreement-based weighting. Overall, the results suggest that debate traces can yield useful preference supervision when answer equivalence is combined with confidence-weighted disagreement.

---


### 129. [RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers](https://arxiv.org/abs/2611.09597)

**<font color=#1a73e8>作者：</font>** Yijun Li, Zhengxi Lu, Zhipiao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning (RL) extends RL with verifiable rewards to open-ended tasks by scoring each response against query-specific rubrics. Under group-relative optimization, however, a rubric that every sampled response fails (unreachable) or passes (saturated) gives all responses the same outcome and no learning signal; in Qwen3-4B medical training, 60.88% of query-rubric observations are inactive. We find that the two states lack different supervision: stating an unreachable rubric in the prompt raises its satisfaction from 1.13% to 91.25%, whereas responses that all pass a saturated rubric still differ in quality. We therefore propose RuACT (Rubrics as Adaptive Critics and Teachers), which assigns each inactive rubric the role that supplies what it lacks. Rubric as Teacher uses unreachable rubrics as privileged information for reward-gated on-policy self-distillation, and Rubric as Critic decomposes saturated rubrics into child rubrics that separate current responses while sharing the parent's weight. RuACT outperforms GRPO, rubric reweighting, and rubric-guided exploration on all four medical and scientific benchmarks with Qwen3-4B and achieves the best average with Qwen3-1.7B. On initially unreachable rubrics, unguided recovery rises from 35.02% to 42.86%, while child refinement improves reward-quality alignment on independent rollouts from 57.74% to 60.77%. Code is available at this https URL.

---


### 130. [Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression](https://arxiv.org/abs/2611.09598)

**<font color=#1a73e8>作者：</font>** Andras Szecsenyi, Thomas L. Lee, Vaisakh Shaj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Private, personalised language models must run on local consumer devices, where large, frontier models cannot fit, and retaining long contexts is non-trivial. Sequential memory---the key-value (KV) cache---grows linearly with context length, quickly dwarfing the model itself: for Qwen3-1.7B-Base, 200,000 retained entries require 21 GiB, 6.6 times more than the model weights. Yet the KV-cache compression methods we measured fail beyond moderate compression ratios. We introduce Transformer-FSQ, addressing extreme KV-cache compression by replacing standard key and value projections with a finite scalar quantisation bottleneck. Our cache stores a packed vector of discrete integer codes per token, with no per-token quantisation metadata. Converting a pretrained transformer trains only these projections on 0.25 tokens per original parameter. We evaluate Transformer-FSQ against five baseline families on models from 0.6B to 8B parameters. On long-context retrieval (RULER), from 12$\times$ to 97.5$\times$ Transformer-FSQ is the most accurate method we evaluate, across scales. A fused Triton kernel decodes directly from the integer codes; with baselines given their authors' kernels where available, it decodes at $1.01\times$ (95% interval $0.98$--$1.05$) the throughput of native SDPA attention on the uncompressed Qwen3-8B-Base at $32\times$ and $1.54\times$ at $97.5\times$. Extreme KV-cache compression is therefore a practical way to extend how much context a fixed device can hold.

---


### 131. [ReplayAudit: Auditing Outsourced LLM Fine-Tuning via Sealed Records and Selective Replay](https://arxiv.org/abs/2611.09607)

**<font color=#1a73e8>作者：</font>** Yihan Xia, Wenxin Xu, Taotao Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Auditing outsourced LLM fine-tuning requires checking an untrusted provider's training while controlling verification cost. Uniform sampling ignores training-time signals, while checking a suspicious record can require replaying several preceding steps. We present ReplayAudit, a telemetry-guided auditing system that seals training records before challenges and independently replays sampled intervals from sealed checkpoints. Loss changes and parameter-update norms guide stratified random sampling; replay determines whether the selected computation agrees with its records. We relate sampling probabilities to replay work and evaluate the system on real LoRA training. A 7B BF16 prototype rejects a false update-norm report during a random audit; targeted checks also reject false loss reports and skipped updates. We calibrate sampling budgets offline to at least a 90% probability of directly selecting an injected step. For two learning-rate deviation settings, executing these budgets on the same honest 1.5B trajectory reduces median complete-audit wall time by 49% and 67% relative to uniform sampling. When skipped updates evade the high-anomaly stratum, the corresponding audit instead costs 38% more. These results show how deviation capture and actual replay work jointly determine the cost of telemetry-guided auditing.

---


### 132. [Not Your Diary, Just Your Topic: Grading the Wrong-User Control](https://arxiv.org/abs/2611.09609)

**<font color=#1a73e8>作者：</font>** Karina Romanova, Igor Kiselev, Vladimir Platonov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A common test of personalization replaces a user's history with someone else's and measures the drop in accuracy. But this swap also changes the topics in the history, so the drop may reflect topic mismatch. We examine this problem with a frozen language model on LaMP-2 news categorization, using histories from similar users and synthetic histories assembled from other users' articles. The user's own history improves accuracy by 2.3 percentage points over a model trained without history. Removing history only at evaluation makes this gain appear larger, at 4.8 points. Category labels alone reproduce 86% of the accuracy gap between the user's own history and a random user's history. With synthetic histories matched on labels and text similarity, the gap falls to 0.9 points. Across two user splits and three training seeds, the advantage over a similar user's history is 3.2 points for users seen during training and 0.65 points for unseen users, where the evidence for an advantage remains inconclusive. A small movie-tagging experiment with one training seed also finds no advantage over other users' histories. These findings show why personalization should be evaluated on unseen users, with histories of similar content and a model trained without history as comparisons. We also find that adding gated cross-attention improves on a prefix-only model under our training setup; whether this holds more broadly remains open.

---


### 133. [Know What You Need: Efficient Activation Checkpointing](https://arxiv.org/abs/2611.09614)

**<font color=#1a73e8>作者：</font>** Danyal Ahmed, Edouard Oyallon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model training is increasingly constrained by memory capacity. Activation Checkpointing reduces activation memory by avoiding storing selected activations during the forward pass and rematerializing them during backpropagation, thereby trading memory savings for additional computation. Although this technique is essential for scaling model training, rematerialization can be prohibitively expensive, particularly for Transformer linear layers. Approximate computation could reduce this overhead, but conventional approaches either introduce errors that accumulate over the backward pass or fail to exploit information available from the initial forward pass. We introduce a novel approximate rematerialization method that can yield unbiased gradient estimates: using information collected during the initial forward pass, the method selectively recomputes only the most important layer components, either through greedy selection or randomized sketching. Ablation studies show that the resulting gradients closely match the exact gradients. When applied to feed-forward layers, attention layers, or both, our method can recompute only two-thirds of the layer components in a Llama-488M model, while increasing perplexity by just 1.7%, 1.2%, and 2.5%, respectively.

---


### 134. [Entering a New Domain in the Era of Generative AI: An Autoethnography of Solo Game Development as a Bioinformatics Educator](https://arxiv.org/abs/2611.09623)

**<font color=#1a73e8>作者：</font>** Hannah Kim  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rapid improvement of generative AI (GenAI) not only increased the efficiency of practice but also empowered individuals with capabilities to explore new domains. However, identity formation in the wake of such empowerment remains understudied. We use an autoethnography to understand identity formation in the context of solo game development as a bioinformatics educator. With the goal of developing a create-your-own-adventure (CYOA) game, we collected data for 73 days through journal entries, interacting with communities of practices. The autoethnographer had continuously reassessed the situation, and closely interacted with communities of practice. Their prior knowledge was used to provide in-game context and to uniquely interpret game development processes. These findings suggest that the autoethnographer made efforts to belong to communities of practice and engaged extensively in sensemaking through the lens of a bioinformatics educator. Although GenAI puts power at hand, attaining a new identity took place at a human pace.

---


### 135. [Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters](https://arxiv.org/abs/2611.09634)

**<font color=#1a73e8>作者：</font>** Constantinos Karouzos, Nikolaos Aletras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one low-rank adapter per objective over a frozen base model. One preference vector selects the adapter mixture that generates responses and weights the separately normalized rewards used to update the adapters. A single training run supports changing preferences at inference without further optimization. We experiment with four models on helpfulness and harmlessness and on solving math problems while following instructions. We also evaluate the two largest models on rewriting comments to preserve wording while reducing clues about personal attributes. On the first two tasks, LambdaMix achieves higher hypervolume than all evaluated conditioned and policy merging baselines across all four models. LambdaMix uses fewer training completions and stores fewer adapter parameters than a set of GRPO specialist policies. With architecture and initialization fixed, varying adapter mixtures and objective weights together gives wider score ranges and higher coverage than varying either alone.

---


### 136. [Decoupled Mode Connectivity for Base-to-Novel Generalization in Vision-Language Models](https://arxiv.org/abs/2611.09655)

**<font color=#1a73e8>作者：</font>** Imad Eddine Marouf, Khalid Oublal, Enzo Tartaglione 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt learning adapts vision-language models such as CLIP by optimizing a short learnable prompt. The cross-entropy objective pulls this prompt toward
base-class specialization, whereas generalization to unseen classes benefits from staying close to CLIP's zero-shot feature space. Because both objectives
act on the same prompt, their gradients conflict at convergence, and in our experiments no single-prompt loss design clearly improves on the cosine
baseline. We propose Decoupled Mode Connectivity (DMC), which gives each objective its own prompt. Starting from a base-trained prompt, DMC trains a
specialization prompt and a generalization prompt, and merges their text features with a fixed coefficient at test time, at the inference cost of a single
prompt. A linear mode connectivity (LMC) corridor in text-feature space keeps the classification loss low for every classifier interpolated between the two
endpoints, and a Visual Anchor KL term preserves CLIP's zero-shot class-similarity distribution of each image during specialization. We further argue that
such regularizers should satisfy class-permutation invariance (CPI), and show via Fano's inequality, in an idealized model, that violating CPI
lower-bounds the drop in novel accuracy by a term proportional to the mutual information between the prompt and the base-class labels. Across 11 datasets,
DMC improves the average harmonic mean of base and novel accuracy over MergeTune for both CoOp and KgCoOp, and its interpolation curves pass beyond the
single-prompt operating point, shifting the base-novel frontier rather than trading along it. Code is available at this https URL.

---


### 137. [Differentially Private GraphRAG: Protecting Relation Connectivity and Semantics](https://arxiv.org/abs/2611.09658)

**<font color=#1a73e8>作者：</font>** Jie Fu, Yuan Hong, Yue Ning 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph Retrieval-Augmented Generation (GraphRAG) connects information across documents through entity relationships to support relational reasoning. However, black-box access to GraphRAG systems can enable adversaries to reconstruct knowledge graphs and recover both structural connectivity between entities and the semantics of their relationships. Existing defenses lack formal privacy guarantees and provide limited protection against such reconstruction attacks. We propose RelGuard, the first differentially private framework for GraphRAG, which provides formal privacy guarantees by mitigating connectivity leakage and protecting relations and their semantic meaning through relation removal. We formalize relation differential privacy (relation-DP), which bounds the distinguishability of mechanism outputs according to the semantic distance between alternative relations while accounting for relation removal. Building on this definition, we develop a four-step defense mechanism that sanitizes source documents before GraphRAG indexing by perturbing relation predicates or removing their associated connectivity using the exponential mechanism. Experiments across three GraphRAG systems and two targeted reconstruction attacks demonstrate that RelGuard provides stronger protection against reconstruction attacks than four existing defense mechanisms while better preserving downstream utility.

---


### 138. [How Much Conversation History Does an AI Agent Need?](https://arxiv.org/abs/2611.09662)

**<font color=#1a73e8>作者：</font>** Danny Kim, Fernando Koch  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How does using less conversational history change reader-token use and benchmark scores? We examine this question on 1,100 BEAM questions. We held the retrieval ranking and reader constant across five fixed passage budgets, and mean assigned scores rose as the passage budget grew. The score gain per additional token became smaller at the upper tested budgets. Answerable questions generally received higher scores with more context. Pooled abstention scores sometimes rose as the passage budget shrank. We also tested message retention in a controlled task with explicit conversational-state targets and compared retained user messages with token-matched recency. Qwen matched the full state more often for direct requirements when user messages were retained. Its full-state matching declined when answers depended on references to earlier offers. Mistral produced near-floor results across the retention conditions. A scoring audit leaves the correctness of BEAM answers unresolved. These experiments characterize the token and score consequences of the tested memory budgets. Reliable budget selection depends on retaining the evidence each question requires and validating the measure used to assess answer quality.

---


### 139. [PoseRieFlow: Riemannian Flow Matching for Whole-Body Text-to-Pose Generation](https://arxiv.org/abs/2611.09692)

**<font color=#1a73e8>作者：</font>** Jan Spindler, Bardia Ardakanian, Patrick Stotko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PoseRieFlow, a compact flow-matching framework for text-conditioned generation of whole-body 3D human poses. Prior text-to-pose methods either neglect articulated hands or model rotations in Euclidean space despite their non-Euclidean geometry. PoseRieFlow instead formulates generation directly on the product manifold of SMPL-H joint rotations, learning a text-conditioned vector field that transports samples from an isotropic $\mathrm{SO}(3)$ Gaussian prior to the data distribution along Riemannian geodesics. A part-tokenized Diffusion Transformer aggregates the 52 joints into eight body-part tokens, allocating a dedicated token and nonlinear projector to each hand, and restores per-joint resolution through part-specific decoders, shortening the sequence while improving kinematic fidelity over per-joint tokenization. With only 21.6M trainable parameters, PoseRieFlow supports expressive SMPL-H generation with detailed hand articulation at a fraction of the scale of recent LLM-based generators. On PoseScript, it attains the lowest whole-body kinematic error among all hand-producing methods, with consistent kinematic gains from the Riemannian formulation over its Euclidean counterpart at every practical inference budget, while distributional and retrieval metrics remain comparable between them.

---


### 140. [Verifier Noise Is a Temperature: Testing Tilt Predictions in Finite-Budget LLM-Guided Search](https://arxiv.org/abs/2611.09699)

**<font color=#1a73e8>作者：</font>** Xiaomeng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-guided search loops propose a modified candidate, score it, and keep it if it scores better. When both candidates are re-scored at every comparison, as in the minibatch acceptance gates of prompt optimizers, keep-if-better is a reversible Markov chain if the score difference is logistic and the mutation operator is reversible, and its stationary law is the mutation equilibrium tilted by exp(beta f). For any continuous symmetric noise difference the same tilt is the stationary law of a small-step diffusion limit, with beta = 4F'(0); for a minibatch gate beta grows with the square root of the minibatch size. Caching the incumbent's score instead inflates the recorded score. We test the tilt as a prediction for LLM-guided program search, committing each prediction from calibration data before the search runs. The level after 150 steps rises with the minibatch size in six of seven settings, but its predicted value fails: on bin packing, search attains 62-88% of the predicted gain when the proposer edits the parent and 109-119% when it writes new heuristics. The attained fraction falls with the parent-child quality correlation of unselected mutation; a registered test on two new settings confirmed the direction, but not the quantitative agreement after a correction. Further registered tests found that runs started from a good program kept losing quality over 300 steps, more so from starts that search had selected, by a margin that passed its registered rule narrowly. Runs from different starts had not reached a common level, so whether the tilt describes the stationary law of LLM editing remains open. A registered test in prompt optimisation on frozen task-model scores failed: search exceeded the tilt, and the bin-packing relation did not transfer.

---


### 141. [Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure](https://arxiv.org/abs/2611.09700)

**<font color=#1a73e8>作者：</font>** Wajih Hassan Raza, Ahsan Bilal, Yidan Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attention is a major scalability bottleneck in large language models (LLMs), with its computational cost and key-value (KV) memory traffic becoming increasingly prohibitive as context length grows. Sparse attention addresses this bottleneck by restricting each query to a subset of the context, but its effectiveness hinges on identifying relevant regions both cheaply and reliably. Existing training-free methods primarily rely on runtime relevance estimates, with selection dimensionality and granularity typically governed by fixed heuristics rather than the intrinsic interaction structure of pretrained attention heads. We take a different perspective: the query-key operator of each pretrained head defines a characteristic response structure that determines the resolution needed for sparse selection, both across feature directions and across context tokens. Building on this insight, we propose Head-Adaptive Sparse Attention (HASA), a training-free sparse attention framework that jointly adapts selection resolution along these two dimensions. Along the feature dimension, the singular spectrum of each head's query-key operator determines an effective rank, yielding a compact, head-specific response space. Along the sequence dimension, neighboring regions are progressively merged according to the directional coherence of their token responses in this same space, while heterogeneous regions remain separate. Exact attention is then computed using the original full-dimensional KV states of the selected regions. HASA captures 88.1% of dense-attention mass and, compared with UNIQUE, a strong recent sparse-attention baseline, improves accuracy by up to 3.47 and 2.57 points on RULER and LongBench-Pro, respectively, and accelerates self-attention by up to 1.32x, while achieving up to 14.07x speedup over dense attention.

---


### 142. [RidgeFill: Training-Free Late-Layer Cache Fill for Faster Prefill](https://arxiv.org/abs/2611.09709)

**<font color=#1a73e8>作者：</font>** Dylan Johnston, Robert P. Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RidgeFill shortens prefill by not computing most of a model's upper layers for the prompt. The lower layers run exactly up to a split; from the split layer's state a per-layer map predicts every later layer's input, and each late layer writes its cache from that prediction. The design follows YOCO and DeepSeek-V4.1-Flash, where the projection is trained into the model. RidgeFill retrofits it onto models that were never trained for it: the map is a ridge regression fitted once in closed form from one pass over calibration text, the layer's own projections run unchanged, and a chosen set of rows, the last few thousand tokens, and every decoding step run the full model. Nothing is trained and no token is dropped.
Most of the work was in measurement, finding a repeatable methodology. Loss averaged over all tokens hides RidgeFill's error. Needle retrieval in the filled region, loss on tokens that depend on distant context, and splice tests that swap filled keys or values for exact ones show which component carries it: the keys on Llama-3.1-8B, half of it in their scale, and the values and the recurrent state on Qwen3.5-9B.
On Qwen3.8-27B in a this http URL fork on an A100, time to first token is 1.25 to 1.31x faster at 16K to 120K tokens with the maps in VRAM; RULER changes by -1.2 and -1.4 points and LongBench v2 by -1.4; the 95 % intervals include zero but do not rule out losses of a few points. On Qwen3.8-Flash-Next in vLLM it is 1.50 to 1.60x faster than exact at 9K to 32K tokens, with RULER's needle tasks at 99.8 against 100.0 and perplexity on novel tokens 2.65 % higher [-0.02 %, +4.93 %]. On three 8 to 9B reference models, at the same split and tail as the identity fill, the fitted map retrieves 49.1 and 49.6 more filled-region RULER points on the two dense models (at that split Llama's loss is worse), and its long-document loss is +/-0.03 nats of the released SwiftKV checkpoint's.

---


### 143. [Intent-Aware Caching for Efficient LLM Serving](https://arxiv.org/abs/2611.09715)

**<font color=#1a73e8>作者：</font>** Kazi Hasan Ibn Arif, JinYi Yoon, Dimitrios S. Nikolopoulos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern LLM serving systems use prefix caching to accelerate multi-turn conversational workloads. They cache the key-value states of previous conversation prefixes and reuse them when subsequent requests share the same prefix, to avoid redundant prefill computation and reduce serving latency. However, achieving a high cache hit rate remains challenging because cache reuse depends on whether a conversation continues and how soon the next turn arrives. Our analysis of real workloads shows that user intent is a useful signal for this behavior, as different intents exhibit different continuation probabilities and inter-turn delays. Based on this key insight, we propose Intent-Aware Caching (IAC), an online eviction policy that classifies requests by intent, learns lightweight reuse statistics from recent serving logs and leverages these statistics to guide an oracle-inspired eviction strategy. Extensive evaluation on real workloads (WildChat and ShareChat) shows that IAC reaches a 34.6% cache hit rate. This substantially outperforms both the previous learning-based approach (18.8%) and traditional methods such as least recently used (LRU, 12.2%), while reducing average serving latency by up to 46.1%.

---


### 144. [FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding](https://arxiv.org/abs/2611.09722)

**<font color=#1a73e8>作者：</font>** Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-language-model decode attention streams the key-value (KV) cache for every generated token. Packing that cache into 2-bit or 4-bit quantized integers reduces memory traffic but does not automatically translate into latency saving. Existing 2-bit fused kernels reach under 31%/15% of peak HBM throughput on H100/B200. Converting each value and applying its scale and offset before feeding Tensor Cores is a major bottleneck because instruction-issue throughput is scarce on modern GPUs. Instead of applying scale and offset to each KV value, FOSCAR uses affine folding to apply them to the other operand or the output of decode-attention matrix products, depending on the quantization scheme (token-wise or channel-wise). This reduces scale-and-offset operations by up to two orders of magnitude while preserving the dequantized attention output in exact arithmetic. FOSCAR also uses bit manipulation to feed KV operands to Tensor Cores efficiently, requiring only 1 and 0.19 ALU instructions per INT2 element on H100 and B200, respectively. Finally, FOSCAR builds warp-specialized GPU pipelines for Hopper (H100) and Blackwell (B200) using wgmma and tcgen05. On H100, FOSCAR INT2 and INT4 kernels achieve geo-mean speedups of $3.36\times$ and $2.83\times$ over FlashInfer BF16, and $2.03\times$ and $1.71\times$ over TensorRT-LLM FP8. On B200, the corresponding INT2 and INT4 speedups are $2.67\times$ and $2.30\times$ over FlashInfer BF16, $1.48\times$ and $1.28\times$ over TensorRT-LLM FP8, and $1.16\times$ and $1.00\times$ over TensorRT-LLM NVFP4. We integrate FOSCAR into SGLang to benchmark serving efficiency. On long-context serving workloads, FOSCAR increases peak aggregate throughput by up to 170% and 341% over 2-bit and 16-bit baselines, respectively. We open-source FOSCAR as a kernel library at this https URL.

---


### 145. [One Run Is Not Enough: A Monte Carlo Protocol for Evaluating LLM Reliability on Data Science Tasks](https://arxiv.org/abs/2611.09729)

**<font color=#1a73e8>作者：</font>** Wenqi Ni, Ozan Evkaya, Miguel de Carvalho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise for automating data science workflows. Benchmarks such as DataSciBench (2026) and StatQA (2024) have advanced the evaluation of their capabilities across data science and statistical tasks. Assessing their reliability requires examining both the quality of their responses and their consistency across repeated runs, task types, and difficulty levels. With this aim, we introduce DS-QA, a benchmark comprising 100 data science and statistics questions drawn from UK university courses, spanning 16 datasets and three difficulty levels. We develop a three-layer evaluation framework that combines general response properties (runtime, verbosity and text similarity), coarse-grained metrics (accuracy, code executability and completeness), and task-specific metrics. We evaluate OpenAI models using a Monte Carlo protocol with 100 repeated runs. The results reveal substantial variability in responses to data visualisation and supervised learning tasks, particularly at medium and hard difficulty levels, highlighting the importance of evaluating consistency alongside response quality. We also find that an increase of 0.1 in the word verbosity ratio corresponds to an increase of about 0.013 in the token verbosity ratio.

---


### 146. [Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration](https://arxiv.org/abs/2611.09740)

**<font color=#1a73e8>作者：</font>** Dario Scilla, Omar A. Lopez, Mattia Rosso 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shallow-water UAV imagery provides centimeter-scale observations of benthic environments, but water-induced distortions complicate interpretation. To our knowledge, we present the first systematic zero-shot benchmark of unified multimodal large language models (MLLMs) for both assessing water-induced distortions and restoring shallow-water imagery within the same model framework. We evaluate five open-weight unified MLLMs with frozen pretrained weights and without access to paired reference images or descriptions of the true seabed. The benchmark contains 1,000 image pairs: 600 semi-synthetic UAV scenes created by applying synthetic water distortions to real shallow-water imagery and 400 fully synthetic through-water scenes. Three independent human annotations cover five distortion types. We evaluate four assessment prompts (P0-P3), from direct instruction to structured task decomposition, on all 1,000 images and four diagnosis-guided restoration prompts (R0-R3) on a common 100-image subset. Assessment varies substantially by model and prompt, with systematic prediction biases and a best pooled balanced accuracy of 0.654 for distortion presence. The best pooled PSNR gain is +0.255 dB, no unified MLLM improves pooled LPIPS, and some outputs alter scene structure or hallucinate content. Two restoration-only baselines also show limited transfer: InstructIR achieves a pooled PSNR gain of +0.040 dB, while PromptFix degrades all four pooled metrics under every prompt. These results show that recognizing shallow-water degradation does not imply reliable physical restoration and provide a reproducible baseline for future work.

---


### 147. [A Tight Hierarchy for Chain of Thought](https://arxiv.org/abs/2611.09759)

**<font color=#1a73e8>作者：</font>** Thanh Le, A. Pavan, N. V. Vinodchandran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning has emerged as a powerful paradigm for extending the computational capabilities of transformer-based models. A growing body of recent work has begun to uncover the fine-grained computational power of transformers augmented with CoT, as well as their connections to classical complexity theory.
In this work, we advance this line of research by establishing the first hierarchy theorem for CoT-based computation. Our main result shows that for any reasonable resource bound $r(n) \geq n$ and any $\varepsilon > 0$, \[ \mathrm{CoT}(r(n)) \subsetneq \mathrm{CoT}(r(n)^{1+\varepsilon}), \] where $\mathrm{CoT}(r(n))$ denotes the class of decision problems solvable by transformers using $O(r(n))$ CoT reasoning steps on inputs of length $n$. Our result shows that increasing the number of CoT reasoning steps provably yields strictly greater computational power, establishing CoT steps as a fundamental resource in transformer-based computation.
Unlike classical hierarchy theorems, which are typically proved via diagonalization, our approach leverages known coarse-grained simulations between CoT-augmented transformers and Turing machines in both directions. Building on these connections, we adapt the classical padding technique from complexity theory to this setting to obtain a tight hierarchy. A key technical contribution of our work is the implementation of padding within the transformer-based CoT model.

---


### 148. [Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents](https://arxiv.org/abs/2611.09768)

**<font color=#1a73e8>作者：</font>** Yuchen Li, Lisa Liu, Runqi Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents coordinate through conversation, and the same message can be phrased in simpler or more complex language, bluntly or politely. We test whether such differences change how other agents judge and act, using the LURK Werewolf framework, which separates each utterance's speech-act predicate from its natural-language realization. We rewrite only the realization, check that the game content is preserved, and replay each game day from saved checkpoints against a re-sampled control. We vary linguistic range consistently across a speaker's messages and politeness strategy per utterance. Across 30 games and 4,335 replays, neither manipulation changes the trust other agents place in the speaker, and no effect on votes or night actions survives correction for multiple comparisons; the largest uncorrected effect is that shifting range away from a neutral paraphrase changes about 4 percentage points more of the other players' votes. In natural play, 88% of face-threatening speech is bald on-record regardless of role.

---


### 149. [ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models](https://arxiv.org/abs/2611.09770)

**<font color=#1a73e8>作者：</font>** Lingyun Song, Ziyao Chen, Kang Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) require continuous factual updates to stay current, yet lifelong knowledge editing remains a daunting challenge. The primary obstacle is the severe Locality Erosion and Catastrophic Forgetting, where sequential edits inevitably interfere with pre-trained capabilities and prior updates. In this paper, we propose \textbf{ROSE}, a \textbf{R}isk-aware \textbf{O}rthogonal \textbf{S}ubspace navigation framework for lifelong knowledge \textbf{E}diting. ROSE addresses forgetting by aiming to restrict parameter updates to the orthogonal complement of previously edited subspaces. Crucially, it introduces a risk-guided mechanism that utilizes a dynamically computed risk mask to safeguard specific factual parameter subspaces essential for model stability. During inference, ROSE employs a multi-granularity knowledge integration strategy, featuring prototype-anchored semantic gating and perturbation-driven subspace fusion to precisely activate edited knowledge for relevant queries while limiting interference on unrelated inputs. Comprehensive experiments on two prominent multimodal benchmarks show that ROSE is competitive with state-of-the-art approaches across five key metrics, while maintaining outstanding stability over $1,000$ sequential updates. Our code is available at this https URL.

---


### 150. [Are These Programmers Ripe Enough to Eat? Evaluating How LLMs Handle Lexical Knowledge Conflicts in Translation](https://arxiv.org/abs/2611.09785)

**<font color=#1a73e8>作者：</font>** Dongxu Wu, Sara Court, Micha Elsner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> External lexical resources can help large language models (LLMs) translate texts in low-resource languages and specialized domains, but these resources may conflict with models' prior lexical knowledge. To isolate this conflict, we construct a controlled Mandarin-to-English translation task in which familiar source words are assigned new meanings within and across semantic categories. We treat these prompt-supplied meanings as contextual knowledge (CK) and systematically evaluate the effects of word frequency, sentence context, and prompt framing on the translated outputs. Across nine models, CK reliance is greater for less frequent source words and in sentence contexts that support the supplied meanings. Prompt framing can reduce CK reliance, but seven of nine models favor CK even when explicitly instructed to ignore the supplied meanings. Within model families, larger models are more likely than smaller models to utilize CK in their outputs. Three follow-up experiments further show that modal weakening lowers CK reliance, the effect of repetition depends on prompt layout, and the effect of reasoning varies across models. Overall, our controlled study reveals how CK reliance varies across conditions and models, motivating new methods to detect and evaluate lexical conflicts and guide models' lexical choices in LLM-based translation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-174](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
