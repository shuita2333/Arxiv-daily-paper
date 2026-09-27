# 📦 其他研究 | 2026年09月28日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-266**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-266**

---

### 251. [T-Backdoor: Exploiting Temporal Redundancy in Neuromorphic Data for Spike-preserving Backdoor Attacks on SNNs](https://arxiv.org/abs/2609.30119)

**<font color=#1a73e8>作者：</font>** Abdullah Arafat Miah, Kevin Vu, Yu Bi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks are a serious security threat to deep neural networks (DNNs) and remain largely underexplored for spiking neural networks (SNNs). Existing attacks primarily introduce spatiotemporal triggers that induce deviations in the spike distribution of poisoned samples relative to their clean counterparts. To address this limitation, this work proposes a novel backdoor attack on SNNs, termed \textbf{T-Backdoor}, which operates using purely temporal triggers such as \textit{Rate}, \textit{Latency}, and \textit{Jitter} without introducing any spatial perturbation, making the shift in spike distributions significantly harder to detect. Through extensive experiments on three benchmark neuromorphic datasets: N-MNIST, CIFAR10-DVS, and N-Caltech101, and evaluation against seven baseline backdoor defense methods, we demonstrate that T-Backdoor achieves a near-perfect 100\% attack success rate (ASR) in both single target and multi target settings with only minor degradation in clean accuracy, while remaining robust against existing backdoor detection and mitigation techniques. The codes are available at this https URL .

---


### 252. [EnigmaForge: The Question Is Hidden in the Story](https://arxiv.org/abs/2609.30144)

**<font color=#1a73e8>作者：</font>** Daniel Eisner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most benchmarks hand the model a question. EnigmaForge hands it a stack of old documents and no question at all. Buried in the letters, receipts, and logbook margins is a small logic puzzle whose solution is unique - proved by a SAT solver at generation time, with an ablation certificate showing every clue is load-bearing. Because instances are generated rather than collected, the corpus renews forever. The headline measure is intuition: task success when handed only the story, with world reconstruction as the secondary axis. Twenty-five frontier models ran over 600 instances (17,400 scored records) under three matched conditions. Intuition reshuffles the leaderboard: a 22x spread where fact recovery spans 1.6x, the second-best fact-recoverer ranks fourteenth, one model is indifferent to being told the question, and another is significantly better without it. Several models were blocked by their own content filters before reaching the puzzle - any benchmark scoring refusals as failure is quietly measuring filter behavior.

---


### 253. [Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management](https://arxiv.org/abs/2609.30150)

**<font color=#1a73e8>作者：</font>** Giacomo Arcieri, Gregory Duthé, Christophe Muller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern infrastructure asset management constitutes a complex sequential decision-making problem, characterized by long planning horizons and system-level interactions, such as spatial deterioration correlations and economies of scale. While deep reinforcement learning has shown promise in optimizing maintenance policies, scaling to real-world networks remains challenging. Centralized approaches become computationally intractable in large-scale systems, whereas decentralized approaches often fail to capture essential coordination mechanisms. To address these challenges, we propose a graph-based framework that integrates accurate environment modeling with scalable decision support. First, we employ a hierarchical Bayesian model leveraging a Gaussian Process on Graph kernel to infer a realistic, spatially correlated networked environment of railway maintenance planning from real-world data provided by the Swiss Federal Railways. Second, we introduce a topology-aware Multi-Agent Reinforcement Learning (MARL) framework by integrating graph neural networks and graph Transformers to optimize network-level policies. A central contribution of this work is the demonstration of scalability through zero-shot transfer learning: graph-based agents, trained only on small network portions, are successfully deployed in a zero-shot manner on large-scale unseen networks without any retraining. Numerical results indicate that the proposed method significantly outperforms optimized heuristics and standard MARL baselines, reducing computational training time while maintaining superior performance on large-scale networks.

---


### 254. [A Training Criterion with Token-Level Tolerance to Transcription Ambiguity for Automatic Speech Recognition](https://arxiv.org/abs/2609.30160)

