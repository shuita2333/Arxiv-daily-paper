# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

---

### 301. [Q-DEQ: Discrete Solving and Quantization for Deep Equilibrium Models in Time Series Forecasting under Edge Deployment Coding Constraints](https://arxiv.org/abs/2609.24042)

**<font color=#1a73e8>作者：</font>** Ruotong Yang, Hongdong Zhu, Qi Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge deployment motivates forecasting models with compact parameter storage and low-bit representations. Deep equilibrium models (DEQs) obtain implicit depth by repeatedly applying a shared layer, reducing the parameter cost of explicit layer stacking. Their usual Anderson solver, however, searches for update coefficients in the continuous real domain. We propose Q-DEQ, which formulates local updates in DEQ forward solving as discrete optimization problems. Candidate directions are constructed from the current state and iteration history, and a local quadratic residual model is used to evaluate their combinations. Binary encoding of the direction coefficients yields a quadratic unconstrained binary optimization (QUBO) problem that can be solved by simulated annealing (SA) or a coherent Ising machine (CIM). After fixed-point solving, a re-forward pass applies W8A8 fake quantization to the shared layer's weights and activations. We evaluate Q-DEQ with an iTransformer backbone on five multivariate time series forecasting datasets. Relative MSE differences from the explicit multi-layer baseline range from $-1.16\%$ to $+2.90\%$, with lower MSE on two datasets. DEQ parameter sharing reduces parameter counts by factors of $1.80\times$--$3.82\times$; combined with W8A8, static weight storage is reduced by factors of $4.3\times$--$12.8\times$. Local QUBO problems solved using CPU-based SA and the Kaiwu CIM physical backend produce closely matching downstream forecasts. These results establish local discrete solving as a viable component of DEQ time series forecasting and provide a route for executing fixed-point updates through different combinatorial optimization backends.

---


### 302. [U-PEN Mamba: Progressive Expansion with Selective State-Space Modeling for Efficient Retinal Vessel Segmentation](https://arxiv.org/abs/2609.24049)

**<font color=#1a73e8>作者：</font>** Abel A. Reyes-Angulo, Sidike Paheding, Vijayan K. Asari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate retinal vessel segmentation is important for computer-aided ophthalmic analysis, yet thin vessels, low contrast, and severe foreground-background imbalance remain challenging for encoder-decoder networks. This paper presents U-PEN Mamba, a U-shaped retinal vessel segmentation architecture that couples progressive nonlinear feature expansion with selective state-space modeling. The proposed network enriches local vessel responses with progressive expansion, models long-range spatial dependencies through a Mamba Global Context (MGC) block with linear sequence complexity, and uses attention-based decoder fusion to recover fine vascular boundaries. We evaluate U-PEN Mamba on CHASE DB1 and DRIVE using a consistent patch-based preprocessing pipeline and compare it with convolutional, attention-based, transformer-based, and Mamba-based segmentation baselines. U-PEN Mamba obtains the best mean intersection over union among the compared methods, achieving 0.8394 on CHASE DB1 and 0.8221 on DRIVE, with Dice scores of 0.8187 and 0.8078, respectively, using 21.6M trainable parameters. Ablation studies show that the MGC block contributes the largest gain over the U-Net baseline, while projection dimension and state size provide practical accuracy-efficiency control. These results indicate that selective state-space modeling is a promising global-context mechanism for parameter-efficient retinal vessel segmentation. Code is available at: this https URL.

---


### 303. [Vision Transformers versus convolutional neural networks for fine-grained orchid genus identification in a species-rich, data-poor flora: a controlled benchmark on the Orchidaceae of New Guinea](https://arxiv.org/abs/2609.24064)

**<font color=#1a73e8>作者：</font>** Reza Saputra, Diah Harnoni Apriyanti, André Schuiteman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> New Guinea is the world's richest island flora (~2,856 orchid species), yet most species are represented by only a handful of photographs, far fewer than direct species-level classification requires. Methods for fine-grained identification in such species-rich, data-poor floras are needed, and it remains unclear which backbone architecture and pretraining strategy best support them. We built a two-stage system that first predicts the genus of a query photograph, then retrieves visually similar reference images of candidate species using FAISS. We compared four pretrained backbones -- two Vision Transformers (ViTs; DINOv2, BioCLIP 2) and two CNNs (ConvNeXt V2-L, EfficientNetV2-L) -- fine-tuned under an identical protocol on a fixed, species-stratified partition of 16,701 photographs spanning 120 genera and 1,350 species, assessing accuracy, calibration, error structure, species retrieval, and open-set detection of novel genera. DINOv2 attained the best genus performance (macro top-1 66.9%, 95% CI 63.7-70.6; global top-1 88.9%); both ViTs outranked both CNNs, and general-purpose self-supervised pretraining (DINOv2) outperformed domain-matched biological pretraining (BioCLIP 2) by 7.1 points of macro top-1. Errors concentrated on two abundant genera acting as error attractors. DINOv2 embeddings achieved species Recall@5 of 86.6% and genus Recall@5 of 98.7%; temperature scaling reduced every backbone's Expected Calibration Error to about 0.03; and a distance-based open-set gate flagged unseen genera (mean AUROC 0.958). A self-supervised Vision-Transformer backbone combined with embedding retrieval is an effective, deployable strategy for fine-grained identification in species-rich, data-poor floras. The system is released as an open web application (the New Guinea Orchid Identifier), offering a practical template for other hyperdiverse, under-documented taxa.

---


### 304. [Bridging Reconstruction and Generation: A Latent Distribution Perspective on Evaluation and Improvement](https://arxiv.org/abs/2609.24088)

**<font color=#1a73e8>作者：</font>** Xianghong Fang, Wenjie Shu, Tongda Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In latent generative models, reconstruction quality is often assumed to correlate with generative performance. However, reconstruction FID (rFID) can exhibit weak or even negative correlation with generation FID (gFID). We attribute this discrepancy to a latent distribution mismatch: reconstruction evaluates the decoder on encoder-induced latents, whereas generation uses the same decoder on latents produced by the generative model. To characterize this shift, we introduce generation-aware reconstruction (GAR), which constructs a continuous trajectory from standard reconstruction toward generation by perturbing encoder latents with noise and denoising them through the generative model before decoding. GAR probes the decoder behavior along this trajectory, making the transition from encoder to generation-time latent distributions observable and diagnosable. The resulting trajectory-based diagnostic, GAR-FID, exhibits strong empirical correlation with gFID across diverse tokenizers and scales. Importantly, intermediate GAR latents become more generation-aware while preserving correspondence with their source images, thereby retaining paired supervision that is absent for fully generated latents. This correspondence enables decoder adaptation on intermediate GAR latents, consistently improving generative quality across model scales. Overall, latent distribution mismatch provides a useful perspective for evaluating and improving latent generative models.

---


### 305. [FlashBoB: I/O-Efficient Exact Backward-over-Backward for Softmax Attention](https://arxiv.org/abs/2609.24089)

**<font color=#1a73e8>作者：</font>** Anthony Givans, Michael Crawshaw, Mingrui Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer models built on the attention mechanism have become a central building block in modern deep learning, yet softmax attention remains a major bottleneck for long-context workloads. While FlashAttention makes the forward and first backward passes I/O-efficient, it does not support backward-over-backward (BoB), which enables exact differentiation through the backward pass for applications such as second-order optimization, test-time training, gradient-based memory, and meta-learning. Existing BoB implementations either materialize large intermediate tensors or exhaust GPU memory at long sequence lengths. We present FlashBoB, an exact, I/O-efficient algorithm for BoB in softmax attention that keeps computation within on-chip tiles and avoids all $N \times N$ intermediate tensors, where $N$ is the sequence length. The key insight is a hierarchical affine structure in the softmax double backward: two row-wise scalars determine all outputs through affine transformations. This yields a two-pass schedule with bounded on-chip static random-access memory (SRAM) usage and minimal off-chip high-bandwidth memory (HBM) traffic. FlashBoB achieves $\Theta(N^2 d^2/M)$ HBM traffic ($d$ is the head dimension and $M$ is the memory size) and, within the standard FlashAttention-style score-recomputation model, matches the inherited large-cache lower bound for exact forward attention. Empirically, it scales exact attention BoB to $N=262\text{K}$ on a single A100 80GB GPU, where prior PyTorch exact baselines fail by $N=16\text{K}$, and is up to $6.3\times$ faster than FlashBack. These results make exact second-order attention practical at long-context sequence lengths where prior implementations cannot run efficiently.

---


### 306. [HDND: Hierarchical Dynamic Neural Decoding for Multilingual Word/Character Retrieval from Non-Invasive Brain Recordings](https://arxiv.org/abs/2609.24095)

