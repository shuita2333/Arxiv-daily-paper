# 📦 其他研究 | 2026年06月02日

> 本类共 **317** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-317](./part-07.md)

---

### 101. [Learning Agent-Compatible Context Management for Long-Horizon Tasks](https://arxiv.org/abs/2605.30785)

**<font color=#1a73e8>作者：</font>** Lu Yi, Runlin Lei, Liuyi Yao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly face long-horizon tasks such as web search and deep research in real-world applications, where accumulated context can cause long-context degradation and reasoning failures. Prior work mitigates this through context management with agent-side context control or fixed strategies such as summarization, which require training the agent itself for adaptation - making it impractical for closed-source agents and ignoring that different agents may require different strategies. We introduce Adaptive Context Management (AdaCoM), which trains an external LLM to manage the context of a frozen agent through flexible modification actions and end-to-end reinforcement learning. Across diverse agents on web search and deep research benchmarks, AdaCoM substantially improves performance by preserving task constraints and progress while pruning stale content. The learned strategies reveal a Fidelity-Reliability Trade-off: agents with higher vanilla ReAct performance benefit from higher-fidelity context preservation, whereas lower-performing agents require more aggressive compression to stay within a reliable reasoning regime. Transfer experiments show that AdaCoM generalizes most effectively across agents with similar capability (measured by vanilla ReAct performance), suggesting a practical path toward reusable context managers for agent systems.

---


### 102. [AbstainGNN: Teaching Graph Neural Networks to Abstain for Graph Classification](https://arxiv.org/abs/2605.30786)

**<font color=#1a73e8>作者：</font>** Xixun Lin, Zhiheng Zhou, Zhengyin Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph classification is a core task in graph data mining with widespread real-world applications. Recent advances in graph neural networks (GNNs) have led to substantial performance improvements for graph classification. However, existing GNNs are typically forced to make predictions even under high uncertainty or unknown conditions, resulting in unreliable decisions that can severely impact downstream tasks, particularly in safety-critical scenarios. To address this critical limitation, we propose AbstainGNN, a novel and theory-driven framework for graph classification with abstention, which enables GNNs to reject uncertain predictions instead of producing incorrect decisions. Specifically, AbstainGNN explicitly models both the predictive function and the abstention function, allowing for effective utilization of graph structural information. Moreover, unlike existing heuristic abstention methods, we theoretically characterize the trade-off between classification errors and rejection costs from a PAC-Bayesian generalization perspective, and derive a unified learning objective for model optimization. Guided by this theoretical insight, we further develop an efficient two-stage training strategy consisting of predictive function warm-start and abstention function calibration. Extensive experiments on five benchmark datasets show that AbstainGNN outperforms existing abstention methods, achieving superior classification performance under the same rejection rates.

---


### 103. [XLGoBench: Detecting cross-lingual skill gaps with algorithmic tasks](https://arxiv.org/abs/2605.30788)

**<font color=#1a73e8>作者：</font>** Purvam Jain, Preethi Jyothi, Vihari Piratla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a set of synthetic algorithmic tasks to detect cross-lingual gaps in the abilities of large language models. Our benchmark is commensurate across languages, since it requires models to perform the same underlying task in different languages; scalable, since each task can be generated at varying levels of complexity allowing it to be adapted to models with different capabilities; quantifiable, since every task admits an objective notion of correctness; and transparent, since tasks are generated from simple templates that can be readily audited for translation errors. Because our benchmark focuses on algorithmic tasks, differential performance is a sufficient -- but not necessary -- indicator of cross-lingual gaps. Nevertheless, we show through extensive experiments that our benchmark exposes persistent cross-lingual gaps in multiple state-of-the-art models.

---


### 104. [Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO](https://arxiv.org/abs/2605.30789)

**<font color=#1a73e8>作者：</font>** Yiming Ren, Yiran Xu, Zicheng Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We identify a new dimension for enhancing rollout diversity in Group Relative Policy Optimization (GRPO) for LLMs. While GRPO relies on diverse rollouts, prevailing strategies primarily increase diversity by injecting more token-level randomness, which may introduce step-wise noise and lead to incoherent trajectories. We uncover that smaller models within the same model family inherently exhibit higher policy-level diversity, indicated by their superior pass@k relative to larger counterparts as sample counts increase. Unlike token-level noise, this diversity is temporally correlated, preserves logical consistency, and provides structured exploration signals for gradient estimation. We thus propose S2L-PO (Small-to-Large Policy Optimization), a framework that leverages fixed small models as natural explorers to train larger models. To balance exploration and exploitation, we design a progressive annealing strategy that transitions from offline small-model rollouts to the large learner's own sampling. This shift elegantly avoids mid-training performance drops caused by the small model's capacity limits, achieving faster convergence and unlocking a higher performance ceiling. S2L-PO improves accuracy on diverse mathematical reasoning benchmarks (e.g., +8.8% on AIME 24 using a 1.7B explorer to guide the 8B model) while reducing rollout compute.

---


### 105. [Computer-Aided Tagging on Wikimedia Commons: Designing for Human-AI Collaboration in Open Knowledge Work](https://arxiv.org/abs/2605.30800)

**<font color=#1a73e8>作者：</font>** Yihan Yu, David W. McDonald  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study investigates Wikimedia Commons contributors' lived experiences with the Computer-Aided Tagging (CAT) tool, an AI-assisted image tagging system designed to improve Commons' discoverability, searchability, accessibility, and multilingual support. Using a qualitative analysis of 595 CAT-related community comments from 11 wiki pages and 16 in-depth interviews, we identify seven key issues that contributed to CAT's mixed reception and eventual deactivation. We also offer community-informed suggestions for improving the tool. We reflect on the implications for designing human-AI collaboration on Commons and for developing AI-assisted tools that support open knowledge work. This work contributes to HCI and CSCW research by extending the understanding of human-AI collaboration beyond Anglophone, text-centric, corporate platforms.

---


### 106. [Conformal Reliability: A New Evaluation Metric for Conditional Generation](https://arxiv.org/abs/2605.30807)

**<font color=#1a73e8>作者：</font>** Yachen Gao, Xinwei Sun, Yikai Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional generative models have recently achieved remarkable success in various applications. However, a suitable metric for evaluating the reliability of these models, which takes into account their inherent uncertainty, is still lacking. Existing metrics, which typically assess a single output, may fail to capture the variability or potential risks in generation. In this paper, we propose a novel evaluation metric called reliability score based on conformal prediction, which measures the worst-case performance within the prediction set at a pre-specified confidence level. However, computing this score is challenging due to the high-dimensional nature of the output space and the nonconvexity of both the metric function and the prediction set. To efficiently compute this score, we introduce Conformal ReLiability (CReL), a framework that can (i) construct the prediction set with desired coverage; and (ii) accurately optimize the reliability score within the constructed prediction set. We provide theoretical results on coverage and demonstrate empirically that our method produces more informative prediction sets than existing approaches. Experiments on synthetic data and the image-to-text and text-to-image tasks further demonstrate the interpretability of our new metric, and the validity and effectiveness of our computational framework. Source code can be found at this https URL.

---


### 107. [IRIS: time-structured manifold projections](https://arxiv.org/abs/2605.30810)

**<font color=#1a73e8>作者：</font>** Brian Ondov, Chia-Hsuan Chang, Weipeng Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional biomedical data, such as cell-by-gene matrices, are increasingly generated temporally. However, Manifold Learning algorithms, like t-SNE and UMAP, cannot incorporate time-ordering in their layouts, obfuscating the dynamics of cell types or other classes. As a solution, we present IRIS, a new Manifold Learning algorithm that structures layouts both chronologically and by manifold topology. IRIS can visualize a wide range of dynamic biomedical data, including scRNA-seq, comparative metagenomics, and literature.

---


### 108. [Non-destructive Identification of Oyster Species is possible from Hyperspectral Images with Machine Learning](https://arxiv.org/abs/2605.30811)

