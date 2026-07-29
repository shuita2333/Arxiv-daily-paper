# 📦 其他研究 | 2026年07月30日

> 本类共 **229** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-229**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-229**

---

### 201. [A2TTA: Anchored-and-Agile Test-Time Adaptation for Evolving Traffic Sensor Networks](https://arxiv.org/abs/2607.25875)

**<font color=#1a73e8>作者：</font>** Du Yin, Xiachong Lin, Yue Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting is important for efficient traffic management and route planning in smart cities. Existing traffic forecasting studies typically assume fixed sensor graphs, overlooking the continuous evolution of real-world traffic networks, e.g., ongoing road network construction and evolving human mobility patterns. These dynamic changes can substantially degrade conventional forecasting models, motivating test-time adaptation (TTA) to efficiently adapt pretrained models during deployment. However, applying TTA to evolving traffic sensor networks remains challenging in two aspects. First, topology expansion introduces new sensors and connections, continuously reshaping the sensor graph. Second, tem- poral shifts vary in time scale and stability, requiring differentiated adaptation to long-term and short-term shifts. In this study, we address these challenges by proposing A2TTA, an Anchored-and-Agile Test-Time Adaptation framework for evolving traffic sensor networks, which transforms topology-induced forecasting errors into an expandable output calibration problem and separates tem- poral adaptation into persistent global correction and agile context-specific specialization. By jointly addressing topology evolution and multi-scale temporal shifts, A2TTA enables efficient and robust adaptation to continuously evolving traffic environments. Extensive experiments on ten real-world traffic networks demonstrate that A2TTA consistently improves forecasting performance across different backbones, datasets, and prediction horizons. Our code is available in this https URL.

---


### 202. [A Machine-Learning-Based Gas Lift Optimization Workflow for Unconventional Fields](https://arxiv.org/abs/2607.25885)

**<font color=#1a73e8>作者：</font>** Miao, Alexandra Vendetti, Logan Smart 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present an automated data-driven workflow using Machine Learning (ML) for gas lift optimization in unconventional fields. This workflow integrates a ML model that accurately forecasts the Gas Lift Performance Curve, and a Bayesian Optimization Framework to solve for the optimal gas injection rates under the constraints of facility capacity. The ML model leverages the historical production time series data without requiring downhole gauges or multi-rate well tests. We piloted this workflow on 30 wells across 5 well pads in Bakken and obtained >5% production uplift on average. With the success of the pilot, we have now fully-deployed this workflow in Bakken across 200+ gas lift and plunger-assisted gas lift (PAGL) wells. Moreover, the ML-based gas lift optimization workflow presented in this paper is an effective and economic solution for other assets where downhole data or multi-rate testing are not available/feasible due to cost or facility constraints.

---


### 203. [Distributing Security Controls Through Harness Engineering](https://arxiv.org/abs/2607.25890)

**<font color=#1a73e8>作者：</font>** William Robert Gore  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations. Existing security controls for coding agents are not systematically distributed to engineering teams, and vendor-native solutions introduce ecosystem dependencies that may not suit every deployment context. This paper investigates whether off-the-shelf security controls can be implemented on commercial AI coding agents and scaled to a distributed user base via a custom agent harness. A phased testing methodology was applied across four agent configurations --- two commercial agents with and without controls, a baseline harness, and a security-hardened harness --- using a 23-test suite derived from the OWASP Top 10 for Agentic Applications. SHarD (Secure Harness Distribution), a distributable harness built on the Pi agent harness, demonstrated that three categories of security controls --- OS sandboxing, skill scanning, and tool restriction --- can be embedded and distributed via a single install command while retaining equivalent efficacy to direct installation on commercial agents. SHarD achieved an adjusted score of 100\%, matching the best securely configured commercial agent, with no regression across any test category. Notable observations include evidence that model non-determinism produces inconsistent security outcomes and that autonomous agent behavior can cross system boundaries in ways that OS sandboxing directly mitigates. Initial characteristics toward a control harness fitness framework are proposed, and a third research question is identified for future investigation.

---


### 204. [Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation](https://arxiv.org/abs/2607.25891)

**<font color=#1a73e8>作者：</font>** Stefan Krsteski, Charlotte Meyer, Guillaume Allegre 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating AI agents in interactive environments is hindered by fragmented tasks, scaffolds, verifiers, and scoring rules. Existing efforts focus on narrow settings, remain limited in scale, or require costly reruns, leaving much of the empirical record incomparable. We introduce Messier, a unified corpus of 957,253 records that span 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers. Messier consolidates public benchmark scores and supplements them with five-agent runs across six underrepresented professional and scientific domains, including a recent legal benchmark. Each record is standardized by model, scaffold, environment, task, verifier, and aggregation rule, with SOC/NAICS classifications for occupational and industry analysis. Using this corpus, we show frontier progress is uneven across benchmark types, with "function calling" saturated, "programming" improving the fastest, and "enterprise workflows" remaining the most challenging. Furthermore, counterfactual rescoring shows that strict all-pass aggregation in multi-verifier tasks can obscure progress and artificially alter agent rankings. From these standardized records, we derive capability scales that align with Epoch's Evaluation Capability Index rankings at Spearman \r{ho} = 0.81 and can be specialized by domain, occupation, action space, or verifier type. Messier provides a foundational, reusable infrastructure for agent capability scaling, benchmark auditing, and fine-grained analysis of evaluation failures.

