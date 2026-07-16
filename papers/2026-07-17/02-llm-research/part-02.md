# 🧠 大模型相关研究 | 2026年07月17日

> 本类共 **73** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-73**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-73**

---

### 51. [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705)

**<font color=#1a73e8>作者：</font>** Zichen Ding, Jiaye Ge, Shufan Jiang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) evolve into autonomous agents, the need for unified evaluation infrastructure becomes critical. However, current evaluation pipelines remain highly fragmented and tightly coupled, hindering reproducibility and causing redundant engineering. To address this, we introduce AgentCompass, an open-source, lightweight, and extensible infrastructure for evaluating LLM-based agents. AgentCompass organizes the evaluation process around three independent components, namely Benchmark, Harness, and Environment, thereby enabling flexible configurations without requiring the reimplementation of complex execution logic. Furthermore, it features a fault-tolerant asynchronous runtime and comprehensive trajectory analysis tools to transparently diagnose nuanced failure modes like reward-hacking. Natively supporting over 20 benchmarks across five capability dimensions, AgentCompass provides the community with a scalable and reproducible infrastructure for advancing agent research.

---


### 52. [The Test Oracle Problem in Synthetic LLM-as-Judge Corpora: Disappearance, Distortion and a Validation Protocol](https://arxiv.org/abs/2607.13707)

**<font color=#1a73e8>作者：</font>** Serkan Ballı  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Studies of bias in LLM-as-judge systems typically build synthetic corpora by prompting an LLM to generate a hallucinated answer to pair with a factual one, then presenting both to a judge. We report a case in which this generation step silently failed, and use it to argue that the failure mode is structural rather than incidental. In a multilingual (Turkish/English) faithfulness-judgment corpus, a decoding-budget parameter shared between judging and generation calls truncated one producer's hallucinated answers to a few words. The resulting items produced a large, statistically robust effect: a 32-point cross-lingual collapse in one judge's selection accuracy, replicated from N=50 to N=500, explained by a three-layer mechanistic account, and confirmed by a controlled producer-swap experiment, none of which was real. The effect vanished to ceiling once the shared parameter was corrected, and only manual reading of the raw generations, not any aggregate statistical check, exposed the fault. A second measured bias (Markdown-formatting preference) was not fabricated but distorted by the same fault, its magnitude and in one case its sign shifting with stimulus length, a mode aggregate metrics cannot distinguish from the first. We frame the underlying vulnerability using the test oracle problem: corpora whose negative examples are LLM-generated carry no mechanical way to verify item integrity, while corpora built by deterministic perturbation of a gold answer carry an item-level oracle for free. A positive control supports this claim directly: an analogous fault injected into a minimal perturbation-based corpus is caught with 100% accuracy by a zero-cost, zero-human gold-to-negative string comparison. We close with a validation protocol, derived from our own case, for analysts working in the oracle-less regime that we argue describes most contemporary multilingual LLM-as-judge corpora.

---


### 53. [Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal LLMs](https://arxiv.org/abs/2607.13712)

**<font color=#1a73e8>作者：</font>** Zhixiao Zheng, Zheren Fu, Zhiyuan Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid progress of Multimodal Large Language Models (MLLMs), they still suffer from untruthfulness issues, such as visual hallucinations, content fabrication, and unfaithful reasoning, which substantially undermine their faithfulness and practical utility. Alignment methods based on human preference, such as Direct Preference Optimization (DPO), have been widely adopted to address these issues. However, multimodal reasoning errors often propagate across stages, and final-answer errors can often be traced to mistakes in early grounding stages, yet standard DPO typically applies preference optimization at the final-answer level. This credit-assignment challenge means that supervision for early grounding stages is indirect rather than stage-specific, making it difficult to suppress error propagation arising from grounding drift and context inconsistency. To address this, we propose Grounded Context Preference Optimization (Groc-PO), a grounded preference optimization framework for MLLMs. We further construct the Grounded Context Preference Dataset (GCPD), organizing multi-stage preference samples around three stages of Object Grounding, Contextual Grounding, and Grounded Reasoning, to capture the formation, integration, and utilization of grounded context. By introducing more explicit preference supervision over multiple grounded stages, Groc-PO strengthens context-dependent reasoning and mitigates cross-stage error propagation. Extensive experiments show that, compared with standard DPO and other strong baselines, Groc-PO achieves improved performance in hallucination mitigation, faithful reasoning, and overall reliability, supporting the value of more explicit grounded supervision for trustworthy multimodal reasoning.

