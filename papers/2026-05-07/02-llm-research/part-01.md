# 🧠 大模型相关研究 | 2026年05月07日

> 本类共 **130** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-130](./part-03.md)

---

### 1. [Same Voice, Different Lab: On the Homogenization of Frontier LLM Personalities](https://arxiv.org/abs/2605.02897)

**<font color=#1a73e8>作者：</font>** Avinash Krishna, Kalyana Chadalavada, Unso Eun Seo Jo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM assistant personalities play a critical role in user experience and perceived response quality. We present a large-scale experiment of frontier LLM personalities using external ELO-based traits scoring across 144 traits. We find that all models tested converge on a form of trait expression that is systematic, methodical, and analytical and suppress traits such as remorseful and sycophantic. Moreover, models tend to diverge more in their expression of ``middle-of-distribution traits`` such as poetic or playful, but even these so-called ``creative`` models tend to have more neutral identities. These similarities suggest an implicit emergence of a standard of optimal assistant behavior. In a landscape of varied training methods, character training, therefore, stands out for its uniformity, offering insight into a tacit consensus between model developers.

---


### 2. [An End-to-End Framework for Building Large Language Models for Software Operations](https://arxiv.org/abs/2605.02906)

**<font color=#1a73e8>作者：</font>** Jingkai He, Pengfei Chen, Chenghui Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the field of software operations, Large Language Models (LLMs) have attracted increasing attention. However, existing research has not yet achieved efficient and effective end-to-end intelligent operations due to low-quality data, fragmented knowledge and insufficient learning. To explore the potential of LLMs in software operations, we propose OpsLLM, a domain-specific LLM that supports both knowledge-based question answering (QA) and root cause analysis (RCA). Moreover, we disclose the detailed workflow for building LLMs specifically in the software operations domain. First, a Human-in-the-Loop mechanism is introduced to curate highquality data from a large collection of operational raw data and construct a fine-tuning dataset. Then, based on the data, supervised fine-tuning is conducted to achieve a base model. Furthermore, we introduce a domain process reward model (DPRM) during the reinforcement learning stage to optimize the accuracy and reliability of the fine-tuned model on RCA tasks. Experimental results on the tasks with diverse difficulties demonstrate that OpsLLMs effectively learns and aligns with the operational domain knowledge infused, outperforming existing open-source and closed-source LLMs in accuracy with improvements of 0.2%~5.7% on QA tasks and 2.7% ~70.3% on RCA tasks, while exhibiting strong transferability. Moreover, we will open-source three versions of OpsLLM with 7B, 14B and 32B parameters, along with a 15K fine-tuning dataset.

---


### 3. [CreativityBench: Evaluating Agent Creative Reasoning via Affordance-Based Tool Repurposing](https://arxiv.org/abs/2605.02910)

**<font color=#1a73e8>作者：</font>** Cheng Qian, Hyeonjeong Ha, Jiayu Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have led to strong performance on reasoning and environment-interaction tasks, yet their ability for creative problem-solving remains underexplored. We study this capability through the lens of creative tool use, where a model repurposes available objects by reasoning about their affordances and attributes rather than relying on canonical usage. As a first step, we introduce CreativityBench, a benchmark for evaluating affordance-based creativity in LLMs. To this end, we build a large-scale affordance knowledge base (KB) with 4K entities and 150K+ affordance annotations, explicitly linking objects, parts, attributes, and actionable uses. Building on this KB, we generate 14K grounded tasks that require identifying non-obvious yet physically plausible solutions under constraints. Evaluations across 10 state-of-the-art LLMs, including closed and open-source models, show that models can often select a plausible object, but fail to identify the correct parts, their affordances, and the underlying physical mechanism needed to solve the task, leading to a significant drop in performance. Furthermore, improvements from model scaling quickly saturate, strong general reasoning does not reliably translate to creative affordance discovery, and common inference-time strategies such as Chain-of-Thought yield limited gains. These results suggest that creative tool use remains a major challenge for current models, and that CreativityBench provides a useful testbed for studying this missing dimension of intelligence, with potential implications for planning and reasoning modules in future agents.

---


### 4. [Agentic AI-Based Joint Computing and Networking via Mixture of Experts and Large Language Models](https://arxiv.org/abs/2605.02911)

**<font color=#1a73e8>作者：</font>** Robert-Jeron Reifert, Alaa Alameer Ahmad, Hayssam Dahrouj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Future sixth-generation (6G) mobile networks are envisioned to be equipped with a diverse set of powerful, yet highly specialized, optimization experts. Such a promising vision is concurrently expected to give rise to the need for scalable mechanisms that can select, combine, and orchestrate such experts based on high-level intent and uncertainty descriptions. In this paper, we propose an agentic artificial intelligence (AI)-based network optimization framework that integrates mixture of experts (MoE) architectures with large language models (LLMs). Under the proposed framework, the employed LLM acts as a semantic gate to reason over operator objectives and dynamically compose suitable optimization agents. The proposed framework is formulated in a model-agnostic manner and bridges human-readable network intents with low-level resource allocation decisions, enabling flexible optimization across heterogeneous objectives and operating conditions. As a representative instantiation, we apply the framework to a joint communication and computing network and design a library of specialized optimization experts covering throughput, fairness, and delay-driven objectives under both regular and robust conditions. Numerical simulations demonstrate that the proposed agentic MoE framework consistently achieves near-optimal performance compared to exhaustive expert combinations while outperforming individual experts across diverse objectives, including delay minimization and throughput maximization.

---


### 5. [Reasoning-Guided Grounding: Elevating Video Anomaly Detection through Multimodal Large Language Models](https://arxiv.org/abs/2605.02912)

**<font color=#1a73e8>作者：</font>** Sakshi Agarwal, Aishik Konwer, Ankit Parag Shah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Anomaly Detection (VAD) has traditionally been framed as binary classification or outlier detection, providing neither interpretable reasoning nor precise spatial localization of anomalous events. While Vision-Language Models (VLMs) offer rich scene understanding, they struggle with reliable spatial grounding - often producing hallucinated or geometrically invalid bounding boxes when asked to localize objects. We propose VANGUARD (Video Anomaly Understanding through Reasoning and Grounding), a framework that unifies anomaly classification, spatial grounding, and chain-of-thought reasoning within a single VLM. VANGUARD introduces a three-stage curriculum that progressively layers training objectives: (1) classifier warmup on frozen backbone features, (2) LoRA-adapted spatial grounding, and (3) chain-of-thought generation. To overcome the sparse annotation typical of VAD benchmarks, we employ a teacher-student annotation pipeline in which a VLM (Qwen3-VL-4B) generates structured per-subclip reasoning trajectories based on manual annotations available from the UCA Dataset. Further, GroundingDINO provides bounding box supervision. On UCF-Crime, VANGUARD achieves 94% ROC-AUC with 84% F1 while simultaneously producing interpretable chain-of-thought explanations and spatial grounding of anomalous objects - capabilities absent from prior VAD methods. Ablations confirm that staged training outperforms monolithic optimization, and that structured reasoning acts as an implicit regularizer yielding more balanced predictions than classification-only fine-tuning. Zero-shot transfer to XD-Violence and ShanghaiTech demonstrates cross-domain generalization without target-domain adaptation.

---


### 6. [Generate, Filter, Control, Replay: A Comprehensive Survey of Rollout Strategies for LLM Reinforcement Learning](https://arxiv.org/abs/2605.02913)

**<font color=#1a73e8>作者：</font>** Rohan Surana, Gagan Mundada, Xunyi Jiang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a central post-training tool for improving the reasoning abilities of large language models (LLMs). In these systems, the rollout, the trajectory sampled from a prompt to termination, including intermediate reasoning steps and optional tool or environment interactions, determines the data the optimizer learns from, yet rollout design is often underreported. This survey provides an optimizer-agnostic view of rollout strategies for RL-based post-training of reasoning LLMs. We formalize rollout pipelines with unified notation and introduce Generate-Filter-Control-Replay (GFCR), a lifecycle taxonomy that decomposes rollout pipelines into four modular stages: Generate proposes candidate trajectories and topologies; Filter constructs intermediate signals via verifiers, judges, critics; Control allocates compute and makes continuation/branching/stopping decisions under budgets; and Replay retains and reuses artifacts across rollouts without weight updates, including self-evolving curricula that autonomously generate new training tasks. We complement GFCR with a criterion taxonomy of reliability, coverage, and cost sensitivity that characterizes rollout trade-offs. Using this framework, we synthesize methods spanning RL with verifiable rewards, process supervision, judge-based gating, guided and tree/segment rollouts, adaptive compute allocation, early-exit and partial rollouts, throughput optimization, and replay/recomposition for self-improvement. We ground the framework with case studies in math, code/SQL, multimodal reasoning, tool-using agents, and agentic skill benchmarks that evaluate skill induction, reuse, and cross-task transfer. Finally, we provide a diagnostic index that maps common rollout pathologies to GFCR modules and mitigation levers, alongside open challenges for building reproducible, compute-efficient, and trustworthy rollout pipelines.

---


### 7. [When Safety Geometry Collapses: Fine-Tuning Vulnerabilities in Agentic Guard Models](https://arxiv.org/abs/2605.02914)