**<font color=#1a73e8>作者：</font>** Saurabh Kumar, Diptiman Mohanta, Prasanta Kumar Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition is typically trained assuming that the reference transcript is the only valid labeling of an utterance, yet even nominally verbatim transcripts contain localized differences in pronunciation, spelling, or lexical realization that the acoustics do not uniquely determine. Omni-temporal Classification (OTC) tolerates such noise by adding wildcard paths to the connectionist temporal classification (CTC) alignment graph, but its word-level arcs are too coarse, since bypassing one unsupported token discards supervision for the whole word. We move wildcard arcs to token granularity so unsupported tokens can be bypassed while the rest of the word stays supervised, and we combine token- and word-level arcs as complementary escape paths. Across 19 languages and three corpora, token-level OTC improves over CTC on all 25 tasks. We also replace epoch-indexed relaxation of the wildcard weights with a predictive-entropy-indexed schedule, which performs comparably while reducing dependence on training length. Combining this schedule with the hybrid graph gives the lowest mean word error rate (WER) on every corpus and a 9.45% average relative WER reduction over CTC. Independent validator transcriptions show that token-level models place significantly more wildcard-bypass probability than CTC on disputed characters, indicating that token-level tolerance targets localized transcript ambiguity.

---


### 255. [Intrinsic-Extrinsic Coupling in Learning Dynamics](https://arxiv.org/abs/2609.30185)

**<font color=#1a73e8>作者：</font>** Qinyou Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learner's current observations need not determine its response to further training. We formulate intrinsic-extrinsic coupling through the continuation-conditioned value of a constrained learning-state intervention, with observation-relative fibers describing present agreement. An executable finite-frame classifier-head write protects current logits while repairing specified historical margins under finite-precision acceptance checks. We distinguish local admissibility, continuation-conditioned intervention value, and complete-policy performance. A matched four-cell contrast identifies readout-specific non-additivity between the same intrinsic intervention and alternative external continuations. In a CLINC-derived class-incremental setting, replay changes the write's 32-update contribution from five correct predictions to zero. Nonzero interactions also occur under output distillation, with a RoBERTa backbone, and under optimizer-native SGDW dynamics. Under SGDW, correct-count interactions are negative in all three activated roots at 128 updates, showing that coupling need not imply positive synergy. The mathematical analysis distinguishes feasible local repairs and favorable terminal outputs from training-reachable repair regions. Separate coordination tests show that content controls match or exceed the development gain, while a five-root fresh-test comparison with Fiber present in every arm shows root-dependent rather than uniformly beneficial correct-count effects. On the secondary cross-entropy readout, guided allocation yields lower mean loss than standard replay in all five pairs. Together, these results make intrinsic-extrinsic coupling operational by connecting executable state geometry to continuation-conditioned value, matched interaction identification, and closed-loop coordination, while separating identified coupling from complete-policy performance.

---


### 256. [Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures](https://arxiv.org/abs/2609.30187)

**<font color=#1a73e8>作者：</font>** Abhiram Maddukuri, Georgios Pavlakos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ego-Exo4D is a large-scale dataset providing synchronized egocentric and multi-view exocentric video, a rich resource for skill learning and assessment, procedural activity understanding, and embodied AI. However, the dataset ships with only sparse 3D human pose annotations, and reconstructing dense human motion from its multi-view captures is nontrivial. To this end, we present Ego-Exo4D-HM, a large-scale dataset of 4D human motion reconstructions for Ego-Exo4D's captures, and release the accompanying reconstruction pipeline. The code, dataset, and documentation can be found at this https URL.

---


### 257. [Beyond Compression: Training Latent Representations for Stable Long-Horizon Rollout in Neural Surrogate Solvers](https://arxiv.org/abs/2609.30198)