---


### 54. [CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems](https://arxiv.org/abs/2607.13716)

**<font color=#1a73e8>作者：</font>** Zexun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems increasingly act through heterogeneous runtimes: local coding hooks, SDK tools, browser automation, managed-agent traces, API gateways, and workflow engines. A single operational act such as publishing code, changing identity state, moving money, or exporting data may therefore be represented by many incompatible runtime records. This makes a basic governance question difficult to answer: what action was actually approved, what evidence binds the approval to execution, and can an independent verifier reproduce the same action identity later?
This paper presents Canonical Action Verification and Attestation (CAVA), a runtime-semantics layer for converting heterogeneous agent activity into canonical runtime action objects. CAVA is positioned below Proof-Carrying Agent Actions (PCAA): PCAA defines the deployer-owned route-review-prove governance process, while CAVA defines the stable action object that process governs. The paper formalizes canonical action identity, semantic pattern detection, approval binding, receipt integrity, runtime-portable projection, and optional attestation substrates. We study a reference implementation through a 96-seed, 384-variant benchmark covering semantic equivalence, semantic separation, wrapper bypass, false-positive control, approval binding, receipt reproducibility, attestation tamper detection, runtime portability, semantic pattern detection, policy degradation, and Azure deployment drills. The contribution is a systems formulation of action-level canonicalization and policy-addressable semantic patterns as a necessary substrate for deployer-side AI governance.

---


### 55. [Post-Training Shifts Confidence: A Three-Stage Analysis of How SFT, RL, and OPD Shape Pre-, Intra-, and Post-CoT Calibration](https://arxiv.org/abs/2607.13753)

**<font color=#1a73e8>作者：</font>** Shuhao Li, Guodong Du, Anhao Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have made strong reasoning gains through supervised fine-tuning, reinforcement learning, and on-policy distillation, yet these post-training methods are usually evaluated only by final-answer accuracy. We study how they reshape confidence during reasoning. We introduce a three-stage calibration framework that evaluates confidence before, during, and after chain-of-thought generation, corresponding to difficulty estimation, early termination, and answer aggregation. Through a controlled comparison on mathematical reasoning benchmarks, we find that OPD provides the most useful pre-reasoning confidence, SFT gives the strongest online signal for early stopping, and RL produces the most reliable trace-level signal for aggregation. We further show that confidence reliability is position-dependent: RL confidence becomes informative after a path-commitment phase, while OPD confidence is useful early but can become inversely calibrated later. Based on this observation, we propose PosConf, a position-aware confidence strategy that uses confidence only from reliable relative-position intervals. PosConf improves RL answer aggregation by 6.1 points over majority voting and consistently improves OPD early stopping under tight token budgets, with gains up to 4.3 points by avoiding its later inverse-calibration region, showing that \emph{confidence in reasoning models should be used both stage-wise and position-awarely}. Our code is available at this https URL.

---


### 56. [MxGPS: Multiplex Graph Transformers for a Power Grid Foundation Model](https://arxiv.org/abs/2607.13763)

**<font color=#1a73e8>作者：</font>** Charilaos Papaioannou, Ioannis Tsantilas, Dimitris Giannakakos 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-task fine-tuning of graph neural networks (GNNs) for power grid problems exhibits a systematic failure mode: models that achieve the lowest in-distribution error degrade the most under topology shift. We term this topology overfitting: the tendency of task-specific gradient signals to encode relational structure particular to the training topologies rather than the underlying physics, causing models to fail on unseen grids despite strong in-distribution performance. To expose and address this failure mode, we introduce MxGPS (Multiplex GPS), a multiplex graph transformer that runs K task-specialised GPS branches over a shared node encoder, jointly trained on Static State Estimation (SSE) and AC Power Flow (PF) via a self-supervised pre-training and multi-task fine-tuning protocol, with a cross-branch attention module evaluated in ablation. The joint SSE+PF objective forces the shared encoder to simultaneously satisfy complementary gradient signals, preventing it from overfitting to topology-specific relational structure. Under a 3-fold sliding-window cross-validation spanning four unseen topologies (14-, 24-, 162-, and 300-bus), MxGPS attains 0% boundary violation rate (BVR) on all four zero-shot Power Flow topologies. Critically, models with substantially lower in-distribution PF error degrade by 190% to 1400% under topology shift, whereas MxGPS degrades by only 39%, an inversion that directly implicates topology overfitting as the failure mechanism rather than insufficient model capacity. With only 1.6M parameters (12x fewer than the GridFM reference baseline), MxGPS demonstrates that multi-task joint training is a principled and parameter-efficient mechanism for topology-agnostic generalisation in power grid foundation models.

