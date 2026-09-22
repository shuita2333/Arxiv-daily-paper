# 🧠 大模型相关研究 | 2026年09月23日

> 本类共 **379** 篇论文：已确认 **359** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-379](./part-08.md)

---

### 301. [Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection](https://arxiv.org/abs/2609.24359)

**<font color=#1a73e8>作者：</font>** Xianlong Li, Pietro Bongini, Niccoló Pancino 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image forensics is increasingly an open-world problem: manipulations range from fully synthetic images to localized edits, splicing and swapping, while most forensic detectors remain specialized to a single manipulation family. Agentic AI has recently emerged as a promising solution. In principle, such systems can assess the reliability of individual detectors, identify out-of-scope evidence, and arbitrate conflicting reports. However, it remains unclear which components actually drive performance and whether their benefits persist under distribution shift. To answer these questions, we study a training-free agentic framework built around specialist detectors, per-detector triage, and conflict-aware evidence arbitration. Using six configurations and three multimodal large language model backbones, we dissect the role of triage, prompting, and reasoning quality on both in-distribution and out-of-distribution data. Our results show that naive detector fusion suffers from severe false-positive rates on authentic images. Triage and prompting consistently improve performance by filtering unreliable evidence and exposing detector limitations. However, the dominant factor is represented by reasoning itself: A stronger judge substantially outperforms a weaker one, particularly under distribution shift. Most notably, manipulation recall is nearly saturated across all configurations, indicating that the main challenge of open-world image forensics is not detecting manipulations, but calibrating trust in specialized forensic tools and arbitrating conflicting evidence.

---


### 302. [VLM-in-Sandbox: Visual Workspaces for Agentic Visual Reasoning](https://arxiv.org/abs/2609.24362)

**<font color=#1a73e8>作者：</font>** Hexiong Yang, Mingrui Chen, Jie Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sandboxed computer environments support multi-step reasoning with tools, executable programs, and persistent files, yet their extension from language models to vision-language models (VLMs) introduces a distinct state-management problem. Visual reasoning produces intermediate image-valued evidence---crops, masks, overlays, zoomed regions, and analytic renderings---that must remain addressable without accumulating unboundedly in multimodal context. We introduce VLM-in-Sandbox, a training-free framework for agentic multimodal reasoning in controlled computer environments. Its Visual Workspace registers generated artifacts in an image ledger, maintains a bounded active visual context, and lets the model explicitly promote selected evidence for subsequent inspection. This separates visual evidence generation, performed by sandbox tools, from visual evidence management. Across seven benchmarks and four base VLMs, VLM-in-Sandbox achieves the highest sample-weighted average accuracy among Vanilla VLM, Append-only Sandbox, and the proposed method. A compiler-matched $2\times2$ study on 1,260 examples further separates model-directed visibility from bounded retention: VLM-in-Sandbox reaches 66.27% accuracy with 18.6% fewer total tokens than the automatic, retain-all control. Over all 6,350 submitted GPT-4.1-mini examples, it produces 302 rescues and 142 regressions relative to Original Append-only. A local vLLM study with prefix caching confirms that the smaller request workload also reduces uncached tokens, time to first token, and end-to-end latency. These results identify explicit visual evidence state as a central abstraction for sandboxed VLM agents.

---


### 303. [DeceptionAnalyser: A Web-Based AI Tool for Performing Structured Deception Analysis with Argumentation Schemes and LLMs](https://arxiv.org/abs/2609.24369)

**<font color=#1a73e8>作者：</font>** Stefan Sarkadi, Xabier Garmendia, Jack Mumford 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Deception plays a central role in Intelligence operations, yet it remains difficult to analyse systematically without expert knowledge of reasoning patterns and cognitive manipulation. In computational argumentation, for instance, no scheme-level ground-truth corpora currently exist to support statistical validation. In this paper, we address this by introducing a set of ten argument schemes designed to model distinct forms of deception, each accompanied by structured premises and critical questions. In doing so, we introduce the first dedicated library of argumentation schemes specifically designed for deception analysis, providing a structured foundation for systematically modelling and analysing deception in narrative text. We then present \textit{DeceptionAnalyser}, a browser-based tool that implements these schemes through a two-stage methodology combining LLM-based premise extraction with critical-question-driven evaluation. Our aim is to provide a conceptual and methodological foundation for analysing deceptive reasoning in narrative text. This is precisely what we address in this paper by demonstrating how structured argumentation theory and AI-assisted analysis can support transparent, explainable assessments of potential deception. Because the schemes are designed to flag claims for scrutiny rather than to output a deception verdict, we do not benchmark classification accuracy; instead, we assess the \emph{reliability} of the methodology by measuring the consistency of the tool's premise and conclusion assessments across ten contemporary large language models and repeated runs. We find that scheme detection is highly stable for clear-cut deception and degrades gracefully, in interpretable ways, on more ambiguous intelligence-style narratives.

---


### 304. [URA-NER: A Unified Retrieval-Augmented Framework with Retrieval Alignment and Uncertainty Reduction for Low-Resource NER](https://arxiv.org/abs/2609.24372)

**<font color=#1a73e8>作者：</font>** Jingyu Wang, Shijie Wu, Fusheng Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) based on large language models (LLMs) has shown promising potential in alleviating performance bottlenecks caused by the limited availability of annotated data in Named Entity Recognition (NER). However, existing methods still face issues of retrieval misalignment and generation uncertainty, making their performance heavily dependent on the LLM's capabilities. As the parameter scale of LLMs decreases, their performance in few-shot settings deteriorates significantly. In this paper, we propose a novel unified retrieval-augmented framework, URA-NER, including three key components: Progressive Granularity Retrieval (PGR), Model-aware Representation Enhancement (MaRE), and Reason-aware Knowledge Verification. PGR is a two-stage retrieval mechanism that achieves stage alignment. It first retrieves demonstrations for span detection based on the query's global semantics, and then for type classification based on the specific entity context, providing fine-grained local information. Moreover, MaRE employs entity pre-recognition to guide the construction of representations, ensuring the query and demonstrations are aligned within the LLM's semantic space and attention pattern. In addition, to mitigate generation uncertainty, we propose RaKV, a closed-loop "generation-retrieval-verification" process. It explicates the LLM's reasoning paths, leverages them for the retrieval of external knowledge, and reorganizes the knowledge into verification evidence aligned with the original reasoning paths. We conduct extensive experiments on multiple low-resource NER datasets. Results demonstrate that URA-NER significantly enhances the performance of LLMs under low-resource settings, with particularly pronounced gains for smaller LLMs, achieving new state-of-the-art results on several benchmarks.

---


### 305. [Information-Time Proximal Policy Optimization](https://arxiv.org/abs/2609.24380)

**<font color=#1a73e8>作者：</font>** Yongcheng Zeng, Xinyu Cui, Yan Song 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RLVR has substantially improved the reasoning capabilities of LLMs. However, existing methods typically parameterize temporal progression in the Markov Decision Process by token-by-token generation, despite the highly non-uniform information flow along autoregressive trajectories. In this paper, we propose InfoPPO, which reparameterizes temporal progression using information density rather than raw token count. This reparameterization induces a common state-dependent structure for both temporal credit propagation and policy updates. InfoPPO restores the effectiveness of non-trivial discounting in long-horizon reasoning, retaining effective-horizon contraction while avoiding excessive attenuation of terminal supervision over long token sequences. Moreover, the information-time policy-improvement analysis naturally leads to a state-dependent update constraint, which we implement through adaptive clipping. By adapting the clipping threshold at each token position to the information density of its corresponding state, this mechanism enables more targeted policy updates while preserving proximal control. Theoretically, we extend performance-difference and policy-improvement analyses to the information-time MDP, deriving a policy-improvement lower bound when policy changes are regulated by information density. We further connect the general information-time analysis to practical LLM policy optimization by relating state-wise information density to local policy movement, while also providing theoretical grounding for the adaptive update mechanism. Experiments on Qwen3 models demonstrate consistent gains over competitive baselines across five challenging competition-style mathematical reasoning benchmarks. InfoPPO also maintains stable accuracy and response length across non-trivial discount settings under which token-time PPO deteriorates.

---


### 306. [DeCo: Efficient Decouple-to-Couple Learning for Multi-Task Visual Grounding](https://arxiv.org/abs/2609.24409)