**<font color=#1a73e8>作者：</font>** Yueyang Li, Shuran Chen, Wai Ting Siok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While deep learning has enabled language decoding from intracranial brain recordings, extending this capability to non-invasive recordings remains an unresolved challenge. Decoding individual words from non-invasive brain recordings is particularly difficult, as word-level neural evidence is weak, temporally distributed, and entangled with acoustic, lexical, and semantic structure. Existing retrieval pipelines often collapse these factors into a single representation, potentially discarding information available at intermediate temporal scales. Here, we introduce Hierarchical Dynamic Neural Decoding (HDND), a hierarchical dynamic decoding framework that treats word decoding as structured refinement rather than flat label retrieval. HDND combines intermediate neural representations, contextual semantic predictions, and, for selected reading conditions, an auxiliary character-form objective. We evaluate HDND across seven electroencephalography (EEG) and magnetoencephalography (MEG) datasets spanning English, Dutch, Mandarin, and Cantonese listening, reading, and reading-aloud conditions. Across the nine-condition word-retrieval benchmark, the proposed HDND yields a higher participant-averaged balanced Top-10 point estimate than the matched contextual word-decoding baseline in every condition and achieves the highest mean among all compared methods in eight of nine conditions. Across the same nine matched conditions, HDND also yields higher token-micro and pooled word-macro Top-10 point estimates in every setting. Sentence retrieval favors HDND in eight of nine conditions, while auditory speech-segment retrieval is mixed across the six listening conditions. These results show that hierarchical residual refinement can improve multilingual word retrieval from heterogeneous non-invasive brain recordings.

---


### 307. [When More Evidence Hurts: Publication-Bias Drift and Principled Stopping for Biomedical Causal Search](https://arxiv.org/abs/2609.24101)

**<font color=#1a73e8>作者：</font>** Fred Sun, Shangqi Guo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated biomedical evidence synthesis depends on retrieving published studies, but the biomedical literature is systematically skewed toward positive findings. Deeper retrieval can therefore make a system \emph{more} likely to falsely infer benefit when the true effect is null. We formalise this phenomenon as \emph{evidence drift} and prove that, under a standard publication-bias model, the false-positive probability on null-effect queries follows a strictly increasing large-sample envelope in retrieval depth, approaching one. Empirically, on a held-out test set of 140 Cochrane-derived queries, drift rises monotonically from 7.9\% to 15.7\% as the retrieval budget grows from 3 to 20 steps, and concentrates in the null-effect class. We present DACG-agent, a drift-aware causal-graph agent that incrementally builds a causal knowledge graph from PubMed abstracts and applies a two-layer stopping policy with complementary roles: a KL-divergence monitor that detects posterior convergence (the accuracy layer), and a Bradley--Terry process reward model (PRM) whose online decline detection halts retrieval once evidence quality peaks (the efficiency layer). Against full-budget retrieval, DACG-agent reduces evidence drift from 15.7\% to 6.4\% and improves null-effect accuracy by 21 percentage points (40.0\%$\to$61.4\%) while using 67\% fewer retrieval steps; overall accuracy rises from 61.4\% to 69.3\% (95\% CI 61--77). A simulation confirms the drift result transfers from the analysed vote-counting aggregator to the deployed noisy-OR one.

---


### 308. [Reinforcement Learning under State and Outcome Uncertainty: A Foundational Distributional Perspective](https://arxiv.org/abs/2609.24103)

**<font color=#1a73e8>作者：</font>** Larry Preuett, Qiuyi Zhang, Muhammad Aurangzeb Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many real-world planning tasks, agents must tackle uncertainty about the environment's state and variability in the outcomes of any chosen policy. We address both forms of uncertainty as a first step toward safer algorithms in partially observable settings. Specifically, we extend Distributional Reinforcement Learning (DistRL)-which models the entire return distribution for fully observable domains-to Partially Observable Markov Decision Processes (POMDPs), allowing an agent to learn the distribution of returns for each conditional plan. Concretely, we introduce new distributional Bellman operators for partial observability and prove their convergence under the supremum p-Wasserstein metric. We also propose a finite representation of these return distributions via psi-vectors, generalizing the classical alpha-vectors in POMDP solvers. Building on this, we develop Distributional Point-Based Value Iteration (DPBVI), which integrates psi-vectors into a standard point-based backup procedure-bridging DistRL and POMDP planning. By tracking return distributions, DPBVI lays the foundation for future risk-sensitive control in domains where rare, high-impact events must be carefully managed. We provide source code to foster further research in robust decision-making under partial observability.

---


### 309. [You Can Tell Who's Asking: What the Web's Questions Are Made Of, and Where They Come From](https://arxiv.org/abs/2609.24106)

**<font color=#1a73e8>作者：</font>** Calvin Zhou, Vincent McCloskey, Krishna Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Questions scraped from the web are used across academia and industry as a proxy for what people want to know. Across QA training data, retrieval benchmarks, and content strategy, questions on a page are assumed to reflect human intent. We test this assumption at scale by extracting 13.4B question occurrences across 110 FineWeb snapshots (2013-2025), and report three findings. First, you can tell who is asking: provenance (the host/page of questions) leaves a signal in question form, and a logistic model can separate genuine user questions from templated/manufactured ones at AUC 0.725 via length and surrounding context rather than question type, though only 0.554 against commerce FAQ writing. Second, question frequency does not measure demand: the most-frequent questions are boilerplate/templated (over 70% of the top thousand), so occurrence counts measure how often a string was published and not how often it was asked. Third, over twelve years the genuine share of occurrences fell by 79% (42-56% after controlling for crawl composition), with question length and context decreasing. We present the first diachronic, occurrence-level measurement of web question provenance, and find the crawlable web's questions have shifted from being asked by humans toward manufactured for machines to read.

---


### 310. [Adaptive Cortically Constrained EEG-Vision Alignment for Zero-Shot Brain-to-Image Retrieval](https://arxiv.org/abs/2609.24109)

**<font color=#1a73e8>作者：</font>** Ye Wang, Haokun Ren, Wei Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot brain-to-image retrieval requires robust alignment between noisy EEG responses and visual representations. Existing EEG-vision alignment methods often operate in sensor space and apply fixed visual supervision to all responses, ignoring both spatial mixing in scalp EEG and response-wise variability in alignment reliability. We propose an adaptive cortically constrained EEG-vision alignment method for zero-shot brain-to-image retrieval. The method reconstructs EEG responses into predefined ROI-level source-pattern representations and encodes them with a Neuro-ROI Attention Encoder. To handle response-wise variability, we introduce an evidence-based adaptive visual supervision strategy that weights detail-controlled visual targets using model-based alignment evidence. On THINGS-EEG, the proposed method achieves strong 200-way zero-shot retrieval performance, with ROI-level attribution providing post hoc interpretability of the learned source-pattern representations. These results show that cortically constrained representation learning and adaptive supervision can jointly support EEG-vision alignment for zero-shot brain-to-image retrieval.

---


### 311. [ProbeScout: Visual Analytics for Attribute-Guided Image Search](https://arxiv.org/abs/2609.24110)

**<font color=#1a73e8>作者：</font>** Yifan Lv, Yiyun Chen, Daojun Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Analysts often need to identify images that jointly satisfy multiple visual conditions, such as a crossroads with traffic lights at dusk, for model diagnosis, dataset curation, and targeted training. Embedding-based retrieval can rank the large gallery efficiently, but a visually dominant condition can obscure weaker conditions, and a single similarity score does not enforce the required conjunction. Visual question answering (VQA) can explicitly verify conditions, yet exhaustively applying it to the full gallery is costly, especially when analysts refine their query. These limitations motivate keeping humans in the loop at the attribute level, where analysts can quickly build evidence for each condition and reuse it when the request changes. We therefore present ProbeScout, a visual analytics system that supports this loop. It first builds composable attribute probes from sparse VQA labels and fuses them into a conjunction-aware initial ranking. Coordinated views support rapid screening, near-miss diagnosis, and on-the-fly subset construction by filtering and combining these probe outputs. Analysts provide lightweight attribute- and query-level feedback, which drives staged refinement of fusion weights while keeping the probes fixed. These verified attributes can be reused for future queries. We evaluate ProbeScout on 17 retrieval tasks across three datasets, showing improved retrieval over embedding baselines. A separate 10-task comparison achieves higher task-macro AP and F1 than exhaustive VQA while labeling at most 2% of the gallery images. Two case studies further demonstrate how ProbeScout supports interactive analysis and refinement in realistic workflows.

---


### 312. [SPeaR: Test-Time Adaptation with Steering Primitives for Realigning Representations](https://arxiv.org/abs/2609.24111)

