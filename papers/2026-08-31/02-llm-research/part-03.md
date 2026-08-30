# 🧠 大模型相关研究 | 2026年08月31日

> 本类共 **231** 篇论文：已确认 **221** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-231](./part-05.md)

---

### 101. [AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling](https://arxiv.org/abs/2608.26623)

**<font color=#1a73e8>作者：</font>** Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation. The benchmark comprises 3,808 instances spanning six DAG topologies and three difficulty tiers, evaluated with five generators (3B-70B open-weight models and GPT-5.4) and six judges (20B to frontier scale) under paired with- and without-ground-truth conditions. Judge alignment degrades monotonically with task difficulty, 1.5x faster without ground truth, and on hard queries without ground truth all six judges converge to a narrow 77-82% band regardless of scale, revealing a structural ceiling driven primarily by task difficulty, though its height is partly prompt-dependent for weaker generators, that model capacity alone cannot overcome. Ground-truth exposure is not uniformly beneficial: it reduces alignment for GPT-5.4 (1.5 pp) and Gemini-2.5-Pro (3.9 pp), consistent with over-anchoring. Among mitigation strategies, chain-of-thought reasoning and judge temperature both have negligible effect, while structured evaluation rubrics improve alignment by up to 6.5 pp but do not generalize uniformly across judge-generator pairs. With ground truth, QwQ-32B best matches the programmatic reference, while a human validation study identifies GPT-OSS-120B as the most human-aligned judge; without it, frontier judges lead only marginally within the shared ceiling. These results expose fundamental limitations of current LLM judges and yield practical guidelines for reliable evaluation in agentic systems.

---


### 102. [Who Remains, What Changes: Identity Anchored Composed Gait Retrieval](https://arxiv.org/abs/2608.26632)

**<font color=#1a73e8>作者：</font>** Jingchen Fei, Zengbin Wang, Yukun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition has achieved remarkable progress, yet existing methods remain confined to rigid visual matching and often overlook the potential of natural language instructions for interactive retrieval. In this paper, we introduce Composed Gait Retrieval (CoGR), a novel task that retrieves a target gait sequence based on a reference sequence and a natural language modification query. To address the absence of existing datasets for this task, we design an automated annotation pipeline powered by large vision-language models (VLMs) to construct the first gait-language datasets: Language-Augmented CCPG and Language-Augmented CASIA-B. Building on this, we propose ComposeGait, an identity-anchored composition framework designed to prevent the identity drift that arises when generic composed retrieval follows the instruction but returns the wrong person. Its Part-aware Identity Adapter (PIA) aggregates multi-frame, part-aware identity evidence into a sample-specific ID token. We inject the ID tokens into both branches of a shared Q-Former to preserve identity, while excluding the ID-token outputs from the final retrieval embeddings. Joint identity and task-adapted composed-retrieval objectives optimize this space end to end. We evaluate ComposeGait on both benchmarks and show that it achieves the best R@1 among the compared methods, reaching 72.38% on Language-Augmented CCPG and 83.61% on Language-Augmented CASIA-B. These results establish ComposeGait as a strong baseline for CoGR. The datasets and code will be made publicly available.

---


### 103. [Information-Guided Frontier Decoding: Contextual Utility-Driven Commitment in dMLLMs](https://arxiv.org/abs/2608.26641)

**<font color=#1a73e8>作者：</font>** Xingyou Fang, Jingxing Zhong, Xiaosong Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decoding quality in diffusion multimodal language models (dMLLMs) depends heavily on the order in which masked tokens are committed. Existing confidence-based strategies prioritize locally easy tokens, but confidence does not necessarily reflect contextual usefulness. As a result, structurally easy tokens such as punctuation may be committed before informative semantic anchors, weakening context propagation and increasing error accumulation. We propose Information-Guided Frontier Decoding (IGFD), a training-free decoding strategy that ranks candidates using token confidence, neighborhood uncertainty, and structural commitment risk. IGFD encourages early commitment of reliable semantic anchors while delaying fragile structural tokens, improving contextual support during decoding. A dynamic candidate frontier further constrains token selection to locally expandable regions under the same decoding budget. The method requires no additional training, auxiliary models, or extra forward passes. Experiments across multimodal understanding, reasoning, grounding, and hallucination benchmarks show that IGFD consistently outperforms existing decoding strategies across the majority of benchmarks and diffusion MLLM backbones under identical decoding budgets.

---


### 104. [Meta-Learning Where to Allocate Experts: Task-Conditioned Layer-Wise Compression for MoEs](https://arxiv.org/abs/2608.26650)

**<font color=#1a73e8>作者：</font>** Rongfeng Wang, Shichao Weng, Zhiqiang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models route each token to a subset of expert networks, increasing capacity while keeping per-token computation sparse. In many deployed MoEs, the number of active experts is fixed across layers and tasks, although layer roles and expert redundancy vary with depth and demand varies with difficulty. Existing approaches address only part of this setting: layer-wise allocations are usually determined offline and reused for all tasks, while token-level methods vary expert activation using local routing signals without task-level context. We propose MetaNet, a support-set controller that predicts, for each layer, an expert-retention threshold and a bounded routing bias. The backbone, experts, and router remain frozen. On DeepSeek-MoE-16B-Chat, MetaNet provides a tunable accuracy-expert-activation trade-off. Relative to fixed k=6, a conservative setting activates 3.61 experts on average (40% fewer) and achieves comparable MMLU accuracy (0.489 vs. 0.474), whereas an aggressive setting activates 2.28 experts on average (62% fewer) with accuracy approximately 3.7 percentage points lower. The MMLU-trained controller also transfers to C-Eval without retraining, activating 2.90 experts on average (52% fewer than fixed k=6) at 0.386 accuracy.

---


### 105. [Beyond Vector Hiding: Breaking and Mitigating Shared-Direction Weight Obfuscation in TEE-Offloaded Large Language Models](https://arxiv.org/abs/2608.26651)

**<font color=#1a73e8>作者：</font>** Menghui Zhang, Aoying Zheng, Guoxiao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environment (TEE)-shielded partitioning of Large Language Models (LLMs) accelerates on-device inference by offloading obfuscated linear layers to an untrusted accelerator while retaining only a small correction inside the TEE. However, earlier lightweight obfuscation schemes preserved weight-vector directions and were broken by ArrowMatch. To defend against this attack, ArrowCloak injects scalar multiples of the same hidden direction into all weight vectors, enabling lightweight trusted correction. We show that this reuse leaves a rank-one relation across the complete accelerator-visible matrix. For the released real-valued scheme, we propose SpectralLeak, which estimates and removes the shared component. Across 12 task settings, its surrogates achieve $87.98\%$ mean accuracy versus $89.85\%$ for the victims. In our defense-favorable mod-$Q$ realization of ArrowCloak's published modular security formulation, mod-$Q$ arithmetic suppresses this spectral signal but retains the algebraic rank-one relation modulo $Q$. We therefore propose LatticeLeak, which exploits the resulting hidden lattice. In our BERT-Base and GPT2-Base experiments, it reconstructs every protected fixed-point parameter exactly; across all evaluated architectures, the reconstructed models retain victim-level task accuracy without victim queries, labels, or fine-tuning. These findings identify shared rank-one reuse as the root cause of the leakage exploited by our attacks. Guided by this insight, we design ButterflyCloak, a keyed maximal-rank butterfly mask that replaces the reused direction with distinct mask rows while retaining fast trusted correction...

---


### 106. [Do LLMs Understand Personality? Rethinking Persona Fidelity Evaluation through Structured Behavioral Inference](https://arxiv.org/abs/2608.26674)

**<font color=#1a73e8>作者：</font>** Mengfan Li, Zesheng Wei, Xuanhua Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly deployed to simulate diverse human characters, ensuring persona fidelity, defined as the extent to which an agent's behavior consistently reflects the psychological and stylistic characteristics of a target persona, has become a critical requirement. However, existing evaluation paradigms primarily rely on either holistic LLM-based judges, which are prone to "holistic appraisal hallucination'', or static psychometric inventories, which fail to capture the context-dependent fidelity required in dynamic dialogue. To address these limitations, we propose PRISM (Persona Reasoning with Inverse SFL-based Modeling), a psycholinguistically grounded framework that reformulates persona fidelity evaluation as a structured inverse inference task. Inspired by Systemic Functional Linguistics (SFL), PRISM decomposes persona fidelity into three functional dimensions: Task Framing, Interpersonal Stance, and Linguistic Style. It estimates dimension-specific evidence over a persona-conditioned label space and aggregates these signals into an interpretable and auditable evaluation process. Experiments show that PRISM yields more accurate and stable judgements than traditional holistic judging, providing a more reliable framework for persona fidelity evaluation.

