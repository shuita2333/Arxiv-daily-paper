# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**601-650**（第 13/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-651](./part-14.md)

---

### 601. [PRIMA: Boosting Animal Mesh Recovery with Biological Priors and Test-Time Adaptation](https://arxiv.org/abs/2606.02366)

**<font color=#1a73e8>作者：</font>** Xiaohang Yu, Ti Wang, Mackenzie Weygandt Mathis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PRIMA (*PRI*ors for *M*esh *A*daptation), a framework for robust 3D quadruped mesh recovery under severe species and pose imbalance. Existing animal reconstruction methods often regress toward mean shapes and poses due to limited 3D supervision and long-tailed species distributions, resulting in poor generalization to underrepresented animals and rare articulations. PRIMA addresses this challenge through three key contributions. First, we incorporate BioCLIP embeddings as biological priors to inject semantic and morphological knowledge into the reconstruction process, enabling more accurate and generalizable shape prediction across diverse quadrupeds. Second, we introduce a test-time adaptation (TTA) strategy that refines SMAL predictions using 2D reprojection constraints together with auxiliary keypoint guidance, improving pose and shape estimation while enabling the generation of high-quality pseudo-3D annotations from existing 2D datasets. Third, leveraging this TTA framework, we construct Quadruped3D, a large-scale pseudo-3D dataset that covers diverse species and pose variations to systematically improve model performance. Extensive experiments on Animal3D, CtrlAni3D, Quadruped2D, and Animal Kingdom demonstrate that PRIMA achieves state-of-the-art results, with particularly strong improvements on underrepresented species and challenging poses. Our results highlight the importance of biological priors and adaptation-driven data expansion for scalable and generalizable animal mesh recovery. Code is available at this https URL.

---


### 602. [Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses](https://arxiv.org/abs/2606.02373)

**<font color=#1a73e8>作者：</font>** Pengcheng Jiang, Zhiyi Shi, Kelly Hong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search agents are often trained as policies over growing transcripts: the model must decide how to search while also remembering what it has seen, which evidence is useful, which constraints remain open, and which claims have actually been checked. We argue that this formulation puts too much routine state management inside the policy: reinforcement learning is forced to optimize both semantic search decisions and recoverable bookkeeping that the environment can maintain more reliably. We introduce Harness-1, a 20B search agent (retrieval subagent) trained with reinforcement learning inside a stateful search harness. The harness maintains environment-side working memory, including a candidate pool, an importance-tagged curated set, compact evidence links, verification records, compressed and deduplicated observations, and budget-aware context rendering. The policy retains the semantic decisions: what to search, which documents to keep or discard, what to verify, and when to stop. Across eight retrieval benchmarks spanning web, finance, patents, and multi-hop QA, Harness-1 achieves 0.730 average curated recall, outperforming the next strongest open search subagent by +11.4 points and remaining competitive with much larger frontier-model searchers. Its gains are especially strong on held-out transfer benchmarks, suggesting that reinforcement learning over explicit search state can produce retrieval behaviors that generalize beyond the training domains. Our code is available at this https URL.

---


### 603. [WAXAL-NET: Finetuned Edge ASR Across 19 African Languages](https://arxiv.org/abs/2606.02375)

**<font color=#1a73e8>作者：</font>** Victor Tolulope Olufemi, Oreoluwa Babatunde, Ramsey Njema 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We evaluate whether compact domain-specialized ASR models can outperform massively multilingual foundation models for conversational African speech across 19 languages in the WAXAL corpus. Fine-tuned edge models achieve a macro-averaged WER of $38.0\%$ compared to $64.9\%$ for the best zero-shot baseline, a $26.9$ percentage-point reduction using models $3-40\times$ smaller. Results confirm that domain specialization dominates scale for spontaneous African speech. Cross-domain evaluation shows that fine-tuned models recover usable performance on out-of-distribution (OOD) speech, while zero-shot models regain an advantage when the test domain matches their pretraining distribution. A distributed native-speaker audit across all surveyed languages produces a linguistically-grounded error taxonomy, showing that CTC and autoregressive architectures behave differently across language families. We further show that WER alone misrepresents performance for syllabary-script languages where CER/WER ratios reveal substantially higher character-level accuracy than headline WER suggests. Finally, to contribute to future African ASR research, we release all model weights, fine-tuning and evaluation scripts, and a cleaned WAXAL subset covering all $19$ languages.

---


### 604. [When Do Attention Circuits Form? Developmental Trajectories of Capability and Attention-Sink Emergence Across Three 1B-ClassArchitectures](https://arxiv.org/abs/2606.02378)

**<font color=#1a73e8>作者：</font>** Yongzhong Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We track the developmental trajectory of attention-head circuit formation across three 1B-class language models spanning two architecture families (dense transformer, mixture-of-experts) and two pretraining corpora (The Pile, DCLM): Pythia 1B, OLMo 1B-0724-hf, and OLMoE 1B-7B-0924. At each of 10 log-spaced revisions per model -- 30 mechanistic-interpretability runs in total -- we apply a participation-ratio (PR) spectral signal and an all-head capability-specific selectivity screen to track induction, previous-token, and BOS-attractor heads as they emerge.
Five findings. (F1) Layers 0 and 1 produce zero BOS-classified heads at every revision in every model: the L0/L1 zero-BOS floor is an architectural property, not a learned outcome. (F2) The whole-model BOS-attractor fraction follows three distinct emergence shapes -- a gradual ramp in Pythia 1B, a sharp phase transition in OLMo 1B (7% to 70% between adjacent checkpoints), and a gradual ramp in OLMoE 1B-7B. (F3) In DCLM models, induction-circuit formation precedes BOS-attractor formation by 10-20x in tokens; capability-circuit formation and attention-sink formation are two transitions, not one. (F4) The capability-specific screen converges to the final induction circuit within 0.3-2% of total training tokens -- circuit identification does not require the final model. (F5) For every final-checkpoint induction head sampled across all three models, per-head PR is elevated at or before the first revision at which that head crosses its capability-selectivity threshold.
The results refine the induction-phase-transition framing: in 1B-class models trained on DCLM, the induction transition and the attention-sink transition are separated by an order of magnitude in tokens and have qualitatively different shapes.

---


### 605. [Honey, I Shrunk the Arc de Triomphe!](https://arxiv.org/abs/2606.02379)

**<font color=#1a73e8>作者：</font>** Yuanbo Xiangli, Hanyu Chen, Xueqing Tsang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metric scale monocular geometry estimation has seen significant progress through large-scale data aggregation, yet current foundation models suffer from a persistent ''scale-collapse'' phenomenon: distant landmarks and vast landscapes are metrically underestimated. We hypothesize that this performance gap stems from a training data bottleneck, where existing metric-scale datasets are hardware-constrained to homogenous vehicle-captured LiDAR or short-range indoor scans, or consist of synthetic data that lacks the semantic complexity of the physical world. To bridge this gap, we curate a new metrically-grounded, in-the-wild dataset that we call MetricScenes, gathered from a variety of sources including Internet photo collections and stereo imagery. We estimate camera poses and initial depth maps for each scene using off-the-shelf methods, and recover absolute scale from geo-tagged metadata as well as known stereo camera baselines. We also improve the quality of depth maps derived from MetricScenes via a new two-stage Poisson completion method. Fine-tuning MoGe-2 on our dataset significantly mitigates scale-collapse and achieves superior metric accuracy in unconstrained, open-domain scenes while maintaining state-of-the-art performance on standard benchmarks.

---


### 606. [SPADE-Bench: Evaluating Spontaneous Strategic Deception in Agents via Plan-Action Divergence](https://arxiv.org/abs/2606.02380)