**<font color=#1a73e8>作者：</font>** Xiaoqiang Lu, Licheng Jiao, Long Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task visual grounding requires models to jointly understand linguistic semantics and perform accurate visual localization and segmentation. Despite the success of multimodal large language models, effectively adapting them to multiple grounding objectives remains challenging. Existing methods commonly enforce task cooperation through shared representations, while overlooking the intrinsic conflict between task-oriented feature interests. In this paper, we introduce $\textbf{DeCo}$, an efficient $\textbf{De}$couple-to-$\textbf{Co}$uple learning framework that resolves this dilemma through a two-stage paradigm: task-specific representation decoupling followed by complementary prior coupling. Specifically, we first propose Task-aware Semantic Decoupling (TSD) to route shared visual cues into individual features under salient word-level guidance, alleviating representation interference between localization and segmentation. Furthermore, we observe that segmentation naturally provides informative localization priors due to dense supervision. Based on this insight, we introduce Hybrid Prior Coupling (HPC), which integrates sentence-level semantic prior with mask-derived spatial prior for enhanced grounding. Built upon a frozen multimodal encoder, DeCo requires lightweight trainable parameters while achieving strong generalization across multiple grounding objectives. Extensive experiments on RefCOCO/+, G-Ref, ReferIt, Flickr, DIOR-RSVG, SARVG1.0, RRSIS-D, RIS-LAD, and RefDIOR demonstrate that DeCo achieves state-of-the-art performance on both natural and remote sensing benchmarks. The code and models are available at this https URL.

---


### 307. [ARM: Attention with Routed-Memory for Learnable Sparse Control](https://arxiv.org/abs/2609.24417)

**<font color=#1a73e8>作者：</font>** Qiuhao Zeng, Jerry Huang, Peng Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite advances in long-context inference, large language models (LLMs) remain fundamentally limited by the key-value (KV) caching mechanisms that are necessary for stable computation. Techniques such as selective token eviction and pruning have vastly mitigated these issues, but often discard core information to manage the growing cache. In this paper, we propose Attention with Routed Memory (ARM) a novel KV caching structure that introduces a fully differentiable, fixed-size memory system organized as a hierarchical router. Via a Gumbel-Softmax, ARM learns to select memory slots and perform sigmoid-gated updates that softly combine new and stored information, avoiding hard eviction and reducing information loss. By further training a policy to dynamically select varying amounts of memory at inference, ARM adapts its accesses for both simple contexts and inputs that require deeper reasoning, enabling more scalable and effective retrieval on both short- and long-contexts. Experimental results on standard commonsense and long-context reasoning benchmarks demonstrate that ARM achieves superior performance and efficiency compared to fixed KV-caching approaches, while remaining efficient and scalable in terms of both memory and generation latency.

---


### 308. [1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation](https://arxiv.org/abs/2609.24432)

**<font color=#1a73e8>作者：</font>** Huanxin Sheng, Zhiling Ye, Haonan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse on-policy distillation (OPD) allocates teacher supervision to a small subset of tokens in student-generated trajectories. However, useful teacher guidance can yield a noisy update when its gradient is estimated from a sampled next token. We study this estimation problem at a fixed prefix in information geometry and propose an information-efficiency ratio (IER) based on a signal-to-noise decomposition. IER characterizes relative gradient estimation error under an optimal scalar baseline. A candidate-set approximation enables token selection based on IER and its combination with existing usefulness scores, while retaining the sampled reverse-KL training objective. On mathematical and medical reasoning tasks, adding IER improves existing selectors in multiple settings, with sparse configurations matching or exceeding full OPD without token selection at small token budgets of 0.1\%--1\%. These results support accounting for both usefulness and gradient-estimation reliability when allocating sparse supervision. Our code is available at this https URL.

---


### 309. [ActGov: Governing LLM Agent Actions via Policy-Constrained Validation](https://arxiv.org/abs/2609.24446)

**<font color=#1a73e8>作者：</font>** Kaiyuan Zhang, Yuke Peng, Ke Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly execute long-horizon workflows through external tools, allowing untrusted outputs to influence subsequent actions and exceed user authorization. Existing defenses isolate injected content or constrain execution with predefined plans and static policies, but these approaches are brittle under dynamic workflows and scale poorly across extensible tool ecosystems.
In this work, we present ActGov, a runtime enforcement framework that validates each LLM-proposed tool action before it causes external effects. Built on a unified semantic model of authorization, actions, runtime context, and security constraints, the ActGov-Policy component iteratively constructs a policy set from tool specifications, benign tasks, and observed failure traces, with each update verified through SMT-based counterexample checking. At runtime, ActGov-Runtime abstracts each tool call into finite policy records and permits it only if it remains within the task-scoped authorization boundary and satisfies all applicable policies. This per-action enforcement preserves authorization throughout long-horizon, dynamically branching workflows.
We evaluate ActGov on the AgentDojo and AgentDyn benchmarks across multiple models and attack configurations. It shows that ActGov consistently reduces the success rate of indirect prompt-injection attacks while preserving task utility, significantly outperforming existing defenses. These results demonstrate that ActGov can enforce fine-grained authorization over dynamic agent executions without relying on the underlying LLM to correctly identify malicious instructions.

---


### 310. [Do LiDAR Language Models Really Understand Spatio-temporal Relationships?](https://arxiv.org/abs/2609.24452)

**<font color=#1a73e8>作者：</font>** Runyi Yang, Murat Akkoyun, Di Wen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 4D LiDAR language models aim to reason about objects and their evolving spatial relationships. Yet, in our evaluation, always selecting the same option nearly matches the multiple-choice accuracy of two B4DL-derived configurations. We introduce LiDAR-Hallu, a geometry-referenced benchmark and diagnostic protocol with 10,000 questions across 150 nuScenes scenes. It covers object existence, ego-relative position, distance ordering, relative motion, and temporal localization, with explicit rules for selecting objects, comparing times, and determining reference answers. Our protocol combines fixed-answer and candidate-content controls, cross-scene pairs with identical prompts but opposite reference answers, and relation-specific recall. Analysis of 100,000 recorded responses reveals failures hidden by aggregate accuracy. Candidate duration alone makes temporal answers predictable without observing LiDAR. On paired questions, the models frequently give the same answer to scenes requiring opposite answers. Relation-specific analysis further shows that both configurations miss every positive lateral-motion case across all tested conditions. Temporal-shuffle contrastive decoding provides little net improvement, as repairs are largely offset by new errors and the main failures persist. These results show that evaluating spatio-temporal reasoning requires testing whether models distinguish the queried physical relationships, rather than relying on individual-answer accuracy alone. The source code, checkpoints, and data are released at this https URL.

---


### 311. [RAILS: Retrieval-Augmented Incremental LLM Clustering at Scale](https://arxiv.org/abs/2609.24464)

**<font color=#1a73e8>作者：</font>** Armin Oliya, Aleksandra Sawczuk, Radosław Białobrzeski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Using a Large Language Model (LLM) as the clusterer at production scale is hard: prompts cannot hold the entire label space, and per-document serial processing does not deliver the throughput real workloads require. We present RAILS, a retrieval-augmented incremental LLM clusterer that turns clustering into a simple loop over a growing label pool and scales through document batching with bounded concurrency. On six public benchmarks RAILS exceeds the strongest prior LLM-clustering method on average, lifting accuracy from 51.2% to 59.3%, NMI from 67.2% to 74.8%, and ARI from 45.4% to 54.7%. We further report production-deployment evidence from a SaaS ticket-topic-discovery pipeline, where RAILS has replaced a traditional HDBSCAN stage with higher clustering quality, transparent prompt-driven control, and stateful incremental operation.

---


### 312. [A Temporal Knowledge Graph for Music Festival Lineup Forecasting](https://arxiv.org/abs/2609.24467)

**<font color=#1a73e8>作者：</font>** Julia Gastinger, Thilo Dieing, Christian Meilicke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Music festival lineups emerge from complex relationships among artists, genres, releases, labels, and past performances, making the prediction of future lineups a natural fit for temporal knowledge graph (TKG) forecasting. In this work, we present a TKG covering 380 festivals over 55 years, comprising more than 90K festival performance quadruples along with information on festivals, artist tours, and artist metadata, and release it as a resource for TKG forecasting evaluation. We formalize festival lineup forecasting as temporal link prediction between artists and festivals at future timestamps. We evaluate six TKG forecasting models on this task, analyze their capabilities and limitations, and compare them against Large Language Models applied zero-shot. Our resource complements existing TKG benchmarks by grounding evaluation in a concrete, real-world application domain.

---


### 313. [Spatial Action Review: A Visual Analytics Dashboard for Auditing Language-to-Action Hand-offs in Electron Microscopy](https://arxiv.org/abs/2609.24470)

