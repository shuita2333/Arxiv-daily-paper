# 📦 其他研究 | 2026年06月29日

> 本类共 **245** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-245](./part-05.md)

---

### 101. [FracEvent: Event-Camera Simulation via Fractional-Relaxation Pixel Dynamics](https://arxiv.org/abs/2606.26636)

**<font color=#1a73e8>作者：</font>** Langyi Chen, Chuanzhi Xu, Haoxian Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras asynchronously report brightness changes with microsecond-level temporal resolution, but real event data remain difficult to collect at scale because specialized sensors, careful synchronization, and task-specific annotations are required. Event-camera simulation is therefore important to event-based vision tasks. Most practical simulators build on contrast-threshold event generation, some with additional filtering, stochastic noise, or hand-tuned sensor parameters. While effective, such formulations often simplify the temporal structure produced by the lifecycle of each pixel, which can distort event timing and weaken downstream transfer. We introduce FracEvent, an event simulator that models this pixel-level lifecycle with fractional-relaxation voltage dynamics. Given a log-intensity trajectory, FracEvent drives a compact stack of relaxation modes, combines their responses into a voltage state, emits ON/OFF events by localizing threshold crossings on the continuous voltage trajectory, and updates the reference while retaining the underlying memory modes. This retained state links residual voltage response to later event timing. We evaluate FracEvent through event-stream comparison and downstream transfer on image reconstruction and optical flow estimation. Across multiple datasets, FracEvent improves the temporal structure of generated events and achieves stronger downstream-transfer results than competing simulator baselines, showing its practical value for event-camera simulation.

---


### 102. [Invisible Impact of Empathy on Behavioral Change: Isolating the Effect of Empathy in Long-term Physical Activity Coaching Chatbot Interactions](https://arxiv.org/abs/2606.26641)

**<font color=#1a73e8>作者：</font>** Li Siyan, Kai-Hui Liang, Shopnil Shahriar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current dialogue systems, powered by large language models, often treat empathy as essential without assessing its true impact, especially in behavior change, where motivation and adherence often depend on subtle user-chatbot dynamics. We examine this assumption by building three WhatsApp physical-activity (PA) coaching chatbots that differ only in empathy level and evaluating them in a six-week within-subject study (N = 13). Participants struggled to distinguish between the empathy conditions, and the non-empathetic version was often rated as more engaging and useful. However, higher-empathy variants were still associated with a larger overall average increase in step counts and faster improvement in intention to follow advice. These results suggest empathy's role is nuanced: it may be hard for lay users to identify explicitly, but it can still shape motivation and trust that support sustained change. We interpret this pattern through the Elaboration Likelihood Model's peripheral route. We highlight design implications for building next-generation PA coaching chatbots that balance effectiveness with human-like connection.

---


### 103. [LayersReg: A Layer-by-Layer Progressive Regressor for Reliable Intraoperative 3D/2D Registration](https://arxiv.org/abs/2606.26647)

**<font color=#1a73e8>作者：</font>** Xiyuan Wang, Zhenchao Wang, Xinran Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D/2D registration serves as a cornerstone technique in surgical navigation. Traditional iterative optimization algorithms suffer from low efficiency and high failure rates in intraoperative settings. Deep learning-based methods reformulate registration from iterative optimization to a regression problem that maps image appearance features to spatial pose, typically achieving improved real-time performance and accuracy. However, such learnable methods are confined to memory-driven retrieval of specific pose features rather than understanding the task of image alignment itself, which limits their generalization in complex scenarios. We propose LayersReg, a pioneering regression paradigm that endows the model with 3D anatomical awareness and searches for the correct pose in a progressive, layer-by-layer manner. Inspired by the iterative pose-searching optimization criterion of classical registration, LayersReg searches for correlations between the moving and fixed images in feature space, capturing the trend of pixel flow and thereby converging iteratively toward the correct spatial pose transformation. We further design a coupling of node-wise regression with the progressive registration framework to enhance the model's perception of spatial pose changes. Experimental results demonstrate that under large offsets and multimodality conditions, LayersReg achieves high accuracy on both X-ray/CT registration (0.68°, 1.41 mm) and slice localization (0.73°, 1.55 mm) tasks, outperforming existing state-of-the-art methods while meeting the intraoperative demands for precision and real-time capability.

---


### 104. [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/abs/2606.26649)

**<font color=#1a73e8>作者：</font>** Adam Mondl, Matthew Maisel, John H. Brock  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent safety in high-stakes domains requires formal policy enforcement, but most existing approaches either rely on probabilistic guardrails (fine-tuned classifiers, prompt-based steering) that offer no formal guarantees, or on hand-coded symbolic enforcement that does not scale to the breadth of real policy specifications. We present an autoformalization pipeline that translates agent prompts, MCP tool descriptions, and natural language policy documents into formally verified policies using an LLM-based generator-critic loop. The resulting policies are written in the Cedar Policy Language. On the MedAgentBench benchmark, our autoformalized policies cover substantially more of the source natural-language specification than the hand-coded symbolic enforcement in prior work.

---


### 105. [Target-Aware Bandit Allocation for Scalable Surrogate Optimization in Chemical Space](https://arxiv.org/abs/2606.26657)

**<font color=#1a73e8>作者：</font>** Mohammad Haddadnia, Yuvan Chali, Abhilash Jayaraj 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying high-utility candidates from massive discrete spaces under expensive evaluations is a recurring challenge across the sciences, with structure-based drug discovery as a prominent example. While surrogate-based optimization can increase sample efficiency by reducing the number of expensive evaluations, modern molecular libraries have reached billions to trillions of compounds, making full-library surrogate inference itself a major computational bottleneck. We introduce BOBa, a bandit-guided surrogate optimization framework that eliminates full-library inference by adaptively allocating computation across partitions of the action space. By treating partitions as arms in a multi-armed bandit, BOBa concentrates inference and evaluations on empirically promising partitions while maintaining principled exploration. Experiments on real-world synthesis-on-demand libraries demonstrate that optimism-under-uncertainty bandits, combined with meaningful action space partitioning, are essential for effective allocation of inference and evaluations. Our findings reveal a tunable tradeoff between screening performance and surrogate inference cost, which supports practical optimization over current libraries, and establishes a viable route to ultra-large library virtual screening.

---


### 106. [Zero-Shot Size Transfer for Neural ODEs on Sparse Random Graphs: Graphon Limits and Adjoint Convergence](https://arxiv.org/abs/2606.26662)

**<font color=#1a73e8>作者：</font>** Mingsong Yan, Zhida Wang, Sui Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Differential Equations (GNDEs) model continuous-time graph dynamics by parameterizing Neural ODE velocity fields with Graph Neural Networks. Their local, size-independent filters suggest a zero-shot size-transfer principle: train on a small graph and deploy on larger, similar graphs without retraining. We develop a quantitative theory for this principle on sparse random graphs sampled from graphons. We consider Graphon Neural Differential Equations (Graphon-NDEs) and adjoint Graphon-NDEs as the infinite-node limits of the forward and adjoint GNDE systems, and establish well-posedness. For an $n$-node random graph with sparsity parameter $\alpha_n$, we prove trajectory-wise convergence of GNDE solutions to Graphon-NDE solutions at rate $O((\alpha_n n)^{-1/2})$, up to logarithmic factors, with high probability. We also establish uniform-in-time convergence bounds for adjoint systems governing hidden-state and parameter gradients. We further study discretize-then-optimize (DTO) and optimize-then-discretize (OTD) training. Under explicit Euler discretization with $M$ steps, we show that DTO and OTD are asymptotically consistent, with hidden-state and local parameter-gradient discrepancies of orders $O(1/M)$ and $O(1/M^2)$, respectively, up to sparsity and logarithmic factors. Experiments on HSBM and tent graphons support the theoretical rates, while zero-shot transfer experiments across four graphon classes demonstrate accurate deployment of learned GNDEs on larger independently sampled graphs.

---


### 107. [TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems](https://arxiv.org/abs/2606.26664)

**<font color=#1a73e8>作者：</font>** Ngoc Bao Anh Le, Thai T. Vu, John Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. We propose TGHE (Template-based Graph Homomorphic Encryption), an ego-centric framework that resolves this by exploiting a template phenomenon: local computation trees in transaction graphs converge into a small set of structural shapes. TGHE canonicalizes ego-graphs at the edge and packs structurally identical trees into shared CKKS ciphertexts for SIMD-parallel encrypted inference, with two long-tail optimizers (Approximate Template Fitting and Topology Collapse) ensuring full SIMD coverage. On DGraphFin (3.7M nodes, 4.3M edges), TGHE-Collapse achieves a 66.9x speedup over the sequential encrypted baseline with less than 0.002 AUC loss.