**<font color=#1a73e8>作者：</font>** Andreas E. Robertson, Ashley T. Lenau, John D. Shimanek 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent neural surrogate solvers, or latent dynamics models, accelerate simulations of time-dependent physical systems by evolving a compressed latent space rather than resolving full-resolution fields directly. In principle this reduces computational cost and simplifies learning, but in practice errors often accumulate rapidly during long autoregressive rollouts, limiting predictive utility. We show that this instability does not stem from the latent representation itself, but arises when it is trained solely for reconstruction, producing representations poorly suited to long-horizon forecasting. We systematically evaluate training-level interventions that align latent representations with long-horizon rollout: Koopman operator learning and Hamming noise injection during autoencoder training to improve compression, together with noise injection and multi-step rollout fine-tuning to improve dynamics. Interventions that improve long-horizon rollout stability often degrade conventional training metrics, including reconstruction and one-step prediction accuracy. Collectively, these interventions reduce long-rollout error by approximately 40\% and match or exceed the accuracy of full-resolution models on two physics benchmarks, while requiring 2 orders of magnitude fewer floating point operations and half the GPU memory. Applied to mesoscale crystal-plasticity simulations of high-cycle fatigue, the resulting surrogate achieves stable extrapolation over horizons orders of magnitude beyond those observed during training. More broadly, these results show that neural compression should be designed not merely to reduce dimensionality, but to restructure the solution space for stable dynamical evolution, a key requirement for reliable, efficient neural surrogates in scientific applications.

---


### 258. [ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds](https://arxiv.org/abs/2609.30199)

**<font color=#1a73e8>作者：</font>** Ming Zhang, Zhenghao Xiang, Peizhong Gao 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery begins where known problems end. There, AI systems must engage in exploration: framing hypotheses, designing experiments, and iterating on the results. However, evaluating this ability is difficult: (1) how to verify whether a genuinely new hypothesis holds, and (2) how to determine whether a system has discovered it through exploration or merely recalled related knowledge from pre-training data. To this end, we introduce ExplorationBench, which turns the wicked problem of evaluating scientific exploration into a concrete and tractable framework built on verifiable Alien Worlds: their rules are executable, so every answer can be checked exactly, and they conflict with familiar knowledge, so recall alone cannot solve the tasks. The benchmark contains two sandboxes, AlienCode (31 discovery targets, 70 tasks) and AlienLogic (24 discovery targets, 70 tasks). Each sandbox provides a flawed manual, task-specific environmental feedback, and a dedicated tool-call schema. Systems use these resources to explore the sandbox, then solve held-out tasks. We evaluate 10 AI systems and find that the strongest systems can acquire and apply unfamiliar rules, while performance varies substantially across trajectories and continued exploration can stall or reverse earlier gains. ExplorationBench represents a step towards AI systems that can acquire and apply genuinely new knowledge through exploration in unknown environments.

---


### 259. [TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations](https://arxiv.org/abs/2609.30222)

**<font color=#1a73e8>作者：</font>** Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing point tracking models face a fundamental tradeoff: they can either track a sparse set of query points over long horizons, or track all points across only short clips. We introduce TrackEverything, a 3D point tracker that breaks this trade-off by representing videos as persistent 3D scene tracks in world coordinates. Grounded in the insight that videos are 2D projections of an underlying 3D world, TrackEverything decouples model complexity from video duration, allowing it to scale with unique physical scene geometry instead. Our approach introduces three key innovations. First, we employ a voxelization-based de-duplication mechanism at sliding-window boundaries to merge co-located tracks, preventing repeated observations of the same surface from redundantly accumulating. Second, we decompose tracking into an endpoint refiner that predicts each point's destination and static-versus-dynamic classification, followed by a lightweight trajectory refiner that decodes dense trajectories exclusively for dynamic points. Third, we propose 3D WAFT, replacing memory-prohibitive 4D correlation volumes with efficient feature sampling in the scene cloud. To the best of our knowledge, TrackEverything is the first 3D tracker capable of tracking all visible points across videos exceeding 1000 frames within 40 GB of GPU memory. On TAPVid-3D, TrackEverything outperforms all open-source all-frame dense 3D trackers by more than 20% APD on short clips, while remaining competitive with state-of-the-art sparse trackers on long sequences, despite tracking far more points.

---


### 260. [BiCC: Bidirectional Connected-Component Loss for Instance-Aware Segmentation](https://arxiv.org/abs/2609.30223)