**<font color=#1a73e8>作者：</font>** Muhammad Sudipto Siam Dip, Ali Etemad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) addresses distribution shift using only unlabeled test data. Existing methods typically adapt pretrained models by updating their parameters, limiting both what is adapted and where adaptation can occur within the network. We instead keep the pretrained network frozen and steer its intermediate representations. We introduce SPeaR (Steering Primitive for Realigning Representations), which inserts lightweight learnable modules at stage boundaries and optimizes them directly from the test stream, requiring neither source data nor supervised warm-up. Each primitive is optimized using a gated objective that reduces uncertainty only when adaptation is beneficial, along with a diversity regularizer to prevent collapse, and a multi-depth anchor to stabilize adaptation. We show that steering early representations is the most effective strategy, and that the same primitive transfers across convolutional and Transformer architectures. Across CIFAR-10-C, CIFAR-100-C, and ImageNet-C, SPeaR consistently matches or outperforms methods that adapt orders of magnitude more parameters, remains robust across a wide range of batch sizes, and preserves source-domain performance during continual adaptation.

---


### 313. [Patch-to-Global: Random Patch Diffusion for Globally Consistent Megapixel Artifact Inpainting in Whole Slide Images](https://arxiv.org/abs/2609.24116)

**<font color=#1a73e8>作者：</font>** Hyeseong Lee, Eunsu Kim, D M Bappy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although deep learning has advanced Whole Slide Image (WSI) Analysis, tissue artifacts like bubbles and folds often cause silent failures by concealing essential morphology. Current pathology image restoration methods are mostly restricted to small patches, struggling to maintain global structural coherence at a megapixel scale. We introduce RestorePath, a framework for globally consistent megapixel scale inpainting that reconstructs diagnostic structures in histological image to prevent incorrect high-confidence predictions and lower error rates. Our model utilizes a Latent Diffusion Model (LDM) conditioned on Pathology Foundation Model (PFM) embeddings, integrating Large Kernel Attention (LKA) to manage long-range dependencies during random patch diffusion. Enhanced by Distance-Weighted Interpolation (DWI) and an Adaptive Guidance Scale (AGS), RestorePath ensures structural consistency and fidelity by modulating information from surrounding patches. Evaluations across TCGA-BRCA, BACH, and Camelyon16 datasets for images ranging from 512 to 4608 pixels demonstrate state-of-the-art performance in maintaining histological consistency. RestorePath significantly improves downstream Computational Pathology (CP) tasks, outperforming both raw artifact images and the conventional Detect-and-Discard (D&D) approach. The code is available at this https URL

---


### 314. [PAC-Bayesian Meta-Learning for Few-Shot Identification of Linear Dynamical Systems](https://arxiv.org/abs/2609.24117)

**<font color=#1a73e8>作者：</font>** Chenfeng Huang, George Michailidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying linear time-invariant (LTI) dynamical systems is challenging when trajectories are short, noisy, or high-dimensional. Traditional system identification typically treats each system independently and cannot exploit shared structure across related systems. We propose PBML-LTI, a PAC-Bayesian meta-learning framework for few-shot LTI system identification that learns a transferable prior over task-specific dynamics while preserving task heterogeneity. Each task corresponds to an unknown LTI system, and the meta-learner uses training trajectories to learn a data-dependent prior over transition matrices. For a new system with limited data, PBML-LTI performs Bayesian adaptation under this prior to obtain a task-specific posterior, providing accurate estimates and principled uncertainty quantification.
A key challenge is temporal dependence, since LTI trajectories violate the i.i.d. assumptions underlying most PAC-Bayes meta-learning analyses. We address this with a martingale PAC-Bayes analysis for dependent trajectory losses and derive a support-query predictive-risk bound that motivates a fit-KL meta-training objective. The bound clarifies the roles of empirical fit, posterior complexity, and prior quality in few-shot adaptation under sequential dependence. We further derive corollaries for transition-matrix recovery and multi-step trajectory prediction, connecting uncertainty-aware meta-identification with finite-sample guarantees for dependent dynamical data.

---


### 315. [Positive Pair Geometry Matters: Optimal Transport for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2609.24125)

**<font color=#1a73e8>作者：</font>** Akshit Nanda, Shahzad Ahmad, Ram Prasad Padhy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive self-supervised learning has achieved strong performance by learning representations from multiple augmented views of the same image. However, most existing methods construct positive pairs using independently sampled stochastic augmentations, which may alter semantic content and ignore the intrinsic geometry of the data distribution. In this work, we propose OTCLR, an optimal transport-aware framework for contrastive learning representations that generates geometry-consistent positive samples. Instead of directly contrasting two randomly augmented views, we construct intermediate views between the original image and its augmented variants through entropic optimal-transport displacement interpolation. These transport-interpolated samples serve as positive views that better preserve image structure while explicitly modeling spatial distributional geometry. To further promote smooth representation learning, we evaluate auxiliary Sinkhorn regularization terms that encourage transport-interpolated views to remain consistent with their endpoint images. The proposed method can be incorporated into standard contrastive learning pipelines without modifying the encoder architecture. Experiments on multiple benchmark datasets show that our approach improves representation quality and transfer learning performance compared with conventional augmentation-based contrastive learning baselines.

---


### 316. [Action-Slot: Structured Action-Centric Representation Learning for Multi-Agent Atomic Activity Understanding](https://arxiv.org/abs/2609.24127)

**<font color=#1a73e8>作者：</font>** Yu-Ho Chang, Chi-Hsi Kung, Yi-Hsuan Tsai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Atomic activity understanding aims to recognize and localize structured traffic behaviors that jointly encode motion patterns and their grounding in road topology. Unlike conventional action recognition, atomic activities are multi-agent, multi-label, and topology-aware: multiple activities co-occur while many agents remain inactive. We introduce Action-Slot, a structured action-centric representation learning framework. Slot attention is widely used for object-centric decomposition, but its permutation-invariant design and object-level inductive bias are misaligned with atomic activity semantics. We reformulate slot learning as structured activity decomposition through three designs: (1) category-aligned action slots that anchor slots to predefined activity categories, (2) parallel spatio-temporal slot updating for holistic video-level reasoning, and (3) background and negative-slot regularization that enforces competition between foreground activities and irrelevant regions. Together these establish an activity-centric inductive bias that disentangles concurrent and asynchronous activities directly from raw video. Beyond recognition, the learned representations encode transferable spatio-temporal grounding signals. We further propose an attention-difference-based pseudo mask selection framework that suppresses false positives by measuring attention changes before and after candidate region removal, enabling weakly supervised localization without dense annotations. To support systematic evaluation, we introduce TACO, a balanced synthetic dataset with full atomic activity coverage and pixel-level annotations. Experiments on OATS, TACO, and annotated nuScenes show superior recognition, strong sim-to-real transfer, and state-of-the-art weakly supervised localization.

---


### 317. [Monet: Measuring the Ecosystem of Open-Source Text-to-Image Models Tailored for Harmful Services](https://arxiv.org/abs/2609.24134)

**<font color=#1a73e8>作者：</font>** Zihao Wang, Jiacen Xu, Zilong Lin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The open-source text-to-image (T2I) ecosystem enables rapid model development and sharing, but also hosts models intentionally tailored for harmful services, which we call Monets. Prior work has examined specific types of harmful T2I models on individual platforms, but a Monet does not exist in isolation. The broader Monet ecosystem, spanning model characteristics, cross-platform propagation, governance evasion, monetization, and downstream deployment, remains poorly understood.
In this study, we present the first systematic, ecosystem-level measurement of Monets. Grounded in the policies of real-world model hubs, we construct a taxonomy of ten harmful service categories and identify 23,947 Monets across eight major T2I model hubs, with the most popular exceeding 19 million downloads. While some developers employ anti-theft mechanisms against unauthorized re-uploading, Monets propagate across platforms at scale, with 40.76% mirrored across hubs. Such propagation further enables governance evasion via cross-platform archiving, keeping 11.99% of Monets accessible after bans on their original platforms, alongside other evasion strategies including keyword obfuscation and model-level safeguard circumvention. Monets also anchor coordinated commercial campaigns---one spanning 668 models with 914 completed commissions and another advertising gray-market account-farming service---and reach users through GitHub projects and inference APIs, raising downstream child safety concerns. These findings expose the limitations of platform-siloed defenses and highlight the need for cross-platform threat intelligence, coordinated governance, and technical safeguards.

---


### 318. [The Visual Target Matters: Learning across the Visual Hierarchy for Brain-to-Image Retrieval](https://arxiv.org/abs/2609.24136)