---


### 107. [FOCUS & RePAIR: Mitigating Text Degeneration via Token-Level Guidance for Pruned Large Language Models](https://arxiv.org/abs/2608.26676)

**<font color=#1a73e8>作者：</font>** Junyoung Lee, Sehyeon Park, Shinhyoung Jang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pruning is a practical approach to compress large language models (LLMs), but it can amplify text degeneration, especially repetition loops, even when perplexity and task accuracy remain largely unchanged. In this work, we present a token-level analysis of this failure mode by viewing decoding as a dynamical process that enters and persists in a small set of recurrent contexts. Our analysis decomposes degeneration into loop entry risk and loop persistence, and shows that persistence is controlled by the escape mass assigned to plausible alternatives within the token sampling set. Motivated by these findings, we propose two token-level guidance objectives for post-pruning fine-tuning. FOCUS reweights distillation toward high-confidence teacher regions to suppress leakage, while RePAIR uses onset-centered positive/negative continuation pairs with a margin loss to promote plausible alternatives and prevent early commitment to repetition loops. Experiments on open-ended continuation and instruction-based generation show that both methods consistently reduce repetition and improve generation quality.

---


### 108. [Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs](https://arxiv.org/abs/2608.26684)

**<font color=#1a73e8>作者：</font>** Ji Soo Lee, Jinyoung Park, Seohyun Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent large language models achieve strong performance on complex reasoning tasks, where reinforcement learning with Group Relative Policy Optimization (GRPO) has emerged as a leading paradigm for optimizing models on self-generated trajectories. However, the on-policy nature of GRPO bounds the model to the reasoning skills it can already produce, restricting to learn more advanced capabilities. Prior works inject privileged reasoning traces from a stronger teacher policy to guide training, yet these traces are inherently out of distribution with respect to the student policy. We observe that this mismatch between on-policy and off-policy causes gradient clipping on semantically critical reasoning tokens, ultimately rewarding correct answers while leaving the reasoning that justifies them unlearned. Hence, we propose \textbf{Echo-GRPO}, a framework that lets the model reason in the words it speaks. Rather than imitating low-probability privileged traces from the teacher model, Echo-GRPO rewrites them into the student policy's own \textit{idiolect}, that is, its own characteristic vocabulary and expression patterns, while preserving their semantics via Dual-Reference Decoding. We instantiate this framework as \textbf{VideoEcho-R1} for video reasoning distillation, achieving consistent improvements across three multimodal LLM backbones and five benchmarks. Finally, we show that our idiolectal paraphrasing is a plug-in module that consistently improves both RL and supervised fine-tuning frameworks for reasoning distillation, demonstrating that policy-aligned supervision extends beyond GRPO.

---


### 109. [Relational Over-Regularization: Graph-Based AI-Generated Text Detection via Sentence Transition Deviation](https://arxiv.org/abs/2608.26694)

**<font color=#1a73e8>作者：</font>** Hyeonchu Park, Bugeun Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detecting AI-generated text (AIGT) remains challenging because existing approaches rely on token-level statistical signals or independent stylometric features, causing them to overfit to specific generators and fail under distribution shift. We identify a structural signal at the sentence-pair level: LLMs produce inter-sentence transition variance that deviates from human writing through inflated variance driven by recurring similarity bursts at paragraph boundaries and templated transitions. We formalize this as Relational Over-Regularization (ROR) and validate it across four benchmarks (p < 0.001). The central contribution is this relational problem formulation, not a novel GNN architecture; CSFG is one concrete instantiation for operationalizing ROR. To exploit this signal, we propose the Cross-Source Stylometric Fingerprint Graph (CSFG), a graph-based framework that encodes positional, sequential, semantic, and transition deviation signals as learnable GNN edge features. The per-edge signed deviation {\delta}_ij operationalizes ROR without hand-crafted thresholds and acts as a false-positive calibrator. CSFG achieves 97.14% accuracy under binary detection, outperforming the strongest graph-based baseline by 11.14 pp, with a false-positive rate of 1.57% and robust generalization to unseen LLMs in the inflated-variance regime; detection degrades for generators whose transition variance falls at or below the human baseline.

---


### 110. [KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference](https://arxiv.org/abs/2608.26699)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Yingnan Zhou, Weijie Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As the most widely used container orchestration platform, Kubernetes provides flexible privilege configuration by allowing developers to manage Linux capabilities via manifest files. However, developers rely on default settings or coarse-grained security contexts in practice, violating the principle of least privilege and enlarging the attack surface of containerized workloads. Existing studies either detect vulnerable patterns in Kubernetes manifests or infer required capabilities for standalone Linux programs, but they do not directly address capability minimization in Kubernetes.
To bridge this gap, we first conduct an empirical study on three open-source datasets, revealing that 74.67% of projects lack capability configurations. Motivated by our observations, we propose KubeCap, a framework for Kubernetes capability minimization. KubeCap translates deployment specifications into deterministic manifests, locates container entrypoints, performs reachability-guided system call analysis, and leverages LLM-assisted rule specification to derive syscall--parameter--capability relations from Linux kernel code. Based on these results, KubeCap infers the minimal capability set required by each workload and automatically generates repaired manifests. Evaluation on 10 representative Go-based Kubernetes projects shows an average capability reduction rate of 54.97%, outperforming rapid type analysis and class hierarchy analysis baselines while maintaining practical analysis cost. These results demonstrate KubeCap's effectiveness in enforcing least privilege in Kubernetes.

---


### 111. [Accelerating Scientific Research with Gemini in the Real-World](https://arxiv.org/abs/2608.26701)

**<font color=#1a73e8>作者：</font>** Samuel Schmidgall, Xiaokai Zhu, Marian Shaw 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an extension and comprehensive real-world validation of Co-Scientist, a Gemini-based multi-agent system designed to accelerate end-to-end scientific research across hypothesis generation, experimentation, and manuscript generation. Moving beyond in silico hypothesis generation, this specialized configuration transitions Co-Scientist into an execution-grounded research partner advancing closed-loop scientific workflows across materials science, biology, and computer science. In materials science, Co-Scientist interfaced with a semi-automated chemical vapor deposition reactor to design a safe precursor route for MXenes; experimental execution produced a lamellar 2D material sharing key structural similarities with the Ti3C2Tx MXene lattice, although further experiments are needed to confirm the atomic structure. Leveraging Gemini 3 Deep Think for rapid, lab-in-the-loop execution, it also tailored growth recipes to laboratory constraints in minutes, enabling single-attempt growth of monolayer MoS2, MoSe2, and WS2 semiconductors. In biology, Co-Scientist predicted emergent swarming phenotypes of engineered E. coli across inducer (IPTG) gradients from sparse imaging data, quantitatively matching unpublished wet-lab morphological measurements. In computer science, Co-Scientist autonomously discovered an inference-time scaling architecture that outperformed six frontier models on HealthBench (Hard and Professional) while reducing potential clinical harm under blinded physician evaluation. Finally, a double-blind study of end-to-end generated papers with 30 domain experts across 450 reviews demonstrates that Co-Scientist's reliability modules reduce hallucination and plagiarism while improving research safety. Together, these results demonstrate progress toward closed-loop multi-agent scientific AI systems capable of accelerating real-world scientific discovery.

---


### 112. [Towards Expert Financial QA via Self-Improving RAG](https://arxiv.org/abs/2608.26706)

**<font color=#1a73e8>作者：</font>** Junjie Xiong, Shawheen Ghezavat, Aum Hirpara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expert-level financial question answering requires both grounded verification to catch numeric hallucinations and audit trails for regulatory compliance, attributes that standard single-pass RAG systems lack. We take a step toward this goal with Self-Improving RAG, a framework that decomposes document QA into three specialized agents (Retrieval, Reasoning, and Judge) coordinated by an orchestrator with feedback-driven self-correction. When the Judge Agent scores an answer below a dynamic threshold, the system triggers retry with escalated strategies: broader retrieval, more careful prompting, and relaxed acceptance criteria. We evaluate on FinanceBench (SEC filing QA), where Self-Improving RAG achieves 86% oracle-guided accuracy (measuring agreement with gold answers) with a 36.4% Lazarus Rate, recovering nearly 4 in 10 initially incorrect answers through targeted retry. A key finding is that a fixed retrieval pipeline with judge-driven retry achieves strong results without dynamic routing, providing full interpretability. Every decision is logged with confidence scores, enabling the audit trails required for regulated financial applications.