---


### 108. [Disco-LoRA: Disentangled Composition of Content, Style, and Motion for Multi-concept Video Customization](https://arxiv.org/abs/2606.26668)

**<font color=#1a73e8>作者：</font>** Xuancheng Xu, Gengyun Jia, Bing-Kun Bao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video customization based on Text-to-Video (T2V) models aims to learn specific features from reference data to generate controllable videos. While significant strides have been made in image stylization and video motion customization, simultaneously controlling multiple concepts, such as content, style, and motion, remains a major challenge. In this work, we systematically define the task of multi-concept video customization, which requires the joint control of content, style, and motion. To facilitate research in this area, we construct a comprehensive benchmark and propose Disco-LoRA, a unified framework designed to tackle this problem by disentangling and flexibly recombining different concepts in two stages: (1) We decompose the objective into two sub-tasks: Content-Style and Content-Motion. Each sub-task is addressed using our Iterative Dual-LoRA Disentanglement Framework, which effectively disentangles distinct concepts within the data. (2) We identify layer-wise weight trends as crucial for LoRA identity, while weight magnitudes dictate composability. To harmonize these scales, we propose a Z-score-based statistical regularization that aligns weight distributions, preserving layer-wise trends while minimizing interference between different LoRAs. Extensive experiments show that Disco-LoRA excels in multi-concept video customization, effectively preserving appearance, style, and motion for controllable text-to-video generation.

---


### 109. [SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills](https://arxiv.org/abs/2606.26669)

**<font color=#1a73e8>作者：</font>** Zhongxin Guo, Danrui Qi, Hanwen Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents often repeatedly solve similar task instances from scratch, leading to unnecessary reasoning cost and long execution traces. Prior work has explored workflow reuse and executable skill induction, but it remains unclear which task scenarios admit procedural skills and how the shared procedural structure should be represented across successful traces. We study this problem in FSM-defined scenarios, where successful traces can be viewed as paths in an unknown transition graph, and formulate procedural skills as reusable parameterized control-flow subgraphs. Based on this view, we introduce SkillDisCo, a distillation-and-compilation framework that distills reusable PFSM subgraphs from successful traces and compiles them into callable, executable, and verifiable procedural skills. Experiments on ALFWorld and WebArena show that SkillDisCo improves success rates and reduces agent turns across benchmarks and model scales, demonstrating the benefits of representing shared experience as reusable execution structures.

---


### 110. [From Content to Strategy: Understanding the Motivations, Processes, and Impacts of AI-Guided Communication](https://arxiv.org/abs/2606.26672)

**<font color=#1a73e8>作者：</font>** Chang Wan, Angel Hsing-Chi Hwang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence-mediated communication (AI-MC) is conceptualized as applying AI to augment or generate message content (Hancock et al., 2020). However, advances in generative AI have expanded its use beyond generating content to guiding individuals' communication strategies, that is, AI-guided communication, yet theoretical and empirical understandings of this emerging use pattern and its consequences remains limited. To address this gap, this study conducted 26 in-depth interviews with individuals who have used AI to develop their communication strategies. Findings suggest participants strongly preferred using AI to analyze challenging scenarios in close relationships, because it fostered self-reflection, eased emotions, prevented conflict escalation, offered multiple perspectives, and provided a safe, nonjudgmental space for self-disclosure. Participants also stated that AI-guided communication enhanced their empathy and communication skills, though some voiced self-doubt and worried about losing their uniqueness. Views on long-term relational impact were mixed, depending on perceived usefulness of AI for resolving short-term interpersonal challenges.

---


### 111. [Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation](https://arxiv.org/abs/2606.26686)

**<font color=#1a73e8>作者：</font>** Dongbin Na  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In order to screen a prompt or a response, the recent guardrail methods generate a chain-of-thought (CoT) before they issue a verdict. This design follows a common belief that step-by-step reasoning improves a decision. However, CoT also makes the guard heavy and slow, because the model must generate many tokens before it decides. This may not match how guardrails are actually deployed. A guardrail sometimes should not be heavy and slow, and it often runs on-device, for example on an embodied robot. In this paper, we pose a question whether a safety guardrail really needs to reason. To answer this question, we train a lightweight bidirectional encoder and a reasoning guard on the same corpus, and we then remove only the reasoning while we keep everything else fixed. With this controlled same-base comparison, we show that the chain does not improve moderation accuracy. We name the resulting guard LeanGuard. A 395M label-only encoder reaches an average F1 of 82.90 $\pm$ 0.26 over public benchmarks. It matches a reasoning guard that is built on a much larger decoder, while it uses only a single forward pass over an input of at most 512 tokens. This is about a ~100x reduction in inference compute. We further show that this label-only encoder stays robust under training-label noise and retains far more recall at a strict false-positive rate than the reasoning guard, so a heavier reasoning guard is not the more robust choice either. Our finding suggests that the current guardrail benchmarks may not be hard enough to reward reasoning, and that the necessity of CoT for moderation is still not proven. We release all source codes and models including LeanGuard at this https URL.

---


### 112. [DeCoFlow: Structural Decomposition of Normalizing Flows for Continual Anomaly Detection](https://arxiv.org/abs/2606.26687)

**<font color=#1a73e8>作者：</font>** Hun Im, Jungi Lee, Subeen Cha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In industrial environments, new product categories arrive sequentially, requiring continual anomaly detection without access to past data. Normalizing Flows (NFs) provide exact density estimation but suffer from catastrophic forgetting as parameter updates across tasks distort the density manifold. While parameter isolation can prevent interference, it must preserve the strict invertibility and Jacobian validity of NFs. To satisfy these requirements, we exploit the inherent property that affine coupling layers maintain transformation validity regardless of subnet parameterization. Based on this, we propose DeCoFlow, which decomposes subnets into a frozen universal base and task-specific low-rank adapters to isolate updates. We further introduce Task-Specific Alignment, Auxiliary Coupling Layers, and Tail-Aware Loss to compensate for frozen-base rigidity. DeCoFlow achieves state-of-the-art image-level AUROCs of 98.40% on MVTec-AD and 93.00% on VisA, while maintaining parameter-level zero forgetting (0.00% FM under correct routing) with only 2.27M parameters per task.

---


### 113. [The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in Asset-Backed Tokens](https://arxiv.org/abs/2606.26704)

**<font color=#1a73e8>作者：</font>** JJ Jia Jing Tan, Eva Meng, Josh Ng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The tokenization of real-world assets (RWAs) has emerged as a transformative application of blockchain technology, with market projections estimating trillions of dollars in tokenized assets within the coming decade. However, a fundamental challenge remains unaddressed: physical assets such as precious metals, stored commodities, and warehoused goods incur structural negative carry -- custody, insurance, and audit costs that accumulate over time. While existing tokenization models have successfully established the market for digital gold and treasuries, they typically manage operational costs at the issuer level. The FRS introduces a framework to bring these economics directly on-chain, avoiding mechanisms such as token rebasing that compromise fungibility and composability with decentralized finance (DeFi) protocols. This paper proposes the Fungible Reserve Standard (FRS), a deterministic token design framework that encodes carrying costs transparently into on-chain logic. The FRS introduces an asset-per-token variable q(t) that decreases according to a predefined annualized carrying cost rate, coupled with a supply reconciliation mechanism that preserves holder balances and ERC-20 composability. While mathematically inspired by the daily expense ratio accrual in traditional asset management -- which often embed centralized profit margins -- the FRS design specifically encodes actual operational carrying costs to provide pure institutional-grade accounting clarity without compromising DeFi compatibility. The framework is asset-agnostic and applicable to any real-world asset with positive, predictable holding costs.

---


### 114. [Algorithmic Foundations of Deep Learning: Complexity-Theoretic Rates and a Characterization of Universal Approximation](https://arxiv.org/abs/2606.26705)