---


### 205. [TIGA: Trajectory-Injected Generative Attack against Black-box AIGC Detectors](https://arxiv.org/abs/2607.25894)

**<font color=#1a73e8>作者：</font>** Xia Du, Zhuosen Bao, Zheng Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion models have achieved remarkable realism in facial image synthesis, posing growing challenges to artificial intelligence-generated content (AIGC) forensic this http URL evasion methods typically perturb pre-generated images or require detector-aware training, which may introduce visible or statistical artifacts and limit applicability when the diffusion model must remain frozen and the target detector is accessible only through black-box queries. We propose Trajectory-Injected Generative Attack (TIGA), a source-image-free and training free framework that generates detector-evasive images within a single diffusion sampling trajectory. TIGA steers the latent Denoising Diffusion Implicit Model (DDIM) trajectory so that adversarial properties emerge during generation rather than being added afterward. TIGA first aggregates gradients from multiple white-box surrogate detectors to form a transferable, sign-aware prior, and then performs anisotropic directional search with symmetric finite-difference queries to estimate the black-box target response. The estimated directions are stabilized by decayed momentum and injected according to the DDIM noise schedule, with frequency-domain reshaping to suppress high frequency artifacts. Experiments on surrogate and unseen specialized forensic detectors show that TIGA achieves strong blackbox attack performance, transferability, and high robustness under common post-processing operations without source images or diffusion-model retraining, while preserving high perceptual quality.

---


### 206. [Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification](https://arxiv.org/abs/2607.25904)

**<font color=#1a73e8>作者：</font>** Chenrui Shi, Yuwei Wu, Yang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical user interface task evaluation aims to determine whether a GUI agent has successfully completed a user instruction. Automated GUI task evaluation has received increasing attention because the evaluation results can serve as reward signals for both test-time scaling and post-training. However, reliable GUI task evaluation remains challenging because the judgments often require access to environment states, such as system configurations, file data, and application settings, beyond the screenshots of execution trajectories. In this paper, we propose an interactive reward agent (IRA) based on a propose-then-verify framework to acquire and verify evidence from the post-execution environment. Given a task instruction and a GUI environment after the GUI agent execution, IRA first proposes the task completion conditions and then verifies them by invoking system tools, application tools, and GUI tools. This design combines evidence from both visible interfaces and the environment state in an interactive process. We further introduce GUI-RewardBench, a benchmark of 321 GUI task trajectories spanning 10 Ubuntu desktop application categories. Experiments show that IRA achieves 86.9% accuracy on GUI-RewardBench, outperforming existing evaluator baselines. We further apply IRA to reinforcement learning of GUI agents, achieving a 34.0% OSWorld success rate, which demonstrates that IRA can provide effective reward signals for training GUI agents.

---


### 207. [AnnoBench: A Benchmark for Visualization Annotation Generation](https://arxiv.org/abs/2607.25911)

**<font color=#1a73e8>作者：</font>** Md Rahat-uz-Zaman, Md Dilshadur Rahman, Andrew McNutt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Annotation is among the most demanding visualization tasks to automate, as it simultaneously requires correctly navigating visual, semantic, and stylistic constraints. Failure to meet any of these conditions severely undermines the utility of an annotation, rendering it challenging to read, inaccurate, or visually discordant. Despite a growing body of annotation tools and automations, no existing benchmark or evaluation framework tests whether these conditions are met because of their scope and annotation not being the focus of their studies. We introduce AnnoBench, a benchmark for visualization annotation that materializes the inherent challenges of this domain in a structured and testable manner. AnnoBench pairs visualizations from professional data journalism and visualization galleries with annotation tasks, spanning four representation formats, five chart description conditions, and two prompt specification levels. The benchmark is executed via VLM-as-a-judge, using models aligned with manual human assessment. We evaluate the benchmark via four one-factor-at-a-time experiments, exploring the effects of input representation, semantic context, and prompt specificity, and model selection on annotation quality. This work provides a foundation for advancing annotation automation, tooling, and visualization-generation pipelines.

---


### 208. [Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks](https://arxiv.org/abs/2607.25914)