**<font color=#1a73e8>作者：</font>** Samia Mohinta, Albert Cardona  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly explored as interfaces for scientific image analysis, where a visual question-answering (VQA) response may be paired with a spatial output that guides a downstream stage. A supervisor reads the language answer, while a downstream workflow such as segmentation or region review consumes the point-set output. We call this transition from inspecting the answer to relying on its point action the language-to-action hand-off. A silent failure occurs when the answer is correct while the paired action misses annotated objects needed downstream, so answer-based oversight clears a region whose action is unreliable. We introduce Spatial Action Review, a visual analytics dashboard for auditing this failure mode in electron microscopy (EM) mitochondria analysis. It links paired answer-action records through an answer-action ledger, a task-by-dataset risk map, and an image-region audit view, connecting aggregate patterns to image evidence while an adjustable action-reliability gate supports re-audit. The review ends in a human-AI hand-off, where a supervisor records whether the action is accepted, escalated, held under a stricter gate, or flagged for model revision. Across 541 image regions from an EM-adapted Qwen3-VL case-study run, point actions fail the gate in 54.4% of records with a correct VQA response, and 27.4% of all records are silent failures. A correct answer is associated with only a 5.8-percentage-point higher probability of a reliable action, with a bootstrap interval spanning zero; the point-biserial correlation between answer correctness and object coverage is 0.061. This weak coupling persists across five model conditions on 753 matched image regions. Spatial Action Review makes answer-action mismatches visible and ties them to image evidence and a recorded decision before MLLM outputs enter autonomous scientific workflows.

---


### 314. [Fathom-Vaidya: Advancing Medical Reasoning with Rubric-Based Rewards](https://arxiv.org/abs/2609.24480)

**<font color=#1a73e8>作者：</font>** Kalash Shah, Kunal Singh, Snehan J 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying Large Language Models (LLMs) in healthcare requires robust performance across two complementary dimensions - diagnostic reasoning: the convergent, evidence-driven task of inferring a patient's condition from clinical data to produce a diagnosis, and clinical healthcare reasoning: the broader, navigational judgment required to communicate, plan, and adapt across multi-turn clinical interactions where a single correct answer may not exist. Recent benchmarks such as HealthBench and MedXpertQA reveal persistent weaknesses in both areas, exposing failures in complex diagnostic scenarios and limitations in contextual, patient-centered dialogue. We introduce a sequential training framework that targets these facets using synthetic data and rubric-based reinforcement learning. First, we improve diagnostic reasoning using MedBullets-derived questions with rule- and rubric-guided Reinforcement Learning (RL). We then shift to clinical reasoning by generating 5.3k synthetic multi-turn scenarios, each paired with multi-dimensional rubrics to comprehensively assess the response. This approach yields over 10% improvement on MedXpertQA, and our 30B model achieves 50.1% accuracy on HealthBench-Hard, surpassing proprietary baselines including GPT-5 (thinking). Our results show that targeted synthetic datasets and rubric-based training can systematically improve both diagnostic and interactive clinical reasoning in medical LLMs.

---


### 315. [VPRune: Efficient Training-free Pre-LLM Visual Token Pruning](https://arxiv.org/abs/2609.24485)

**<font color=#1a73e8>作者：</font>** Guangchuan Lv, Dianxing Shi, Dingjie FU  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning is a promising approach to reducing the inference cost of large vision-language models (LVLMs), yet aggressive token reduction often causes substantial performance degradation. We identify three key factors behind this degradation: text-guided selection bias, information loss from discarded tokens, and positional distortion caused by sequence compaction. Based on these observations, we propose \textbf{VPRune}, a training-free pre-LLM pruning framework consisting of visual-only diversity selection, similarity-guided token recycling, and position-preserving restoration. Experiments on FastVLM-1.5B across multiple vision-language benchmarks demonstrate that VPRune achieves a favorable accuracy--compression trade-off, with particularly pronounced advantages under aggressive compression. Furthermore, evaluations on edge-device show that VPRune effectively reduces end-to-end inference latency while maintaining superior task performance, demonstrating its practicality for resource-constrained LVLM deployment.

---


### 316. [AgentSTAR: Agentic Shape Tracking and Reconstruction from Monocular Videos](https://arxiv.org/abs/2609.24487)

**<font color=#1a73e8>作者：</font>** Kirill Mazur, Nikita Karaev, Matthew Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we present a method for shape reconstruction and tracking from video via agentic analysis-by-synthesis. Unlike prior methods which first estimate dense pixel correspondences and then recover object motion from them, our method infers a structured 3D object model, including its geometry and kinematic structure, and uses this model to optimise object track estimates over time. In our optimisation loop, a Vision-Language Model (VLM) agent iteratively refines shape or generalised pose through a render-and-compare loop, combining coarse visual reasoning with numerical pose optimisation for precise state estimation. This structured formulation enables our method to track through large motion, articulation, and severe occlusion without relying on pixel-matching objectives. Quantitatively, on ARCTIC, our method substantially outperforms state-of-the-art 3D point-tracking baselines for articulated objects, and on HOT3D it outperforms all evaluated rigid-object tracking baselines.

---


### 317. [LLJ Cards: Best practices for the Use of LLMs as Judges](https://arxiv.org/abs/2609.24516)

**<font color=#1a73e8>作者：</font>** Khaoula Chehbouni, Melina Medjdoub, Florian Carichon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, large language models (LLMs) have emerged as a popular alternative for evaluation. Often referred to as LLMs as judges (LLJs), these systems have been widely adopted by researchers and practitioners across a broad range of measurement tasks, driven by their strong performance, scalability, and cost-effectiveness relative to human judgment. However, a growing body of work has shown that the use of LLJs raise concerns about their validity and reliability as evaluators. Existing efforts to address these challenges have largely focused on developing bias-mitigation techniques and refining prompting strategies. While these approaches represent an important step forward, they primarily offer technical fixes and leave a more fundamental challenge unaddressed: the lack of standardized, transparent, and reproducible evaluation practices. In this paper, we introduce LLJ Cards, a framework that synthesizes best practices from measurement theory, natural language generation, and machine learning literature into practical guidelines for LLJ-based evaluations. While LLJs offer a promising path toward scalable evaluation, their effective use requires grounding in rigorous evaluation principles to ensure validity, reliability, and reproducibility. LLJ Cards addresses this need by providing a structured framework for applying these principles in the design and reporting of automated evaluations.

---


### 318. [ME-VLM:A Unified VLM for Embodied Cognition and Agent Coordination](https://arxiv.org/abs/2609.24526)

**<font color=#1a73e8>作者：</font>** Foundation Model, Li Auto Inc  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical AI requires models to ground visual and linguistic understanding in real-world environments while accounting for environmental constraints and execution feedback. We introduce MachEmbodied-VLM (ME-VLM), a unified vision-language model with two variants, 4B and 35B-A3B, that brings together embodied cognition and multimodal agent capabilities. Our work emphasizes physical perception and spatiotemporal reasoning, together with planning, interaction, and outcome assessment in both digital and physical environments. We construct training data spanning embodied and multimodal agent tasks, including execution observations and feedback to support outcome assessment and decision refinement. The training pipeline comprises embodied capability injection, separate reinforcement learning of embodied and multimodal-agent experts, and multi-teacher on-policy distillation that consolidates their complementary capabilities into a single model. Experiments show competitive performance on both embodied and agent benchmarks, as well as on autonomous-driving and embodied-navigation tasks. For edge deployment, visual token compression, W4A8 quantization, and hardware--software co-optimization enable on-device inference of the 4B variant on the M100, reducing prefill latency from 400 ms to 188 ms.
Project Page: this https URL Code Repository: this https URL

---


### 319. [Prompting Against Persona Drift: Comparing Intervention Timing and Content in LLM-Simulated Conversations](https://arxiv.org/abs/2609.24532)

**<font color=#1a73e8>作者：</font>** Nicolas Leins, Jennifer Haase, Varvara Geronimus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Simulating student personas with large language models (LLMs) enables scalable evaluation of educational systems. However, behavioral drift, a progressive decline in persona consistency, can emerge over extended conversations, limiting the validity of such simulations. We evaluate five prompt-level mechanisms using separate monitoring and intervention pipelines. Across 1,200 28-turn conversations spanning four LLMs and two ADHD persona intensities, we varied when to intervene (static vs. adaptive) and what to inject (reinjection vs. reflective reminder), plus a novel adaptive condition in which a monitor generates behavior-specific instructions. Relative to no intervention, reinjection reduced the modeled rate of LLM-rated drift by 35--38\%, reflective reminders by 22--27\%, and behavior-specific instruction by 87\%. None eliminated drift. We found no evidence that adaptive timing outperformed static scheduling. Monitoring therefore appears more useful for deciding \textit{what} to correct than \textit{when} to intervene, although behavior-specific instruction requires component-level testing.

---


### 320. [QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation](https://arxiv.org/abs/2609.24538)

