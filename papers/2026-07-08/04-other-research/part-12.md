# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**551-571**（第 12/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-571**

---

### 551. [Steering Optimisation Trajectories in Diffusion Representation Learning](https://arxiv.org/abs/2607.05319)

**<font color=#1a73e8>作者：</font>** Rajat Rasal, Avinash Kori, Tian Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study why diffusion autoencoders can achieve similar image quality while learning substantially different latent structures. We trace this behaviour to optimisation dynamics; we analyse curves of image reconstruction against latent representation quality, revealing trajectories that organise around two distinct regimes early in training. Models in the reconstruction regime prioritise image fidelity early, whereas those in the disentanglement regime improve reconstruction and disentanglement more gradually. We hypothesise that this behaviour can be influenced by targeting shortcut pathways in the diffusion U-Net and controlling early noise-level exposure, thereby shaping the reconstruction-disentanglement trade-off during training. To steer optimisation toward stronger representations, we introduce SteeringDRL, combining gated residual U-Nets with a simple noise-level exposure curriculum for training. Across disentanglement benchmarks, SteeringDRL improves representation quality and reduces seed sensitivity. Our method further extends to spatial disentanglement in object-centric learning, improving segmentation quality on synthetic and real-world datasets.

---


### 552. [CenSynCMB: Centre Maps and Physics-Guided Synthesis for Microbleed Detection](https://arxiv.org/abs/2607.05325)

**<font color=#1a73e8>作者：</font>** Lucas He, Hanyuan Zhang, Krinos Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cerebral microbleeds (CMBs) are MRI markers of small vessel disease and the microbleed component of amyloid related imaging abnormalities (ARIA-H), but their small size, sparsity, and similarity to vessels, calcification-like foci, and artefacts make automated detection difficult. We propose CenSynCMB, a centre-guided and mimic-aware framework combining a 3D Attention U-Net, auxiliary centre-map supervision, false-negative-driven reweighting, and fold-wise physics-guided synthesis of positive CMBs and labelled hard negatives. Synthetic data expose the detector to compact lesions and common mimics without validation or test leakage. On VALDO Task 2, CenSynCMB achieved the best local-comparison lesion-level F1 (74.3%, p = 0.020); on external AIBL SWI, it achieved the highest local-comparison recall (88.5%, p = 0.0058) and F1 (65.0%, p = 0.0016). Together, these results support scalable CMB candidate extraction in large, unlabelled MRI cohorts, while highlighting cohort-specific calibration as the next step toward reliable burden estimation.

---


### 553. [How Far is Too Far? Defining the Distance Threshold for Verification Siamese Networks](https://arxiv.org/abs/2607.05329)

**<font color=#1a73e8>作者：</font>** Heloísa Dias Viotto, Cauê Samonek, Lucas Garcia Pedroso 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Siamese verification networks are widely used to compare items such as faces, cars, or signatures. In these scenarios, the network is trained to learn an embedding space in which similar objects are mapped closer together, while dissimilar objects are mapped further apart. Two objects are considered to belong to the same class (e.g., the same person in two different images) when the distance between their embeddings falls below a predefined threshold. Defining this threshold, however, is a non-trivial task and typically requires labeled data. In this work, we assume that the distribution of distances produced by a siamese verification network can be approximated by a bimodal function. Based on this assumption, we propose an unsupervised method to determine the verification threshold by identifying the minimum point between the two modes. The proposed approach does not require annotated samples, enabling the verification threshold to be updated directly in the deployment environment without the cost of manual labeling. We evaluate our method on four datasets: MNIST, CIFAR-10, LFW, and PKLot. The results indicate that the proposed approach achieves an average verification accuracy of 94%, comparable to the Equal Error Rate method, while eliminating the need for labeled data.

---


### 554. [TREK: Distill to Explore, Reinforce to Refine](https://arxiv.org/abs/2607.05339)