**<font color=#1a73e8>作者：</font>** Ethan Kane Waters, Max Wingfield, Aiden Mellor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiating between oyster species is important for developing new commercial oyster species suited to production systems and is critical for traceability in seafood supply chains. Common methods, such as DNA profiling, are destructive and time consuming. The possibility of using hyperspectral imaging (HSI) for discriminating between Black-Lip rock (BL) and Sydney rock (SR) oysters was investigated. Live BL and SR samples (N = 156) were scanned with a HSI camera (950-2515nm). Partial Least Square Discriminant Analysis and Convolutional Neural Networks were trained with Monte Carlo Cross Validation to distinguish BL and SR oysters from the spectral reflectance of their left and rights valves. The PLS-DA model successfully distinguished between the species from both the left and right valves with a median test set classification accuracy of 100%, out performing the CNN with 83% and 96% respectively. Elemental and mineralogical composition in the surface and cross-section of oyster valves were measured with electron microscopy. Analysis of the right valve revealed a greater number of layers in BL compared to SR (4 vs 2). The concentrations of carbon and oxygen varied in the outer layer of the right valves, with BL being rich in carbon and SR being rich in oxygen. The variation in carbon and oxygen concentrations observed between BL and SR right valves may reflect differences in the relative abundance or composition of chitin and glycoproteins. This is supported by model-derived wavelength importance corresponding to vibrational modes of functional groups characteristic of these compounds. Transmittance analysis revealed that light was transmitted through the valves, around the valve edges, indicating that the spectral signatures may have been influenced by the other valve or the meat. Ultimately, the findings highlight an effective rapid, non-destructive methodology for oyster species.

---


### 109. [Learning Permutation-invariant Macroscopic Dynamics](https://arxiv.org/abs/2605.30812)

**<font color=#1a73e8>作者：</font>** Zhichao Han, Mengyi Chen, Qianxiao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately modeling the macroscopic dynamics of high-dimensional microscopic systems is of broad interest across the sciences. Many data-driven approaches learn a low-dimensional latent state through an autoencoder trained for pointwise input reconstruction. These methods typically assume a fixed ordering of microscopic degrees of freedom in the input. However, in many settings, such as particle systems, the microscopic state is inherently unordered. This motivates an autoencoder framework that learns permutation-invariant latent representations. To this end, we adopt a permutation-invariant encoder and design the decoder to reconstruct the mass distribution centered at the observed points rather than per-sample reconstruction. We then jointly learn the macroscopic dynamics of the observables together with the latent states. We demonstrate the effectiveness and robustness of the proposed method across a range of microscopic settings, including learning the energy dynamics in interacting particle systems, predicting mixing dynamics in Lennard-Jones fluids, and modeling the stretching dynamics from video data of polymers moving in an elongational force field.

---


### 110. [Incremental BPE Tokenization](https://arxiv.org/abs/2605.30813)

**<font color=#1a73e8>作者：</font>** Shenghu Jiang, Ruihao Gong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a novel algorithm for incremental Byte Pair Encoding (BPE) tokenization. The algorithm processes each input byte in worst-case $\mathcal{O}(\log^2 t)$ time, leading to an overall complexity of $\mathcal{O}(n \log^2 t)$, where $n$ is the input length and $t$ is the maximum token length. The algorithm incrementally maintains BPE tokenization results for every prefix of the input text, implementing the standard BPE merge procedure defined by a fixed set of merge rules. This enables efficient partial tokenization in streaming settings. Functioning as a drop-in replacement for standard BPE, our approach achieves a speedup of up to ${\sim}3\times$ over Hugging Face's tokenizers, and demonstrates significant latency reductions over OpenAI's tiktoken on pathological inputs. We further introduce an eager output algorithm that enables streaming output, emitting tokens as soon as token boundaries are determined during incremental tokenization. Overall, our results demonstrate that BPE tokenization can be performed incrementally with strong worst-case guarantees, while providing practical latency benefits in modern large language model pipelines. Code: this https URL

---


### 111. [Function2Scene: 3D Indoor Scene Layout from Functional Specifications](https://arxiv.org/abs/2605.30819)

**<font color=#1a73e8>作者：</font>** Ruiqi Wang, Qimin Chen, Daniel Ritchie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most text-driven 3D indoor scene synthesis methods generate rooms from object-centric prompts, asking what furniture should be placed rather than how the space is used. Yet in real interior design, a layout is judged by how well it supports its occupants, e.g., their activities and physical needs. We introduce Function2Scene, a framework for generating 3D indoor layouts from functional specifications, i.e., natural-language design briefs describing who will use a room and what they need to do there. Given such a specification, our system parses occupant personas and activities, derives a customized set of functional design constraints from a taxonomy of 17 criteria spanning spatial, ergonomic, activity, and environmental considerations, and uses these constraints to guide layout generation. Rather than relying on an LLM to directly produce a final scene, Function2Scene performs iterative evaluation and refinement through a tool-augmented check-and-repair loop, combining geometric measurements, LLM-based contextual reasoning, and VLM-based visual assessment. Experiments on 30 professionally written interior-design cases show that Function2Scene produces layouts that better satisfy functional requirements than recent LLM-based scene synthesis baselines, with our results preferred in 94.3% of pairwise comparisons. Our work reframes text-driven indoor scene synthesis from placing plausible objects to designing spaces that support human use.

---


### 112. [Planner-Centric Reinforcement Learning for Deep Research with Structure-Aware Reward](https://arxiv.org/abs/2605.30824)

**<font color=#1a73e8>作者：</font>** Mustafa Anis Hussain, Xinle Wu, Yao Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research tasks require LLMs to plan what to investigate, retrieve evidence, and synthesize long-form answers across multiple branches of inquiry. Existing training paradigms either rely on short-form verifiable QA as a proxy or optimize monolithic long trajectories, which makes planning and execution difficult to disentangle and yields weak credit assignment for the planning process. We propose DecomposeR, a planner-centric deep research framework that represents research plans as typed directed acyclic graphs (DAGs), allowing planning to be made explicit, structured, and rewardable. We train a Qwen3-8B model in two stages: planner reinforcement learning (RL) first learns graph structure and query decomposition to improve research planning, and answerer reinforcement learning (RL) then learns branch-level execution and final synthesis conditioned on the learned plan. By assigning rewards to explicit planner tokens and structured components rather than to a flat trajectory, DecomposeR enables finer-grained optimization of planning while reducing the ambiguity of end-to-end training. Experiments show that DecomposeR-8B improves over strong comparable open baselines by 5.1-8.0 points on popular long-form benchmarks due to improved planning and answering capabilities.

---


### 113. [Unlearning in Diffusion Models: A Unified Framework with KL Divergence and Likelihood Constraints](https://arxiv.org/abs/2605.30825)

**<font color=#1a73e8>作者：</font>** Shervin Khalafi, Alejandro Ribeiro, Dongsheng Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning in diffusion models aims to remove undesirable data or concepts while preserving the utility of pretrained models -- two fundamentally conflicting objectives. We propose a principled constrained optimization framework that formulates unlearning as minimizing the deviation from a pretrained model, subject to explicit separation constraints from the unlearning distributions. Specifically, we formulate three constrained optimization problems based on reverse and forward KL divergences, and likelihood constraints. The first two generalize existing approaches for concept and data unlearning, while the third offers a novel and natural formulation for unlearning. Despite the nonconvexity of the KL constraints, we establish strong duality for all three problems, enabling us to explicitly characterize their optimal solutions as unlearning targets and develop primal-dual algorithms for each formulation. Experimental results demonstrate that our KL-constrained approach achieves superior retention-unlearning tradeoffs compared to weight-based baselines for concept and data unlearning, and that our likelihood-based approach matches unlearning effectiveness while better preserving retained concepts compared to baselines.

---


### 114. [Beyond Agreement: Scoring Panel-Surfaced Biomedical Entity Candidates for Curator Triage](https://arxiv.org/abs/2605.30826)