**<font color=#1a73e8>作者：</font>** Yuyan Bu, Haowei Li, Qirui Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM-based agents expand their operational scope, reliability becomes a prerequisite for real-world deployment. However, in practical applications, human users cannot monitor every immediate behavior; instead, the execution process often remains a black box, leaving users dependent solely on the agent's self-reported updates. This opacity creates a critical risk: agents may present observer-facing reports that diverge from their executed actions, rendering the system uncontrollable, especially in high-stakes autonomous scenarios. We term such self-reported plan-action divergence as agent deception. To assess this, we introduce SPADE-Bench, a benchmark designed to evaluate spontaneous plan-action divergence. Unlike prior deception benchmarks, SPADE-Bench simultaneously integrates actual tool execution and controlled pressure scenarios. This design ensures ecological validity and rigorously distinguishes strategic deception from mere hallucination through controlled plan-action comparisons under pressure. Experiments across mainstream models confirm that agent deception is a genuine and pressing issue in tool-use contexts. By providing a comprehensive and robust evaluation framework, SPADE-Bench fills a critical gap in agent safety, facilitating the community's progress toward building trustworthy and controllable autonomous systems.

---


### 607. [A Mathematical Conflict Framework for Contextual Data Modulation](https://arxiv.org/abs/2606.02381)

**<font color=#1a73e8>作者：</font>** Hakan Emre Kartal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this study, a generalized operator-based mathematical conflict framework is presented to explicitly represent structural discrepancies between raw data and contextual data. The proposed structure treats conflict as a local, directional, and context-sensitive quantity, integrating components such as weighting, scale behavior, and output mapping under a unified abstract operator. Without being reduced to a specific learning algorithm or optimization method, the framework is defined as a general structure adaptable to different classes of problems. While existing approaches typically treat conflict merely as an implicit side effect embedded within the optimization process, the proposed framework considers conflict as an independent, operator-based, and component-level mathematical object.

---


### 608. [A Game-Theoretic Decision Framework for Optimal Selection of Coordination Detection Methods in Multi-UAV Fleet Operations](https://arxiv.org/abs/2606.02383)

**<font color=#1a73e8>作者：</font>** Christian Manasseh  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Detecting coordination among unmanned aerial vehicle (UAV) fleets operating in shared airspace and identifying the route-lead aircraft whose navigation decisions govern fleet behavior presents a fundamental speed--accuracy trade-off: fast methods enable real-time traffic management but sacrifice detection fidelity, while accurate methods may exceed the time budget for actionable airspace deconfliction. This paper presents a game-theoretic decision framework that resolves this trade-off by formulating method selection as a two-player zero-sum game between a Monitor (selecting computational methods and parameters) and Nature (selecting the unknown traffic scenario). We construct an end-to-end pipeline from trajectory surveillance data through eight candidate detection algorithms, a Monte Carlo sensitivity analysis characterizing their stochastic performance, and finally a multi-objective optimization layer that identifies Pareto-optimal method portfolios. The minimax solution provides a robust mixed strategy with a probability distribution over methods that guarantees worst-case performance regardless of scenario uncertainty. Experimental evaluation across 200 randomized configurations spanning 5--50 aircraft demonstrates that the framework recommends distinct method portfolios depending on operational priority: Koopman Phase dominates balanced (70.6%) and speed-priority (79.7%) profiles, while CRQA emerges as primary (47.4%) when route-lead identification is prioritized. The framework achieves a guaranteed game value of 0.29--0.53 (normalized utility) across all tested preference profiles, providing the first principled, scenario-adaptive methodology for computational method selection in UTM fleet monitoring operations.

---


### 609. [TabPrep: Closing the Feature Engineering Gap in Tabular Benchmarks](https://arxiv.org/abs/2606.02384)

**<font color=#1a73e8>作者：</font>** Andrej Tschalzev, Nick Erickson, Yuyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Progress in tabular machine learning has largely focused on increasingly sophisticated model architectures. At the same time, feature engineering remains a critical yet underexplored component of real-world modeling pipelines that is entirely absent from modern benchmarks, which creates an unquantified evaluation gap. In this work, we introduce TabPrep, a lightweight preprocessing pipeline composed of feature generators that are carefully designed to target three specific structural data patterns. We show that many widely used model classes exhibit predictable blind spots to these patterns and that systematic feature engineering alone can establish new peak performance. Across the TabArena benchmark, integrating TabPrep into model training and tuning consistently improves performance for tree-based, neural, linear, and foundation models, often surpassing gains achieved by model-centric innovations alone. TabPrep outperforms previous automated feature engineering approaches in performance, efficiency, and applicability across datasets, enabling integration into large-scale benchmarks. By releasing TabPrep (see this https URL), we enable researchers to integrate feature engineering into their benchmarking setup, filling a longstanding gap in tabular evaluations.

---


### 610. [Explainable Forensics of Manipulated Segments in Untrimmed Long Videos](https://arxiv.org/abs/2606.02402)

**<font color=#1a73e8>作者：</font>** Yue Feng, Jingjing Li, Qijia Lu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of AI-driven video generation has transformed content creation, while simultaneously increasing the risk of misinformation through localized manipulations in long-form videos. Existing video forensic methods predominantly operate on short, independent clips, and thus fail to capture realistic scenarios where AI-generated content is sparsely embedded within otherwise authentic footage. To bridge this gap, we formulate the task of Temporal AI-Generated Segment Localization and Explanation, which targets authenticity detection, temporal localization, and interpretable analysis of manipulated segments in untrimmed long videos. We further introduce TASLE, a large-scale benchmark comprising 12,472 untrimmed videos with diverse manipulation patterns and rich annotation signals, including temporal boundaries, authenticity labels, and segment-level rationales. In addition, we propose MSLoc, a coarse-to-fine forensic baseline that combines a boundary-sensitive proposal generation module for efficient long-video scanning with an MLLM-based refinement module for precise boundary localization and interpretable reasoning. Experiments validate the effectiveness of the proposed baseline, highlighting the importance of segment-level explainable forensics for long-form AI-generated video analysis. Our dataset and code are publicly available at this https URL.

---


### 611. [AutoForest: Automatically Generating Forest Plots from Biomedical Studies with End-to-End Evidence Extraction and Synthesis](https://arxiv.org/abs/2606.02403)

**<font color=#1a73e8>作者：</font>** Massimiliano Pronesti, Angelo Miculescu, Mohsin Kapdi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic reviews rely on forest plots to synthesise quantitative evidence across biomedical studies, but generating them remains a fragmented and labour-intensive process. Researchers must interpret complex clinical texts, manually extract outcome data from trials, define appropriate interventions and comparators, harmonise inconsistent study designs, and carry out meta-analytic computations-typically using specialised software that demands structured inputs and domain expertise. While recent work has demonstrated that large language models can extract study-level data from unstructured text, no existing system automates the complete pipeline from raw documents to synthesised forest plots. To address this gap, we introduce AutoForest, the first end-to-end system that generates publication-ready forest plots directly from biomedical papers. Given one or more study papers, AutoForest automatically suggests ICO (Intervention, Comparator, Outcome) elements, extracts outcome data, performs statistical synthesis, and renders the final forest plot. We describe the system architecture, user interface and demonstrate its effectiveness on real-world examples through a user study involving clinicians, showing how AutoForest can accelerate evidence synthesis and substantially lower the barrier to conducting meta-analyses.

---


### 612. [Edge Prediction for Roof Wireframe Reconstruction with Transformers](https://arxiv.org/abs/2606.02406)

**<font color=#1a73e8>作者：</font>** Gustav Hanning, Ludvig Dillén, Jonathan Astermark 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a competitive solution to the S23DR Challenge 2026, which aims to reconstruct 3D house roof wireframe models from sparse SfM point clouds and ground-level semantic segmentations and depth maps. Our proposed method utilizes an end-to-end Transformer encoder-decoder architecture inspired by DETR. To effectively process the geometric and semantic data, the sparse SfM point cloud input is dynamically subsampled based on semantic priority and augmented with Gestalt and ADE20k class features. To further increase segmentation context, we fuse the point features with additional Gestalt feature encodings which are obtained by projecting the points into latent feature maps produced by a frozen autoencoder. Learned query embeddings are then decoded directly into 3D wireframe edges via cross-attention mechanisms. Evaluated on the "HoHo 22k" dataset, our approach significantly outperforms both handcrafted and learned baselines, achieving a Hybrid Structure Score (HSS) of 0.6476 and securing the second-highest position on the challenge's private leaderboard.

---