**<font color=#1a73e8>作者：</font>** Yuanda Xu, Zhengze Zhou, Kayhan Behdin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) is effective when the current policy already samples useful reasoning trajectories, but it stalls on hard prompts whose correct solution modes lie outside the student's on-policy support. We propose TREK (Teacher-Routed Exploration via Forward KL), a simple staged procedure that uses distillation not for imitation but for exploration support expansion. A key advantage of TREK is its generality: because it only consumes verified output trajectories, it can use an external black-box teacher, a white-box teacher, or the same model given additional inference-time context, and it can efficiently identify which hard-prompt samples are most worth consolidating even when teacher internals are unavailable. TREK first identifies prompts where the unaided student has very low pass rate, queries a proposal source to produce verified candidate solutions, keeps the top-$r$ proposals ranked by current student likelihood, applies a short forward-KL phase to pull those verified modes into the student's support, and then returns to standard on-policy GRPO refinement. On mathematical reasoning, TREK with DeepSeek-V4 proposals improves Qwen3 models across all tested scales on AIME 2024 and AIME 2025; for Qwen3-8B, it improves AIME 2025 from 36.9 to 40.3 and AIME 2024 from 47.9 to 51.1 (avg@16), while the self-context variant reaches 38.5 and 49.6 without an external teacher. On agentic tasks, TREK raises ALFWorld success rate from 75.8 to 82.8 and ScienceWorld success rate from 12.5 to 26.7; notably, on the hardest task types, TREK achieves high success rates early in training while unaided GRPO requires substantially more optimization steps to reach comparable levels.

---


### 555. [OptiAgent: End-to-End Optimization Modeling via Multi-Agent Iterative Refinement](https://arxiv.org/abs/2607.05346)

**<font color=#1a73e8>作者：</font>** Adriana Laurindo Monteiro, Nayse Fagundes, Gabriel Mattos Langeloh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose OptiAgent, a multi-agent framework that, given a natural language description of an Operations Research problem, is able to output a solver-ready mathematical formulation as well as executable code. Our architecture prioritizes the mathematical modeling step, where dedicated agents extract structures, such as decision variables and constraints, enabling iterative self-correction. We introduce a novel multi-loop validation architecture with four specialized feedback mechanisms, each targeting a distinct failure mode such as misinterpretation, structural defects, mathematical inconsistencies, validation failures, and code errors. Alongside accuracy, our modular design improves the process of solving optimization problems by improving transparency, as each agent exposes its reasoning and feedback, making the full modeling process auditable. Our framework achieves state-of-the-art performance on 3 out of 4 benchmarks across LP, MILP, and Nonlinear Programming tasks, while remaining highly competitive on the remaining dataset.

---


### 556. [WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347)

**<font color=#1a73e8>作者：</font>** Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While feedforward 3D reconstruction excels at efficient novel view synthesis, it typically falters when faced with scenes under varying illumination. To this end, we introduce WildSplat, the first feedforward 3D Gaussian Splatting framework capable of appearance-conditioned novel-view synthesis for unposed in-the-wild images. To handle inconsistent photometric conditions, we propose a dual-branch architecture that explicitly decouples geometry from appearance. The geometry branch extracts an appearance-invariant 3D structure and jointly predicts camera poses. To govern the rendering appearance, the appearance branch injects target appearance cues into the content features via a globally pre-modulated cross-attention mechanism. To further prevent feature entanglement, we introduce a joint multi-reference training strategy that stabilizes the training process. Extensive experiments show that WildSplat surpasses existing optimization-based and feedforward methods, achieving state-of-the-art performance in in-the-wild novel view synthesis and appearance editing from sparse inputs in a single forward pass.

---


### 557. [Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis](https://arxiv.org/abs/2607.05348)

**<font color=#1a73e8>作者：</font>** Xianhao Chen, Jiarui Hu, Yuanbo Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene understanding aims to segment 3D scenes beyond predefined categories by transferring semantic knowledge from vision-language models. Existing methods have advanced this task by lifting language-aligned 2D features into 3D, yet they often rely on context-independent semantic representations, leaving object relationships underexplored for contextual refinement. We propose RelGraphOV, a relationship-aware framework that uses 3D scene graphs to enhance open-vocabulary 3D understanding. Our method constructs relational scene graphs from multi-view observations by leveraging vision-language reasoning to infer object relationships and prune geometrically implausible connections, without manual relationship annotations. To aggregate relational context while avoiding feature interference, we introduce an Adaptive Gated Dual-Stream Contextual GAT that separates dense geometric features and semantic CLIP embeddings, performs edge-guided message passing, and adaptively fuses complementary semantics. A hierarchical contrastive objective further promotes instance-level consistency and category-level discrimination. Experiments on ScanNetV2, ScanNet200, ScanNet$++$, and Replica demonstrate strong performance and generalization ability. Project Page: this https URL

---