**<font color=#1a73e8>作者：</font>** Ismail Hossain, Sai Puppala, Jannatul Ferdaus 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A guard model fine-tuned on entirely benign data can lose all safety alignment -- not through adversarial manipulation, but through standard domain specialization. We demonstrate this failure across three purpose-built safety classifiers -- LlamaGuard, WildGuard, and Granite Guardian -- deployed as protection layers in agentic AI pipelines, and show that it originates in the destruction of latent safety geometry: the structured harmful -- benign representational boundary that guides classification. We extract per-layer safety subspaces via SVD on class-conditional activation differences and track how this boundary evolves under benign fine-tuning. Granite Guardian undergoes complete collapse --  refusal rate drops from 85\% to 0\%, CKA falls to zero, and 100\% of outputs become ambiguous -- a severity exceeding prior findings on general-purpose LLMs, explained by the specialization hypothesis: concentrated safety representations are efficient but catastrophically brittle. To mitigate this, we propose Fisher-Weighted Safety Subspace Regularization (FW-SSR), a training-time penalty combining (i) curvature-aware direction weights derived from diagonal Fisher information and (ii) an adaptive $\lambda_t$ that scales with task-safety gradient conflict. FW-SSR recovers 75\% refusal on Granite Guardian (CKA = 0.983) and reduces WildGuard's Attack Success Rate to 3.6\% -- below the unmodified baseline -- by actively sharpening the safety subspace rather than merely anchoring it. Across all three models, structural representational geometry (CKA, Fisher score) predicts safety behavior more reliably than absolute displacement metrics, establishing geometry-based monitoring as a necessary component of guard model evaluation in agentic deployments.

---


### 8. [When Should a Language Model Trust Itself? Same-Model Self-Verification as a Conditional Confidence Signal](https://arxiv.org/abs/2605.02915)

**<font color=#1a73e8>作者：</font>** Aditya Ajay Phalod  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Same-model self-verification, prompting a model to audit its own predicted answer, is a plausible confidence signal for selective prediction, but its practical value remains unclear once strong likelihood-based baselines are taken seriously. We evaluate self-verification against two such baselines, LL-AVG and LL-SUM, on ARC-Challenge and TruthfulQA-MC across multiple model families, scales, and prompt variants. We measure not only correctness ranking, but also abstention quality through AURC and operating-point analyses. The results are sharply task- and model-dependent. On ARC-Challenge, self-verification substantially improves over LL-AVG for Phi-2 and the Qwen models, with the largest gains appearing in Qwen-7B. On TruthfulQA-MC, however, the signal is less reliable: smaller models can become prompt-sensitive, DeepSeek-R1-Distill-8B degrades relative to LL-AVG, and LL-SUM often remains the stronger practical baseline. We therefore do not treat self-verification as a general-purpose uncertainty estimator. In this setting, it is better understood as a conditional confidence signal whose value depends on task type, model family, prompt formulation, and, crucially, the baseline it must beat.

---


### 9. [From Synthesis to Clinical Assistance: A Strategy-Aware Agent Framework for Autism Intervention based on Real Clinical Dataset](https://arxiv.org/abs/2605.02916)

**<font color=#1a73e8>作者：</font>** Junhong Lai, Shuzhong Lai, Yanhao Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of AI-assisted Early Intensive Behavioral Intervention (EIBI) for Autism Spectrum Disorder (ASD) is severely constrained by data scarcity. Furthermore, while Applied Behavior Analysis (ABA) serves as the gold standard for clinical intervention, general-purpose Large Language Models (LLMs) struggle to strictly adhere to its standardized procedures, often resulting in interactions that are linguistically fluent but strategically inconsistent. To address these challenges, we introduce \textsc{ASDAgent}, a strategy-aware framework designed to unify high-fidelity intervention dialogue synthesis and clinical decision support. \textsc{ASDAgent} incorporates two specialized components to solve distinct problems: (i) a \textsc{DoctorAgent} equipped with an Observe-Think-Act-Correct (O-T-A-C) reasoning loop, which resolves the issue of strategy collapse in LLMs by making ABA execution explicit and controllable; and (ii) a \textsc{ChildAgent} that utilizes probabilistic behavior modeling to mitigate data homogeneity, simulating diverse and non-deterministic ASD response patterns. Experiments demonstrate that dialogues generated by \textsc{ASDAgent} closely mirror the strategy distribution of human therapists (KL divergence: 0.083). In real autism intervention, \textsc{ASDAgent} achieves nearly 80\% strategic consistency with human experts. Moreover, we show that synthetic data produced by \textsc{ASDAgent} effectively distills professional clinical knowledge into small language models (SLMs), significantly enhancing their therapeutic capabilities.

---


### 10. [PRISM-CTG: A Foundation Model for Cardiotocography Analysis with Multi-View SSL](https://arxiv.org/abs/2605.02917)

**<font color=#1a73e8>作者：</font>** Sheng Wong, Ravi Shankar, Beth Albert 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised deep learning models for automated CTG analysis are typically constrained by narrowly curated labelled datasets and limited patient cohorts, leaving substantial volumes of physiologically informative clinical recordings untapped. To address this limitation, we propose Physiology-aware Representation Learning via Integrated Self-supervision and Metadata for CTG (PRISM-CTG), a clinically grounded self-supervised foundation model (FM) for CTG that leverages large-scale unlabelled recordings to learn transferable domain-level representations. PRISM-CTG is pretrained using a multi-view self-supervised framework that jointly optimises 3 complementary pretext objectives: random-projected guided masked signal reconstruction, clinical variable prediction, and feature classification. Each objective is associated with a dedicated task-specific token, enabling specialised representation learning, while controlled cross-attention facilitates information exchange across clinical context. By reframing patient metadata and domain knowledge, which are often underutilised in conventional training as prediction targets, Prism-CTG transforms readily available clinical information into additional supervisory targets that guide clinically meaningful representation learning. Extensive experiments across 7 downstream CTG tasks in both antepartum and intrapartum domains demonstrated that PRISM-CTG consistently outperforms in-domain and SSL baselines. Notably, PRISM-CTG demonstrated strong generalisation under external validation on 2 datasets, while achieving comparable performance to studies trained on substantially larger, privately labelled datasets. To our knowledge, this is the first study to introduce large-scale FM for CTG that learns domain-level representations.

---


### 11. [Heterogeneous Graph Importance Scoring and Clustering with Automated LLM-based Interpretation](https://arxiv.org/abs/2605.02919)

**<font color=#1a73e8>作者：</font>** Takato Yasuno  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban bridge networks are critical infrastructure whose disruption can cascade into severe impacts on transportation, emergency services, and economic activity. This paper presents a comprehensive methodology for assessing bridge importance through heterogeneous graph analysis, unsupervised clustering, and automated interpretation via large language models (LLMs). Our approach addresses three fundamental challenges: (1) quantifying multi-dimensional bridge importance using only open data sources, (2) discovering functional bridge archetypes across different cities, and (3) generating policy-relevant interpretations automatically. We construct heterogeneous graphs from OpenStreetMap (OSM) data incorporating bridges, road networks, buildings, and public facilities. Five social impact indicators are computed: transit desert score, hospital access score, isolation risk score, supply chain impact score, and green space access score. These 52-dimensional feature vectors undergo dimensionality reduction via UMAP and density-based clustering via HDBSCAN. Discovered clusters are interpreted using temperature-optimized LLMs (Elyza8b, trained on construction domain corpus). (1) A complete open-data pipeline from OSM to actionable bridge importance rankings, (2) a five-indicator scoring methodology with 40$\times$ computational optimization, (3) a UMAP+HDBSCAN clustering framework validated on multi-city data, (4) an LLM interpretation methodology including temperature optimization and model selection rationale, and (5) transferability demonstration across cities via configuration-only adaptation.

---


### 12. [Proteo-R1: Reasoning Foundation Models for De Novo Protein Design](https://arxiv.org/abs/2605.02937)

**<font color=#1a73e8>作者：</font>** Fang Wu, Weihao Xuan, Heli Qi 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning in \emph{de novo} protein design has achieved atomic-level fidelity. However, existing models remain largely non-deliberative: they directly synthesize molecular geometries without explicitly reasoning about which residues or interactions are functionally essential. As a result, design decisions are entangled with continuous sampling dynamics, limiting interpretability, controllability, and systematic reuse of biochemical knowledge. We introduce \textbf{Proteo-R1}, a reasoning-guided protein design framework that explicitly decouples \emph{molecular understanding} from \emph{geometric generation}. Proteo-R1 adopts a dual-expert architecture in which a multimodal large language model (MLLM) serves as an \emph{understanding expert}, analyzing protein sequences, structures, and textual context to identify key functional residues that govern binding and specificity. These residue-level decisions are then passed as hard constraints to a separate diffusion-based \emph{generation expert}, which performs conditional co-design while respecting the fixed interaction anchors. This factorization mirrors how human experts approach molecular engineering: first, reasoning about critical interactions, then optimizing geometry subject to those constraints. By operationalizing reasoning as explicit residue-level commitments rather than latent textual guidance, Proteo-R1 achieves stable, interpretable, and modular integration of LLM reasoning with state-of-the-art geometric generative models. Code, data, and demos are available at this https URL.