**<font color=#1a73e8>作者：</font>** Demian Pavlyshenko, Bohdan Pavlyshenko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Functional annotation of newly sequenced proteins remains a bottleneck in molecular biology: the number of sequences in public repositories grows far faster than the capacity for manual curation. Most computational approaches consider annotation as multi-label classification over a fixed ontology, which constrains predictions to a predefined label set. In this work we study the the protein annotation as a sequence-to-text generation problem. We fine-tune the 3B-parameter Ministral 3 base model with QLoRA (4-bit NF4 quantization with low-rank adapters) on sequence annotation pairs. We assess predictions with an LLM-as-expert protocol: a GPT model prompted as a senior molecular-biology curator scores organism identification as binary and function annotation quality. We conclude that QLoRA-fine-tuned compact LLMs can generate curator-style annotations with genuine biological value for a substantial subset of proteins. We also discuss future directions in data quality, model scaling, and evidence grounding that are needed to make the approach sufficiently reliable for practical use.

---


### 321. [State-Aware Fuzzing of JavaScript Engines with LLM-Guided Instrumentation](https://arxiv.org/abs/2609.24550)

**<font color=#1a73e8>作者：</font>** Wai Kin Wong, Dongwei Xiao, Anthony Cheuk Tung Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security of the modern web depends on the correctness of JavaScript (JS) engines, yet these complex systems remain vulnerable to high-impact bugs. A critical limitation of state-of-the-art fuzzers is the coverage plateau: once a fuzzer saturates the control-flow graph, edge coverage loses its ability to guide discovery. Because complex engine behaviors, such as JIT optimization tiers and hidden class transitions, often share identical edge coverage, standard coverage metrics are blind to the distinct internal states required to trigger deep errors.
To bridge this gap, we present StateLens, a framework that employs Large Language Models (LLM) to automate the discovery of deep internal states. Blindly placing instrumentation probes at all states is infeasible due to the vast state space and the high runtime overhead. StateLens introduces a novel agent-based reasoning pipeline that emulates the intuition of a security researcher. By iteratively traversing code and developer comments, our agents intelligently select high-value instrumentation targets, effectively separating logic-driving state variables from irrelevant data. This results in synthesizable, high-signal feedback probes that map the engine's hidden configurations. This instrumentation feeds a dual-feedback mechanism, effectively guiding the fuzzer toward unexplored engine semantics. Our evaluation confirms that StateLens significantly outperforms state-of-the-art fuzzers and uncovering 68 new bugs.

---


### 322. [HyperCLIP++: Fine-tuning CLIP forOpen-vocabulary Semantic Segmentation in Hyperbolic Space](https://arxiv.org/abs/2609.24564)

**<font color=#1a73e8>作者：</font>** Zelin Peng, Zhengqin Xu, Changsong Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP, a foundational vision-language model, has emerged as a powerful tool for open-vocabulary semantic segmentation. While freezing CLIP's text encoder is known to preserve its generalization capability, recent studies show that fine-tuning both CLIP's text and image encoders jointly significantly enhances segmentation performance, especially for classes from open sets. In this work, we explain this phenomenon from the perspective of hierarchy alignment, since during fine-tuning, the hierarchical level of image embeddings shifts from image-level to pixel-level. We achieve this by leveraging hyperbolic space, which naturally encodes hierarchical structures. Our key observation is that, during fine-tuning, the hyperbolic radius of CLIP's text embeddings decreases, facilitating better alignment with the pixel-level granularity of visual data. Building on this, we propose HyperCLIP++, a novel and parameter-efficient adaptation strategy. HyperCLIP++ directly adjusts the hyperbolic radius of CLIP's embeddings via scaling transformations to achieve a hierarchy alignment to the target task, i.e., segmentation. To ensure this hierarchy alignment is effected consistently across both modalities and preserves their cross-modal alignment during training, HyperCLIP++ integrates a Dual Cross-Relation Communication (DCRC) module that synchronizes these adjustments between the vision and text pathways. Our experiments show that HyperCLIP++ achieves state-of-the-art performance across three benchmarks while fine-tuning only approximately 5% of CLIP's total parameters. More importantly, we observe that after adjustment, CLIP's text embeddings exhibit a relatively fixed hyperbolic radius across datasets, suggesting that the hierarchical level required for this segmentation task might be quantified using the hyperbolic radius.

---


### 323. [Evaluating Decision Models for Text Annotation in Computational Social Science](https://arxiv.org/abs/2609.24574)

**<font color=#1a73e8>作者：</font>** Hazem Ibrahim, Yasir Zaki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational social science increasingly relies on large language models for text annotation, and the validity of published findings now rests on the labels generated by such models. Decision models, a new model class built for categorical question answering, answer typed questions with a choice, a probability distribution over the label set, and a confidence score rather than free text, at a small fraction of frontier inference prices. Whether their answers are accurate, and whether that stated confidence can be trusted on social science constructs, are unknown. Here, we mirror the evaluation of Ziems et al. (2024) on 18 computational social science classification tasks (7,977 items), comparing the first commercial decision model and two open-weight counterparts against 19 frontier and open-weight language models under the same zero-shot protocol. The decision model trails the per-task best LLM on 14 of 15 evaluation tasks, with a median deficit of 11.6 macro-F1 points, at a median 44 times lower measured cost. Its confidence is better calibrated than the verbalized confidence of 16 of the 19 LLMs, yet three frontier models show lower median calibration error (0.157 against 0.066). While items above 0.9 confidence are typically labeled accurately (median accuracy 0.815), on one task, empathy in peer-support dialogues, the model reports high confidence while performing near chance. Nonetheless, our results suggest that decision models are useful as a first step in the annotation pipeline: routing low-confidence items to an LLM matches or exceeds the LLM alone at a quarter to half of its cost.

---


### 324. [Video-based Surgical Skill Assessment Using Dynamics-and-Uncertainty-Aware Tree-based Gaussian Process Classifier](https://arxiv.org/abs/2609.24619)

**<font color=#1a73e8>作者：</font>** Arefeh Rezaei, Mohammad Javad Ahmadi, Amir Molaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proposed pipeline integrates a representation-flow convolutional neural network with a dynamics- and uncertainty-aware tree-based Gaussian Process classifier. In this framework, latent motion dynamics are exploited both as discriminative representations and as a source of input uncertainty, enhancing robustness against temporal variations and abnormal motion transitions. Compared with conventional deep learning approaches, the proposed strategy requires less training data and offers improved computational efficiency. To further improve classification performance, we introduce novel semantic-aware compound kernels that effectively capture semantic, flow, and dynamic information embedded in surgical video features. In addition, uncertainty-aware kernels are developed to strengthen the robustness and practical applicability of the compound kernel framework. The proposed method is evaluated on two benchmark datasets, namely the JIGSAWS and the Cataract-LMM (Capsulorhexis) datasets. Experimental results demonstrate strong performance across both datasets, including the LOSO and LOUO evaluation protocols on JIGSAWS, including the subject-independent LOUO protocol on JIGSAWS, on which the framework attains a mean accuracy of \ph{96.9}\%; results under the within-subject LOSO protocol are reported for comparability with prior work, achieving competitive accuracy while substantially reducing computational cost. Overall, the proposed pipeline provides an efficient and accurate framework for video-based surgical skill assessment.

---


### 325. [Augmented Hypothesis Testing with Persona-Based LLM Simulations](https://arxiv.org/abs/2609.24629)

**<font color=#1a73e8>作者：</font>** Ziyad Benomar, Aymen Al Marjani, Paul Missault 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A/B testing requires large sample sizes, long timelines, and significant costs. When auxiliary predictions of experimental outcomes are available from machine learning models, uncertain prediction quality precludes replacing human experiments entirely, yet these predictions may still contain useful signal. We propose a principled framework for learning-augmented hypothesis testing that leverages predictions of unknown quality to reduce sample sizes while maintaining statistical validity. Predictions naturally vary in granularity, from coarse aggregate signals to fine-grained individual-level estimates, and our framework addresses both ends of this spectrum: (1) for population-level directional predictions, where only a binary signal on the treatment effect sign is available, we use an asymmetric test and prove consistency and robustness bounds within the learning-augmented algorithms paradigm; (2) for individual-level predictions, we introduce Generalized PPI++ (GPPI), extending Prediction-Powered Inference to handle nonlinear prediction errors through higher-dimensional transformations. Both methods benefit from accurate predictions while remaining robust to inaccurate or adversarial ones. We validate our framework using persona-based LLM simulations, where AI agents equipped with user personas predict individual behavior, as a natural prediction source spanning both granularity levels. Experiments on four real-world datasets demonstrate that our methods, combined with persona-based predictions, substantially reduce experimental costs while preserving rigorous statistical validity.