---


### 113. [AesCanvas: A Large-Scale Dataset and Benchmark for Aesthetic Critique and Contextual Suitability](https://arxiv.org/abs/2608.26713)

**<font color=#1a73e8>作者：</font>** Xuanwei Hu, Haoyu Dong, Kejun Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) have extended Image Aesthetic Assessment (IAA) beyond scalar scores toward interpretable critique and guidance. Yet existing benchmarks mainly assess intrinsic visual quality or fixed domain criteria, leaving open whether an appealing image is appropriate for a specific purpose, audience, cultural setting, or domain convention. We introduce AesCanvas, a unified suite with two complementary components: CritiqueCanvas with 519,136 instruction-response pairs from 54,300 images supports long-form, multi-dimensional critique across photography, painting, and virtual imagery, whereas ContextCanvas with 301 expert-reviewed use scenarios evaluates contextual aesthetic suitability in realistic use scenarios. Under a unified protocol, we evaluate closed-source frontier, open-weight general, and aesthetic-specific MLLMs. Results reveal a clear separation between critique generation and context-sensitive judgment: reference-based lexical and semantic metrics only partially capture critique quality, while aesthetic specialists remain competitive on selected critique metrics yet substantially lag strong general-purpose MLLMs on ContextCanvas. Further analyses show that aesthetic specialization does not reliably transfer to contextual suitability and that model decisions may fail to track or ground themselves in decisive contextual visual cues. These findings establish culturally situated, evidence-grounded suitability as a distinct objective for aesthetic modeling.

---


### 114. [RegulAR: Graph-Grounded Error Recognition and Assistance for Procedural Tasks in AR](https://arxiv.org/abs/2608.26715)

**<font color=#1a73e8>作者：</font>** Yi-Lin Ye, Jindu Wang, Hiu Tung Wong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Errors are inevitable in procedural tasks, yet most AR guidance systems focus on step-by-step instruction delivery rather than helping users recognize and recover from mistakes. We present RegulAR, an AR task assistant for procedural error recognition and recovery. RegulAR models task instructions as a hierarchical dependency graph and combines this structure with a Multimodal Large Language Model (MLLM) to interpret egocentric observations during execution. This enables RegulAR to track progress, identify deviations by error type, estimate their impact on later steps, and deliver appropriately salient interventions through an in-situ head-up display that visualizes task state and recovery guidance. By making procedural structure explicit, RegulAR supports not only next-step guidance, but also reasoning about what went wrong, why it matters, and how users can get back on track. In a within-subject study (N=12), participants reported better task-structure understanding and recovery support with RegulAR than the MLLM-only baseline.

---


### 115. [Beyond Atomic Layouts: Compositional Design Understanding with Vision-Language Models](https://arxiv.org/abs/2608.26716)

**<font color=#1a73e8>作者：</font>** Yiyang Huang, Zhaowen Wang, Simon Jenni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Layout understanding, or the interpretation of element organization, is essential for document analysis, user interface (UI) creation, and graphic design. While recent vision-language models (VLMs) excel at interpreting atomic layouts composed of independent elements, they struggle with compositional layouts that require reasoning over visually entangled elements within hierarchical multi-layer structures. In this paper, we introduce a new task, compositional layout understanding, and present CoDeLayout, a VQA dataset of ~20K real-world multi-layer layouts annotated with compositional element pairs and design intent. Through empirical analysis on CoDeLayout, we identify two key challenges for existing VLMs: semantic drift between textual metadata and visual content, and structural ambiguity in hierarchical inter-element relationships. To address these challenges, we propose MASON, a post-training paradigm that integrates multimodal alignment (MA) and structural perception (SP). MA enhances element interpretation by grounding metadata-defined elements to their visual counterparts, mitigating semantic drift, while SP models layer-aware inter-element spatial relationships to improve hierarchical understanding and reduce structural ambiguity. Experiments reveal substantial gaps in existing VLMs: even the strongest baseline, GPT-o3, achieves only 79.68% accuracy, whereas Qwen2.5-VL 7B with MASON reaches 91.66%. Notably, MASON surpasses full-data Direct Finetune using only 30% of the training data and scales better with additional data.

---


### 116. [UniGeo: A Multi-modal Large Language Model for Text-Guided Cross-View Geo-Localization](https://arxiv.org/abs/2608.26722)

**<font color=#1a73e8>作者：</font>** Jiahao Wen, Hang Yu, Zhedong Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided drone geo-localization aims to identify a target region in a large-scale image gallery from a natural-language description. Existing methods mainly formulate this task as direct matching between an open-ended text query and candidate images. However, incomplete queries and highly similar candidates often make global cross-modal matching insufficient for reliable fine-grained localization. We propose UniGeo, a unified multimodal large language model (MLLM) for text-guided drone geo-localization. Built on a shared vision-language framework, UniGeo jointly supports geo-semantic understanding, cross-view semantic generation, and candidate-level verification. Specifically, it establishes stable correspondences among local scene elements, spatial relations, and language descriptions through geo-semantic learning, and further models semantic mappings between drone and satellite views through cross-view generation. Based on these capabilities, a plug-and-play verification module performs fine-grained discrimination among highly confusable candidates. We further introduce a multi-stage training strategy that progressively learns geo-semantic understanding, cross-view generation, and candidate verification, improving adaptation to text-guided geo-localization. Experiments demonstrate consistent improvements across multiple retrieval backbones. On GeoText-1652, UniGeo improves R@10 and mAP by 13.59 and 2.83 percentage points, respectively, validating its effectiveness for fine-grained text-guided drone geo-localization.

---


### 117. [Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training](https://arxiv.org/abs/2608.26730)

**<font color=#1a73e8>作者：</font>** Tingyun Li, Wenfeng Feng, Weiqing Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models offer broad capabilities, but adapting them to evolving domains, tools, and requirements often entails repeated post-training. Autonomous systems automate parts of this process by proposing updates, training candidates, and using evaluation feedback to select subsequent proposals. As evidence accumulates, a central problem emerges: which past update evidence remains actionable after subsequent training has changed the parent model? An update's effect depends on its parent, data, and training stage. Treating past success as context-free permission can waste compute. If the resulting child is promoted, it can also degrade the subsequent training trajectory. We formulate this problem as conditional experience transfer and introduce Boundary-Calibrated Intervention Transfer (BCIT), a method that authorizes experience reuse before weight-changing training. BCIT binds an observed effect to its source context, checks applicability conditions, vetoes candidates with named hard conflicts, and obtains current-state evidence through a bounded training trial when needed. Fully trained candidates still face a shared adoption rule, and only observed events extend memory. On one 4B model adapted across finance reasoning, text-to-SQL, and function calling, candidate updates exhibit heterogeneous target and retention effects across the evaluated contexts. Under matched candidates, evidence, and compute, BCIT authorizes fewer harmful updates and attains higher equal-budget final-model quality than the evaluated alternatives. These results support treating experience authorization as a distinct problem in autonomous post-training.

---


### 118. [Rethinking Message Passing as Retrieval for Text-Attributed Graph Learning](https://arxiv.org/abs/2608.26732)

**<font color=#1a73e8>作者：</font>** Jintang Li, Yuhong Chen, Ruofan Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are typically conceptualized as message-passing neural networks, yet it remains unclear why neighborhood aggregation reliably outperforms node-wise multilayer perceptrons (MLPs). Despite its empirical success, this paradigm can be computationally expensive and sensitive to imperfect graph structures. In this work, we present a retrieval-augmented view of GNNs: each layer makes predictions by applying an MLP to a node representation together with a permutation-invariant summary of retrieved graph context. Motivated by this perspective, we propose RTA, a simple MLP-based framework that replaces structural message passing with label-aware retrieval and propagation. We provide theoretical insights that (i) connect retrieval-based aggregation to softmax-attention message passing, and (ii) establish the robustness of retrieved-context supervision to mis-retrieved outliers. Experiments on multiple text-attributed graph benchmarks show that RTA matches or even outperforms strong GNN and graph LLM baselines while improving efficiency and robustness across diverse scenarios.