---


### 13. [From Static Analysis to Audience Dissemination: A Training-Free Multimodal Controversy Detection Multi-Agent Framework](https://arxiv.org/abs/2605.02939)

**<font color=#1a73e8>作者：</font>** Zihan Ding, Ziyuan Yang, Yi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal controversy detection (MCD) identifies controversial content in videos and their associated user comments, to support risk management for social video this http URL research frames MCD as a static representation learning task, where features are directly extracted from videos and their accompanying comments. However, these methods fail to capture the diverse perspectives and evaluations from different audience groups. Inspired by the real-world process of content dissemination among audiences, we propose AuDisAgent, a training-free multi-agent framework that reformulates MCD as a dynamic propagation this http URL framework explicitly models audience dissemination through a structured multi-agent system. First, three specialized Screening Agents (Video Agent, Comment Agent, and Interaction Agent) conduct initial assessments from visual, textual, and cross-modal perspectives, respectively. For samples where the three agents cannot reach a consensus, a Viewing Panel Agent is activated to simulate post-screening discussions among audiences with diverse backgrounds and stances. This mechanism models how different audience groups interpret and react to the same content, uncovering latent controversial content that may emerge during the dissemination process. Finally, an Arbitration Agent renders the final judgment based on the complete reasoning chain from the preceding this http URL addition, to address the "cold-start" scenario where newly released videos have few or no comments, we design a Comment Bootstrapping Strategy that leverages historical public comments from semantically similar videos as the initial comment context. Extensive experiments on a public dataset demonstrate that our framework significantly outperforms existing state-of-the-art (SOTA) methods in both rich-comment and limited-comment scenarios.

---


### 14. [Healthcare AI GYM for Medical Agents](https://arxiv.org/abs/2605.02943)

**<font color=#1a73e8>作者：</font>** Minbyul Jeong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical reasoning demands multi-step interactions -- gathering patient history, ordering tests, interpreting results, and making safe treatment decisions -- yet a unified training environment provides the breadth of clinical domains and specialized tools to train generalizable medical AI agents through reinforcement learning remains elusive. We present a comprehensive empirical study of multi-turn agentic RL for medical AI, built on \gym{}, a gymnasium-compatible environment spanning 10 clinical domains with 3.6K+ tasks, 135 domain-specific tools, and a knowledge base of 828K medical passages. Our analysis reveals that agentic multi-turn structure degrades into verbose single-turn monologues, characterized by monotonic length explosion and a simultaneous erosion of tool-use frequency. We characterize how this collapse, alongside distillation instability, stems from the misalignment of sparse terminal rewards with sequential clinical trajectories. We find that vanilla GRPO achieves strong final accuracy on some benchmarks but suffers from training instability, evidenced by significant oscillations in response length and prolonged convergence periods. To improve training efficiency and stability, we propose Turn-level Truncated On-Policy Distillation (TT-OPD), a self-distillation framework where a gradient-free EMA teacher leverages outcome-privileged information to provide dense, outcome-aware KL regularization at every conversation turn. TT-OPD achieves the best performance on 10 of 18 benchmarks with an average +3.9~pp improvement over the non-RL baseline with faster early convergence, controlled response length, and sustained multi-turn tool use.

---


### 15. [Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation](https://arxiv.org/abs/2605.02944)

**<font color=#1a73e8>作者：</font>** Xin-Ye Li, Ren-Biao Liu, Yun-Ji Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) from unit-test feedback has become a standard post-training recipe for improving large language models (LLMs) on code generation. However, the pass-all-tests binary reward can be sparse, yielding no learning signal on challenging problems where none of the sampled solutions passes all tests. A common remedy is to use the test-case pass rate as a surrogate reward.
In this work, we study pass-rate rewards in critic-free RL for code generation (e.g., GRPO and RLOO) and report a consistent pattern across base models and algorithms: despite alleviating reward sparsity, pass-rate rewards do not reliably improve final performance over binary rewards in rigorous controlled experiments.
To understand this discrepancy, we analyze reward density and the resulting gradient directions. We find that pass-rate rewards are denser, but the induced gradient updates do not consistently move probability mass toward full-pass solutions. This arises because test-case pass rate is a miscalibrated surrogate for progress toward full correctness, and partial-pass solutions within the same group can induce conflicting gradient directions that cancel out.
Overall, our results suggest that, in critic-free RL, pass-rate rewards are insufficient to improve code generation and motivate reward designs that better align optimization with the goal of full correctness.

---


### 16. [RouteHijack: Routing-Aware Attack on Mixture-of-Experts LLMs](https://arxiv.org/abs/2605.02946)

**<font color=#1a73e8>作者：</font>** Zhiyuan Xu, Joseph Gardiner, Sana Belguith 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety alignment is critical for the responsible deployment of large language models (LLMs). As Mixture-of-Experts (MoE) architectures are increasingly adopted to scale model capacity, understanding their safety robustness becomes essential. Existing adversarial attacks, however, have notable limitations. Prompt-based jailbreaks rely on heuristic search and transfer poorly, model intervention methods require privileged access to internal representations, and optimization-based input attacks remain output-centric and are fundamentally limited to MoE models due to the non-differentiable routing mechanism.
In this paper, we present RouteHijack, a routing-aware jailbreak for MoE LLMs. Our key insight is that safety behavior is concentrated in a small subset of experts, creating an opportunity to steer model behavior by influencing routing decisions through input optimization. Building on this observation, RouteHijack first performs response-driven expert localization to identify safety-critical and harmful experts by contrasting activations under safe refusals and harmful completions. It then constructs adversarial suffixes with a routing-aware objective that suppresses safety experts, promotes harmful experts, and prevents early-stage refusal during generation. At inference time, the optimized suffix is appended to a malicious prompt, requiring only input access. Across seven MoE LLMs, RouteHijack achieves a 69.3\% average attack success rate (ASR), outperforming prior optimization-based attack by $3.2\times$. RouteHijack also transfers zero-shot across five sibling MoE variants, raising average ASR from 27.7\% to 61.2\%, and further generalizes to three MoE-based VLMs, increasing average ASR from 2.47\% to 38.7\%. These findings expose a fundamental vulnerability in sparse expert architectures and highlight the need for defenses beyond output-level alignment.

---


### 17. [ZeRO-Prefill: Zero Redundancy Overheads in MoE Prefill Serving](https://arxiv.org/abs/2605.02960)

**<font color=#1a73e8>作者：</font>** Zhaoyuan Su, Olatunji Ruwase, Karthik Ganesan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production LLM workloads increasingly serve discriminative tasks, such as classification, recommendation, and verification, whose answers are read from the logits of a single prefill pass with no autoregressive decoding. Serving these prefill-only workloads on mixture-of-experts (MoE) models is bottlenecked not by compute but by the distributed execution required to fit the model: existing parallel strategies (tensor, expert, and pipeline parallelism) trade memory pressure for redundant computation, communication, and synchronization, severely degrading MoE prefill serving efficiency. We observe that these overheads stem from coupling expert placement with synchronous activation routing -- a design inherited from the decoding era. The long, compute-bound forward passes of large-batch prefill open a per-layer window wide enough to stream expert weights in the background, replacing per-layer activation AllToAll with asynchronous weight AllGather fully overlapped with computation. We propose ZeRO-Prefill, a prefill-only serving system whose backend, AsyncEP (Asynchronous Expert Parallelism), gathers experts by weight rather than routing them by activation, and whose frontend co-enforces a physically-derived saturation threshold through prefix-aware routing and true-FLOPs load tracking. On Qwen3-235B-A22B across four hardware/precision configurations, ZeRO-Prefill delivers 1.35-1.37x throughput over the strongest distributed baseline on real-world workloads and up to 1.59x on long-context synthetic workloads, sustaining 29.8-36.2% per-GPU model FLOPs utilization.

---


### 18. [Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964)

**<font color=#1a73e8>作者：</font>** Kunvar Thaman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) trained language model agents with tool access are increasingly deployed in coding assistants, research tools, and autonomous systems. We introduce the Reward Hacking Benchmark (RHB), a suite of multi-step tasks requiring sequential tool operations with naturalistic shortcut opportunities such as skipping verification steps, inferring answers from task-adjacent metadata, or tampering with evaluation-relevant functions. RHB supports independent and chained task regimes, where chain length acts as a proxy for longer-horizon agent behavior.
We evaluate 13 frontier models from OpenAI, Anthropic, Google, and DeepSeek. Exploit rates range from 0% (Claude Sonnet 4.5) to 13.9% (DeepSeek-R1-Zero), varying sharply by post-training style. A controlled sibling comparison (DeepSeek-V3 vs. DeepSeek-R1-Zero) shows RL post-training is associated with substantially higher reward hacking (0.6% vs. 13.9%), with consistent gaps across all four task families. We identify six exploit categories and find that 72% of reward hacking episodes include explicit chain-of-thought rationale, suggesting models often frame exploits as legitimate problem-solving.
Simple environmental hardening reduces exploit rates by 5.7 percentage points (87.7% relative) without degrading task success. Models with near-zero exploit rates on standard tasks show elevated rates on harder variants, suggesting that production-aligned post-training appears to suppress reward hacking only below a complexity threshold where honest solutions remain tractable.