**<font color=#1a73e8>作者：</font>** Anastasis Kratsios, Simone Brugiapaglia, Bum Jun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feedforward neural network (NN) expressivity is typically studied by emulating optimal basis-expansion schemes. While powerful, this perspective is incomplete: it primarily captures complexity through regularity, and therefore does not distinguish intuitively simple and complicated objects with comparable regularity, such as the square-root function and a typical Brownian path.
The guiding message is that neural networks should be viewed not only as flexible basis functions, but also as models of computation. If a function is computable by a real-valued circuit over a prescribed elementary gate language, then it can be computed to comparable accuracy by an NN with explicit depth, width, and non-zero-parameter bounds controlled by the depth, width, gate count, and gate structure. Thus, neural-network complexity is not governed by regularity alone, but also by algorithmic complexity. We then show that any definable NN model satisfying a natural parallelization condition, allowing possibly multivariate non-linearities such as attention or layer normalization, is a universal approximator if and only if it contains a non-affine nonlinearity.
The scope of our theory is illustrated by deducing universal approximation guarantees for continuous functions, minimax-optimal approximation guarantees for Besov classes, logarithmic-error complexity for holomorphic functions, and by showing that NNs can emulate numerical algorithms such as Newton-Raphson root finding and power iteration without architecture-specific arguments. Its precision is illustrated by shortest-path computation on $k$-vertex graphs: compiling the tropical dynamic-programming circuit yields NNs with O(log(1/{\epsilon})) non-zero parameters, exponentially improving in 1/{\epsilon} over the generic $O({\epsilon}^{-c k^2})$ Lipschitz-approximation scale, for a constant c>0.

---


### 115. [Intracranial Aneurysm Classification and Segmentation via Tri-Axial ROI and Multi-Task Learning](https://arxiv.org/abs/2606.26706)

**<font color=#1a73e8>作者：</font>** Pengcheng Shi, Kaiyuan Yang, Houjing Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intracranial aneurysms are often asymptomatic until rupture, which carries high mortality. Rupture risk assessment and treatment planning depend on both aneurysm morphology and anatomical location, yet existing automated methods remain limited to binary detection without fine-grained anatomical classification or multi-class segmentation. We present a multi-task framework that simultaneously performs multi-label classification, multi-class aneurysm segmentation, and multi-class vessel segmentation across 13 anatomical locations and four imaging modalities (CTA, MRA, T2, T1-post). Our two-stage approach combines a fast 2D tri-axial Region of Interest (ROI) extraction method with a 3D multi-task nnU-Net backbone. A dual-decoder design mitigates the extreme volume imbalance between aneurysm and vessel classes, while cross-attention pooling and modality-specific auxiliary heads improve feature learning across heterogeneous inputs. Our two-fold ensemble achieved 2nd place in the RSNA 2025 Intracranial Aneurysm Detection challenge. Code, model weights, and a 3D Slicer plugin are publicly available.

---


### 116. [DroidBreaker: Practical and Functional Problem-Space Attacks on Machine-Learning Android Malware Detectors](https://arxiv.org/abs/2606.26707)

**<font color=#1a73e8>作者：</font>** Christian Scano, Diego Soi, Angelo Sotgiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial APKs are Android applications modified in the problem space to evade machine-learning malware detectors. In this work, we first show that, despite claims, existing problem-space attacks remain largely impractical. Most techniques leverage software transplantation to inject entire benign modules, introducing many side-effect features and often causing build-time failures. Fine-grained methods that inject only a narrow subset of components exhibit limited effectiveness, while those that also use obfuscation rely on brittle bytecode rewriting, producing APKs that are syntactically valid but semantically unusable. Prior work further overestimates attack success rates by running smoke tests that only validate installation and basic execution, without assessing whether the modified APK still preserves its intended behavior. To overcome these limitations, we present DROIDBREAKER, a practical (build-safe) and functional (semantics-preserving) problem-space attack framework that provides: (i) query-efficient white- and black-box attacks by manipulating only the APK components most influential to the target model; (ii) a set of fine-grained, build-safe manipulations (including injection and obfuscation of API calls, app modules, permissions, and URLs) with minimal side effects; and (iii) a semantics-preserving functionality test that enforces runtime equivalence by comparing execution logs and API-level traces between the initial and the modified APK. Evaluated on a recent corpus of Android applications, DROIDBREAKER achieves high evasion rates with few queries and minimal side effects in both white-box and black-box settings, and drastically reduces detections by commercial malware scanners hosted on VirusTotal.

---


### 117. [Kalman Prototypical Networks for Few-shot Fault Detection in Combined Cycle Gas Turbines](https://arxiv.org/abs/2606.26710)

**<font color=#1a73e8>作者：</font>** Mohammed Ayalew Belay, Lucas Ferreira Bernardino, Adil Rasheed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combined-cycle gas turbines (CCGTs) play a key role in modern power generation, offering both high efficiency and reduced environmental impact. However, their complex thermo-fluid and mechanical interactions complicate fault detection, particularly when labeled fault data are scarce. In this paper, we introduce the Kalman Prototypical Network (KPN), a metric-based few-shot learning (FSL) framework specifically tailored for CCGT fault diagnosis. We model the evolution of class prototypes as latent stochastic states in a dynamic system to reduce episodic variance and improve robustness in embedding representation. Synthetic data sets generated with a high-fidelity Modelica-based dynamic simulation of an offshore CCGT system were used, simulating both normal operation and progressive leak faults under transient conditions. Application of the proposed framework on simulated leak fault detection tasks demonstrate that KPN outperforms conventional FSL methods such as Matching Networks, Relation Networks, and MAML in both accuracy and stability under varying support and query configurations. The proposed framework significantly improves training convergence and generalization by stabilizing class representations, making it well-suited for real-world CCGT fault detection where labeled data is limited.

---


### 118. [Mask to Concept: Auto-Promptable SAM3 via Efficient Test-Time Concept Embedding Search for Few-Shot Annotation](https://arxiv.org/abs/2606.26711)

**<font color=#1a73e8>作者：</font>** Quan Zhou, Shaoqing Zhai, Qiang Hu Jia Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transforming foundation segmentation models from human-prompted tools into auto-promptable annotators is critical for scalable medical data annotation. Current methods commonly depend on external feature matchers or auxiliary networks to automate geometric prompting, but introducing architectural overhead and limiting performance scalability. Although SAM3 natively supports concept segmentation via reusable text prompts, its direct use in medical imaging is hindered by a lack of fine-grained clinical knowledge and the ambiguity of human-written descriptions. In this work, we propose Mask to Concept (M2C), an efficient framework that adapts SAM3 for medical few-shot annotation without external modules, parameter retraining, or manual text engineering. Using only a few labeled images, M2C enables SAM3 to automatically search for transferable visual concepts entirely within its frozen architecture: it initializes a learnable concept embedding, uses it to prompt segmentation, and updates the embedding by gradients of minimizing the concept segmentation error. We further introduce a Hybrid Uncertainty Estimation (HUE) module that calculates the prediction entropy and maps concept predictions back to the box prompts, measuring concept-geometry prompting inconsistency. Highly uncertain samples are flagged actively for human correction, and the corrected masks are then fed back to M2C to continuously search for more precise concept embeddings, forming a self-enhancing annotation loop with minimal expert effort. Experiments on medical segmentation benchmarks show that our method achieves SOTA few-shot segmentation performance and outstanding annotation efficiency, offering a practical and efficient pathway toward scalable medical image labeling. Codes are at this https URL.

---


### 119. [Extracting Neural Materials from Multi-view Images](https://arxiv.org/abs/2606.26715)

**<font color=#1a73e8>作者：</font>** Kim Youwang, Jon Hasselgren, Peter Kocsis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural materials can represent complex specular reflections and scattering effects in a compact, universal basis. However, acquiring and authoring such materials remains challenging. We present NeuMatEx, a differentiable inverse rendering method for extracting spatially varying neural materials from images. The nonlinear structure of neural material latent spaces makes optimization with naive inverse rendering infeasible. To address this, we train a Large Material Reconstruction Model (LMRM) that directly predicts initialbase color, neural material latents, and aleatoric uncertainty guides from images. This material prior provides a good initialization and better constrains our subsequent optimization using inverse path tracing. The predicted uncertainty further helps by anchoring high-confidence regions more tightly to the LMRM prediction, preventing lighting and complex specular effects from being baked into materials. Experiments on synthetic and real assets show that NeuMatEx extracts complex materials with better visual quality and material decomposition than PBR-based methods.

---


### 120. [A Latent ODE Approach to Spatiotemporal Modeling of Cine Cardiac MRI](https://arxiv.org/abs/2606.26718)