**<font color=#1a73e8>作者：</font>** Ye Wang, HaoKun Ren, Hong Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain-to-image retrieval seeks to identify the visual stimulus that elicited a non-invasive neural response. Candidate images are typically represented by pretrained vision models, whose internal representations vary in abstraction across depth. Existing methods usually train the neural encoder to recover a fixed final-layer visual target. Under this formulation, the visual hierarchy is reduced to a single prescribed endpoint, preventing representations at other depths from directly shaping the visual target. This limitation motivates learning how information across visual depths should contribute to the retrieval target. To this end, we introduce NeuroGlyph, which learns a trial-independent visual target from multiple depths of a frozen visual backbone. NeuroGlyph decomposes the target into factor-specific subspaces. Each subspace learns an image-conditioned allocation over visual depth. The resulting subspaces are fused into a single embedding for retrieval. Across THINGS-EEG and THINGS-MEG, NeuroGlyph outperforms final-layer supervision in all controlled comparisons. It also surpasses the post hoc best fixed-layer oracle in three of four comparisons. Parameter-matched ablations support both factorized target construction and image-conditioned depth allocation. Under comparable 200-way retrieval protocols, NeuroGlyph achieves the strongest system-level performance in six of eight reported metrics. These results support learning retrieval targets across the visual hierarchy rather than prescribing one visual depth.

---


### 319. [STAR: Scene- and Task-Aware 4D Radar Preprocessing Towards End-to-End Cognitive Radar](https://arxiv.org/abs/2609.24151)

**<font color=#1a73e8>作者：</font>** Seung-Hyun Song, Dong-Hee Paek, Seung-Hyun Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Four-dimensional (4D) Radar has emerged as a key sensor for environmental perception, providing range, azimuth, elevation, and Doppler measurements while remaining robust to illumination changes and adverse weather conditions. However, conventional Radar preprocessing methods, such as constant false alarm rate (CFAR) detection, select measurements primarily based on signal-level criteria and may therefore discard information valuable for downstream perception during point cloud generation. In addition, existing 4D Radar perception pipelines typically optimize Radar data processing and downstream perception independently, preventing task objectives from directly guiding the preprocessing stage. To address these limitations, we propose a Scene- and Task-Aware Radar (STAR) Preprocessor together with an end-to-end training framework. The STAR Preprocessor incorporates scene context and downstream task objectives to generate task-relevant Radar points, enabling the Radar representation to be optimized directly for perception. On the K-Radar benchmark, the proposed method achieves 74.3 AP, outperforming the previous state of the art by 5.6 AP points. Furthermore, applying the task-relevant points generated by STAR to various existing 3D detectors improves detection performance in most evaluation settings and yields an overall positive average gain over point clouds produced by conventional preprocessing.

---


### 320. [Relightable 3D Avatar Reconstruction with Semantic-Adaptive Motion-Illumination Responses](https://arxiv.org/abs/2609.24158)

**<font color=#1a73e8>作者：</font>** Jiankuo Zhao, Xiangyu Zhu, Jijie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing expressive and relightable 3D head avatars from monocular videos remains challenging in computer vision, as it requires accurate modeling of both non-rigid facial motion and illumination-dependent appearance. Existing Gaussian avatar methods commonly rely on globally coupled representations, in which Gaussian primitives share a unified motion or illumination response model. Such uniform modeling neglects the distinct motion patterns and material/reflectance properties of different facial semantic regions, thereby limiting fine-grained animation accuracy and reducing relighting plausibility. To address this limitation, we propose SAMIRA, a 3D Gaussian avatar framework for semantic-adaptive motion-illumination response modeling. For motion response modeling, the Semantic-Adaptive Motion Response module rasterizes current-to-reference mesh displacements into a topology-consistent UV space and leverages facial semantics to route displacement features through semantic-specific modulators, predicting localized Gaussian geometric residuals beyond coarse mesh binding. For illumination response modeling, the Semantic-Adaptive Illumination Response module learns compact diffuse and specular response factors for each facial region, allowing Gaussians in different regions to adapt their illumination responses to novel environment lighting. These response factors are incorporated into deferred physically based shading, providing a lightweight approximation of semantic-dependent illumination effects. Extensive experiments on self-reenactment, cross-reenactment, and relighting demonstrate that SAMIRA improves both fine-grained expression reconstruction and relighting realism over existing methods.

---


### 321. [KEVGraph: Exploitation-Aware Dependency Vulnerability Remediation](https://arxiv.org/abs/2609.24164)

**<font color=#1a73e8>作者：</font>** Daniel Okumu Omondi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dependency scanning tools surface hundreds of vulnerabilities but provide no exploitation-aware ordering, leaving practitioners to decide which upgrades to perform first with no principled guidance. The dominant practice, ordering by CVSS severity, is structurally misaligned with active exploitation: in our npm corpus, 186 non-KEV vulnerabilities carry CVSS scores greater than 8, all outranking three CISA Known Exploited Vulnerability (KEV)-listed packages and causing CVSS-first tools to defer the first actively exploited fix by 17 upgrade actions. KEVGraph is an eight-stage pipeline that frames remediation as a KEV-aware set-cover problem: it constructs per-repository dependency graphs from lockfiles, joins them against OSV and the CISA KEV catalogue, and produces a minimum-cardinality upgrade plan ordered to eliminate actively exploited vulnerabilities as early as possible via exact Integer Linear Programming (ILP) or a KEV-aware greedy algorithm. Evaluated on 924 real-world npm repositories (1,046 vulnerabilities, 5 KEV-listed), the ILP planner achieves AUCCKEV = 0.997 versus a random-baseline mean of 0.663 (95 percent CI [0.519, 0.831], n = 30), resolves the first KEV vulnerability at plan step 1, and requires only 417 upgrade actions, 15.9 percent fewer than the random mean of 495.4. CVSS-first and Dependabot-style ordering are strictly dominated: they defer the first KEV fix to step 18 while requiring more actions (419 and 421, respectively). The framework generalises: Maven (1,200 repos) achieves AUCCKEV = 0.988 versus random mean 0.486; PyPI (300 repos) achieves AUCCKEV = 1.000. Each plan is accompanied by a machine-verifiable certificate enabling automated compliance verification under CISA BOD 22-01.

---


### 322. [Lightweight Pedestrian Head-Orientation Recognition Network for Safe Pedestrian-Vehicle Interaction](https://arxiv.org/abs/2609.24193)

**<font color=#1a73e8>作者：</font>** Yuanzhe Li, Yidi Huang, Xiaotong Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian head orientation recognition plays an important role in autonomous driving by providing valuable cues for understanding pedestrian attention and anticipating potential crossing behavior. However, reliable recognition in real-world traffic scenes remains challenging because pedestrian head regions are often captured at low resolution. To address this challenge, we propose a lightweight Low-Resolution Head Orientation Convolutional Neural Network (LRHO-CNN) for pedestrian head orientation recognition. We construct a new dataset by extracting pedestrian head images from multiple public datasets and manually annotating them into eight orientation categories. The collected images are systematically preprocessed and augmented to increase data diversity and better represent variations in illumination and image quality. The experimental analysis compares LRHO-CNN with three fine-tuned baseline models, namely ResNet-18, ResNet-34, and VGG-16. The results demonstrate that LRHO-CNN achieves the highest classification accuracy among the evaluated models. LRHO-CNN is further evaluated on the JAAD and PIE datasets, demonstrating its effectiveness in recognizing pedestrian head orientation in real-world traffic scenes and providing informative head-orientation cues that can support downstream pedestrian behavior and intention prediction.

---


### 323. [Vimarsha: Faithful ASR Evaluation for Indian Languages with Demographic Diversity, In-the-Wild Audio and Spelling Variations](https://arxiv.org/abs/2609.24199)

**<font color=#1a73e8>作者：</font>** Kaushal Santosh Bhogale, Srija Anand, Sadakopa Ramakrishnan Thothathiri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation benchmarks for Indian language automatic speech recognition (ASR) suffer from two systematic biases: optimistic scores from clean, controlled audio conditions, and pessimistic scores from overly rigid transcription standards that penalize valid linguistic variations. We introduce Vimarsha, a 100-hour benchmark spanning all 22 scheduled Indian languages, designed to address both distortions. Vimarsha combines demographically diverse on-field recordings with carefully mined in-the-wild audio selected for acoustic difficulty, alongside a lattice of variations framework that encodes multiple valid transcriptions per utterance. Evaluations of 10 state-of-the-art ASR models reveal substantial shifts in model rankings under realistic conditions, geographic and demographic performance disparities, and systematic failure modes across speaking rates and acoustic environments.

---


### 324. [SAFe: Segment-guided Aggregation of Feature Densities for Anomaly-aware Segmentation](https://arxiv.org/abs/2609.24204)

**<font color=#1a73e8>作者：</font>** Anja Delić, Jurica Runtas, Marin Oršić 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual segmentation systems encounter objects outside their training distribution during real-world deployment, hindering reliable autonomous systems that depend on scene parsing in the perception stage. Many recent methods address this by using self-supervised foundation models to train density estimators that yield low likelihood in anomalous image regions. Although promising, these methods suffer from poor feature semantics or they lack spatial consistency, both of which undermine critical downstream decisions. We address this problem with~\method, a generative method based on class-conditional density estimation over self-supervised representations. SAFe trains lightweight normalizing flows that produce class-conditional normalized likelihood estimates over frozen DINOv3 features. We combine density estimates from transformer features with density scores over multi-scale convolutional features to capture both global semantics and local detail. We introduce a method-agnostic post-processing step based on SAM3 that connects per-location likelihoods into spatially coherent segments while suppressing false positives, and enables instance-level anomaly detection without retraining. The post processing further distinguishes novel categories among anomalous objects by a similarity-based agglomerative clustering scheme. SAFe sets a new state of the art on the PANIC, OoDIS, SMIYC ObstacleTrack with strong performance on the ISSU benchmark.