---


### 119. [Daydreaming: Stealing Hidden Agent Skills through Black-Box Task Interaction](https://arxiv.org/abs/2608.26733)

**<font color=#1a73e8>作者：</font>** Yu-Lin Tsai, Yu-An Lu, Ci-Yang Tsai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills bundle instructions, reference data, and executable helpers that let a general agent perform specialized tasks. Hosted providers can keep these files secret while selling access to task results, making the skill itself a valuable target. Existing disclosure defenses can block requests that ask for the skill or reproduce its text, but they cannot block customers from submitting the ordinary tasks the service is built to complete. We present Daydreaming, an execution-only attack that steals a multi-file skill through black-box task interactions. The victim is never asked to reveal the skill or grade a reconstruction. Instead, Daydreaming adaptively creates crafted tasks whose results distinguish possible hidden behaviors. It tests individual behaviors, uses attacker-controlled shadow agents to choose a design, and completes each file using stored victim results and local execution checks. We formalize three nested threat levels of access as Differential, Trace, and Output, and focus on Output, where the attacker sees only the final response and returned files. Across 7 skills and 4 victim models, Daydreaming recovers 86.8% of the original skill's capability at Output, outperforming SigLeak by almost 4x. It produces installable skills using a median of 32 victim calls per skill even with disclosure defenses enabled. These results show that hiding skill files and filtering direct disclosure do not, by themselves, prevent functional reconstruction through normal use.

---


### 120. [Preserving General Capabilities during Domain Specialization with Uncertainty-Calibrated MOPD](https://arxiv.org/abs/2608.26735)

**<font color=#1a73e8>作者：</font>** Ziyuan Liu, Jiao Ou, Jian Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Specializing large language models to vertical domains improves domain-specific behavior but often degrades general capabilities such as reasoning, coding, instruction following, and creative writing. We study this domain--general trade-off in Multi-Teacher On-Policy Distillation (MOPD), where a specialized student is supervised on its own sampled trajectories by domain and general teachers. Standard MOPD faces two limitations: ordinary on-policy sampling rarely exposes tokens with large positive teacher--student advantages, while the advantage sign alone does not establish whether the resulting update direction is reliable. We propose uncertainty-calibrated MOPD to address these limitations. Dual-temperature sampling broadens the candidate trajectory pool, and positive-advantage-density filtering selects trajectories with stronger positive learning signals. Centered log-likelihood (CLL) filtering then computes an entropy-calibrated teacher-endorsement score and probabilistically retains token updates according to direction--endorsement consistency. Experiments on role-playing and medical-domain specialization show that our method improves the general-capability average over standard MOPD by $4.73\%$ and $10.84\%$, respectively, while maintaining vertical-domain performance. Ablations and diagnostic analyses further confirm that the gains do not merely result from a larger rollout budget and that the proposed trajectory- and token-level mechanisms address their intended failure modes.

---


### 121. [Graph-Guided Selective Unlearning for Language Models: Controlling Support Routes Beyond Forget Seeds](https://arxiv.org/abs/2608.26743)

**<font color=#1a73e8>作者：</font>** Waqas Khan, Tabinda Sarwar, Jingyue Cong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprises fine-tune language models on proprietary data that may later require removal due to privacy, contractual, or compliance obligations. Selective unlearning removes requested knowledge while preserving model utility, offering a practical alternative to full retraining, but existing methods treat the explicitly identified forget examples as the complete deletion scope. This is insufficient when target knowledge remains recoverable through paraphrases, aliases, or neighboring training examples. We propose GRAPHSU, a graph-guided controller that expands the deletion scope beyond forget seeds by constructing a weighted support-route graph, propagating deletion pressure through it, and applying graded forgetting strengths to high-risk neighbors. On the Task of Fictitious Unlearning (TOFU), a synthetic author-profile question-answering benchmark, and PISTOL, a structural-unlearning benchmark built around interconnected factual samples, with GPT-2 Medium and Llama-3.2-3B-Instruct, GRAPHSU achieves the lowest utility-feasible soft leakage across all deletion settings, reducing leakage by up to 49.5 percentage points over a matched seed-only baseline, demonstrating that effective enterprise unlearning requires controlling support routes, not just forget seeds.

---


### 122. [G2D: Generative-to-Discriminative Collaborative Inference for Zero-Shot Image Classification](https://arxiv.org/abs/2608.26744)

**<font color=#1a73e8>作者：</font>** Zehua Hao, Fang Liu, Qinliang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot classification needs efficient label retrieval and fine-grained visual reasoning, yet discriminative and generative vision-language models fail in complementary this http URL CLIP's top-1 prediction is wrong, the correct label often remains in its top-$K$ shortlist, making disambiguation rather than recall the key this http URL generative models, however, are hindered by large label spaces and unconstrained this http URL complementarity motivates separating broad candidate retrieval from fine-grained, image-grounded this http URL propose G2D, a training-free framework that uses a generative VLM to verify CLIP-retrieved candidates against the this http URL names and CLIP probabilities provide a structured prior for resolving visually similar this http URL confidence routing, entropy-adaptive candidate sizing, and trie-constrained decoding focus generative reasoning on uncertain samples and ensure one valid output for each input at test this http URL eight benchmarks, G2D achieves 68.85% average accuracy, versus 59.35% for CLIP and 63.11% for the standalone this http URL seven generator configurations, candidate-set verification improves average accuracy by 1.08--27.42 percentage points.G2D also transfers to DCLIP, WaffleCLIP, and CuPL, supporting a practical interface between discriminative proposal and generative visual reasoning. Code: this https URL

---


### 123. [AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design](https://arxiv.org/abs/2608.26747)

**<font color=#1a73e8>作者：</font>** Mingquan Liu, Jiangyu Chen, Hanqun Cao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific LLM agents have shown promise in literature reasoning, tool use, and experiment planning, but it remains unclear whether they can autonomously improve large, tightly coupled scientific machine-learning systems through executable code changes and computationally expensive validation. We study this question in protein folding, where progress requires coordinated architectural modifications, multi-objective evaluation, and domain-aware interpretation. We present AgentFold, a multi-agent framework that formulates folding-model development as a closed-loop search over executable code variants. Starting from ESMFold, AgentFold proposes hypotheses, implements and debugs code-level modifications, evaluates model variants, analyzes experimental outcomes, and stores both successful and failed interventions in structured memory. An MCTS-style policy allocates computational resources across high-scoring search branches. On an engineering-scale protein-folding codebase comprising more than 2,000 lines of code, AgentFold explores approximately 80 model variants using approximately 5,000 GPU-hours and 170 million LLM tokens. Under a matched computational budget, AgentFold improves the best lDDT by 7.5% over independent Codex proposals and outperforms a random-search control. Beyond model improvement, the resulting intervention traces reveal recurring empirical design patterns: stable gains tend to arise from early, soft, learnable priors and gated refinement, whereas direct geometric perturbations and geometry-conditioned feedback often destabilize training. The code and experimental resources are publicly available at this https URL.

---


### 124. [Discovering Relationships in Data Lakes Using Large Language Models: An Industrial Case](https://arxiv.org/abs/2608.26750)

**<font color=#1a73e8>作者：</font>** Ahlame Diouan, Eric Ferey, Sabine Loudcher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data lakes rely on metadata to remain usable, yet this meta data is often limited or weakly informative for column relationship discovery, especially in ERP-derived datasets with coded or abbreviated schema labels. We propose ColRel, a two-stage method that builds column embeddings from metadata and data available at ingestion time. In difficult cases, such as coded schemata, business dictionaries help better interpret column names and support the generation of short natural-language descriptions used in the second stage. Experiments on public benchmarks and an industrial ERP dataset show that ColRel is particularly effective in semantically related, weak-signal settings.

---


### 125. [DEEPCHART: How Far are LLMs from Faithful Data-Science Chart Generation?](https://arxiv.org/abs/2608.26757)