**<font color=#1a73e8>作者：</font>** David Brüggemann, Ekaterina Krymova, Firat Özdemir 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cardiac magnetic resonance imaging (CMR) captures rich spatiotemporal information about ventricular structure and motion, but conventional risk models use only a few image-derived indices from selected cardiac phases. We present a latent dynamical model that encodes bi-ventricular anatomy and full-cycle cine motion as a continuous latent trajectory, using heart-rate-aware neural ordinary differential equation (ODE) dynamics and a graph-based mesh autoencoder to reconstruct anatomically consistent 3D+t ventricular motion. A covariate-conditioned prior defines the expected end-diastolic latent state, and a Cox proportional hazards model tests whether deviations from this prior predict incident heart failure. We studied 72,386 UK Biobank participants without baseline cardiovascular disease, including 367 incident heart failure events. In a held-out evaluation subset, adding the latent score to refitted pooled cohort equations improved the stratified C-index from 0.704 to 0.785, compared with 0.764 for seven established cardiac markers. Compared with non-graph and non-ODE approaches, the proposed model gave the best trade-off between reconstruction fidelity, generative realism, and downstream prognostic performance. These results suggest that continuous full-cycle modeling of ventricular motion provides informative cardiac phenotypes beyond conventional CMR summaries, while external validation in more representative patient cohorts is required before clinical risk-prediction use.

---


### 121. [Full spectrum Unlearnable Examples via Spectral Equalization](https://arxiv.org/abs/2606.26719)

**<font color=#1a73e8>作者：</font>** Jiale Cai, Gezheng Xu, Zhihao Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlearnable examples (UEs) protect training data by injecting imperceptible perturbations so that models fail to extract exploitable representations. In this paper, we reveal that existing UEs exhibit a critical failure once low-pass filtering is applied, indicating that the effective perturbation signals for unlearnability concentrate predominantly in high frequencies. Hence, we argue that reliable UEs should remain effective across the full spectrum. To this end, we propose Full-spectrum Unlearnable examples via Spectral Equalization (FUSE), which aims to generate spectrum-agnostic perturbations by equalizing the contributions from different bands and enforcing cross-band consistency. Specifically, FUSE adopts a Random Spectral Masking (RSM) strategy during generator training, which randomly removes a contiguous frequency band, forcing the remaining bands to maintain unlearnability. In addition, FUSE further integrates Cross-Band Guidance (CBG), which enforces mutual consistency between high- and low-frequency components, thereby further enhancing low-frequency unlearnability and regulating high-frequency perturbations to preserve the semantic fidelity of images. Extensive experiments across multiple datasets, architectures, and spectral filtering demonstrate the strong protection achieved by FUSE.

---


### 122. [Socratic agents for autonomous scientific discovery in high-dimensional physical systems](https://arxiv.org/abs/2606.26722)

**<font color=#1a73e8>作者：</font>** Xianrui Zeng, Pengfei Liu, Yirui Zang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The automation of scientific discovery has reached an inflection point. While AI systems now operate instruments, optimize parameters and generate hypotheses, most remain procedural: they execute workflows fixed by human designers. True autonomous science demands epistemic autonomy--the capacity to construct, challenge and revise physical explanations in response to evidence. Here we introduce AHOIS, a multi-agent AI scientist that embeds Socratic midwifery into closed-loop experimentation. A physics-critic agent interrogates hypotheses through causal questioning, constraint checking, counterexample generation and falsification-criteria formulation. We evaluate AHOIS on a real multimode-fibre optical platform, a high-dimensional system with complex wave transformations, indirect detection, environmental drift and multi-modal acquisition. Without prior encoding schemes, classifiers or speckle models, the system autonomously proposed and validated a random-interference encoding hypothesis, discovered task-adaptive sparse-measurement strategies, diagnosed distinct failure modes (encoding instability, fluorescence contamination and detector noise) and translated a published imaging protocol into an executable workflow on a non-original configuration. The discovered encoding yielded 16x16 measurements with effective rank 56.9 and classification accuracies of 76.97% on MNIST and 83.17% on Fashion-MNIST. Ablations show that Socratic interrogation improves physical consistency, hypothesis completeness, uncertainty calibration and experimental-plan validity. These results establish a route from workflow automation towards evidence-grounded, self-correcting autonomous discovery in complex physical environments.

---


### 123. [Modeling Adaptive Visual Search in Semantically Hierarchical Layouts](https://arxiv.org/abs/2606.26725)

**<font color=#1a73e8>作者：</font>** Saku Sourulahti, Jussi P. P. Jokinen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper introduces a computational cognitive model to investigate how information grouping impacts visual search, a key consideration in user interface design. The model uses computational rationality to view user behavior as an adaptation to cognitive and task constraints. Our work highlights that humans use hierarchical task representations, exploiting semantic and visual structures to improve search efficiency within the constraints of the visual system. We validate this model with data from two human studies focused on visual search and semantic categorization, demonstrating that semantic grouping improves search performance when it aligns with spatial grouping. Our model replicates task durations and eye movement patterns. By improving understanding of how hierarchical memory structures are utilized in human cognition, the model extends previous visual search models. We showcase our model in the rapid prototyping and evaluation of semantic visual groupings within user interface wireframes, suggesting a pathway toward applications in more complex, real-world interface design.

---


### 124. [Scientific discovery as meta-optimization: a combinatorial optimization case study](https://arxiv.org/abs/2606.26728)

**<font color=#1a73e8>作者：</font>** Yuan-Hang Zhang, Chesson Sipling, Massimiliano Di Ventra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery is fundamentally an optimization problem, defined by a vast "state space" of theories and experiments, and an evaluation criterion based on quality, novelty, and validity. Large language models (LLMs) have enabled automated exploration of this space, but we argue that simultaneous modification of the evaluation criteria is equally important. Here, we propose formalizing research as meta-optimization, where the optimization objective itself is also being optimized. Our key contribution is "consensus objective aggregation," where LLM-generated objective functions are combined via correlation-weighted voting, yielding a stable, self-correcting evaluation criterion that evolves as understanding deepens. We apply this framework to algorithm discovery for 3-SAT problems based on digital MemComputing machines, reducing the baseline scaling with problem size $N$ from $\sim N^{2.51}$ to $\sim N^{1.33}$ and delivering a $\sim 67\times$ speedup on the largest instances tested. As a problem-agnostic framework, we hope this approach will considerably aid scientific discovery.

---


### 125. ['A bit of chaos and madness': The AI Assessment Scale and the work of assessment reform](https://arxiv.org/abs/2606.26729)

**<font color=#1a73e8>作者：</font>** Mike Perkins, Darius Postma, Jasper Roe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (GenAI) has intensified pressure on universities to redesign assessment while maintaining integrity, equity, and validity. Structured frameworks such as the Artificial Intelligence Assessment Scale (AIAS) offer one response, but evidence of how staff experience their implementation remains limited. This qualitative study examines AIAS implementation at a private international university in Vietnam and a public university in the United Kingdom. Data from five focus groups with 30 academic staff were analysed using hybrid thematic analysis, with Critical AI Literacy used as a sensitising concept. Six themes were developed: recognising and integrating AI, facilitating conditions, building capacity, pathways to adoption, ethics in practice, and reframing pedagogy.
Staff valued the AIAS as a shared language for legitimising GenAI use, clarifying boundaries, and prompting reflection on assessment design. However, implementation was shaped by governance, tool access, staff confidence, workload, integrity concerns, disciplinary context, and alignment with learning outcomes. The findings show that the AIAS could prompt authentic assessment design and student engagement, but may become a compliance layer when disconnected from learning outcomes, disciplinary context, and staff capacity. This study contributes empirical evidence on the institutional conditions through which GenAI assessment frameworks move from policy adoption to pedagogical enactment.

---


### 126. [Robust Onion: Peeling Open Vocab Object Detectors Under Noise](https://arxiv.org/abs/2606.26734)

**<font color=#1a73e8>作者：</font>** Priyank Pathak, Mukilan Karuppasamy, Aaditya Baranwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The impact of real-world noise on Open Vocabulary Object Detectors (OV-ODs) remains poorly understood due to their architectural complexity. We present our comprehensive analysis Robust Onion, an empirical study that uses controlled synthetic visual degradations to peel OV-ODs layer-by-layer, revealing how, why, and where robustness degrades, systematically analyzing feature collapse. Our findings reveal that models with similar vision backbones exhibit comparable robustness, driven by similar feature collapse at similar layers, while factors such as pretraining strategy, architectural nuances, and caption supervision contribute little. Robustness is primarily governed by the image domain rather than annotations, explaining the similar robustness impact on COCO and LVIS, and why datasets like ODinW-13 can give an impression of inflated robustness due to large, isolated objects. Finally, we validate our insights by improving robustness on real-world BDD100K, WiderFace, and VisDRONE via our lightweight plug-and-play NN & TK0 approach, using 96x fewer trainable parameters than end-to-end training. We also explain the prior works' robustness observations.