### 613. [Fostering Emotional Perspective-Taking: An Exploration of Affective Face-Tracking Interactions in the VR Narrative Rekindle](https://arxiv.org/abs/2606.02425)

**<font color=#1a73e8>作者：</font>** Hector Fan, Casper Hartveld, Mark Sivak  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interest in leveraging emotions in Interactive Digital Narrative (IDN) has been growing, and Virtual Reality (VR) offers rich access to real-time biometric data such as facial expressions; yet this capability remains underexplored in novel IDN design. Existing approaches typically treat emotion input superficially, such as adjusting system difficulty or aesthetics, but rarely influence how players experience the narrative itself. Prior work also lacks a focus on a specific authored narrative. We propose an experimental affective interaction model that uses a VR headset's built-in face-tracking capability to recognize player emotional states, fostering "emotional perspective-taking" between the player and their embodied story character, thereby deepening the player's emotional connection to the character and their narrative engagement with the VR experience.

---


### 614. [Bridging the Sim-to-Real Gap in Semiconductor Visual Program Synthesis via Input Binarization](https://arxiv.org/abs/2606.02434)

**<font color=#1a73e8>作者：</font>** Yusuke Ohtsubo, Kota Dohi, Koichiro Yawata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Precise parametric control over circuit geometry is essential for semiconductor inspection, yet obtaining sufficient real training data remains costly. Although generative models such as diffusion models and Generative Adversarial Networks (GANs) can augment training data, they cannot guarantee the nanometer-scale geometric accuracy required for metrology tasks. We propose a visual program synthesis framework in which a Vision-Language Model (VLM) converts inspection images into editable Domain-Specific Language (DSL) code describing circuit geometries, enabling controlled generation of training data with exact parameter manipulation. Because the VLM is trained solely on synthetic DSL-rendered data, a domain gap arises when processing real Scanning Electron Microscope (SEM) images. We bridge this gap with an input binarization strategy that strips SEM-specific texture and noise, letting the model focus on geometric structure. On the MIIC dataset, binarized inputs improve the mean Dice coefficient from 0.4393 to 0.5256 over the raw-input baseline, demonstrating that simple texture abstraction substantially mitigates the sim-to-real gap.

---


### 615. [On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters](https://arxiv.org/abs/2606.02437)

**<font color=#1a73e8>作者：</font>** Mind Lab, Song Cao, Vic Cao 等 54 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) is usually treated as a cheaper alternative to full fine-tuning. We study a broader role: small trainable adapters as persistent local state on top of strong shared foundation models. In this framing, the base model provides shared competence while adapters carry instance-specific behavior such as preferences, skills, tool habits, and memory-like updates. We organize the problem around three scaling axes: Scale Up, where stronger shared priors make small local updates more useful; Scale Down, where we study how small adapters can be while remaining reliable; and Scale Out, where many persistent adapted instances coexist. MinT provides one infrastructure example for managing adapter identity, revision, provenance, evaluation, and serving residency. Together, the results suggest that PEFT can be a compact substrate for persistent personal models rather than only a budget substitute for full fine-tuning.

---


### 616. [Spatial-Temporal Decoupled Reference Conditioning for Identity-Preserving Text-to-Video Generation](https://arxiv.org/abs/2606.02441)

**<font color=#1a73e8>作者：</font>** Yuheng Chen, Teng Hu, Yuji Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-preserving video generation (IPVG) aims to synthesize high-fidelity videos that follow text prompts while faithfully preserving a reference identity. Despite recent progress, existing IPVG methods still struggle to balance high-level semantic control and low-level identity fidelity. To bridge this gap, we propose ST-DRC, an effective Spatial-Temporal Decoupled Reference Conditioning framework for identity-preserving text-to-video generation. At the framework level, ST-DRC performs latent in-context feature injection by encoding the reference image with the video VAE and concatenating it with noisy video latents, enabling rich low-level identity details to be accessed without additional adapters. To separate identity-aware reference retrieval from appearance copying, we introduce TASS-RoPE, a Temporal-Adjacent Spatial-Shifted RoPE scheme that places reference tokens near the video sequence in time but shifts them in space, allowing reference information to flow through spatio-temporal attention while suppressing pixel-level copy-paste shortcuts. To further prevent shortcut learning and strengthen the otherwise diluted identity supervision in the diffusion objective, we combine appearance-invariant reference augmentation with face-guided identity objectives, encouraging the model to preserve identity under variations in color, pose, and layout. At inference time, we introduce a three-stream reference classifier-free guidance strategy that independently controls text adherence and reference fidelity. Experiments demonstrate that ST-DRC achieves strong identity preservation, prompt alignment, temporal consistency, and video quality with a lightweight design built on LTX-2.3. Our method ranks among the top submissions in the facial identity-preserving video generation track, validating the effectiveness of spatial-temporal decoupled reference conditioning.

---


### 617. [HLL: Can Agents Cross Humanity's Last Line of Verification?](https://arxiv.org/abs/2606.02449)

**<font color=#1a73e8>作者：</font>** Xinhao Song, Su Su, Sirui Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal agents are increasingly expected to operate interfaces on behalf of users, raising a central deployment question: can they truly substitute for humans in workflows that services deliberately protect against automation? CAPTCHA verification makes this question concrete. It is not merely a visual puzzle, but a human-verification boundary placed before account creation, content access, form submission, and other protected actions. We introduce \textbf{Humanity's Last Line of Verification (HLL)}, a controlled benchmark that uses interactive CAPTCHA verification to evaluate whether agents can cross this boundary through grounded, human-like interaction rather than recognition alone. HLL covers diverse CAPTCHA interactions and exposes agents to controlled realism stressors, including cluttered webpages, harder task variants, and trace-conditioned validation of the solving process. We evaluate eight frontier multimodal agents in a closed-loop GUI environment. The results show that current agents remain brittle at this human-substitution boundary: performance varies sharply across verification types, degrades under realistic interface conditions, and drops further when correct answers must be supported by valid action traces. By exposing gaps in localization, action calibration, state tracking, and process consistency, HLL provides a concrete testbed for measuring how close multimodal agents are to acting as human substitutes in protected real-world workflows. Our code is available at this https URL

---


### 618. [Reason-Then-Retrieve for CoVR-R with Structured Edit Prompts and Dense-Sparse Fusion](https://arxiv.org/abs/2606.02450)

**<font color=#1a73e8>作者：</font>** DongQing Liu, MengShi Qi, HongWei Ji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CoVR-R studies reason-aware composed video retrieval: given a reference video and an edit instruction, the system must retrieve the target video that satisfies the edit. The main difficulty is that the target is not described directly; it must be inferred from fine-grained changes in object identity, action order, final state, hand interaction, and scene transition. We build a zero-shot reason-then-retrieve pipeline around Qwen3.5-27B. For each gallery video, the model generates a retrieval-oriented structured description and a dense embedding by pooling generated-token hidden states with token-dependent weights. For each query, the model first performs edit reasoning over the reference video and instruction, then generates a target-video description whose hidden states serve as the query embedding. We complement dense retrieval with a TF-IDF branch over the generated texts and fuse the two rankings with split-specific weights. On validation, the current best submission reaches 80.81 at R@1, 94.86 at R@5, 97.11 at R@10, and 98.59 at R@50. On the blind test split, it reaches 89.73 at R@1, 95.79 at R@5, 96.63 at R@10, and 97.98 at R@50.

---


### 619. [Initialization is Half the Battle: Generating Diverse Images from a Guidance Potential Posterior](https://arxiv.org/abs/2606.02453)

**<font color=#1a73e8>作者：</font>** Xiang Li, Dianbo Liu, Kenji Kawaguchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable fidelity of generative models, they frequently suffer from mode collapse. Existing strategies for enhancing diversity predominantly focus on intervening during the generation trajectory. We identify a critical oversight that the standard Gaussian initialization often causes trajectories to collapse into dominant modes because it is agnostic to the guidance potential landscape. In this work, we formulate selecting the initial noise from a guidance potential posterior, which effectively re-weights the prior towards diversity-rich regions. To sample from this distribution efficiently, we introduce Diversity-inducing Initialization (DivIn), which leverages Langevin dynamics to actively navigate the initialization landscape, steering initial noise away from collapsing regions while anchoring them to the valid data manifold. Our method serves as an inference-time diversity enhancement compatible with both diffusion and flow matching models. Extensive experiments show that DivIn exhibits a superior performance in both class-to-image and text-to-image scenarios. Furthermore, we highlight that as DivIn is orthogonal to trajectory-based methods, combining them significantly expands the diversity-quality Pareto frontier beyond what either achieves in isolation.