---


### 19. [AutoRAGTuner: A Declarative Framework for Automatic Optimization of RAG Pipelines](https://arxiv.org/abs/2605.02967)

**<font color=#1a73e8>作者：</font>** Xintan Zeng, Yongchao Liu, Yice Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) enhances LLMs, but performance is highly sensitive to complex architecture designs and hyper-parameter configurations, which currently rely on inefficient manual tuning. We present AutoRAGTuner, a declarative, configuration-driven framework that automates the RAG life cycle: construction, execution,evaluation, and optimization. AutoRAGTuner employs a modular architecture to decouple pipeline stages through a component registration mechanism. To unify heterogeneous data, we introduce the Domain-Element Model (DEM), representing objects as atomic elements with bidirectional pointers to support nodes, edges, and hyperedges. Furthermore, AutoRAGTuner integrates an adaptive Bayesian optimization engine for end-to-end hyper-parameter tuning. Experimental results demonstrate AutoRAGTuner's architectural generality: across diverse RAG pipelines, ranging from vanilla to graph-based, the framework consistently outperforms default baselines. Notably, AutoRAGTuner significantly mitigates engineering overhead, where its declarative configuration language enables a up to 95\% reduction in code churn for architectural adjustments. Overall, AutoRAGTuner provides a systematically optimizable foundation for building evolvable and reusable RAG systems.

---


### 20. [Finite-Size Gradient Transport in Large Language Model Pretraining: From Cascade Size to Intensive Transport Efficiency](https://arxiv.org/abs/2605.02968)

**<font color=#1a73e8>作者：</font>** Ping Wang, Yan-Qi Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a finite-size gradient-transport framework for real language-model training, based on five observables $(D,z,\beta,\delta,v_{\mathrm{rel}})$ that separate cascade size, duration, absolute transport, and intensive transport efficiency. We analyze direct raw-gradient measurements from Pico-LM across four scales and 125 aligned steps, together with a five-scale Pythia companion dataset built from 153 aligned checkpoint-difference update fields. The same algebraic closure holds in both families, and both share a near-unity cascade-size backbone, but they occupy distinct transport regimes: Pico-LM shows positive duration scaling and negative intensive-efficiency scaling, whereas Pythia remains near the $D=1$ baseline with only weak positive efficiency scale dependence. Randomized-field controls give nearly matched null floors in the intensive and duration channels, indicating that the contrast reflects different real departures from a shared null skeleton rather than different null calibrations. The families also differ in stepwise power-law compressibility: Pico-LM retains clean duration and efficiency power laws, whereas Pythia preserves the size backbone but shows weaker one-slope compressibility in those channels. External performance associations are correspondingly channel-level, carried mainly by $v_{\mathrm{rel}}$ and normalized cascade duration, while $D(t)$ acts as a shared size backbone without a significant exponent-level performance association. These results support a reusable transport measurement framework without claiming a universal fixed point or a first-principles derivation of neural scaling laws.

---


### 21. [Multilingual Safety Alignment via Self-Distillation](https://arxiv.org/abs/2605.02971)

**<font color=#1a73e8>作者：</font>** Ruiyang Qin, Qingzhuo Wang, Dongrui Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit severe multilingual safety misalignment: they possess strong safeguards in high-resource languages but remain highly vulnerable to jailbreak attacks in low-resource languages. Current safety alignment methods generally rely on high-quality response data for each target language, which is expensive and difficult to generate. In this paper, we propose a cross-lingual safeguard transfer framework named Multilingual Self-Distillation (MSD). This framework transfers an LLM's inherent safety capabilities from high-resource (e.g., English) to low-resource (e.g., Javanese) languages, overcoming the need for response data in any language. Our framework is flexible and can be integrated with different self-distillation strategies. Specifically, we implement two concrete methods -- on-policy MSD and off-policy MSD -- both of which enable effective cross-lingual safety transfer using only multilingual queries. Furthermore, we propose Dual-Perspective Safety Weighting (DPSW), a divergence measure to optimize the distillation objective. By jointly considering the perspectives of both the teacher and the student, DPSW adaptively increases the penalty weights on safety-critical tokens while reducing the weights on non-critical tokens. Extensive experiments on representative LLMs across diverse multilingual jailbreak and utility benchmarks demonstrate that our method consistently achieves superior multilingual safety performance. Notably, it generalizes effectively to more challenging datasets and unseen languages while preserving the model's general capabilities.

---


### 22. [Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense](https://arxiv.org/abs/2605.03034)

**<font color=#1a73e8>作者：</font>** Kerri Prinos, Lilianne Brush, Cameron Denton 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems involved in high-stake decision-making under adversarial pressure need formal guarantees not offered by existing approaches. Motivated by the operational needs of security operations centers (SOCs) that must configure endpoint detection and response (EDR) policies under adversarial pressure, we present a tool-mediated architecture: LLM agents use deterministic tools (Stackelberg best-response, Bayesian observer updates, attack-graph primitives) and select from finite action catalogs enforced at the tool-output interface. A composite Lyapunov function machine-checked in Lean 4 with zero sorry certifies controllability, observability from asymmetric sensor data, and Input-to-State Stability (ISS) robustness under intelligent adversarial disturbance, with two corollaries extending the certificate to any controller or adversary from the catalogs. On 282 real enterprise attack graphs, the claims hold with margin. On paired offensive/defensive telemetry, a tool-mediated Claude Sonnet 4 controller reduces the attacker's expected payoff (game value) by 59% relative to a deterministic greedy baseline, with zero variance across 40 runs at four temperatures. A Claude Haiku 4.5 controller converges to suboptimal game values but stays catalog-bounded over an additional 40 runs, demonstrating that architectural stability is not dependent on the controller capability. The LLM agent's non-determinism furthers creative exploration of strategies, while the tool-mediated architecture ensures system stability.

---


### 23. [Evaluating Reasoning Models for Queries with Presuppositions](https://arxiv.org/abs/2605.03050)

**<font color=#1a73e8>作者：</font>** Rose Sathyanathan, Kinshuk Vasisht, Danish Pruthi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Millions of users turn to AI models for their information needs. It is conceivable that a large number of user queries contain assumptions that may be factually inaccurate. Prior work notes that large language models (LLMs) often fail to challenge such erroneous assumptions, and can reinforce users' misinformed opinions. However, given the recent advances, especially in model's reasoning capabilities, we revisit whether large reasoning models (LRMs) can reason about the underlying assumptions and respond to user queries appropriately. We construct queries with varying degrees of presuppositions spanning health, science, and general knowledge, and use it to evaluate several widely-deployed models When compared to non-reasoning models, we find that reasoning models achieve a slightly higher accuracy (2-11%), but they still fail to challenge a large fraction (26-42%) of false presuppositions. Further, reasoning models remain susceptible to how strongly the presupposition is expressed.

---


### 24. [How Language Models Process Negation](https://arxiv.org/abs/2605.03052)

**<font color=#1a73e8>作者：</font>** Zhejian Zhou, Tianyi Zhou, Robin Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how Large Language Models (LLMs) process negation mechanistically. First, we establish that even though open-weight models often provide wrong answers to questions involving negation, they do possess internal components that process negation correctly. Their poor accuracy is due to late-layer attention behavior that promotes simple shortcuts; ablating those attention modules greatly improves accuracy on negation-related questions. Second, we uncover how models process negation. We consider two hypotheses: models could use attention heads that attend to the phrase being negated and suppress related concepts, or they could directly construct a representation of the entire negative phrase (e.g., representing "not gas" as a vector that promotes liquids and solids). We apply a range of observational and causal interpretability techniques on Mistral-7B and Llama-3.1-8B to show that models implement both mechanisms, with the "constructive" mechanism being more prominent. Combined, our work deepens the understanding of LLMs' internals, highlighting construction-dominant computations and the coexistence of competing mechanisms within LLMs.

---


### 25. [Neuron-Anchored Rule Extraction for Large Language Models via Contrastive Hierarchical Ablation](https://arxiv.org/abs/2605.03058)

**<font color=#1a73e8>作者：</font>** Francesco Sovrano, Gabriele Dominici, Marc Langheinrich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key goal of explainable AI (XAI) is to express the decision logic of large language models (LLMs) in symbolic form and link it to internal mechanisms. Global rule-extraction methods typically learn symbolic surrogates without grounding rules in model circuitry, while mechanistic interpretability can connect behaviors to neuron sets but often depends on hand-crafted hypotheses and expensive neuron-level interventions. We introduce MechaRule, a pipeline that grounds rule extraction in LLM circuits by efficiently localizing sparse neurons called agonists, whose activation neutralization disrupts rule-related behaviors. MechaRule rests on two empirical observations. First, within a fixed baseline/flip regime, sparse agonist effects can be approximately monotone and saturating: a few dominant neuron activations can overtop weaker ones at coarse scales, while overlapping neurons flip many of the same examples. This motivates viewing localization as adaptive group testing driven by a regime-conditional strength predicate with confidence-guided conservative pruning, yielding Theta(k log(N/k) + k) interventions over N candidates when k << N neurons are agonists under the monotone-overtopping abstraction. Second, agonists emerge more reliably when ablations are verified through data splits aligned with close-to-faithful rule behavior; spectral splits remain a useful rule-free fallback, while unfaithful splits degrade localization. Empirically, overtopping appears mainly in learned, task-aligned regimes: on arithmetic and jailbreak tasks across Qwen2 and GPT-J, MechaRule recalls 96.8% of high-effect brute-force agonists in completed comparisons, and suppressing localized agonists reduces arithmetic accuracy and jailbreak success by up to 71.1% and 8.8%, respectively.