---


### 127. [Do Image Editing Models Understand Lighting?](https://arxiv.org/abs/2606.26738)

**<font color=#1a73e8>作者：</font>** Tim Küchler, Johann-Friedrich Feiden, Matthias Nießner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent advancements in generative image editing models have achieved stunning visual fidelity, it remains an open question whether these systems possess an intrinsic knowledge of real-world lighting. Existing benchmarks typically evaluate high-level plausibility of perceptual light transport on curated internet imagery, using VLMs or human judgement, or they rely on synthetically generated datasets. In this work, we introduce the 3D-anchored Light Probe (3DLP) benchmark, for which we have captured a new high-fidelity HDR dataset of real-world lighting changes. The dataset consists of 1K image pairs of diverse indoor scenery in which light probes are physically turned on and off. To allow for a granular performance analysis, we annotated specific image regions such as cast shadows or metallic surfaces. With this data, we evaluate a range of state-of-the-art image editing models by measuring how well their light probe edits align with reality. The evaluation uses two new scores to compensate for AI-generated photographic effects, such as adjusted white balance. Our results show that the overall performance of models differs considerably, with differences slightly less pronounced for specular highlights. The best image editing models are remarkably consistent with real-world physics, however, they still leave room for improvement. We observe that image regions that receive less light from the light probe are more prone to errors for all models. Furthermore, building on their success in evaluating macroscopic lighting plausibility, we test VLMs on our task but find that they are unsuitable for pixel-level light transport analysis. We will make the benchmark, together with the real-world dataset, publicly available to encourage future research on this topic.

---


### 128. [LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing](https://arxiv.org/abs/2606.26740)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Chongbo Zhao, Fangneng Zhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video editing has made rapid progress, yet practical deployment is still limited by two core issues: maintaining stable backgrounds and non-edited regions over time, and achieving the low latency required for real-time interactive scenarios. Meanwhile, recent streaming video generation methods are mostly developed for synthesis and cannot be directly applied to editing due to the strict preservation requirement and region-specific control. In this work, we present a novel streaming video editing framework that performs causal, frame-by-frame editing with strong content preservation and real-time responsiveness. Our key design is a three-stage distillation pipeline that progressively transfers editing capability from a powerful bidirectional foundation model to an efficient unidirectional streaming editor, enabling stable long-horizon edits without sacrificing visual fidelity. To further support real-time deployment, we introduce an AR-oriented mask cache that reuses region-related computation across frames, substantially reducing redundant processing and accelerating inference. Finally, we establish a dedicated benchmark for streaming video editing. Extensive evaluations demonstrate that our method achieves state-of-the-art visual quality among streaming baselines while drastically boosting inference speed to 12.66 FPS, making it suitable for interactive and augmented reality applications.

---


### 129. [HyperDFlash: MHC-Aligned Block Speculative Decoding with Gated Residual Reduction](https://arxiv.org/abs/2606.26744)

**<font color=#1a73e8>作者：</font>** Luxi Lin, Shuang Peng, Rui Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present HyperDFlash, a block-parallel speculative decoding framework tailored to the novel multi-hyper-connection (MHC) architecture proposed by DeepSeek-V4. Despite the strong initial-token drafting performance of the native Multi-Token Prediction (MTP) module in DeepSeek-V4, its draft accuracy degrades sharply at later positions, as error accumulation from unverified intermediate tokens harms acceptance rates. Although the original DFlash method supports efficient one-pass block drafting, it cannot be seamlessly adapted to the MHC paradigm, since the multi-path residual stream of DeepSeek-V4 induces feature misalignment with conventional drafting designs. To resolve this mismatch, we propose two model-aligned optimizations for MHC residual streams. First, we adopt pre-collapse residual states as the exclusive conditioning signal, preserving multi-path structural information and aligning the drafter with the native prediction pathway of the target model. Second, we replace the heavy generic linear compressor with a lightweight gated residual reducer, whose parameters are inherited from the built-in hyper-connection head. This design yields input-aware path aggregation with three orders of magnitude fewer parameters while maintaining architectural alignment. We further enhance training via a targeted KL distillation loss applied to the LM-head, which regularizes predictions against the full target probability distribution and improves draft quality at early training stages. Experiments across math reasoning, code synthesis, and conversational benchmarks show that HyperDFlash consistently outperforms both the native MTP baseline and vanilla DFlash adaptation. It achieves substantial gains in average accepted draft length and decoding speedup, validating the effectiveness of MHC alignment, gated reduction, and targeted distillation for high-performance speculative decoding.

---


### 130. [Structure Before Collapse: Transient semantic geometry in next-token prediction](https://arxiv.org/abs/2606.26749)

**<font color=#1a73e8>作者：</font>** Yize Zhao, Isabel Papadimitriou, Christos Thrampoulidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Collapse predicts that balanced one-hot classification pushes model representations to be equally far from each other; a symmetric configuration that depends only on the output label and ignores any semantic similarity in the inputs. This creates a puzzle: next-token prediction language models are trained predominantly (as context length increases) with one-hot labels: the same context is very unlikely to appear twice in training with different labels. However, they clearly learn latent structural features. That is, despite the one-hot training regime, a language model's contextual embeddings represent the fact that the next word in ''Mary broke the ___'' is likely to be filled by tokens in the latent classes of a) medium-sized, b) rigid, c) inanimate nouns. How does gradient descent find such categorical semantic structure when co-occurrence statistics collapse to one-hot sparsity, eliminating any shared next-tokens among different contexts? To investigate this tension we identify three synthetic controlled settings where inputs have latent semantic factors but are mapped to distinct one-hot labels. We find that semantic geometry emerges early in training, and that representations cluster by shared attributes despite receiving no explicit supervision to do so. This structure is transient: with sufficient capacity and time, the model eventually reaches the predicted symmetric state where all representations are equally separated. We study this phase transition through Gram matrix analysis and propose a preliminary modification to the commonly used unconstrained features model to capture the emergent semantic geometry.

---


### 131. [ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification](https://arxiv.org/abs/2606.26753)

**<font color=#1a73e8>作者：</font>** Taiheng Pan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational memory retrieval optimizes relevance, yet a retrieved memory can be relevant and simultaneously outdated: a later turn updates, corrects, or supersedes it. ConvMemory v3 adds a validity context layer that detects and surfaces this update evidence through target-conditioned relation verification, sitting after the v1/v2 retrieval path. The core mechanism is a dual-evidence gate that conditions a relation judgment on the specific target proposition, scoring a (target, source) pair through the product of a MiniLM slot head and a DeBERTa-v3 slot head and gating it by conservative event/operation evidence. On a synthetic multi-hop validity benchmark the gate reaches 90.12% +/- 1.73 accuracy; through a real-data feedback loop that mines failure patterns but trains on synthetic pairs only, the verifier transfers to Memora role binding with zero target-side labels, reaching 98.8% +/- 0.9 group-all-correct. The deployed layer preserves retrieval by default: a context mode attaches structured validity metadata while keeping the candidate set and rank order fixed, and a query-conditioned demote mode is an explicit opt-in for dense current-state workloads, where it raises current-active H@1 from a never-demote baseline of 45.1% to 95.7% +/- 1.2 while protecting non-superseded memories at 99.4% recall. Six machine-verifiable safety contracts pin the layer's behavior. Multi-hop graph propagation is validated as a mechanism; fully automatic construction of strict prerequisite edges is characterized as a boundary, since strict necessity requires counterfactual world knowledge. This report extends ConvMemory v1 (arXiv:2605.28062) and v2 (arXiv:2606.10842).

---


### 132. [Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting](https://arxiv.org/abs/2606.26754)

**<font color=#1a73e8>作者：</font>** Zhihao Wen, Yixin Yang, Bojian Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) provides an efficient and explicit representation for novel view synthesis, enforcing stylistic coherence across viewpoints remains challenging. Existing 3D stylization methods typically apply 2D feature-matching losses independently per rendered view, which leads to unstable style allocation, many-to-one feature reuse, and limited cross-view consistency. We propose a capacity-controlled framework for multi-view stylization of 3DGS, grounded in optimal transport. Specifically, we reformulate local style matching as a semi-balanced optimal transport problem. By introducing explicit column-capacity constraints with tunable strength, our formulation mitigates many-to-one matching and enables controllable allocation of style features. This transport-based objective provides a principled mechanism for balancing feature coverage and stylistic diversity while maintaining stable correspondences across viewpoints. To further enhance cross-view coherence, we incorporate a novel cross-view matching guidance to constrain correspondences between scene content and style patterns. In addition, we introduce several geometric regularizations to enhance the vanilla 3DGS, thereby enabling optimized Gaussian primitives to represent finer-grained textures during stylization. Extensive experiments demonstrate that our approach significantly improves multi-view stylistic consistency and produces stable, expressive 3D stylizations while preserving the core semantic structure of the scene.