---


### 620. [Speculative Sampling For Faster Molecular Dynamics](https://arxiv.org/abs/2606.02455)

**<font color=#1a73e8>作者：</font>** Arthur Kosmala, Stephan Günnemann, Meng Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular dynamics (MD) is a key tool for simulating the dynamical behavior of atomic systems. However, MD is inherently serial, which makes it difficult to increase single-system throughput with concurrent compute. To address this, we introduce Langevin Speculative Dynamics (LSD), a distributed and model-agnostic speculative sampler for accelerating MD without adding relative error. Inspired by speculative methods in language and diffusion modeling, LSD uses a draft model to propose fast simulation steps and verifies them in parallel with a slower target model, applying a transport map from the draft to the target distribution. We extend speculative sampling to second-order Langevin dynamics, derive the achievable speedup as a function of physical parameters, show that LSD generalizes across different systems and draft-target combinations with a 3-9x speedup, and confirm theoretically and empirically that LSD samples trajectories from its target model distribution.

---


### 621. [Beyond One-shot: AI Agents for Learning in Field Experiments](https://arxiv.org/abs/2606.02458)

**<font color=#1a73e8>作者：</font>** Junjie Luo, Ritu Agarwal, Gordon Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations routinely run experiments for A/B testing, yet the data generated from one experiment is underutilized to inform subsequent intervention design. Significant barriers exist to extracting actionable knowledge from prior experimental data to inform new interventions. We study whether tool-augmented agentic AI can automatically learn from experimental data to generate new interventions in subsequent experiments. Through two-stage field experiments in healthcare prescription messaging (693,139 patient visits), we compare a Human + Chatbot method (Stage 1: behavioral experts with conversational AI co-designing 13 message variants, 444,691 patient visits) against a Tool-Augmented Agentic AI method (Stage 2: AI autonomously extracting principles from Stage 1 data to generate 17 new variants, 248,448 patient visits). The Agentic AI method, equipped with analytical tools, structured Data-Information-Knowledge-Wisdom (DIKW) reasoning agents, and transparent evidence chains, produces superior interventions: the best AI-generated message achieved a 69.8% CTR (+6.5 percentage points over baseline). Critically, our results suggest that the value comes from domain-specific experimental data, not from general reasoning ability: frontier LLMs operating without experimental data failed to predict which interventions would succeed. The field experiments also revealed that general-purpose behavioral theories used for intervention design do not extend uniformly to specific healthcare contexts, motivating an agentic AI approach to theory audits at field-experiment scale. Our research shows that tool-augmented AI can learn from experimental data and generate improved domain-relevant interventions, transforming behavioral experimentation from one-shot evaluation into a scalable system for cumulative design learning.

---


### 622. [AGENTCL: Toward Rigorous Evaluation of Continual Learning in Language Agents](https://arxiv.org/abs/2606.02461)

**<font color=#1a73e8>作者：</font>** Yiheng Shu, Bernal Jiménez Gutiérrez, Saisri Padmaja Jonnalagedda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents spend substantial inference time solving individual tasks, yet the experience acquired in one episode is often underutilized in future episodes. Continual learning expects an agent to accumulate reusable experience across a stream of tasks, improve over time, and avoid interference from irrelevant experiences. Unfortunately, existing benchmarks struggle to evaluate continual learning in language agents rigorously. Most efforts focus on retrieval and reasoning over long-context conversations or documents, while recent lifelong-adaptation benchmarks often rely on naive task streams with limited analysis of cross-task relationships, making it difficult to understand what an agent learns and reuses over time. This paper presents an evaluation framework AgentCL for continual learning in agents, centered on controlled task streams and metrics for transfer gains. AGENTCL constructs compositional streams where earlier sub-solutions, evidence, or workflows are intentionally reusable in later tasks, and contrasts them with naive streams where such reusability is not guaranteed. We use the benchmark to evaluate non-parametric memory designs for continual learning. To diagnose how memory design choices affect continual learning, we develop MemProbe, a probing method that stores interactions, insights, and skills, while filtering unreliable experiences during consolidation. Empirical analysis across coding, deep research, and language understanding/reasoning tasks shows that naive streams offer limited ability to distinguish memory designs, whereas controlled streams more clearly distinguish their plasticity. Meanwhile, naive and held-out settings often yield limited gains and can expose memory-induced degradation. These results highlight the need for stronger memory designs that balance plasticity and stable reuse.

---


### 623. [MASER: Modality-Adaptive Specialist Routing for Embodied 3D Spatial Intelligence](https://arxiv.org/abs/2606.02463)

**<font color=#1a73e8>作者：</font>** Hilton Raj, Vishnuram AV  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In 3D environments, Embodied Agents answer spatially relevant questions through reasoning from a mixture of modalities including natural language, RGB images, point clouds, depth maps and camera poses. Existing Vision-Language models (VLMs) are fine-tuned over a single modality. This completely ignores the question semantics which may favor a different modality than the finetuned modality. To address this, we propose MASER (Modality-Adaptive SpEcialist Routing), a lightweight framework that trains five different modality adapters of a shared VLM backbone and learns a neural routing policy that selects the best adapter based on the question during inference. We encode each question with a frozen sentence transformer and pass the embedding through a small Multi-layer Perceptron (MLP) trained on oracle adapter-accuracy labels. We evaluate our methodology over the Open3D-VQA benchmark and our evaluations show that no single modality is universally optimal -- point-cloud answers are best in 51.5% of cases. MASER routes with 51.3% oracle agreement, outperforming a Random-Forest ablation (43.5%), with only a single adapter call per question.

---


### 624. [Learning When to Translate for Multilingual Reasoning](https://arxiv.org/abs/2606.02465)

**<font color=#1a73e8>作者：</font>** Deokhyung Kang, Hyounghun Kim, Gary Geunbae Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models (RLMs) achieve strong performance on complex reasoning tasks, but still exhibit substantial multilingual reasoning gaps, largely due to language-understanding failures in non-English inputs. English translation can mitigate these failures by expressing non-English inputs in a form that RLMs can more reliably interpret, yet translating every input is unnecessary when the model can reason reliably from the original query. To address this challenge, we propose Luar, a Language Understanding Boundary-aware Reinforcement Learning framework that trains RLMs to selectively invoke translation when direct understanding is unreliable. Luar trains the model to choose between solving the original input directly and reasoning over its English translation, encouraging translation only when translator-augmented reasoning is expected to substantially outperform direct reasoning. Across multilingual reasoning benchmarks, Luar outperforms standard GRPO and other training-based baselines, with particularly large gains on low-resource languages. Further analysis shows that Luar avoids unnecessary translation in cases where direct reasoning is sufficient, while extending its translator-call behavior to unseen low-resource languages. Together, our work suggests a selective approach to multilingual reasoning: RLMs can learn to invoke translation only when their direct understanding is unreliable. The project will be made publicly available at this https URL

---


### 625. [Places in the Wild: A Large, High-Resolution RAW Photograph Dataset for Ecologically Valid Vision Research](https://arxiv.org/abs/2606.02481)

**<font color=#1a73e8>作者：</font>** Michelle R. Greene  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large image datasets have accelerated progress in cognitive neuroscience and computer vision. However, most datasets are low-resolution, internet-sourced JPEGs with unknown capture conditions and limited spatial context. Places in the Wild is a dataset of 67,574 high-resolution photographs collected in situ across 810 physical locations spanning 260 basic-level scene categories, including indoor, urban, and natural environments. At each location, a 45-megapixel Canon EOS R5 mounted on a panoramic tripod captured 72 images at 5-degree horizontal intervals plus 12 images at varying elevations, yielding dense 360-degree viewpoint sampling. All images were recorded simultaneously as 14-bit RAW (CR3) files and compressed JPEGs, preserving sensor-level detail for analyses of luminance, contrast, color, and other image statistics. The dataset is accompanied by complete EXIF metadata and a suite of image-quality metrics. Places in the Wild supports research on viewpoint-dependent recognition in humans and models, training and evaluation of scene-understanding systems under realistic conditions, characterization of natural scene statistics, and experiments requiring near-full-field visual displays.