---


### 57. [Multimodal Assessment of Pancreatic Cancer Resectability Using Deep Learning](https://arxiv.org/abs/2607.13826)

**<font color=#1a73e8>作者：</font>** Vincent Ochs, Christoph Kuemmerli, Florentin Bieder 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate determination of pancreatic ductal adenocarcinoma (PDAC) resectability relies on evaluating how the tumor interacts with major peripancreatic vessels on CT imaging, yet expert assessment often shows substantial variability. We introduce a fully automated multimodal deep learning framework that jointly analyzes 3D contrast enhanced CT and structured clinical information to classify patients into the three National Comprehensive Cancer Network (NCCN) resectability categories (upfront resectable, borderline resectable, locally advanced). The approach uses a Swin-UNETR backbone to obtain anatomy aware image representations through auxiliary segmentation of pancreas, tumor, and vascular structures. These features are fused with a compact clinical embedding derived from 17 routinely collected variables and processed by a lightweight classification head. Model training is guided by a dynamic multitask objective that adapts the balance between segmentation and classification based on current tumor Dice performance, promoting feature representations that remain both anatomically informed and discriminative.

---


### 58. [SPyCE: Skill-Policy Co-evolution for Multimodal Agents](https://arxiv.org/abs/2607.13854)

**<font color=#1a73e8>作者：</font>** Ru Zhang, Weijie Qiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal agents that think with images iteratively manipulate visual evidence and invoke tools across many steps. Existing reinforcement learning methods reduce trajectories to scalar rewards, forcing the policy to discover reusable tool-use patterns from scratch on every new task; memory-based alternatives retain past experience, yet they rely on test-time retrieval, without updating the policy to absorb reusable patterns from that experience. Our key insight is that multimodal reasoning trajectories should be distilled into reusable skills that co-evolve with the policy during training, rather than being consumed as rewards or retrieved from a static store. To this end, we propose SPyCE (Skill-Policy Co-evolution), a framework that distills trajectories into a hierarchical skill library and updates it throughout reinforcement learning. Execution skills capture local visual operations, while workflow skills encode high-level priors that orchestrate tool use. During training, the policy model conditions on retrieved skills to guide its rollouts, while the skill library evolves using valuable rollouts generated by the policy. This creates a closed loop in which improved policies yield better skills, and the evolving skill library, in turn, provides stronger priors for policy rollouts. Experiments across eight benchmarks demonstrate that SPyCE consistently outperforms both RL-based and memory-based baselines. Further analysis reveals that both the hierarchical skill design and the co-evolution mechanism are critical to our design. These results suggest joint skill-policy optimization as a promising paradigm for building capable multimodal agents.

---


### 59. [Towards Enhancing 3D Spatial Reasoning in Medical Multimodal Large Language Models](https://arxiv.org/abs/2607.13860)

**<font color=#1a73e8>作者：</font>** Zhuoyuan Fu, Zeshang Li, Yiqiong Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have demonstrated remarkable success in 2D medical image understanding, their extension to 3D volumetric imaging remains hindered by prohibitive annotation costs and dataset opacity. Current data formats, predominantly consisting of rigid Visual Question Answering (VQA) pairs or unstructured final clinical reports, typically fail to capture explicit clinical reasoning. To address this limitation, we introduce a large-scale structured reasoning dataset constructed via a novel slice-wise data synthesis paradigm. Inspired by the genuine diagnostic workflow of radiologists, this paradigm models visual cognition by decomposing the complex 3D reading process, translating global clinical priors into fine-grained, per-slice observations that are subsequently synthesized into an interpretable Chain-of-Thought (CoT). Crucially, this synthesized reasoning framework enforces essential clinical principles: sequential spatial tracking, multi-slice spatial awareness for artifact mitigation, and differential exclusion. To validate this approach, we instruction-tune a standard 2D-pretrained MLLM baseline using the synthesized data to enhance its volumetric comprehension. Comprehensive evaluations across multiple 3D medical benchmarks demonstrate that our method yields significant performance improvements over the 2D baseline. Furthermore, the resulting model exhibits robust spatial reasoning capabilities and rivals resource-intensive native 3D architectures, effectively bridging the performance gap. Ultimately, this data-centric strategy unlocks deep volumetric understanding and highly interpretable clinical logic without requiring computationally expensive 3D-specific pre-training. The complete repository, including datasets and training workflows, is publicly available at this https URL.