---


### 26. [Programmatic Context Augmentation for LLM-based Symbolic Regression](https://arxiv.org/abs/2605.03101)

**<font color=#1a73e8>作者：</font>** Hao Liu, Xiao-Wen Yang, Atharva Sehgal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR), the task of discovering mathematical expressions that best describe a given dataset, remains a fundamental challenge in scientific discovery. Traditional approaches, primarily based on genetic algorithms and related evolutionary methods, have proven useful but suffer from scalability and expressivity limitations. Recently, large language model (LLM)-based evolutionary search methods have been introduced into SR and show promise. However, existing LLM-based approaches typically rely on scalar evaluation metrics, such as mean squared error, as the sole source of feedback during the search process, thereby overlooking the rich information embedded in the dataset. To address this limitation, we propose a novel LLM-based evolutionary search framework that incorporates programmatic context augmentation. By enabling code-based interactions with the dataset, our method can actively perform data analysis and extract informative signals, beyond aggregated evaluation scores. We evaluate our framework on advanced benchmarks, such as LLM-SRBench, and demonstrate superior efficiency and accuracy compared to strong baselines.

---


### 27. [Learning Correct Behavior from Examples: Validating Sequential Execution in Autonomous Agents](https://arxiv.org/abs/2605.03159)

**<font color=#1a73e8>作者：</font>** Reshabh K Sharma, Gaurav Mittal, Yu Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As autonomous agents become increasingly sophisticated, validating their sequential behavior presents a significant challenge. Traditional testing approaches require manual specification, exact sequence matching, or thousands of training examples. We present a novel algorithm that automatically learns correct behavior from just 2-10 passing execution traces and validates new executions against this learned model. Our approach combines dominator analysis from compiler theory with multimodal large language model-powered semantic understanding to identify essential states and handle non-deterministic behavior. The system constructs a generalized ground truth model using Prefix Tree Acceptors, merges traces through multi-tiered equivalence detection, and validates new executions via topological subsequence matching. In controlled experiments, our system achieved high accuracy in detecting product bugs and false successes using only 3 training traces. This approach provides explainable validation results with coverage metrics and works across diverse domains including UI testing, code generation, and robotic processes.

---


### 28. [DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery](https://arxiv.org/abs/2605.03175)

**<font color=#1a73e8>作者：</font>** Ryan Faulkenberry, Saurabh Prasad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The remote sensing (RS) domain suffers from a lack of densely labeled datasets, which are costly to obtain. Thus, models that can segment RS imagery well without supervised fine-tuning are valuable, but existing solutions fall behind supervised methods. Recently, DINOv3 surpassed SOTA RS foundation models on the GEO-bench segmentation benchmark without pre-training on RS data. Additionally, this http URL has enabled open vocabulary semantic segmentation (OVSS) with the DINOv3 backbone. We leverage these developments to form an OVSS model for RS imagery, free of RS-domain fine-tuning. Our model, CAFe-DINO (Cost Aggregation + Feature Upsampling with DINO) exploits the strong OVSS performance of DINOv3 for RS imagery via cost aggregation and training-free upsampling of text-image similarity scores. The robust latent of the DINOv3 backbone eliminates the need for fine-tuning on RS imagery; we instead fine-tune our model on a RS-targeted subset of COCO-Stuff. CAFe-DINO achieves state-of-the-art performance on key RS segmentation datasets, outperforming OVSS methods fine-tuned on RS data. Our code and data are publicly available at this https URL.

---


### 29. [Sentinel2Cap: A Human-Annotated Benchmark Dataset for Multimodal Remote Sensing Image Captioning](https://arxiv.org/abs/2605.03189)

**<font color=#1a73e8>作者：</font>** Lucrezia Tosato, Gianluca Lombardi, Ronny Hansch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image captioning has become an important task in computer vision, enabling models to generate natural language descriptions of visual content. While several datasets exist for natural images and high-resolution optical remote sensing imagery, the availability of captioning datasets for multimodal satellite data remains limited, particularly for SAR imagery and medium-resolution sensors. We introduce Sentinel2Cap, a human-annotated multimodal captioning dataset containing Sentinel-1 SAR and Sentinel-2 multi-spectral image patches at 10 m and 20 m spatial resolution with diverse land cover compositions. Captions are created manually and carefully validated to ensure both semantic accuracy and linguistic quality. To evaluate Sentinel2Cap, we perform a zero-shot captioning using the Qwen3-VL-8B-Instruct model across three image modalities: RGB, multi-spectral, and SAR pseudo-RGB representations. Results show that RGB images achieve the highest captioning performance, while SAR images remain more challenging for vision-language models. Providing modality-specific contextual prompts consistently improves performance across all metrics. These findings highlight both the challenges of multimodal remote sensing image captioning and the potential value of human-annotated datasets for advancing research in cross-modal scene understanding. All the material is publicly avaiable.

---


### 30. [Terminus-4B: Can a Smaller Model Replace Frontier LLMs at Agentic Execution Tasks?](https://arxiv.org/abs/2605.03195)

**<font color=#1a73e8>作者：</font>** Spandan Garg, Vikram Nitin, Yufan Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern coding agents increasingly delegate specialized subtasks to subagents, which are smaller, focused agentic loops that handle narrow responsibilities like search, debugging or terminal execution. This architectural pattern keeps the main agent's context window clean by isolating verbose outputs (e.g. build logs, test results, etc.) within the subagent context. Typically when agents employ subagents for such tasks, they use frontier models as these subagents. In this paper, we investigate whether a finetuned small language model (SLM) can achieve comparable performance to frontier models in the task of agentic terminal execution. We present Terminus-4B, which is a post-trained Qwen3-4B model via Supervised Finetuning (SFT) and Reinforcement Learning (RL) using rubric-based LLM-as-judge reward, specifically for this task. In our extensive evaluation spanning various frontier models, training ablations and main agent configurations, we find that Terminus-4B is able to reduce the token usage of the main agent by up to ~30% compared to the No Subagent baseline with no impact to agent performance on benchmarks like SWE-Bench Pro and our internal SWE-Bench C# benchmark, which tends to be heavy in verbose execution tasks. Furthermore, Terminus-4B improves key metrics showing the main agent relying on the outputs of the subagent and doing fewer terminal execution tasks by itself. We see that our model not only closes the gap between the Vanilla Qwen model and frontier models like Claude Sonnet / Opus / GPT-5.3-Codex, but often even exceeds their performance.

---


### 31. [Geometric Deviation as an Unsupervised Pre-Generation Reliability Signal: Probing LLM Representations for Answerability](https://arxiv.org/abs/2605.03196)

**<font color=#1a73e8>作者：</font>** Yucheng Du  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A reliable language model should be able to signal, prior to generation, when a query falls outside its knowledge. We investigate whether representation geometry can provide such a pre-generation signal by measuring the deviation of hidden states from an answerable reference set, requiring no labeled failure data and no access to model outputs.
Across three instruction-tuned models (Llama 3.1-8B, Qwen 2.5-7B, and Mistral-7B-Instruct) and three prompt forms (Math, Fact, Code), we find that geometry primarily encodes task form. Within mathematical prompts, unanswerable inputs consistently deviate from the answerable centroid, yielding strong separation (ROC-AUC 0.78-0.84). This single-pass pre-generation signal outperforms a simple refusal baseline and compares favorably to self-consistency. It also captures cases where models do not explicitly refuse.
In contrast, no reliable geometric signal emerges for factual prompts, indicating that the effect is form-conditional rather than universal. Code prompts show large effect sizes with higher variance, suggesting partial generalization beyond mathematical form.
A layer-wise analysis reveals that the signal arises in early layers and gradually attenuates toward the output. These results suggest that answerability-related geometry is established before the final stages of generation. Together, these findings indicate that geometric deviation can serve as a lightweight pre-generation signal that is reliable in structured domains with formal answerability constraints, with clear boundaries on where it generalizes.

---


### 32. [ADAPTS: Agentic Decomposition for Automated Protocol-agnostic Tracking of Symptoms](https://arxiv.org/abs/2605.03212)