---


### 626. [Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools](https://arxiv.org/abs/2606.02483)

**<font color=#1a73e8>作者：</font>** Bardia Mohammadi, Lars Klein, Akhil Arora 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-augmented language agents speculatively issue likely future tool calls to hide latency, but those calls leak inferred user intent to external services before the agent commits to the branch. Every external observer that received the call retains the disclosure after the agent abandons the branch. Timing is the issue, not authorization: no commit-time cleanup, read-only restriction, or access-control allow-list unsends what an observer already holds. We call these invocations ghost tool calls and propose Speculative Tool Privacy Contracts, a runtime abstraction that treats observation before commitment as a first-class effect, distinct from state mutation. We implement the contracts in a prototype runtime and evaluate twelve policies across three corpora. Speculative dispatch increases what an observer can infer about user intent; post-hoc filters, read-only restrictions, and access-control allow-lists leave that inference intact; only issue-time policies that change or suppress the speculative call's argument or destination projection before dispatch reduce it.

---


### 627. [RASER: Recoverability-Aware Selective Escalation Router for Multi-Hop Question Answering](https://arxiv.org/abs/2606.02488)

**<font color=#1a73e8>作者：</font>** Yuyang Li, Zihe Yan, Tobias Käfer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-hop question-answering systems often use expensive retrieval on every question. They may decompose the question, run several retrieval rounds, or search through bridge entities before answering. All of these strategies rely on repeated LLM calls to rewrite or decompose the question, which increases extra token cost, and it is not fitting when the LLM budget is tight. However, our analysis shows that lots of multi-hop questions are already answered correctly by a single one-shot RAG, so running an extra retrieval on every question wastes the budget. We introduce RASER (Recoverability-Aware Selective Escalation Router), a family of cheap routers built on one-shot RAG and six features from it. RASER-2 decides whether to stop or escalate to the extra-retrieval action PRUNE. RASER-3 chooses among one-shot RAG, PRUNE, and iterative retrieval IRCoT, using the same features but adding an explicit cost-accuracy trade-off. Neither router makes an extra LLM call to decide. Across six LLMs and three multi-hop QA benchmarks, both routers stay competitive with the other state-of-the-art (SOTA) baselines in F1 while spending only 41-49% of always-prune's tokens and also less than the iterative and decomposition retrieval baselines.

---


### 628. [Expressivity of congruence-based architectures for DNNs on positive-definite matrices](https://arxiv.org/abs/2606.02490)

**<font color=#1a73e8>作者：</font>** Antonin Oswald, Estelle Massart  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work studies neural architectures for classifying symmetric positive-definite matrices, focusing on congruence-like layers, in which the input matrix is multiplied on the left and right by a (possibly rectangular) weight matrix $W$ and its transpose. Such layers lie at the core of the celebrated SPDNet and have also been employed independently for dimensionality reduction on positive-definite data. We show that the (semi)-orthogonality constraint commonly imposed on $W$ limits the expressivity of these layers: for certain activation functions, the resulting architecture collapses to a one-hidden-layer equivalent. This lack of expressivity follows from a loss of spectral diversity in congruence-like layers for semi-orthogonal $W$ and is a direct consequence of Poincaré's separation theorem. We then examine the choice of the final classifier, comparing several Riemannian classifiers and discussing their compatibility with the feature maps produced by congruence-like layers.

---


### 629. [MORPHOS: Autoregressive 4D Generation with Temporal Structured Latents](https://arxiv.org/abs/2606.02491)

**<font color=#1a73e8>作者：</font>** Minkyung Kwon, Jinhyeok Choi, Youngjin Shin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MORPHOS, a novel autoregressive framework that generates dynamic 3D assets from videos across diverse representations, including meshes, 3D Gaussians, and radiance fields. Existing methods are typically limited to a single representation, struggle to model topological changes, or fail to maintain temporal consistency over long videos. To address these limitations, we introduce the Temporal Structured Latents (T-SLAT), a unified 4D representation that jointly encodes geometry and appearance along the temporal dimension. Leveraging T-SLAT, MORPHOS autoregressively generates dynamic 3D assets via causal attention, conditioning each frame on its preceding history to ensure temporal consistency while handling evolving topologies. We also propose a temporal-structural augmentation to mitigate error accumulation in autoregressive generation. MORPHOS achieves state-of-the-art performance in appearance and competitive results in geometry across multiple benchmarks, demonstrating superior generalization across various representations and robustness in long-horizon generation.

---


### 630. [GloResNet: A lightweight 3D CNN with global topological features for preterm brain injury prediction](https://arxiv.org/abs/2606.02498)

**<font color=#1a73e8>作者：</font>** Boyu Yuan, Jiamiao Lu, Weichuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study introduces an automated deep learning framework for predicting brain injury (BI) in preterm infants from T2-weighted MRI (dHCP dataset). We propose GloResNet, a lightweight 3D CNN based on ResNet-10, pretrained on MedicalNet to address data scarcity. A global manifold mapping strategy first resamples each 3D volume to 128x128x128 and then applies subject-wise z-score intensity normalization, thereby preserving global topology while standardizing appearance. Training integrates mixup, class weighting, and test-time augmentation for robustness. In 5-fold cross-validation, GloResNet achieved 75.18% average accuracy (peak 81.82%), with specificity 0.81 and sensitivity 0.76. Results demonstrate that a topology-aware lightweight CNN has the capability to effectively predict neonatal BI, offering a non-invasive screening tool. The source code of this paper can be obtained from the GitHub repository: this https URL

---


### 631. [Question-Aware Evidence Ledgers for Video Relational Reasoning](https://arxiv.org/abs/2606.02506)

**<font color=#1a73e8>作者：</font>** Yilin Ou, Mengshi Qi, Huadong Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The VRR-QA challenge evaluates visual relational reasoning in videos, where answers often depend on implicit spatial relations, event boundaries, target identity, and dialogue context rather than a single salient frame. We present a test-time reasoning pipeline built around a strong GPT-5.5 video QA solver and a set of question-aware evidence ledgers. The initial solver answers each question from a uniform video representation, while routed ledgers are prompted to make the required targets, count units, reference frames, and temporal or spatial scope explicit for counting, spatial, endpoint, viewpoint, and dialogue reasoning. External tools such as open-vocabulary detection, depth cues, pair crops, ASR, and scene-graph ledgers are used only as evidence sources. A conservative gate keeps the current answer unless independent evidence uniquely supports a different option. The final evidence-gated pipeline achieves 92.95% overall accuracy and 93.79% macro accuracy on the challenge test split.

---


### 632. [Not All Points Are Equal: Uncertainty-Aware 4D LiDAR Scene Synthesis](https://arxiv.org/abs/2606.02510)

**<font color=#1a73e8>作者：</font>** Xiang Xu, Alan Liang, Youquan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Constructing faithful 4D worlds from LiDAR-acquired sequences is crucial for embodied AI, yet current generative frameworks apply uniform modeling capacity across all spatial regions. This ignores that perceptual difficulty varies dramatically within a single scan: distant surfaces, occluded boundaries, and small-scale objects carry far higher uncertainty than well-observed structures. We present U4D, a new framework that explicitly leverages spatial uncertainty to guide LiDAR scene generation in a "hard-to-easy" schedule. U4D derives per-point uncertainty maps via Shannon Entropy from a pretrained segmentor, then applies an unconditional diffusion stage to synthesize high-entropy areas with precise geometry, followed by a conditional completion stage that fills in the remaining regions using these structures as priors. A MoST (Mixture of Spatio-Temporal) block further maintains cross-frame coherence by dynamically balancing spatial detail and temporal continuity. Extensive experiments on nuScenes and SemanticKITTI demonstrate state-of-the-art scene fidelity, temporal consistency, and downstream performance.