**<font color=#1a73e8>作者：</font>** Ravi Kant Sharma, Ashutosh Uttam, Ajay Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust visibility. When a tool from Vendor B is compromised, agents from Vendor A continue invoking it -- unaware of the trust degradation -- causing cascading service impact. We present AgentToolMO, a proposed 3GPP NRM information model for agent tool trust management. The model comprises: a formally defined trust state machine with provable graduated enforcement, damped cascade propagation with bounded convergence, cross-vendor trust notifications via existing Management Services (MnS) interfaces, and retroactive impact assessment through NRM dependency graph traversal. Simulation-based evaluation across multi-vendor topologies shows that standardized cross-vendor notifications reduce blast radius from hours-scale undetected propagation to near-real-time containment bounded by MnS notification delivery, with cascade convergence guaranteed in bounded iterations and sub-linear notification scaling across vendor domains. The framework operates within existing 3GPP management infrastructure, leverages existing protocols, and provides a standardization pathway for trustworthy multi-vendor autonomous network management.

---


### 209. [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](https://arxiv.org/abs/2607.25915)

**<font color=#1a73e8>作者：</font>** Yutong Chen, Shouqian Shi, Xinran Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex structured reasoning tasks often require additional computation, yet current language models obtain it mainly by increasing parameter scale or by serializing intermediate steps as chain-of-thought (CoT) tokens. The former raises training and deployment costs, while the latter ties reasoning computation to autoregressive output length. We introduce Penelope, an efficient latent-reasoning framework for pretrained decoder-only Transformers that localizes recurrent computation to a selected decoder interval. The lower decoder prefix is evaluated once to construct a problem-conditioned boundary memory, which is then iteratively refined through time-modulated GRU dynamics and recurrent readout states before answer generation. A progressive CoT-to-latent curriculum transfers visible reasoning into this internal recurrent path, allowing additional computation to be allocated in latent space without repeatedly executing the complete decoder or generating a long intermediate trace. Experiments on open-source structured-reasoning benchmarks show that, at validation-selected latent budgets, Penelope attains competitive accuracy relative to established latent-reasoning models while reducing measured inference latency. These results show that latent refinement can be localized to a narrow decoder interval, reducing repeated full-decoder execution without generating a long visible reasoning trace and providing a practical accuracy-efficiency tradeoff for decoder-only Transformer models.

---


### 210. [Faster, Higher, Stronger? The Impact of GenAI on Knowledge Work Productivity - Evidence from the Field](https://arxiv.org/abs/2607.25922)

**<font color=#1a73e8>作者：</font>** Sven Bottesch, Chiara Schwenke, Jakob Zimmermann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rise of generative artificial intelligence (GenAI) has fueled high expectations regarding its potential to enhance knowledge work productivity in terms of efficiency and quality. Building on task-technology fit (TTF) theory, we empirically examine the extent of GenAI's productivity effect for different task types. We conducted a randomized lab-in-the-field experiment with 128 knowledge workers from a multinational industrial organization. Participants completed three representative knowledge work tasks (knowledge acquisition, packaging, and creation), either with or without GenAI. Results show that GenAI consistently increases efficiency across tasks. However, its impact on quality is task-contingent: quality increases for knowledge packaging and creation but declines for knowledge acquisition. Furthermore, GenAI tends to reduce quality variance for knowledge packaging and creation, primarily benefiting lower-performing knowledge workers. However, it increases quality variance for knowledge acquisition. These findings contribute to a more granular, differentiated understanding of GenAI's productivity impact and hold implications for research and practice alike.

---


### 211. [dtControl2+$\varepsilon$: Trading Optimality for Explainability in MDPs via Decision Trees](https://arxiv.org/abs/2607.25925)

**<font color=#1a73e8>作者：</font>** Tereza Kinská, Jan Křetínský, Tobias Meggendorfer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Over the past decade, decision trees have been used to represent controllers (a.k.a. policies) in an explainable way, with dtControl2 as a current state-of-the-art tool. However, for systems that are large or have many corner cases, even such representations tend to be too complex and not human-comprehensible. Unfortunately, reducing the size of the decision tree is not straightforward, as missing just a single crucial case might result in an incorrect controller. We tackle this issue in the setting of Markov decision processes, extending dtControl2 by "$\varepsilon$" functionality: Given an allowed imprecision $\varepsilon \geq 0$, we construct a smaller decision tree, distilling the essence of the controller, while still guaranteeing its $\varepsilon$-optimality. This enables us to provide tunably simpler explanations, omitting a controllable amount of detail. Our tool constructs decision trees that are orders of magnitude smaller than the state of the art.

---


### 212. [Face De-Identification: A Domain-Centric Survey from Capture to Processing](https://arxiv.org/abs/2607.25926)