---


### 60. [Unleashing Multimodal Large Language Models for Training-free HOI Detection in the Wild](https://arxiv.org/abs/2607.13881)

**<font color=#1a73e8>作者：</font>** Ting Lei, Jialin Liu, Zhu Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-object interaction detection (HOID) has traditionally been formulated as a supervised detection problem over predefined interaction categories. While such paradigms achieve strong performance on closed-set benchmarks, they fundamentally entangle interaction understanding with dataset-specific supervision, limiting their ability to generalize to open-world and compositional scenarios. Recent HOI detectors attempt to leverage MLLMs through prompting strategies to transfer interaction-specific knowledge. However, such prompt-based approaches primarily focus on extracting discriminative representations from pretrained models, while underexploring their inherent multimodal reasoning capabilities. As a result, they struggle to provide informative contextual reasoning for ambiguous and open-world interaction scenarios. In this work, we present AgentHOI, a training-free, agentic framework that transfers the generalist multimodal reasoning capabilities of foundation models to HOI detection in the wild. Instead of learning interaction classifiers, AgentHOI modularly orchestrates complementary vision foundation modules to perform open-ended semantic reasoning and spatial grounding in a coordinated manner. To address the challenges of incomplete interaction discovery and ambiguous localization in complex scenes, we introduce two key mechanisms: (1) Context-aware Multi-round Reasoning, which progressively refines interaction hypotheses to ensure exhaustive and compositional HOI discovery, and (2) Multifaceted Interaction Localization, which enhances grounding precision by generating instance-specific descriptions that integrate semantic, spatial, and appearance cues. Extensive experiments demonstrate that AgentHOI achieves superior performance over state-of-the-art supervised and weakly supervised methods in real-world settings, despite requiring no HOID data for training.

---


### 61. [Experience Memory Graph: One-Shot Error Correction for Agents](https://arxiv.org/abs/2607.13884)

**<font color=#1a73e8>作者：</font>** Wenjun Wang, Yuchen Fang, Fengrui Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have shown remarkable capabilities in autonomous decision-making by generating sequential trajectories of states, actions, and observations. However, in complex, long-horizon tasks, these agents frequently suffer from compounding errors and struggle to recover from failures. Existing self-correction mechanisms rely on prompt-based reflection, which is inherently brittle, incurs heavy time and API costs due to iterative trial-and-error loops, and produces task-specific memory that may be hard to generalize to new scenarios. To address this, we propose Experience Memory Graph (EMG), a framework that reformulates agent failure recovery as a graph matching problem. At training time, we convert both failed exploration trajectories and successful expert trajectories into directed action decision graphs. By matching these graphs, we extract common subgraphs (successful workflows) and graph edit paths that explicitly indicate how to correct failures (e.g., which actions to add, delete, or relabel under a given observation), and store them in a memory graph with intra-task nodes and cross-task edges. At test time, EMG retrieves relevant insights and guides the agent in a single, loop-free execution. Experiments on ALFWorld and ScienceWorld show that EMG consistently outperforms state-of-the-art reflection baselines in success rate and average reward, while requiring no test-time trial-and-error.

---


### 62. [SIVA-RL: Sensitivity-Invariance Visual Alignment for Multimodal Reinforcement Learning](https://arxiv.org/abs/2607.13931)