**<font color=#1a73e8>作者：</font>** Shuheng Cao, Ruiqi Chen, Renjie Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical NER is deceptively simple for modern LLMs: plausible biomedical mentions are easy to surface, but corpus-convention correctness depends on annotation conventions, span boundaries, entity granularity, and type schemas. Multi-LLM agreement is a salience signal, not corpus-convention correctness. We introduce a candidate-level panel-output benchmark for panel-surfaced candidate verification, where the unit is an aligned candidate surfaced by an explicitly defined multi-model panel rather than a standalone extractor output. The benchmark aligns eight LLMs' predictions over five public biomedical NER datasets into a candidate master table. BioConCal is an in-domain supervised scorer that instantiates this layer with inference-time gold-free agreement, mention, surface-availability, and document features for a fixed candidate stream. In domain, BioConCal improves AUROC from 0.753 for raw agreement to 0.910. At a validation-selected 0.95 precision target it selects 1,340 candidates at empirical test precision 0.939, compared with 293 for raw agreement. This corresponds to candidate-level recall 0.592 and corpus-level recall 0.523 against a within-panel row-label ceiling of 0.883. The main benefit is not recovering entities missed by every panel member, but reshaping a noisy panel stream into a higher-yield review queue. Under entity-type shift, thresholds require target-domain validation, and exact character localization remains a separate deterministic post-processing step.

---


### 115. [LegSegNet: A Public Deep Learning System for Lower Extremity CT Tissue Segmentation and Quantification](https://arxiv.org/abs/2605.30829)

**<font color=#1a73e8>作者：</font>** Yuwen Chen, Yaqian Chen, Roy Colglazier 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lower extremity computed tomography (CT) contains clinically relevant information for body composition analysis, sarcopenia assessment, and musculoskeletal disease monitoring, but extracting these measurements at scale requires accurate tissue segmentation and an automated quantification workflow. Existing public segmentation tools are not designed for comprehensive lower extremity CT analysis, particularly for clinically important inter/intramuscular adipose tissue, and most public methods only provide mask prediction rather than an end-to-end quantification system. To address this problem, we present LegSegNet, a deep learning system for lower extremity CT tissue segmentation and body composition quantification. Given an input CT scan, LegSegNet segments bone, skeletal muscle, subcutaneous adipose tissue, and inter/intramuscular adipose tissue. It then computes quantitative tissue measurements for downstream analysis. We developed the segmentation model using 1,302 manually annotated CT slices and evaluated it on 900 held-out test slices, with all annotations reviewed by radiologists. We benchmark LegSegNet against a broad set of 2D segmentation methods, including CNN-based models, transformer-based models, and finetuned foundation models, and further evaluate its generalization on an external public CT dataset. LegSegNet achieves the best overall segmentation performance, with an average Dice score of 89.31 on the held-out test set. To our knowledge, LegSegNet is the first publicly available end-to-end system for lower extremity CT tissue segmentation and quantification, providing a practical evaluation tool for future computer vision research in medical image analysis. The code and model weights are available at: this https URL

---


### 116. [SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning](https://arxiv.org/abs/2605.30832)

**<font color=#1a73e8>作者：</font>** Jian Yao, Xiongcai Luo, Ran Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Reasoning Models have significantly improved chain-of-thought (CoT) capabilities via reinforcement learning (RL). However, generated reasoning chains frequently suffer from structural redundancy (i.e., \emph{overthinking}), incurring high computational overhead without improving answer correctness. Existing mitigation strategies typically rely on token-uniform length penalties, which provide coarse, segment-agnostic pressure toward shorter outputs and can inadvertently suppress useful reasoning alongside redundancy. To address this, we demonstrate that inefficiency concentrates in high-probability segments with low marginal utility. We derive a theoretical characterization of segment suboptimality under the correctness-length trade-off objective and propose \textsc{SLAT} (Segment-Level Adaptive Trimming), an RL framework that selectively suppresses redundant segments based on this criterion. Empirical results on standard benchmarks indicate that \textsc{SLAT} establishes a superior accuracy-efficiency Pareto frontier, reducing reasoning length by $50\%$ relative to uncompressed baselines while maintaining competitive accuracy. Overall, our results suggest that theoretically grounded, segment-aware trimming is a promising direction for efficient CoT reasoning in large language models.

---


### 117. [Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation](https://arxiv.org/abs/2605.30833)

**<font color=#1a73e8>作者：</font>** Yanjiang Liu, Jie Lou, Xinyan Guan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation transfers reasoning capabilities by training a student model on its own generated trajectories using token-level feedback from a teacher. However, we identify a critical bottleneck, \textbf{Supervision Fidelity Decay (SFD)}: as student-generated prefixes lengthen, the teacher's next-token distribution becomes less confident and less discriminative. Consequently, the teacher-dependent corrective signal in reverse-KL distillation weakens, causing student drift to compound across long reasoning chains. To mitigate SFD, we introduce \textbf{Lookahead Group Reward (\ours{})}. Building on the insight that next-step teacher confidence reflects the discriminative strength of future reverse-KL supervision, \ours{} evaluates the student's top-K candidate tokens by the teacher confidence they induce at the subsequent step and assigns a group-normalized reward. To maintain computational efficiency, we further design an entropy-triggered tree-attention mechanism. Across six math and code benchmarks, \ours{} improves mean@8 by \textbf{2.57} points over OPD for a 7B student, with gains increasing in longer-generation and reaching +\textbf{4.92} points on AIME-26 at 39k tokens.

---


### 118. [Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense](https://arxiv.org/abs/2605.30837)

**<font color=#1a73e8>作者：</font>** Shuhao Zhang, Jiarui Li, Qi Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt-injection detectors are heterogeneous: each is strong on a different slice of attacks, and none is always reliable. Yet existing systems still treat detection as a fixed single-detector pipeline, committing every request to one detector's blind spots. We reframe defense as detector allocation: given a heterogeneous pool, decide per request which detectors to run and whether to escalate to an LLM judge. Our framework SCOUT (Scalable and Controllable Outcome-prediction for Uncertainty-aware Triage) makes this decision dynamic by predicting each detector's per-sample reliability and latency from how it behaved on similar past inputs, and exposes a single safety-utility threshold to the operator (where utility bundles benign-pass rate and wall-clock). To evaluate this setting, we build SCOUT-450, a benchmark that captures the structurally complex, agent-facing injections that older prompt-injection sets under-represent. On SCOUT-450, a safety-oriented operating point reduces attack-success rate by 46% and total wall-clock by 40% relative to an always-on GPT-4o judge, at a 5.1-point benign-utility drop. SCOUT also transfers to three external benchmarks (BIPIA, IPI, and IHEval), improving the safety-utility frontier.

---


### 119. [CoMem: Context Management with A Decoupled Long-Context Model](https://arxiv.org/abs/2605.30842)

**<font color=#1a73e8>作者：</font>** Yuwei Zhang, Chengyu Dong, Shuowei Jin 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Context management enables agentic models to solve long-horizon tasks through iterative summarization of previous interaction histories. However, this process typically incurs substantial decoding overhead for the extra summarization tokens, which significantly affect the end-to-end response latency at deployment. In this paper, we introduce CoMem, a novel framework that decouples memory management from the primary agent workflow, enabling these processes to execute in parallel. We propose a $k$-step-off asynchronous pipeline that overlaps the memory model's summarization with the agent's inference, effectively masking the latency of context processing. To ensure robustness under this asynchronous setting, we introduce a reward-driven training strategy that aligns the memory model to capture sufficient statistics for the agent's decision-making. Theoretical analysis confirms that CoMem offers a superior efficiency-effectiveness trade-off compared to coupled architectures. Our extensive experimental results on SWE-Bench-Verified show that CoMem provides 1.4x latency improvements upon vanilla long-context solutions while preserving most of the performance. Furthermore, we demonstrate that these latency gains scale favorably with increased system throughput, offering a modular path forward for the independent optimization of agent reasoning and memory compression.

---


### 120. [A Lecture Note on Offline RL and IRL, Part II: Foundations of Inverse Reinforcement Learning and Dynamic Discrete Choice Models](https://arxiv.org/abs/2605.30843)

**<font color=#1a73e8>作者：</font>** Enoch Hyunwook Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the forward reinforcement-learning problem, the reward is fixed and known; the learner is asked to find a good policy or value function. Here we turn the question around. Given offline data generated by an expert, can we recover the reward the expert was optimizing? This is the inverse reinforcement learning problem, and remarkably, two communities, structural econometricians studying dynamic discrete choice (DDC) and machine learners studying entropy-regularized IRL, have been working on exactly the same probabilistic model under different names. We begin by proving their equivalence. We then develop the classical identification result of Magnac and Thesmar and the classical computational paradigms that grew out of it: Rust's nested fixed-point algorithm, the conditional-choice-probability approach of Hotz and Miller, and the two temporal-difference approaches of Adusumilli and Eckardt: linear semi-gradient TD and approximate value iteration. Each route has its limits: dimensionality, transition-kernel estimation, the deadly triad, or projected fixed-point bias. We then walk through the modern ML/IRL strand: adversarial IRL, occupancy matching, IQ-Learn, and offline ML-IRL, deriving each method's actual objective and stating precisely what it does and does not identify. We close with the empirical-risk-minimization framework of Kang et al., which yields a gradient-based estimator for offline IRL/DDC.