**<font color=#1a73e8>作者：</font>** Hui Wei, Hao Yu, Guoying Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face de-identification (De-ID) aims to remove or conceal personally identifiable facial features in images or videos to prevent identity recognition while preserving utility for downstream tasks. With the rising emphasis on data privacy and responsible AI, face De-ID has emerged as an active research area spanning computer vision and privacy-preserving communities. Early approaches, and many contemporary ones, operate in the digital domain by modifying pixel-level or appearance-level features through post-capture processing. Recent advances extend face De-ID beyond post-processing by integrating privacy mechanisms directly into sensors during image acquisition, bridging sensing systems and downstream vision algorithms. In parallel, physical-domain methods explore wearable accessories and materials that conceal identity information in real-world environments prior to capture. In this survey, we present the first unified overview that spans the full data acquisition pipeline, encompassing the physical, sensor, and digital domains. Through this domain-centric lens, we systematically analyze current methodologies, technical progress, and the distinct challenges inherent to each stage. We then review and organize existing evaluation protocols, examining current practices and highlighting the critical need for standardized, comprehensive benchmarks. Finally, we identify key open problems and outline emerging research directions to guide future work in this rapidly evolving field. To support ongoing research, we maintain a project page that organizes relevant literature with collected datasets and open source code: this https URL.

---


### 213. [MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities](https://arxiv.org/abs/2607.25948)

**<font color=#1a73e8>作者：</font>** Mingqiao Ye, Zhaochong An, Zhitong Gao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Any-to-any models predict any modality from any combination of others within a single network, a formulation used in multimodal vision and vision-language models, and increasingly in scientific domains such as ecology and astronomy. Existing any-to-any models are typically trained from scratch using encoder-decoder or diffusion architectures, impacting their performance and preventing them from using strong pre-trained decoder-only models as a prior. In this work, we investigate decoder-only any-to-any multimodal modeling, which treats all modalities symmetrically and supports arbitrary modalities as inputs and outputs without modality-specific heads, losses, or task pipelines. Because every modality is both an input and an output of the same model, the resulting model, named Modus, can support a range of applications, such as chained generation through intermediate modalities or cross-modal self-verification by scoring the model's own outputs with another generated modality. Modus demonstrates strong out-of-the-box performance and is competitive with specialist and multitask baselines using a single model across various benchmarks. All materials are open-sourced at this https URL.

---


### 214. [Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs](https://arxiv.org/abs/2607.25959)

**<font color=#1a73e8>作者：</font>** Fanfu Wei, Thibault Ehrhart, Raphaël Troncy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raises a practical question: when these modalities disagree, how can we detect and explain the conflict? We study this problem as \emph{modality-level inconsistency detection}. We first introduce a taxonomy of cross-modal knowledge inconsistencies, covering information granularity differences, direct conflicts, temporal changes, and KG incompleteness. We then present \textsc{Kontrast}, an automatic framework that uses Text-to-SPARQL and LLM reasoning to compare table-based answers with KG evidence and categorize the resulting inconsistencies. Experiments on various Table-QA datasets show that cross-modal inconsistencies are common and informative. They reveal not only true knowledge conflicts, but also missing KG structure and temporal mismatches while being limited by Text-to-SPARQL errors and noise. Our analysis shows that text, tables, and KGs can complement and correct one another through systematic comparison. \textsc{Kontrast} provides a practical tool for large-scale knowledge auditing and establishes a benchmark for future work on cross-modal knowledge consistency. Code and data are available at this https URL.

---


### 215. [Quasi-SVD: Learning a Lie-constrained matrix factorisation for real-time imaging](https://arxiv.org/abs/2607.25967)

**<font color=#1a73e8>作者：</font>** Christopher Hahne  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Singular Value Decomposition (SVD) underlies matrix factorisation tasks across computational imaging, with medical applications increasingly demanding real-time processing. Yet SVD algorithms are inherently sequential, constraining real-time GPU throughput and limit online deployment in clinical pipelines. This study introduces Quasi-SVD, a differentiable, fully parallelized matrix factorization framework for GPUs. Rather than enforcing orthogonality on both factors, it guarantees exact orthogonality for a single Lie-parameterized factor while recovering the remaining components through soft constraints, enabling efficient parallel decomposition without iterative singular-vector optimization. This asymmetric design, provably sufficient for valid factorisation, achieves reconstruction fidelity of SSIM = 0.89-0.94 and accelerates computation by 3-20x relative to cuSOLVER and randomised SVD, enabling throughput above 25 FPS. Performance is evaluated on two medical imaging tasks spanning complementary computational regimes: (1) spatio-temporal background subtraction for ultrasound localisation microscopy, requiring high-dimensional matrix separation, and (2) Mueller matrix polarimetry for neurosurgical tissue characterisation, requiring massive batch processing of small matrices. Across both regimes and multiple imaging instruments, the proposed framework demonstrates robust domain transfer and throughput exceeding 25 FPS at clinical matrix scales, a rate sufficient for live image-guided workflows that classical solvers cannot currently support in these settings. By prioritising downstream reconstruction fidelity over exact spectral recovery, Quasi-SVD makes structured matrix factorisation practical for real-time imaging.

---