---


### 133. [Batch-Invariant Spectral Intelligence for Robust and Explainable Insect Authentication](https://arxiv.org/abs/2606.26757)

**<font color=#1a73e8>作者：</font>** Majharulislam Babor, Giacomo Rossi, Annalisa Altavilla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edible insects offer an efficient source of alternative protein, requiring less land, water and emitting less greenhouse gas than conventional livestock. However, their successful integration into the food supply chain demands reliable species authentication to control allergen exposure, prevent adulteration, and meet regulatory standards. Near-infrared spectroscopy provides a rapid analytical tool, but its performance drops when applied to production batches unseen during training due to batch-to-batch variation in spectral measurements. We introduce the Batch-Invariant Spectral Network (BISN), an end-to-end framework that combines a learnable preprocessing module, initialised with Savitzky-Golay filtering, with an entropy-regularised adversarial objective to suppress batch-specific spectral variation. In contrast to Domain-Adversarial Neural Networks, which enforce domain adaptation only after feature extraction, BISN suppress batch-effects before species-specific features are learned. Using 2,700 spectra from three species (Acheta domesticus, Hermetia illucens, and Tenebrio molitor) collected across three independent production batches, BISN achieves a mean leave-one-batch-out accuracy of 0.93 (standard deviation 0.04), outperforming the strongest baseline by four percent. Further insights gained by using explainable AI confirm that model decisions consistently rely on the lipid and protein absorption regions across all folds, connecting predictive performance to known insect biochemistry. BISN addresses both cross-batch robustness and biochemical interpretability for automated insect species authentication under realistic industrial conditions. The source code and dataset are publicly available at this https URL.

---


### 134. [ProtoKV: Streaming Video Understanding under Delayed Query with Summary-State Memory](https://arxiv.org/abs/2606.26762)

**<font color=#1a73e8>作者：</font>** Le Tu Ngoc Minh, Jinyeong Lim, Dongsu Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding (SVU) must answer queries that arrive asynchronously while visual tokens stream continuously under strict GPU-memory and query-time latency budgets. A key challenge is delayed query: decisive cues may appear briefly, yet many subsequent updates occur before the query arrives, increasing the risk that those cues are evicted or diluted under bounded memory. We propose ProtoKV, a constant-footprint SVU memory that represents far history as a fixed-capacity summary state rather than retaining token instances. ProtoKV keeps an exact near-window KV cache and aggregates older content into a semantic-spatial prototype bank with residual statistics. At query time, each prototype is exposed through a bounded pseudo-token interface that is drop-in compatible with standard attention. Under matched budgets and comparable query-time cost, ProtoKV improves accuracy by up to 12.5 points over token-retention baselines on SVU benchmarks in the long-delay regime, with gains that grow as query delay increases.

---


### 135. [Calibrated Harmonic Overlaid Implicit Neural Representations for Multi-Dimensional Data](https://arxiv.org/abs/2606.26763)

**<font color=#1a73e8>作者：</font>** Honghang Chen, Xiujun Zhang, Xiaoli Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representation (INR) has emerged as a powerful prior for multi-dimensional data (e.g., multispectral images and videos). However, most INR methods employing periodic activation functions (e.g., Sine) predominantly rely on function composition. This mechanism introduces optimization instability as network depth increases, thereby limiting their performance. Meanwhile, these methods fail to incorporate proper physical priors to effectively alleviate spectrum bias. To address these issues, inspired by the commonalities between deep periodic networks and generalized Fourier series, we propose a novel Calibrated Harmonic Overlaid Implicit Neural Representation (CHOIR). Specifically, we utilize Coordinated Harmonic Superposition (CHS) to replace the conventional function composition used in most INRs, thereby ensuring optimization stability when scaling network depth. Furthermore, we introduce a Perceptual Spectrum Calibration (PSC) to mitigate spectrum bias. This calibration embeds the ubiquitous power-law spectrum prior of natural images and adjusts the globally fixed spectrum towards a physically plausible log-uniform distribution. Extensive experiments on various multidimensional data recovery problems demonstrate that our method achieves superior performance over state-of-the-art approaches. Code is available at this https URL.

---


### 136. [Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis](https://arxiv.org/abs/2606.26764)

**<font color=#1a73e8>作者：</font>** Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a 4D controllable generative framework for anatomically consistent data augmentation. A semi-supervised variational autoencoder learns a compact latent representation of anatomical volumes while jointly predicting aligned segmentation masks in a unified framework. Anatomical structure is then disentangled from temporal dynamics through a cascaded latent diffusion model (LDM). A static LDM generates subject-specific anatomy conditioned on clinical priors (diagnosis and volumes measures) and a subsequent motion LDM estimates residual latent motions, ensuring strict temporal coherence across the 4D sequence. The proposed approach was evaluated on cine cardiac MRI as a representative 4D imaging application. Experiments across multiple datasets demonstrate high controllability of static anatomy (Pearson r > 0.8) and strong temporal coherence (FVD = 288.08). In cross-vendor generalization experiments, augmenting training sets with synthetic 4D sequences significantly improves downstream segmentation performance. Using nnU-Net, the proposed augmentation strategy improves the average Dice score by 1.4% and reduces the Hausdorff Distance by 3.0mm compared to training on real data alone, for the left ventricle, Dice improves by 2.8% with a 5.4mm reduction in boundary error. Overall, this framework provides a scalable and controllable solution for 4D medical image synthesis, supporting the development of more robust models with limited annotations and cross-vendor variability. Code available on this https URL.

---


### 137. [ResilPhase: Plug-and-Play Phase Mapping and Noise-Resilient Macro-Trajectory Extrapolation for Diffusion Acceleration](https://arxiv.org/abs/2606.26769)

**<font color=#1a73e8>作者：</font>** Qicheng Zhao, Yu Li, Qi Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The adoption of powerful diffusion models is hindered by their significant inference latency. Recent ``cache-then-forecast'' schemes alleviate this issue by accelerating DiTs using derivative-based polynomials, but they suffer from severe quality degradation at high acceleration ratios. Our analysis reveals its root cause: the discrete extrapolation performed on representations that are misaligned with the continuous diffusion trajectory and are numerically unstable. Thus, accelerated DiTs suffer from accumulated spatial errors, noisy derivative amplification, and high-order instability. We therefore reformulate accelerated inference as stable macro-trajectory extrapolation in ordinary differential equation (ODE) space. Instead of predicting intermediate features, we align forecasting with the model's Global Drift (GD), i.e., the end-to-end state evolution, thereby eliminating feature inconsistency and memory overhead. However, even this smooth macro-trajectory remains vulnerable to the derivative fallacy: its higher-order temporal derivatives are intrinsically noisy. Thus, we introduce a derivative-free barycentric Lagrange extrapolator to effectively bypass derivative instability and approximation error. We further propose a bounded Phase Mapping that regularizes the extrapolation domain, suppressing oscillatory error growth. These elements collectively constitute ResilPhase, a noise-resilient acceleration framework. Experiments on FLUX.1-dev and HunyuanVideo demonstrate state-of-the-art fidelity under aggressive acceleration ratios.

---


### 138. [Escaping Iterative Parameter-Space Noise: Differentially Private Learning with a Hypernetwork](https://arxiv.org/abs/2606.26772)

**<font color=#1a73e8>作者：</font>** Naoki Nishikawa, Shokichi Takakura, Satoshi Hasegawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private (DP) training of neural networks is often hindered by the large amount of noise required by gradient-based methods such as DP-SGD, which repeatedly inject high-dimensional noise in parameter space throughout training. In this paper, we propose a new framework for DP learning that avoids iterative optimization in parameter space. Instead of updating the target model using privatized gradients, we employ a hypernetwork trained on public datasets to map a private dataset to the parameters of the target model. Specifically, each example is embedded into a low-dimensional representation, the embeddings are aggregated and perturbed to obtain a DP dataset embedding, and the hypernetwork generates the target model parameters from this noisy embedding. Because privacy noise is injected only once into a low-dimensional dataset representation, our approach can significantly reduce the adverse effect of noise. We theoretically show in a synthetic setting that, under a fixed privacy budget, models produced by our approach achieve higher utility than those trained with DP-SGD. Moreover, we apply our approach to LoRA fine-tuning of diffusion models and show that it achieves lower FID than LoRA models trained with DP-SGD and other public-data-guided methods.