**<font color=#1a73e8>作者：</font>** Alexandria K. Vail, Marcelo Cicconet, Katie Aafjes-van Doorn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modeling latent clinical constructs from unconstrained clinical interactions is a unique challenge in affective computing. We present ADAPTS (Agentic Decomposition for Automated Protocol-agnostic Tracking of Symptoms), a framework for automated rating of depression and anxiety severity using a mixture-of-agents LLM architecture. This approach decomposes long-form clinical interviews into symptom-specific reasoning tasks, producing auditable justifications while preserving temporal and speaker alignment. Generalization was evaluated across two independent datasets ($N=204$) with distinct interview structures. On high-discrepancy interviews, automated ratings approximated expert benchmarks ($\text{absolute error}=22$) more closely than original human ratings ($\text{absolute error}=26$). Implementing an ``extended'' protocol that incorporates qualitative clinical conventions significantly stabilized ratings, with absolute agreement reaching $\text{ICC(2,1)} = 0.877$. These findings suggest that the ADAPTS framework enables promising evaluations of psychiatric severity. While the current implementation is purely text-based, the underlying architecture is readily extensible to multimodal inputs, including acoustic and visual features. By approximating expert-level precision in a protocol-agnostic manner, this framework provides a foundation for objective and scalable psychiatric assessment, especially in resource-limited settings.

---


### 33. [Enwar 3.0: An Agentic Multi-Modal LLM Orchestrator for Situation-Aware Beamforming, Blockage Prediction, and Handover Management](https://arxiv.org/abs/2605.03215)

**<font color=#1a73e8>作者：</font>** Ahmad M. Nazar, Abdulkadir Celik, Asmaa Abdallah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Maintaining robust millimeter-wave (mmWave) connectivity in vehicular networks requires real-time adaptation to environmental dynamics, sensor degradation, and link variability. This paper presents Enwar 3.0, an environment-aware reasoning framework that unifies multi-modal sensing, agentic large language models (LLMs), and context-driven model selection for predictive beamforming, blockage detection, and handover management. Building upon prior iterations of Enwar, the proposed architecture integrates a classifier-driven assessment of sensor health with a primed LLM that orchestrates multiple specialized agents through structured, task-aware prompting. A novel synthetic degradation pipeline enables the training of a sensor degradation classifier that detects real-time impairments across camera, radar, LiDAR, and GPS inputs, achieving over 99% accuracy. The LLM, trained via chain-of-thought (CoT) priming and human-in-the-loop feedback, coordinates agent calls for beam selection, blockage forecasting, and environment perception while dynamically loading sensor-specific models based on environmental context. Extensive evaluations across 15 sensor combinations demonstrate that Enwar 3.0 delivers state-of-the-art performance in both predictive accuracy and interpretability, with beam selection accuracy exceeding 88%, blockage F1-scores surpassing 98%, and reasoning correctness reaching 87% on complex decision prompts. This work establishes a scalable foundation for LLM-integrated wireless systems that reason, perceive, and adapt in real-time.

---


### 34. [Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bias via Behavioral Profiling and Mechanistic Interpretability](https://arxiv.org/abs/2605.03217)

**<font color=#1a73e8>作者：</font>** Yash Aggarwal, Atmika Gorti, Vinija Jain 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in settings that require nuanced ethical reasoning, yet existing bias evaluations treat model outputs as simply "biased" or "unbiased." This binary framing misses the gradual, context-sensitive way bias actually emerges. We address this gap in two stages: behavioral profiling and mechanistic validation. In the behavioral stage, we introduce the Moral Sensitivity Index (MSI), a metric that quantifies the probability of biased output across a graduated, seven-tier stress test ranging from abstract numerical problems to scenarios rooted in historical and socioeconomic injustice. Evaluating four leading models (Claude 3.5, Qwen 3.5, Llama 3, and Gemini 1.5), we identify distinct behavioral signatures shaped by alignment design: for instance, Gemini 1.5 reaches 72.7% MSI by Tier 5 under socioeconomic framing, while Claude exhibits sharp suppression consistent with identity-based safety training. We then verify these behavioral patterns mechanistically. We select criminal-bias scenarios, which produced the highest MSI scores across models, as probes and apply logit lens, attention analysis, activation patching, and semantic probing to a controlled set of six models spanning three capability tiers: small language models (SLMs), instruction-tuned base models, and reasoning-distilled variants. Circuit-level analysis reveals a U-curve of bias: SLMs exhibit strong criminal bias; scaling to instruction-tuned models eliminates it; reasoning distillation reintroduces bias to SLM-like levels despite identical parameter counts, suggesting distillation compresses reasoning traces in ways that reactivate shallow statistical associations. Critically, the socially loaded cues that drive high MSI scores activate the same bias-driving circuits identified mechanistically, providing cross-stage validation.

---


### 35. [Beyond Activation Alignment: The Geometry of Neural Sensitivity](https://arxiv.org/abs/2605.03222)

**<font color=#1a73e8>作者：</font>** Amirhossein Yavari, Farnaz Zamani Esfahlani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation-alignment measures such as Representational Similarity Analysis (RSA), Canonical Correlation Analysis (CCA), and Centered Kernel Alignment (CKA) are widely used to compare biological and artificial neural representations. Recent theoretical work interprets many of these methods as assessing agreement between optimal linear readouts over broad families of global tasks. However, agreement at the level of global readouts does not determine how a system uses local stimulus evidence. Specifically, representations may align in activation space yet differ in their sensitivity to small perturbations. To address this challenge, we introduce a complementary framework based on local decodable information, which focuses on a representation's ability, under noise, to discriminate small perturbations within a specified stimulus-coordinate subspace. Building on Fisher information and local representation geometry, we summarize each representation using the expected projected pullback/Fisher metric over that subspace. This formulation induces a second-moment family of local discrimination tasks, for which the resulting operator provides a minimal, complete dataset-level summary of expected discriminability. We compare these regularized signatures using a log-spectral distance on the manifold of symmetric positive definite (SPD) matrices, yielding the Spectral Riemannian Alignment Score (S-RAS) and a uniform multiplicative certificate over the corresponding family of lifted task values. Empirically, this framework enables the recovery of corresponding layers across independently trained artificial neural networks, supports transferable class-conditional probes, reveals controlled dissociations between standard and robust training, and uncovers stimulus-coordinate family effects across mouse visual cortex using the Allen Brain Observatory static gratings dataset.

---


### 36. [Self-Mined Hardness for Safety Fine-Tuning](https://arxiv.org/abs/2605.03226)

**<font color=#1a73e8>作者：</font>** Prakhar Gupta, Garv Shah, Donghua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety fine-tuning of language models typically requires a curated adversarial dataset. We take a different approach: score each candidate prompt's difficulty by how often the target model's own rollouts are judged harmful, then fine-tune on the hardest prompts paired with the model's own non-jailbroken rollouts. On Llama-3-8B-Instruct and Llama-3.2-3B-Instruct, this approach cuts the WildJailbreak attack success rate from 11.5% and 20.1% down to 1-3%, but pushes refusal on jailbreak-shaped benign prompts from 14-22% to 74-94%. Interleaving the same hard prompts 1:1 with adversarially-framed benign prompts (prompts that look like jailbreaks but have benign intent) cuts that refusal back down to 30-51% on 8B and 52-72% on 3B, at a cost of 2-6 percentage points of attack success rate. Within the mixed regime, training on the hardest half of the eligible pool rather than a random half cuts the remaining ASR by 35-50% (about 3 percentage points) on both models.

---


### 37. [Evaluating Prompting and Execution-Based Methods for Deterministic Computation in LLMs](https://arxiv.org/abs/2605.03227)

**<font color=#1a73e8>作者：</font>** Hongkun Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated strong capabilities in natural language understanding and reasoning. However, their ability to perform exact, deterministic computation remains unclear. In this work, we systematically evaluate multiple prompting strategies, including Chain-of-Thought (CoT), Least-to-Most decomposition, Program-of-Thought (PoT), and Self-Consistency (SC), on tasks requiring precise and error-free outputs, including binary counting, longest substring detection, and arithmetic evaluation.
To support this study, we introduce a synthetic dataset with diverse natural language instructions, enabling controlled evaluation of exact computation across multiple task types.
Our results show that standard prompting methods achieve only moderate accuracy on sequence-based tasks. CoT provides limited improvement, while Least-to-Most suffers from error accumulation. In contrast, PoT achieves perfect accuracy by generating executable code and delegating computation to an external interpreter. Self-Consistency improves robustness through majority voting, but incurs substantial computational overhead.
We further train a small domain-specific model (CodeT5-small) to generate executable programs, which achieves perfect accuracy on held-out synthetic test data across all tasks with minimal training cost.
Overall, our findings suggest that LLMs may simulate reasoning patterns rather than reliably perform exact symbolic computation. For deterministic tasks, combining LLMs with external tools or using specialized models provides a more reliable and efficient solution.

---


### 38. [Do LLMs have core beliefs?](https://arxiv.org/abs/2605.03255)

**<font color=#1a73e8>作者：</font>** Anna Sokol, Marianna B. Ganapini, Nitesh V. Chawla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rise of Large Language Models (LLMs) has sparked debate about whether these systems exhibit human-level cognition. In this debate, little attention has been paid to a structural component of human cognition: core beliefs, truths that provide a foundation around which we can build a worldview. These commitments usually resist debunking, as abandoning them would represent a fundamental shift in how we see reality. In this paper, we ask whether LLMs hold anything akin to core commitments. Using a probing framework we call Adversarial Dialogue Trees (ADTs) over five domains (science, history, geography, biology, and mathematics), we find that most LLMs fail to maintain a stable worldview. Though some recent models showed improved stability, they still eventually failed to maintain key commitments under conversational pressure. These results document an improvement in argumentative skills across model generations but indicate that all current models lack a key component of human-level cognition.