### 216. [E-MagDiP: Electro-Magnetic based Differential Privacy for EEG based Community Sensing](https://arxiv.org/abs/2607.25968)

**<font color=#1a73e8>作者：</font>** Ayanga Imesha Kumari Kalupahana, Vishruti Ranjan, Li-Shiuan Peh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> EEG-based community sensing programs are emerging globally as a tool to leverage aggregated brain data to gain insights into attentiveness of students and employees. But these programs raise privacy concerns because EEG signals contain sensitive personal information. Differential Privacy (DP) can protect individuals while preserving aggregate statistics yet applying DP to EEG data is challenging as it requires user-level noise generation, which increases power and latency. Besides, most commercial EEG headsets cannot be modified to add such noise. We propose E-MagDiP, a framework that uses an external radio to transmit RF signals onto EEG headsets, perturbing signals at acquisition to induce DP noise. To the best of our knowledge, E-MagDiP is the first framework to use RF signals for privacy instead of attacks, enabling practical DP for EEG community sensing without any user-level modification.

---


### 217. [Reinforcement Learning for Code Optimization](https://arxiv.org/abs/2607.25970)

**<font color=#1a73e8>作者：</font>** Pierre Chambon, Kunhao Zheng, Juliette Decugis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL for code correctness is now established: have the model generate a program, run it against hidden test cases, and reward solutions that pass. Extending this to code optimization seems straightforward: just add execution time to the reward. But in practice, once timing drives the reward, small problems in measurement noise, reward sparsity, or GRPO instability overwhelm the signal and make RL fail: generated solutions are barely faster, and more of them can fail. We make execution time learnable through three stages: (1) how code is tested, by building DMC-Optim with large optimization tests and a calibrated sandbox; (2) how speed is turned into reward, by composing correctness and speed in the RL environment and using an offline simulator to predict the most promising configurations; and (3) how the model learns from that reward, by adapting GRPO and evaluation to the sparser, noisier timed-execution setting. On DMC-Optim, the strongest optimization-aware configurations improve strict top-50% pass@1 from 18.0% to 31.3% on Qwen 2.5 7B and from 30.7% to 50.4% on CWM 32B. These gains further increase at stricter percentiles such as top-30%, with 125% relative improvement for CWM 32B, while preserving pure-correctness scores. When the timing sandbox is degraded, robust optimization RL reaches 100% to 200% improvement over standard RLVR, depending on the evaluation criterion. On LCB, CWM 32B wins up to 83% of median-sample speed comparisons against standard RLVR. Relative to the fastest correct human submissions per problem, it reaches about half the human rate of complexity-class improvements (14% vs. 28%).

---


### 218. [Who is scientific code for? Maintaining human-readable landmarks in agent-written code](https://arxiv.org/abs/2607.25975)

**<font color=#1a73e8>作者：</font>** Elle O'Brien  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scientific research involving code has long rested on the assumption that at least one person understands why the code exists. As scientists adopt coding agents, this assumption is breaking down. Drawing on an ongoing contextual inquiry of scientific programmers working with agentic tools (four cases to date), a survey of over 800 scientific programmers, and my own analysis workflows, this position piece describes how scientists are inventing personal conventions, "landmarking strategies", for marking which artifacts in a codebase are meant for human understanding and which are context for agents. They repurpose shared infrastructure (version control especially) in idiosyncratic ways, and I argue that this quiet de-standardization could complicate collaboration in teams with heterogeneous software practices. Alternatively, teams that explicitly delineate what is human-readable versus agent context will be better able to develop, document, and maintain scientific code.

---


### 219. [Schrödinger's Cat: Probabilistic Representation and Prediction of Potential Scene Kinematics](https://arxiv.org/abs/2607.25984)

**<font color=#1a73e8>作者：</font>** Timy Phan, Jannik Wiese, Björn Ommer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting how a scene may evolve from partial observations requires reasoning about multiple possible futures rather than committing to a single trajectory. Existing approaches either generate appearance-dominated video predictions or sample a small number of trajectories without explicitly modeling the distribution of possible motion. We introduce Goal-Aware Representations of Future kInEmatic Latent Distributions (GARFIELD), a probabilistic model of scene kinematics that learns a structured spatio-temporal latent representation of the distribution over possible futures given an image and optional spatio-temporally sparse constraints. The same latent representation enables both joint sampling of all trajectories and direct access to the underlying motion distribution through an efficient deterministic density decoder. As a result, uncertainty about future motion can be localized to specific scene elements and timesteps and progressively refined through additional constraints. Experiments demonstrate strong motion planning performance competitive with large video generation models while sampling trajectories $97\times$ faster. Our method further estimates motion densities two orders of magnitude faster than Monte-Carlo sampling from motion generation models, enabling interactive exploration and uncertainty-aware planning.

---


### 220. [Generator-Aligned Representation Interfaces for Diagnostic Soft Equivariance](https://arxiv.org/abs/2607.25988)