---


### 121. [Count Anything](https://arxiv.org/abs/2605.30846)

**<font color=#1a73e8>作者：</font>** Mengqi Lei, Shuokun Cheng, Wei Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object counting remains fragmented across domain-specific datasets and task formulations, despite rapid progress in generalist vision models. Existing counting models are often tailored to scenarios such as crowds, vehicles, cells, crops, or remote-sensing objects, and thus struggle to generalize across categories, visual domains, object scales, and density distributions. In this paper, we study text-guided object counting across domains, where a model takes an image and a natural-language query as input and returns an instance-grounded set of target points whose cardinality gives the count. This formulation unifies category-conditioned counting with interpretable spatial localization. To support this setting, we construct CLOC, a Cross-domain Large-scale Object Counting dataset that reorganizes diverse public data sources into a unified benchmark. CLOC covers six visual domains: General Scene, Remote Sensing, Histopathology, Cellular Microscopy, Agriculture, and Microbiology, with about 220K images, 619 categories, and 15M object instances. Based on CLOC, we propose Count Anything, a generalist model for text-guided object counting. Unlike density-map-based methods, which dominate counting models, Count Anything adopts discrete instance points and performs dual-granularity instance enumeration. A Region-level Sparse Counter provides object-level anchors for large and sparse targets, while a Pixel-level Dense Counter handles small, crowded, and weakly bounded targets via dense point prediction. A point-centric supervision strategy enables learning from heterogeneous annotations, and Complementary Count Fusion combines both counters in a parameter-free manner. Extensive experiments show that Count Anything achieves strong accuracy and multi-domain generalization, outperforming existing open-world counting methods. Code is available at: this https URL.

---


### 122. [Speculative Pipeline Decoding: Higher-Accruacy and Zero-Bubble Speculation via Pipeline Parallelism](https://arxiv.org/abs/2605.30852)

**<font color=#1a73e8>作者：</font>** Yijiong Yu, Huazheng Wang, Shuai Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative Decoding (SD) accelerates low-concurrency LLM inference by employing a draft-then-verify paradigm. However, mainstream methods typically rely on multi-token prediction, which introduces escalating prediction difficulty and serial drafting latency. To address these, we propose Speculative Pipeline Decoding (SPD), a groundbreaking framework that unlocks the true potential of pipeline parallelism. By partitioning the target LLM into $n$ pipeline stages, SPD allows LLM to process $n$ tokens in parallel to accelerate decoding. To continuous fill the pipeline in single sequence decoding, a speculation module aggregates intermediate features across different pipeline depths to predict the next token, executing strictly in parallel with the target model's pipeline step, to realize bounded difficulty, higher acceptance rates, and zero latency bubbles. Our experiments demonstrate that SPD achieves a significantly higher theoretical speedup compared to mainstream baselines, offering a highly scalable solution for LLM decoding acceleration. Our code is available at this https URL

---


### 123. [Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation](https://arxiv.org/abs/2605.30855)

**<font color=#1a73e8>作者：</font>** Hanlin Chen, Jiaxin Wei, Xibin Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frame-wise action-controlled image-to-video generation is a promising paradigm for interactive world simulation, where each control signal should elicit an immediate visual response. However, maintaining visual fidelity and 3D consistency over long autoregressive rollouts remains challenging. Existing 3D-aware methods often suffer from catastrophic drift due to two impediments: information loss from \textit{Latent--RGB Cycling}, where generated latents are repeatedly decoded to RGB and re-encoded for future conditioning, and the training--inference gap induced by the \textit{error-free hypothesis}, where clean training memory fails to match prediction-corrupted inference memory. To address these challenges, we present \textbf{Robust Dreamer}, a memory-augmented framework built around how to design 3D memory and how to use it robustly. First, we introduce \textbf{Latent Gaussian Memory}, which anchors diffusion latents inherited from the generation process to Gaussian primitives and recalls them via latent-space Gaussian splatting. This provides dense, geometry-aware, view-aligned conditioning while avoiding accumulated degradation from repeated VAE conversion. Second, we propose \textbf{Deviation Learning with Dynamic Deviation Archive}, which synthesizes rollout-induced latent deviations through a one-step approximation, stores them by autoregressive stage and denoising timestamp, and injects them into historical memory during training. This exposes the generator to realistic corrupted memory states and teaches internal correction before inference. Experiments on ScanNet, DL3DV, and OmniWorldGame demonstrate state-of-the-art long-horizon performance.

---


### 124. [DSD-GS: Dynamic-Static Decomposition of Gaussian Splatting for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.30863)

**<font color=#1a73e8>作者：</font>** Youngtae Han, Sung-hwan Han, Youngmin Yi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic scene reconstruction and novel view synthesis are fundamental to next-generation visual intelligence applications such as virtual reality, robotics, and digital twins. However, high-fidelity reconstruction of complex, time-varying scenes from arbitrary viewpoints remains a significant challenge. Existing dynamic 3DGS methods suffer from computational inefficiency, since they model all Gaussians as dynamic components. While recent decomposition-based approaches address this issue, they still struggle with degraded reconstruction quality and prolonged training time. To mitigate these limitations, we propose a novel dynamic reconstruction framework built upon an efficient static-dynamic decomposition strategy using a Feed-Forward Gaussian Splatting encoder and an optical flow model. By eliminating redundant computations on static regions, our method achieves state-of-the-art performance, outperforming existing baselines across rendering quality, training and rendering speed, and storage efficiency. Notably, on the Neural 3D dataset, our framework requires only 10 minutes for training and achieves a rendering speed of over 700 FPS on a single NVIDIA RTX 5090 GPU at resolution of 1352x1014. Furthermore, our decomposition strategy eliminates the need for COLMAP preprocessing and enables deterministic initialization, thereby enhancing both efficiency and reproducibility.

---


### 125. [What makes an action sequence enjoyable to watch?](https://arxiv.org/abs/2605.30864)

**<font color=#1a73e8>作者：</font>** Jean-Peïc Chou, Kristine Zheng, Junyi Chu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People often seek out ways to watch others perform complex action sequences (e.g., sports). What makes some sequences more enjoyable to watch than others? We generated 24 video clips of gameplay from a Flappy Bird-style video game. Clips varied in difficulty (how often players succeeded on average) and in moment-to-moment uncertainty (how likely the player was to crash at any given step). Participants (N=864) rated each video on one of three dimensions: how much they enjoyed it, how difficult the level appeared, or how dangerous the player's trajectory appeared. We found that participants preferred videos where the player seemed to be completing more difficult obstacle courses, but dangerousness did not predict enjoyment ratings. These findings show how procedurally generated stimuli can isolate the factors that affect how enjoyable an action sequence is to watch.

---


### 126. [GUI-C$^2$: Coarse-to-Fine GUI Grounding via Difficulty-Aware Reinforcement Learning](https://arxiv.org/abs/2605.30884)

**<font color=#1a73e8>作者：</font>** Junlong Li, Chao Hao, Lap-Pui Chau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing agentic reinforcement learning methods for GUI grounding have limitations at two levels. At the data level, current approaches typically treat all training samples equally, although their training value to the baseline model varies with difficulty. Overlooking this can greatly reduce training efficiency or even cause collapse. At the strategy level, existing frameworks struggle to balance the trade-off between cropping larger regions for sufficient context and smaller ones for reduced redundancy, a tension inherent to tool-augmented grounding agents. In addition, overly complex decision-making is difficult for small-parameter models and significantly increases inference time. To address these issues, at the data level, we propose GUI-D, a data mining and difficulty scoring pipeline that identifies the training-worthy samples by proper testing and assigns difficulty scores to guide subsequent training weights. At the strategy level, we propose GUI-C$^2$, which employs an area-gated coarse-to-fine refinement mechanism that progressively narrows the visual field via model-internal uncertainty signals, adaptively reserving context for large targets while amplifying precision for small ones, reinforced by improvement-aware stage rewards that ensure each refinement genuinely advances grounding. Meanwhile, we simplify the decision-making process to greatly reduce additional inference time. Finally, extensive experiments show that our method achieves state-of-the-art performance. The code and data will be publicly available.