**<font color=#1a73e8>作者：</font>** Cheng Tang, Junzhi Ning, Min Cen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) drives multimodal reasoning, but answer-level correctness does not guarantee that a vision-language model grounds its predictions in visual evidence. Existing visual-intervention methods contrast policy behavior on original and modified images, yet assign supervision by the type of intervention rather than its observed effect. This assumption fails: identical operators produce heterogeneous outcomes across samples. We propose SIVA-RL, a Sensitivity-Invariance Visual Alignment framework that replaces operator-conditioned regularization with sample-wise, outcome-conditioned supervision. SIVA-RL constructs localized interventions through token-aligned, distance-constrained within-image PatchSwap. A frozen audit policy then scores each clean-intervention pair, and the observed reward drop becomes soft routing weights. Large-drop pairs drive sensitivity alignment, low-drop pairs drive clean-anchored invariance alignment, and ambiguous pairs are down-weighted. This design decouples intervention construction from supervision assignment and is compatible with both GRPO and DAPO backbones. Across nine multimodal reasoning benchmarks spanning mathematical, logical, and vision-dependent tasks, SIVA-RL improves 3B and 7B models over matched RL baselines in every setting. It yields an 8.79 percentage-point gain on vision-dependent reasoning and up to 14.9% relative overall improvement across all four GRPO- and DAPO-based configurations.

---


### 63. [Pezego-HITL: A policy-grounded large language model architecture for agricultural extension in Ghana](https://arxiv.org/abs/2607.13934)

**<font color=#1a73e8>作者：</font>** Shunbao Li, Zhipeng Yuan, Amoako Ofori 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in agricultural decision-support settings, yet high-stakes crop protection in smallholder agriculture requires more than output-quality benchmarks. Over a two-year design and evaluation programme, we formalise policy-constrained large language model assessment as an adaptive compute allocation problem that jointly captures safety compliance, helpfulness, operational latency, and expert supervision workload. We introduce P-EVAL (Policy-grounded Expert-calibrated VALidation protocol), a unified evaluation framework for policy-grounded decision support, evaluating the architecture on a simulated field query database consisting of 1,240 cases. The protocol is instantiated on the Pezego advisory architecture (Pezego-HITL) and evaluated in Ghana. Following offline judge calibration against gold-standard human expert decisions ($\kappa = 0.77$), we evaluate the architectural performance under simulated query workloads. Under P-EVAL, our memory-routed architecture improves the Policy Alignment Rate (PAR) to 0.94 and the Agronomic Utility Rate (AUR) to 0.95, while reducing P95 latency by 55% (from 28.6s to 12.9s) through a 59.6% cache reuse ratio. We also demonstrate generalisability using the open-source \texttt{Qwen3.5-9B-DeepSeek-V4-Flash} model, achieving a PAR of 0.86 and a 54.5% latency reduction (to 10.2s). To evaluate practical utility and socio-technical integration, we administer detailed questionnaires to Ghanaian Extension Services Officers ($N=30$) and smallholder farmers ($N=36$). Taken together, this work demonstrates how policy-grounded structured retrieval-augmented generation with validated-memory routing makes safety-utility-latency trade-offs explicit, offering a scalable template for trustworthy AI-driven extension in smallholder farming systems.

---


### 64. [A novel unsupervised machine learning strategy to handle multimodal cardiac PET/MRI data](https://arxiv.org/abs/2607.13936)

**<font color=#1a73e8>作者：</font>** Brunnhilde Ponsi, Thomas Carlier, Lara Marteau 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Arrhythmogenic left ventricular cardiomyopathy is a genetic myocardial disease difficult to diagnose due to the lack of gold standard criteria. Simultaneous PET/MR imaging, combined with multiparametric quantitative analysis, could facilitate the identification of different profiles related to the phenotype and progression of cardiomyopathy. This preliminary study focuses on a methodological strategy for dealing with PET/MRI data, including inter-patient data linkage and regional analysis. Two-step clustering was applied to T1 and T2 maps, LGE, and 18F-FDG-PET images of 99 patients genetically diagnosed with arrhythmogenic left ventricular cardiomyopathy. Each patient's images were independently z-scored and summed into a single volume, which was clustered into supervoxels. Thirty-two inter-patient groups of supervoxels were obtained by spectral clustering. An "abnormality" score was assigned to each cluster and modality, and used to visualise abnormal regions likely associated with disease. They enabled the generation of automated textual and bullseye health reports for each patient, which were compared with cardiac imager assessments using balanced accuracy in repeated nested cross-validation. This approach was further validated on a larger cohort of 167 numerical phantoms. The reports generated by clustering accurately identified most of the cardiac physicians' observations (BA = 0.76 $\pm$ 0.04 in repeated nested cross-validation on patients, and BA $\ge$ 0.8 on phantoms). Furthermore, the identified abnormal clusters closely matched their visual observations, facilitating the identification of varying degrees of fibrosis or inflammation on the images. This approach enables a more systematic handling of multimodal PET/MRI data to characterise myocardial heterogeneity in arrhythmogenic left ventricular cardiomyopathy patients.