---


### 633. [A Biconvex Formulation for Stable Transport of Mixture Models with a Unique Solution](https://arxiv.org/abs/2606.02515)

**<font color=#1a73e8>作者：</font>** Yeganeh Marghi, Kelly Jin, Uygar Sümbül  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal transport (OT) provides a principled framework for mapping between probability distributions. Despite extensive progress, applying OT to large-scale data remains computationally demanding, and the resulting pointwise transport plans are often difficult to interpret. We introduce Optimal Mixture Transport (OMT), a scalable framework that shifts the transport paradigm from individual samples to mixtures of subpopulations, reformulating the transport problem as a strictly biconvex optimization with a unique global minimizer. We further establish theoretical guarantees on the stability of the OMT map, showing that bounded perturbations of the underlying distributions lead to bounded changes in the transport plan. By formulating subpopulations as exponential-family distributions, OMT decouples computational complexity from the sample size, scaling solely with the number of mixture components. We demonstrate the effectiveness and practicality of OMT on a wide range of synthetic benchmarks and real-world datasets, including image data and large-scale single-cell RNA sequencing measurements.

---


### 634. [ToolFG: Towards Well-Grounded Fine-Grained Image Classification](https://arxiv.org/abs/2606.02518)

**<font color=#1a73e8>作者：</font>** Yu Xue, Haoxuan Qu, Zhuoling Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained image classification (FGIC) has broad applications and has attracted significant research attention. In this paper, we explore a novel paradigm for solving FGIC by proposing \textbf{ToolFG}, the first tool-integrated MLLM-based framework tailored to FGIC. ToolFG enables MLLMs to autonomously and flexibly use external tools during the reasoning process, actively interact with images, and collect verifiable visual cues for distinguishing highly similar categories in a more \textit{reliable} and \textit{well-grounded} manner. To equip the model with such tool-use ability, we design a novel \textbf{MCTS-guided tool-use knowledge distillation mechanism}, which effectively mines tool-use- and FGIC-relevant knowledge from advanced proprietary MLLMs for model training. Furthermore, we propose a \textbf{model-tool co-evolution mechanism} that jointly refines the toolset and the model's tool-use policy, driving them toward a mutually adapted and FGIC-specialized state. Extensive experiments demonstrate the effectiveness of our framework.

---


### 635. [Drifting Preference Optimization for One-Step Generative Models](https://arxiv.org/abs/2606.02521)

**<font color=#1a73e8>作者：</font>** Zhou Jiang, Yandong Wen, Zhen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-step text-to-image generators are attractive for deployment because they generate an image with a single forward pass, but preference finetuning them remains difficult: standard alignment methods often rely on policy likelihoods, denoising trajectories, differentiable reward gradients, or test-time optimization. We propose Drifting Preference Optimization (DrPO), an online preference-finetuning method for deterministic one-step generators. For each prompt, DrPO samples candidates from the current generator, ranks them with a target reward, and uses high- and low-scoring samples to synthesize a feature-space update direction. The update is a non-parametric dipole preference field plus a reference drift estimated from the frozen base generator, and is optimized through a detached feature-space regression target. The target reward is used only for ranking, so DrPO can train with large, black-box, or non-differentiable rewards while inference remains a single generator call. We evaluate DrPO on SD-Turbo and SDXL-Turbo with multiple target rewards and benchmarks, including HPSv3 and GenEval. DrPO improves alignment over reward-gradient-free one-step preference baselines and reduces HPSv3 training computation by $3.51\times$ under the matched effective-batch setting by removing reward-model backpropagation. Initial offline experiments suggest that sample-based gradient synthesis can also be used beyond online reward ranking.

---


### 636. [FigSIM: A Dataset for Fine-grained Suicide Severity and Figurative Language in Suicide Memes](https://arxiv.org/abs/2606.02523)

**<font color=#1a73e8>作者：</font>** Liuliu Chen, Elise R. Carrotte, Brian E. Chapman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Suicide memes are memes used to express suicide-related thoughts or comment on suicide-related issues. Suicide memes are increasingly common on social media, yet remain poorly understood and potentially harmful. There is an urgent need to better understand their characteristics and to develop appropriate content moderation strategies that limits users' exposure to potentially harmful content. Currently, the absence of annotated datasets of suicide memes remains a key barrier to developing and evaluating automated moderation approaches. In this paper, we introduce FigSIM, the first dataset designed for fine-grained analysis of suicide memes. The dataset consists of 1049 memes, each annotated for (1) fine-grained suicide severity levels, (2) figurative phenomena (e.g., metaphors), and (3) suicide-related content (e.g., suicide method depiction). We benchmark 16 unimodal and multimodal models across three tasks: figurative language, suicide severity, and suicide-related content detection. Overall, FigSIM demonstrates that suicide memes pose unique challenges for both modeling and content moderation. Analysis revealed biases, such as underprediction of higher suicide severity levels, especially for figurative memes. The dataset (including splits used for analyses) is publicly available. Content Warning: This paper contains suicide-related content that may be triggering.

---


### 637. [Why Not Hyperparameter-Friendly Optimisation? A Monotonic Adaptive Norm Rescaling Approach For Long-Tailed Recognition](https://arxiv.org/abs/2606.02526)

**<font color=#1a73e8>作者：</font>** Shuo Zhang, Chenqi Li, Tingting Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed recognition poses a significant challenge for deep learning. The two-stage decoupling paradigm, which separates representation learning from classifier retraining, offers a promising solution. During the classifier retraining stage, adaptive norm rescaling is a popular technique. It adjusts the per-class weight norms via parameter regularization, which inevitably introduces hyperparameters. However, many studies report that long-tailed recognition is sensitive to these hyperparameters, as their setup significantly impacts performance. In this paper, we first provide a class-conditional distribution perspective to support norm rescaling methods. Furthermore, we propose a simple but effective approach called Self-Adaptive Monotonic Normalization (SAMN). SAMN avoids the need for parameter regularization. It directly enforces monotonicity on per-class weight norms using the Pool Adjacent Violators Algorithm, making the method hyperparameter-friendly. SAMN is a universal strategy that integrates seamlessly with other methods for enhanced performance. Experiments on benchmark datasets demonstrate that our method significantly boosts long-tailed recognition performance, often achieving state-of-the-art results.

---


### 638. [Improving Combined Detection and Classification of TEM Defects via Mask-Conditioned Latent Diffusion Augmentation](https://arxiv.org/abs/2606.02532)

**<font color=#1a73e8>作者：</font>** Ni Li, Nuohao Liu, Ryan Jacobs 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analyzing microstructural defects in transmission electron microscopy (TEM) images, particularly in irradiated metal alloys, is often limited by the availability of high-quality, labeled data. To address this, we introduce a generative data augmentation approach using a mask-conditioned latent diffusion model (LDM) for synthesizing realistic TEM images with controllable, automatically labeled multi-class defect masks. Without requiring manual annotations for generation, our method enables the creation of synthetic image-mask pairs by sampling distributions learned from experimental masks. These generated data were used to augment small experimental datasets of varying sizes (10, 50, and 100 labeled experimental images) to train a Mask Regional Convolutional Neural Network (R-CNN) model for defect detection and classification. Our results show that generative augmentation yields small overall model performance improvements, with up to a 0.02 gain in the harmonic mean of detection and classification F1 scores. However, we also find that the relative contributions to detection and classification improvement depend on the specific train/test data split. These findings highlight the potential of targeted generative models to enhance deep learning performance in data-scarce microscopy-based image quantification tasks.

---


### 639. [LL-Bench: Rethinking Low-Level Vision Evaluation in the Era of Large-Scale Generative Models](https://arxiv.org/abs/2606.02535)