### 558. [Geometric Reciprocity: Unlocking Self-Supervision for Stereoscopic Video Generation](https://arxiv.org/abs/2607.05354)

**<font color=#1a73e8>作者：</font>** Jingyi Lu, Kai Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular-to-stereo conversion synthesizes stereoscopic content from 2D videos for immersive 3D experiences. In modern Depth-Image-Based Rendering (DIBR) approaches, stereo inpainting of disocclusions is the critical bottleneck. Training-based methods achieve superior quality but rely on scarce stereo pairs or synthetic data with domain gaps. We address this through the first self-supervised framework learning from monocular videos via cycle consistency. Our key contribution is the Geometric Reciprocity Theorem (GRT): under the nearest-neighbor DIBR formulation, the disocclusion mask when synthesizing a target view equals the mask of pixels lost when warping back from target to source, enabling analytical computation of test-time disocclusion masks directly from monocular images. This yields train-test consistency for the stated warping formulation, supporting self-supervised learning from unlimited monocular videos and substantial improvements over training-free and supervised state-of-the-art methods. Project page: this https URL

---


### 559. [Faithfulness to Refusal: A Causal Audit of Neuron Selectors](https://arxiv.org/abs/2607.05355)

**<font color=#1a73e8>作者：</font>** Ananth Eswar, Pratinav Seth, Utsav Avaiya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally important rows is rarely tested directly. We address this with two paired audits built on one-shot neuron-row zeroing. We first audit selectors at the language-modeling level: attribution methods substantially outperform activation and magnitude-based baselines at identifying dispensable rows across five LLMs. We then adapt the same intervention into a behavior test by driving it with a contrastive harmful-versus-benign signal; the attributed rows are sufficient to install refusal on hate and crime while keeping benign over-refusal low and preserving language model fluency, and specific in that layer-matched random controls at the same depths fail. Highly rank-stable selectors can be among the least causally valid. Refusal moreover lives in a redundant subspace, where different attribution methods install it through largely disjoint row sets, so the recovered edit is one realization of a sufficient set rather than a unique mechanism. Together, these findings show that rank-stability proxies miss the kinds of selector failures a direct causal audit can surface.%

---


### 560. [ReCal3R: Reliability-Calibrated Learning Rates for Streaming 3D Reconstruction](https://arxiv.org/abs/2607.05356)

**<font color=#1a73e8>作者：</font>** Xinze Li, Yiyuan Wang, Pengxu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction relies on a compact recurrent scene state to process long image streams in linear time and bounded memory. However, repeated updates can gradually corrupt this state, causing reliable historical information to be overwritten by noisy or ambiguous observations. We introduce ReCal3R, a reliability-calibrated learning rate method for recurrent 3D reconstruction. Instead of directly applying a candidate learning rate, our method estimates state token reliability from the maintained scene state and uses it to calibrate a candidate learning rate derived from token alignment, state reconstruction residual, and recent update pressure. The resulting token-wise learning rate interpolates between a conservative base rate and the candidate rate, suppressing aggressive updates on unreliable tokens while preserving adaptation to informative frames. Applied to CUT3R as a training-free calibration rule, ReCal3R reaches strong performance on long sequences in pose, depth, and reconstruction quality, including a 3.7$\times$ reduction in ATE, with comparable runtime and memory. Code is available at: this https URL.

---


### 561. [Graph Sparse Sampling: Breaking the Curse of the Horizon in Continuous MDP Planning](https://arxiv.org/abs/2607.05359)

**<font color=#1a73e8>作者：</font>** Idan Lev-Yehudi, Vadim Indelman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning under uncertainty in continuous domains is essential for autonomous systems, yet computationally demanding. Tree-based search methods such as Monte Carlo Tree Search (MCTS) remain popular, but their branching structure can require sampling budgets that grow exponentially with lookahead depth in the worst case. From a tree perspective, continuous state or action spaces become especially challenging, since the planner must decide where to search in an infinite branching hierarchy. We propose Graph Sparse Sampling (GSS), an online planning algorithm that shares sampled futures across many candidate decisions, rather than sampling separate successors for each candidate action. This branch-free graph exposes large GPU-friendly batches, while using heuristics to focus computation. We prove finite-sample performance guarantees for GSS covering full-rank or low-rank generative simulators via smoothed backups, and discrete or sampled continuous action spaces. Under suitable overlap, regularity, and action-coverage conditions, these bounds have polynomial dependence on the planning horizon, formalizing when shared futures can avoid the exponential horizon dependence of tree-shaped sparse sampling. We demonstrate continuous-control simulations where GSS substantially outperforms tree-based planners on long horizons or achieves near-optimal performance, supporting no-branching graph planning as a complementary design principle for online control.