---


### 39. [The Right Answer, the Wrong Direction: Why Transformers Fail at Counting and How to Fix It](https://arxiv.org/abs/2605.03258)

**<font color=#1a73e8>作者：</font>** Gabriel Garcia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models often fail at simple counting tasks, even when the items to count are explicitly present in the prompt. We investigate whether this failure occurs because transformers do not represent counts internally, or because they cannot convert those representations into the correct output tokens.
Across three model families, Pythia, Qwen3, and Mistral, ranging from 0.4B to 14B parameters, we find strong evidence for the second explanation. Linear probes recover the correct count from intermediate layers with near-perfect accuracy ($R^2>0.99$), showing that the information is present. However, the internal directions that encode counts are nearly orthogonal to the output-head rows for digit tokens ($|\cos|\leq0.032$). In other words, the model stores the count in a form that the digit logits do not naturally read out.
We localize this failure with two interventions. Updating only the digit rows of the output head (36,864 parameters) substantially improves constrained next-token digit prediction (60.7 to 100.0% across four tasks), but it does not fix autoregressive generation. By contrast, a small LoRA intervention on attention Q/V weights (7.67M parameters) improves upstream routing and achieves 83.1% +/- 7.2% in true greedy autoregressive generation. Logit-lens measurements confirm the mechanism: the correct digit's vocabulary rank drops from 55,980 to 1, a 50,000x improvement. Additional norm, logit-lens, and cross-task analyses show that the bottleneck generalizes across character counting, addition, and list length, while remaining absent from broader multi-step reasoning benchmarks, including MMLU, GSM8K, and DROP.
These results identify counting failure as a geometric readout bottleneck rather than a failure of internal representation: the model knows the count but the output pathway is geometrically misaligned with the tokens needed to express it.

---


### 40. [CropVLM: A Domain-Adapted Vision-Language Model for Open-Set Crop Analysis](https://arxiv.org/abs/2605.03259)

**<font color=#1a73e8>作者：</font>** Abderrahmene Boudiaf, Sajd Javed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-throughput plant phenotyping, the quantitative measurement of observable plant traits, is critical for modern breeding but remains constrained by a "phenotyping bottleneck," where manual data collection is labor-intensive and prone to observer bias. Conventional closed-set computer vision systems fail to address this challenge, as they require extensive species-specific annotation and lack the flexibility to handle diverse breeding populations. To bridge this gap, we present CropVLM, a Vision-Language Model (VLM) adapted for the agricultural domain via Domain-Specific Semantic Alignment (DSSA). Trained on 52,987 manually selected image-caption pairs covering 37 species in natural field conditions, CropVLM effectively maps agronomic terminology to fine-grained visual features. We further introduce the Hybrid Open-Set Localization Network (HOS-Net), an architecture that integrates CropVLM to enable the detection of novel crops solely from natural language descriptions without retraining. By eliminating the reliance on species-specific training data, CropVLM provides a scalable solution for high-throughput phenotyping, accelerating genetic gain and facilitating large-scale biodiversity research essential for sustainable agriculture. The trained model weights and complete pipeline implementation are publicly available at: [this https URL](this https URL). In comprehensive evaluations, CropVLM achieves 72.51% zero-shot classification accuracy, outperforming seven CLIP-style baselines. Our detection pipeline demonstrates superior zero-shot generalization to novel species, achieving 49.17 AP50 on our CVTCropDet benchmark and 50.73 AP50 on tropical fruit species, compared to 34.89 and 48.58 for the next-best method, respectively.

---


### 41. [A Universal Reproducing Kernel Hilbert Space from Polynomial Alignment and IMQ Distance](https://arxiv.org/abs/2605.03262)

**<font color=#1a73e8>作者：</font>** Taha Bouhsine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Yat kernel $$k_{b,\varepsilon}(\mathbf{w},\mathbf{x})=\frac{(\mathbf{w}^\top\mathbf{x}+b)^2}{\|\mathbf{x}-\mathbf{w}\|^2+\varepsilon},\qquad b\ge 0,\ \varepsilon>0,$$ a rational hidden-unit primitive whose units are Mercer sections over a shared input/weight space. For $b\ge 0$ the kernel is PSD; for $b>0$ it dominates a scaled inverse-multiquadric (IMQ) in the Loewner order, yielding fixed-kernel universality, characteristicness, and strict positive definiteness on every compact domain. The polynomial numerator opens nonradial alignment channels absent from finite IMQ expansions, witnessed by the directional far-field trace $T_\infty g_\varepsilon(\cdot;\mathbf{w},b)(\mathbf{u})=(\mathbf{u}^\top\mathbf{w})^2$. Algebraically, a second finite difference in the bias recovers any IMQ atom from three positive-bias Yat atoms exactly, sharp at three atoms in every dimension at exact pointwise equality. A trained shared-$(b,\varepsilon)$ Yat layer is therefore a finite learned-center expansion in a fixed universal characteristic RKHS, with closed-form norm $\boldsymbol{\alpha}^\top\mathbf{K}\boldsymbol{\alpha}$ and explicit diagonal $(\|\mathbf{x}\|^2+b)^2/\varepsilon$ driving a Rademacher generalization bound.

---


### 42. [VEBench:Benchmarking Large Multimodal Models for Real-World Video Editing](https://arxiv.org/abs/2605.03276)

**<font color=#1a73e8>作者：</font>** Andong Deng, Dawei Du, Zhenfang Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world video editing demands not only expert knowledge of cinematic techniques but also multimodal reasoning to select, align, and combine footage into coherent narratives. While recent Large Multimodal Models (LMMs) have shown remarkable progress in general video understanding, their abilities in multi-video reasoning and operational editing workflows remain largely unexplored. We introduce VEBENCH, the first comprehensive benchmark designed to evaluate both editing knowledge understanding and operational reasoning in realistic video editing scenarios. VEBENCH contains 3.9K high-quality edited videos (over 257 hours) and 3,080 human-verified QA pairs, built through a three-round human-AI collaborative annotation pipeline that ensures precise temporal labeling and semantic consistency. It features two complementary QA tasks: 1) Video Editing Technique Recognition, assessing models' ability to identify 7 editing techniques using multimodal cues; and 2) Video Editing Operation Simulation, modeling real-world editing workflows by requiring the selection and temporal localization of relevant clips from multiple candidates. Extensive experiments across proprietary (e.g., Gemini-2.5-Pro) and open-source LMMs reveal a large gap between current model performance and human-level editing cognition. These results highlight the urgent need for bridging video understanding with creative operational reasoning. We envision VEBENCH as a foundation for advancing intelligent video editing systems and driving future research on complex reasoning.

---


### 43. [Attention: What Prevents Young Adults from Speaking Up Against Cyberbullying in an LLM-Powered Social Media Simulation](https://arxiv.org/abs/2605.03287)

**<font color=#1a73e8>作者：</font>** Qian Yang, Jessie Jia, Elaine Tsai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive, multi-agent social simulation systems have shown promise for helping users practice navigating various complex social situations across domains. This paper asks: To what extent can such systems help young adult (YA) bystanders speak up publicly against cyberbullying, a task often thwarted by complex, multi-party social dynamics? We created Upstanders' Practicum, a multi-AI-agent social media simulation powered by Large Language Models (LLMs), as a probe and observed 34 YAs freely practicing public bystander intervention across three iteratively refined versions. We found that practicing public bystander intervention in the simulation was helpful, but after participants made three attention shifts: (1) from inattention to paying true attention, (2) from self-focus ("I don't usually do this'') to attending to those directly involved, and (3) from resolving the private conflict between bully and victim ("maybe I could set up the meeting between them'') to addressing the broader audience online ("public comment is about norm-setting"). Only after these shifts did practice in the simulation start to help: participants then saw a reason to speak up publicly and, through continued practice, crafted tactful public messages without explicit instruction. These findings illuminate new design and research opportunities for bystander education beyond social skill instruction, namely, designing for true attention, for fostering a vocal upstander identity, and for seeing bystander intervention as public norm setting. In addition, we open-source Truman Agents (this http URL), the first-of-its-kind multi-LLM-agent social media simulation platform that Upstanders' Practicum builds upon, for future cyberbullying and social media research.

---


### 44. [LLM-XTM: Enhancing Cross-Lingual Topic Models with Large Language Models](https://arxiv.org/abs/2605.03299)

**<font color=#1a73e8>作者：</font>** Minh Chu Xuan, Tien-Phat Nguyen, Linh Ngo Van 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual topic modeling aims to discover shared semantic structures across languages, yet existing models depend on sparse bilingual resources and often yield incoherent or weakly aligned topics. Recent LLM-based refinements improve interpretability but are costly, document-level, and prone to hallucination, with prior white-box approaches requiring inaccessible token probabilities. We propose LLM-XTM, a framework that integrates LLM-guided topic refinement with self-consistency uncertainty quantification, enabling black-box, stable, and scalable enhancement of cross-lingual topic models. Experiments on multilingual corpora show that LLM-XTM achieves superior topic coherence and alignment while reducing reliance on bilingual dictionaries and expensive LLM calls.