**<font color=#1a73e8>作者：</font>** Lu Liu, Huiyu Duan, Chenxin Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale generative models have demonstrated remarkable capabilities across image generation and editing tasks. However, their performance in low-level vision tasks, which require pixel-wise control, remains insufficiently studied. To address this gap, we introduce \textbf{LL-Bench}, a comprehensive \textbf{Benchmark} for evaluating the capabilities of large-scale generative models on \textbf{L}ow-\textbf{L}evel vision tasks. The benchmark comprises 2,469 real-world degraded images covering 16 low-level degradation tasks, and 28,919 restored images produced by 10 state-of-the-art large-scale generative models and 21 conventional restoration models, which are annotated with 152,020 expert-level pairwise human preferences and 28,334 quality scores. Built upon LL-Bench, we present a systematic diagnosis that reveals the performance boundaries and unique failure modes of large-scale generative models across diverse low-level vision tasks, compared with conventional representative restoration approaches. Moreover, we investigate the effectiveness of current quality evaluation metrics on LL-Bench, which exhibit significant discrepancy with human ratings. To better align restored-image quality assessment with human preferences, we further propose \textbf{LL-Score}, an MLLM-based evaluator that captures both restoration quality and hallucination existence. Extensive experiments demonstrate that LL-score not only outperforms existing image quality assessment metrics, but also serves as a promising reward model for training generative models on low-level vision tasks.

---


### 640. [Tracking the Behavioral Trajectories of Adapting Agents](https://arxiv.org/abs/2606.02536)

**<font color=#1a73e8>作者：</font>** Jonah Leshin, Manish Shah, Ian Timmis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text files such as skill files, memory files, and behavioral configuration files play a central role in defining how modern agents act. Through edits by humans or the agents themselves, these files may evolve over time, directly steering the agent's behavior in future interactions. We present a methodology and framework for measuring agent $traits$ by defining traits as directions in the embedding space of a text embedding model. We train a linear model on labeled "before" versus "after" skill file diffs to learn a trait vector, then score arbitrary skill edits by projecting their embedding diffs onto this vector. Evaluated on 68 labeled skill diff pairs for the trait of propensity to seek sensitive data, our method achieves 91.2% sign classification accuracy and a Spearman rank correlation of $\rho = 0.82$ under leave-one-out cross-validation. We build this trait evaluation into a broader agent-to-agent protocol that enables one agent to evaluate another's skill file updates through a trusted intermediary.

---


### 641. [SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction](https://arxiv.org/abs/2606.02540)

**<font color=#1a73e8>作者：</font>** Yuting Ning, Zhehao Zhang, Yash Kumar Lal 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent skills occupy a privileged position in the agent workflow, as agents are expected to implicitly follow and execute them, rendering third-party skills a vulnerable attack surface. Existing studies have revealed unsafe agent behaviors induced by skill-based attacks, but they primarily evaluate poisoned skills within a single task execution and enumerate harms through ad-hoc risk lists. To bridge these gaps, we introduce SkillHarm, a benchmark of skill-based attacks across the skill-use lifecycle, paired with a systematic taxonomy of skill-relevant risks. SkillHarm evaluates two attack scenarios: Fixed-Payload Poisoning (FPP), where a fixed poisoned skill package directly compromises any task session that invokes it, and Self-Mutating Poisoning (SMP), where an initially benign execution silently mutates persistent skill content, deferring harm until a subsequent reuse. It further defines 12 risk types based on the agent workflow component targeted by the harm: data pipelines, system environments, and agent autonomy. To instantiate these attacks at scale, we build AutoSkillHarm, an automated construction pipeline with coding agents driven by natural-language harnesses. The resulting benchmark contains 879 attack samples across 71 skills. Experiments show that current agents remain vulnerable with attack success rates up to 86.3% in FPP and 69.3% in SMP. Our analysis further reveals a latent risk: many apparent attack failures stem from the agent failing to engage with the poisoned file rather than genuine resistance, and current defenses still fail to reliably mitigate the threat.

---


### 642. [Transferable Self-Harm Surveillance from Emergency Department Triage Notes Using an Evidence-Augmented Machine Learning Approach](https://arxiv.org/abs/2606.02545)

**<font color=#1a73e8>作者：</font>** Liuliu Chen, Gowri Rajaram, Eleanor Bailey 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-harm is a major public health concern, but current surveillance relying on hospital presentations is inadequate due to the low sensitivity of diagnostic codes. Emergency Department (ED) triage notes, recorded at the initial point of contact, provide a succinct summary of presentations and an opportunity to identify self-harm. We developed a three-stage approach, augmenting traditional machine learning with large language model-based screening and evidence extraction to detect self-harm in ED triage notes. We assessed model transferability across three Australian hospitals. Our approach showed AUPRCs of 0.887 +/- 0.016 and 0.884 +/- 0.012 during internal and external validation. Prospectively, it achieved AUPRC of 0.881 +/- 0.008 at the development site, and 0.879 +/- 0.012 and 0.816 +/- 0.015 at two external sites without site-specific retraining. A key advantage of the approach is that it enables identification of the primary self-harm method with an accuracy of 95%, supporting more granular surveillance beyond binary classification.

---


### 643. [SN-WER: Script-Normalized WER for Multi-Script Indic ASR Evaluation](https://arxiv.org/abs/2606.02548)

**<font color=#1a73e8>作者：</font>** Priyaranjan Pattnayak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word Error Rate (WER) is the dominant metric for automatic speech recognition (ASR), but it can overestimate errors when references and hypotheses encode the same words in different scripts. This issue is common in multilingual settings where ASR models may emit romanized text. We propose Script-Normalized WER (SN-WER), a training-free, evaluation-only scoring method that transliterates both reference and hypothesis text into a language-specific canonical script before computing WER. We evaluate SN-WER on 5 Indic languages, 2 datasets, and 3 ASR models. On curated FLEURS data, SN-WER reduces inflated model gaps by up to 12%, while on noisier Common Voice data the reductions are smaller or inconsistent, indicating genuine recognition weaknesses rather than only script mismatch. Controlled stress tests show a 67% attenuation of artificial romanization-induced WER inflation, while lexical-substitution controls show near-identical sensitivity to semantic errors, with Delta SN-WER / Delta WER approximately 1.09. SN-WER is robust to transliterator choice, normalization changes, and shows low token-collision rates below 0.1% in the evaluated Indic setting. We argue that SN-WER should be reported alongside WER and CER as a companion metric for script-insensitive ASR evaluation, especially when transcripts feed downstream search, indexing, or multilingual LLM pipelines.

---


### 644. [Modeling Depth Ambiguity: A Mixture-Density Representation for Flying-Point-Free Depth Estimation](https://arxiv.org/abs/2606.02552)

**<font color=#1a73e8>作者：</font>** Siyuan Bian, Congrong Xu, Jun Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advances in depth estimation, flying points remain a persistent failure mode: near object boundaries, depth estimators often predict spurious 3D points in the empty space between foreground and background surfaces. We trace this artifact to a standard modeling choice: assigning each pixel a single depth hypothesis. At boundaries, a pixel can straddle a foreground and a background surface, so its true depth is ambiguous between the two. A model that predicts a single depth cannot keep both possibilities, so training instead pulls the prediction toward an intermediate depth that lies on neither surface. We address this with MDA, a mixture-density representation that lets the model predict multiple depth hypotheses and their associated probabilities for each pixel. Near boundaries, different hypotheses can align with different surfaces, and the decoded depth is selected from one of these hypotheses rather than placed in the empty space between them. Across different backbones, MDA substantially improves boundary reconstruction and largely removes flying-point artifacts even under severe input blur, while adding negligible runtime overhead. The same mixture-density framework naturally extends to transparent objects, where it predicts multiple depth layers at transparent pixels, and to sky regions, where a dedicated component separates the unbounded sky from finite-depth regions, producing flying-point-free skylines. Project Page: this https URL.

---


### 645. [HERO'S JOURNEY: Testing Complex Rule Induction with Text Games](https://arxiv.org/abs/2606.02556)