---


### 562. [SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](https://arxiv.org/abs/2607.05363)

**<font color=#1a73e8>作者：</font>** Dylan Zongmin Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal agents are becoming persistent user-owned intermediaries: they remember preferences, filter platform-mediated information, use tools, and negotiate with services. Existing benchmarks evaluate tool use, web navigation, desktop control, personalization, recommendation, and evolving context, but rarely ask whether an agent preserves user sovereignty: advancing the user's current interests while respecting privacy, consent, evidence, user burden, and resistance to manipulative incentives. We introduce SovereignPA-Bench, an executable benchmark for evaluating user-owned personal agents under evolving intent, platform mediation, privacy boundaries, consent constraints, evidence requirements, and burden tradeoffs. The benchmark separates agent-visible ObservableState from evaluator-only HiddenLabels, reports component metrics for task success, alignment, privacy, consent, evidence, manipulation, burden, and auditability, and preserves paired scenario ordering for model and policy comparisons. We evaluate 120 sovereignty stress scenarios across 4 model families and 8 policy baselines, yielding 3,840 frozen-prompt trajectories with raw prompts, outputs, provider-form responses, parsed actions, recomputable metrics, hard-set analyses, qualitative cases, and a blinded 3-annotator audit over 240 items. Full-sovereign scaffolding improves sovereignty score over direct, memory-only, consent-only, evidence-only, ReAct/tool-use, safety-prompt, and judge-guard baselines while reducing privacy leakage, consent violation, over-concession, and manipulation capture. Human audit shows high agreement on privacy and consent and lower agreement on manipulation, identifying the subjective frontier of platform-persuasion judgments. These results show that personal-agent evaluation must move beyond task completion toward representative, consent-aware, evidence-grounded action.

---


### 563. [PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space](https://arxiv.org/abs/2607.05373)

**<font color=#1a73e8>作者：</font>** Sensen Gao, Zhaoqing Wang, Qihang Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction and generation are commonly tackled by separate paradigms: pixel-based regression for reconstruction, and latent diffusion for generation. Recent works attempt to unify them in latent space, but with notable drawbacks: the diffusion objective is defined on latent features rather than the underlying 3D representation, and both branches suffer from information loss introduced by latent encoding, while requiring a pretrained Variational Autoencoder (VAE) or Representation Autoencoder (RAE). In this paper, we reformulate these two tasks under a unified pixel-space diffusion paradigm and introduce PixWorld, a single model that jointly addresses 3D reconstruction and generation. By supervising diffusion directly on rendered images, PixWorld removes the above limitations and aligns optimization with 3D scene fidelity. Beyond photometric and perceptual supervision that operates at the 2D image level and lacks 3D geometric awareness, we further introduce a geometry perception loss that aligns rendered views with their ground truth in the geometry-aware feature space of a pretrained 3D foundation model, providing 3D structural supervision. PixWorld consistently outperforms prior latent-space generation methods and matches state-of-the-art reconstruction methods, demonstrating the superiority of a unified pixel-space approach.

---


### 564. [MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing](https://arxiv.org/abs/2607.05376)

**<font color=#1a73e8>作者：</font>** Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion models have enabled either long single-view generation through temporal autoregression, or short multi-view synthesis through bidirectional attention. However, generating long, multi-view consistent videos of dynamic scenes remains unsolved. In this work, we present MV-Forcing, a framework that composes temporal and view-wise autoregression within a single diffusion model by introducing a 4D geometric bridge between sequentially generated views. Our key insight is that an autoregressive 3D reconstruction model naturally interfaces between autoregressively generated views. Given a completed source view, we reconstruct its 3D structure and render a geometric prior of the next target viewpoint, which the diffusion model refines into a high-quality video. To extend generation beyond the teacher's fixed temporal window, we introduce a joint denoising regime where both view slots are initialized from noise during training, enabling temporally unbounded generation. We distill the model via Distribution Matching Distillation with Spatio-Temporal Self-Forcing, closing the train-inference exposure bias gap for both temporal and view-sequential autoregression. Extensive experiments on both synthetic and real-world data demonstrate that MV-Forcing produces geometrically consistent multi-view videos of dynamic scenes at arbitrary lengths and viewpoint counts using a single few-step student model.