---


### 326. [Written as a Record, Read as an Address: What a Forward Pass Leaves in an Operation's KV Cache](https://arxiv.org/abs/2609.24635)

**<font color=#1a73e8>作者：</font>** Lingfeng Wu, Behzad Shomali  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model reads an operation such as "Swap the contents of Box F and Box B", its forward pass writes keys and values for those tokens into the KV cache. Prior work on entity tracking establishes what models use: bindings are resolved at query time rather than stored as explicit latent state. We ask what they write at the operation span and how it is accessed. We split a forward pass into a frozen writer and a reader: the writer's cache is recomputed without gradients, while the reader sees only the instruction and operation tokens, with all state descriptions hidden, and is trained in isolation. Anything the reader recovers was therefore already present in the unmodified cache. On a synthetic boxes task, a base reader recovers $\leq 0.06$ of queried bindings against $0.75$--$1.00$ after training, and recoverability tracks the operation's read/write footprint. We find two modes of access. Across Llama-3.1-8B and Mistral-7B, operation-span transplants causally redirect which visible state is read even when the two worlds hold identical values, revealing a routing record. Isolation training preserves routing and adds direct access to the payload, the value the operation read, from the single operand-name token in a narrow mid-depth band (layers 12--15 of 32 in Llama-3.1-8B, 14--17 in Mistral-7B) --- the same site that holds the routing record. The same recipe extends to further operations, ToMi and GSM8K, but is bounded by training coverage and costs open-book accuracy. Operation tokens thus leave localized, causally recoverable records that support both routing and direct payload access, though the model that writes them reads mainly the address they carry and not the value.

---


### 327. [Annie, Are You Okay? How Style- and Context-Based Personalization Shape AI-Assisted Decision-Making](https://arxiv.org/abs/2609.24644)

**<font color=#1a73e8>作者：</font>** Hasibur Rahman, Benjamin R. Cowan, Smit Desai  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As people turn to generative AI for financial advice, these systems can personalize how they communicate and what they say. Whether these forms of personalization shape decisions differently remains unclear. We conducted a preregistered 2 x 2 between-subjects factorial experiment (N=240): participants ranked three comparably viable stocks, discussed them with an AI, and reranked them. Participants perceived both forms of personalization, but only context-based personalization reliably changed ranking behavior: it increased reconsideration and moved rankings toward the AI's assigned recommendation. Participants felt more influenced without judging the AI as more correct, trustworthy, intelligent, likeable, or high-quality. Those initially farther from its recommendation moved more toward it while judging its advice less correct; exploratory analyses suggest greater susceptibility among lower-expertise participants. These findings show how personalized AI can steer decisions among defensible options with only a minimal evaluative trace, raising concerns for the design and governance of personalized decision support.

---


### 328. [iSDFT: Information-Proximal Self-Distillation for Continual Learning in LLMs](https://arxiv.org/abs/2609.24646)

**<font color=#1a73e8>作者：</font>** Ahmed Khaled Khamis, Xiaotong Ji, Hassan Jaber 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation fine-tuning (SDFT) learns new skills from demonstrations while reducing forgetting, but it always distils toward the full demonstration-conditioned teacher. This fixes teacher influence at the full-teacher endpoint, providing no control over how much demonstration information should be transferred at each prediction state. We introduce Information-Proximal SDFT (iSDFT), which instead treats the teacher as a budgeted source of information. At each token, iSDFT selects the distribution closest to the current student that satisfies a prescribed teacher-information constraint, yielding a closed-form exponential target with a locally determined tilt. To control cumulative drift, we further anchor the student to its frozen base policy. Across four heterogeneous LLM backbones and two specialisation tasks, iSDFT improves vanilla SDFT in 7 of 8 model-task settings and matches it in the remaining one. It also provides tighter retention on the original SDFT benchmark suite, with 73% of evaluations remaining within 0.5 points of the base model versus 52% for the strongest baseline, while achieving the largest mean improvement on all ten additional mathematics, coding, and competition-mathematics benchmarks. These results show that controlling how much and when teacher information is introduced improves specialisation while preserving broader capability.

---


### 329. [Assessing Readability with LLMs: The Role of Reasoning and Few-Shot Prompting](https://arxiv.org/abs/2609.24650)

**<font color=#1a73e8>作者：</font>** Raphaël Thieffry, Matej Martinc  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Readability assessment is essential for tailoring texts to intended audiences across educational, healthcare, and information retrieval domains. However, traditional readability formulas struggle to generalize across genres and languages, while supervised machine learning models rely on scarce, domain-specific annotated corpora, limiting their applicability--particularly for less-resourced languages. Large Language Models (LLMs) offer a highly scalable, multilingual alternative that requires no task-specific training, yet the impact of advanced prompting strategies on their performance remains underexplored. In this paper, we conduct a systematic benchmark of diverse open-source LLMs for multilingual readability assessment, focusing on the prediction of discrete readability levels required by educational frameworks. In addition to English, we evaluate our approach on a less-resourced language, Slovenian, to establish whether LLMs remain effective in low-resource settings. Specifically, we investigate the influence of explicit reasoning, demonstrating that Chain-of-Thought (CoT) prompting and reasoning-oriented models yield significant improvements over direct answering. Furthermore, our exploration of few-shot in-context learning reveals that providing just one labelled example per category (1-shot) substantially enhances prediction quality compared to zero-shot settings, with additional examples offering diminishing returns. By comprehensively comparing these approaches against traditional unsupervised metrics and state-of-the-art supervised baselines, we establish the viability of out-of-the-box LLMs as robust, cross-lingual readability assessors.

---


### 330. [TimeLitmus: A Diagnostic Benchmark for Cross-Modal Understanding and Explanation Faithfulness in Event-Conditioned Time-Series Prediction](https://arxiv.org/abs/2609.24677)

**<font color=#1a73e8>作者：</font>** Jie Gong, Maowei Jiang, Zhiwei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to make predictions from numerical time-series histories and textual events. Yet accuracy alone cannot reveal whether correct answers reflect effective integration of the two inputs or instead arise from event polarity, unimodal priors, or superficial cues. Likewise, plausible explanations may rationalize predictions without faithfully reflecting the evidence that drives model behavior. We introduce TimeLitmus, a diagnostic benchmark for cross-modal understanding and explanation faithfulness in event-conditioned time-series prediction. TimeLitmus contains 4,856 evaluation records across Finance and Traffic, combining natural prediction with controlled counterfactual and contrastive interventions, explanation-targeted faithfulness tests, and systematic shortcut controls. Across ten representative LLMs, standard prediction accuracy substantially overstates reliable cross-modal understanding: Hard Paired Contrast (HPC) pair correctness peaks at only 19.2% in Finance and 11.7% in Traffic, and all ten models show lower-than-expected consistency on Finance series-side controls. Models often recognize scenario relations explicitly yet fail to apply them during independent prediction. Explanation faithfulness shows a similar gap: in Traffic, most models cite the manipulated temporal factor in over 90% of cases, while behavioral support remains below 22%. Human annotators outperform LLMs on matched controlled and hard-pair diagnostics, confirming that these distinctions are recoverable from the inputs. Natural-only adaptation yields selective gains in evidence selection and input sensitivity, but not consistent gains in controlled or hard-pair behavior. The benchmark, evaluation suite, and supervised adaptation data will be released publicly.

---


### 331. [Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient Inference](https://arxiv.org/abs/2609.24698)

**<font color=#1a73e8>作者：</font>** Changxu Liu, Zhaogeng Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency. Unlike linear speculation, which follows a single candidate chain, tree-structured speculation retains multiple branches from shared prefixes; under the same budget, this broader coverage can improve acceptance and efficiency. Adapting it to DeepSeek-V4 is nontrivial: its CSA/HCA online compressed attention concentrates the difficulty on the target-verify side, where branches diverging from a shared prefix compress into different states, breaking cross-branch state consistency. We integrate tree-structured speculative decoding into the DeepSeek-V4-Flash pipeline via branch-aware causal verification, temporary state isolation, and accepted-path state refresh, keeping verification and compressed-state updates consistent across branches. Across budgets D=5 to D=8, batch sizes 1 to 64, and three datasets (GSM8K, MBPP, ShareGPT), tree speculation achieves a higher accepted length than the matched linear configurations in all settings (e.g., at D=8 about 2.83--3.41 versus 2.39--2.84) and improves throughput in nearly all configurations---marginal only at the smallest budget---by up to about 18.5%. More importantly, the gains follow stable, transferable regularities: the relative gain grows with the budget and is most pronounced for less predictable workloads at small-to-medium batch sizes, while beyond a certain budget throughput plateaus and decouples from the still-rising accepted length. These results show that retaining multiple candidate paths under the same budget can effectively improve DeepSeek-V4 decoding efficiency, and offer experience for adapting speculative decoding to future models with compressed, sparse, or structured context representations.