---


### 65. [TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents](https://arxiv.org/abs/2607.13988)

**<font color=#1a73e8>作者：</font>** Leitian Tao, Baolin Peng, Wenlin Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training. Outcome rewards provide reliable supervision for short-horizon reasoning, but become sparse and high-variance as trajectories grow to tens or hundreds of tool calls. They can also be misleading: a failed rollout may contain many useful actions that move the agent closer to the goal, yet outcome-only training assigns them the same negative advantage as the eventual mistake. We propose TRACE (Turn-level Reward Assignment via Credit Estimation), a dense credit-assignment method for agentic reinforcement learning. TRACE represents rollouts as state transitions at tool-call boundaries, obtains gold-answer log-probabilities from a frozen reference model, transforms them into log-ratio state values, and derives per-action rewards as Temporal-Difference changes in those values. This requires no additional critic or process-label training, and its one-step log-ratio TD component telescopes across redundant tool calls. On long-horizon complex search, TRACE substantially improves base-model tool-use ability using pure RL, without a cold-start supervised fine-tuning stage, an agentic mid-training stage, or training on live-web data. On the closed-web BrowseComp-Plus benchmark, it raises Qwen3-4B from $7.2$ to $35.6$ and Qwen3-30B-A3B from $8.4$ to $42.6$. The learned search behavior also transfers to open-web benchmarks, and the learning curves show earlier improvement and faster convergence during RL training.

---


### 66. [M$^\text{4}$World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming](https://arxiv.org/abs/2607.14005)

**<font color=#1a73e8>作者：</font>** Ke Cheng, Hanqiao Ye, Lei Shi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability. We present M$^\text{4}$World, a Multi-view and Multimodal generative driving world model that synthesizes future surround-view video streams and synchronized LiDAR scans while supporting interactive object Manipulation and stable Minute-long streaming. Fine-grained object manipulation is realized through a flexible conditioning interface that supports explicit control over both the spatial layout and visual appearance of individual objects. Stable minute-long streaming, on the other hand, is achieved through a multi-stage training framework that enables online causal generation in only four denoising steps while maintaining coherent world dynamics throughout extended rollouts. Building on these components, we introduce an efficient few-clip post-training as well as a suite of visual reference-conditioned generation models, preserving general generation ability while allowing rare-case customization for long-tail controllability. To assess controllability beyond realism, we further introduce an automated VLM-based judging pipeline that evaluates scene-level condition adherence, view-wise object controllability, and cross-view object consistency. Comprehensive experiments show that M$^\text{4}$World consistently delivers high generation quality, precise controllability, and stable minute-long streaming. Together with downstream long-tail augmentation and scene editing, these results demonstrate the potential of M$^\text{4}$World for controllable, scalable driving simulation.

---


### 67. [Can an Old Dog Be Taught New Tricks? Taking LLMs Beyond Sentence Level Translation](https://arxiv.org/abs/2607.14040)

**<font color=#1a73e8>作者：</font>** Alaina Brandt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic translation systems, from CAT tools to MT, overwhelmingly treat translation as a sentence-by-sentence act. This paper asks whether LLMs can be moved beyond that paradigm through whole-document, corpus-informed translation. We present PAT (Pragmatic Auto-Translator), a RAG-based system that pairs user-configured specifications with context from a comparable corpus of authentic longform texts in U.S. English and Latin American Spanish, passing retrieved paragraph-, section-, and document-level examples to an LLM for whole-document generation. The goal is draft translation for professional verification: target texts reformulated to fit their Spanish-language context, where discourse organization, rhetorical style, and pragmatic norms differ meaningfully from English. We evaluated six automatic translations of essays on generative AI across three projects using a customized MQM typology, assessed by two trained evaluators working from U.S. English into LATAM and Mexican Spanish. Results show that a limited prompt produced no meaningful reformulation, and specifications and corpus-informed translations at times showed substantial reformulation, though not always to effect. We find that LLMs can be moved toward reformulation and away from the sentence-by-sentence paradigm, though more work is needed to improve the effectiveness of those reformulations. In this paper, we discuss considerations related to automatic translation system design, corpus construction, and translation quality evaluation methodology and results.