**<font color=#1a73e8>作者：</font>** Weitao Li, Gong Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exact-equivariant architectures typically encode prescribed group actions in specialized operators, which can complicate their reuse with generic backbones and across data modalities. We introduce the Generator-Aligned Representation Interface (GARI), a representation-level design principle that exposes selected transformation generators to a generic sequence backbone through aligned canonical and generator-induced views. We formalize the resulting behavior using a probe-specific soft-equivariance residual defined over declared data and transformation distributions. This framework distinguishes representation consistency from task robustness and exact equivariance, and localizes residual mismatch to interface construction, shared stream processing, and terminal fusion. We instantiate the interface as GARI-Net, which constructs generator-indexed streams, converts them into a common interaction frame, processes them with shared parameters, repairs ordering-induced context mismatch, enables cross-stream information exchange, and aggregates them using inter-stream discrepancy. Direct Equivariance Error (DEE) provides a frozen-checkpoint diagnostic of the prescribed representation relation under known token or voxel actions. Experiments on genomic sequences, images, and three-dimensional point clouds examine sequence reversal, planar rotations and reflections, and controlled axial transfer. Across these settings, the same interface principle supports task-relevant transformation consistency and generalization to declared held-out probes without requiring group-specific redesign of the sequence backbone. GARI therefore provides a portable diagnostic complement to hard-equivariant architectures: it makes generator structure accessible, learnable, and measurable, while finite-probe evidence remains distinct from certification of exact equivariance over a continuous group.

---


### 221. [On the Use of Synthetic Data for Threshold Calibration in Face Recognition: Performance and Security Implications for Border Control Systems](https://arxiv.org/abs/2607.25990)

**<font color=#1a73e8>作者：</font>** Arto Apila  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recently deployed Entry/Exit System (EES) introduces large-scale biometric verification into European border control, requiring face recognition systems to operate at extremely low false match rates (FMR). While regulatory frameworks define performance targets at the EES Central System level, they do not specify how verification thresholds should be calibrated in practice at the Member State level. In operational settings, obtaining representative real-world data for calibration is often constrained by legal, logistical, and privacy limitations.
In this work, we investigate the use of synthetic face data for threshold calibration in document-to-live verification scenarios relevant to border control systems. We analyze the alignment of genuine and impostor score distributions between synthetic and real datasets and evaluate the transferability of calibrated thresholds across domains, with a focus on low-FMR operating points.
Our results show that synthetic data can approximate calibration behavior in controlled settings, but fails to reliably generalize to unconstrained conditions due to mismatches in score distribution tails. These discrepancies lead to significant degradation in recognition performance and increased vulnerability to morph-based attacks. We further demonstrate that calibration outcomes are highly dataset-dependent, even across synthetic datasets.
Overall, our findings highlight that while synthetic data is useful for system development and preliminary calibration, our results indicate that reliable threshold selection in high-security deployments typically requires validation and adjustment using representative real-world data.

---


### 222. [Sharpness-Aware Minimization and Muon: Robustness under the Spectral Norm](https://arxiv.org/abs/2607.26001)

**<font color=#1a73e8>作者：</font>** Wenzhi Zhong, Edward Milsom, Michael Murray  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sharpness-Aware Minimization (SAM) aims to improve generalization by encouraging insensitivity to small, worst-case parameter perturbations. However, the notion of a "small" perturbation is inherently geometry-dependent: while existing SAM variants have explored a wide range of choices, a clear perspective on which geometries are most effective in practice remains elusive. Recent work on matrix-aware optimization, particularly the Muon optimizer, suggests that respecting the matrix structure of hidden-layer weights can lead to strong empirical performance. Motivated by this, we study matrix-aware geometry in both stages of SAM: we introduce a layerwise spectral inner perturbation for matrix-valued hidden-layer parameters and combine it with either AdamW/SGDW or Muon in the outer update. Across ImageNet-1K experiments on ViT-Small/16 and ResNet-50, we find that the combination of a spectral inner step with a Muon outer step performs consistently strongly, achieving the best validation accuracy on both models among the evaluated methods.

---


### 223. [Parallel Decoding Distillation for Fast Image and Video Generation](https://arxiv.org/abs/2607.26004)

**<font color=#1a73e8>作者：</font>** Neta Shaul, Chao Liu, Arash Vahdat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process. Current state-of-the-art (SOTA) acceleration methods heavily rely on variational score distillation (VSD) and adversarial losses to distill diffusion models into few-step generators. Albeit achieving high-quality video generation, these training losses are notoriously hard to optimize and suffer from mode collapse, leading to loss of video diversity and lack of motion. In this paper, we introduce Parallel Decoding Distillation (PDD), a simplified and scalable trajectory-based distillation method for fast inference of diffusion and flow matching models. Our architecture and training procedure are compatible with any pre-trained model and support sampling with a varying number of function evaluations (NFE). PDD accelerates generation by predicting multiple denoising steps per network evaluation. Conceptually, it learns a representation of the mean velocity without regressing its derivative using JVPs or finite-difference approximations. Our method achieves SOTA performance with 4-8 NFE on LTX-2.3 Text-to-Video/Audio, Wan 14B Text-to-Video, and Qwen-Image Text-to-Image. Moreover, PDD presents a significant improvement in generated video diversity.