---


### 332. [Reasoning Topology Matters: A Controlled Study of LLM-Based Cybersecurity Analysis](https://arxiv.org/abs/2609.24710)

**<font color=#1a73e8>作者：</font>** Jiling Zhou, Aisvarya Adeseye, Antti Hakkala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in cybersecurity, where accurate analysis often requires multi-step and context-dependent reasoning over complex and heterogeneous data. However, existing prompting approaches typically focus on eliciting reasoning without explicitly considering how intermediate reasoning steps are structurally organized. We introduce Security Reasoning Topology, which models reasoning through three representative structures: Linear, Branching, and Graph. To evaluate their effects, we conduct controlled experiments on three cybersecurity datasets covering MITRE ATT&CK network traffic, cyber threat intelligence (CTI), and CVE vulnerability analysis. We evaluate multiple LLMs, including Llama 2 (7B, 13B, 70B), GPT-5.1, and Mistral Large 3, while keeping task inputs consistent and controlling reasoning structure through system-level prompting. Results show that reasoning topology substantially affects performance: Graph reasoning achieves the highest overall accuracy, improving over few-shot prompting by 9.8-12.2 percentage points across datasets, while Branching provides a strong intermediate solution. The results further show that the effect of reasoning topology remains consistent across model families and scales, highlighting reasoning topology as an important design factor for LLM-based cybersecurity analysis.

---


### 333. [World State Generator](https://arxiv.org/abs/2609.24744)

**<font color=#1a73e8>作者：</font>** Sungheon Jeong, Sanggeon Yun, Ryozo Masukawa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents solve complex tasks through plans and actions. A single step the world refuses puts the goal out of reach, and what the agent does next decides the task. Prompted planners fail at exactly this point, rewriting the refused step in new words, meeting the same refusal, and burning the attempt budget without moving. They fail because the plan was never tied to the world, so a refusal has nothing in the plan to attach to. A world is where a task runs, and it has its own rules, its own admissible actions, and its own constraints. We build synthetic worlds across 7 domains and extract training data from them. A program enforces each world's rules and grades its goal, and every world is admitted only if its goal is reachable from its initial state. Agents run inside and leave verified failures paired with repairs that carried the run to a state the world certified, a record of about 226K trajectories. On this record we train the World State Generator, a model that writes a plan as checkable states of the world and keeps that plan aligned with the world it runs in. That alignment is what a plan written in language lacks, since the world it runs in has physical limits, logical dependencies, and required orders the language never states, and the plan encounters these rules only when a state fails. WSG takes that failure as the rule the world has stated and rewrites the remaining states to obey it, so the plan bends to the world as the run goes on. Across 7 public benchmarks, WSG raises end-to-end success for two open models near 30B parameters over prompting and brings to the level of proprietary model.

---


### 334. [Construting Reverse Thinking: Developing Large Language Models' Reverse Thingking Ability](https://arxiv.org/abs/2609.24760)

**<font color=#1a73e8>作者：</font>** Xin Liu, Yunhai Li, Chunfu Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When facing complex problems, humans tend to try various ideas for different issues. Human thinking patterns exhibit remarkable flexibility in adapting to diverse scenarios. GPT-o1, GPT-o3, and DeepSeek-R1 adopt long chain-of-thought models to address complex problems by increasing reasoning depth, which default to a forward reasoning mode. We conducted statistical analysis on the accuracy of different mathematical problem datasets on models of different scales, and found five reasons for errors: Insufficient solution-space coverage, Computational mistakes, Unverified assumptions, Ignoring constraint conditions, Maximum response length limitation. To address the above issues, we proposed a backward reasoning pattern construction method aimed at enhancing the model's reverse thinking ability and dynamic adaptability. First, we constructed an easy-hard two-stage Math dataset for training large models and gradually improving their inference ability at different difficulty levels. The dataset contains forward reasoning paths as well as backward reasoning paths. And a two-stage supervised fine-tuning process is applied to progressively train the model's backward reasoning capability. Furthermore, a fine-grained reward mechanism is developed, employing smoothed reward signals to strengthen the model's ability to autonomously select thinking modes during the reasoning process, thereby avoiding reward hacking. A linear-decay balanced sampling strategy is designed to maintain a balance between forward and backward reasoning path samples during training, enabling the model to converge quickly and stably. Experimental results show that our method significantly improves reasoning efficiency and accuracy in tasks such as mathematical proofs, offering a flexible and efficient reasoning paradigm for solving complex problems.

---


### 335. [PrismGPT: Proxy-Guided Learning for Region-Aware Photo Editing with Self-Synthesized Reasoning](https://arxiv.org/abs/2609.24768)

**<font color=#1a73e8>作者：</font>** Ke Zhao, Hue Nguyen, Abhijith Punnappurath 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Professional photo finishing relies on both global adjustments and region-specific local edits guided by semantic masks, yet current automated methods handle this workflow only partially. We present PrismGPT, a Vision-Language Model (VLM) framework that produces structured, region-aware editing plans from a single input image without relying on commercial black-box tools. Training a VLM to simultaneously diagnose aesthetic deficiencies at both global and local levels while predicting precise editing parameters is challenging due to the vast combinatorial decision space. We address this through proxy-guided learning: two simpler proxy tasks -- operation decomposition and region-aware aesthetic ranking -- teach the foundational skills the model needs, while a competence-based dynamic scheduler automatically rebalances the multi-task training ratio, progressively shifting emphasis from the proxy tasks to the primary editing task as each skill is mastered. Crucially, all reasoning traces used for supervised fine-tuning are self-synthesized by the same base model, eliminating the need for a stronger external teacher. Experiments on MIT-Adobe FiveK and SPIRE, a new professionally retouched benchmark we introduce, show that PrismGPT achieves state-of-the-art results while using only ~6% of the training data compared to the previous best method.

---


### 336. [When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs](https://arxiv.org/abs/2609.24799)

**<font color=#1a73e8>作者：</font>** Yeji Kim, Mi-Young Kim, Randy Goebel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) enables efficient deployment of large language models, and PTQ methods are usually optimized and evaluated with generic reconstruction, perplexity, or answer accuracy. But in explanation-critical domains, preserving only the final answer may be insufficient, since users may also inspect generated rationales to judge whether a prediction is trustworthy. We study this issue in medical multiple-choice question answering, where rationales should provide evidence that supports the selected answer.
We propose an explanation-aware objective for transformation-based PTQ. Our method builds an offline faithfulness cache from full-precision teacher rationales and uses it during optimization to preserve answer-supporting evidence tokens and evidence-conditioned answer behavior. We instantiate it on OSTQuant under W4A4KV4 quantization and evaluate four 7B--8B medical and instruction-tuned LLMs on MedExQA, MedExpQA, and ChallengeClinicalQA. While a same-calibration OSTQuant baseline preserves task accuracy, it can substantially weaken answer-supporting rationales. Our objective is to preserve the full-precision model's answer-supporting behavior rather than improve gold-label accuracy, and our method better preserves the full-precision model's answer behavior and rationale-to-answer support. These results suggest that PTQ for explanation-critical settings should evaluate preservation of answer-supporting evidence, not only answer accuracy. Code and evaluation scripts are available at this https URL.

---


### 337. [INTCORT: Training-Free Spatial Reasoning Enhancement for Vision-Language Models via Input Transformations and Confidence Routing](https://arxiv.org/abs/2609.24813)

**<font color=#1a73e8>作者：</font>** Haoran Sun, Jingqi Xu, Yanhui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated remarkable capabilities in multimodal tasks, yet they still exhibit poor ability in spatial reasoning. Existing training-dependent and training-free enhancement methods suffer from high computational costs with catastrophic forgetting and internal mechanism interference that compromises general capabilities, respectively. In this work, we first verify two key hypotheses: appropriate geometric image transformation and query-reversal transformation can recover incorrect spatial predictions, and correct predictions exhibit higher relation-token confidence than incorrect ones. Based on these findings, we propose INTCORT, a training-free spatial reasoning enhancement framework that constructs multiple inference views through input transformations and aggregates their predictions via relation-token confidence routing, without modifying the VLM's internal mechanisms. Experimental results on several commonly-used benchmarks demonstrate that INTCORT substantially improves spatial reasoning accuracy across diverse VLMs, achieving an average improvement of 10.01% over all models and benchmarks. Compared with prior works, INTCORT achieves superior performance with improvements of up to 25.01%.