---


### 325. [CoaG: Cylinders on a Grid: Coarse 3D Layout Control for Video Generation](https://arxiv.org/abs/2609.24208)

**<font color=#1a73e8>作者：</font>** Zhangsihao Yang, Mengyi Shan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We ask how little geometry a person has to draw to control both where people stand and where the camera moves in a generated video. Our answer is a ground plane and one cylinder per person. A user draws a grid on the ground, places one cylinder where each person should stand, moves the cylinders and the camera over 81 frames, and the model renders a photoreal video in which the people occupy the cylinders' positions, move as the cylinders move, and are seen from the drawn camera. Appearance comes from a text prompt and a background reference image; layout and motion come from the geometry. Because no dataset pairs such a signal with video, we build the pairs ourselves: an automatic engine writes 2000 captions from a combinatorial seed, generates a clip for each with a text-to-video model, and lifts every clip back to its geometry with person tracking, background inpainting, an agentic ground-mask loop, feed-forward multi-view reconstruction and a plane fit, with no real footage and no manual labels. A LoRA on Wan2.2-Fun-Control trained on 1935 such tuples follows drawn layouts and camera paths on hold-out clips: the generated people match the cylinders' count, order, position and height, the text changes who they are, the reference image changes where they are, and dolly-in, orbit, pan and crane paths are followed, dolly-out only weakly.

---


### 326. [Displacement Geometry Captures Platonic Shared Reality Across Models and Modalities](https://arxiv.org/abs/2609.24209)

**<font color=#1a73e8>作者：</font>** Chenming Shang, Yujin Tang, Jun Jie Ou Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Platonic Representation Hypothesis (PRH) claims that independently trained models converge on a shared statistical model of reality, yet recent work finds only weak pointwise similarity between models. In this paper, we show that what models share is not the location of samples in representation space, but the directions (displacement vectors) between them. Under a single orthogonal alignment--rotation and reflection only--these displacement vectors are substantially preserved across 44 independently trained vision and language encoders spanning modalities and asymmetric capability pairs, consistent with the PRH evidence. The samples' absolute positions are not, consistent with recent counter-evidence. Both arise from a single decomposition: representations split into a shared semantic component that is linearly aligned across models, and a private capability component that is not. We trace this geometry to concept-level structure: within a model, parent concepts are orthogonal to their child variation vectors; across models, concept displacements are parallel. Our theory falsifiably predicts (and experiments confirm) that fine-tuning preserves pointwise similarity but collapses displacement, and that relational distillation does the opposite.
A major implication is that, because semantics align linearly but capabilities do not, capabilities can be imported from one model to another using a single cached forward pass through the source. We call this Shadow Casting. As a proof of concept, our SHADOWCLIP instantiation outperforms strong fine-tuned baselines at orders of magnitude less compute. A cache can be released alongside open model weights, letting one model's capabilities be downloaded and imported into any number of other models without fine-tuning.

---


### 327. [Beyond Emotion Prompts: Fine-Grained Text-to-Image Generation Driven by Valence-Arousal-Dominance](https://arxiv.org/abs/2609.24215)

**<font color=#1a73e8>作者：</font>** Minglang Li, Yueyue Fang, Xieping Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although text-to-image models can accurately depict subjects and scenes, creators still struggle to specify the fine-grained emotions an image should convey without rewriting its content description. Natural language can suggest emotions, but it offers no control scale with stable meanings and ordered intensities. We propose EMOTRANS, which transforms psychologically grounded valence-arousal-dominance (VAD) coordinates into generation conditions that are independent of the content text and modulated across denoising stages, making emotional style a finely adjustable creative variable. To support this goal, we construct EMOVAD, an art-painting dataset that pairs objective content descriptions with separately collected emotional ratings from multiple annotators. We also coordinate emotional expression and content preservation through dual-branch training with a shared model. Objective and human evaluations show that the framework improves the accuracy of three-dimensional emotion control and produces perceptible, orderable continuous changes while maintaining competitive text alignment and image quality. This work provides a practical emotion-driven approach to image generation that extends objective content depiction to fine-grained emotional adjustment.

---


### 328. [DiaSeg: Diagonal Segment Extraction from DTW Paths for Interpretable Gait Analysis](https://arxiv.org/abs/2609.24223)

**<font color=#1a73e8>作者：</font>** Tresor Y. Koffi, Amel Hidouri, Corentin Legrand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic Time Warping (DTW) is the dominant approach for measuring similarity between time series, yet standard practice discards the optimal warping path after computing a single distance value, losing local alignment information most relevant to clinical diagnosis. We introduce DiaSeg, a framework that extracts diagonal segments from DTW paths with controlled breaks, characterizing each segment by five geometric features (effective length, interruption count, cost variation, temporal position, and path context), and enabling unsupervised pattern discovery without domain-specific feature engineering. Validated on 91 subjects across six clinical conditions (healthy aging, Parkinson's, Huntington's, ALS, brain tumor, and stroke), three findings emerge. First, diagonal segments form consistent unsupervised patterns (silhouette 0.33) aligned with biomechanical phase annotations, with label-based validation confirming near-perfect separation of healthy and pathological gait (ARI up to 0.986). Second, segments discriminate pathology at 69% (supervised) and 75% (patient-level clustering), with pathology manifesting through distributional shifts in segment length; combining segment and cycle-level features further improves classification to 91.7%. Third, while cycle-based methods achieve higher accuracy (91%), diagonal segments provide phase-specific interpretability unavailable in global representations, localizing where coordination breaks down within the gait cycle. DiaSeg thus transforms DTW from a black-box distance into a source of interpretable temporal features for neurodegenerative disease assessment.

---


### 329. [SRPR-Net: Semantic and Relational Prompt Refinement for Automated SAM-based Instance Segmentation](https://arxiv.org/abs/2609.24226)

**<font color=#1a73e8>作者：</font>** Lufei Liu, Guojie Li, Suncheng Xiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance segmentation is a fundamental computer vision task with diverse real-world applications. Recently, prompt-driven foundation models have shown promising generalization. However, automated prompting remains limited by insufficient semantic guidance and inter-instance modeling. To address this challenge, we propose a novel architecture, named Semantic Relational Prompt Refinement Network (SRPR-Net), for automated SAM-based instance segmentation. A sequential prompt refinement mechanism is introduced to enrich detector geometry with visual-language semantics and then incorporate same-image instance dependencies, enabling context-aware box adjustment before SAM segmentation. Experiments on multiple standard benchmarks demonstrate that SRPR-Net achieves consistent improvements in segmentation performance over existing state-of-the-art approaches. The code is publicly available at this https URL.

---


### 330. [IMPLICIT-Bench: Measuring Implicit Bias in Text-to-Image Models under Neutral Prompts](https://arxiv.org/abs/2609.24228)

**<font color=#1a73e8>作者：</font>** Yue Dai, Ziyang Liu, Marc Cheong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models are typically evaluated for bias using slot-based templates such as ``a photo of a [profession]''. Such templates probe only \emph{explicit} demographic attributes (e.g., gender, skin tone) in isolation. They overlook a broader \emph{implicit} bias that arises in natural prompts: when stereotype-relevant attributes are left unspecified, models still default to stereotypical outputs. We introduce IMPLICIT-Bench, a benchmark for measuring implicit bias in T2I models under such prompts. The key design is a structured-knowledge-graph (KG) construction of controlled prompt triplets: neutral, stereotype, and anti-stereotype variants that differ only along a single bias dimension while preserving scene semantics. This enables precise attribution of bias effects that template benchmarks cannot achieve. IMPLICIT-Bench comprises 5,493 prompts across 11 bias categories, validated through multi-model agreement, CLIP-based verification, and human evaluation. Using this benchmark, we show that state-of-the-art T2I models exhibit systematic bias under neutral prompts, a failure mode largely invisible to existing evaluations. We then use IMPLICIT-Bench to evaluate debiasing methods, uncovering a fundamental trade-off between bias reduction and semantic fidelity.

---


### 331. [Recovering Lost Details: Multi-Scale Frequency Compensation for Long-Term Time Series Forecasting](https://arxiv.org/abs/2609.24229)