---


### 224. [Pictura: Perspective-View Self-Play at Scale for Driving](https://arxiv.org/abs/2607.26005)

**<font color=#1a73e8>作者：</font>** Yuan Yin, Elias Ramzi, Marc Lafon 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-play in simulation produces robust driving policies at scale. Demonstrations of such behavior have been made using privileged vectorized observations such as exact poses and velocities, even for occluded agents. This assumes that perception is solved and introduces a representation gap with the partial observation of a deployed agent driving from the perspective view of egocentric cameras. A common fix, distilling the privileged policy into a camera-input student, leaves the student imitating decisions its own view cannot justify. Instead, we establish perspective-view self-play as a practical training regime. We introduce Pictura, a GPU-accelerated multi-agent driving simulator that renders each agent's egocentric view at every step, mitigating the representation gap at its source. Pictura sustains up to 500K agent-steps/s (2M images/s) on a single H100. Using Pictura, we train Alberti by self-play with plain PPO. It is the first large-scale driving self-play policy trained directly from perspective images, without privileged observations. Training spans 50B agent steps for ~35M km of driving. It approaches the driving performance of its privileged vectorized counterpart, and transfers zero-shot to Waymo Open Motion Dataset layouts re-rendered in Pictura, where it outperforms privileged vectorized agents. Project page: this https URL

---


### 225. [UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams](https://arxiv.org/abs/2607.26017)

**<font color=#1a73e8>作者：</font>** Siyu Xia, Chenheng Zhang, Yanting Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory is essential for LLM agents to accumulate task experience and reuse task-specific execution strategies. However, real-world deployment over boundary-agnostic and evolving task streams exposes a fundamental stability-plasticity dilemma. External retrieval-based memory can rapidly absorb new evidence, but it often fails to internalize recurring execution patterns and incurs inference-time retrieval overhead. Parametric memory enables stable and efficient execution once learned, but typically relies on explicit task boundaries and fixed parameter budgets. Inspired by the human brain, which balances plasticity and stability through complementary episodic storage and gradual consolidation, we propose UniMem, a self-routing framework for autonomous memory management. UniMem uses learnable routing tokens as memory controllers, enabling adaptive coordination between complementary memory pathways: novel or sparse tasks are retained in an episodic buffer for retrieval-augmented execution, while recurring and reliable patterns are consolidated into expandable parametric memory. By decoupling task identification from task execution with routing tokens and parametric memory blocks, UniMem expands memory on demand without task labels during deployment or uncontrolled parameter growth. Experiments on long-horizon streaming task sequences show that UniMem consistently outperforms baselines while maintaining execution fidelity, achieving an average gain of 4.0 EM points across three backbone models.

---


### 226. [Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment](https://arxiv.org/abs/2607.26034)

**<font color=#1a73e8>作者：</font>** Elias Fernández Domingos, Anh Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Technological races create tension between speed and safety: actors may gain by moving faster than competitors, even when risky development is harmful. This is prominent in debates about artificial intelligence (AI), where competitive pressure is often argued to incentivise riskier, less safety-conscious development. We study this using a framed behavioural experiment based on an idealised AI race, in which paired participants repeatedly chose between Safe and Unsafe development under an uncertain time horizon. Unsafe development gave faster progress and higher immediate payoffs but accumulated private risk up to a treatment-specific maximum of 10\%, 60\%, or 90\%; the race's competitive structure was held constant, and only this maximum risk varied. Neither the pre-registered comparison between risk levels nor the role of elicited risk preferences was supported by the data. Instead, exploratory analyses motivated by the task's repeated structure show that Unsafe behaviour is shaped less by risk preferences than by the evolving strategic state of the race: participants are more likely to choose Unsafe after their opponent does so, being ahead reduces Unsafe play while falling behind increases it, and first-round choices predict later behaviour. To interpret these effects we introduce a reduced evolutionary model with four strategies -- Always Safe, Always Unsafe, Conditionally Safe, and Conditionally Antisocial Safe -- which reproduces the treatment effect and shows how conditional Unsafe behaviour can be favoured by competitive race dynamics. Together, the experiment and model show that unsafe development can emerge from early behavioural momentum, opponent behaviour, and fear of falling behind, rather than from risk preferences alone, suggesting policy should focus on reducing competitive pressure and promoting cooperation in AI development rather than only individual risk.

---


### 227. [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](https://arxiv.org/abs/2607.26041)