---


### 68. [Deep Interaction: An Efficient Human-AI Interaction Method for Large Reasoning Models](https://arxiv.org/abs/2607.14049)

**<font color=#1a73e8>作者：</font>** Hefeng Zhou, Jinxuan Zhang, Jiong Lou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of Chain-of-Thought (CoT) reasoning has significantly enhanced the ability of large language models (LLMs) to tackle complex, multi-step tasks. However, when errors occur, current interaction approaches typically involve re-generating another response that may make mistakes again, or users laboriously flag the faulty step in follow-up turns that may get responses <You are right, I made a mistake here> followed by similar errors recurring. To address this issue, we propose an efficient human intervention mechanism for precisely correcting reasoning errors in LLMs, termed Deep Interaction. Our approach enables direct editing of the original response, allowing erroneous parts to be corrected while preserving accurate reasoning steps. We refine the edited CoT into a distilled prompt, which then steers the LLM along the corrected reasoning path. Experimental results show that our method achieves over a 25% improvement in correction success rate and reduces token usage by approximately 40% on STEM tasks reasoning compared to baseline approaches.

---


### 69. [Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters](https://arxiv.org/abs/2607.14051)

**<font color=#1a73e8>作者：</font>** Xiao Ye, Jacob Dineen, Evan Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Forecasters are evaluated by backtesting, which replays resolved questions and grades the probability the system would have assigned before the outcome was known. For LLMs, two channels leak the answer into this test. A model that retrieves can surface reports written after the event, turning forecasting into a lookup, and each new model is trained on data closer to the event, so a question that lay in the future for last year's models sits inside this year's training data. Either way, the test grades recall while claiming to grade foresight. We introduce Hindcast, which closes both leaks by grading a model as if it stood at a chosen past date $t_0$, before the outcome existed in either channel. Hindcast replays resolved Polymarket prediction markets against a frozen snapshot of public Reddit, lets the model read only posts written before $t_0$, and scores each forecast against both what happened and the market's own price at $t_0$, itself a human forecast made from the same past information. Because the cutoff is set per market and the snapshot never changes, the evaluation re-runs on new markets as models improve, without going stale. Once the leak is closed, retrieval still helps most models, but only where Reddit discussed the event beforehand. Where the archive carried only speculation, retrieval hurts.

---


### 70. [MetaPerch: Learning from metadata for bioacoustics foundation models](https://arxiv.org/abs/2607.14072)

**<font color=#1a73e8>作者：</font>** Mustafa Chasmai, Vincent Dumoulin, Jenny Hamer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bioacoustic foundation models rely on large-scale citizen science platforms like Xeno-Canto for geographically and ecologically diverse data. Recent work has shown that supervision alone can produce SotA species detection models when trained on this large-scale data -- however, there remains unutilized potential in the form of recording metadata readily available within these community-driven data hubs. In this work, we explore the use of metadata -- such as location and time -- as auxiliary supervision signals, allowing the model to leverage species-metadata correlations in its learned representation. Auxiliary metadata losses provide additional information beyond vocalizations alone that can encourage a richer, more robust representation that generalizes better to species distribution and acoustic domain shifts -- important challenges for deployment in real-world passive acoustic monitoring (PAM) settings. We introduce MetaPerch, a new foundation model that achieves strong species identification performance across multiple challenging domains and present an extensive empirical study of the effects of 9 diverse metadata sources on 17 bioacoustic datasets.

---


### 71. [From Pixels to States: Rethinking Interactive World Models as Game Engines](https://arxiv.org/abs/2607.14076)