**<font color=#1a73e8>作者：</font>** Runmin Zou, Siyi Xie, Yaohui Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting has made significant progress by leveraging multi-scale information to capture hierarchical temporal patterns and model long-range dependencies. However, temporal downsampling in existing multi-scale methods inevitably smooths detailed temporal fluctuations, and this information loss is further aggravated by their emphasis on dominant trends across scales, resulting in insufficiently expressive representations. To address this, we propose a Multi-Scale Wavelet Mixing (MWMixer) model, which incorporates a Bidirectional Frequency-Bands Mixing strategy to recover lost temporal details across scales, enabling complementary cross-scale information interactions. Then, a Dynamic Scale-Adaptive Fusion module learns time-varying weights for each scale to fuse multi-scale forecasts into the final prediction, enhancing the flexibility of multi-scale aggregation. In addition, a cross-scale consistency loss aligns each coarse-scale prediction with the interval-averaged fine-scale outputs, while a multi-scale supervision loss enforces prediction accuracy at each scale, promoting consistent learning across scales. Extensive experiments on seven real-world datasets demonstrate that MWMixer achieves competitive performance in long-term forecasting.

---


### 332. [Adaptive Forgetting for Nonstationary Optimization: Towards Robust EEG Decoding](https://arxiv.org/abs/2609.24233)

**<font color=#1a73e8>作者：</font>** Hongyu Zhu, Lin Chen, Jing Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) provides non-invasive monitoring of brain activity and is widely used in emotion recognition, motor imagery and sleep staging. Although within-subject decoding has achieved considerable progress, cross-subject generalization remains a central challenge in practical applications. EEG decoders are typically trained with Adam/AdamW under a fixed second-moment decay coefficient, even though cross-subject learning involves low signal-to-noise ratios, subject variability, and gradient nonstationarity. A fixed coefficient implicitly assumes that gradient statistics are homogeneous across layers and time, which can limit model's adaptability to cross-subject EEG signals and degrade generalization. To address these issues, we propose AFOR, a tensor-wise adaptive optimizer that converts the fixed second-moment decay coefficient into a dynamic coefficient estimated online from local gradient state. AFOR combines a Residual-Alignment Signal Scorer (RASS) and an Adaptive Forgetting Controller (AFC). RASS summarizes local gradient residuals and directional agreement into a signal-quality score, and AFC maps this score through self-referential normalization to a bounded per-step decay coefficient, with cumulative-product initialization correction maintaining consistency under time-varying decay.
Under a strict cross-subject protocol on three EEG benchmarks that cover three representative fields, AFOR achieves the best average performance among the compared optimizers, improving the mean test accuracy over Adam by 3.00%, 2.07%, and 4.38%, respectively.

---


### 333. [Hessian Rank Constraint for Learning Structure of Nonlinear Latent Variable Models](https://arxiv.org/abs/2609.24241)

**<font color=#1a73e8>作者：</font>** Zijian Li, Ruichu Cai, Feng Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncovering latent variables and their causal relations from observed data is a fundamental yet challenging problem. Existing methods often rely on restrictive assumptions, such as linear relations or invertible mixing functions. To better address this problem under general nonlinear mixing procedures, we propose a condition called the cross-Hessian Rank Constraint (HRC), which serves as a primitive rank-based tool for nonlinear latent causal discovery. In particular, we show that a rank-based property arises from the cross-Hessian of the observed-data log-density in the nonlinear case, revealing information about the latent variables, and reduces to the Tetrad constraints in the linear Gaussian case. More specifically, when two groups of observed variables are d-separated by a set of lower-dimensional latent variables, the rank of this cross-Hessian is equal to the dimension of the latent variables, under a mild affine derivative assumption on the conditional log-density derivatives. This assumption can be naturally satisfied when the noise level is low or the relevant nonlinearity is moderate. As a downstream application, we instantiate HRC in the pure one-factor measurement setting for locating latent variables and recovering their causal structure up to Markov equivalence. Experimental results on synthetic and real-world datasets support the theoretical claims.

---


### 334. [AI-Assisted Social Story Intervention for Special Education: The Design of AdaptED Stories](https://arxiv.org/abs/2609.24245)

**<font color=#1a73e8>作者：</font>** Buyankhishig Enkhjargal, Himanshi Lalwani, Hanan Salam  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social Stories are widely used to support autistic children in understanding and preparing for everyday situations, but creating stories that are appropriately tailored to each child's needs remains labor-intensive for practitioners. Existing digital tools support story assembly and delivery, but much of the work of writing, visual preparation, and personalization remains manual. Recent AI-based approaches have enabled automated story generation, yet offer limited support for practitioner oversight, context-sensitive personalization, and the use of supportive visuals grounded in individual learner profiles. We present AdaptED Stories, a practitioner-guided system for authoring, personalizing, and delivering Social Stories in special-education contexts. The system uses student profiles to draft story text and visuals, supports review and refinement by practitioners, and includes reading-session support with comprehension activities and session records. We report findings from a practitioner-informed design process, assessments of generated stories and visuals, and a usability study with seven special-education practitioners. Our findings suggest that AI assistance can reduce story-preparation burden and support more individualized story creation, alongside the importance of practitioner oversight, cultural and contextual specificity, and designing for varied learner needs. These findings contribute design implications for AI-assisted accessibility tools in special-education.

---


### 335. [Reinforcement Learning Inspired Black-box Adversarial Attacks for Computer Vision](https://arxiv.org/abs/2609.24249)

**<font color=#1a73e8>作者：</font>** Florian Krone, Elena Hoemann, Sven Hallerbach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks, both convolution or transformer based, are essential for modern computer vision systems. However, they are vulnerable to small perturbations, almost imperceptible to humans, which significantly alter the model's prediction. These adversarial attacks are often considered to be a significant threat to the implementation of neural networks in safety-critical applications. Most attacks utilize the white-box threat model and therefore require full access to the target model, making them unrealistic to use in practice. We propose a novel approach under the more realistic black-box threat model that utilizes concepts from reinforcement learning to optimize perturbations with a non-differentiable target model. Reinforcement learning algorithms have already been optimized to be query efficient, making them an ideal starting point when designing black-box adversarial attacks. We show the success of our reinforcement learning inspired black-box adversarial attack (RIBA) in generating adversarial perturbations using only a small number of queries to the target model, by comparing it to state of the art attacks on different models on the Cifar10 and ImageNet data sets. RIBA takes $25.4\%$ fewer median queries to generate attacked images against a ResNet-18 on Cifar10 and $22.5\%$ fewer median queries to fool a Vit-B/16 model on ImageNet. Additionally, we demonstrate that RIBA can match the performance of white-box attacks on an adversarially trained model.

---


### 336. [Explainable Predictive Condition-based Maintenance of Naval-Propulsion Systems using Fuzzy Logic](https://arxiv.org/abs/2609.24250)

**<font color=#1a73e8>作者：</font>** Dionisis Kalogeropoulos, Georgia Sovatzidi, Panagiotis G. Kalozoumis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The shipping industry has a significant impact on the global economy, emphasizing the need for operational availability and safety through the use of effective maintenance techniques. During the last decades, predictive maintenance (PdM) has emerged as a promising solution compared to the existing conventional maintenance systems. This is because it offers several advantageous functions, such as damage predictions for vessel components, reduced downtime, improved and extended life of machinery, as well as higher safety during voyages. However, existing methodologies developed for performing PdM do not provide explanations of their results to users, so that they can understand the failures that may occur. To address this limitation, this paper proposes a novel framework based on a fuzzy decision tree and a deep residual neural network, aiming to perform explainable PdM on naval vessels. The proposed framework is able to generate fuzzy local rules based on the dataset used, and can provide explanations of its outcomes, using cause-and-effect relationships, in a way that are understandable to users, thereby gaining their trust. Experiments using a publicly available dataset demonstrate the effectiveness of the proposed framework, as it achieves an accuracy of 99.24%.

---


### 337. [Making Fragmented Reports Legible: Finding Patterns and Perceptions of Sexual Violence in Bangladesh](https://arxiv.org/abs/2609.24254)

**<font color=#1a73e8>作者：</font>** Sheherjan Haq, Sharifa Sultana  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Evidence about sexual violence in Bangladesh is fragmented across individual reports, while official and civil-society statistics rarely provide reusable case-level detail. We examine how structured analysis can make one part of this fragmented record legible without treating it as prevalence data. Our corpus contains 2,811 articles timestamped 2013-2023 from the Prothom Alo publishing ecosystem; 2,794 include parseable metadata about reported victims, alleged perpetrators, incidents, legal responses, and locations. We combine descriptive and spatial analysis of these records with thematic analysis of 115 convenience-sample survey responses collected in late 2020. The corpus documents many young, female, and student victims, frequent acquaintance and neighbor relationships, uneven geographic documentation, and substantial missingness in legal outcomes. Respondents most often describe weak enforcement, insecurity, patriarchal socialization, education gaps, and community inaction as conditions enabling persistence. These findings characterize news documentation and public perceptions; they do not estimate incidence, geographic risk, or causality. We contribute an uncertainty-aware framing for HCI research using sensitive, low-resource news data and identify design requirements for provenance, privacy, validation, and responsible communication.