**<font color=#1a73e8>作者：</font>** Jiahui tang, Kuicai Dong, Dexun Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Faithful chart generation in real-world data-science workflows requires grounding visualizations in scattered evidence, computing chart-ready quantities, and rendering them accurately. Modern LLMs can produce visually plausible, instruction-compliant charts, yet data-level hallucinations remain difficult to detect in long, noisy, and multimodal contexts. To measure this gap, we introduce DEEPCHART, an expert-annotated benchmark of 1,482 task-conditioned chart-generation instances drawn from real-world scientific papers, financial filings, and ecosystem reports. DEEPCHART formulates chart generation as an Extract--Reason--Visualize pipeline and evaluates source-data extraction, derived-data reasoning, and chart rendering stage by stage. Experiments with state-of-the-art models show that visually plausible charts often conceal data-level hallucinations, with extraction and reasoning errors common in realistic long and multimodal settings. These findings suggest that larger context windows alone are insufficient; faithful chart generation also requires reliable evidence extraction and quantitative reasoning before rendering. Our benchmark and associated resources are available at this https URL.

---


### 126. [Equal Ranking Quality, Different Decisions: Training Order-Consistent LLM Scorers](https://arxiv.org/abs/2608.26762)

**<font color=#1a73e8>作者：</font>** Markus Frohmann, Mahdiyar Alavi, Elizabeth Lingg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rerankers, reward models and multi-document QA scorers score candidate documents or responses in one LLM prompt, so each score depends on their order. Such scorers are selected on ranking quality, but their scores determine a decision: what a score threshold retains, a reader answers, or a preference model selects. However, equal ranking quality does not imply equal decisions: on passage reranking, five trained scorers within 0.010 nDCG@10 retain sets that overlap by only 0.66-0.84 when reordered. A published reranker takes the highest retained-set F1 in our comparison and still overlaps by only 0.667. No prompt-time change we test removes that order dependence: the only one that gains ranking quality leaves all three decisions unchanged. Order-consistency SFT (OC-SFT) attenuates it in the weights, training a candidate's score not to depend on the order. It holds ranking quality and leads every decision-stability measure among trained scorers on all three tasks: it flips the reader's answer on 0.125 of permutation pairs against 0.149-0.164 for three other objectives that target order. It is more stable than order-averaged distillation on 12 base models, and one OC-SFT permutation retains sets that overlap more than ten averaged off-the-shelf permutations. A comparison should therefore report what a threshold retains and a reader answers, not ranking quality alone. Code is available at this https URL.

---


### 127. [Instruction Quality Matters: Refining Instructions for Effective Preference Learning](https://arxiv.org/abs/2608.26779)

**<font color=#1a73e8>作者：</font>** Seohyeong Lee, Hwaran Lee, Buru Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference learning optimizes models using response pairs, yet the informativeness of these pairs is fundamentally shaped by the instructions from which they are generated. We identify instruction quality as a hidden bottleneck in preference learning: low-quality or ambiguous instructions restrict the response-quality distribution, limiting strong chosen responses and weakening preference signals. Through Best- and Worst-of-N analyses, we show that instruction quality constrains both the ceiling and floor of sampled response quality. Motivated by this observation, we introduce an instruction-refinement pipeline that selects weak instructions using reward signals and revises them with rubric-guided LLM feedback, improving preference data without discarding examples. Across offline and online preference learning settings, experiments on multiple models and benchmarks show broad alignment improvements over original data and alternative data-improvement strategies. Further analyses indicate that instruction refinement raises achievable response quality and complements response-centric preference data curation. Overall, instruction quality emerges as a key factor governing how informative preference signals are formed for LLM alignment. Code is available at: this https URL

---


### 128. [AI Control Scientist: LLM-driven Agentic System for Automated Control Design](https://arxiv.org/abs/2608.26780)

**<font color=#1a73e8>作者：</font>** Haiteng Wang, Weihao Li, Jing Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Control system design is critical for modern industry, such as chemical process temperature regulation and aero-engine control. However,traditional control design workflows rely heavily on expert knowledge and extensive manual parameter tuning, resulting in limited efficiency and scalability. To this end, this paper proposes AI Control Scientist (AICS), the first large language model (LLM)-driven agent capable of automatically generating optimized controller from language design requirements. Specifically, a Task Modeling Agent interprets user requirements to engineering constraints; a Controller Design Agent generate candidate controller structures and executable code; and a Parameter Tuning Agent refine controller parameters under closed-loop performance criteria. Experiments demonstrate that the proposed agentic system can automatically generate multiple representative control systems, outperforms existing automated baselines in both design success rate and optimization efficiency. This work has the potential to transform control system design from human-driven to agent-driven, paving the way for model predictive control and other advanced control systems design.

---


### 129. [Decoupling Planning and Control for Instructable Agents](https://arxiv.org/abs/2608.26788)

**<font color=#1a73e8>作者：</font>** Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model controller to act autonomously at high frequency when conditioned on sparse, higher-latency, and high-level text instructions generated by a VLM planner. To train controllers to be language-instructable, we relabel segments of controller policy rollouts with synthetic instructions and jointly optimize a behavior-cloning objective along with existing reward-maximizing and world-modeling objectives. We evaluate our proposed approach across seven embodied environments, including three multi-agent environments where VLM planners coordinate through language while trained controllers serve as their actuators. Under matched observation and action spaces, our decoupled approach consistently outperforms controller-only and direct VLM action-generation variants, preserves fast control, and lets us swap in different pretrained VLM planners without fine-tuning, while remaining competitive with strong vision-language-action and multi-agent RL baselines on six of seven tasks.

---


### 130. [On the Indistinguishability of Human v/s AI Generated Text](https://arxiv.org/abs/2608.26797)

**<font color=#1a73e8>作者：</font>** Jaee Ponde, Aritra Das, Mihir More 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid improvement of LLMs has made distinguishing AI-generated text from human writing a pressing problem. This challenge is further amplified by paraphrasing tools designed to make machine-generated text appear more "human". We study how access to human writing samples can be used to strategically paraphrase machine-generated responses toward the human distribution. Under a multi-sample setting with human and machine responses to the same prompts, we show that repeated paraphrasing moves the machine distribution toward the empirical human distribution under simple mixing and stability conditions. Our results derive an explicit convergence rate, extend the analysis to a finite-sample setting, and characterize how the required number of human samples and paraphrasing rounds scale with the desired error.

---


### 131. [Multi-Image Visual Token Pruning in Large Visual Language Models](https://arxiv.org/abs/2608.26806)

**<font color=#1a73e8>作者：</font>** Rongyang Zhang, Chengqiang Lu, Cong Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the growing demand for processing multiple image sequences in real-world applications, various visual token pruning methods have emerged to mitigate the computational and context length constraints faced by Large Vision Language Models (LVLMs). However, most existing pruning approaches rely on static strategies that struggle to adapt across different architectural LVLMs and multi-image scenarios, and are additionally constrained by their dependence on attention computations that are incompatible with efficient techniques like FlashAttention. To address these limitations, we propose a training-free, Adaptive Visual Token Pruning (AVTP) framework, applicable to diverse LVLM architectures. We strategically determine pruning layers based on empirical analysis of visual attention distributions across various LVLMs, and implement adaptive pruning ratios in multi-image contexts where images of higher importance retain proportionally more tokens. We conduct extensive experiments across different LVLMs to demonstrate the effectiveness and robustness of AVTP. Specifically, Qwen3VL-8B achieves 2 times inference speedup while maintaining 96.1\% of its original accuracy on multiple multi-image benchmarks, InternVL3.5-8B retains 94.1\% accuracy, and LLaVA-OV-7B even exceeds its original baseline performance. Our code is available at \href{this https URL}{this link}.

---


### 132. [Behavior2Trip: Towards Personalized Travel Planning via User Behavior Trajectory](https://arxiv.org/abs/2608.26807)

**<font color=#1a73e8>作者：</font>** Zihao Cheng, Yingyu Shan, Hongru Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Travel planning agents assist users in generating personalized travel plans by modeling their individual preferences. Existing agents either rely on explicit user instructions or engage in multi-turn clarification to elicit user preferences. However, both approaches overlook the rich behavioral signals latent in users' past behaviors, which implicitly encode their preferences. This over-reliance on active user input increases interaction burden and limits plan personalization. To bridge this gap, we introduce a new task, Behavior-Aware Travel Planning, which infers user preferences directly from past behaviors and generates personalized travel plans. To facilitate research on this task, we introduce Behavior2Trip, a benchmark constructed from one of the largest Chinese online travel platforms, comprising 11,400 instances. Each instance represents an average of 39.8 past user behaviors spanning 14 attributes across 5 preference dimensions. We further propose B2T-Agent, a reinforcement learning-based agent that leverages user behavior trajectories, interacts with external tools for preference-aligned retrieval, and maintains an internal memory module. Experiments on Behavior2Trip show that GPT-4.1 achieves a full-constraint pass rate of only 0.5\% on the hardest tasks, while B2T-Agent built upon Qwen3-8B outperforms all baselines, highlighting the substantial challenge of this task. Moreover, Qwen3-8B trained with B2T-Agent also outperforms GPT-4.1 on the TravelPlanner benchmark, demonstrating strong generalization. Code and data are available at this https URL