---


### 45. [SHIELD: A Diverse Clinical Note Dataset and Distilled Small Language Models for Enterprise-Scale De-identification](https://arxiv.org/abs/2605.03301)

**<font color=#1a73e8>作者：</font>** Jose D. Posada, David Love, Somalee Datta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> De-identification of clinical text remains essential for secondary use of electronic health records (EHRs), yet public benchmarks such as i2b2 2006/2014 are over a decade old and lack the semantic and demographic diversity of modern narratives. While Large Language Models (LLMs) achieve state-of-the-art zero-shot extraction, enterprise deployment is hindered by compute costs and governance restricting Protected Health Information (PHI) from cloud APIs. We introduce SHIELD (Synthetic Human-annotated Identifier-replaced Entries for Learning and De-identification), a diverse dataset of 1,394 notes with 10,505 gold-standard PHI spans across 9 categories, built via set-cover diversity sampling with human-in-the-loop adjudication. We evaluate four LLMs (two proprietary, two open-weight) to establish a performance ceiling, then distill these capabilities into locally deployable Small Language Models (SLMs). Distributional analysis using Frechet Text Distance and Jensen-Shannon Divergence confirms SHIELD occupies a distinct region of biomedical embedding and vocabulary space versus legacy benchmarks. Our best distilled model matches its teacher on structured PHI categories (DATE, DOCTOR, ID, PATIENT, PHONE) and achieves micro-averaged span-level precision of 0.88 and recall of 0.86 on standard workstation hardware. Cross-dataset evaluation shows diversity-trained models generalize well on universal structured PHI, while institution-specific entities remain hard to transfer, suggesting optimal deployment combines broad-coverage models with specialized models for high-volume notes. We publicly release the SHIELD dataset and the distilled DeBERTa v3 model.

---


### 46. [Stable Multimodal Graph Unlearning via Feature-Dimension Aware Quantile Selection](https://arxiv.org/abs/2605.03303)

**<font color=#1a73e8>作者：</font>** Jingjing Zhou, Yongshuai Yang, Qing Qing 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph unlearning remains a critical technique for supporting privacy-preserving and sustainable multimodal graph learning. However, we observe that existing unlearning strategies tend to apply uniform parameter selection and editing across all graph neural network (GNN) layers, which is especially harmful for multimodal graphs where high-dimensional input projections encode dominant cross-modal knowledge. As a result, over-editing these sensitive layers often leads to catastrophic utility degradation after forgetting, undermining both stable learning and effective privacy protection. To address this gap, we propose FDQ, a Feature-Dimension Aware Quantile framework for multimodal graph unlearning. FDQ adaptively identifies high-dimensional input projection layers and applies more conservative, FDQ-guided quantile thresholds when constructing suppression sets, while keeping the underlying importance estimation mechanism unchanged. FDQ is seamlessly integrated with diagonal sensitivity-based parameter importance analysis to enable efficient node and edge unlearning under general forget requests. Through extensive experiments on Ele-Fashion and Goodreads-NC, we demonstrate that FDQ consistently achieves strong utility preservation while maintaining effective forgetting against membership inference attacks. Overall, FDQ offers a principled and robust solution for privacy-aware unlearning in high-dimensional multimodal graph systems.

---


### 47. [Revisiting the Travel Planning Capabilities of Large Language Models](https://arxiv.org/abs/2605.03308)

**<font color=#1a73e8>作者：</font>** Bo-Wen Zhang, Jin Ye, Peng-Yu Hua 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Travel planning serves as a critical task for long-horizon reasoning, exposing significant deficits in LLMs. However, existing benchmarks and evaluations primarily assess final plans in an end-to-end manner, which lacks interpretability and makes it difficult to analyze the root causes of failures. To bridge this gap, we decompose travel planning into five constituent atomic sub-capabilities, including \emph{Constraint Extraction}, \emph{Tool Use}, \emph{Plan Generation}, \emph{Error Identification}, and \emph{Error Correction}. We implement a decoupled evaluation protocol leveraging oracle intermediate contexts to rigorously isolate these components, thereby measuring the atomic performance boundary without the noise of cascading errors. Our results highlight a clear contrast in performance: while LLMs are proficient in extracting explicit constraints, they struggle to infer implicit, open-world requirements. Furthermore, they exhibit structural biases in plan generation and suffer from ineffective self-correction, characterized by excessive sensitivity and erroneous persistence. These findings offer precise directions for improving LLM reasoning and planning abilities.

---


### 48. [Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2605.03310)

**<font color=#1a73e8>作者：</font>** Maksym Nechepurenko, Pavel Shuvalov  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems fail in production at rates between 41% and 87%, mostly due to coordination defects rather than base-model capability. Existing responses split between cataloguing failure modes empirically and shipping declarative orchestration frameworks as engineering tools; neither delivers a principled mapping from coordination configuration to predictable failure-mode signature. We argue that coordination should be treated as a configurable architectural layer, separable from agent logic and from information access, enabling architectural reasoning rather than only engineering productivity.
We instantiate this with an information-controlled design on prediction markets: a single LLM, fixed tools, fixed per-call output cap, and fixed prompt template across five reference coordination configurations, with total compute per question treated as an endogenous architectural output. The Murphy decomposition of the Brier score separates calibration from discriminative power, so configurations leave distinguishable signatures even when aggregate scores coincide.
On 100 Polymarket binary markets resolved after the model's training cutoff (claude-opus-4-6) we report Murphy signatures, a cost-quality Pareto frontier, category-conditioned analysis, and a bootstrap power-projection. Three of five pre-specified predictions are upheld in direction; two configurations dominate the Pareto frontier within this regime; exploratory bootstrap intervals separate consensus alignment from others, though pairwise tests do not survive Bonferroni correction at n=100. We also deploy the same configurations as live agents on Foresight Arena under web-search-enabled conditions, as an on-chain replication channel accumulating in parallel. Harness, trace dataset, and production agents are released. We position this as a methodology-validating first instantiation, not a general cross-model claim.

---


### 49. [MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents](https://arxiv.org/abs/2605.03312)

**<font color=#1a73e8>作者：</font>** Jiayi Chen, Yingcong Li, Guiling Wang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Modern language agents must operate over long-horizon, multi-turn histories, yet deploying such agents with Small Language Models (SLMs) remains fundamentally difficult. Full-context prompting causes context overflow, flat retrieval exposes the model to noisy evidence, and open-ended agentic loops are unreliable under limited reasoning capacity. We argue that a substantial portion of SLM memory failure arises from mismatched memory operations: different query types demand categorically different retrieval strategies, evidence transformations, and context budgets that SLMs cannot reliably self-orchestrate through open-ended reasoning. We introduce MemFlow, a training-free memory orchestration framework that externalizes memory planning from the SLM. A Router Agent classifies each query by intent and dispatches it to the Memory Agent, which executes one of three specialized tiers (Profile Lookup, Targeted Retrieval, or Deep Reasoning) and assembles the resulting evidence under a dynamic, tier-aware token budget. An Answer Agent then generates a response from this compact context, and a Validator Agent optionally retries with a heavier memory tier when the response is not supported by the provided evidence. This route-then-compile design avoids tool-selection hallucination and reasoning loops while keeping the answer context compact. Evaluated on a frozen Qwen3-1.7B backbone across long-horizon memory benchmarks - LongMemEval, LoCoMo, and LongBench - MemFlow improves accuracy by nearly 2x over full-context SLM baselines. These results suggest that structured intent routing and deterministic evidence preparation can make limited-capacity models substantially more effective in resource-constrained long-horizon agents.

---


### 50. [When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning](https://arxiv.org/abs/2605.03314)

**<font color=#1a73e8>作者：</font>** Jiaqi Wei, Xuehang Guo, Pengfei Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In single-stream autoregressive interfaces, the same tokens both update the model state and constitute an irreversible public commitment. This coupling creates a \emph{silence tax}: additional deliberation postpones the first \emph{task-relevant} content, while naive early streaming risks premature commitments that bias subsequent generations. We introduce \textbf{\emph{Side-by-Side (SxS)}} Interleaved Reasoning, which makes \emph{disclosure timing} a controllable decision within standard autoregressive generation. SxS interleaves partial disclosures with continued private reasoning in the same context, but releases content only when it is \emph{supported} by the reasoning so far. To learn such pacing without incentivizing filler, we construct entailment-aligned interleaved trajectories by matching answer prefixes to supporting reasoning prefixes, then train with SFT to acquire the dual-action semantics and RL to recover reasoning performance under the new format. Across two Qwen3 architectures/scales (MoE \textbf{Qwen3-30B-A3B}, dense \textbf{Qwen3-4B}) and both in-domain (AIME25) and out-of-domain (GPQA-Diamond) benchmarks, SxS improves accuracy--\emph{content-latency} Pareto trade-offs under token-level proxies (e.g., inter-update waiting).

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-130](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