---


### 338. [Unsupervised Brain Anomaly Detection as a Bayesian Inverse Problem with Diffusion Prior](https://arxiv.org/abs/2609.24265)

**<font color=#1a73e8>作者：</font>** Hugues Roy, Reuben Dorent, Ninon Burgos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unsupervised anomaly detection (UAD) aims to localize abnormal regions in medical scans without pixel-level annotations. A typical strategy seeks to reconstruct a pseudo-healthy image that preserves subject-specific anatomy. Recently, diffusion models have been proposed to perform UAD. However, these methods rely on heuristic noise schedules or synthetic corruptions to balance subject-specificity and anomaly removal. In this work, we propose an alternative formulation of UAD as a Bayesian inverse problem under a diffusion prior. First, we introduce a latent spatial anomaly mask that models pixel-wise consistency between a test image and its latent corresponding pseudo-healthy image. Then, we propose an approximation of the unknown generation process that links healthy anatomy, anomalies, and the observed image, enabling a well-defined likelihood within the Bayesian framework. Building on recent advances in diffusion-based inverse problem methods, we jointly infer the pseudo-healthy image and the anomaly mask via annealed posterior sampling. We evaluate our approach on FDG PET (ADNI) and FLAIR MRI (BraTS 2021), demonstrating improved anomaly localization performance compared to other diffusion-based approaches and validating the contribution of our introduced model. Our code is available at this https URL.

---


### 339. [Structure Before Sampling: Community-Aware Core-Set Selection for Data-Efficient Text-to-Speech](https://arxiv.org/abs/2609.24275)

**<font color=#1a73e8>作者：</font>** Mizbaul Haque Maruf, Muhammad Nur Yanhaona  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-speech (TTS) corpora are costly to record, yet many utterances add little new phonetic information. Core-set selection reduces this cost by choosing a small training subset under a fixed audio-duration budget. We represent a corpus as a phonotactic graph that links each utterance to its most phonemically similar ones, and we first test whether this graph has structure. In Bangla and English corpora, its clustering is 199 and 56 times that of a size-matched random graph, and its modularity is more than twice that of a degree-preserving random graph. We then propose Community Representative, a selector that samples across graph communities and spreads its choices within each one, starting from utterances rich in rare phonemes. At every budget and in both languages, it covers more rare phoneme bigrams than random and entropy-based selection, and this lead holds on held-out utterances. TTS models trained on its 20% core-sets have a significantly lower character error rate (CER) than models trained on equal-duration random or entropy-based subsets in both languages. When all models train for the same number of epochs, the Bangla core-set model also outperforms full-corpus training (3.93% vs. 4.47% CER) with 4.5x less training time.

---


### 340. [High-Dimensional Online Change Point Detection with Adaptive Thresholding and Interpretability](https://arxiv.org/abs/2609.24278)

**<font color=#1a73e8>作者：</font>** Sven Jacob, Bardh Prenkaj, Weijia Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Change point detection (CPD) identifies abrupt and significant changes in sequential data, with applications in human activity recognition, financial markets, cybersecurity, manufacturing, and autonomous systems. Traditional CPD methods often face computational challenges in high-dimensional settings and typically provide limited explanations for detected changes, which can restrict their practical usability. This paper introduces a CPD framework that improves scalability and interpretability by leveraging the Sliced Wasserstein (SW) distance. Our contributions are fourfold: (1) we transform multivariate sequential data into one-dimensional scores using the SW distance, making the resulting representation compatible with existing CPD methods; (2) we analyze the distributional behavior of random slices of the SW distance and show that, under suitable assumptions, they can be approximated by a Gamma distribution, providing a principled basis for threshold calibration; (3) we propose a self-adapting online CPD algorithm that combines this SW-based score with an adaptive quantile-based threshold; (4) we introduce a model-specific framework for generating contrastive explanations for annotated change points. Empirically, our method reduces false positives by at least $48\%$ on average compared with popular online and offline CPD baselines, while maintaining competitive or superior detection performance. Code is available at this https URL. At the same time, it produces interpretable change-point annotations, making it practical for deployment in high-stakes applications.

---


### 341. [Temporal Generalization and Explanation Stability of Control Flow Graph Neural Networks for Malware Detection](https://arxiv.org/abs/2609.24280)

**<font color=#1a73e8>作者：</font>** Md. Asif Sajeed, Md. Nazrul Islam Mondal, Md Ashraful Hossen Akash  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware detection is a critical task in cybersecurity, and graph neural networks over control flow graphs have shown promising results for it. However, detectors are usually evaluated on a random split of a corpus collected over a single period, which cannot show how well a model generalizes to later samples. This study addresses that limitation with a strict temporal split: every model is trained on one period and scored once on a later one. Two corpora of control flow graphs, each node carrying 37 features, were extracted statically from 1,989 Windows portable executables: 459 graphs from 2024-2025 for training and 223 from 2026 for evaluation. Twelve variants and a flat-feature control were trained on the earlier corpus. The choice of message-passing operator changes robustness to the shift significantly, and every pairwise gap that survives correction separates an aggregating architecture from one built around a learned attentional readout. The ranking also reverses: the flat control, which sees node features but no topology, is the best in-distribution model and among the worst across the boundary, so a conventional benchmark would have rejected message passing. Neither recalibration nor ensembling substitutes for the operator choice. Attributions do not shift, but explanation validity is architecture-specific, and the most accurate operator on the later corpus is the hardest to explain. An architecture derived from the finding matches the best searched operator without search. The shift affects both malware and benign classes alike, so these are results about robustness to distribution shift, not malware evolution.

---


### 342. [Classifier-Free Guidance in Flow Matching: Non-Autonomous Potentials, Overshoot, and Posterior-Mean Control](https://arxiv.org/abs/2609.24287)

**<font color=#1a73e8>作者：</font>** Jishen Peng, Zheng Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) improves conditional generation in Flow Matching, but strong guidance can distort the generated distribution and reduce diversity. We provide a geometric account of this behavior by viewing Flow Matching as a time-varying gradient flow and characterizing how CFG reshapes its underlying potential. This view explains how stronger alignment can be accompanied by mean displacement and trajectory concentration, and motivates controlling guidance through the model-implied terminal posterior mean. We therefore propose Posterior-Mean-Capped CFG (PMC-CFG), a training-free, per-sample method that adaptively retains the strongest feasible guidance without additional network evaluations. Experiments on synthetic and large-scale image-generation benchmarks show that PMC-CFG limits guidance-induced distortion and concentration while improving the alignment--diversity trade-off, with particularly strong benefits when nominal guidance is large.

---


### 343. [rApp/xApp Attestation: A New Security Use Case for O-RAN](https://arxiv.org/abs/2609.24296)

**<font color=#1a73e8>作者：</font>** Hamed Alimohammadi, Burcu Şahin, Arda Akman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The disaggregation and softwarization introduced by the Open Radio Access Network (O-RAN) architecture enable multi-vendor innovation but also expose the RAN Intelligent Controller (RIC) ecosystem to new runtime security risks. Existing O-RAN specifications define strong safeguards for onboarding, authentication, identity management, and secure communication; however, they do not provide a concrete mechanism for verifying whether deployed rApps and xApps remain in their intended, untampered state during operation.
This paper introduces rApp/xApp attestation as a RIC-native O-RAN security use case for runtime integrity verification. Rather than proposing a new cryptographic protocol, the work defines how existing integrity verification techniques can be integrated into O-RAN through attestation modules, attestation agents, RIC application interfaces, and SMO-driven policy coordination. We map the use case to relevant O-RAN Alliance working groups, identify required standardization extensions, and demonstrate feasibility through a lightweight hash-based prototype implemented on the Near-RT RIC platform. Experimental results show attestation latencies below 40 ms across multiple cryptographic hash functions, indicating that runtime attestation can be performed without disrupting time-sensitive RIC operations when appropriately scheduled. Finally, we discuss remaining technical and standardization challenges, including trusted verification, known-good runtime states, scalability, mitigation policies, and future hybrid attestation mechanisms.

---


### 344. [HappyWorld-Bench](https://arxiv.org/abs/2609.24308)