---


### 127. [Bandwidth Allocation with Device Partitioning for Federated Learning over Industrial IoT networks](https://arxiv.org/abs/2605.30892)

**<font color=#1a73e8>作者：</font>** Kangmin Kim, Jaeyoung Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider a federated learning (FL) system in which Industrial Internet-of-Things (IIoT) devices collaboratively train a global model over wireless channels without sharing local data. In such systems, communication time is a primary bottleneck that constrains overall training efficiency. Unlike conventional networks that prioritize individual quality-of-service requirements, FL systems collectively aim to converge to an optimal global model as efficiently as possible, which calls for a fundamentally different approach to bandwidth allocation. In this paper, we propose a novel bandwidth allocation policy that exploits the heterogeneity of device computing capabilities to minimize total training time. Rather than distributing bandwidth among all selected devices simultaneously, the proposed policy partitions the participating devices into ordered subsets and sequentially grants each subset exclusive access to the full bandwidth. We formally prove that this partitioning-based policy achieves a strictly lower training time than any bandwidth allocation scheme without partitioning, irrespective of the underlying scheduling algorithm. Furthermore, by reducing per-device transmission duration, the proposed policy also minimizes uplink energy consumption, which is particularly beneficial for battery-constrained IIoT devices. Extensive experiments on real-world datasets - including GC10-Det, an industrial surface defect benchmark, and CIFAR-10, a standard image classification benchmark - demonstrate that the proposed policy consistently reduces training time and energy consumption compared to existing bandwidth allocation schemes, approaching the theoretical lower bound on round time.

---


### 128. [Foundation VAEs for 3D CT Reconstruction, Augmentation, and Generation](https://arxiv.org/abs/2605.30893)

**<font color=#1a73e8>作者：</font>** Qi Chen, Shuhan Ding, Yu Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Variational autoencoders (VAEs) compress high resolution CT volumes into compact latents while preserving clinically relevant structure. However, training CT-specific VAEs from scratch or heavily fine-tuning them incurs substantial computational and engineering cost, and often degrades under heterogeneous scanners, protocols, and diseases. This paper makes a progressive stride toward training-free medical VAEs by leveraging a critical observation: a single Foundation VAE, pretrained at scale on natural images and videos, can serve as a unified interface for CT Reconstruction, Augmentation, and Generation. With both encoder and decoder frozen, the Foundation VAE reconstructs CT volumes with preserved anatomy while suppressing acquisition noise; training segmentation models on these reconstructions improves surface accuracy by 3.9% NSD on average for pancreatic tumor and lung tumor. Within the same Foundation VAE latent space, a conditional latent diffusion model achieves 3.9% lower average FVD with 36.2% higher CT CLIP score, and improves multi-disease generation faithfulness across 18 types by 2.76% AUC. These results demonstrate Foundation VAEs as a practical interface for scalable CT representation reuse and faithful CT generation. Our code and demo are available at this https URL.

---


### 129. [SteerFace: Debiasing Synthetic Face Generation via Adaptive Residue Perturbation](https://arxiv.org/abs/2605.30894)

**<font color=#1a73e8>作者：</font>** Yuxi Mi, Qiuyang Yuan, Jianqing Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The shortage of legally compliant data for face recognition training has sparked growing interest in using synthetic data as an alternative. While recent diffusion-based methods enable the generation of photorealistic face images with strong identity adherence and data diversity, their downstream recognition performance still exhibits a significant synthetic-real gap. This paper identifies visual tendency as a previously underexplored limitation, whereby synthetic data exhibit an unrealistic prevalence of visual attributes and thus deviate from the real-data distribution. Visual tendency can be attributed to the generator's conditioning on identity embeddings, through which co-occurring residual visual cues are unintentionally absorbed into learned identity semantics. To discourage the generator from exploiting such visual cues, this paper proposes SteerFace, a simple and efficient training framework that perturbs identity embeddings by steering them toward random orthogonal directions on the embedding hypersphere. The perturbation serves as an identity-preserving regularizer that penalizes the generator's reliance on non-identity components, as supported by theoretical analysis. This paper further introduces an adaptive strategy that learns perturbation strengths with both sample-wise preference and favorable overall statistics. Extensive experiments show that SteerFace effectively mitigates visual tendency, outperforms prior methods in downstream face recognition, and generalizes well across different training datasets and generation pipelines.

---


### 130. [Zero Collapse: A Failure Mode of Policy Gradient Methods in Discontinuous Reward Environments](https://arxiv.org/abs/2605.30896)

**<font color=#1a73e8>作者：</font>** Nishant Kumar, Enrique Areyan Viqueira, Amy Greenwald  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bidding in repeated auctions is a central challenge for reinforcement learning (RL), combining continuous control with the strategic complexities of digital advertising. While policy gradient and value-based methods seem well-suited for these settings, they often struggle with the discontinuous, "cliff-like" nature of auction reward landscapes. In a first-price auction, for example, a bidder receives zero reward until they cross a specific threshold, after which the reward decreases as the bid increases. This creates a landscape of flat, zero-reward regions separated by sharp boundaries.
We identify a fundamental failure mode in this setting termed "zero collapse." We show that stochastic exploration and gradient-based updates can cause policies to overshoot optimal high-reward regions and enter flat, zero-reward regimes. Once there, the lack of an informative gradient signal makes recovery extremely sample-inefficient, effectively trapping the agent. We find that actor-critic methods are particularly susceptible, as biased value estimates can accelerate this movement toward unstable regions.
Our contributions include: (1) a mechanistic explanation of how discontinuous rewards lead to vanishing signals and zero collapse; (2) an analysis of the interaction between policy stochasticity and step size; and (3) an empirical demonstration of this phenomenon across REINFORCE and actor-critic variants. We propose practical mitigation strategies involving initialization and architectural choices to improve stability. Finally, we introduce a formal RL framework for auction environments highlighting their unique structural properties.

---


### 131. [UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling](https://arxiv.org/abs/2605.30898)

**<font color=#1a73e8>作者：</font>** Kaiyu Huang, Xingyu Wang, Mingze Kong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In real-world deployments of large language models (LLMs), balancing inference quality and computational cost has become a central challenge. Existing approaches tackle this trade-off along two largely independent dimensions: model routing, which switches among models of different scales to match request complexity, and test-time scaling (TTS), which adjusts inference-time compute within a fixed model for fine-grained control. However, this decoupled design introduces inherent limitations. Model routing yields coarse-grained, discrete performance changes due to the sparse set of model scales, while single-model TTS often encounters capacity ceilings and exhibits diminishing returns as compute increases. Moreover, treating the two mechanisms separately restricts adaptability in dynamic inference environments. To overcome these limitations, we introduce Unified Inference Scaling (UIS), which unifies model routing and TTS in a single optimization space. Building on this formulation, we propose UniScale, an online framework that models adaptive UIS as a contextual multi-armed bandit problem and learns inference policies via LinUCB. The framework incorporates efficiency-aware learning and cost modeling to ensure stable and scalable optimization over high-dimensional action spaces. Evaluation shows that UniScale effectively exploits the synergy in the UIS space to deliver a fine-grained and consistently better quality-cost trade-off across diverse, dynamic inference scenarios.

---


### 132. [Density-Guided Robust Counterfactual Explanations on Tabular Data under Model Multiplicity](https://arxiv.org/abs/2605.30901)