---


### 565. [CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents](https://arxiv.org/abs/2607.05378)

**<font color=#1a73e8>作者：</font>** Yujiang Li, Zhenyu Hou, Yi Jing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic LLMs are increasingly limited by finite context windows, as extended interaction trajectories can exceed the maximum context length before a task is completed. Context compaction offers a natural solution by summarizing previous interaction states and continuing the rollout under a compressed context, but incorporating compaction into reinforcement learning remains underexplored. We propose CompactionRL, a reinforcement learning strategy to train long-horizon agentic LLMs with context compaction. Our approach jointly optimizes task execution and summary generation with token-level loss normalization and cross-trajectory generalized advantage estimation. This design enables the LLM agents to learn from compacted long-horizon trajectories. We train CompactionRL on top of open models and observe consistent performance gains on agentic coding tasks. CompactionRL enables the open GLM-4.5-Air model (106B-A30B) to achieve Pass@1 scores of 66.8% on SWE-bench Verified and 24.5% on Terminal-Bench 2.0, with absolute gains of 7.0 and 3.1 points, respectively. Built upon GLM-4.7-Flash (30B-A3B), CompactionRL improves Pass@1 by 5.5 and 6.8 points, reaching 56.0% on SWE-bench Verified and 20.2% on Terminal-Bench 2.0, respectively. CompactionRL is thus deployed in the RL pipeline for training the open GLM-5.2 model (750B-A40B).

---


### 566. [TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning](https://arxiv.org/abs/2607.05380)

**<font color=#1a73e8>作者：</font>** Yury Gorishniy, Akim Kotelnikov, Ivan Rubachev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In deep learning for tabular data, efficient ensembles of multilayer perceptrons (MLPs) have recently emerged as effective and practical architectures. Existing methods of this kind use the same hyperparameters for all underlying MLPs, which requires hyperparameter tuning for achieving the best performance. In this work, we introduce TabPack, an efficient MLP ensemble with strong out-of-the-box performance and reduced reliance on traditional tuning. In a single run, TabPack samples and trains many MLPs with different hyperparameters efficiently in parallel and selects ensemble members on the fly during training. Thus, TabPack only requires specifying ranges from which to sample MLP hyperparameter rather than exact hyperparameter values, which naturally demands less precision for good performance. In experiments on medium-to-large public datasets, TabPack with default settings performs on par with extensively tuned prior methods, thus substantially reducing effort and compute resources needed to achieve competitive results on tabular tasks. Notably, running the default TabPack configuration on a modern MacBook took less time than tuning some baselines on an industry-grade GPU.

---


### 567. [What Does a Discrete Diffusion Model Learn?](https://arxiv.org/abs/2607.05381)

**<font color=#1a73e8>作者：</font>** Rodrigo Casado Noguerales, Bernhard Schölkopf, Thomas Hofmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What does a discrete diffusion model learn: a denoiser, a score ratio, or a bridge plug-in predictor? At the level of jump rates, these are one object in different coordinates, and reading a neural network in the wrong coordinate changes the process being trained and sampled. Starting with a rigorous derivation of the continuous-time Markov chain (CTMC) ELBO for any noising process, boundary terms included, we prove the \emph{Oracle Distance} theorem: the negative ELBO is exactly equal to the data entropy plus the path KL from the oracle reverse process to the learned one, not merely a bound. Its unique optimizer is therefore the conditional expectation of the true reverse jump rate given the current noisy state, and its irreducible cost is the rate at which the forward process $Z_t$ destroys information about the clean data $Z_0$, $-\tfrac{d}{dt}I(Z_0; Z_t)$, so every noising process shares the same best achievable negative ELBO: the data entropy. For sequences with token-factorizing noise, the oracle projection yields three exact coordinates for the optimizer: denoiser, cavity (bridge plug-in), and score, with closed-form conversions among them. This framework identifies which law each loss in the literature actually optimizes, recovering MDM, UDM, SEDD, and GIDD as special cases; explains why denoiser and cavity coincide for masked diffusion but not for uniform diffusion; proves that a denoiser parameterization makes the uniform ELBO diverge at initialization while the bridge plug-in stays finite; and calibrates ELBO implementations exactly at initialization. Every identity is verified numerically, without approximation, on an exactly solvable model.