**<font color=#1a73e8>作者：</font>** Zhiqi Bai, Junai Cai, Yixin Chen 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating world models requires assessing both the quality of the worlds they generate and their consistency and responsiveness under exploration, interaction, and modification. We introduce HappyWorld-Bench, a comprehensive benchmark that evaluates whether generated worlds remain reliable as agents interact with them. Our design is built on a hierarchical capability framework of six world capabilities (W1-W6), from generative construction to unified world modeling, instantiated across three independent evaluation tracks: video world models, spatial world models, and embodied world models. HappyWorld-Bench comprises 1,138 video prompts, 300 spatial scenes, and 254 embodied test cases. Across all three tracks, we build and operate HappyWorld-Arena to organize human A/B comparisons and derive model-level Elo ratings, which complement newly designed automated metrics that capture behavioral correctness. We evaluate 14 video world models, 9 spatial systems, and 8 embodied candidates under this unified framework. Results reveal remaining reliability gaps across all three tracks: video models exhibit reduced consistency during extended rollouts and revisits, spatial models achieve at best 70.14% placement accuracy and 73.33% edit execution, and embodied models struggle to preserve state across multi-step actions and respond precisely to altered action conditions and physical rules. These findings highlight the need to evaluate world models not only by visual quality, but also by state consistency and the correctness of their responses to actions and interventions.

---


### 345. [AnalogDepth: Multi-view Geometry from FPV drones under Analog Video Transmission](https://arxiv.org/abs/2609.24312)

**<font color=#1a73e8>作者：</font>** André Amorim, Pedro F. Proença  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analog video transmission (VTX) remains widespread in FPV drones due to low latency, weight and low cost. However analog VTX suffers from complex spatially structured image degradation which differ fundamentally from digital image corruption (e.g. AWGN) used in standard training augmentation. This work shows that this type of noise severely degrades the accuracy of Depth Anything 3 (DA3), a state-of-the-art feed forward visual geometry foundation model.
To address this gap, we present AnalogDepth, a parameter-efficient training pipeline that adapts DA3 to analog FPV imagery using student-teacher knowledge distillation with Low-Rank Adaptation (LoRA) injected into the DINOv2 backbone. Rather than synthesizing noise analytically, we build a noise bank from static FPV recordings under diverse conditions and compare real-noise injection against PSD-matched Gaussian synthesis and AWGN as baselines. Experiments on six real FPV flight sequences across three indoor scenes show that training with our noise bank consistently reduces per-frame depth RMSE and 3D reconstruction Chamfer distance compared to the pretrained DA3 baseline and both Gaussian noise variants. These results demonstrate that replicating the spatial structure of real analog transmission noise is critical for effective adaptation.

---


### 346. [NeuIDO: Neural Intrinsic Dynamics Operator for Physics-Informed 4D World Models](https://arxiv.org/abs/2609.24313)

**<font color=#1a73e8>作者：</font>** Jiajing Lin, Xin Zhang, Jianhua Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models aim to capture environmental dynamics and predict future trajectories, showing growing potential for embodied intelligence. Physics-informed 4D generation integrates physical simulation to predict 3D object interactions, offering a promising pathway toward world models. However, this paradigm relies on manually imposed dynamical assumptions rather than internalizing world dynamics, and thus still leaves a gap toward a true world model. To bridge this gap, we propose NeuIDO, a novel world dynamics modeling framework that learns a unified intrinsic dynamics representation from visual observations, advancing physics-informed 4D generation toward a world model. Specifically, we formulate world modeling as a neural operator learning problem and introduce a two-stage training strategy to learn a generalizable mapping from the visual observation distribution to the intrinsic dynamics distribution. Building on this observation-dynamics mapping, NeuIDO enables zero-shot dynamics inference directly from videos and can be further aligned with complex real-world dynamics via few-shot adaptation. Extensive experiments demonstrate that NeuIDO effectively unifies the intrinsic dynamics underlying diverse visual observations into a shared representation and rapidly infers dynamics in novel scenes.

---


### 347. [The Undetected Damage of Quantization on Retrieval and How to Fix It](https://arxiv.org/abs/2609.24322)

**<font color=#1a73e8>作者：</font>** Luca Zhou, Alessandro Zirilli, Daniele Solombrino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that a quantized model that keeps its classification accuracy still changes $14$ to $46\%$ of its top-1 retrieval results, and that aggregate ranking metrics reveal only part of this damage. We tie this failure to the gap between the two highest scores and use that gap to decide when a quantized answer can be trusted and where additional precision should be spent. We show that the top-1 result is guaranteed to survive quantization only when this gap exceeds twice the largest rounding error. In classification, scores are the logits, and the loss function pushes the correct class away from other classes, encouraging this gap. In retrieval, scores are query-document scores, and nothing separates the top-1 item from the second. This gap can be measured without labels. Before deployment, it predicts which models will break under quantization, and at deployment time it tells, per input, whether the quantized answer still matches the full-precision answer. Most classification inputs have a gap wide enough to trust the quantized answer, but few retrieval queries do. That gap motivates a different fix in each task. In retrieval, spending extra bit-width on the layers whose quantization moves the gap most recovers up to three-quarters of an extra bit's benefit for half its cost. In classification, routing the few low-gap inputs to full precision recovers most of the lost accuracy at a fraction of the cost.

---


### 348. [Brain-Token Learning: Microstate-Based Tokenization and Multi-Scale Interaction for Long-Horizon EEG Sequence Modeling](https://arxiv.org/abs/2609.24324)

**<font color=#1a73e8>作者：</font>** Weishan Ye, Yue Pan, Li Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) provides a non-invasive window into dynamic brain activity, yet modeling long-horizon EEG sequences remains challenging due to their high temporal complexity, substantial variability across subjects, and the lack of biologically meaningful sequence representations. Existing tokenization strategies, such as fixed-window and patch-based representations, discretize EEG signals according to artificial temporal boundaries, which may disrupt intrinsic brain-state dynamics. In this work, we propose Brain-Token Learning, a neuroscience-inspired framework that introduces Brain Tokenization for long-horizon EEG sequence modeling. Instead of partitioning EEG signals into predefined temporal segments, Brain Tokenization represents EEG as sequences of recurrent microstate-derived brain tokens, where each token corresponds to a quasi-stable large-scale brain state with variable temporal duration. Based on these biologically grounded tokens, we further develop a multi-scale token interaction module consisting of Latent State Aggregation and State Transition Modeling to jointly capture global brain-state context and local microstate transitions. We evaluate Brain-Token on five heterogeneous EEG datasets, including the newly collected long-horizon NeuroLong dataset and four affective or clinical EEG datasets (SEED, DEAP, MDD, and NSSI). Extensive experiments demonstrate that Brain-Token consistently outperforms conventional CNN/LSTM architectures, Transformer-based models, and domain adaptation methods across diverse EEG scenarios. Further analysis verifies the effectiveness of microstate-based tokenization and multi-scale interaction for learning robust and interpretable EEG representations. These results establish Brain-Token as a biologically grounded tokenization paradigm for long-horizon EEG sequence modeling.

---


### 349. [AlignMorph: Tuning-Free Diffusion Image Morphing via Explicit Semantic Transport](https://arxiv.org/abs/2609.24330)

**<font color=#1a73e8>作者：</font>** Wuyi Liu, Xu Han, Yuren Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image morphing aims to produce a smooth and semantically consistent transition between two input images. Existing diffusion-based morphing methods either require expensive per-pair optimization or rely on implicit spatial alignment, which easily fails under large layout discrepancies. To address these limitations, we propose AlignMorph, a novel tuning-free diffusion framework guided by the principle of transport-then-denoise. We explicitly decouple geometric alignment from generative denoising to avoid structural entanglement. Our framework consists of two core components. (1) Global Semantic Transport, which achieves diffusion-compatible semantic alignment via entropic optimal transport and reliability-aware latent warping; and (2) Coordinate-Aligned Generation, which uses a symmetric bi-phase attention handoff to maintain consistent spatial coordinates throughout denoising. Without any tuning, AlignMorph effectively eliminates ghosting and achieves superior structural coherence and temporal smoothness on morphing benchmarks. Code is available at this https URL.

---


### 350. [LiAuto-MindViT: A Hybrid Vision Backbone with Adaptive Bidirectional Mamba](https://arxiv.org/abs/2609.24337)

**<font color=#1a73e8>作者：</font>** Lifu Mu, Shuai Chen, Wen Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Mamba-based models have shown strong potential for long sequence modeling, adapting them to vision is challenging due to the requirement of local neighborhood correlations and multi-directional spatial contexts for visual understanding. In this paper, we present LiAuto-MindViT, a novel hybrid vision backbone that synergizes the strengths of CNNs, Mamba, and Transformers. The core of our design is the Adaptive Bidirectional Mamba (ABM), which eliminates the directional bias of unidirectional SSMs through bidirectional selective scanning with learnable alpha blending, enabling content-adaptive directional fusion without the overhead of exhaustive multi-path routing. To further accelerate inference, we propose a deployment-friendly Reparameterized ConvSE (RepConvSE) module that leverages structural reparameterization to reduce latency and memory access overhead. Extensive experiments demonstrate that LiAuto-MindViT achieves state-of-the-art performance on image classification, object detection, and semantic segmentation while enabling efficient inference through reparameterization.

---


> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