**<font color=#1a73e8>作者：</font>** Jun Tan, Qing Guo, Zicheng Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations (CEs) are essential for actionable recourse, yet their reliability is often compromised in low-density regions, where classifiers exhibit high variance. Unlike existing methods that rely on expensive ensemble intersections to define stability, we propose \textit{DensityFlow}, a generative framework that constructs robust CEs by adhering to the high-confidence data manifold. Specifically, we model the counterfactual generation as continuous-time dynamics parameterized by Neural ODE, guided by a differentiable density score to actively avoid uncertain, low-density areas. This density score is learned via Noise Contrastive Estimation, effectively leveraging a $(K{+}1)$-way discriminator to estimate density ratios. For black-box settings, we introduce a local proxy distillation mechanism that aligns a lightweight surrogate with the target model strictly within the trajectory of CE generation, enabling efficient gradient-based optimization with minimal queries. Experiments demonstrate that \textit{DensityFlow} achieves superior validity under model multiplicity while significantly reducing query costs compared to ensemble-based baselines. Our implementation is available at this https URL.

---


### 133. [A Core-Structure-Based Automated Analysis Tool for Commercial Virtualization Obfuscation Deobfuscation](https://arxiv.org/abs/2605.30902)

**<font color=#1a73e8>作者：</font>** Wanju Kim, Seoksu Lee, Eun-Sun Cho  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Virtualization obfuscation is a more powerful obfuscation technique compared to other obfuscation methods, and as it is increasingly being applied to malware, it demands significant effort and time from analysts. This study analyzes virtualization obfuscation and proposes a tool called VMPredator that automatically extracts semantic units. The proposed tool performs various analyses including memory analysis and trace analysis, while minimizing dependency on the specific internal structure of virtual machines in order to handle diverse forms of virtualization obfuscation that existing tools are unable to process. Experimental results demonstrate that the length of obfuscated programs was reduced by approximately 85%, and it was verified through validation that small-scale programs were fully restored to semantics identical to the original.

---


### 134. [MergeTok: Unified Continuous and Discrete Visual Tokenization via Token Merging](https://arxiv.org/abs/2605.30904)

**<font color=#1a73e8>作者：</font>** Luyuan Zhang, Siyuan Li, Zedong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most visual tokenizers for image generation are bifurcated into two families with complementary limitations: continuous VAEs offer high-fidelity reconstruction but suffer from dense, entangled latents that are poorly suited for semantic control, whereas discrete VQ-based models enable autoregressive generation yet struggle with gradient sparsity, unstable training, and codebook collapse. In this work, we introduce MergeTok, a unified tokenizer that jointly optimizes continuous (VAE) and discrete (VQ) tokenizers within a encoder-decoder architecture, leveraging token merging techniques as a semantic bridge. By clustering similar tokens during encoding, MergeTok establishes a structural prior that provides dual supervision signals: (i) it imposes merged-token semantic alignment in the VAE branch, regularizing its latent space toward disentangled, semantic-aware representations; (ii) it derives group-wise constraints, promoting intra-group diversity and inter-group exclusivity that stabilize VQ training. MergeTok shows competitive reconstruction and generation performance on ImageNet-256, with substantially lower rFID than strong VAE and VQ models under matched token budgets, while producing semantically-organized token representations compatible with both autoregressive and diffusion generators. This shows that a single architecture can endow visual tokenizers with robust semantic organization and generator-friendly discreteness.

---


### 135. [PINNs Failure Modes are Overfitting](https://arxiv.org/abs/2605.30910)

**<font color=#1a73e8>作者：</font>** Nigel T. Andersen, Takashi Matsubara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) are a common class of machine learning-based partial differential equation (PDE) solvers which train a network to represent a solution by minimizing a residual loss that encodes the PDE. Despite their successes, they are known to fail on certain simple equations, converging to an incorrect solution despite low loss. These failure modes have garnered significant attention in the literature over the past several years, motivating both architectural and optimization based solutions. By directly visualizing the residual, we show that failure modes are the result of overfitting: the loss is minimized on the collocation points, but not elsewhere. Applying regularization causes the failure modes to vanish. Finally, we extend double backpropagation over the full set of residuals, and use it to achieve state-of-the-art performance on four standard failure mode equations with up to $23\times$ fewer collocation points and a vanilla architecture.

---


### 136. [Automating Formal Verification with Reinforcement Learning and Recursive Inference](https://arxiv.org/abs/2605.30914)

**<font color=#1a73e8>作者：</font>** Max Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated formal verification remains challenging for large language models because data for proof assistants and verification-aware languages is scarce, and correctness depends on satisfying precise machine-checkable specifications rather than producing plausible code. This thesis studies how verifier environments can improve LLM generation of verified programs and proofs through reinforcement learning from verifiable rewards (RLVR) and verifier-guided inference-time search. First, we train open-source models in Dafny with RLVR using Group Relative Policy Optimization (GRPO) and related variants, assembling generated candidates into complete programs and scoring them with compiler and verifier outcomes. Initial experiments on an APPS-derived Dafny dataset increased verified reward from 2.2% to 58.1%, but revealed specification hacking, where models exploit weak formal specifications instead of implementing the intended solutions. After filtering underspecified and vulnerable tasks, multi-turn RLVR on the refined benchmark improves the verified pass rate from 9.7% to 31.1%. Second, we develop a verifier-guided inference scaffold in Lean that treats proof generation as structured search over decomposed subgoals, verifier feedback, diagnostics, and repair. With a fixed base model, the full scaffold with proof reviser improves pass rate on an initial VeriCoding pilot set from 46.2% under direct repair to 69.2%. On the larger VERINA dataset, whole-task decomposition plus proof reviser solves 7 of 42 previously unsolved tasks. We also introduce Dalek-Bench, a repository-scale Lean benchmark derived from the Rust $\texttt{curve25519-dalek}$ verification project; preliminary results remain weak, indicating that stronger progress evaluation and task-specific tool-use policies are still needed.

---


### 137. [Welfare, Improvability, and Variance: A Principal-Agent Approach to Optimal Benchmark Item Aggregation](https://arxiv.org/abs/2605.30916)

**<font color=#1a73e8>作者：</font>** Andreas Haupt, Justin Hartenstein, Anka Reuel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI benchmarks have well-documented limitations, with prior work examining contamination, saturation, and construct underspecification. Aggregation has received far less attention: benchmarks are typically summarized by uniformly averaging item-level scores, implicitly treating every test item as equally valuable. We model benchmarking as a multitask principal-agent game and show that the welfare loss from a benchmark is determined jointly by three item-level primitives: alignment with normative welfare priorities, marginal improvability, and performance variance. We translate the theory into an audit framework that ranks items along each of these three axes, and apply it to OLMES items using WORKBank for welfare, the EvoLM 4B suite for improvability, and the PolyPythias 410M panel for variance. The framework surfaces items that are Pareto-inferior within OLMES subject to a pro-worker welfare operationalization. All code is available at this https URL.

---


### 138. [Unsupervised Diffusion Solver for Combinatorial Optimization via Combinatorial Adjoint Matching](https://arxiv.org/abs/2605.30920)

**<font color=#1a73e8>作者：</font>** Shengyu Feng, Tarun Suresh, Yiming Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based neural solvers have shown strong promise for combinatorial optimization (CO), but existing methods typically rely on supervised training with large collections of near-optimal solutions. In this work, we extend adjoint-based trajectory optimization methods to discrete combinatorial domains. We formulate diffusion-based CO as a stochastic control problem over Continuous-Time Markov Chains and introduce discrete adjoint dynamics for propagating optimization signals through discrete generative trajectories. Building on this formulation, we propose Combinatorial Adjoint Matching (CAM), an unsupervised training framework for discrete diffusion solvers with structured and low-variance trajectory-level optimization signals. Empirically, CAM consistently outperforms existing unsupervised diffusion baselines and achieves performance competitive with strong supervised diffusion solvers and even traditional solvers across diverse combinatorial optimization problems. Our code is available at this https URL.

---


### 139. [MultiAct: Text-to-Motion Generation from Composite Text via Tailored Attention Guidance](https://arxiv.org/abs/2605.30925)