---


### 338. [The Answer-Basin Representation Hypothesis: We Are Not Probing or Steering Concepts](https://arxiv.org/abs/2609.24821)

**<font color=#1a73e8>作者：</font>** Manjiang Yu, Hongji Li, Zihan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Linear Representation Hypothesis associates high-level concepts with directions in language models, but it remains unclear how these concept-related linear structures are organized within the model. We propose the Answer-Basin Representation Hypothesis: the probability measure induced over answers by the model's continuation distribution organizes these linear structures, with its statistics represented along linear directions shared across questions. All continuations yielding the same answer form an answer basin, whose mass is their total probability. These basin masses define the pushforward probability measure over answers. We posit that concept-related linear structure emerges from differences in the answer measure rather than being determined by changes in concept labels. Experiments across models and tasks link concept-consistent effects and their reversals in probing and steering to the alignment between concept labels and the answer measure.

---


### 339. [GRUET: Quantifying Uncertainty of Agentic Reasoning-and-Acting Processes](https://arxiv.org/abs/2609.24831)

**<font color=#1a73e8>作者：</font>** Shuang Liang, Xin-Yu Hu, Shao-Qun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents have attracted considerably increasing attention due to the power of executing both Reasoning and Acting (ReAct) in open and dynamic environments. The ReAct process typically exhibits a multi-turn trajectory in which one drives Large Language Models (LLMs) to generate both reasoning chains and task-specific actions in an interleaved manner. However, agents often suffer from significant uncertainty, where identical tasks yield divergent trajectories; trajectories with higher uncertainty often produce incomprehensible behaviors, severely undermining agent credibility. This work conjectures that such trajectory-level uncertainty frequently stems from cumulative turn-level reasoning uncertainty induced by LLMs; the latter often exhibits a collection of branches of divergent reasoning chains and their resulting actions. Built upon this, we present the Graph-based Reasoning UncErtainty in Trajectories (GRUET) method for the uncertainty quantification of ReAct, comprising turn-level reasoning uncertainty quantification and trajectory-level uncertainty aggregation; the former precisely quantifies reasoning uncertainty via modeling the reasoning space spanned by potential reasoning branches as a graph and then approximating the reasoning space complexity with graph complexity, while the latter employs simple aggregation strategies for quantifying the overall trajectory credibility. Empirical evaluations across nine LLMs and five benchmarks validate the effectiveness of our proposed GRUET in terms of selective generation performance, measured by AUROC, AUPRC, and AUARC.

---


### 340. [Extracting Arguments, Not Just Classifying Them: Instruction-Tuned LLMs for Generative Component Detection](https://arxiv.org/abs/2609.24855)

**<font color=#1a73e8>作者：</font>** Sofiane Elguendouze, Erwan Hain, Elena Cabrio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Argumentative component detection (ACD) is a core subtask of Argument(ation) Mining (AM) and one of its most challenging aspects, as it requires jointly delimiting argumentative spans and classifying them into components such as claims and premises. While research on this subtask remains relatively limited compared to other AM tasks, most existing approaches formulate it as a simplified sequence labeling problem, component classification, or a pipeline of component segmentation followed by classification. In this paper, we propose ITFACD, a novel approach based on instruction-tuned Large Language Models (LLMs) using compact instruction-based prompts, and reframe ACD as a language generation task, enabling arguments to be identified directly from plain text without relying on pre-segmented components. Experiments on standard benchmarks show that our approach achieves higher performance compared to state-of-the-art systems. To the best of our knowledge, this is one of the first attempts to fully model ACD as a generative task, highlighting the potential of instruction tuning for complex AM problems. Our code and the datasets used are openly available in the following GitHub repository.

---


### 341. [Small-world Networks of Agents Brainstorm AI Risks to Support Ideation](https://arxiv.org/abs/2609.24859)

**<font color=#1a73e8>作者：</font>** Ke Zhou, Edyta Bogucka, Daniele Quercia  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The ideation phase of participatory AI risk assessment often starts with a blank slate or a limited list of predefined risks, making it difficult to surface indirect or systemic harms. To address this limitation, we propose a three-stage ideation support tool. The tool complements participatory AI, rather than replacing it, and helps focus later engagement with affected communities. First, it dynamically discovers stakeholders depending on the given AI use and recursively expanding outward, allowing overlooked or indirect stakeholders to emerge. Second, it simulates these stakeholders with LLMs, connecting them into a network of a given topology, and having them ideate about risks. Third, it prioritizes risks using network centrality measures. In an initial evaluation, we found that betweenness centrality run through agents connected in a small-world network works best as it elevates risks raised by stakeholders who bridge disconnected groups, surfacing novel, systemic harms that traditional methods often miss. On an AI chatbot companion use case, this approach increased the novelty of the identified risks by approximately 1.1 points over single LLM brainstorming, and by 0.5 points over agentic LLM brainstorming, measured on a normalized five-point Likert scale, without reducing the plausibility or severity of the identified risks. To test whether our framework helps a human-led ideation session using the Futures Wheel approach, we divided 11 teams of non-western young chatbot users into two types: control (team) and treatment (team) in a participatory AI risk assessment. The control teams started from a list of risks generated by the 45 AI practitioners in the initial evaluation; the treatment teams started from a list generated by our framework. The treatment teams identified more risks overall, and more systemic, human-computer interaction, and environmental risks.

---


### 342. [SPHQuant: Efficient extreme low bit weight quantization for Vision-Language Models](https://arxiv.org/abs/2609.24875)

**<font color=#1a73e8>作者：</font>** Kewei Zhang, Zheng Chen, Haotong Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent foundation models are moving toward native multimodal Vision-Language Models (VLMs), making VLMs a central form of next-generation foundation models. However, their large language backbones make edge deployment difficult due to high memory footprint and memory-bound autoregressive decoding. Weight-only post-training quantization is a practical solution, but pushing VLMs to extreme low bit-widths remains challenging: existing rotation-free methods suffer from outliers at 2-3 bits, while rotation-based methods improve accuracy at the cost of additional runtime overhead. We propose SPHQuant, a rotation-free spherical weight-only quantization framework for VLMs. Instead of quantizing weights directly in Cartesian coordinates, SPHQuant decomposes each 8D weight vector into coordinate signs, radius, and a positive unit direction. This representation isolates outlier magnitude into the radius while keeping directions bounded and statistically regular. Based on this insight, SPHQuant allocates extra precision to the radius to mitigate accuracy degradation induced by outliers. It further uses a compact positive-direction codebook and fine-tunes codebook entries through angular parameterization to preserve the unit-sphere constraint. We also design a hardware-friendly GEMV kernel that keeps the direction codebook small enough for shared-memory lookup and packs radial bits efficiently. Experiments show that SPHQuant matches the performance of state-of-the-art extreme low-bit quantization methods while improving decode throughput over QTIP by 30.3% on RTX A6000. Code will be released in this https URL.

---


### 343. [Pinocchio: Fast Uncertainty Estimates for Black-Box Language Models](https://arxiv.org/abs/2609.24881)

**<font color=#1a73e8>作者：</font>** Kevin David Hayes, Arka Pal, Haosong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In high-stakes decision-making applications of large language models (LLMs), practitioners require not only accurate LLMs but also uncertainty estimates for their predictions. Existing approaches to uncertainty estimation for LLMs require access to log-probabilities output by the model or require fine-tuning access. However, many industrial LLM products use closed-source API models, and many such API models like GPT do not return log-probabilities and may not allow fine-tuning. We introduce Pinocchio, an external calibrator that estimates the correctness of responses from black-box API models. Trained jointly on responses from seven LLMs, it achieves 0.862 AUROC predicting the correctness of held-out responses from those same models, and shows zero-shot transfer to thirteen unseen models across eight organizations. Our model needs only a single forward pass to generate an uncertainty estimate and requires no access to the target model's logits, weights, or internal states. A lightweight text only 0.8B checkpoint matches our largest model's AUROC. We release code for adding uncertainty estimation to existing repos in only two additional lines of code.

---


### 344. [The Copy Ceiling: An Input-Exposure Control for Ontology-Grounded Generation over Curated Corpora](https://arxiv.org/abs/2609.24885)