---


### 133. [Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning](https://arxiv.org/abs/2608.26809)

**<font color=#1a73e8>作者：</font>** Chenyang Wu, Fuchen Long, Binyuan Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While generative AI has significantly advanced video editing, existing methods primarily focus on single-shot or short video clips. Editing long videos with multiple instructions remains a formidable challenge. Naive chunking strategies, e.g., fixed-duration segmentation, often lead to entity fragmentation, severe editing hallucinations, and disrupted temporal continuity. To bridge this gap, we introduce the Multi-Instruction Multi-Shot Long-Video Editing (MMLVE) task, which is structured around three core objectives: Cross-Shot Editing Consistency (CSEC), Multi-Instruction Decoupling (MID), and Zero-Destruction on Spatiotemporal Structure (ZDSS). To tackle these three unique challenges, we introduce an agentic editing framework that leverages the synergy of Large Language Models (LLMs) and Vision-Language Models (VLMs) to achieve shot-level video decoupling and precise instruction parsing. Furthermore, to comprehensively evaluate this task, we construct MMLVE-Bench, which is an MMLVE-focused dataset characterized by complex real-world spatiotemporal dynamics, high-density heterogeneous instructions, and sparse, random entity distributions. Three MMLVE-focused evaluation metrics are further exploited to assess the quality of the editing results. Extensive experiments demonstrate that our MMLVE-Agent outperforms existing closed-source SOTA approaches (e.g., Seedance 2.0), successfully eliminating editing hallucinations, preserving cross-shot editing consistency, and attaining seamless spatiotemporal transitions.

---


### 134. [LLaVAFlow: Preserving Latent Alignment Flow for Parameter-Efficient Multimodal Fine-Tuning](https://arxiv.org/abs/2608.26820)

**<font color=#1a73e8>作者：</font>** Muyao Yuan, Muyan Jiao, Jiangyong Ying 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) exhibit strong generalization, visual instruction tuning for downstream tasks inevitably causes catastrophic forgetting, impairing overall generalization. While existing methods regulate weight updates to reduce forgetting, they overlook the fundamental cross-modal alignment in MLLMs. Based on prior work and our observations, we argue that cross-modal alignment is implicitly captured in the information-compression trajectory. To preserve the alignment flow embedded in the trajectory, we propose LLaVAFlow, an information-theoretic distillation framework. First, we compress the mutual information between the extracted relations and MLLM embeddings, encouraging a learnable module to produce a refined alignment flow that benefits downstream tasks. Second, we maximize the mutual information between the extracted alignment flows of the pretrained and fine-tuned MLLMs, enabling the transfer of compact alignment information. Extensive experiments show that LLaVAFlow is an effective plug-and-play framework that preserves alignment flow and enhances both downstream performance and generalization.

---


### 135. [SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting](https://arxiv.org/abs/2608.26829)

**<font color=#1a73e8>作者：</font>** Haizhao Fan, Xinyi Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting models operate on raw numerical sequences, lacking the semantic knowledge that domain experts implicitly leverage, such as the physical meaning of each variable, its statistical behavior, and its temporal dynamics. Recent efforts to bridge this gap fall into two camps. Some rely on large language models at inference time, which is computationally expensive. Others apply uniform textual prompts at the dataset level, ignoring the heterogeneous semantics across individual variates. We propose SAGE (Seeing and Augmenting with Grounded Encoding), an end-to-end CLIP-based framework that jointly models temporal, cross-variable, textual, and visual information. The CLIP text encoder processes frequency-enhanced patches and variable tokens, while gated residual paths inject variable-specific descriptions and statistical descriptors. In parallel, the frozen CLIP vision encoder aligns rendered series with temporal representations through a training-only contrastive objective. This dual use of CLIP adds complementary semantic and visual supervision without placing an LLM in the forecasting loop. Across eight long-term benchmarks and M4, SAGE achieves state-of-the-art accuracy. Ablations confirm complementary gains from multimodal alignment and variable-level knowledge.

---


### 136. [RuleWeaver: Benchmarking Rule-Centered Scenario Reasoning for Large Language Models](https://arxiv.org/abs/2608.26832)

**<font color=#1a73e8>作者：</font>** Bohan Yu, Shi-Yang Li, Pengfei Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly applied to specialized domains, where effective use of domain expertise often requires reasoning over complex rules in concrete scenarios. However, existing benchmarks only partially evaluate this capability, as they either focus on output-level instruction constraints or overlook the distinct roles that rules play in scenario reasoning. To address these gaps, this paper introduces RuleWeaver, a benchmark construction framework for evaluating rule-centered scenario reasoning. RuleWeaver starts from corpus-derived IF-THEN Meta Rules, progressively augments them into complex rules, and composes these rules into rule-centered scenario QA instances. Beyond final-answer correctness, RuleWeaver further supports process-level evaluation through rubric-based answer quality, rule recall, and rule precision. Experiments on 11 representative LLMs show that current models still struggle with complex rule-centered scenario reasoning, with even the best-performing model achieving only around 50% of the maximum rubric score. We make our code and dataset available here: this https URL.

---


### 137. [SymbolLKG: Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers](https://arxiv.org/abs/2608.26836)

**<font color=#1a73e8>作者：</font>** Haizhao Fan, Yuchi Xiong, Jize Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable proficiency in natural language understanding, yet they struggle with strict multi-step reasoning, frequently suffering from hallucinations and inconsistency. Existing solutions like Chain-of-Thought (CoT) lack rigorous verification mechanisms, while standard Retrieval-Augmented Generation (RAG) often misses the complex, structural dependencies inherent in logical tasks. To bridge this gap, we propose a Neuro-Symbolic architecture that integrates a Logical Knowledge Graph (LKG) with dynamic solver routing. Specifically, we introduce an ontology-based LKG that treats logical rules and constraints as first-class topological nodes, enabling explicit modeling of dependencies extracted from text. We further design a Logic Router to dynamically dispatch tasks to the optimal symbolic engine, which is supported by a topology-aware hybrid retrieval mechanism. Experimental results on logical reasoning benchmarks demonstrate that our framework significantly outperforms state-of-the-art prompting and RAG baselines, delivering higher accuracy and verifiable reasoning paths.

---


### 138. [Are We Shooting Flies with Cannons? Trade-off Analysis for AI-based 5G Intrusion Detection](https://arxiv.org/abs/2608.26844)

**<font color=#1a73e8>作者：</font>** Federica Uccello, Simin Nadjm-Tehrani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of Artificial Intelligence (AI) in network intrusion detection raises the question of whether complex and computationally expensive models are justified for this task. In this work, we investigate the trade-off between detection performance and computational cost for intrusion detection in 5G network telemetry. We compare traditional machine learning (ML) models, including XGBoost as a representative of tree ensemble, and TabNet for tabular deep neural network (DNN), with a large language model (LLM) used as a general-purpose intrusion detector. The LLM is evaluated under both zero-shot and few-shot prompting configurations. We evaluate the models in terms of detection performance, inference time, and CPU time as a proxy for energy efficiency. Using a relatively large available 5G dataset, we show that traditional ML models consistently achieve near-perfect detection performance with negligible inference time, while LLM-based approaches perform significantly worse and incur orders-of-magnitude higher CPU usage. Few-shot prompting improves recall, but at the cost of lower accuracy and further increased CPU time, without closing the performance gap. These findings indicate that, for tabular intrusion detection in 5G networks, XGBoost offers a substantially better performance-cost trade-off than DNNs and LLMs, highlighting the importance of selecting models based on task suitability rather than increasing complexity.

---


### 139. [Evaluating Confidence-Gated Retrieval with Matched Trajectory Replay](https://arxiv.org/abs/2608.26846)