**<font color=#1a73e8>作者：</font>** Luc Bouteille, Frederic Jonske, Jens Kleesiek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Common segmentation losses aggregate errors voxel-wise, so lesions influence the objective in proportion to their volume, giving small but clinically critical lesions disproportionately little weight. Instance-aware losses aim to address this mismatch by assigning each lesion its own term. However, blob loss and CC-DiceCE derive their regions solely from annotations, so false-positive components receive no instance-level term. This matters in computer-assisted review, where each false-positive component may require separate inspection, making precision and false-positive burden important alongside recall. We introduce the bidirectional connected-component loss (BiCC), which pairs annotation- and prediction-derived partitions to score predicted components on their own scale. By deriving instances from the predictions, this branch directly penalizes false-positive components regardless of their size. The balance parameter $\alpha$ allows control over the lesion-wise precision-recall trade-off. Across five datasets with five-fold cross-validation using nnU-Net, BiCC outperforms CC-DiceCE in lesion-wise F1 on four datasets and blob loss on all five. It significantly improves over DiceCE on three datasets and matches it on two; CC-DiceCE instead loses up to 0.363 precision by favoring recall. Code is available at this https URL.

---


### 261. [PoEM: Predicting RL Outcomes from Existing Policies](https://arxiv.org/abs/2609.30226)

**<font color=#1a73e8>作者：</font>** Kimia Hamidieh, Giannis Daras, Antonio Torralba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we want to combine multiple rewards. We hence ask: given a new reward function, is it possible to predict the RL outcomes without actually running RL on it? We answer this in the affirmative by introducing PoEM, a framework to predict the outputs of RL on a new reward function using a set of models already post-trained on other rewards. First, we show that if the new reward function can be written as a linear combination of existing ones, then the new policy in log-space can be written as a linear combination of the existing log-policies. Surprisingly, even in cases where the rewards are not linearly connected, we observe that often log-policies from RL training span an approximately low-rank subspace across rewards. To our benefit, the weighting coefficients for this combination can be estimated using only the reward or basis policy outputs on the samples. We turn these observations into an algorithm that takes post-trained models and a new reward function, and approximates the target RL policy without actually running any additional RL training. We experimentally validate our approach across synthetic and real rewards, spanning both text and image modalities.

---


### 262. [JevOut: Natural Context Can Flip Decision Models](https://arxiv.org/abs/2609.30243)

**<font color=#1a73e8>作者：</font>** Zixiang Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dedicated decision models such as Jev map unstructured language to probability distributions over finite choices, allowing their outputs to directly route requests, select tools, and trigger actions. Yet real-world inputs rarely arrive in isolation: they come with background details and surrounding context. We find that short additions that fit naturally into this context can nevertheless redirect an otherwise correct decision, even when the correct answer remains unchanged. To study this behavior, we fix a wrong target option for each initially correct item and use the model's option probabilities to refine fluent context additions while preserving the source, question, choices, and gold answer. Within 64 accepted target evaluations, the optimizer identifies contexts that redirect Jev on 312 of 508 initially correct decisions (61.4%); in 229 cases, Jev assigns at least 0.7 probability to the fixed wrong option. Across seven datasets, three additional decision systems show targeted flip rates of 64.9%-73.2% on decisions they initially answer correctly. Taken together, these results expose a pronounced fragility in current decision models: short, ordinary-looking context can shift a correct choice to a high-confidence wrong one. Because these models turn language directly into downstream choices, this sensitivity raises concerns about treating their probability outputs as reliable decision interfaces.

---


### 263. [Towards Practical Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2609.30245)

**<font color=#1a73e8>作者：</font>** Pengpeng Yu, Yueru Chen, Fei Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D representations, increasing the complexity of training and coding. Meanwhile, floating-point context inference can introduce numerical inconsistencies across platforms, causing entropy-decoding failures. To address these practical challenges, we propose COSA-GS, which constructs context without spatial aggregation through anchor-wise causal factorization. Specifically, we use geometry context derived from each anchor's coordinates to model a compact learnable anchor latent. The anchor latent is then fused with the geometry context to form an anchor context for attribute coding. The resulting context model features a simple architecture composed solely of linear transformations and activations. We train COSA-GS using rate--distortion optimization with adaptive Gaussian pruning. Further, we develop quantization-aware training and integer inference for the context model to achieve bit-exact consistency of entropy-decoded symbols across platforms. Experiments demonstrate that COSA-GS achieves state-of-the-art compression performance while retaining fast and consistent cross-platform decoding, providing a simple yet effective framework for practical 3DGS compression. Code is available at this https URL.

---


### 264. [Agentic Detection of Online Conspiracies](https://arxiv.org/abs/2609.30250)