**<font color=#1a73e8>作者：</font>** Zhen Li, Zian Meng, Shuwei Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building interactive worlds that respond coherently to player actions has long been a shared goal of computer graphics, games, and artificial intelligence. Recent video generative models provide a data-driven route toward this goal by predicting future observations conditioned on user actions, and are increasingly regarded as potential next-generation game engines. Realizing a genuinely interactive game world, however, requires interaction outcomes that follow rules over evolving game conditions, consequences that persist over long horizons, and a generation loop that operates in real time. Conventional game engines realize these properties through a recurrent action-state-observation loop, in which player actions update an explicit game state according to predefined rules and observations are rendered from the resulting state. Taking this loop as an organizing lens, this paper examines interactive game world modeling along four dimensions: player action control, game state dynamics, state-observation persistence, and real-time interactive generation. For each dimension, we start from the capabilities required by an interactive game world, group existing approaches into representative families, and discuss the strengths and trade-offs of each family. Complementing this analysis, we present a scalable data engine for Black Myth: Wukong that collects over 90 hours of gameplay with frame-aligned player actions, ground-truth game states, and visual observations, together with structured and semantic annotations, as a resource for state-aware game world modeling. We hope this paper offers a clear picture of where the field stands and fosters progress toward interactive game worlds.

---


### 72. [Leveraging unlabelled data for generalizable neural population decoding](https://arxiv.org/abs/2607.14086)

**<font color=#1a73e8>作者：</font>** Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust and accurate neural decoders are integral to neurotechnologies such as brain-computer interfaces and closed-loop experiments. Recent work has shown that tokenizing neural data at the spike level facilitates multi-session pretraining and delivers state-of-the-art decoding performance. However, current spike-based models are restricted to supervised learning (SL), limiting training to datasets with paired behavioural labels. To address this limitation, we introduce MOJO (Masked autOencoder-based JOint training), a training framework for spike-tokenizing models that jointly leverages self-supervised learning (SSL) via masked autoencoding and SL objectives. We evaluate MOJO on three spiking datasets spanning monkey motor cortex during reaching tasks and multi-regional mouse recordings during vision and decision making tasks, demonstrating superior performance over purely SL-trained models. This improvement is especially pronounced when training with limited labelled data, particularly in few-shot finetuning, where only a small amount of labelled data from a new session is available. Incorporating SSL also yields more interpretable neuronal representations, improving performance on brain region classification and spike-statistics prediction without explicit optimization for these tasks. We further show that MOJO generalizes beyond spiking data to human electrocorticography during speech, where it continues to outperform purely SL-trained models and achieves performance comparable to neuro-foundation models (NFMs) designed specifically for continuous signals. Overall, augmenting spike-tokenizing models with SSL improves performance in label-impoverished settings and enables the use of unlabelled data across various tasks and species, while generalizing to other neural modalities. These results suggest a path towards more flexible and scalable data usage when training NFMs.

---


### 73. [VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders](https://arxiv.org/abs/2607.14088)

**<font color=#1a73e8>作者：</font>** Zhihao Xie, Junfeng Wu, Xinting Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generative models commonly rely on latent spaces learned by 3D Variational Autoencoders (3D-VAEs). However, conventional 3D-VAEs are mainly optimized for pixel-level reconstruction, which can limit the semantic and spatio-temporal structure captured by their latents. Meanwhile, Video Foundation Models (VFMs) such as V-JEPA 2 and VideoMAEv2 show strong video understanding capabilities, yet whether their frozen representations can be transformed into compact, reconstruction-capable, and generation-friendly video latents remains largely unexplored. We answer this question with VideoRAE, a representation autoencoder that leverages multi-scale hierarchical features from a frozen video foundation encoder and compresses them with a lightweight 1D self-attention projector. VideoRAE supports both continuous latents for Diffusion Transformers and discrete tokens for autoregressive models via multi-codebook high-dimensional quantization. During decoding, a local-and-global representation alignment objective with the frozen VFM teacher improves semantic preservation and enables training without KL regularization. Experiments show that VideoRAE achieves strong reconstruction in both continuous and discrete regimes. On UCF-101, it obtains state-of-the-art class-to-video gFVDs of 40 and 93 with AR and DiT generators, respectively, while converging approximately 5x faster than competing autoencoder baselines. In a controlled 2B-scale text-to-video study, replacing LTX-VAE with VideoRAE leads to faster convergence under comparable settings. These results validate frozen VFM representations as versatile and generation-friendly video latents. The model and code will be released on this https URL.

---


> [!TIP]
> 当前位于：**51-73**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-73**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