**<font color=#1a73e8>作者：</font>** Prateek Chhikara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interactive language-model agents use confidence signals to decide whether to answer immediately, retrieve additional evidence (from memory or external knowledge), or defer. Yet confidence is usually evaluated in isolation, without measuring the trajectory-level consequences of the actions it triggers. We propose matched trajectory replay, a controlled protocol for comparing confidence-to-action mappings. The protocol holds candidate answer states, evidence points, budgets, and action costs fixed. We use it to compare raw verbalized confidence with post-hoc isotonic calibration in a multi-hop question-answering system using Mistral, GPT, and Qwen models on HotpotQA and MuSiQue datasets. At the same numerical commitment threshold, calibration changes which questions agents ultimately commit to answering. Across all six model-dataset pairs, it increases accuracy among committed answers by up to 41 percentage points. However, it can reduce coverage and increase retrieval use. Overall accuracy improves by up to 15 percentage points on HotpotQA but falls by up to 17 percentage points on MuSiQue. These effects reflect a shift to a more selective, lower-risk operating point, not improved answers or confidence ranking. A calibration map fitted before retrieval improves held-out calibration through retrieval depths one and two, but is worse than raw confidence at depth three for all three models. Additional evidence helps on average, but this aggregate effect does not establish whether confidence identifies which individual episodes will benefit from another retrieval. Taken together, these results show that calibration can make commitment risk interpretable, but it does not estimate the expected benefit of another retrieval. Retrieval therefore requires a separate value-of-information or utility estimate. Evaluations should report held-out calibration, risk-coverage, and retrieval cost.

---


### 140. [MedFG-VQA: Low-Frequency Memory and Graph Attention for Lightweight Medical VQA](https://arxiv.org/abs/2608.26848)

**<font color=#1a73e8>作者：</font>** Haowen Gu, Gensheng Pei, Zeren Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Visual Question Answering (Med-VQA) holds significant promise for clinical decision support, yet faces challenges due to limited annotated data and the high computational demands of existing large vision-language models. We propose MedFG-VQA, a lightweight framework that leverages a memory bank to augment DCT-based low-frequency features and employs graph-enhanced cross-attention for effective visual-textual alignment. Specifically, our approach features two key components: Frequency-Memory Fusion (FMF), which enhances low-frequency features by retrieving from a learnable memory bank built on DCT decomposition, and Graph-Aware Cross-Attention (GACA), which aligns visual-textual features via cross-attention and refines them through graph-convolutional aggregation. To address data scarcity, we construct SynMed-VQA, a large-scale synthetic dataset comprising over 2 million question-answer pairs across 9 imaging modalities and 10 major organs, generated with GPT-4o. Extensive experiments on SynMed-VQA and three other standard biomedical VQA benchmarks demonstrate that MedFG-VQA achieves competitive or superior performance compared to much larger models while maintaining significantly lower computational costs, highlighting its efficiency and potential for clinical deployment.

---


### 141. [LiveSim: Simulating Environment-Shaped Users in Multi-Agent Live-Stream Ecosystems](https://arxiv.org/abs/2608.26849)

**<font color=#1a73e8>作者：</font>** Jiaqi Xu, Yiran Qiao, Jing Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User behavior simulation with large language models~(LLMs) is increasingly used to support multi-agent ecosystem simulation. Existing simulators typically rely on static user profiles inferred from historical observations, which become inadequate in socially intensive environments such as live streaming where interaction dynamics continuously reshape user behavior. We propose \textbf{LiveSim}, an LLM-based framework for live-stream ecosystem simulation. It represents users as editable behavioral hypotheses and progressively refines them through trajectory-grounded interactions, where discrepancies between simulated and observed trajectories reveal missing environmental shaping effects. These signals are further extracted as transferable environment-behavior patterns and accumulated in a collective behavioral memory to improve user-level behavioral fidelity and support ecosystem-level simulation. Experiments on real-world live-stream risk-control data validate the effectiveness of LiveSim in improving user-level behavioral fidelity and enabling ecosystem-level analysis of risk evolution and platform intervention effects.

---


### 142. [From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation](https://arxiv.org/abs/2608.26856)

**<font color=#1a73e8>作者：</font>** Haowen Gu, Gensheng Pei, Junzhu Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \textsc{\textsc{MedREAL}} (\textbf{Med}ical \textbf{RE}asoning-driven \textbf{A}nswering and \textbf{L}ocalization), a unified framework that seamlessly aligns linguistic reasoning with spatial grounding. Specifically, \textsc{MedREAL} introduces \textbf{S}eg \textbf{A}nchored \textbf{R}easoning \textbf{P}ooling (SARP) to distill task-relevant semantic evidence directly from \texttt{[SEG]} tokens within the MLLM's hidden states. Furthermore, a \textbf{R}easoning-to-\textbf{V}isual (R2V) fusion mechanism is proposed to effectively inject these reasoning-aware features into a segmentation pipeline for accurate mask decoding. To facilitate this paradigm, we construct MedRAVS-13K, a comprehensive dataset comprising 13,824 expertly validated samples across four diverse imaging modalities. Extensive experiments demonstrate that \textsc{MedREAL} significantly outperforms state-of-the-arts, achieving 68.49\% gIoU and 70.47\% cIoU on benchmark evaluations. By generating evidence masks that are strictly consistent with textual diagnoses, \textsc{MedREAL} provides a robust, interpretable framework for reasoning-driven medical image analysis.

---


### 143. [Order Matters: A Chinese Multi-Panel Meme Benchmark for Vision-Language Reasoning](https://arxiv.org/abs/2608.26866)

**<font color=#1a73e8>作者：</font>** Haihan Li, Haihao Li, Zhenfei Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many multimodal tasks depend on how visual elements are ordered and composed, not only on recognizing them in isolation. Internet memes are a compact case of this problem: their punchline often depends on a constrained reading order and cross-panel visual--textual cues. While large vision-language models (LVLMs) show strong performance on single-image understanding, it remains unclear whether they can perform sequence-aware reasoning over structured meme layouts, especially in Chinese social media. We introduce CMPM, a Chinese Multi-Panel Meme benchmark with 1,214 annotated samples covering five structural types, ordering dependency, panel-order constraints, and optional comment context. We formulate a two-layer evaluation: Task1 probes structure typing and order-sensitive panel sequencing (with a context ablation setting), and Task2 evaluates Chinese meme explanation generation with human ratings on five 1-3 Likert dimensions (visual, panel, humor, context, and faithfulness). We benchmark five representative LVLMs under a unified protocol. Results indicate that canonical-display accuracy is not by itself evidence of order understanding: the primary shuffled condition produces a sharp accuracy drop, revealing a persistent gap in order-sensitive multimodal reasoning. Task2 preferences place Gemini 3.1 Pro and GPT-5.5 above the open models, while comment context yields only a small and mixed Core4 gain. Code and data will be released upon acceptance.

---


### 144. [BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click](https://arxiv.org/abs/2608.26867)

**<font color=#1a73e8>作者：</font>** Mesut Toruk  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents reason, call tools, and act autonomously over many steps, but their agentic skills-correctly sequencing tools, planning under dependencies, judging untrusted inputs, and grounding generated arguments-are hard to measure with accuracy-only leaderboards. We present BekchiAI, which addresses both sides: a benchmark for measuring agentic skill and a platform for observing and controlling live agents. The BekchiAI-Benchmark, a suite of 13 tool-using ReAct agents across 7 task categories (arithmetic, structured/SQL, security detection, URL grounding, planning, orchestration, and tool-policy), totalling 2,057 deterministic, committed test tasks. Every task is verifier-checkable gold answers are computed by running canonical SQL against a real database, computing the exact schedule of a directed acyclic graph (DAG), or evaluating closed-form lambdas including adversarial security samples paired with deliberately imperfect signature scanners so a score reflects the model's own judgment, not the copying of an oracle. We define a small set of behavioral metrics beyond accuracy-tool-call adherence, URL hallucination and source-match, and per-model token cost and report a four-model comparison (Qwen3.7-Max, gemma-4-31B-it, gemma4:26b, gpt-oss-120b) whose story is in the per-family spread, not the aggregate. The benchmark runs are executed using the provided evaluation scripts. BekchiAI-Platform is a complementary web-based observability and control layer for deployed agents, providing full token and latency telemetry as well as remote run termination. The benchmark, evaluation tools, and platform are publicly released.

---


### 145. [C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning](https://arxiv.org/abs/2608.26870)