**<font color=#1a73e8>作者：</font>** Lior Biton, Oren Tsur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conspiratorial discourse on social media is not always expressed through explicit claims or stable lexical markers. The same surface content may express endorsement, legitimate concerns, criticism, satire, or mockery. The main challenge is therefore not only recognizing conspiracy-related claims, but inferring the speaker's intent -- the utterance's illocutionary force. We argue that this can be achieved through the use of relevant social contexts and propose an agentic framework, equipped with a set of tools supporting social queries.
We demonstrate the benefits of our approach on a unique dataset of Hebrew tweets, covering 80\%--90\% of the public Hebrew tweets published over a four-year span (late 2018-- early 2023), encompassing several election cycles as well as the COVID pandemic years and related vaccination campaigns. This extensive coverage can be used in recovering different social contexts. Evaluating our framework on a manually-annotated adversarial dataset, we find that context-aware workflows consistently outperform text-only classification and that the agentic framework performs significantly better than other frameworks and settings, including a non-agentic model exposed to the same contexts available to the agent. We further provide an analysis of the results, the errors and efficiency (token economy) tradeoffs.
These findings support viewing the task of conspiracy detection as a socially embedded interpretation task, in which effective classification depends not only on access to contexts, but also on adaptive reasoning in which the agent uses tools on a per-case basis, asking only for evidence relevant to its current reasoning step.

---


### 265. [Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning](https://arxiv.org/abs/2609.30258)

**<font color=#1a73e8>作者：</font>** Sudip Bhujel, Shanghao Shi, Ruiquan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed learning in embodied reinforcement-learning agents offers a degree of privacy by retaining raw sensor data on-device and transmitting only policy gradients to the server. Yet temporal structure can amplify this leakage beyond single-frame attacks. We introduce Temporal Reconstruction Attack on Consecutive Encodings (TRACE), an amortized temporal gradient-inversion attack that autoregressively reconstructs the sequence of private observation-action trajectories from per-step policy-learning gradients. The attack exploits two structural signals ignored by prior single-frame methods: (i) cross-time correlation between successive embodied gradients, which we formalize via a conditional mutual-information bound, and (ii) closed-form action recovery from policy-head gradient structure, which we prove exact when standard entropy regularization is sufficiently small. On held-out embodied scenes, TRACE reaches $18.8$ dB PSNR with near-perfect action recovery at $3$-$4.5$ ms per reconstructed frame, dominating the learning-based baseline across all reconstruction metrics and exceeding optimization attacks while running orders of magnitude faster. Further evaluation demonstrates TRACE's broader applicability across recurrent, residual, and compact transformer victim architectures, multi-modal inputs, and larger discrete action spaces. Defense experiments suggest that protecting temporal gradient streams may require sequence-aware privacy mechanisms.

---


### 266. [AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control](https://arxiv.org/abs/2609.30264)

**<font color=#1a73e8>作者：</font>** Jiabin Qiu, Zixuan Chen, Hongye Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state. A model can therefore achieve low factual prediction error yet poorly distinguish candidate actions. We introduce AD-WM, an action-discriminative joint-embedding world model for counterfactual MPC. AD-WM combines residual latent dynamics with predictor-level action-recovery regularization, using inverse dynamics and a normalized recovery objective motivated by conditional mutual information. Both objectives encourage planning transitions to preserve action information; their auxiliary heads are discarded at test time, leaving MPC unchanged. On OGBench-Cube, AD-WM improves hard-start success from 3.7% to 52.0% over a matched LeWM baseline and improves mean success over the reproduced baseline in four of five simulation environments. Planning diagnostics show that factual prediction error and whole-bank action ranking do not follow the closed-loop success ordering, whereas CEM-aligned elite regret tracks success more closely. With a frozen V-JEPA 2 encoder and matched DROID post-training, AD-WM also improves zero-shot transfer to our Franka setup, increasing basic pick-and-place success from 42.2% to 71.1% without lab-specific adaptation. These results suggest that world models for planning should preserve action-dependent differences needed for counterfactual selection, rather than optimize factual prediction accuracy alone. More videos and code are available at this https URL.

---


> [!TIP]
> 当前位于：**251-266**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-266**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