---


### 139. [Evaluation Pitfalls and Challenges in Multimedia Event Extraction](https://arxiv.org/abs/2606.26775)

**<font color=#1a73e8>作者：</font>** Philipp Seeberger, Steffen Freisinger, Tobias Bocklet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimedia event extraction aims to jointly identify events and their arguments across multiple modalities, such as text and images, to support more comprehensive event understanding. While recent work reports steady and substantial progress, the reliability and comparability of these results critically depend on consistent and rigorous evaluation. In this work, we present the first systematic analysis of evaluation pitfalls in multimedia event extraction and identify three major sources of issues: inconsistent data processing, inconsistent task assumptions, and overly relaxed evaluation settings. We demonstrate, through a series of controlled experiments under a strict evaluation framework, that minor evaluation choices can cause large performance variations and lead to overestimation of a model's ability to ground real-world events across modalities. Our findings highlight the need for comparable evaluation standards and encourage a shift toward more rigorous evaluation in multimedia event extraction.

---


### 140. [LearniBridge: Learnable Calibration of Feature Caching for Diffusion Models Acceleration](https://arxiv.org/abs/2606.26778)

**<font color=#1a73e8>作者：</font>** Xuyue Huang, Zhe Chen, Wang Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have driven substantial progress in image and video generation but suffer from prohibitive computational costs. Feature caching accelerates inference by reusing intermediate representations. Existing methods rely on historical features for implementation simplicity, yet suffer from severe error accumulation at high acceleration ratios. To address this limitation, we investigate the nature of the requisite feature correction. We demonstrate that the optimal calibration update is characterized by a shared low-rank subspace across diverse prompts. Guided by this structural insight, we propose LearniBridge, a learnable calibration mechanism for feature caching that bridges multiple timesteps through lightweight LoRA updates. This mechanism enables effective calibration requiring only 3-5 training samples. Extensive experiments on image and video generation show that LearniBridge achieves up to $5.87\times$, $5.75\times$, and $4.10\times$ acceleration on FLUX, HunyuanVideo, and WAN2.1, respectively. On WAN2.1, it improves VBench by 1.28% over the previous SOTA at $4.10\times$ acceleration. Our code is available at this https URL.

---


### 141. [Event-based Gaze Control System for Accurate Real-time Spin Estimation in Professional Ball Games](https://arxiv.org/abs/2606.26780)

**<font color=#1a73e8>作者：</font>** Yunpu Hu, Fabian Schilling, Valentina Cavinato 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spin plays a crucial role in many ball sports due to its effect on the trajectory of the ball. Vision-based estimation of the ball's spin during a game with conventional cameras is challenging due to the ball's small size, high speed, and fast rotation. To address these challenges, we propose an event-based active vision system that can track unmodified balls and measure their spin in real-time. The system consists of an event camera for its high temporal resolution and minimal motion blur, high-speed pan/tilt galvanometer mirrors to keep the ball in the field of view, and a low-latency focus-tunable telephoto lens to increase the spatial resolution on the ball and keep it in focus. To track the ball, we use a hybrid approach that combines 2D event-based detection for centering and 3D positions from a ball localization system for re-initialization. For high-accuracy spin estimation, we propose an offline method that performs contrast maximization on the sphere (s-CMax). This method achieves state-of-the-art accuracy on static balls across multiple sports (table tennis, baseball, tennis, and golf), with mean magnitude and axis errors of 2.1% and 4.0 degrees, respectively. We then develop a low-latency online method for table tennis as a case study in real-time applications. This method uses an uncertainty-aware convolutional neural network trained on pseudo-ground-truth spin labels from the offline approach, combined with a GPU-accelerated batch implementation of contrast maximization for refinement. We demonstrate reliable tracking and spin estimation with a three-view setup during professional table tennis matches, with high accuracy (8.8% magnitude and 6.4 degrees axis mismatch), 3 ms latency, and 750 Hz throughput.

---


### 142. [MergeLLL: A Hierarchical Divide-and-Conquer Framework for LLL-Based Lattice Reduction](https://arxiv.org/abs/2606.26784)

**<font color=#1a73e8>作者：</font>** Niharika Gauraha  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Lattice basis reduction algorithms have various applications in computational number theory and lattice-based cryptography, but their complexity increases rapidly with the dimension. Motivated by the divide-and-conquer strategy of merge sort and incorporating PotLLL-style deep insertions during recombination, MergeLLL is proposed. In this framework, a lattice basis is split into sub-bases, local reductions are performed independently, and the full basis is reconstructed through hierarchical merging.
The approach is focused on improving local lattice structure first before global basis properties are refined, resulting in enhanced Gram-Schmidt orthogonality and numerical stability, while overall computational cost is reduced. The method is naturally parallelizable, allowing efficient multicore and distributed execution. It is shown that the reduction and merging steps preserve the lattice structure through unimodular transformations and achieve logarithmic parallel depth. In experiments on subset-sum and NTRU-derived lattices, improvements over classical lattice reduction algorithms are demonstrated, including better orthogonality, a reduced number of expensive swap operations, and an improved Hermite factor, indicating higher-quality reduced bases.

---


### 143. [NaviCache: Test-Time Self-Calibration Caching for Video Generation](https://arxiv.org/abs/2606.26795)

**<font color=#1a73e8>作者：</font>** Zheqi Lv, Zhibo Zhu, Jinke Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Diffusion Models (VDMs) is constrained by immense computational costs. While offline calibration-based acceleration suffers from calibration data dependency, prohibitive calibration duration, and susceptibility to distribution shifts, offline calibration-free methods eliminate these hurdles. However, since they rely on instantaneous zero-order approximations where the mapping between input and output differences varies in real-time, they are susceptible to observational noise and ignore the intrinsic momentum within the diffusion trajectory. In this paper, we propose NaviCache, a plug-and-play test-time self-calibration method re-conceptualizing feature evolution as an Inertial Navigation System (INS) problem. NaviCache bridges the fundamental domain gap and the non-stationary nature of diffusion by modeling the relative coupling between input and output variations. We introduce a dual-state estimation architecture that adaptively tracks the feature change ratio and its latent drift, initialized via a specialized Initial Alignment phase. By integrating a time-dependent noise schedule with an uncertainty-aware Measurement Update mechanism, NaviCache provides a theoretically grounded mechanism for error-bounded computation skipping. Extensive experiments on the HunyuanVideo, Wan, and Open-Sora series demonstrate that NaviCache exhibits more accurate error judgment for computation skipping and achieves outstanding comprehensive performance.

---


### 144. [From Vajrayana Tara to Bengali Baul: A Computational Study of Lexical Transmission Across Buddhist, Shakta, and Vaishnava Traditions in Bengal](https://arxiv.org/abs/2606.26803)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a computational corpus study of vocabulary relationships across eight tradition layers of Bengali and Sanskrit devotional literature spanning the 8th to 19th centuries, encompassing Buddhist Vajrayana, Shakta Tantra, Vaishnava, and Baul traditions. Using a corpus of 75 texts and TF-IDF character n-gram vectorization with cosine similarity analysis, we address the historically argued but previously unquantified claim that Buddhist Vajrayana vocabulary survived the collapse of the Pala monasteries and was absorbed into the Shakta Tantra tradition of Bengal. The central finding is a specificity result: the Gitagovinda (Vaishnava Sanskrit, 12th century) has zero cosine similarity to Shakta Kali texts, while Bridge Tara texts (Buddhist-Shakta transitional, same century, same language) have cosine similarity 0.54 to Shakta Kali. This 8.5-fold contrast between two Sanskrit traditions from the same century demonstrates that the Buddhist-Shakta vocabulary overlap is not a generic property of Sanskrit devotional literature but is specific to the Buddhist-Shakta transmission chain. Three Brihannilatantra Tara texts show Shakta-to-Buddhist vocabulary ratios of 2.0 to 4.0, constituting measurable evidence of lexical transition within that chain. Ramprasad Sen's 18th-century Bengali Kali songs preserve Buddhist vocabulary residue including 56 occurrences of Tara alongside 103 occurrences of Kali. The Vaishnava Bengali tradition contributes a parallel chain to modern Baul vocabulary (similarity 0.29), slightly weaker than the Buddhist Sahajiya chain via Charyapada (0.31). These results provide the first quantitative multi-tradition corroboration of historically argued Buddhist-Shakta syncretism in Bengal.