**<font color=#1a73e8>作者：</font>** Nathan Sala, Ofir Abramovich, Ariel Shamir 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion generation has progressed rapidly in recent years, offering an expressive interface for animation and human-computer interaction. However, current models remain brittle when handling prompts that describe multiple actions occurring at the same time. Rather than realizing all components of a composite description, models frequently prioritize a single dominant action and neglect the rest, leading to incomplete or ambiguous motion. We present MultiAct, an unpaired, inference-time framework for compositional text-to-motion synthesis that operates directly on pretrained motion generators without retraining or architectural modification. Our method counteracts semantic collapse by adaptively amplifying cross-attention scores associated with underrepresented prompt components. We note that effective modulation depends on prompt-specific choices, such as which tokens and layers to target, and introduce a lightweight auxiliary decision scheme that determines the most effective attention-strengthening parametrization. Extensive quantitative and qualitative evaluations demonstrate that MultiAct consistently outperforms existing baselines on composite prompts, achieving improved semantic coverage while preserving motion realism. Project page: this https URL.

---


### 140. [Local linear convergence of gradient methods for overparameterized Gaussian mixtures](https://arxiv.org/abs/2605.30936)

**<font color=#1a73e8>作者：</font>** Jingxing Wang, Vasileios Charisopoulos, Maryam Fazel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of learning Gaussian mixture models under overparameterization. Prior work has shown that while overparameterization is essential for avoiding spurious local optima and enables global recovery of the ground-truth model using the gradient-EM (expectation-maximization) algorithm, it can dramatically slow down the local rate of convergence. Under certain assumptions on the mixture weights, we show that a standard divergence measure minimized by statistical learning procedures possesses a manifold of slow growth on which the well-known Polyak stepsize reduces the loss geometrically, and design a gradient-based method that converges to minimizers at a locally linear rate. Additionally, we show that our method converges to nearly optimal solutions -- up to a natural misspecification threshold -- for mixtures with arbitrary weights. At a high level, the method alternates between several "short" gradient descent steps that approach the manifold and "long" Polyak steps that contract the distance to minimizers. Our results suggest that slow convergence is not an intrinsic challenge of overparameterization, but can be overcome by exploiting the favorable structure of the loss landscape.

---


### 141. [IAF-Net: Illumination-Adaptive Fusion for Low-Light Urban Road Segmentation](https://arxiv.org/abs/2605.30939)

**<font color=#1a73e8>作者：</font>** Bingtao Wang, Daojie Peng, Fulong Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic road segmentation is important for autonomous driving, but existing methods suffer severe performance degradation under low-light conditions. Many existing multi-modal fusion methods do not explicitly adapt to illumination-dependent changes in modality reliability, which can propagate degraded RGB features into the fused representation at night. We propose IAF-Net (Illumination-Adaptive Fusion Network), an end-to-end framework with illumination-adaptive fusion for robust road segmentation across different lighting conditions. It dynamically adjusts fusion weights of RGB and geometric features via the core Illumination-Adaptive Fusion (IAF) module, and enhances low-light feature selection with a brightness-modulated attention decoder. We also construct two dedicated datasets: nuScenes Nighttime Road Segmentation (nuScenes-NRS) and CARLA Multi-Weather Road Segmentation (CARLA-MWRS). Experiments on nuScenes-NRS show state-of-the-art overall performance among the compared methods, while CARLA-MWRS further validates robustness across adverse weather conditions. Ablation studies on a 40% training subset further highlight the importance of the IAF module, which provides the largest individual gain of 0.70% in MaxF.

---


### 142. [PRISM: Progressive Reasoning through Iterative Slot Memory for Vision](https://arxiv.org/abs/2605.30942)

**<font color=#1a73e8>作者：</font>** Ziyu Wang, Shuangpeng Han, Mengmi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision models process images in a single feed-forward pass, which limits their ability to recover missing evidence or refine uncertain representations under incomplete observations. Inspired by the iterative nature of human perception, we introduce PRISM (Progressive Reasoning through Iterative Slot Memory), a pyramid vision architecture that reasons over images through iterative refinement. At a high level, PRISM groups visual features into object-centric representations, retrieves relevant patterns from a learned memory, and iteratively refines the representation to resolve ambiguity and recover missing information. This organize-recall-refine process operates recurrently across multiple scales, enabling progressive improvement of visual representations. Across standard vision tasks, including image classification, object detection, and semantic segmentation, PRISM achieves competitive performance while demonstrating improved robustness under incomplete observations such as occlusion. These results suggest that iterative reasoning with structured representations and memory is a promising direction for building more resilient and adaptive vision models. Source code and models will be released.

---


### 143. [Extending AI for Research to the Humanities: A Multi-Agent Framework for Evidence-Grounded Scholarship](https://arxiv.org/abs/2605.30947)

**<font color=#1a73e8>作者：</font>** Yating Pan, Jiajun Zhang, Jun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based research agents have advanced rapidly in science and engineering, where research is organized around executable experiments, code, and quantitative signals. Humanities scholarship, however, requires a different mode of reasoning: interpretive, evidence-grounded argument over primary sources, where scholarly value depends on faithful quotation, verifiable provenance, and close reading. Existing research agents remain largely optimized for execution and retrieval, not evidence-grounded interpretive reasoning. To address this gap, we introduce SPIRE (Scholarly-Primitives-Inspired Research Engine), a multi-agent framework for evidence-grounded humanities scholarship. Drawing on Scholarly Primitives theory, SPIRE casts recurring humanities operations as cooperating agent roles (source discovery, evidence annotation, comparison, provenance checking, sampling, citation binding, and argumentative synthesis) over a multi-scale close-reading substrate of passages, intra-context graph communities, and cross-context semantic clusters. On a peer-reviewed-paper benchmark over classical Chinese and Greco-Roman Latin scholarship, SPIRE recovers cited primary-source evidence more reliably than Naive LLM, Text RAG, and GraphRAG, and receives higher blind-judge scores on answer accuracy, depth, coverage, and evidence quality. Ablations show that both the scholarly-operation agents and close-reading retrieval contribute to evidence-grounded essays. Code, data catalogues, and reproduction scripts are released at this https URL.

---


### 144. [Spectral Anatomy of Quantum Gaussian Process Kernels](https://arxiv.org/abs/2605.30952)

**<font color=#1a73e8>作者：</font>** Jian Xu, Chao Li, Guang Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two recent results have reshaped quantum Gaussian processes (QGPs). On the one hand, \citet{lowe2025assessing} rule out the exponential speedups claimed by HHL-based QGP regression in the typical, well-conditioned regime; on the other, an independent line of work shows that highly expressive quantum kernels suffer posterior pathologies that break Bayesian optimization. We show that these seemingly unrelated phenomena are governed by the same quantity: the normalized spectral entropy $S(K)/\log n$ of the kernel Gram matrix. We prove a Cauchy--Schwarz tail bound on Nyström approximation error, a finite-sample variance-contraction identity in terms of Bach's degrees of freedom $d_\sigma(K)$, and a characterization of the \emph{target-dependent} optimal entropy via the intrinsic dimension of the target in the kernel eigenbasis. Empirically, the diagnostic is kernel-agnostic: hardware-efficient, matchgate, IQP \emph{and} RBF/Matérn/RFF/deep-kernel families all collapse onto identical $S/\log n$ curves on dequantization, ECE, and variance-contraction panels. The NLL sweet spot lives at high entropy for smooth targets and at low entropy for band-limited quantum-data targets. The diagnostic transfers from simulator to IBM Heron hardware with median absolute error $3.2\%$ and mean $5.2\%$ in $S/\log n$ across $24$ configurations at $n_q = 4$, with matchgate and IQP within $5\%$ mean and a single HE configuration returning a $30\%$ outlier that drops to $0.5\%$ on rerun (attributed to calibration drift); the same diagnostic transfers to a second Heron backend (mean error $2.7\%$) and to a $n_q = 6$ scale-up on the original backend (mean error $1.7\%$). No error mitigation is applied throughout.

---


### 145. [Revisiting Zeroth-Order Hessian Approximation: A Single-Step Policy Optimization Lens](https://arxiv.org/abs/2605.30960)