**<font color=#1a73e8>作者：</font>** Anshun Asher Zheng, Kanishka Misra, David I. Beaver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce HERO'S JOURNEY, a benchmark for rule induction in goal-directed episodic tasks, where agents must infer hidden rules from demonstrations and act on them through multi-step execution. HERO'S JOURNEY covers eight tasks across attribute and procedural induction families, each with four structural rule forms, controllable lexical grounding, and identifiability conditions. Evaluating state-of-the-art LLMs, we find that models show evidence of rule induction, but the ability is limited and uneven across tasks. Meanwhile, process execution adds an execution bottleneck for models, whereas surface semantics has minimal effect. Induction-specific steering methods improve performance on attribute tasks but show no reliable gains on procedural tasks, suggesting the gap in procedural induction remains an open challenge.

---


### 646. [IntraShuffler: A Privacy Preserving Framework for Heterogeneous DP Federated Learning](https://arxiv.org/abs/2606.02563)

**<font color=#1a73e8>作者：</font>** Farhin Farhad Riya, Olivera Kotevska, Jinyuan Stella Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous Differential Privacy (HDP) in Federated Learning (FL) allows clients to select individual privacy budgets ($\varepsilon_i$) according to institutional policies and data sensitivity. In practice, many HDP-FL systems employ $\varepsilon$-aware server aggregation to improve model utility by re-weighting client updates according to their declared privacy budgets. However, gradient updates in FL retain structural patterns induced by non-independent and identically-distributed (non-IID) data, and these additional signals exposed by $\varepsilon$-aware aggregation create new opportunities for inference by an honest-but-curious server. In this work, we first show that a server equipped with gradient denoising and surrogate modeling can mount a \emph{Privacy Inference Attack} that infers distributional attributes of clients and links updates from the same client across training rounds, measured via surrogate inference accuracy and linkage success, under realistic knowledge constraints.
The Shuffle-Model has been widely studied as a defense against such inference risks by anonymizing update sources, but it is fundamentally incompatible with HDP-FL $\varepsilon$-aware aggregation. To address this challenge, we propose \textbf{IntraShuffler}, a middleware defense framework designed for HDP-FL systems. IntraShuffler introduces a privacy-aware shuffling mechanism that groups clients into privacy-compatible buckets and performs parameter-level shuffling within each bucket to disrupt persistent gradient structure while preserving $\varepsilon$-aware aggregation. Experiments across four different datasets show that IntraShuffler reduces gradient recoverability by over 60% and decreases surrogate inference accuracy from 0.78 to 0.33 while maintaining comparable model utility across multiple FL aggregation rules.

---


### 647. [VLMs are Good Teachers for Video Reasoning via Adaptive Test-Time Optimization](https://arxiv.org/abs/2606.02564)

**<font color=#1a73e8>作者：</font>** Junhao Cheng, Liang Hou, Tianxiong Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recent "Reasoning with Video" paradigm utilizes Video Generation Models (VGMs) to generate temporally coherent visual trajectories to complete reasoning tasks. Although state-of-the-art VGMs excel at visual quality, they often struggle to understand and follow task-specific rules, leading to logical failures across diverse reasoning scenarios. Existing efforts try to utilize Vision-Language Models (VLMs) as problem pre-solvers to produce or refine textual guidance for the VGM. However, textual descriptions fail to capture intricate spatiotemporal details, and VGMs often struggle to faithfully execute fine-grained or long-tail instructions even with a valid plan. While VLMs struggle as solvers, they possess strong perception capabilities to evaluate process-constraint satisfaction and final-goal achievement. Leveraging this strength, we introduce a paradigm shift that transitions the role of VLMs to "teachers". Specifically, a VLM teacher extracts task-specific rules to formulate differentiable rewards, guiding a VGM Reasoner via test-time online optimization of a lightweight LoRA module. This strategy enables adaptive test-time optimization and extends the reasoning capabilities beyond the VGM's intrinsic boundaries. Evaluations on symbolic (VBVR-Bench) and general-purpose (RULER-Bench) video reasoning benchmarks show that the proposed method yields a 16.7-point average performance gain, outperforming the VLM-as-Solver paradigm (+0.4 points) and Best-of-N scaling (+2.2 points) by a large margin at comparable test-time cost. These findings reveal that integrating VLMs as test-time teachers offers a promising paradigm for achieving generalizable video reasoning. Project Page: this https URL

---


### 648. [Policy-based Foveated Imaging and Perception](https://arxiv.org/abs/2606.02565)

**<font color=#1a73e8>作者：</font>** Howard Xiao, Jan Ackermann, Boyang Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-high-resolution image sensors offer the potential to capture fine spatial details critical for many visual perception tasks, but acquiring and processing all pixels at full resolution is often infeasible under realistic bandwidth, latency, and power constraints. Existing approaches address this challenge through acquisition strategies such as spatial or temporal downsampling, which irrevocably discard information before task relevance can be assessed. In this work, we introduce a real-time, predictive, and task-aware foveated imaging system that operates directly at image acquisition time. Leveraging emerging dual-stream sensor architectures, our method dynamically allocates limited pixel bandwidth to task-relevant regions of interest while maintaining a low-resolution global context. We formulate foveated acquisition as a sensor attention policy-learning problem, in which past observations guide actions that determine future measurements, closing the perception-acquisition loop. Through extensive simulation across multiple perception tasks, we demonstrate that our approach achieves high task performance under strict pixel budgets and significantly outperforms relevant baselines operating at the same bandwidth. We further validate our system on a 200-megapixel dual-stream sensor, capturing real-world videos under realistic bandwidth and latency constraints, demonstrating the practical feasibility of task-driven, acquisition-time foveated imaging.

---


### 649. [ClinEnv: An Interactive Multi-Stage Long Horizon EHR Environment for Agents](https://arxiv.org/abs/2606.02568)

**<font color=#1a73e8>作者：</font>** Yuxing Lu, Yushuhong Lin, Wenqi Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical practice is not the selection of an answer from enumerated options: a physician gathers heterogeneous information incrementally and commits to sequential, irreversible decisions under uncertainty. Static benchmarks cannot probe and existing interactive medical benchmarks each compromise on at least one of them. We present ClinEnv, an interactive benchmark that evaluates LLMs as attending physicians over real inpatient admissions under a paradigm we term Longitudinal Inpatient Simulation. Each case is automatically constructed into an ordered sequence of decision stages; at every stage the model must actively query four specialized agents before committing to medications, procedures, and diagnoses. ClinEnv scores both what the model decides, through deterministic ontology-grounded matching, and how it gathers information. Across seven models, the strongest reaches only 0.31 decision F1, and outcome quality is sharply decoupled from process quality. Difficulty concentrates in management decisions and later stages, where models recover discharge diagnoses far more reliably than management actions (0.51 vs. 0.17 F1) and continue to issue redundant queries as cases progress. ClinEnv makes this information-acquisition gap, invisible to outcome-only evaluation, directly measurable.

---


### 650. [VISReg: Variance-Invariance-Sketching Regularization for JEPA training](https://arxiv.org/abs/2606.02572)

**<font color=#1a73e8>作者：</font>** Haiyu Wu, Randall Balestriero, Morgan Levine  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning methods prevent embedding collapse via modeling heuristics or explicit regularization of the embedding space. Among the latter, VICReg decomposes regularization into variance and covariance objectives, offering flexibility and interpretability. However, covariance captures only second-order statistics -- encouraging decorrelation but failing to enforce the full distributional shape needed for stable training. Sketching-based methods such as SIGReg address this by aligning embeddings to an isotropic Gaussian, but lack flexibility and suffer from vanishing gradients under collapse. We propose Variance-Invariance-Sketching Regularization (VISReg), which replaces covariance with a Sliced-Wasserstein-based sketching objective that enforces full distributional shape, while retaining a variance term for scale control. By decoupling scale and shape, VISReg combines VICReg's flexibility with the distributional rigor of sketching methods, providing robust gradients even under collapse. We show that VISReg scales linearly, outperforms existing regularization on low-quality datasets, and is resilient to long-tailed and low-rank regimes. Pre-trained on ImageNet-1K, VISReg achieves state-of-the-art performance on out-of-distribution datasets. Pre-trained on ImageNet-22K, it matches DINOv2's OOD performance despite the latter using 10x more data (LVD-142M). Project and code: this https URL.

---


> [!TIP]
> 当前位于：**601-650**（第 13/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