---


### 145. [Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents](https://arxiv.org/abs/2606.26806)

**<font color=#1a73e8>作者：</font>** Haoliang Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running language agents need more than memory access. Retrieval systems can fetch past facts at query time, but they do not decide which experiences should continue to shape behavior after the working context is unloaded. We study this separate problem as memory depth: durable goal-conditioned tendencies written into a small parametric store. We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. We evaluate EVAF, a surprise- and valence-gated LoRA consolidation mechanism. Across GPT-2 and TinyLlama, retrieval is strongest on shallow factual recall (short-fact accuracy 0.956--0.973), while EVAF is strongest on goal persistence and post-unload recovery (0.812--0.904) with only 2--3 parametric writes per 200 events. Mechanism controls show that selective consolidation factorizes into two controllable dimensions: selection and actuation. Matched random gates isolate selection beyond sparse writing; fixed-inner controls across GPT-2, TinyLlama, and Mistral-7B show that inner-loop write strength is model-dependent; and a Mistral-7B matched-gate inversion reveals asymmetric selection-actuation coupling under miscalibrated actuation. Public Memora event streams serve as an external diagnostic, exposing stale-memory invalidation as an unresolved boundary. Within this probe, selective parametric consolidation supplies memory depth distinct from and complementary to retrieval access.

---


### 146. [Multi-modality Image Fusion under Adverse Weather: Mask-Guided Feature Restoration and Interaction](https://arxiv.org/abs/2606.26812)

**<font color=#1a73e8>作者：</font>** Xilai Li, Xiaosong Li, Haishu Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modality image fusion (MMIF) enhances scene representation by exploiting complementary cues from different modalities. Adverse weather, however, causes significant image degradation, disrupting feature representation and requiring simultaneous feature restoration and cross-modal complementarity. Existing methods often struggle with effective representation learning under such conditions, limiting their practical performance. To address these challenges, we propose a mask-guided MMIF method that integrates feature restoration and interaction. We first introduce "Pseudo Ground Truth" to simplify training, promoting faster and more effective feature learning. Then, we design a mask generation mechanism based on the mapping relationship between the fused result and the source images, quantifying the relative contribution of each modality during the fusion process. By incorporating the proposed mask-guided cross-modal cross-attention mechanism, the network is encouraged to selectively attend to informative features during modality interaction, mitigating the risk of overfitting to the static distribution of the "Pseudo Ground Truth". Additionally, we propose a mask-guided learning strategy and a task-coupled degradation-aware learning strategy to balance feature restoration and interaction. Extensive experiments on synthetic and real-world datasets demonstrate that our method surpasses state-of-the-art approaches in visual quality, quantitative metrics, and downstream tasks. The source code is available at this https URL.

---


### 147. [Computational Analysis of Heart Rate Variability in Healthy Adults](https://arxiv.org/abs/2606.26816)

**<font color=#1a73e8>作者：</font>** María J. Lado, Arturo J. Méndez, Leandro Rodriguez-Liñares 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heart Rate Variability (HRV) analysis is a key indicator of cardiac physiological state and aids in disease diagnosis. However, research on HRV parameters in healthy individuals remains limited, and no gold standard exists. This study evaluates HRV indices in 40 healthy adults (20 men, 20 women, aged 30-50) to improve HRV's clinical utility. Using computational methods for signal processing and data analysis, time, frequency, and nonlinear indices were analyzed to address five questions: (1) normality, (2) stability, (3) correlation, (4) reproducibility, and (5) consistency. Key findings: (1) Time-domain and nonlinear indices, particularly global and LF (low frequency), follow normal distributions, with gender differences noted. (2) Most indices are stable except HF (high frequency)-related ones. (3) High correlations in HF-related indices suggest redundancy, indicating only one is necessary in studies. (4) Comparisons with the Fantasia database revealed less than 10% error for most indices, except SD2 and SDNN in women (greater than 15%). (5) Time-domain and nonlinear indices show low inter-study variability, while frequency-domain indices exhibit high variability, limiting cross-study comparisons. The selected indices-ApEn and IRRR (global variability), HRVi and SD2 (LF), and MADRR or rMSSD (HF)-are best suited for accurately representing HRV components and enhancing its clinical and research relevance.

---


### 148. [Quantization in Federated Learning: Methods, Challenges and Future Directions](https://arxiv.org/abs/2606.26822)

**<font color=#1a73e8>作者：</font>** Farwa Ikram, Dipanwita Thakur, Antonella Guzzo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) has become a foundational paradigm for privacy-preserving distributed intelligence, yet its scalability remains fundamentally constrained by communication bottlenecks, device heterogeneity, and the challenges of training under statistically non-IID data. Quantization is one of the most effective mechanisms for mitigating these limitations, reducing both uplink/downlink payloads and on-device computation. This paper provides the first FL-centric systematic review of quantization, introducing a novel taxonomy organized around FL-specific dimensions, including client heterogeneity, aggregation consistency, communication-scheduling adaptation, non-IID robustness, privacy/security integration, and hardware/energy co-optimization. Beyond cataloging existing methods, we analyze how quantization interacts with core FL behaviors such as client drift, partial participation, convergence stability, secure aggregation, and differential privacy. We further identify cross-method insights, open research gaps, and design guidelines for practitioners deploying quantized FL on mobile, IoT, and edge platforms. This survey thus establishes quantization not merely as a compression technique, but as a fundamental systems component shaping the performance, robustness, and practicality of modern FL.

---


### 149. [Learning Adversarial Augmentation Policies for Robust Garlic Seedling Detection](https://arxiv.org/abs/2606.26828)

**<font color=#1a73e8>作者：</font>** Soeun Lee, Chanho Kim, Yeji Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate seedling detection during early growth stages is essential for timely replanting and effective crop management in precision agriculture. However, existing studies are mostly evaluated under relatively stable imaging conditions, such as UAV imagery or greenhouse environments, leaving robust detection under severe and spatially heterogeneous illumination in ground-based outdoor monitoring insufficiently explored. In addition, many illumination-robust detection methods rely on additional enhancement or feature-extraction modules, which increase inference-time overhead and are not tailored to seedling detection and downstream missing seedling localization. To address these gaps, we construct a new garlic seedling dataset captured using a ground-based monitoring platform under real outdoor field conditions with highly variable illumination. We further propose an illumination-robust seedling detection framework based on adversarial augmentation policy learning. The proposed method jointly optimizes a stochastic augmentation policy agent and an object detector, enabling the detector to learn robust representations under challenging visual conditions. A structural penalty is introduced to prevent unrealistic distortions while encouraging challenging augmentations during training. Extensive experiments show that the proposed approach achieves an AP$_{50}$ of 91.6%, improving the baseline by 0.9 percentage points and outperforming the previous best-performing method by 0.2 percentage points. For downstream missing seedling localization, it achieves 75.0% precision and a 67.0% F1-score, improving the baseline by 4.8 and 2.0 percentage points, respectively. These results demonstrate the effectiveness of the proposed framework for practical ground-based agricultural monitoring under complex outdoor lighting conditions without additional inference-time computational overhead.

---


### 150. [Identifying the Unknown: Prompt-Free Open Vocabulary Anomaly Recognition for Robot-Object Interaction](https://arxiv.org/abs/2606.26829)

**<font color=#1a73e8>作者：</font>** Philipp Allgeuer, Jan-Gerrit Habekost, Stefan Wermter  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots operating in real-world environments must in general be able to recognize previously unseen objects. As robotic systems move toward open-world autonomy, there is a growing, yet largely unmet, need for open vocabulary object detectors that are prompt-free and efficient enough for continuous deployment. We present AnomNOVIC, a two-stage known-workspace framework that combines a masked autoencoder (MAE) trained for anomaly detection, with NOVIC, a powerful real-time prompt-free open vocabulary image classifier. The MAE produces generic object-agnostic bounding boxes, allowing NOVIC to classify salient image regions without requiring a predefined candidate class list. We evaluate AnomNOVIC against strong open vocabulary baselines in a tabletop robot-object environment featuring the NICOL humanoid robot, reaching 47.1% AP / 57.5% AP50 for prompt-free recognition, and 59.0% AP / 72.5% AP50 if class candidates are provided. Across additional datasets, including an in-the-wild test set with 48 unique objects, AnomNOVIC reaches up to 82.6% prompt-free detection and classification accuracy. These results significantly surpass all tested open vocabulary baselines, including YOLO-World-v2, OWLv2, and YOLOE.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-245](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