**<font color=#1a73e8>作者：</font>** Junbin Qiu, Zhaowei Hong, Renzhe Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate Zeroth-Order (ZO) Hessian estimation is a cornerstone of derivative-free methods, essential for tasks such as bilevel optimization, Bayesian inference, and uncertainty quantification. However, obtaining a complete suite of low-variance estimators for the Hessian and its inverse in high-dimensional settings remains a significant challenge. To address this, we propose a unified framework that reinterprets ZO Hessian approximation through the lens of single-step Policy Optimization (PO). This perspective establishes a theoretical equivalence between general ZO Hessian estimators and the Hessian of a smoothed PO objective, unifying distinct classical randomized estimators as specific instances of baseline selection. Building on this foundation, we introduce ZoVH, a comprehensive suite of variance-reduced estimators for the full Hessian matrix, its regularized inverse, and the bias-corrected inverse Hessian-gradient product. ZoVH leverages two key techniques: (1) a unique optimal baseline derived to provably minimize variance, and (2) a query reuse strategy that incorporates historical function queries to enhance sample efficiency without inflating costs. Our rigorous theoretical analysis confirms the unbiasedness of the Hessian estimator, validates the variance optimality of our baseline, provides error bounds for the entire ZoVH suite, and establishes convergence guarantees for the resulting curvature-aware ZO algorithm. Extensive empirical results validate our theoretical findings, demonstrating that ZoVH achieves superior estimation accuracy and convergence performance in real-world applications. Code is available at this https URL

---


### 146. [Variational Adapter for Cross-modal Similarity Representation](https://arxiv.org/abs/2605.30968)

**<font color=#1a73e8>作者：</font>** WenZhang Wei, Zhipeng Gui, Dehua Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The core of vision-language models lies in measuring cross-modal similarity within a unified representation space. However, most image-text matching or multi-class image classification datasets lack fine-grained cross-modal matching annotations, forcing the continuous similarity space into binary classification boundaries. This compression induces false negative samples and significantly impairs the generalization performance of cross-modal tasks. While prior research has attempted to mitigate this by modeling intra-modal ambiguity, it often overlooks inherent annotation flaws, leading to suboptimal uncertainty allocation. To address these challenges, we propose a Variational Adapter for Cross-modal Similarity Representation (VACSR). This approach reformulates image-text matching with fine-grained semantic scarcity as a variational inference problem. It constructs a latent space for cross-modal similarity and uses regularization techniques to mitigate overfitting to binary annotations. Experiments on image-text retrieval, domain generalization, and base-to-novel generalization demonstrate the proposed method's effectiveness and robust generalization ability.

---


### 147. [Omni-Supervised Motion Editing: Balancing Change and Invariance through Positive-Negative Learning](https://arxiv.org/abs/2605.30969)

**<font color=#1a73e8>作者：</font>** Zhenwu Shi, Jingyu Gong, Peiwei Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based human motion editing aims to modify existing motion sequences according to natural language instructions while maintaining the consistency of the original motion. Existing diffusion-based approaches often rely on heuristic similarity cues or coarse global conditioning, leading to motion distortion and suboptimal semantic alignment. The key challenge lies in balancing change (i.e. precisely editing target regions) and invariance (i.e. preserving unedited parts). To handle such challenge, we propose an Omni-Supervised Positive-Negative Learning framework, named OmniME. Our method integrates three complementary components: (1) retrospective feature supervision that enforces coarse-to-fine consistency across transformer layers,(2) motion preservation mechanism that focuses on subtle variations according to the source-target similarity, and (3) triplet-based semantic alignment that strengthens text-motion correspondence. Together, these components form a unified supervision paradigm that balances change and invariance. Extensive experiments on the MotionFix and STANCE Adjustment datasets demonstrate that OmniME achieves state-of-the-art performance in editing alignment, validating the effectiveness of our unified learning framework. Our source codes and models have been released at: this https URL

---


### 148. [BiSegMamba: Efficient Bidirectional Tri-Oriented Mamba for 3D Medical Image Segmentation](https://arxiv.org/abs/2605.30972)

**<font color=#1a73e8>作者：</font>** Bakht Zada, Chao Tong, Qile Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D medical image segmentation requires both long-range volumetric context and fine boundary preservation. CNN-based methods have limited global dependency modeling, while Transformer-based models are often computationally expensive for dense 3D inputs. Recent Mamba-based methods provide an efficient alternative, but existing volumetric designs still depend on repeated high-resolution scanning, forward-only sequential modeling, and fixed directional summation, causing high cost, scan-order bias, and suboptimal directional aggregation. We propose BiSegMamba, an efficient bidirectional tri-oriented Mamba network for 3D medical image segmentation. BiSegMamba follows a compact-to-detail design, where a progressive compacting stem (PCS) enables efficient latent-space reasoning while retaining shallow high-resolution features for reconstruction. A multi-scale spatial mixer (MSSM) captures local anatomical patterns in early stages, and the proposed bidirectional tri-oriented Ortho Mamba (Bi-ToOM) block models long-range dependencies from multiple orthogonal views using jointly processed forward and backward scan sequences. Adaptive directional fusion (ADF) learns input-dependent channel-wise weights across scan orientations, replacing fixed summation with orientation-aware fusion. Experiments on a collected carotid CTA dataset and three public benchmarks, BraTS2023, ACDC, and AMOS-CT, show that BiSegMamba generalizes well across vascular, cardiac, brain tumor, and abdominal multi-organ segmentation tasks. Compared with SegMamba-V2, BiSegMamba achieves slightly better performance on BraTS2023 and clear improvements on ACDC and the carotid dataset, while reducing computational cost by up to 77.9% FLOPs, demonstrating a strong accuracy-efficiency balance for general 3D medical image segmentation.

---


### 149. [Cognitive Fatigue in Autoregressive Transformers: Formalization and Measurement](https://arxiv.org/abs/2605.30981)

**<font color=#1a73e8>作者：</font>** Riju Marwah, Ritvik Garimella, Vishal Pallagani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models frequently degrade during long-horizon generation, producing repetitive text, losing instruction adherence, and exhibiting unstable entropy. Despite the prevalence of these failures, practitioners lack online diagnostics to detect them in real-time as they occur. We formalize this degradation as cognitive fatigue, a measurable generation-time state characterized by decay in attention to the original prompt, representational drift, and entropy miscalibration. We introduce the Fatigue Index (FI), a lightweight, model-agnostic diagnostic that aggregates these three signals under explicit axioms (monotonicity, boundedness, interpretability) enabling reliable runtime monitoring. Across nine models (1B-13B parameters), FI trajectories exhibit structured temporal dynamics, predict task degradation (AUROC = 0.95) and repetition (Spearman rho = 0.94), and reveal non-monotonic scaling behavior: instruction-tuned models below 3B exhibit faster collapse than base models, with this trend reversing at 7B. Stress analyses further show that FI onset accelerates under longer contexts, middle-positioned evidence, and reduced numerical precision. These results establish cognitive fatigue as a coherent and measurable phenomenon, and position FI as a principled tool for runtime reliability monitoring in production LLM systems.

---


### 150. [Can BEV Perception Gracefully Degrade under Sensor Failures?](https://arxiv.org/abs/2605.30983)

**<font color=#1a73e8>作者：</font>** Haifa Zhang, Yijing Wang, Haoyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable success of multi-modal bird's-eye view (BEV) perception in autonomous driving, current systems exhibit a critical vulnerability: existing fusion mechanisms are highly brittle to sensor corruptions, often causing catastrophic performance degradation. This vulnerability largely stems from the fact that standard fusion frameworks typically integrate multi-modal representations in a static manner, leading to a precipitous performance collapse under missing or corrupted modalities. In contrast, we show that graceful degradation is achievable through active modality reliability assessment. To this end, we present Grace-BEV, a lightweight and plug-and-play framework that enforces active reliability awareness during multi-modal fusion. Instead of relying on computationally expensive cross-modal interactions, Grace-BEV leverages the aligned BEV space to explicitly assess modality trustworthiness via a TrustGate Router and dynamically recalibrate feature integration using the FailSafe Fusion Block. Furthermore, we devise a Three-Phase Training strategy with Modality Dropout to prevent modality dominance and encourage balanced cross-modal learning under unreliable inputs. Extensive experiments on nuScenes-R and nuScenes-C show that Grace-BEV maintains robust performance across diverse corruption settings. Notably, under catastrophic LiDAR failures where standard baselines collapse to 0.0% mean Average Precision (mAP), Grace-BEV restores performance to as high as 34.7% mAP. Moreover, it improves clean accuracy by up to 1.4%, achieving a strong trade-off between robustness and efficiency.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-317](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