**<font color=#1a73e8>作者：</font>** Abhishek Pillai, Samir Kumar Nayak, Yuan Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates whether a model can reconstruct the causal, task-relevant transition produced by an action- crucial for rejecting stale observations, verifying progress, and recovering from failure. This is difficult because inference, remote input, app rendering, and screenshot capture are asynchronous: the next observation may be delayed, occluded, transient, or unrelated, then misread as progress and carried into subsequent planning. We introduce Desktop-Delta Bench (DDB), an offline step-level benchmark with 2,013 human-verified instances from novel, multi-app Linux trajectories across ~15 applications and 50 task domains. DDB trajectories targets 3 failure dimensions- state verification, source tracking, and context-aware control- through 2 complementary tasks: 463 3-frame temporal-ordering instances, including 105 with a cross-trajectory decoy, and 1,550 before-after pairs labeled from 5 actions + its payload. We evaluate 8 closed and open-source model families across 32 ordering and 16 single-action settings, observing consistent gaps. Ordering remains unsaturated: best non-decoy and decoy exact-match rates are 65.1% and 65.7%. Task context improves decoy identification by 6.9 percentage points but reduces non-decoy exact match by 2.2 points; error analysis reveals systematic copying of the presented A-B-C order. Single-action results show that inferring the action family is harder than locating it: click F1 is 0.96 vs, 0.76 for drag, while recognized drags are generally localized well. DDB, thus, complements end-to-end benchmarks by filling the missing diagnostic layer between GUI grounding and final task success, enabling targeted improvements to desktop CUA verification, reliability, and recovery.

---


### 228. [Re-thinking Mammography Transfer Learning: The Dataset-Informed Transfer Learning (DITL) Framework for Breast Cancer Screening and Lesion Diagnosis](https://arxiv.org/abs/2607.26043)

**<font color=#1a73e8>作者：</font>** Adarsh Bhandary Panambur, Siming Bayer, Andreas Maier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enhancing classification performance in mammography remains a persistent challenge across both small curated datasets and large-scale clinical cohorts. Conventional transfer learning approaches often neglect dataset-specific characteristics, while recent neighborhood-informed methods have been restricted to narrow tasks with rigid formulations, limiting their scalability to population-level datasets. To address these challenges, we propose the Dataset-Informed Transfer Learning (DITL) framework, which integrates dataset-derived difficulty signals with neighborhood-based triplet supervision in a unified objective. DITL introduces two adaptive components: (i) Adaptive Difficulty-Weighted Cross-Entropy (A-DWCE), which assigns per-sample weights based on k-nearest neighbor label purity in a self-supervised feature space, and (ii) Adaptive Neighborhood Representation Triplet (A-NR-Triplet), which enforces intra-class compactness and inter-class separation using a learnable margin. Unlike focal loss, DITL requires no hyperparameter tuning, removes heuristic weighting and fixed margins, and incurs negligible computational overhead, yielding a robust and scalable optimization strategy. On the large-scale VinDR-Mammo dataset, DITL achieves state-of-the-art performance for whole-image breast density classification, with significant improvements across accuracy, F1-score, and AUC (p < 0.0001). Beyond large cohorts, DITL also delivers consistent, statistically significant gains on small ROI datasets (p < 0.0001). By bridging small-scale lesion analysis with large-scale density estimation, DITL establishes a clinically relevant, scalable, and generalizable framework for mammography classification, spanning the full breast cancer screening-to-diagnosis spectrum.

---


### 229. [Pass the Baton: Trajectory-Relayed On-Policy Distillation](https://arxiv.org/abs/2607.26057)

**<font color=#1a73e8>作者：</font>** Haolei Xu, Xiaowen Xu, Haiwen Hong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) grounds token-level supervision in the student's own trajectory, yet suffers from prefix failure: once the student commits to a wrong reasoning direction, all subsequent generation builds on this deviation, producing misdirected continuations that elicit unreliable supervision and waste compute. We identify a teacher-student continuation asymmetry on failed prefixes, where the teacher tends to redirect while the student continues along the original direction, and convert it into a label-free handoff trigger in Relay On-Policy Distillation (Relay-OPD). During training, Relay-OPD constructs relay trajectories by letting the teacher briefly take over at detected trigger points to produce a teacher leg, after which the student resumes and is optimized on the resulting trajectory. A limited relay budget concentrates intervention on critical early positions while limiting departure from the student policy. With a Qwen3-4B-Instruct-2507 teacher and Qwen3-0.6B/1.7B-Non-Thinking students on eight mathematical reasoning benchmarks, Relay-OPD achieves the best or second-best results on every benchmark, outperforming standard OPD by +5.73% and the strongest baseline FastOPD by +1.49% on average for 1.7B, with consistent gains at 0.6B. Training trajectory length is reduced by over 50%.

---


> [!TIP]
> 当前位于：**201-229**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-229**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