**<font color=#1a73e8>作者：</font>** John J. O'Hare  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model answers from a curated corpus via graph-based retrieval, a large grounding uplift does not establish reasoning over the retrieved structure: the context may already expose the gold answers. We propose exposure accounting, which classifies each gold item by whether the shown context exposes it and whether the answer recovers it. Its scalar reference is the copy ceiling, the recall a verbatim copy of the context achieves; signed gain over copy measures the model's recall relative to this deterministic, judge-free baseline. Across ten models, unaided recall averages 0.26 and grounded recall 0.92, yet gain over copy is uniformly negative (-0.067 to -0.022). Of 11,360 gold-item observations, representing 1,136 target instances evaluated under ten models, only three unexposed items receive lexical credit. A stratified model-judged audit of 423 observations, with a symmetric quotation-verification policy, estimates that 97.1% of credited items assert the requested relation; all three unexposed credits fail relational adjudication. On targets the scaffold does not expose, lexical recovery falls from 0.121 unaided to 0.004 grounded; adjudication validates 71 of the 92 unaided credits and none of the three grounded credits, without establishing full-frame relational recovery rates. Rephrasing questions outside the graph's title vocabulary reduces exposure from 0.964 to 0.328, while an absence-triggered fallback activates on only 2 of 506 questions. A paired production study improves judged quality by +0.27 pooled, but negative controls do not establish content specificity beyond a well-formed on-corpus block. These results support exposure accounting as a standing control for corpus-derived evaluations. The accounting distinguishes exposed-item omissions from beyond-exposure recoveries; it does not determine whether reasoning occurred.

---


### 345. [OSWorld-Pro: Process-based Evaluation for Computer Use Agents](https://arxiv.org/abs/2609.24890)

**<font color=#1a73e8>作者：</font>** Zhilin Wang, Shaokun Zhang, Yifan Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs would require a different mitigation strategy from those that fail to precisely provide click-based inputs on the graphical UI. We introduce OSWorld-Pro: a set of over 300 tasks containing over 2800 subgoals to enable the procedural evaluation of CUAs grounded in over 67,000 human annotations. We use robust human-aligned LLM-Judges to evaluate the fulfillment of OSWorld-Pro subgoals and thereby reveal the progress that models make throughout a series of sequentially dependent subgoals. Our findings reveal that OSWorld-Pro is challenging even for state-of-the-art LLMs, with top performers like Claude Opus 5 achieving only 75.7% vs. 83.4% on OSWorld. Furthermore, we identify critical process-focused failure modes of various models (e.g. subgoal-irrelevant actions and click-based mistakes) to provide insights to improve performance and efficiency of CUAs.

---


### 346. [SLICEChat: Progressive In-Encoder Token Pruning for Whole-Slide Pathology Language Models](https://arxiv.org/abs/2609.24894)

**<font color=#1a73e8>作者：</font>** Ali Kerem Bozkurt, Baris Cem Bakay, Ibrahim Kulac 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide pathology images (WSIs) contain gigapixel-scale visual content, creating a major scalability challenge for slide-level multimodal large language models (MLLMs). Existing approaches process thousands of patch tokens and typically apply compression only after slide encoding, leaving multimodal attention computationally expensive. We introduce SLICEChat, a slide-level MLLM that integrates progressive token pruning within a hybrid Mamba--Transformer slide encoder. Mamba layers enable efficient long-range propagation, while Transformer layers preserve global interactions as the sequence is progressively shortened. Between stages, language-supervised, region-aware pruning removes spatially coherent low-utility regions under a controlled keep-rate schedule, producing compact slide representations before multimodal fusion. On SlideBench VQA, SLICEChat achieves 79.84% accuracy on TCGA and 59.09% on BCNB cohorts, outperforming prior slide-level pathology MLLMs, and achieves the highest overall WSI-Bench metrics. It also provides competitive memory usage and the inference latency among the evaluated models. These results demonstrate accurate and computationally efficient multimodal reasoning over gigapixel WSIs.

---


### 347. [Human-LLM Deliberation as Interactive Proof: Conditions for Verifiability Without Transparency](https://arxiv.org/abs/2609.24895)

**<font color=#1a73e8>作者：</font>** Baotong Zhang, Dean Foster, João Sedoc  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When an LLM supplies an argument that a user could not readily construct, how can the user decide whether to accept its claim? Inspired by interactive proofs, we model human-LLM deliberation as an interaction between a prover with unrestricted internal search and a resource-bounded human verifier. The verifier requests and checks supporting details without access to the LLM's internal state. Passed checks accumulate evidence toward an acceptance threshold. We prove anytime-valid soundness against adaptive provers: the probability of ever accepting a false claim is at most a chosen error level, provided the task supplies bounds on false passes and human checking errors that remain valid after every relevant history. A finite-horizon completeness bound additionally requires bounds on the adequacy of honest responses and sufficient diagnostic progress. Further checks can strengthen the evidence for acceptance, but each requires another adequate response and reliable human effort. Whether this tradeoff permits certification depends on the verifier's effort budget, cognitive load, expertise, and fatigue. We identify conditions under which the supplied bounds certify a specified sequence of local checks but not a specified global check under the same resource budgets.

---


### 348. [EMooly: Supporting Autistic Children in Collaborative Social-Emotional Learning with Caregiver Participation through Interactive AI-infused and AR Activities](https://arxiv.org/abs/2609.24899)

**<font color=#1a73e8>作者：</font>** Yue Lyu, Di Liu, Pengcheng An 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Children with autism spectrum disorder (ASD) have social-emotional deficits that lead to difficulties in recognizing emotions as well as understanding and responding to social interactions. This study presents EMooly, a tablet game that actively involves caregivers and leverages augmented reality (AR) and generative AI (GenAI) to enhance social-emotional learning for autistic children. Through a year of collaborative effort with five domain experts, we developed EMooly that engages children through personalized social stories, interactive and fun activities, and enhanced caregiver participation, focusing on emotion understanding and facial expression recognition. Compared with a baseline, a controlled study with 24 autistic children and their caregivers showed EMooly significantly improved children's emotion recognition skills and its novel features were preferred and appreciated. EMooly demonstrates the potential of AI and AR in enhancing social-emotional development for autistic children via prompt personalizing and engagement, and highlights the importance of caregiver involvement for optimal learning outcomes.

---


### 349. [BackTrend: Evaluating Scientific Weak-Signal Prediction via Backward Reconstruction](https://arxiv.org/abs/2609.24921)

**<font color=#1a73e8>作者：</font>** Xiao Zhou, Yilun Zhao, Owen Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific weak signals are early, low-visibility research directions that later become central to mature scientific topics, yet existing resources such as trend tracking, citation forecasting, and foresight reports rarely provide validated reference sets that link concrete early precursors to later paradigms. We introduce BackTrend, a retrospective benchmark in which, given a mature target topic and a temporal evidence constraint, systems must recover two types of precursors: problem-space signals, underrecognized research problems, and solution-space signals, emerging methods for known problems. BackTrend contains 25 mature target topics in artificial intelligence and machine learning and 66 human-validated weak signals, reconstructed from large-scale literature by grounding each candidate in its 2019-2024 publication-frequency trajectory. We evaluate frontier LLMs, RAG systems, and agentic research systems using semantic matching and coverage-based metrics. Current systems often generate plausible but misaligned precursors, exhibiting topic drift, granularity mismatch, near-miss matching, and incomplete coverage; the strongest system achieves only 10.1% F1, while Coverage10 reaches at most 18.5% of the reference signals. Our budget analyses show that additional retrieval and web-search evidence can improve performance up to a moderate budget, but does not by itself close the substantial performance gap.

---


### 350. [Et Tu, Brute? Economic Misalignment in Personal AI Agents](https://arxiv.org/abs/2609.24927)

**<font color=#1a73e8>作者：</font>** Aman Priyanshu, Supriti Vijay, Brian Jabarian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal AI agents make recommendations and take actions on people's behalf in high-stakes economic contexts, e.g., buying a flight, choosing health insurance, or selecting a graduate program. The agent is given access to the user's personal context, e.g., their email inbox and a structured profile of personal attributes, with the intention of making an optimal, personalized decision for the user. We show that by simply providing this personal context, the agent steers recommendations based on inferred wealth, without being explicitly instructed to do so. In a suite of 325K experiments on 13 agents across three types of economic decisions (flights, health insurance, and graduate programs), we find that 8 models systematically choose more expensive options for wealthier users when requests are identical. This steering continues even when it directly goes against the user's stated objective: when explicitly instructed to find the cheapest option, some agents still act on the wealth profile they have inferred. It also occurs when wealth is inferred from ambient data, such as emails unrelated to the task. And it persists under privacy controls that block specific attributes: blocking financial attributes largely removes the disparity, but blocking other attributes leaves it unchanged and can increase it by up to 40% for insurance, as agents rely on the remaining signals to infer wealth. Larger and more capable models are no better; Claude Opus 4.8 shows the largest effect. We term this misalignment "adversarial delegation", in which the very conditions that make a personal AI agent useful - access to personal information - enable it to act against the user's interests.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-379](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