**<font color=#1a73e8>作者：</font>** Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such signals manifest. In this paper, we propose C-Unseen, a self-interpretable framework for weak signal detection in Dynamic Temporal Knowledge Graphs (DTKGs). We define a weak signal as a rare, semantically coherent subgraph that proliferates across consecutive TKG snapshots. The framework operates through two modules: a Rare Subgraphs Extractor, in which an LLM identifies subgraphs whose content is in tension with the dominant snapshot narrative via chain-of-thought reasoning, and a Weak Signal Alerter, in which the persistence of these rare subgraphs is tracked across time steps to isolate true weak signals. Experimental results demonstrate that C-Unseen outperforms keyword-, topic-, and graph-based baselines.

---


### 146. [Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher](https://arxiv.org/abs/2608.26872)

**<font color=#1a73e8>作者：</font>** Shiyi Zhang, Mushui Liu, Yunze Tong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD), which leverages a pre-trained, specialized teacher model to provide dense supervisory signals, has achieved significant success in Large Language Models (LLMs) and has recently been adapted to flow matching models. However, this paradigm suffers from two major issues: First, training a separate, task-specific teacher for every new objective incurs high computational costs. Second, the discrepancy between teacher and student distributions often leads to compounding errors along the generation trajectory. In this paper, we introduce \textbf{Self-OPD}, a teacher-free OPD framework for flow matching models that turns the student's own self-exploration into step-wise supervision. At each timestep, Self-OPD branches the deterministic next-state prediction into $K$ stochastic SDE candidates, rolls them out with the ODE sampler, and compares their rewards against a deterministic self-reference baseline to obtain normalized advantages. The velocity field is optimized with an all-branch pull-push objective, where high-advantage branches attract the student and low-advantage branches repel it under direction-aware attenuation and SDE-variance normalization. For multi-objective alignment, Self-OPD fuses normalized scores at the reward level, avoiding direct gradient conflict. Experiments on single and mixed reward benchmarks show that Self-OPD outperforms prior RL and OPD methods without task-specific teachers.

---


### 147. [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](https://arxiv.org/abs/2608.26882)

**<font color=#1a73e8>作者：</font>** Yitian Zhou, Jingyu Zheng, Qiliang Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial control systems (ICSs) rely on programmable logic controllers (PLCs) to connect networked computation with physical control. Tool-using large language model (LLM) agents represent an emerging attack threat: can an autonomous agent convert a network-reachable PLC into sustained adverse physical impact? However, existing evaluations focus on digital tasks or individual stages of PLC testing. In ICSs, evaluations that stop at software exploitation, an accepted write, or tool access may therefore mischaracterize physical risk.
We present PLCBENCH, to our knowledge, the first real-PLC hardware-in-the-loop (HIL) framework for characterizing this cyber-to-physical capability and its boundaries. It combines vendor-native interaction, commercial PLC execution, closed-loop reduced-order process simulation, and independent outcome verification. A deterministic evaluator applies fixed rules to runner, communication, PLC-object, and process records to assign six hidden diagnostic flags, distinguishing usable PLC interaction, process-linked manipulation, and sustained physical impact. We instantiate PLCBENCH on four commercial PLCs crossed with four closed-loop workloads. Across five LLM families and 240 real-PLC episodes, 75 episodes (31.3%) sustain their respective physical objectives. Stagewise results show that 98 episodes stop before a valid native read, whereas 62 reach a process-linked write but do not sustain the final objective. Notably, richer process observation is associated with an increase in conditional objective attainment after a process-linked write from 44.2% to 64.0%. These measurements localize failure in configured PLC-process deployments and identify intervention points for future defense evaluation. To support reproducibility, we release the safely disclosable PLCBENCH code and a software-only reproduction pipeline through the accompanying artifact.

---


### 148. [Evaluating human and LLM screening workflows in a conceptually complex scoping review: Recall--workload trade-offs and run-to-run consistency](https://arxiv.org/abs/2608.26885)

**<font color=#1a73e8>作者：</font>** Nikol Figalová, Lynn Huestegge, Anne Böckler-Raettig  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background. Large language models (LLMs) are increasingly used for screening in evidence synthesis, where false negatives can remove relevant studies before full-text assessment. We compared human and LLM title-and-abstract screening workflows in a preregistered study embedded in a conceptually complex scoping review.
Methods. After a conservative title-only screen, 1,131 records were screened by one review lead, four trained assistants screening non-overlapping subsets, and seven complete LLM runs using different models and processing configurations, including a nominally identical repeat run. We compared retained workload, operational recall against 316 verified eligible records, agreement, run-to-run consistency, and procedural burden. Because eligibility was verified only for records advanced and assessed in the parent review, recall estimates were operational.
Results. No workflow recovered all verified eligible records. The human workflows and two GPT-5.4 file-batch runs retained 42.2-45.0% of records while achieving 82.3-82.9% recall. Gemini 3.1 file batches achieved the highest recall (83.9%) but retained 56.7% of records. All-at-once configurations recovered fewer eligible records than corresponding file-batch configurations. Two nominally identical GPT-5.4 file-batch runs agreed on 91.7% of records but differed on 94 records, including 29 verified eligible records retained by only one run.
Discussion. LLM screening performance depended on the implemented workflow, not model identity alone. Processing configuration, workload, record-level variation, and human-LLM decision integration are therefore substantive properties of deployed systems. For high-recall tasks, LLMs are better suited to validated, auditable, human-supervised workflows than autonomous exclusion.

---


### 149. [Planting a Latent Variable in Natural-Looking Text: a More Realistic Test of Belief States in LLMs and Their Link to Concept Geometry](https://arxiv.org/abs/2608.26887)

**<font color=#1a73e8>作者：</font>** Alexandru-Iulius Jerpelea  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are thought to track "belief states," i.e., running probability distributions over the latent variables that govern language (Shai et al., 2024; Sarfati et al., 2026), but so far this has only been comprehensively demonstrated on toy synthetic data and in a few isolated case studies. It has also never been empirically connected to the geometry of LLM features (the concepts interpretability finds in model activations). In this work, we plant a controllable latent variable inside natural-looking text. An LLM teacher writes ordinary text while we "subliminally" steer it along one of K = 8 unrelated sparse autoencoder directions at each token, with the active directions following a ring-shaped Markov chain. A small transformer model trained on this corpus does indeed track the Bayesian posterior belief about our planted latent variable. Moreover, it also arranges the 8 states themselves on a ring, in the exact order of the Markov chain, which is supporting evidence that a concept's geometry can be formed by the statistical dynamics of the latent variable behind it.

---


### 150. [Counterfactual Bias Testing for Application Tracking System](https://arxiv.org/abs/2608.26899)

**<font color=#1a73e8>作者：</font>** Sai Yashwant, Shruti Bansal, Anurag Dubey 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated candidate-job matching systems are increasingly classified as high-risk AI under emerging regulation, yet auditing them for demographic bias is expensive: classical correspondence-audit studies require hand-crafted resumes and manual submission, which does not scale to fast pipeline retraining cycles. This paper presents a general, reusable methodology that (1) uses task-specialized LLM agents to synthesize identity-neutral base resumes and inject controlled demographic treatments across five protected-characteristic axes (sex/gender, age, residence, language, disability), producing a K x (1+N) correspondence-audit matrix; (2) qualitatively flags inferred protected characteristics per an EU AI Act-aligned prompt; (3) ranks candidates against a job description via a fine-tuned sentence-embedding model and cosine similarity; and (4) computes a nine-metric fairness suite spanning counterfactual (score delta, mean absolute rank change, flip rate), group-fairness (top-K retention, four-fifths/impact ratio), and merit-aware (Recall@K, nDCG@K, equal opportunity, equalized odds) families, each with bootstrap confidence intervals, significance tests, and Benjamini-Hochberg correction, culminating in an automated PASS/INVESTIGATE/FAIL report with a composite risk score. On an example corpus of 5 job orders, 100 base candidates, and 10 demographic treatments (90 metric x variant evaluations): score shifts, top-K retention, and merit-aware rate gaps stay within tolerance for every treatment, but a rank-stability metric (MARC) and nDCG@K each surface borderline findings - including one on the neutral baseline itself - that a score- or retention-only view would miss. The results argue for multi-metric, multi-family auditing over any single aggregate score, and for LLM-agent-generated audits as a practical, low-cost complement to human-curated audits for any candidate-job matching pipeline.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-231](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