---


### 568. [InFlux++: Real and Synthetic Data for Estimating Dynamic Camera Intrinsics](https://arxiv.org/abs/2607.05389)

**<font color=#1a73e8>作者：</font>** Erich Liang, Caleb Kha-Uong, Chinmaya Saran 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera intrinsics are vital for recovering 3D structure from 2D video. However, most 3D algorithms assume fixed intrinsics throughout a video, an assumption that often fails for real-world in-the-wild videos. Consequently, estimating per-frame intrinsics from RGB images is critical for making 3D methods robust to videos with dynamic intrinsics. InFlux previously advanced this research direction by establishing the first real-world benchmark with per-frame ground truth intrinsics for dynamic intrinsics videos. Nevertheless, existing methods remain inaccurate due to two obstacles: (i) training data is scarce and lacks intrinsics diversity; and (ii) benchmarks, including InFlux, have limited scene and camera motion diversity, making it difficult to properly evaluate methods. To address both gaps, we present InFlux++, consisting of two components. InFlux++ Synth is a large-scale procedurally generated synthetic video dataset with 441K+ annotated frames from 1841 high-resolution videos, providing accurate per-frame ground truth intrinsics for training dynamic intrinsics prediction models; a subset also includes per-frame pose, depth, and normals. The videos feature rich intrinsics diversity through changes in camera zoom and focus, as well as dynamic objects and realistic rendering effects such as lens distortion and defocus blur. InFlux++ Real is a large-scale real-world benchmark that extends InFlux with 514K+ newly captured frames across 334 high-resolution videos, spanning a wider range of scenes and camera motions. Finetuning existing intrinsics prediction methods on InFlux++ Synth consistently improves focal length estimation across both InFlux++ Real and InFlux, suggesting that synthetic supervision is promising for RGB-based intrinsics prediction. For the dataset, benchmark, code, videos, submission instructions, and live leaderboard, please visit this https URL .

---


### 569. [SynCity 3000: Bootstrapping Scene-Scale 3D Diffusion](https://arxiv.org/abs/2607.05392)

**<font color=#1a73e8>作者：</font>** Paul Engstler, Iro Laina, Christian Rupprecht 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SynCity 3000, a framework for generating 3D scenes that are globally coherent while enabling fine-grained layout control. Building on the ability of current image-to-3D generators to produce complex 3D assets from a single image, we extend this capability to the scale of entire scenes by adapting the generator to be applicable as a convolutional operator. We achieve this by fine-tuning the model on scene-like data generated by a new synthetic data engine, which we propose to address the scarcity of 3D scene data for training. The convolutional generator is then applied to a dimetric image of the entire scene, generated from the user prompt, resulting in 3D scenes of arbitrary size and complexity. Across diverse prompts and layouts, SynCity 3000 produces large, coherent, and detailed scenes, addressing the shortcomings of prior approaches to 3D scene generation.

---


### 570. [Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/abs/2607.05394)

**<font color=#1a73e8>作者：</font>** Shiyuan Feng, Huan-ang Gao, Haohan Chi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL weak teacher is not enough, because the teacher's final policy mixes useful RL gains with the limitations of the smaller model. We propose Direct On-Policy Distillation (Direct-OPD), which transfers the teacher's RL-induced policy shift instead. Direct-OPD compares the post-RL teacher with its own pre-RL reference and treats their log-ratio as a dense implicit reward for the student. In plain terms, the checkpoint pair tells us which actions RL made the weak model more or less likely to take, and Direct-OPD applies that signal on the stronger student's own on-policy states. This directly reuses the weak model's RL supervision signal without training an explicit reward model or running sparse-reward RL on the target model. Empirically, Direct-OPD consistently leverages weaker teachers to improve stronger target models; notably, it boosts Qwen3-1.7B from 48.3% to 62.4% on AIME 2024 in just 4 hours on 8 A100 GPUs. It outperforms step-matched direct RL and enables the sequential composition of multiple policy shifts. Our results show that RL outcomes can be reused across model scales as implicit reward signals, not merely as final models to imitate.

---


### 571. [From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model](https://arxiv.org/abs/2607.05396)

**<font color=#1a73e8>作者：</font>** Wenhao Li, Xueying Jiang, Quanhao Qian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: this https URL.

---


> [!TIP]
> 当前位于：**551-571**（第 12/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-571**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
